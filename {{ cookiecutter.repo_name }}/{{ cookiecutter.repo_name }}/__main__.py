import {{ cookiecutter.repo_name }} as root

def main() -> None:
    logging.basicConfig(format=root.LOG_FMT, level=root.LOG_LVL)
    log = logging.getLogger(__name__)

    root.DEBUG = root.CONFIG['main']['debug']

    if root.DEBUG:
        log.info('Debug mode is ON')

if __name__ == '__main__':
    main()
