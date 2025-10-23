#!/usr/bin/env python
# coding: utf-8

# # PRACTICA 4
# 
# ### Resuelve los siguientes ejercicios

# ##### 1.- Abre el fichero dna.txt, guarda una lista del contenido del archivo. Devuelve su longitud y su primer caracter

# In[9]:


with open('dna.txt', 'r') as f:
    dna = f.read().strip() 


# In[10]:


print("Longitud:", len(dna))



# In[11]:


print("Primer carácter:", dna[0])


# ##### 2.- Crea dos archivos. Uno almacena los accession que empiezen por 'a' y el otro el resto

# In[15]:


accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']


# In[16]:


a_accs = [x for x in accs if x.startswith('a')]


# In[17]:


otros = [x for x in accs if not x.startswith('a')]


# In[20]:


with open('a_accs.txt', 'w') as f:
    f.write('\n'.join(a_accs))


# In[21]:


with open('otros_accs.txt', 'w') as f:
    f.write('\n'.join(otros))


# ##### 3.- Imprime solamente los accessions de la lista anterior que empiecen por 'a' y no acaben con '6'. Pista: usa endswith() y startswidth()

# In[23]:


for acc in accs:
    if acc.startswith('a') and not acc.endswith('6'):
        print(acc)


# ##### 4.- Escribe una función que cuente el porcentaje de A de una secuencia

# In[13]:


def porcentaje_A(seq):
    porcentaje = (seq.count('A') / len(seq)) * 100
    return porcentaje


# ##### ¿Puedes hacer que devuelva dos decimales? ¿Y que lidie con mayúsculas y minúsculas?

# In[14]:


def porcentaje_A(seq):
    seq = seq.upper() 
    porcentaje = (seq.count('A') / len(seq)) * 100
    return round(porcentaje, 2) 


# ##### ¿Y que devuelva el número de decimales que yo quiero?

# In[4]:


print(porcentaje_A("AAATTT", 4))


# In[16]:


def porcentaje_A(seq, decimales=2):
    seq = seq.upper()
    porcentaje = (seq.count('A') / len(seq)) * 100
    return round(porcentaje, decimales)


# ##### ¿Sabes poner un valor por defecto en un argumento?

# In[17]:


print(porcentaje_A("AAATTT"))      


# ##### ¿Qué pasa si no ponemos un argumento? ¿Sabrías hacer una función encapsulada?

# In[18]:


print(porcentaje_A("AAATTT", 4))  


# ##### Testea tu función original con assert

# In[19]:


assert porcentaje_A("AAATTT") == 50.0


# In[20]:


assert porcentaje_A("aaaa", 1) == 100.0


# In[21]:


assert porcentaje_A("tttt", 3) == 0.0


# In[ ]:


print("✅ Todos los tests pasaron correctamente")


# #### 5.- De la lista de accessions que se proporciona obtén lo siguiente:
# 1. Los que tengan el número 5
# 2. Los que tengan la letra 'd' o la 'e'
# 3. Los que tengan las letras 'd' y 'e' en ese orden
# 4. Los que tengan las letras 'd' y 'e' en ese orden con una letra cualquiera en medio
# 5. Los que tengan ambas letras 'd' y 'e' en cualquier orden
# 6. Los que empiezan por 'x' o por 'y'
# 7. Los que empiezan por 'x' o 'y' y terminan por 'e'
# 8. Los que tienen tres o más dígitos seguidos
# 9. Los que terminan con 'd' seguidos de 'a' o 'r' o 'p'

# In[2]:


import re


# In[3]:


accs = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']


# In[4]:


print("1.", [a for a in accs if re.search('5', a)])


# In[5]:


print("2.", [a for a in accs if re.search('[de]', a)])


# In[6]:


print("3.", [a for a in accs if re.search('d.*e', a)])


# In[7]:


print("4.", [a for a in accs if re.search('d[a-zA-Z]e', a)])


# In[8]:


print("5.", [a for a in accs if re.search('d', a) and re.search('e', a)])


# In[9]:


print("6.", [a for a in accs if re.match('^[xy]', a)])


# In[10]:


print("7.", [a for a in accs if re.match('^[xy].*e$', a)])


# In[11]:


print("8.", [a for a in accs if re.search(r'\d{3,}', a)])


# In[12]:


print("9.", [a for a in accs if re.search('d[arp]$', a)])

