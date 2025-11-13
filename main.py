from openai import OpenAI
from gtts import gTTS
import pygame
import os
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
ruta = 'audios/audio.mp3'
RobotName = 'asistente'

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

def preguntar(mensaje):    
    chat_completion = client.chat.completions.create(
        model="ollamaTesisQ34b",
        messages=[
            {
                "role": "user", 
                # "content": "Hola, ¿cómo estás? Eres un asistente y tu mision es ayudar a la decana de la facultad respondiendo a tareas cotidianas y sencillas como preguntas frecuentes o busquedas sencillas, no respondas con emojis. solo texto."
                
                "content": mensaje + 
                f"""
                Eres un asistente y tu mision es ayudar a la decana de la facultad respondiendo a tareas cotidianas y 
                sencillas como preguntas frecuentes o busquedas sencillas, no respondas con emojis. solo texto en 
                español y si hay términos en inglés menciona su definición en español. No es necesario que respondas 
                a la última clausula, procura dar respuestas breves y solicitar más detalles si la persona desea una 
                respuesta más elaborada. Ignora la palabra {RobotName} en la solicitud del usuario.
                """
            }
        ],
        stream=False,
    )
    return chat_completion

def ConvertirTexto2Audio(mensaje, ruta):
    tts = gTTS(mensaje, lang='es', slow=False)
    if not os.path.exists("audios"):
        os.makedirs("audios")
    tts.save(ruta)

def ReproducirMensaje(mensaje):
    ConvertirTexto2Audio(mensaje, ruta)

    if os.path.exists(ruta):
        pygame.mixer.init()
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play()               # Carga y reproduce el archivo de audio
        
        while pygame.mixer.music.get_busy():    # Espera mientras se reproduce el audio
            pygame.time.Clock().tick(10)
        pygame.mixer.music.load("audios\empty.mp3")
        os.remove(ruta)
    else:
        ConvertirTexto2Audio('Error gtts001: No se pudo traducir el mensaje de salida.', ruta)

commands = [
    'asistente silencio',
    'asistente registrar rostros',
    'asistente tomar asistencia',
    'asistente',
]

def ReconocerComandos():
    while True:
        with mic as source:
            audio = r.listen(source)
        
        try:
            words = r.recognize_google(audio, language='es-ES')
            
            if words == commands[0]:
                ReproducirMensaje('Silenciando el asistente. Si deseas que te escuche nuevamente solo di mi nombre, hasta luego!')
                print(words)
                # Vuelve a escuchar esperando que llamen por su nombre al asistente
                while True:
                    with mic as source:
                        audio = r.listen(source)
                    try:
                        words = r.recognize_google(audio, language='es-ES')
                        if words in commands[3]:
                            ReproducirMensaje('Ya estoy de nuevo a tu servicio, dime en qué puedo ayudarte.')
                            break
                    except sr.UnknownValueError:
                        continue
            else:
                if 'asistente' in words:
                    print("Procesando solicitud.")
                    ReproducirMensaje('Listo! Dame un momento, estoy procesando tu solicitud')
                    return words
        except sr.UnknownValueError:
            ReproducirMensaje('Disculpa, parece que no te entendí. Debes indicarme tu solicitud y al final decir mi nombre.')
            # print('>>> Trying to undestand what you are talking...')
        except sr.RequestError:
            ReproducirMensaje('Parece que hay mucho ruido, no logro entender si me están hablando jeje')
            # print(f"Could not request results from Google Speech Recognition service; {e}")
            print(words)

if __name__ == "__main__":
    print('Start Talking')
    
    
    while True:
        mensaje = ReconocerComandos()
        chat_completion = preguntar(mensaje)
        print(f'Using model: {chat_completion.model}, asking for a response')
        print(f'Chat Completion: {chat_completion.choices[0].message.content}')
        ReproducirMensaje(chat_completion.choices[0].message.content)

