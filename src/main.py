import pandas as pd
from gemini_integration import generate_advanced_description
from model_training import train_model

def preprocess_data(input_file, output_file):
    df = pd.read_excel(input_file)
    
    
    df['Saving accounts'] = df['Saving accounts'].fillna('unknown').str.lower()
    df['Checking account'] = df['Checking account'].fillna('unknown').str.lower()
    
    
    df['advanced_description'] = df.apply(
        lambda row: generate_advanced_description(row.to_dict()), axis=1
    )
    
    
    def calculate_risk(row):
        risk_score = 0
        if row['Age'] < 25: risk_score += 2
        if row['Credit amount'] > 10000: risk_score += 3
        if row['Duration'] > 24: risk_score += 1
        if row['Saving accounts'] == 'unknown': risk_score += 1
        if row['Checking account'] == 'unknown': risk_score += 1
        return risk_score

    df['risk_score'] = df.apply(calculate_risk, axis=1)
    
    
    df.to_excel(output_file, index=False)
    print(f"Processed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_data('data/credit_risk_reto.xlsx', 'data/credit_risk_enhanced_with_gemini.xlsx')
    train_model('data/credit_risk_enhanced_with_gemini.xlsx')
