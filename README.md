# Credit Risk Analysis with Gemini API

Este proyecto implementa un análisis de datos de riesgo crediticio utilizando la API de **Gemini** para generar descripciones avanzadas, junto con un modelo de aprendizaje automático para predecir el riesgo crediticio basado en diversas características de los datos.

## Estructura del Proyecto

```
credit_risk_analysis/
├── data/
│   └── credit_risk_reto.xlsx
├── models/
│   ├── optimized_risk_classifier_model.pkl
│   ├── optimized_tfidf_vectorizer.pkl
├── src/
│   ├── main.py
│   ├── gemini_integration.py
│   ├── model_training.py
├── requirements.txt
├── README.md
```

---

## Resultados Clave

### 1. Lectura de Datos
![Logo del Proyecto](https://github.com/Jhack20/credit_risk_analysis/blob/main/descarga.png)
![Logo del Proyecto](https://github.com/Jhack20/credit_risk_analysis/blob/main/descarga%20(2).png)
![Logo del Proyecto](https://github.com/Jhack20/credit_risk_analysis/blob/main/descarga%20(5).png)

### 2. Estructura de Respuesta de Gemini
La API de Gemini genera descripciones detalladas basadas en los datos ingresados. Ejemplo de la estructura de respuesta:

```
Estructura de respuesta: response:
GenerateContentResponse(
    done=True,
    result={
        "candidates": [
            {
                "content": {
                    "parts": [
                        {
                            "text": "Estos datos representan un perfil crediticio de un individuo. Se trata de un hombre de 30 años que posee su vivienda y solicita un crédito de 3959 unidades monetarias con una duración de 36 meses (3 años)..."
                        }
                    ],
                    "role": "model"
                },
                "finish_reason": "STOP"
            }
        ]
    }
)
```

### 3. Ejemplo de Descripciones Generadas
Las descripciones avanzadas generadas por Gemini se almacenan en una columna adicional `advanced_description` del conjunto de datos:

| advanced_description | risk_score |
|-----------------------|------------|
| Este conjunto de datos describe a un hombre de... | 1 |
| Esta entrada de datos describe a una mujer de... | 3 |
| Estos datos representan un perfil de crédito d... | 1 |
| Este conjunto de datos describe a un hombre de... | 1 |
| Esta entrada de datos describe a un hombre de... | 0 |

![Logo del Proyecto](https://github.com/Jhack20/credit_risk_analysis/blob/main/descarga%20(4).png)

### 4. Estadísticas del Conjunto de Datos

#### Información General

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 11 columns):
 #   Column                Non-Null Count  Dtype 
---  ------                --------------  ----- 
 0   Age                   1000 non-null   int64 
 1   Sex                   1000 non-null   object
 2   Job                   1000 non-null   int64 
 3   Housing               1000 non-null   object
 4   Saving accounts       1000 non-null   object
 5   Checking account      1000 non-null   object
 6   Credit amount         1000 non-null   int64 
 7   Duration              1000 non-null   int64 
 8   Purpose               1000 non-null   object
 9   advanced_description  1000 non-null   object
 10  risk_score            1000 non-null   int64 
```

#### Estadísticas Descriptivas

| Column              | Mean    | Std     | Min | Max |
|---------------------|---------|---------|-----|-----|
| Age                 | 35.55   | 11.37   | 19  | 75  |
| Credit amount       | 3271.26 | 2822.74 | 250 | 18424 |
| Duration            | 20.90   | 12.05   | 4   | 72  |
| risk_score          | 1.22    | 1.21    | 0   | 7   |

### 5. Distribuciones

- **Distribución de Edad:**

| Age | Frecuencia |
|-----|------------|
| 27  | 51         |
| 26  | 50         |
| 23  | 48         |
| ... | ...        |

- **Distribución de `risk_score`:**

| risk_score | Frecuencia |
|------------|------------|
| 1          | 367        |
| 0          | 310        |
| 2          | 189        |
| ...        | ...        |

![Logo del Proyecto](https://github.com/Jhack20/credit_risk_analysis/blob/main/descarga%20(1).png)

### 6. Modelo de Clasificación

Se entrenó un modelo de bosque aleatorio con hiperparámetros optimizados:

#### Mejores Hiperparámetros
```
{'class_weight': 'balanced', 'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 200}
```

#### Resultados del Modelo

- **Reporte de Clasificación:**
```
              precision    recall  f1-score   support

    bad risk       0.99      1.00      1.00       174
   good risk       1.00      0.99      1.00       173

    accuracy                           1.00       347
   macro avg       1.00      1.00      1.00       347
weighted avg       1.00      1.00      1.00       347
```

- **Matriz de Confusión:**
```
[[174   0]
 [  1 172]]
```

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/username/credit_risk_analysis.git
   cd credit_risk_analysis
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## Uso

1. Asegúrate de tener el archivo de datos `credit_risk_reto.xlsx` en la carpeta `data/`.

2. Ejecuta el script principal:
   ```bash
   python src/main.py
   ```

3. Los resultados se generarán en:
   - **Archivo procesado:** `credit_risk_enhanced_with_gemini.xlsx`
   - **Modelo entrenado:** `models/optimized_risk_classifier_model.pkl`
   - **Resumen del análisis exploratorio:** `exploratory_analysis_summary.xlsx`

---

## Dependencias

- **Python 3.8+**
- **Bibliotecas:**
  - google-generativeai
  - pandas
  - scikit-learn
  - joblib
  - openpyxl

Instala las dependencias con:
```bash
pip install -r requirements.txt
```

---
