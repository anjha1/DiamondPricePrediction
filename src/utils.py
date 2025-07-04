import os
import sys
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging


def save_object(file_path, obj):
    """
    Save any Python object using pickle.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

        logging.info(f"Object saved to {file_path}")

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Load a pickled object from file.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models: dict):
    """
    Evaluate multiple ML models and return a dictionary of R2 scores.
    """
    try:
        report = {}

        for name, model in models.items():
            model.fit(X_train, y_train)

            y_pred_test = model.predict(X_test)
            test_r2 = r2_score(y_test, y_pred_test)

            report[name] = test_r2
            logging.info(f"{name} - R2 Score: {test_r2}")

        return report

    except Exception as e:
        raise CustomException(e, sys)
