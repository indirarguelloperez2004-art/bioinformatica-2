#!/usr/bin/env python
# coding: utf-8

# # PRACTICA 2
# 
# ### ¡Con todo lo aprendido con Python, vamos a resolver unos ejercicios de Bioinformática!
# 
# #### 1.- Concatena las cadenas ATGCC y TCCG

# In[1]:


cadena1 = "ATGCC"
cadena2 = "TCCG"


# In[2]:


lista1 = "ATGCC"


# In[4]:


lista2="TCCG"


# In[5]:


lista_concatenada= lista1+lista2


# In[6]:


print (lista_concatenada)


# #### 2.- ¿Cuál es la longitud de ATGCGAGT?

# In[8]:


dna="ATGCGAGT"


# In[11]:


longitud= len(dna)


# In[12]:


print(len(dna))


# #### 3.- Con la cadena mgXDyTw, ponla en mayúsculas, luego en minúsculas. Extrae su longitud y divide la cadena por la letra "g"

# In[16]:


cadena="mgXDyTw"


# In[18]:


cadena_minuscula = cadena.lower()


# In[19]:


cadena_mayuscula = cadena.upper()


# In[20]:


print(cadena)


# In[21]:


print(cadena_minuscula)


# In[22]:


print(cadena_mayuscula )


# In[37]:


longuitud=len(cadena)


# In[38]:


print(len(cadena))


# In[40]:


resultado=cadena.split('g')


# In[41]:


print(resultado)


# #### 4.- Con la secuencia de aminoácidos vlspadktnv, reemplaza la valina con la tirosina. Pista: usa replace()

# In[23]:


aa = "vlspadktnv"


# In[25]:


cadena_reemplazada_v = aa.replace('v', '(y')


# In[26]:


cadena_final = cadena_reemplazada_v.replace('y', '(v)')


# In[27]:


print(aa)


# In[31]:


print(cadena_reemplazada_v)


# #### 5.- Cuenta las valinas de la secuencia original anterior.

# In[32]:


aa = "vlspadktnv"


# In[33]:


cantidad_valinas = aa.count('v')


# In[34]:


print(cantidad_valinas)


# #### 6.- Con el diccionario siguiente imprime el valor de BisI y saca el valor de EcoRI con pop(). ¿Qué pasa con el diccionario?

# In[21]:


enzR = {
    'EcoRI':r'GAATTC',
    'AvaII':r'GG(A|T)CC',
    'BisI':r'GC[ATGC]GC'
}


# In[ ]:


Tenemos que imprimir el valor.


# In[22]:


print(f"Valor de BisI: {enzR['BisI']}")


# In[ ]:


Tenemos que sacar el valor de EcoRI con pop()
# La función pop() nos devuelve el valor de la clave eliminada.


# In[23]:


valor_eco_ri = enzR.pop('EcoRI')


# In[24]:


print(f"Valor sacado (EcoRI): {valor_eco_ri}")



# In[26]:


print(f"Diccionario después de pop(): {enzR}")


# #### 7.- Con la secuencia y la lista siguiente, escribe un algoritmo que cuente el número de veces que aparece un elemento de la lista en la secuencia. Pista: hacer un diccionario para almacenar los resultados puede ser buena idea

# In[8]:


dna = "AATGATGAACGAC" 
dinucleotides = ['AA','AT','AG','AC', 
                 'TA','TT','TG','TC', 
                 'GA','GT','GG','GC', 
                 'CA','CT','CG','CT'] 


# In[10]:


conteo_dinucleotidos = {} 


# In[11]:


for d_n in dinucleotides:
    conteo_dinucleotidos[d_n] = 0 


# In[ ]:


todos los dinucleótidos de la lista en 0


# In[13]:


conteo_dinucleotidos[d_n] = dna.count(d_n)


# In[14]:


print(conteo_dinucleotidos)


# ##### ¿Cuántos counts tiene TC?

# In[15]:


conteo_tc = conteo_dinucleotidos['TC']


# In[16]:


print (conteo_tc)


# ##### ¿Puedes imprimir los dinuleótidos que tengan counts igual a 2?

# In[17]:


print("\nDinucleótidos con conteo igual a 2:")


# In[19]:


for dinucleotido, conteo in conteo_dinucleotidos.items():
    if conteo == 2:
        


# In[20]:


print(f"El dinucleótido '{dinucleotido}' tiene un conteo de 2.")

