from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def train_and_evaluate(X_train, y_train, X_test, y_test):
    # 1. Buat model
    model = DecisionTreeClassifier(random_state=42)

    # 2. Latih model
    model.fit(X_train, y_train)

    # 3. Prediksi data test
    y_pred = model.predict(X_test)

    # 4. Hitung akurasi
    acc = accuracy_score(y_test, y_pred)
    print(f"📊 Akurasi model: {acc:.4f}")

    return model
