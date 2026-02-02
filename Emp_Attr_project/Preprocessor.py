import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def preprocess_employee_data(file_path, test_size=0.2, random_state=42):
    """
    Preprocess employee attrition dataset for XGBoost training.

    Parameters:
    -----------
    file_path : str
        Path to the CSV dataset.
    test_size : float
        Fraction of data to use for testing (default=0.2).
    random_state : int
        Random seed for reproducibility.

    Returns:
    --------
    dtrain : xgb.DMatrix
        Training data in XGBoost format.
    dtest : xgb.DMatrix
        Test data in XGBoost format.
    X_train, X_test, y_train, y_test : pd.DataFrame, pd.Series
        Preprocessed train/test splits for evaluation.
    """

    # 1. Load dataset
    df = pd.read_csv(file_path)

    # 2. Encode target variable
    df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

    # 3. Separate features and target
    X = df.drop(['Attrition', 'EmployeeID'], axis=1)
    y = df['Attrition']

    # 4. Encode categorical features
    categorical_cols = X.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))

    # 5. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    # 6. Convert to DMatrix
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)

    print("Preprocessing complete. Ready for XGBoost training!")

    return dtrain, dtest, X_train, X_test, y_train, y_test
