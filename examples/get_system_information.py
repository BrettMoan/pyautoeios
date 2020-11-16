"""Simple script to extract system info, to include in the README.md.

This information allows to confirm where tests are working/broken.
"""

import platform as p
from typing import List

def print_as_markdown_table(array: List[str]) -> None:
    print("| {} |" .format(" | ".join(array)))

SYSTEM_INFO = [
    p.python_implementation(),
    p.python_version(),
    str(p.python_build()),
    p.python_compiler(),
    p.platform(),
    p.processor(),
]

HEADERS = [
    "python_build",
    "processor",
    "python_compiler",
    "python_version",
    "python_implementation",
    "platform",
]

print("")
print_as_markdown_table(HEADERS)
print_as_markdown_table(len(HEADERS) * ["---"])
print_as_markdown_table(SYSTEM_INFO)
print("")
