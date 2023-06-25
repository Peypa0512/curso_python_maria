diccionario={}

#Crear diccionario
continuar = True
while continuar:
    palabras =  input('Deme palabras castellano e ingles (castellano:ingles) -> ')
    itemDiccionario = palabras.split(':')
    diccionario[itemDiccionario[0]]=itemDiccionario[1]
    valor= input('Continuar -> ').upper()
    continuar= True if valor=='S' else False


frase = input('Dame frase:')

frase_list = frase.split()
frase_traducida_list = []
for palabra in frase_list:
    if palabra in diccionario.keys():
        frase_traducida_list.append(diccionario[palabra])
    else:
        frase_traducida_list.append(palabra)
frase_traducida = ' '.join(frase_traducida_list)
print('La frase traducida es:')
print(frase_traducida)



