import google.generativeai as genai

API_KEY = "..."  # API key Gemini
genai.configure(api_key=API_KEY)

def generate_advanced_description(row_data):
    try:
        prompt = f"Genera una descripción detallada para los siguientes datos: {row_data}."
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([prompt])
        return response['choices'][0]['text'].strip() if response.get('choices') else "Descripción no disponible"
    except Exception as e:
        print(f"Error generating description: {e}")
        return "Descripción no disponible"
