Obtener el producto de dos numeros enteros positivos mediante sumas sucesivas.

from guizero import App, Text, TextBox, PushButton
import pyttsx3 engine=pyttsx3.init()
prod=0  i=1
def resultado():
    global prod,i
    if int(val1.value)>0 and int(val2.value)>0:
    if int(val1.value)>int(val2.value):
    cons=int(val1.value)   n=int(val2.value)  else:
    cons=int(val2.value)  n=int(val1.value)
        while i<=n:
    prod=prod+cons   i+=1
        result.value=f"el producto es: {str(prod)}" else:
        result.value="Error: numero negativo"
    val1.value=""
    val2.value=""
def mensaje():
    cadena="ingresa los dos valores para calcular su producto"
    engine.say(cadena)  engine.runAndWait()
def nuevo():
    global prod, cons, n, i
    i=1  prod=0
    val1.value=""   val2.value=""
    cons=0   n=0
    result.value=""}
app=App(title="WHILE 5")
button=PushButton(app,text="instruciones", command=mensaje)
titulo= Text(app, text="(for)")
message1 = Text(app, text="valor 1:")
val1= TextBox(app, width=20,)
message2 = Text(app, text="valor 2:")
val2= TextBox(app, width=20,)
button2=PushButton(app,text="producto:", command=resultado)
button3=PushButton(app,text="Nuevo", command=nuevo)
result= Text(app,text="")  app.display()