"""
* MTG Vectors
* Data Gathering and Test Commands
"""

import click

from src.commands.build import build_cli
from src.commands.test import test_cli

"""
* App CLI
"""


@click.group(
    commands={"build": build_cli, "test": test_cli},
    help="Invoke the CLI without a command to launch an ongoing headless Proxyshop application.",
)
def AppCLI():
    pass


# Export CLI
__all__ = ["AppCLI"]
