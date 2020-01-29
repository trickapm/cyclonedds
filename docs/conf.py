#!/usr/bin/env python3
# This is a 'fake' Sphinx conf.py tailored to be used within the readthedocs build environment
# It invokes cmake to generate the actual conf.py and builds the docs target

import sys
import subprocess
import os

from pprint import pprint

def invoke_cmake():
    # Raises exception when a process returns a non-zero exit code
    print("Invoking cmake...")
    cmd = "mkdir ../build; cd ../build; cmake -DBUILD_DOCS=ON .."
    cp = subprocess.run(cmd, shell=True, check=True, timeout=10)

    print("Building docs target...")
    cmd = "cmake --build ../build --target docs"
    cp = subprocess.run(cmd, shell=True, check=True, timeout=10)

is_rtd_build = os.environ.get("READTHEDOCS", None) is not None

if not is_rtd_build:
    print("Fatal: This script must be run in a readthedocs build environment", file=sys.stderr)
    exit(1)

# Check if conf.py exists, run cmake if not
if not os.path.isfile("../build/docs/conf.py"):
    invoke_cmake()

sys.path.append("../build/docs/manual/docs.cache")
from conf import *

#import importlib.util
#spec = importlib.util.spec_from_file_location("conf", "../build/docs/manual/docs.cache/conf.py")
#foo = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(foo)


print("EXTENSIONS: ")
print(extensions)
print(breathe_projects)


