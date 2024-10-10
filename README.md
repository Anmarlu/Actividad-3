# Instrucciones para ejecutar el archivo Python en Visual Studio Code

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas en tu sistema:

1. **[Python](https://www.python.org/downloads/)**: Asegúrate de tener instalado Python 3.12.6 Puedes verificarlo ejecutando el siguiente comando en tu terminal:

    ```bash
    python --version
    ```

2. **[Visual Studio Code (VS Code)](https://code.visualstudio.com/Download)**: Descarga e instala Visual Studio Code.

3. **Extensión de Python para VS Code**: Instala la extensión oficial de Python en Visual Studio Code. Para hacerlo:
   - Abre VS Code.
   - Haz clic en el ícono de extensiones en el menú lateral izquierdo.
   - Busca "Python" en la barra de búsqueda.
   - Instala la extensión de Microsoft llamada "Python".

## Pasos para ejecutar el archivo Python

Sigue los pasos a continuación para ejecutar un archivo Python en VS Code:

### 1. Abre tu proyecto en VS Code

- Abre Visual Studio Code y navega a la carpeta donde tienes tu archivo Python.
- Alternativamente, puedes abrir el terminal y ejecutar:

    ```bash
    code nombre_de_tu_carpeta
    ```

### 2. Configura el intérprete de Python

- Si tienes varias versiones de Python instaladas, debes seleccionar la correcta en VS Code.
  - Presiona `Ctrl + Shift + P` (o `Cmd + Shift + P` en macOS) para abrir la Paleta de Comandos.
  - Escribe `Python: Select Interpreter` y selecciona la versión de Python que deseas usar.

### 3. Ejecuta el archivo Python

- Abre el archivo Python que quieres ejecutar (por ejemplo, `main.py`).
- Para ejecutarlo:
  - Presiona `F5` o selecciona `Run` -> `Start Debugging` en el menú.
  - O bien, abre el terminal integrado (`Ctrl + ``) y escribe:

    ```bash
    python nombre_del_archivo.py
    ```

  (Asegúrate de estar en el directorio correcto).

### 4. Verifica la salida

- La salida del programa se mostrará en el terminal integrado de VS Code, donde podrás ver el resultado de la ejecución.

## Recursos adicionales

- [Documentación oficial de Python en VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
