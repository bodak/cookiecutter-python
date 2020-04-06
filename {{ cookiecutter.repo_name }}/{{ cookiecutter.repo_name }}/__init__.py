import logging

__version__ = '{{ cookiecutter.version }}'
__release__ = __version__

DEBUG = False

{% raw %}LOG_FMT = '%(levelname)s: %(name)s [%(process)d] {%(filename)s@L%(lineno)d}: %(message)s'{% endraw %}
LOG_LVL = logging.INFO
