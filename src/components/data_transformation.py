from sklearn.impute import SimpleImputer  # Handling missing values
from sklearn.preprocessing import StandardScaler  # Feature scaling
from sklearn.preprocessing import OrdinalEncoder  # Ordinal encoding
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import sys
import os
import pandas as pd
import numpy as np
from dataclasses import dataclass
import pickle

from src.exception import CustomException
from src.logger import logging


## Data Transformation config
@dataclass
class DataTransformationConfig:
    preprocessor_ob_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')


## Data Transformation class
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        """
        This function returns a ColumnTransformer object with pipelines for numerical and categorical columns.
        """
        try:
            logging.info("Data Transformation: Creating preprocessing object")

            # Define which columns are numerical and categorical
            numerical_columns = ['carat', 'depth', 'table', 'x', 'y', 'z']
            categorical_columns = ['cut', 'color', 'clarity']

            # Ordinal categories for categorical features
            cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
            # Numerical pipeline
            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            # Categorical pipeline
            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("ordinal_encoder", OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),
                ("scaler", StandardScaler())
            ])

            # Combine pipelines
            preprocessor = ColumnTransformer(transformers=[
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_data_path, test_data_path):
        """
        This function reads the data, applies transformations, and saves the preprocessor object.
        """
        try:
            logging.info("Reading train and test data as DataFrame")

            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformation_object()

            target_column_name = "price"
            drop_columns = ["id", target_column_name]

            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training and testing datasets")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # Combine transformed features with target
            train_arr = np.c_[input_feature_train_arr, target_feature_train_df.to_numpy()]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_df.to_numpy()]

            # Save preprocessor object
            os.makedirs(os.path.dirname(self.data_transformation_config.preprocessor_ob_file_path), exist_ok=True)
            with open(self.data_transformation_config.preprocessor_ob_file_path, "wb") as f:
                pickle.dump(preprocessing_obj, f)

            logging.info("Preprocessing object saved successfully.")

            return train_arr, test_arr, self.data_transformation_config.preprocessor_ob_file_path

        except Exception as e:
            raise CustomException(e, sys)
