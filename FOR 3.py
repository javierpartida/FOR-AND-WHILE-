FOR 3 
# 2n
# Π  i= 2*4*6...2n
# i=2

from guizero import App, Text, TextBox, PushButton
import pyttsx3 engine=pyttsx3.init()
prod=1
def resultado():
global prod
if int(n.value)>0:
for i in range(2,(int(n.value)*2+2),2): prod=prod*i
        result.value=f"la productoria es: {str(prod)}" else:
        result.value="nummero invalido"  n.value=""
def mensaje():
    cadena="ingresa el valor de n para resolver la productoria"
    engine.say(cadena)
    engine.runAndWait()
def nuevo():
    global prod
    prod=1
    n.value=""
    result.value=""
app=App(title="FOR 3")
button=PushButton(app,text="instruciones", command=mensaje)
titulo= Text(app, text="(for)")
formula= Text(app, text="2n\n  Π i= 2*4*6...2n \n i=2 ")
message2 = Text(app, text="ingresa el valor de n:")
n= TextBox(app, width=20,)
button2=PushButton(app,text="Resolver", command=resultado)
button3=PushButton(app,text="Nuevo", command=nuevo)
result= Text(app,text="")
app.display()