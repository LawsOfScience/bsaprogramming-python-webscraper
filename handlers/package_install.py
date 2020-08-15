import sys
import subprocess
from . import log

def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except:
        log.error("Failed to install package \"" + package +\
             "\". Please attempt manual install with \"pip\".")
        sys.exit(1)