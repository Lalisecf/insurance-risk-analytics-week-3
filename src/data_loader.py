import pandas as pd


def load_data(path):
    return pd.read_csv(path, sep='|')


def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing numerical values
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

    for col in numerical_cols:
        df[col] = df[col].fillna(df[col].median())

    return df


if __name__ == "__main__":
    df = load_data("data/MachineLearningRating_v3.txt")

    cleaned_df = clean_data(df)

    cleaned_df.to_csv("data/insurance_data_cleaned.csv", index=False)

    print("Cleaned dataset saved.")
    
