# Textify - Extracción de Texto de Imágenes (OCR) Local

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-2.x-orange.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Textify es una aplicación web gratuita y de código abierto que permite extraer texto de imágenes utilizando tecnología OCR (Reconocimiento Óptico de Caracteres). Desarrollada con Python y Flask, Textify ofrece una interfaz intuitiva, accesible y fácil de usar, permitiendo convertir imágenes con texto en contenido editable en segundos, directamente en tu máquina local.

**Filosofía del Proyecto:**
*   **Privacidad Primero:** Tus imágenes se procesan localmente y nunca abandonan tu computadora.
*   **Accesibilidad:** Diseñada pensando en la accesibilidad (WCAG), incluyendo navegación por teclado, atributos ARIA y retroalimentación clara.
*   **Experiencia de Usuario (UX):** Interfaz limpia, validación de entrada en tiempo real y procesos simplificados.

## Características Principales

*   **Extracción OCR Precisa:** Utiliza Tesseract OCR para una alta calidad de extracción de texto.
*   **Soporte Multi-idioma:** Permite seleccionar el idioma del texto en la imagen (Español, Inglés, Francés, Alemán, Italiano, Portugués por defecto, extensible).
*   **Formatos de Imagen Soportados:** PNG, JPG, JPEG, GIF, BMP, TIFF.
*   **Preprocesamiento de Imágenes:**
    *   Conversión automática a escala de grises.
    *   Binarización con umbral (actualmente fijado en `150` en `app.py`) para mejorar la legibilidad del texto para el OCR.
*   **Interfaz Intuitiva:**
    *   Carga de archivos mediante selección o arrastrar y soltar (drag & drop).
    *   Validación de archivos en el frontend (tipo y tamaño máximo de 16MB) con mensajes de error claros y accesibles.
    *   Previsualización de la imagen cargada en la página de resultados.
    *   Editor de texto para el contenido extraído con opciones de "Seleccionar todo", "Copiar" y "Descargar como .txt".
    *   Indicador del idioma utilizado para el OCR en la página de resultados.
*   **Accesibilidad Mejorada:**
    *   Enlaces "Saltar al contenido principal" (Skip Links) para navegación por teclado eficiente.
    *   Uso semántico de HTML y atributos ARIA para compatibilidad con lectores de pantalla.
    *   Controles accesibles por teclado y con indicadores de foco claros.
    *   Indicador de carga visual y semántico (`aria-busy`).
    *   Mensajes de error y notificaciones en regiones `alert` para retroalimentación inmediata.
*   **Modo Oscuro:** Soporte para el esquema de color preferido del sistema, adaptando la interfaz automáticamente.
*   **100% Local y Gratuito:** Sin límites de uso, sin necesidad de conexión a internet para el procesamiento OCR.

## Requisitos Previos

*   **Python:** Versión 3.7 o superior.
*   **Tesseract OCR:** Debe estar instalado en tu sistema.
*   **pip:** Para la gestión de paquetes de Python.

## Instalación y Ejecución

1.  **Clona el Repositorio:**
    ```bash
    git clone https://github.com/GamaHerrera/Textify.git # Asegúrate que esta sea la URL correcta de tu repositorio
    cd Textify
    ```

2.  **Crea y Activa un Entorno Virtual (Recomendado):**
    *   En macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   En Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Instala las Dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Instala Tesseract OCR (si aún no lo has hecho):**
    *   **Windows:** Descarga el instalador desde [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki). Durante la instalación, asegúrate de incluir los paquetes de idioma que necesites y considera añadir Tesseract al PATH del sistema.
    *   **macOS:**
        ```bash
        brew install tesseract
        brew install tesseract-lang # Para instalar todos los paquetes de idioma disponibles
        ```
    *   **Linux (Ubuntu/Debian):**
        ```bash
        sudo apt update
        sudo apt install tesseract-ocr
        # Para instalar paquetes de idioma específicos (ej. español, francés, alemán):
        sudo apt install tesseract-ocr-spa tesseract-ocr-fra tesseract-ocr-deu
        # O para todos los idiomas disponibles (puede ser grande):
        # sudo apt install tesseract-ocr-all
        ```

