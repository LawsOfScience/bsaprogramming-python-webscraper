from . import log, package_install as pkg
try:
    import yaml
except ModuleNotFoundError:
    log.error("Module \"YAML\" not found. Attempting install.")
    pkg.install("pyyaml")

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def getConfig():
    with open('config.yml', 'r') as file:
        config = file.read()
        file.close()
    return config
