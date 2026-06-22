import os
import urllib.request as request
import zipfile as zip
from ML_Project import logger
from ML_Project.utils.common import get_size
from ML_Project.entity.config_entity import DataIngestionConfig
from ML_Project.config.configuration import ConfigurationManager
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logger.info(f"File {filename} has been downloaded with the following info: {headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zip.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Zip file has been extracted to {unzip_path}")