5.  **Configura la Aplicación (Ruta de Tesseract):**
    *   Textify intentará encontrar Tesseract automáticamente si está en el PATH del sistema.
    *   Si Tesseract no está en el PATH, o si deseas especificar una instalación particular, crea un archivo llamado `config.py` en la raíz del proyecto (junto a `app.py`).
    *   Añade la siguiente línea a `config.py`, ajustando la ruta según tu instalación:
        ```python
        # config.py
        TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Ejemplo para Windows
        # En macOS/Linux, si tesseract está en el PATH, esta línea no es necesaria o puede ser:
        # TESSERACT_PATH = '/usr/local/bin/tesseract' # Ejemplo de ruta común en macOS con Homebrew
        ```

6.  **Ejecuta la Aplicación:**
    ```bash
    python app.py
    ```

7.  **Abre tu Navegador:**
    Visita [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Estructura del Proyecto

```
Textify/
├── app.py                # Lógica principal de la aplicación Flask
├── config.py             # (Opcional) Configuración de la ruta de Tesseract
├── requirements.txt      # Dependencias de Python
├── static/               # Archivos estáticos (CSS, JS, imágenes base)
│   ├── styles.css
│   └── ...
├── templates/            # Plantillas HTML (Jinja2)
│   ├── index.html
│   ├── result.html
│   ├── 404.html
│   ├── 500.html
├── uploads/              # Directorio para imágenes cargadas (creado automáticamente)
├── venv/                 # Entorno virtual (si se crea)
└── README.md             # Este archivo
└── LICENSE               # Archivo de licencia MIT
```

## Tecnologías Utilizadas

*   **Backend:**
    *   [Python](https://www.python.org/)
    *   [Flask](https://flask.palletsprojects.com/): Microframework web.
    *   [Pytesseract](https://github.com/madmaze/pytesseract): Wrapper de Python para Tesseract OCR.
    *   [Pillow (PIL Fork)](https://python-pillow.org/): Biblioteca para manipulación de imágenes.
    *   [python-magic-bin](https://pypi.org/project/python-magic-bin/): Para la detección de tipos MIME de archivos (principalmente para Windows).
*   **Frontend:**
    *   HTML5 (semántico y accesible)
    *   CSS3 (con variables CSS para theming y modo oscuro)
    *   JavaScript (Vanilla JS, sin frameworks pesados)
*   **OCR Engine:**
    *   [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
*   **Iconografía:**
    *   [Font Awesome](https://fontawesome.com/)

## Solución de Problemas Comunes

*   **`TesseractNotFoundError` o `pytesseract.TesseractNotFoundError`**: 
    *   Asegúrate de que Tesseract OCR esté instalado correctamente en tu sistema.
    *   Verifica que la ruta a `tesseract.exe` (o el ejecutable de Tesseract) esté correctamente configurada en `config.py` (si lo usas) o que Tesseract esté en el PATH del sistema.
*   **Resultados de OCR Pobres:**
    *   Asegúrate de seleccionar el idioma correcto para el texto en la imagen.
    *   La calidad de la imagen de entrada es crucial. Imágenes borrosas, con poca luz, con fuentes muy estilizadas o con bajo contraste pueden ser difíciles de procesar.
    *   El preprocesamiento (escala de grises y binarización) ayuda, pero no puede resolver todos los problemas de calidad de imagen.
*   **Errores de Permiso (al guardar archivos en `uploads/`):**
    *   Asegúrate de que la aplicación tenga permisos de escritura en el directorio `uploads/` dentro de la carpeta del proyecto.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar Textify:
1.  Haz un Fork del proyecto.
2.  Crea una nueva rama para tu característica (`git checkout -b feature/AmazingFeature`).
3.  Realiza tus cambios y haz commit (`git commit -m 'Add some AmazingFeature'`).
4.  Haz Push a la rama (`git push origin feature/AmazingFeature`).
5.  Abre un Pull Request.

## Licencia

Este proyecto está distribuido bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.

## Agradecimientos

*   A la comunidad de [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) por su increíble motor de reconocimiento.
*   A los desarrolladores de [Flask](https://flask.palletsprojects.com/), [Pillow](https://python-pillow.org/), y otras bibliotecas de código abierto utilizadas.

---

Desarrollado con ❤️ por Gamaliel Herrera - 2025
