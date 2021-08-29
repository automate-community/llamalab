"""

Simple test to deploy a http test server.
Functions used:
    simple_server() -> Deploys an http web server

Issues: https://github.com/SerTor-Automate/llamalab/issues

"""

from src.llamalab.fast_http import simple_server

simple_server(port=80)
