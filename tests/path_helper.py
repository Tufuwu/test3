import sys
import os.path

"""Make the cabrillo module importable from the tests' point of view."""

project_root_dir = os.path.dirname(os.path.dirname(__file__))

if not project_root_dir in sys.path:
    sys.path.append(project_root_dir)
