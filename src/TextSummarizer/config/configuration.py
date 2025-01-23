import os, sys
from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    locate_data_file: Path
    unzip_dir: Path


import os, sys
from pathlib import Path

from src.TextSummarizer.config.configuration import DataIngestionConfig
from src.TextSummarizer.constants import *  # All Project Config
from src.TextSummarizer.utils.common import read_yaml, create_directories


class ConfigurationManager:

    def __init__(self,
                 config_path = CONFIG_FILE_PATH,
                 params_path = PARAMS_FILE_PATH
                 ):
        
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        # get data ingestion config
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(config.root_dir,
                                                    config.source_URL,
                                                    config.locate_data_file,
                                                    config.unzip_dir
                                                    )
        
        return data_ingestion_config