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
decider = parser.add_mutually_exclusive_group(required=True)
decider.add_argument('--build', action='store_const', const=True, default=False)
decider.add_argument('--test', action='store_const', const=True, default=False)
decider.add_argument('--test-package', action='store_const', const=True, default=False)
decider.add_argument('--demo', action='store_const', const=True, default=False)
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

    python_args = [
        pip_path,
        "install",
        "-e",
        ".",
    ]
    invoke(python_args)
    invoke(["gsheets-assistant-demo", "--spreadsheet", args.spreadsheet])
