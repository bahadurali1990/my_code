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

from Preprocessor import preprocess_employee_data

file_path = "//Users//ahad//Employee_attr_dataset//Employee_datasets.csv"

dtrain, dtest, X_train, X_test, y_train, y_test = preprocess_employee_data(file_path)

print(X_train.head())






