from processing.preprocess import load_and_preprocess
from model.trainer import train_and_evaluate
from evaluation.evaluator import evaluate_model
from utils.logger import log
from utils.visualizer import plot_confusion_matrix

def main():
    log("📥 Memulai pemrosesan data...")
    X_train, X_test, y_train, y_test = load_and_preprocess("churn_predictor/data/churn_data.xlsx")

    model = None
    y_pred = None

    while True:
        print("\n===== MENU UTAMA =====")
        print("1. Latih model")
        print("2. Evaluasi model")
        print("3. Visualisasi confusion matrix")
        print("4. Keluar")

        choice = input("Pilih opsi (1-4): ")

        if choice == "1":
            model = train_and_evaluate(X_train, y_train, X_test, y_test)
            y_pred = model.predict(X_test)
            log("✅ Model selesai dilatih.")

        elif choice == "2":
            if y_pred is None:
                print("⚠️ Latih model dulu sebelum evaluasi.")
            else:
                evaluate_model(y_test, y_pred)

        elif choice == "3":
            if y_pred is None:
                print("⚠️ Latih model dulu sebelum visualisasi.")
            else:
                plot_confusion_matrix(y_test, y_pred)

        elif choice == "4":
            print("🚪 Keluar dari program.")
            break

        else:
            print("❌ Opsi tidak valid. Pilih antara 1-4.")

if __name__ == "__main__":
    main()
