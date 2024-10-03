import nltk
import string
import pickle
import random
import json
from nltk.stem import WordNetLemmatizer

# Descargar stopwords si no lo has hecho aún
nltk.download('punkt')
nltk.download('stopwords')

lematizador = WordNetLemmatizer()

# Cargar el modelo, el vectorizador y el codificador de etiquetas
with open('model.pkl', 'rb') as f:
    vectorizar, le, model = pickle.load(f)

# Cargar las intenciones
with open('intenciones.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Función para preprocesar las oraciones
def preproceso(oracion):
    oracion = oracion.lower()
    oracion = ''.join([char for char in oracion if char not in string.punctuation])
    tokens = nltk.word_tokenize(oracion)
    tokens = [lematizador.lemmatize(word) for word in tokens if word not in nltk.corpus.stopwords.words('spanish')]
    return ' '.join(tokens)

# Función para obtener la respuesta del modelo
def obtener_respuestas(entrada_usuario):
    entrada_procesada = preproceso(entrada_usuario)  # Procesar la entrada del usuario
    X = vectorizar.transform([entrada_procesada])  # Transformar la entrada a la representación del modelo
    confianza = model.predict_proba(X)[0]  # Obtener la probabilidad de cada etiqueta
    max_conf_index = confianza.argmax()  # Índice de la mayor confianza
    max_conf = confianza[max_conf_index]  # Valor de la mayor confianza
    etiqueta = le.inverse_transform([max_conf_index])[0]  # Etiqueta predicha
    print(f"Confianza: {max_conf}, Etiqueta: {etiqueta}")  # Mostrar la confianza y la etiqueta
    
    # Verificar si la confianza es suficientemente alta
    if max_conf < 0.4:
        return "Lo siento, no entendí lo que quisiste decirme"
    else:
        for intencion in data['intenciones']:
            if intencion['etiqueta'] == etiqueta:
                return random.choice(intencion['respuestas'])  # Devolver una respuesta aleatoria de la intención

# Función principal para el chatbot
def chat():
    print("Hola, soy Chatty. Escribe 'salir' para terminar la conversación.")
    while True:
        entrada_usuario = input("Tú: ")  # Leer entrada del usuario
        if entrada_usuario.lower() == 'salir':  # Verificar si el usuario quiere salir
            print("Chatty: ¡Hasta luego!")
            break 
        respuesta = obtener_respuestas(entrada_usuario)  # Obtener la respuesta del chatbot
        print(f"Chatty: {respuesta}")

# Iniciar el chat
chat()
