import importlib.resources

f = importlib.resources.files(__package__)
print(f / "lib")
