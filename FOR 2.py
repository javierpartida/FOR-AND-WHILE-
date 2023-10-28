FOR 2
# n
# Π  i= 1*2*3*4...n
# i=1

from guizero import App, Text, TextBox, PushButton
import pyttsx3 engine=pyttsx3.int()
producto=1
def resultado():
    global producto
    if int(n.value)>0:
    for i in range(1,(int(n.value)+1),1):
     producto=producto*i
     result.value=f"la productoria es: {str(producto)}"
    else:
        result.value="nummero invalido"
    n.value=""
def mensaje():
    cadena="ingresa el valor de n para resolver la productoria"
    engine.say(cadena)
    engine.runAndWait()
def nuevo():
    global producto
    producto=1
    n.value=""
    result.value=""
app=App(title="FOR 2")
button=PushButton(app,text="instruciones", command=mensaje)
titulo= Text(app, text="(for)")
formula= Text(app, text="n\n  Π i= 1*2*3*4...n \n i=1 ")
message2 = Text(app, text="ingresa el valor de n:")
n= TextBox(app, width=20,)
button2=PushButton(app,text="Resolver", command=resultado)
button3=PushButton(app,text="Nuevo", command=nuevo)
result= Text(app,text="")
app.display()