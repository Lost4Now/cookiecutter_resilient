cookiecutter-pypackage-minimal
==============================

An opinionated, minimal [cookiecutter](https://github.com/audreyr/cookiecutter) template for Python packages, and some guidelines for Python packaging.

Usage
-----

    pip install cookiecutter
    git clone https://github.com/Lost4Now/cookiecutter_resilient.git
    cookiecutter cookiecutter_resilient/

You should then change the classifiers in `{{ package_name }}/setup.py` - it is assumed that the project will run on the latest versions of Python 2 and 3, so you should remove any classifiers that do not apply. The full list of PyPI classifiers can be found [here](https://pypi.python.org/pypi?:action=list_classifiers).

Fill out the README, and - if necessary - add a license to the project.

Explanation
-----------


