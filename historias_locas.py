# concatenar cadenas de caracteres.
# supongamos que queremos crear una cadena que diga:
# aprende a programar con___________.

'''
organicacion = "freecodecamp"
print("Aprende a programar con " + organicacion)
print("Aprende a programar con {}". format(organicacion))
print(f"Aprende a programar con {organicacion}") # f-string
'''

# Mad Lips (Historias Locas)

adj = input("Adjetivo: ")
verbo1 = input("verbo: ")
verbo2 = input("verbo: ")
sustantivo_plural = input("Sustantivo (Plural): ")
madlip = f"¡programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freecodecam y alcanza tus {sustantivo_plural}!"

print(madlip)