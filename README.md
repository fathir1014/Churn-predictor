# 🔍 Customer Churn Prediction

Proyek ini membangun sistem prediksi churn pelanggan menggunakan machine learning. Data berasal dari file Excel, kemudian diproses, dianalisis, dan digunakan untuk melatih model klasifikasi.

---

## 📁 Struktur Proyek

churn_predictor/
├── data/ 
├── processing/
│ └── loader.py
├── training/
│ └── trainer.py
├── evaluation/
│ └── evaluator.py
├── utils/
│ └── logger.py
│ └── visualizer.py
├── main.py 
└── README.md 

---

## 🛠️ Tools & Library

- Python
- Pandas, NumPy
- Scikit-learn (LabelEncoder, train_test_split, DecisionTreeClassifier, classification_report)
- Matplotlib & seaborn (untuk visualisasi evaluasi)
- Modular & OOP design pattern

---

## 🔄 Alur Program

1. **Data dibaca dari file Excel**
2. **Data diproses dan dibersihkan**
   - Drop kolom yang tidak relevan (`CustomerID`)
   - Handle missing values
   - Label Encoding untuk data kategorikal
3. **Data dibagi jadi training & testing set**
   - Menggunakan `train_test_split` dengan `stratify=y`
4. **Model Decision Tree dilatih**
5. **Evaluasi menggunakan:**
   - Confusion Matrix
   - Classification Report
   - Akurasi, Precision, Recall, F1 Score
6. **Hasil ditampilkan secara interaktif via CLI**

---

## 📊 Contoh Hasil Evaluasi

       0       0.52      0.55      0.54       507
       1       0.51      0.48      0.49       493

accuracy                           0.52      1000
macro avg 0.52 0.52 0.52 1000
weighted avg 0.52 0.52 0.52 1000


> Akurasi awal masih baseline (~52%) — bisa ditingkatkan dengan tuning, feature engineering, atau model lain.

---

## 🤖 Tujuan Proyek

- Menunjukkan pemahaman pipeline machine learning end-to-end
- Menggunakan pendekatan modular dan clean code
- Menyiapkan sistem real-world untuk prediksi churn

---

## 🙋 Tentang Developer

Proyek ini dibuat sebagai bagian dari portofolio pembelajaran machine learning.  
Penulis memahami alur logika, preprocessing, pemodelan, dan evaluasi model secara menyeluruh — meskipun sebagian kode dibangun dengan referensi sambil belajar.

---

## ✅ Status: SIAP PAKAI & DIPERLUAS
- Sudah bisa langsung dijalankan (`main.py`)
- Siap dikembangkan: tuning model, validasi silang, UI, atau deployment

