import argparse
import os
import subprocess as sub
import sys

# cwd to script's location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

PYTHON_PATH = "/usr/bin/python"
PIP_PATH = "/usr/local/bin/pip"

def invoke(cmd_raw):
    cmd = sub.Popen(cmd_raw)
    cmd.communicate()
    if cmd.returncode:
        sys.exit(1)

def main_tests(**kwargs):
    invoke([
        PYTHON_PATH,
        "-m", "unittest",
        "discover",
        "--start-directory=tests",
    ])

def main_build(**kwargs):
    invoke([
        PYTHON_PATH,
        "setup.py",
        "bdist_egg",
    ])
    invoke([
        PYTHON_PATH,
        "setup.py",
        "test",
    ])

def main_demo(spreadsheet, oauth_client_id, secret_file, **kwargs):
    invoke([
        PIP_PATH,
        "install",
        "-e",
        ".",
    ])
    invoke([
        "gsheets-assistant-demo",
        "--spreadsheet", spreadsheet,
        "--secret-file", secret_file,
        "--oauth-client-id", oauth_client_id
    ])

def main_compare(spreadsheet, oauth_client_id, secret_file, **kwargs):
    invoke([
        PYTHON_PATH,
        "gsheets_assistant/__demo__.py",
        "--spreadsheet", spreadsheet,
        "--secret-file", secret_file,
        "--oauth-client-id", oauth_client_id
    ])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='Action must be...')

    # Tests
    parser_tests = subparsers.add_parser('tests', help='tests help')
    parser_tests.set_defaults(func=main_tests)

    # Build
    parser_build = subparsers.add_parser('build', help='build help')
    parser_build.set_defaults(func=main_build)

    # Demo
    parser_demo = subparsers.add_parser('demo', help='demo help')
    parser_demo.add_argument('--spreadsheet', type=str, help='Spreadsheet ID', required=True)
    parser_demo.add_argument('--oauth-client-id', type=str, help='Name of oauth client ID', required=True)
    parser_demo.add_argument('--secret-file', type=str, help='Path to secret file', required=True)
    parser_demo.set_defaults(func=main_demo)

    # Compare
    parser_compare = subparsers.add_parser('compare', help='compare help')
    parser_compare.add_argument('--spreadsheet', type=str, help='Spreadsheet ID', required=True)
    parser_compare.add_argument('--oauth-client-id', type=str, help='Name of oauth client ID', required=True)
    parser_compare.add_argument('--secret-file', type=str, help='Path to secret file', required=True)
    parser_compare.set_defaults(func=main_compare)

    args = parser.parse_args()
    args.func(**vars(args))

