import re
import sys
import inspect

from tabulate import tabulate

from api.server import router


def row(route):
    return [route.path, inspect.getmodule(route.endpoint).__name__, route.endpoint.__qualname__]


if __name__ == "__main__":
    pattern = "^/"
    if sys.argv[1:]:
        pattern = sys.argv[1]
    rows = [row(route) for route in router.routes if re.match(pattern, route.path)]
    table = tabulate(rows, headers=["Route", "Module", "Function"])
    print(table)
