import setuptools
import os.path
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytestargs=', 'a', "Resilient Environment Arguments")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytestargs = []
        self.test_suite = True

    def finalize_options(self):
        import shlex
        TestCommand.finalize_options(self)
        self.test_args = ["-s",] + shlex.split(self.pytestargs)

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


queries = [u"query_runner/data/queries/" + filename for filename in os.listdir("query_runner/data/queries")]

setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    namespace_packages=['query_runner', 'query_runner.components','query_runner.lib'],

    setup_requires=[''],

    version="{{ cookiecutter.package_version }}",
    url="{{ cookiecutter.package_url }}",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_description }}",
    long_description=open('README.rst').read(),

    packages=find_packages(),

    install_requires=[
        'resilient_circuits>=29.0.0',
        'rc-query-runner',
    ],
    tests_require=["pytest",
                   "pytest_resilient_circuits"],
    cmdclass={"test": PyTest},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
    ],
    data_files = [("query_runner", ["query_runner/LICENSE"]),
                  ("query_runner/data", ["query_runner/data/app.config.{{ cookiecutter.package_name }}",]),
                  ("query_runner/data/queries", queries)],
    entry_points={
        # Register the components with resilient_circuits
        "resilient.circuits.components": ["{{ cookiecutter.class_name }}=query_runner.components.{{ cookiecutter.package_name }}:{{ cookiecutter.class_name }}"],
        "resilient.circuits.configsection": ["{{ cookiecutter.class_name }}_config = query_runner.components.{{ cookiecutter.package_name }}:config_section_data"]
    }

)
