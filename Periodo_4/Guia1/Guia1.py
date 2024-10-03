import re 

intenciones = {
"saludar": ["hola", "buenos días", "buenas tardes", "buenas noches", "qué tal"],
"despedida": ["adiós", "hasta luego", "nos vemos", "chao"],
"pregunta_hora": ["qué hora es", "me puedes decir la hora", "dime la hora"],
"consulta_vuelo": ["consulta de vuelo", "quiero saber el estado de mi vuelo",
"información sobre vuelos"],
"reserva_vuelo": ["quiero reservar un vuelo", "cómo reservo un vuelo", "reserva devuelo"],
}

respuestas = {
"saludar": "¡Hola! ¿En qué puedo ayudarte?",
"despedida": "¡Hasta luego! Que tengas un buen día.",
"pregunta_hora": "Lo siento, no puedo decir la hora ahora mismo.",
"consulta_vuelo": "Puedes consultar el estado de tu vuelo ingresando tu número devuelo.",
"reserva_vuelo": "Puedes reservar un vuelo en nuestro sitio web o llamando a atención al cliente.",
"desconocido": "Lo siento, no entiendo tu mensaje. ¿Puedes reformularlo?"
}

def identificar_intencion(mensaje):
    mensaje= mensaje.lower()
    for intencion, patrones in intenciones.items():
        for patron in patrones:
            if re.search(patron, mensaje):
                return intencion
    return "desconocido"

def chatbot():
    print("Hola, soy tu chatbot. ¿En que puedo ayudarte este día?")
    while True:
        mensaje_usaurio = input("Tu: ")
        if mensaje_usaurio.lower()in intenciones["despedida"]:
            print("ChatBot: " + respuestas["despedida"])
            break
        intencion = identificar_intencion(mensaje_usaurio)
        print("ChatBot: " + respuestas[intencion])
        
chatbot()
