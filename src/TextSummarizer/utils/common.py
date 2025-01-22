import os
import sys
import logging

import yaml

from ensure import ensure_annotations
from box.exceptions import BoxValueError
from box import ConfigBox

from pathlib import Path
from typing import Any

from src.TextSummarizer.logging import logger


@ensure_annotations
def read_yaml(file_path: Path)->ConfigBox:

    try:
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")

            