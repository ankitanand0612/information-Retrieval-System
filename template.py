import os
import pathlib
from pathlib import Path as path
import shutil
import logging
import json



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "project_name"  # Replace with your project name
list_of_files = [

    "src/__init__.py",
    "src/helper.py",
    "config/config.yaml",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "reseach/train.ipynb",
]

for filepath in list_of_files:
    filepath = path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")





