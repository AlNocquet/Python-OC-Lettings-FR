# Day 01 - Initial audit and environment setup

**Date:** 2026-08-20

## Objectives

- Run and inspect the original Django application.
- Validate the existing public pages and Django administration.
- Inspect the initial database, migrations, tests, and linting configuration.
- Establish a reproducible local development environment before refactoring.

## Initial state

The original application runs correctly locally.

Validated features:

- Home page
- Lettings list
- Letting detail
- Profiles list
- Profile detail
- Django administration

Initial database content:

- 6 addresses
- 6 lettings
- 4 profiles

All existing Django migrations are applied.

The project currently contains a single business application, `oc_lettings_site`, containing the Address, Letting, and Profile models.

## Environment

The development environment was stabilized using:

- Python 3.10.11
- Django 3.0
- Flake8 3.7.0
- pytest-django 3.9.0
- six 1.17.0

The virtual environment is named `venv` so that it is excluded by the existing Flake8 configuration.

## Issues identified

### Flake8

Running Flake8 initially failed because an older `.venv` directory was scanned by Flake8. The bundled Pyflakes version could not process syntax found inside installed dependencies.

After using the `venv` directory expected by the existing configuration and removing the obsolete `.venv`, Flake8 ran correctly.

The initial project contains 18 linting errors. These are kept as part of the baseline and will be corrected during the code-quality stage.

### pytest-django dependency

A clean installation from the original `requirements.txt` caused pytest to fail because the `six` package was missing.

Installing `six==1.17.0` restored the test suite, so the dependency was added explicitly to `requirements.txt` to make the environment reproducible.

## Validation

Current checks:

- `python manage.py check` -> no issues
- `pytest` -> 1 test passed
- `flake8` -> runs successfully and reports the existing project linting issues

The existing test is only the original dummy test and does not yet validate application behavior.

## Next steps

- Preserve the initial data during the refactoring.
- Separate the monolithic application into `lettings` and `profiles`.
- Use Django migrations without direct SQL.
- Keep the site's appearance and functionality unchanged.
