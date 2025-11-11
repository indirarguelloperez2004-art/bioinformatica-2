#!/usr/bin/env python
# coding: utf-8

# # TRABAJO DE PYTHON
# 
# ### Este trabajo cuenta el 30% de la nota. 
# 
# ### Resuelve los siguientes ejercicios en Python
# 
# #### Utiliza tantas celdas de código como necesites

# #### 1.- Busca la secuencia del gen CNTNAP2 (cromosma 7) del genoma humano. Descarga la secuencia en formato FASTA e introdúcela en este Notebook . (1 pto)

# In[ ]:


archivo = open("sequence.fasta")


# In[ ]:


archivo


# #### 2.- Muestre el encabezado y la secuencia y guarde cada uno en variables separadas. Elimine el elemento "\n" del encabezado con replace() si es que lo tiene. ¿Cual es la longitud de la secuencia?. (1 pto)

# In[ ]:


contenido = archivo.readlines()


# In[ ]:


contenido


# In[ ]:


contenido[0]


# In[ ]:


contenido[1:]


# In[ ]:


contenido[0].replace("\n", "")


# In[ ]:


"".join(contenido [1:])


# In[ ]:


len(contenido[1:])


# #### 3.- Para el encabezado, extrae empleando expresiones regulares el identificador. (1pto)

# In[ ]:


import re 


# In[ ]:


contenido[0]='>NM_014141.6 Homo sapiens contactin associated protein 2 (CNTNAP2), mRNA\n'


# In[ ]:


match = re.match(r'^>(\S+)',contenido[0])
if match:
    identificador = match.group(1)


# In[ ]:


print("Identificador:", identificador)


# #### 4.- ¿Cuál es el porcentaje de GC de la secuencia? (1 pto)

# In[ ]:


secuencia


# In[ ]:


if isinstance(secuencia, list):
    secuencia = "".join(secuencia)


# In[ ]:


secuencia = secuencia.replace("\n", "").replace(" ", "").upper()


# In[ ]:


gc = secuencia.count("G") + secuencia.count("C")


# In[ ]:


gc_total = secuencia.count("G") + secuencia.count("C")


# In[ ]:


gc_porcentaje = (gc / len(secuencia)) * 100


# In[ ]:


print(gc_porcentaje)%2


# #### 5.- Devuelve la secuencia de ARN que surgiría a partir de la siguiente secuencia. Recuerda que la secuencia de ARN resultante tiene que ser complementaria a la de ADN. (1 pto)

# In[ ]:


secuencia 


# In[ ]:


complemento = {"A":"U", "T":"A", "G":"C", "C":"G"}


# In[ ]:


if isinstance(secuencia, list):
    secuencia = "".join(secuencia)


# In[ ]:


secuencia = secuencia.replace("\n", "").replace(" ", "").upper()


# In[ ]:


arn = "".join(complemento[base] for base in secuencia)


# In[ ]:


print("ARN complementario (100 primeros nt):", arn[:100], "...")


# #### 6.- Realiza una función que realice una digestión con las siguientes enzimas de restricción en nuestra secuencia. La función tiene que devolver la siguiente información: (2 pto)
# 1. Enzimas que tienen sitios de corte en la secuencia y posición (o posiciones de corte)
# 2. Enzimas que no tienen sitios de corte (si las hay)
# 3. Resultado de la digestión: los fragmentos resultantes de nuestra secuencia
# 4. Indicar número y tamaño de cada fragmento

# In[1]:


enzR = {
    'HindIII' : 'A*AGCTT',
    'BamHI' : 'G*GATCC',
    'AluI' : 'AG*CT',
    'Sau3AI' : '*GATC',
    'EcoRI' : 'G*AATTC'
}


# In[2]:


def encontrar_cortes(secuencia, enzimas):
    secuencia = secuencia.upper()
    enzimas_con_corte = {}
    enzimas_sin_corte = []
    cortes = []

    for enzima, sitio in enzimas.items():
        sitio_limpio = sitio.replace('*', '')
        pos_corte_rel = sitio.index('*')

        posiciones = []
        start = 0
        while True:
            idx = secuencia.find(sitio_limpio, start)
            if idx == -1:
                break
            posiciones.append(idx + pos_corte_rel)
            start = idx + 1

        if posiciones:
            enzimas_con_corte[enzima] = posiciones
            cortes.extend(posiciones)
        else:
            enzimas_sin_corte.append(enzima)

    return enzimas_con_corte, enzimas_sin_corte, sorted(set(cortes))


# In[3]:


