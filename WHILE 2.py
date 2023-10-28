WHILE 2
# n
# Π  i= 1*2*3*4...n
# i=1

from guizero import App, Text, TextBox, PushButton
import pyttsx3 engine=pyttsx3.init()
prod=1
i=1
def resultado():
    global prod,i
    if int(n.value)>0:
    while i<int(n.value):
    prod=prod*i  i+=1
   result.value=f"la productoria es: {str(prod)}" else:
        result.value="nummero invalido"
    n.value=""
def mensaje():
    cadena="ingresa el valor de n de la productoria"
    engine.say(cadena)
    engine.runAndWait()
def nuevo():
    global prod,i
    prod=1
    i=1
    n.value=""
    result.value=""
app=App(title="WHILE 2")
button=PushButton(app,text="instruciones", command=mensaje)
titulo= Text(app, text="(while)")
formula= Text(app, text="n\n  Π i= 1*2*3*4...n \n i=1 ")
message2 = Text(app, text="ingresa el valor de n:")
n= TextBox(app, width=20,)
button2=PushButton(app,text="Resolver", command=resultado)
button3=PushButton(app,text="Nuevo", command=nuevo)
result= Text(app,text="")
app.display()