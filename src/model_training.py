import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def train_model(input_file):
    df = pd.read_excel(input_file)
    df['risk_label'] = df['risk_score'].apply(lambda x: 'bad risk' if x >= 3 else 'good risk')
    
    X = df[['Age', 'Credit amount', 'Duration']]
    y = df['risk_label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    
    joblib.dump(model, 'optimized_risk_classifier_model.pkl')
    print("Model saved as 'optimized_risk_classifier_model.pkl'.")

if __name__ == "__main__":
    train_model('data/credit_risk_enhanced_with_gemini.xlsx')
