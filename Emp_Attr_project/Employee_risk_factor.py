# 1- Risk factor who will resign in future from our workforce.
# 2- What are the main factors behind attrition So HR department can take actions.
# 3- Attrition Risk Segmentation
# 4- Department-Level Insights
# 5- Tenure vs. Attrition
# 6- Salary Bands and Attrition
# 7- Retention Strategy Simulation
# 8- Explainability for HR

"""

In short: we can present feature importance, risk segmentation, department-level trends,
tenure/salary effects, predictive metrics, and simulations.
These findings turn the pipeline from a black-box predictor into a decision-support tool for HR

"""
import matplotlib.pyplot as plt
import pandas as pd
from xgboost import plot_importance
from Training_model import train_xgboost_model
from Preprocessor import preprocess_employee_data
from Feature_function import plot_feature_importance

file_path = "//Users//ahad//Employee_attr_dataset//Employee_datasets.csv"
print("We are here")

#data = pd.read_csv(file_path)

dtrain, dtest, X_train, X_test, y_train, y_test = preprocess_employee_data(file_path)

print("We are here--------------------")
print(type(X_train))

model, y_pred, y_pred_prob = train_xgboost_model(dtrain, dtest, y_test, num_boost_round=200)

Leaving_Prod_train = model.predict(dtrain)
Leaving_Prod_test = model.predict(dtest)

X_train['Leaving_Prod'] = Leaving_Prod_train
X_test['Leaving_Prod']  = Leaving_Prod_test

Final_Output = pd.concat([X_train, X_test], axis=0)

imprt_df = plot_feature_importance(model)

print(Final_Output.head(10).to_string())


