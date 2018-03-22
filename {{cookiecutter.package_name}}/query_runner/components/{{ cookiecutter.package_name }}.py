"""Action Module circuits component to update incidents from McAfee searches"""
from pkg_resources import Requirement, resource_filename
import logging
from datetime import datetime
import time
import copy
import json
from string import Template
import resilient_circuits.template_functions as template_functions
from query_runner.lib.query_action import QueryRunner
from query_runner.lib.misc import SearchTimeout, SearchFailure

try:
    basestring
except NameError:
    basestring = str

LOG = logging.getLogger(__name__)
CONFIG_DATA_SECTION = "{{ cookiecutter.config_section }}"


def config_section_data():
    """sample config data for use in app.config"""
    section_config_fn = resource_filename(Requirement("{{ cookiecutter.package_name }}"), "query_runner/data/app.config.{{ cookiecutter.package_name }}")
    query_dir = resource_filename(Requirement("{{ cookiecutter.package_name }}"), "query_runner/data/queries_data.json")

    with open(section_config_fn, 'r') as section_config_file:
        section_config = Template(section_config_file.read())
        return section_config.safe_substitute(directory=query_dir)

class {{ cookiecutter.class_name }}(QueryRunner):
    """ Acknowledges and fires off new query requests """

    def __init__(self, opts):
        query_options = opts.get(CONFIG_DATA_SECTION, {})
        super({{ cookiecutter.class_name }}, self).__init__(opts, query_options, run_search,
                                                 wait_for_complete=True)



#############################
# Functions for running Query
#############################
def run_search(options, query_definition, event_message):
    """ Run McAfee search and return result """
    import json

    LOG.info('No job to run, please tell me what to do.')

    entries = {"entries": []}

    return entries
# end run_search
