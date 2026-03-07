import sys
from site import getsitepackages
from pathlib import Path

from vars import paths


def main(argv=sys.argv):
    filename = argv[1]
    sitepackages = Path(getsitepackages()[0])

    SITE_FILE_PATH = sitepackages / filename

    print(SITE_FILE_PATH)

    with open(SITE_FILE_PATH, "w") as file:
        for path in paths.values():
            file.write(str(path) + "\n")


if __name__ == "__main__":
    main()
