import xgboost as xgb
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt



def train_xgboost_model(dtrain, dtest, y_test, num_boost_round=200):
    """
    Train and evaluate an XGBoost model for employee attrition prediction.

    Parameters:
    -----------
    dtrain : xgb.DMatrix
        Training data in XGBoost format.
    dtest : xgb.DMatrix
        Test data in XGBoost format.
    y_test : pd.Series or np.array
        True labels for the test set.
    num_boost_round : int
        Number of boosting rounds (default=200).

    Returns:
    --------
    model : xgb.Booster
        Trained XGBoost model.
    y_pred : np.array
        Binary predictions (0/1) for test set.
    y_pred_prob : np.array
        Predicted probabilities for test set.
    """

    # Define parameters
    params = {
        'objective': 'binary:logistic',
        'eval_metric': 'auc',
        'max_depth': 5,
        'learning_rate': 0.1,
        'scale_pos_weight': 3,  # adjust for class imbalance
        'random_state': 42
    }

    # Train the model
    model = xgb.train(
        params,
        dtrain,
        num_boost_round=num_boost_round,
        evals=[(dtrain, "Train"), (dtest, "Test")],
        early_stopping_rounds=20
    )

    # Predictions
    y_pred_prob = model.predict(dtest)
    y_pred = (y_pred_prob > 0.5).astype(int)

    # Evaluation
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("ROC-AUC:", roc_auc_score(y_test, y_pred_prob))

    # Feature Importance


    return model, y_pred, y_pred_prob
