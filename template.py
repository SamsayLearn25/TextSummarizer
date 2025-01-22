import os
from pathlib import Path

import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:' )

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", # all components
    f"src/{project_name}/pipeline/__init__.py", # pipeline code for each stage
    f"src/{project_name}/constants/__init__.py", # constants global to project
    f"src/{project_name}/utils/__init__.py", # utils for each components
    f"src/{project_name}/entity/__init__.py", # all entity for corresponding components
    f"src/{project_name}/logging/__init__.py", # logging to be used
    f"src/{project_name}/config/__init__.py",
    
    f"src/{project_name}/utils/common.py", # all common utils
    f"src/{project_name}/config/configuration.py", # configuration to be used for all components, pipelines, entity

    "config/config.yaml", # configuration for project
    "params.yaml", # parameters to be used
    "app.py", # for flask
    "main.py", # to check code on terminal
    "Dockerfile", # to create docker
    "requirements.txt",
    "setup.py",
    "research/research.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating Empty File: {filepath}")
    else:
        logging.info(f"{filename} is already exist")