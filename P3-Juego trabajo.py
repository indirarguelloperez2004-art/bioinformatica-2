#!/usr/bin/env python
# coding: utf-8

# # PRACTICA 3
# 
# 
# ## JUEGO DE ADIVINANZAS
# 
# #### Escribe un programa que coja un número entero del 1 al 100, y los jugadores tienen que tratar de adivinar el número.
# 
# #### Las reglas son las siguientes:
# 
# 1. Si un jugador escoje un número menor que 1 o mayor que 100, el programa dice "FUERA DE LÍMITES"
# 2. En el primer turno del jugador, si está en un rango de 10 del número dice "¡CALIENTE!". Si está fuera de ese rango dice "¡FRIO!"
# 3. En todas las rondas siguientes, si el jugador se acerca más que la vez anterior, dice "¡MAS CALIENTE!". Si está más lejos que la anterior vez dice "¡MAS FRIO!"
# 4. Cuando el jugador acierte el número, les dirá que han acertado y cuántos intentos les ha llevado
# 
# 
# 
# 

# ##### PISTAS
# 1. Trata obtener un número aleatorio entre el 1 y el 100
# 2. Haz una introducción de tu juego y explica las reglas
# 3. Crea una lista que almacene los intentos. 
# 4. Haz un bucle que evalúe un número. Prueba que funcione primero. While podría ir bien
# 5. Modifica ese bucle para que compare nuestro número con el intento. Si se acierta usa break, si no puedes usar continue y tienes que seguir preguntando al jugador por nuevos intentos

# In[8]:


import random


# In[ ]:


print("Bienvenido al Juego de Adivinanzas 🎲")


# In[ ]:


print("He pensado un número entre 1 y 100, ¡intenta adivinarlo!")


# In[ ]:


print("Reglas:")


# In[ ]:


print("1. Si tu número está fuera del rango 1-100: 'FUERA DE LÍMITES'")


# In[ ]:


print("2. En el primer intento, si estás a 10 del número secreto: '¡CALIENTE!', si no: '¡FRÍO!'")



# In[ ]:


print("3. En los siguientes intentos, si estás más cerca que antes: '¡MÁS CALIENTE!', si estás más lejos: '¡MÁS FRÍO!'")


# In[ ]:


print("4. Cuando lo adivines, te diré cuántos intentos hiciste.\n")


# In[9]:


numero_secreto = random.randint(1, 100)


# In[10]:


intentos = []


# In[12]:


while True:
    try:
        intento = int(input("Introduce un número entre 1 y 100: "))
    except ValueError:
        print("Por favor introduce un número válido.")
        continue
        
    # Comprobar si está dentro de los límites
    if intento < 1 or intento > 100:
        print("FUERA DE LÍMITES ❌")
        continue
    
   
    intentos.append(intento)
    

    if intento == numero_secreto:
        print(f"🎉 ¡Felicidades! Has adivinado el número en {len(intentos)} intentos.")
        break


# In[20]:


if len(intentos) == 1:
    if abs(numero_secreto - intento) < 10:
        print("¡CALIENTE! 🔥")
    else:
        print("¡FRÍO! ❄️")
else:
    if abs(numero_secreto - intento) < abs(numero_secreto - intentos[-2]):
        print("¡MÁS CALIENTE! 🔥🔥")
    else:
        print("¡MÁS FRÍO! ❄️❄️")

