from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(y_true, y_pred):
    print("📊 Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    
    print("\n📋 Classification Report:")
    print(classification_report(y_true, y_pred))
