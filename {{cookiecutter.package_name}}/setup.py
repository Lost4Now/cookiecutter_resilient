import setuptools
import os.path
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

def read_version_number():
    path = os.path.join(os.path.dirname(__file__), "{{ cookiecutter.module_name }}", "version.txt")
    with open(path) as f:
        ver = f.read()
    return ver.strip()

version = read_version_number()
major, minor, _ = version.split('.', 2)

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

setup(
    name="{{ cookiecutter.package_name }}",
    version=version,
    url="{{ cookiecutter.package_url }}",
    license='MIT',
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    install_requires=[
        'resilient_circuits>={}.{}'.format(major, minor)
    ],
    tests_require=["pytest",
                   "pytest_resilient_circuits"],
    cmdclass = {"test" : PyTest},

    description="{{ cookiecutter.package_description }}",
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
    ],

    entry_points={
        # Register the component with resilient_circuits
        "resilient.circuits.components": ["{{ cookiecutter.class_name }}={{ cookiecutter.module_name }}.components.{{ cookiecutter.module_name }}:{{ cookiecutter.class_name }}"],
        "resilient.circuits.configsection": ["{{ cookiecutter.class_name }}_config={{ cookiecutter.module_name }}.components.{{ cookiecutter.module_name }}:config_section_data"]
    }
)
