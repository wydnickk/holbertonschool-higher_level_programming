#!/usr/bin/python3
"""This module contains the function text_indentation(text)."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buf = ""
    for ch in text:
        buf += ch
        if ch in ".?:":
            print(buf.strip(), end="")
            print("\n")
            buf = ""

    if buf:
        print(buf.strip(), end="")
