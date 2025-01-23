from src.TextSummarizer.logging import logger
from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.components.data_ingestion import DataIngestion

logger.info("Logging is Implemented")

config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(data_ingestion_config)
data_ingestion.download_file()
data_ingestion.extract_zip_file()