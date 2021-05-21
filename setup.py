try:
    from setuptools import find_packages, setup
except ImportError:
    raise ImportError(
        "'setuptools' is required but not installed. To install it, "
        "follow the instructions at "
        "https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py"
    )
install_req = ["click"]

setup(
    name="starlette-shutdown-example",
    version="1.0",
    author="Abhi",
    author_email="abhi@gmail.com",
    packages=find_packages(),
    install_requires=install_req,  # will be installed with this application
    entry_points={
        "console_scripts": [
            "starlette-ex = server.cli:cli",
        ],
    },
)
