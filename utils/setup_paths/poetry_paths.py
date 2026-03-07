import subprocess
import sys
from shutil import which

from .vars import SETUP_PATHS_DIR


def setup(argv=sys.argv):
    filename = "fd_custom_paths.pth"
    if len(argv) > 1:
        filename = argv[1]

    if sys.platform == "win32":
        EXECUTABLE = which("powershell")
    else:
        EXECUTABLE = which("bash")

    PY_FILE_NAME = "subprocess_setup_paths.py"
    PY_FILE_PATH = SETUP_PATHS_DIR / PY_FILE_NAME

    command = f"poetry run python {PY_FILE_PATH} {filename}"

    result = subprocess.run(
        args=[command],
        check=True,
        shell=True,
        executable=EXECUTABLE,
    )


if __name__ == "__main__":
    setup()
