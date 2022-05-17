__version__ = 0.02

import argparse
import sys

import requests


new = "/v1/new"
slugonly = "/v1/new-slugonly"
endpoint = "https://delta.lab.blucobalt.dev"

buffer = []


def cmdbin_run():
    parser = argparse.ArgumentParser()
    parser.description = "command line interface to cmdbin and it's api"
    parser.add_argument("--input", "-i", help="name of the file to upload, or \"-\" for stdin. defaults to stdin",
                        default="-", type=argparse.FileType("r"))
    parser.add_argument("--passthrough", "-p", help="passthrough lines from stdin to stdout. defaults to no.",
                        action="store_true")
    parser.add_argument("--slugonly", "-s", help="only return the slug, not the full link. defaults to no.",
                        action="store_true")
    parser.add_argument("--endpoint", "-e", help="specify a specific cmdbin endpoint. defaults to https://cmdbin.cc.",
                        default=endpoint)
    args = parser.parse_args()

    try:
        for line in args.input:
            buffer.append(line)
            if args.passthrough:
                sys.stdout.write(line)
    except KeyboardInterrupt as e:
        sys.exit(0)
        pass
    args.input.close()

    response = requests.post(args.endpoint + new if not args.slugonly else args.endpoint + slugonly,
                             headers={"Content-Type": "text/plain"},
                             data="".join(buffer).encode("utf-8"))
    print(response.text)
