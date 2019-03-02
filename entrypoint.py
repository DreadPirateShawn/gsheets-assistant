import argparse
import os
import subprocess as sub
import sys

# cwd to script's location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# parse args
parser = argparse.ArgumentParser()
parser.add_argument('--spreadsheet', type=str, help='Spreadsheet ID', required=False) # actually required but only if certain options
parser.add_argument('--oauth-client-id', type=str, help='Name of oauth client ID', required=False) # actually required but only if certain options
parser.add_argument('--secret-file', type=str, help='Path to secret file', required=False) # actually required but only if certain options
decider = parser.add_mutually_exclusive_group(required=True)
decider.add_argument('--build', action='store_const', const=True, default=False)
decider.add_argument('--test', action='store_const', const=True, default=False)
decider.add_argument('--test-package', action='store_const', const=True, default=False)
decider.add_argument('--demo', action='store_const', const=True, default=False)
decider.add_argument('--compare', action='store_const', const=True, default=False)
args = parser.parse_args()

python_path = "/usr/bin/python"
pip_path = "/usr/local/bin/pip"

def invoke(cmd_raw):
    cmd = sub.Popen(cmd_raw)
    cmd.communicate()
    if cmd.returncode:
        sys.exit(1)

if args.build:
    python_args = [
        python_path,
        "setup.py",
        "bdist_egg",
    ]
    invoke(python_args)

elif args.test:
    python_args = [
        python_path,
        "-m", "unittest",
        "discover",
        "--start-directory=tests",
    ]
    invoke(python_args)

elif args.test_package:
    python_args = [
        python_path,
        "setup.py",
        "test",
    ]
    invoke(python_args)

elif args.demo:
    if not args.spreadsheet:
        parser.error("--demo requires --spreadsheet.")
    if not args.secret_file:
        parser.error("--demo requires --secret-file.")

    python_args = [
        pip_path,
        "install",
        "-e",
        ".",
    ]
    invoke(python_args)
    invoke(["gsheets-assistant-demo", "--spreadsheet", args.spreadsheet, "--secret-file", args.secret_file, "--oauth-client-id", args.oauth_client_id])

elif args.compare:
    if not args.spreadsheet:
        parser.error("--compare requires --spreadsheet.")
    if not args.secret_file:
        parser.error("--compare requires --secret-file.")

    python_args = [
        python_path,
        "gsheets_assistant/__demo__.py",
        "--spreadsheet", args.spreadsheet, "--secret-file", args.secret_file, "--oauth-client-id", args.oauth_client_id
    ]
    invoke(python_args)
