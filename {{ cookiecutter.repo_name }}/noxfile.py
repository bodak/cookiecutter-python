import nox
from nox.sessions import Session

nox.options.sessions = "lint", "mypy", "tests"
locations = "{{ cookiecutter.repo_name }}", "noxfile.py", "doc/conf.py"


@nox.session(python=["{{ cookiecutter.python_version }}"])
def requirements(session: Session) -> None:
    args = session.posargs or ["-o", "requirements.txt", "requirements.in"]
    session.install("pip-tools")
    session.run("pip-compile", *args)


@nox.session(python=["{{ cookiecutter.python_version }}"])
def black(session: Session) -> None:
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["{{ cookiecutter.python_version }}"])
def lint(session: Session) -> None:
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python=["{{ cookiecutter.python_version }}"])
def types(session: Session) -> None:
    args = session.posargs or locations
    session.install("mypy")
    session.run("mypy", *args)


@nox.session(python=["{{ cookiecutter.python_version }}"])
def safety(session: Session) -> None:
    session.install("safety")
    session.run("safety", "check", "--file=requirements.txt", "--full-report")


@nox.session(python=["{{ cookiecutter.python_version }}"])
def tests(session: Session) -> None:
    args = session.posargs or ["{{ cookiecutter.repo_name }}", "--cov"]
    session.install("pytest", "pytest-cov")
    session.run("pip", "install", "-r", "requirements.txt")
    session.run("pytest", *args)


@nox.session(python=["{{ cookiecutter.python_version }}"])
def changelog(session: Session) -> None:
    args = session.posargs or ["--unreleased"]
    session.install("auto-changelog")
    session.run("auto-changelog", *args)


@nox.session(python=["{{ cookiecutter.python_version }}"])
def publish(session: Session) -> None:
    args = session.posargs or ["-r","testpypi"]
    args += ["dist/*"]
    session.install("twine", "wheel", "setuptools")
    session.run("rm", "-rf", "dist", "build", external=True)
    session.run("python", "setup.py", "--quiet", "sdist", "bdist_wheel")
    session.run("twine", "check", "--strict", "dist/*")
    session.run("twine","upload", *args)
