import os

TEMP_FOLDER = os.path.expanduser("~/Desktop/Nobody_temp/")


def ensure_temp_folder() -> str:
    os.makedirs(TEMP_FOLDER, exist_ok=True)
    return TEMP_FOLDER