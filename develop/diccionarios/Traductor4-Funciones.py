
def establecer_diccionario():
    diccionario={}
    while True:
        palabras = input('Deme palabras castellano e ingles (castellano:ingles) -> ')
        itemDiccionario = palabras.split(':')
        diccionario[itemDiccionario[0]] = itemDiccionario[1]
        valor = input('Continuar -> ').upper()
        if valor != 'S':
            print('Esta establecido el diccionario: ',diccionario)
            return diccionario
def traducir(frase):
    frase_list = frase.split()
    frase_traducida_list = []
    for palabra in frase_list:
        if palabra in diccionario.keys():
            frase_traducida_list.append(diccionario[palabra])
        else:
            frase_traducida_list.append(palabra)
    frase_traducida = ' '.join(frase_traducida_list)
    return frase_traducida

#Crear diccionario
diccionario=establecer_diccionario()

# Traducir una frase
frase = input('Dame frase:')
frase_traducida=traducir(frase)
print('La frase traducida es:',frase_traducida)



