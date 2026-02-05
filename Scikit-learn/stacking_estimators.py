import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.utils import shuffle

def load_ames_housing():

    df = fetch_openml(name="house_prices",as_frame=True)
    X = df.data
    y = df.target

    features = [
        "YrSold",
        "HeatingQC",
        "Street",
        "YearRemodAdd",
        "Heating",
        "MasVnrType",
        "BsmtUnfSF",
        "Foundation",
        "MasVnrArea",
        "MSSubClass",
        "ExterQual",
        "Condition2",
        "GarageCars",
        "GarageType",
        "OverallQual",
        "TotalBsmtSF",
        "BsmtFinSF1",
        "HouseStyle",
        "MiscFeature",
        "MoSold",
    ]

    X = X.loc[:,features]
    X ,y = shuffle(X,y,random_state=42)

    return  X ,np.log(y)

X ,y = load_ames_housing()


from sklearn.compose import make_column_selector

cat_selector = make_column_selector(dtype_include=[object, "string"])
num_selector = make_column_selector(dtype_include=np.number)

cat_column = cat_selector(X)
num_column = num_selector(X)

print(cat_column)
print(num_column)


from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder

cat_tree_processor =  OrdinalEncoder(handle_unknown="use_encoded_value",unknown_value=-1,encoded_missing_value=-2,)
num_tree_precessor =  SimpleImputer(strategy="mean",add_indicator=True)

column_preprocessor = make_column_transformer((cat_column,cat_tree_processor),(num_column,num_tree_precessor))

print(column_preprocessor)






