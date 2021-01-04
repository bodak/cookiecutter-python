import re

from pathlib import Path
from textwrap import dedent
from typing import List

from setuptools import (
    find_packages,
    setup,
)

import {{ cookiecutter.repo_name }} as root


def read_requirements(file: str) -> List[str]:
    if not Path(file).is_file():
        raise FileNotFoundError(file)
    with open(file) as fd:
        unparsed_requirements = fd.read()
        return re.findall(r"[\w-]+==[\d.]+", unparsed_requirements)

setup_params = dict(
    name='{{ cookiecutter.name | lower | replace('_', '-') }}',
    version=root.__version__,
    description='{{ cookiecutter.brief }}',
    long_description=dedent("""
        {{ cookiecutter.description | replace('\n', '\n        ') }}
        """).strip(),
    long_description_content_type='text/markdown',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    url='{{ cookiecutter.url }}',
    classifiers=["Programming Language :: Python :: 3"],
    license='{{ cookiecutter.license }}',
    keywords=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.repo_name }} = {{ cookiecutter.repo_name }}.__main__:main',
        ]
    },
    install_requires=read_requirements('requirements.txt'),
    extras_require={},
    setup_requires=[
{%- if cookiecutter.enable_sphinx == 'true' %}
        'sphinx',
{%- endif %}
        'wheel',
    ],
    tests_require=read_requirements('requirements-test.txt')
)


def main() -> None:
    setup(**setup_params)


if __name__ == '__main__':
    main()
