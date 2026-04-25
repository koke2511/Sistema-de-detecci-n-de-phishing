# Sistema de detección de phishing con Machine Learning

##  Descripción

Este proyecto consiste en el desarrollo de una herramienta capaz de detectar URLs maliciosas (phishing) mediante técnicas de Machine Learning.  

El sistema analiza diferentes características estructurales de una URL y, a partir de ellas, determina si se trata de una URL legítima o potencialmente fraudulenta.

Este proyecto está inspirado en tareas reales realizadas en un entorno SOC (Security Operations Center), donde el análisis de URLs sospechosas es una actividad habitual dentro de equipos MDR (Managed Detection and Response).

---

## Objetivo

Desarrollar un sistema que permita:

- Analizar URLs automáticamente
- Identificar patrones típicos de phishing
- Clasificar URLs como legítimas o maliciosas
- Facilitar el análisis en entornos de ciberseguridad

---

## Tecnologías utilizadas

- **Python**
- **pandas** → manipulación de datos
- **scikit-learn** → modelo de Machine Learning
- **tldextract** → análisis de dominios
- **VSCode** → entorno de desarrollo

---

## Funcionamiento del sistema

El sistema sigue las siguientes fases:

1. **Lectura del dataset**  
   Se cargan URLs etiquetadas como legítimas o phishing.

2. **Extracción de características (features)**  
   Se analizan aspectos como:
   - longitud de la URL  
   - uso de HTTPS  
   - número de guiones  
   - presencia de palabras sospechosas (login, verify, etc.)  
   - número de subdominios  

3. **Entrenamiento del modelo**  
   Se utiliza un modelo de clasificación (*Logistic Regression*) para aprender patrones.

4. **Evaluación**  
   Se mide el rendimiento mediante métricas como:
   - Accuracy  
   - Precision  
   - Recall  

5. **Predicción**  
   El usuario puede introducir una URL y el sistema determina si es phishing o legítima.

---

## 📁 Estructura del proyecto
