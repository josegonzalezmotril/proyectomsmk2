import speech_recognition as sr
from pandas import *


datos = read_csv("C:\\Users\\chema\\Downloads\\prueba.csv",encoding = "ISO-8859-1",sep='|')


rec = sr.Recognizer()

with sr.Microphone() as source:
    print("Dime tu nombre:")
    audio = rec.listen(source)
    
    try:
        text = rec.recognize_google(audio, language='es-Es')
      
    except:
        print("Lo siento, no te he entendido, bonico!!")

with sr.Microphone() as source2:
    print("Di el mes a mirar...")
    audio2 = rec.listen(source2)
    
    try:
        text2 = rec.recognize_google(audio2, language='es-Es')      
    except:
        print("Lo siento, no te he entendido, bonico!!")

resultado = datos[(datos.nombre==text)&(datos.mes==text2)]
 	
print('Hola ',text,text2)
print(resultado)
input()
