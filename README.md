﻿# Aplicación Hipotecaria

## Descripción

Esta aplicación es una herramienta interactiva de cálculo de amortización de préstamos. Permite a los usuarios ingresar detalles de su préstamo, como el monto financiado, la tasa de interés, el plazo y la fecha de inicio, para calcular y visualizar el programa de pagos. La aplicación ofrece opciones para editar los pagos, descargar el cronograma de amortización y ver gráficos que muestran el importe pagado y la composición de los pagos a lo largo del tiempo.

## Requisitos

- Python 3.8 o superior
- Paquetes Python: `shiny`, `shiny.express`, `faicons`, `pandas`, `plotnine`

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/CRISHFAS/App-Hipotecaria
    ```

2. **Crear un entorno virtual (opcional pero recomendado):**

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

3. **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Iniciar la aplicación:**

    ```bash
    python app.py
    ```

   La aplicación estará disponible en `http://127.0.0.1:8000`.


### Archivos Principales

- **`app.py`**: Este archivo configura la interfaz de usuario (UI) y la lógica de la aplicación utilizando Shiny. Permite a los usuarios ingresar datos, editar pagos, descargar el cronograma y ver gráficos.

- **`helpers.py`**: Contiene funciones para calcular la amortización del préstamo, generar gráficos y manipular datos.

- **`requirements.txt`**: Lista las dependencias del proyecto. Se puede generar con el siguiente comando:

    ```bash
    pip freeze > requirements.txt
    ```

## Uso

1. **Definir el préstamo**:
   - **Monto Financiado**: El monto total del préstamo.
   - **Tasa de Interés**: La tasa de interés anual del préstamo.
   - **Plazo del Préstamo en Años**: La duración del préstamo en años.
   - **Fecha del Primer Pago**: La fecha en la que se realizará el primer pago.

2. **Editar pagos**:
   - La tabla editable permite ajustar el cronograma de pagos y agregar notas.

3. **Actualizar pagos**:
   - Presiona el botón "Update Payments" para recalcular el cronograma con los ajustes realizados.

4. **Descargar cronograma**:
   - Haz clic en "Download Schedule" para descargar el cronograma de pagos en formato CSV.

5. **Visualizar gráficos**:
   - **Cumulative Amount**: Muestra el monto total pagado (principal e interés) a lo largo del tiempo.
   - **Payment Composition**: Muestra la composición de los pagos (principal e interés) a lo largo del tiempo.

## Recursos

- **Shiny**: Framework para construir aplicaciones web interactivas en Python.
- **Pandas**: Biblioteca de Python para la manipulación y análisis de datos.
- **Plotnine**: Biblioteca de visualización basada en la gramática de gráficos de ggplot2 para Python.
- **Faicons**: Iconos para la interfaz de usuario.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias o mejoras, por favor, abre un problema o una solicitud de extracción (pull request) en el repositorio.

![Captura](public/capture.png)
