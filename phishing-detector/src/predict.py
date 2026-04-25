import joblib
import pandas as pd

from features import extract_features


def main():
    model = joblib.load("models/phishing_model.pkl")

    url = input("Introduce una URL para analizar: ").strip()

    features = extract_features(url)
    X_new = pd.DataFrame([features])

    prediction = model.predict(X_new)[0]
    probability = model.predict_proba(X_new)[0]

    print("\n=== Resultado del análisis ===")
    print(f"URL: {url}")
    print(f"Predicción: {'Phishing' if prediction == 1 else 'Legítima'}")
    print(f"Probabilidad clase legítima: {probability[0]:.4f}")
    print(f"Probabilidad clase phishing: {probability[1]:.4f}")

    print("\nCaracterísticas detectadas:")
    for key, value in features.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
