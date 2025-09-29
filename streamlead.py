pip install sklearn
pip install pandas as pd
pip install os
pip install sqlite3

import pandas as pd, os, sqlite3
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 1. load data (from CSV or SQLite) ---
# Option a: CSV
df = pd.read_csv("reports/Week_5/data/processed/books_clean.csv")

# option B: SQLite
# conn = sqlite3.connect("data/books.db")
# df = pd.read_sql("SELECT * FROM books;", conn)
# conn.close()

print(f"📥 Loaded {len(df)} rows for classification")

# 2. train/test split ---
X_train, X_test, y_train, y_test = train_test_split(
    df["title"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
)

# 3. vectorize text ---
# you can try Bag-of-Words or TF-IDF
vec = TfidfVectorizer()
X_train_vec = vec.fit_transform(X_train)
X_test_vec = vec.transform(X_test)

# 4. train model 
clf = LogisticRegression(max_iter=1000)
# clf = MultinomialNB()   # Try Naive Bayes too
clf.fit(X_train_vec, y_train)

# --- 5. evaluate ---
y_pred = clf.predict(X_test_vec)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.3f}")

print("Classification Report:")
print(classification_report(y_test, y_pred))

# --- 6. save metrics ---
os.makedirs("reports/Week_5/logs", exist_ok=True)
pd.DataFrame([{"accuracy": acc}]).to_csv("reports/Week_5/logs/metrics.csv", index=False)
print("Metrics saved to reports/Week_5/logs/metrics.csv")
