WHILE 4
# n
# ∑   i^3= 1^3 + 2^3 + 3^3...n
# i=1 

from guizero import App, Text, TextBox, PushButton
import pyttsx3 engine=pyttsx3.init() sum=0  i=1
def resultado():
    global sum,i
    if int(n.value)>0:
    while i<int(n.value)+1:    sum+=i**3  i+=1
        result.value=f"la sumatoria es: {str(sum)}" else:
        result.value="nummero invalido"  n.value=""
def mensaje():
    cadena="ingresa el valor de n para resolver la sumatoria"
    engine.say(cadena)
    engine.runAndWait()
def nuevo():
    global sum
    sum=0  n.value=""
    result.value=""
app=App(title="WHILE 4")
button=PushButton(app,text="instruciones", command=mensaje)
titulo= Text(app, text="(while)")
formula= Text(app, text="n\n ∑ i^3= 1^3 + 2^3...n\n i=1")
message2 = Text(app, text="ingresa el valor de n:")  n= TextBox(app, width=20,)
button2=PushButton(app,text="Resolver", command=resultado)
button3=PushButton(app,text="Nuevo", command=nuevo)
result= Text(app,text="") app.display()