def construir_fragmentos(secuencia, cortes):
    fragmentos = []
    inicio = 0
    for c in cortes:
        fragmentos.append(secuencia[inicio:c])
        inicio = c
    fragmentos.append(secuencia[inicio:])
    tamanos = [len(f) for f in fragmentos]
    return fragmentos, tamanos


# In[4]:


def imprimir_reporte(enzimas_con_corte, enzimas_sin_corte, fragmentos, tamanos):
    print("🔹 Enzimas que cortan:")
    for e, pos in enzimas_con_corte.items():
        print(f"  - {e}: posiciones {pos}")
    print("\n🔹 Enzimas que no cortan:", enzimas_sin_corte)
    print("\n🔹 Fragmentos resultantes:")
    for i, frag in enumerate(fragmentos, 1):
        print(f"  Fragmento {i} ({len(frag)} bp): {frag}")
    print("\n🔹 Resumen:")
    print(f"  Número total de fragmentos: {len(fragmentos)}")
    print(f"  Tamaños: {tamanos}")


# In[5]:


def digerir_adn(secuencia, enzimas):
    enzimas_con_corte, enzimas_sin_corte, cortes = encontrar_cortes(secuencia, enzimas)
    fragmentos, tamanos = construir_fragmentos(secuencia, cortes)
    imprimir_reporte(enzimas_con_corte, enzimas_sin_corte, fragmentos, tamanos)
    return enzimas_con_corte, enzimas_sin_corte, fragmentos, tamanos


# In[6]:


seq = "AAGCTTGGAATTCCGATCGGATCCAGCTTAGCTGAATTC"
digerir_adn(seq, enzR)


# 7.- Realiza una función que mediante la introducción de una secuencia de ADN devuelva lo siguiente: (3 pto) 
# Todos los ORFs posibles que puedan surgir de la secuencia.
# Selecciona los 6 ORFs más largos e indica si corresponden a la strand positiva o negativa.
# Devuelve como mejor predicción, el más largo de todos.
# Calcula el porcentaje de aminoácidos aromáticos de esa proteína elegida y su longitud relativa a la secuencia original de ADN.

# pip install biopython
# 
# 
# 

# In[2]:


from Bio.Seq import Seq
from Bio.SeqUtils.ProtParam import ProteinAnalysis


# In[3]:


def encontrar_orfs(secuencia):
    secuencia = secuencia.upper()
    adn = Seq(secuencia)
    orfs = []

    # Buscar ORFs en las 6 posibles lecturas
    for strand, nuc in [(+1, adn), (-1, adn.reverse_complement())]:
        for frame in range(3):
            trans = nuc[frame:].translate(to_stop=False)
            trans_str = str(trans)

            for prot in trans_str.split('*'):  # dividir por STOP
                if len(prot) > 0:
                    orfs.append({
                        'proteina': prot,
                        'longitud': len(prot),
                        'frame': frame + 1,
                        'strand': '+' if strand == 1 else '-'
                    })
    return orfs


# In[4]:


def mostrar_orfs(orfs):
    orfs_ordenados = sorted(orfs, key=lambda x: x['longitud'], reverse=True)
    print("🔹 Se encontraron", len(orfs_ordenados), "ORFs posibles.")
    print("🔹 Los 6 ORFs más largos son:")
    for i, orf in enumerate(orfs_ordenados[:6], 1):
        print(f"  {i}. {orf['longitud']} aa | Frame: {orf['frame']} | Strand: {orf['strand']}")
    return orfs_ordenados


# In[5]:


def analizar_mejor_proteina(orfs, secuencia):
    mejor = sorted(orfs, key=lambda x: x['longitud'], reverse=True)[0]

    print("\n🔹 Mejor predicción (más largo):")
    print(f"  Longitud: {mejor['longitud']} aa | Frame: {mejor['frame']} | Strand: {mejor['strand']}")

    analisis = ProteinAnalysis(mejor['proteina'])
    arom = analisis.aromaticity() * 100
    print(f"🔹 Porcentaje de aminoácidos aromáticos: {arom:.2f}%")

    rel = (mejor['longitud'] * 3 / len(secuencia)) * 100
    print(f"🔹 Longitud relativa de la proteína: {rel:.2f}% del ADN original")

    return mejor, arom, rel


# In[6]:


def analizar_orfs(secuencia):
    orfs = encontrar_orfs(secuencia)
    orfs_ordenados = mostrar_orfs(orfs)
    mejor, arom, rel = analizar_mejor_proteina(orfs_ordenados, secuencia)
    return mejor, orfs_ordenados[:6], arom, rel


# In[7]:


seq = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
analizar_orfs(seq)

