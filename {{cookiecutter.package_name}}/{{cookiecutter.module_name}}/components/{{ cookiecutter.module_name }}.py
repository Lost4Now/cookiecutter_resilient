"""Action Module circuits component to update incidents from McAfee searches"""
from pkg_resources import Requirement, resource_filename
import logging
from datetime import datetime
import time
import copy
import json
from string import Template
from circuits import Component, Debugger
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage

try:
    basestring
except NameError:
    basestring = str

LOG = logging.getLogger(__name__)
CONFIG_DATA_SECTION = "{{ cookiecutter.config_section }}"


def config_section_data():
    """sample config data for use in app.config"""
    section_config_fn = resource_filename(Requirement("{{ cookiecutter.package_name }}"), "{{ cookiecutter.module_name }}/data/app.config.{{ cookiecutter.package_name }}")
    query_dir = resource_filename(Requirement("{{ cookiecutter.package_name }}"), "{{ cookiecutter.module_name }}/data/queries_data.json")

    with open(section_config_fn, 'r') as section_config_file:
        section_config = Template(section_config_file.read())
        return section_config.safe_substitute(directory=query_dir)

class {{ cookiecutter.class_name }}(ResilientComponent):
    """ Acknowledges and fires off new query requests """

    def __init__(self, opts):
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        super({{ cookiecutter.class_name }}, self).__init__(opts)

        # The queue name can be specified in the config file, or default to 'filelookup'
        self.channel = "actions." + self.options.get("queue", "{{ cookiecutter.queue }}")

    @handler("reload")
    def reload_options(self, event, opts):
        """Configuration options have changed, save new values"""
        LOG.info("Storing updated values from section [%s]", CONFIG_DATA_SECTION)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("{{cookiecutter.resilient_rule_name}}")
    def _lookup_action(self, event, *args, **kwargs):
        """The @handler() annotation without an event name makes this
           a default handler - for all events on this component's queue.
           This will be called with some "internal" events from Circuits,
           so you must declare the method with the generic parameters
           (event, *args, **kwargs), and ignore any messages that are not
           from the Action Module.
        """
        incident = event.message["incident"]
        artifact = event.message["artifact"]
        inc_id = incident["id"]
        art_id = artifact['id']

        artifact['description'] = "From script"



        yield "{{cookiecutter.resilient_rule_name}} finished with %s" % inc_id
