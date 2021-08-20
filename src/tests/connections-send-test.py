"""

Simple test to use Cloud Module.
Functions used:
    .send() -> sends a payload

Issues: https://github.com/SerTor-Automate/llamalab/issues

"""
from src.llamalab.connections import Cloud

with Cloud.send("secret", "test@gmail.com", "payload_message") as response: print(response.text)
