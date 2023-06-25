from tkinter import *

def calcular():
    try:
        resultado = eval(entrada.get())
        etiqueta_resultado.config(text="Resultado: " + str(resultado))
    except:
        etiqueta_resultado.config(text="Error al calcular")

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("500x300")

etiqueta = Label(ventana, text="Ingresa una expresión matemática:")
etiqueta.pack()

entrada = Entry(ventana)
entrada.pack()

boton_calcular = Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack()

etiqueta_resultado = Label(ventana, text="Resultado:")
etiqueta_resultado.pack()

ventana.mainloop()