import os
import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer  

if __name__ == '__main__':
    try:
        # Step 1: Data Ingestion
        ingestion = DataIngestion()
        train_data_path, test_data_path = ingestion.initiate_data_ingestion()

        logging.info(f"Train data saved to: {train_data_path}")
        logging.info(f"Test data saved to: {test_data_path}")

        # Step 2: Data Transformation
        transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )

        logging.info(f"Preprocessor object saved at: {preprocessor_path}")

        # Step 3: Model Training
        trainer = ModelTrainer()
        best_model_name, best_score = trainer.initiate_model_trainer(train_arr, test_arr)

        logging.info(f"Best Model: {best_model_name}")
        logging.info(f"R2 Score: {best_score}")


    except Exception as e:
        raise CustomException(e, sys)
