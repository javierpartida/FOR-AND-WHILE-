WHILE 1 
# 2n
# ∑   i= 2+4+6+...2n
# i=2 
from guizero import App, Text, TextBox, PushButton
import pyttsx3 engine=pyttsx3.init() sum=0
i=2 def resultado():
    global sum, i
    if int(n.value)>0:
     while i<(int(n.value)*2+2):
        sum+=i
        i+=2
        result.value=f"la sumatoria es: {str(sum)}" else:
        result.value="nummero invalido" n.value=""
def mensaje():
    cadena="ingresa el valor de n de la sumatoria"
    engine.say(cadena)
    engine.runAndWait()
def nuevo():
    global sum,i
    sum=0
    i=0
    n.value=""
    result.value=""
app=App(title="WHILE 1")
button=PushButton(app,text="instruciones", command=mensaje)
titulo= Text(app, text="(while)")
formula= Text(app, text="2n\n ∑  i= 2+4+6+...2n\n i=2 ")
message2 = Text(app, text="ingresa el valor de n:")
n= TextBox(app, width=20,)
button2=PushButton(app,text="Resolver", command=resultado)
button3=PushButton(app,text="Nuevo", command=nuevo)
result= Text(app,text="")
app.display()