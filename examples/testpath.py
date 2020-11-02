try:
    from importlib.resources import files

    _LIB_DIR = files(__package__) / "lib"
except ImportError:
    import pkg_resources
    from pathlib import Path

    _LIB_DIR = Path(pkg_resources.resource_filename(__package__, "lib"))


print(f"{_LIB_DIR = }")
