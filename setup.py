import setuptools

setuptools.setup(
    name = "cmdbin",
    version = "0.02",
    author = "Luke Schwager",
    description = "Command line interface to cmdbin",
    long_description="""
    usage: cmdbin [-h] [--input INPUT] [--passthrough] [--slugonly] [--endpoint ENDPOINT]

command line interface to cmdbin and it's api

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        name of the file to upload, or "-" for stdin. defaults to stdin
  --passthrough, -p     passthrough lines from stdin to stdout. defaults to no.
  --slugonly, -s        only return the slug, not the full link. defaults to no.
  --endpoint ENDPOINT, -e ENDPOINT
                        specify a specific cmdbin endpoint. defaults to https://cmdbin.cc.""",
    packages = ["cmdbin"],
    license = "BSD-3 Clause"
    install_requires = ["requests"],
    entry_points = {
        "console_scripts": [
            "cmdbin=cmdbin.cmdbin:main"
        ]
    }
)