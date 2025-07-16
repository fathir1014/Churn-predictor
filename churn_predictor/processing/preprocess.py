import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def load_and_preprocess(filepath):
    # 1. Baca file
    df = pd.read_excel(filepath)
    print("Data loaded:", df.shape)

    # 2. Cek missing value
    if df.isnull().sum().any():
        print("Warning: Ada missing values!")
        df = df.dropna()

    # 3. Encode kolom kategorikal
    df['Gender'] = LabelEncoder().fit_transform(df['Gender'])  # Male=1, Female=0
    df['Geography'] = LabelEncoder().fit_transform(df['Geography'])  # France=0, Germany=1, Spain=2

    # 4. Pisahkan fitur dan target
    X = df.drop(['CustomerID', 'Churn'], axis=1)
    y = df['Churn']

    # 5. Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("Train shape:", X_train.shape)
    print("Test shape:", X_test.shape)

    return X_train, X_test, y_train, y_test
