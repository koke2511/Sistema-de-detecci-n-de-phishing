import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from features import extract_features


def main():
    df = pd.read_csv("data/urls.csv")

    feature_rows = df["url"].apply(extract_features)
    X = pd.DataFrame(feature_rows.tolist())
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("=== Classification Report ===")
    print(classification_report(y_test, y_pred))

    joblib.dump(model, "models/phishing_model.pkl")
    print("\nModelo guardado en models/phishing_model.pkl")


if __name__ == "__main__":
    main()
