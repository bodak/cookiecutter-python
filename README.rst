=======================
cookiecutter-python
=======================

``cookiecutter https://github.com/bodak/cookiecutter-python``

Use
    - ``make init`` to init repo and commit blank state
    - ``make requirements`` to update requirements (uses nox if no docker found)
    - ``make install`` creates virtualenv if one does not exists. installs requirements, project to virtualenv
    - ``make run`` runs python library (__main__.py)
    - ``make black`` black formatter (nox)
    - ``make lint`` flake8 linting (nox)
    - ``make safety`` safety review (nox)
    - ``make type`` mypy (nox)
    - ``make tests`` tests inside nox environment
    - ``make docker-build`` builds docker image containing project
    - ``make docker-run`` runs docker image containing project
    - ``make changelog`` updates CHANGELOG.md using commit message in `conventional style`_
    

parts based on
    -  https://github.com/alexkey/cookiecutter-lux-python
    -  https://github.com/cjolowicz/hypermodern-python
    -  https://github.com/othneildrew/Best-README-Template

.. _conventional style: https://www.conventionalcommits.org/en
