###############################################################
# Trabajo final de Bioinformática - Curso 2025/26
# Análisis de parámetros biomédicos por tratamiento
# Autor: Indira Arguello Pérez
###############################################################

# =============================================================
# 1. Cargar librerías y archivo de datos (0.5 pts)
# =============================================================

# Cambia la ruta si tu archivo no está en el Escritorio
setwd("~/Desktop")
getwd()

# Cargar datos del archivo CSV
datos <- read.csv("datos_biomed.csv", header = TRUE, sep = ",")

# Revisar estructura y resumen de los datos
head(datos)       # Primeras 6 filas
str(datos)        # Estructura de las variables
summary(datos)    # Resumen estadístico

# Convertir la variable 'Tratamiento' en factor
datos$Tratamiento <- as.factor(datos$Tratamiento)

# =============================================================
# 3. Gráfica con todos los boxplots por tratamiento (1 pt)
# =============================================================
library(ggplot2)
library(dplyr)
library(tidyr)


datos_largos <- datos %>%
  pivot_longer(cols = c(Glucosa, Presion, Colesterol),
               names_to = "Variable",
               values_to = "Valor")


head(datos_largos)


ggplot(datos_largos, aes(x = Tratamiento, y = Valor, fill = Tratamiento)) +
  geom_boxplot() +
  facet_wrap(~ Variable, scales = "free_y") +
  labs(title = "Boxplots por tratamiento",
       x = "Tratamiento", y = "Valor") +
  theme_minimal()

# =============================================================
# 4. Violin plot (1 pt)
# =============================================================

ggplot(datos, aes(x = Tratamiento, y = Glucosa, fill = Tratamiento)) +
  geom_violin(trim = FALSE) +
  geom_boxplot(width = 0.1, fill = "white") +
  labs(title = "Violin plot de glucosa por tratamiento",
       x = "Tratamiento", y = "Glucosa") +
  theme_minimal()

# =============================================================
# 5. Gráfico de dispersión Glucosa vs Presión (1 pt)
# =============================================================

ggplot(datos, aes(x = Glucosa, y = Presion, color = Tratamiento)) +
  geom_point(size = 2) +
  labs(title = "Glucosa vs Presión por tratamiento",
       x = "Glucosa", y = "Presión") +
  theme_minimal() +
  theme(legend.position = "bottom")

# =============================================================
# 6. Facet Grid: Colesterol vs Presión por tratamiento (1 pt)
# =============================================================

ggplot(datos, aes(x = Colesterol, y = Presion)) +
  geom_point(color = "steelblue") +
  facet_grid(~ Tratamiento) +
  labs(title = "Colesterol vs Presión por tratamiento",
       x = "Colesterol", y = "Presión") +
  theme_minimal()

# =============================================================
# 7. Histogramas para cada variable (0.5 pts)
# =============================================================

datos_largos <- datos %>%
  pivot_longer(cols = c(Glucosa, Presion, Colesterol),
               names_to = "Variable", values_to = "Valor")

ggplot(datos_largos, aes(x = Valor)) +
  geom_histogram(bins = 20, fill = "skyblue", color = "black") +
  facet_wrap(~ Variable, scales = "free") +
  labs(title = "Histogramas de cada variable",
       x = "Valor", y = "Frecuencia") +
  theme_minimal()

# =============================================================
# 8. Crear un factor a partir del tratamiento (1 pt)
# =============================================================

datos$Tratamiento <- as.factor(datos$Tratamiento)
levels(datos$Tratamiento)

# =============================================================
# 9. Media y desviación estándar de glucosa por tratamiento (0.5 pts)
# =============================================================

aggregate(Glucosa ~ Tratamiento, data = datos,
          FUN = function(y) c(media = mean(y), sd = sd(y)))

# =============================================================
# 10. Extraer los datos para cada tratamiento (1 pt)
# =============================================================

farmacoB <- subset(datos, Tratamiento == "FarmacoB")
placebo  <- subset(datos, Tratamiento == "Placebo")

head(farmacoB)
head(placebo)

# =============================================================
# 11. Evaluar normalidad y comparación de medias (1 pt)
# =============================================================

# Prueba de normalidad (Shapiro-Wilk)
by(datos$Glucosa, datos$Tratamiento, shapiro.test)

# Si los datos no son normales:
kruskal.test(Glucosa ~ Tratamiento, data = datos)

# =============================================================
# 12. ANOVA sobre la glucosa por tratamiento (1 pt)
# =============================================================

anova_glu <- aov(Glucosa ~ Tratamiento, data = datos)
summary(anova_glu)

# Comparaciones post-hoc (Tukey)
TukeyHSD(anova_glu)

###############################################################
# FIN DEL TRABAJO
###############################################################
