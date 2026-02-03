import pandas as pd
import matplotlib.pyplot as plt


def plot_feature_importance(model, importance_type='gain'):
    """
    Plot feature importance vertically using original feature names.

    Parameters:
    -----------
    model : xgb.Booster
        Trained XGBoost model.
    importance_type : str
        Type of importance ('weight', 'gain', 'cover').
    """
    # Extract importance scores
    importance = model.get_score(importance_type=importance_type)

    # Convert to DataFrame
    importance_df = pd.DataFrame({
        'Feature': list(importance.keys()),
        'Importance': list(importance.values())
    }).sort_values(by='Importance', ascending=False)

    # Vertical bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(importance_df['Feature'], importance_df['Importance'], color='skyblue')
    plt.xticks(rotation=90)  # rotate labels for readability
    plt.ylabel(f"Importance ({importance_type})")
    plt.title("Feature Importance (Vertical)")
    plt.tight_layout()
    plt.show()

    return importance_df
