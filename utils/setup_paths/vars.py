from pathlib import Path

SETUP_PATHS_DIR = Path(__file__).parent
ROOT_DIR = SETUP_PATHS_DIR.parents[1]

SRC_PATH = ROOT_DIR / "src"
paths = {
    "src": SRC_PATH,
    "core": SRC_PATH / "core",
}
