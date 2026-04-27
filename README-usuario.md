````markdown
# Phidynamics — Manual de Usuario

## Introducción

Phidynamics es una consola de análisis bioestructural orientada al procesamiento de estructuras PDB, simulación fractal y validación dinámica.

Este manual está dirigido al usuario final.

No es necesario modificar código interno ni mover archivos dentro del sistema.  
El usuario solo debe ejecutar la consola y proporcionar rutas de entrada.

---

## Inicio rápido

Desde PowerShell, dentro del entorno del proyecto:

```powershell
python user_console.py
````

Esto abrirá la consola interactiva de usuario.

---

## Menú principal

Al iniciar, el sistema mostrará:

```text
============================================================
                 PHIDYNAMICS — CONSOLA DE USUARIO
============================================================
1. Analizar ID PDB
2. Analizar archivo PDB
3. Analizar lista de IDs
4. Analizar carpeta de estructuras
5. Ejecutar simulación fractal
6. Ejecutar validación
7. Ver reporte
0. Salir
============================================================
```

---

## Modos de uso

### 1. Analizar ID PDB

Permite analizar una estructura remota usando su identificador PDB.

Ejemplo:

```text
1BNA
```

El sistema descargará automáticamente la estructura y ejecutará el análisis.

---

### 2. Analizar archivo PDB

Permite analizar un archivo local `.pdb` o `.ent`.

Ejemplo de ruta:

```text
C:\Users\Fabian\Desktop\mi_proteina.pdb
```

El sistema copiará el archivo al entorno interno y lo procesará.

---

### 3. Analizar lista de IDs

Permite analizar múltiples estructuras desde un archivo `.txt`.

Ejemplo de ruta:

```text
C:\Users\Fabian\Desktop\mis_ids.txt
```

Contenido del archivo:

```text
1BNA
1CRN
1MBN
2POR
```

Cada línea será procesada como una estructura independiente.

---

### 4. Analizar carpeta de estructuras

Permite analizar múltiples archivos `.pdb` y `.ent` contenidos en una carpeta.

Ejemplo de ruta:

```text
D:\Laboratorio\proteinas\
```

Todos los archivos compatibles dentro de esa carpeta serán procesados.

---

### 5. Ejecutar simulación fractal

Ejecuta el motor de simulación geométrica fractal del sistema.

Genera una simulación interna y exporta resultados estructurales.

Salida:

```text
data/simulacion_fractal.json
```

---

### 6. Ejecutar validación

Ejecuta la suite de validación científica del sistema.

Esta opción sirve para:

* verificar consistencia interna
* validar geometría
* comprobar estabilidad del modelo

---

### 7. Ver reporte

Muestra el reporte consolidado de análisis almacenados en bitácora.

Incluye:

* estructuras analizadas
* delta
* frecuencia
* banda espectral
* resumen estadístico

---

## Cómo cargar datos

El usuario puede almacenar sus archivos en cualquier ubicación de su computadora.

No es necesario mover manualmente archivos al proyecto.

El sistema acepta rutas externas y organiza internamente los datos.

Ejemplos válidos:

```text
C:\Users\Fabian\Desktop\proteina.pdb
C:\Users\Fabian\Documents\mis_ids.txt
D:\Laboratorio\estructuras\
```

Phidynamics copiará automáticamente los datos al entorno interno antes de procesarlos.

---

## Qué hace internamente el sistema

Phidynamics organiza automáticamente los datos del usuario en su estructura interna:

* archivos individuales → `input/pdb/`
* listas → `input/lists/`
* carpetas → `input/batch/`

Esto permite mantener:

* orden interno
* reproducibilidad
* aislamiento del motor científico

El usuario no necesita interactuar con estas carpetas manualmente.

---

## Resultados generados

Los resultados se almacenan automáticamente en la carpeta `data/`.

Archivos comunes:

* `data/bitacora_investigacion.json`
* `data/simulacion_fractal.json`

Estos archivos contienen:

* historial de análisis
* resultados estructurales
* registros de simulación

---

## Flujo recomendado de trabajo

1. Preparar archivo, lista o carpeta
2. Ejecutar consola
3. Seleccionar modo
4. Ingresar ruta o ID
5. Ejecutar análisis
6. Revisar resultados en `data/`

---

## Requisitos

Antes de usar el sistema:

* activar entorno virtual
* instalar dependencias
* ejecutar desde la carpeta del proyecto

Ejemplo:

```powershell
.\venv\Scripts\Activate
python user_console.py
```

---

## Notas de uso

* No es necesario editar código
* No es necesario mover archivos manualmente
* No es necesario conocer la arquitectura interna
* El sistema gestiona automáticamente la organización de entradas

El usuario solo debe proporcionar datos y ejecutar el flujo de análisis.

---

## Cierre

Phidynamics está diseñado para separar completamente:

* operación de usuario
* núcleo científico

Esto permite una experiencia de uso simple, reproducible y segura.

```
```
