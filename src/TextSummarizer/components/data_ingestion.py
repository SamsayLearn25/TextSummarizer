import os, sys
from urllib import request
import zipfile

from src.TextSummarizer.logging import logger

from src.TextSummarizer.config.configuration import ConfigurationManager

class DataIngestion:

    def __init__(self, config: ConfigurationManager):

        self.config = config

    def download_file(self):

        if not os.path.exists(self.config.locate_data_file):

            filename, header = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.locate_data_file
            )
            logger.info(f"File is Downloaded")
        else:
            logger.info(f"File already exist")

    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.locate_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)

