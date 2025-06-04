# Textify - Extracción de Texto de Imágenes (OCR) Local

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-2.3.3-orange.svg)](https://flask.palletsprojects.com/)
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

*   **Python:** Versión 3.12 o superior.
*   **Tesseract OCR:** Debe estar instalado en tu sistema con los paquetes de idioma necesarios.
*   **pip:** Para la gestión de paquetes de Python.
*   **Sistema Operativo:** Windows 10/11, macOS, o Linux (probado en Windows 11).

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
    *   **Windows:**
        1. Descarga el instalador desde [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
        2. **IMPORTANTE:** Durante la instalación, asegúrate de marcar la opción "Añadir al PATH del sistema"
        3. Selecciona los paquetes de idioma que necesites (español, inglés, etc.)
        4. Si olvidaste instalar los idiomas, puedes descargarlos manualmente desde [tessdata_best](https://github.com/tesseract-ocr/tessdata_best) y copiarlos a `C:\Program Files\Tesseract-OCR\tessdata\`
    
    *   **macOS:**
        ```bash
        # Instalar Tesseract
        brew install tesseract
        
        # Instalar todos los paquetes de idioma disponibles
        brew install tesseract-lang
        ```
    
    *   **Linux (Ubuntu/Debian):**
        ```bash
        # Actualizar e instalar Tesseract
        sudo apt update
        sudo apt install tesseract-ocr
        
        # Instalar paquetes de idioma específicos
        sudo apt install tesseract-ocr-spa tesseract-ocr-eng tesseract-ocr-fra tesseract-ocr-deu tesseract-ocr-ita tesseract-ocr-por
        
        # Instalar todos los idiomas disponibles (opcional, ocupa más espacio)
        # sudo apt install tesseract-ocr-all
        ```

5. **Configura la variable de entorno TESSDATA_PREFIX (Solo Windows si es necesario):**
   - Abre el Panel de control > Sistema > Configuración avanzada del sistema > Variables de entorno
   - En "Variables del sistema", busca o crea una nueva variable llamada `TESSDATA_PREFIX`
   - Establécelo como `C:\Program Files\Tesseract-OCR`
   - Reinicia tu terminal o IDE después de hacer estos cambios

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
    *   Verifica que la ruta a `tesseract.exe` (o el ejecutable de Tesseract) esté correctamente configurada en `config.py` o que Tesseract esté en el PATH del sistema.
    *   En Windows, verifica que la ruta en `app.py` coincida con tu instalación de Tesseract.

*   **Error de carga de idioma (ej: `Error opening data file .../tessdata/spa.traineddata`):**
    *   Verifica que los archivos de idioma (`.traineddata`) estén en la carpeta `tessdata` dentro del directorio de instalación de Tesseract.
    *   Asegúrate de que la variable de entorno `TESSDATA_PREFIX` esté configurada correctamente.
    *   Los archivos de idioma deben tener permisos de lectura.

*   **Resultados de OCR Pobres:**
    *   Selecciona el idioma correcto para el texto en la imagen.
    *   Mejora la calidad de la imagen: buena iluminación, enfoque adecuado y contraste suficiente.
    *   Imágenes con resolución de al menos 300 DPI funcionan mejor.
    *   Evita imágenes borrosas, con poca luz o con fuentes estilizadas.

*   **Errores de Permiso (al guardar archivos en `uploads/`):**
    *   Asegúrate de que la aplicación tenga permisos de escritura en el directorio `uploads/`.
    *   En Windows, ejecuta el IDE o terminal como administrador si es necesario.

*   **Problemas con Python 3.12:**
    *   Asegúrate de usar las versiones más recientes de las dependencias como se especifica en `requirements.txt`.
    *   Si encuentras problemas con `python-magic-bin`, prueba instalando `python-magic` en su lugar.

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
