import os
import sys
from exception import CustomException
from logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from data_transformation import DataTransformation
from data_transformation import DataTransformtionConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact', "train.csv")
    test_data_path: str = os.path.join('artifact', "test.csv")
    raw_data_path: str = os.path.join('artifact', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion component")
        try:
            df = pd.read_csv("Notebook\stud.csv")
            logging.info('Exported or read the dataset as DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False,header=True)

            logging.info('Train test split initated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)

            logging.info('Data Ingestion completed.')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transforamtion(train_data,test_data)

