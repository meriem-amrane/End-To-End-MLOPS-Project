from ML_Project.constants import *

from ML_Project.utils.common import read_yaml, create_directories

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) 
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
