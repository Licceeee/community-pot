"""
Module: error handling

This module contains the error handling functions.
"""

from datetime import datetime

filename = "log"


def write_in_log(a, e):
    """Write the error in a log file."""
    with open(filename, "a+") as f:
        f.write(f"\n{datetime.now()}: {e} \n {a}\n\n")
