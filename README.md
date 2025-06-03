# Textify - Extracción de texto de imágenes (OCR) Local

![Textify Logo](https://img.icons8.com/color/96/000000/text.png)

Textify es una aplicación web gratuita y de código abierto que permite extraer texto de imágenes utilizando tecnología OCR (Reconocimiento Óptico de Caracteres). Con una interfaz intuitiva y fácil de usar, Textify convierte cualquier imagen con texto en texto editable en cuestión de segundos.

- Python 3.7 o superior
- Tesseract OCR instalado en tu sistema

## Instalación en Windows

1. **Instala Tesseract OCR**:
   - Descarga el instalador desde [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
   - Ejecuta el instalador y anota la ruta de instalación (por defecto: `C:\Program Files\Tesseract-OCR\tesseract.exe`)

2. **Clona o descarga este repositorio**

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Configura la ruta de Tesseract** (si es necesario):
   - Abre `app.py` y actualiza la ruta en la línea:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
     ```

2. **Ejecuta la aplicación**:
   ```bash
   python app.py
   ```

3. **Abre tu navegador** en [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Características

- Extrae texto de imágenes con un solo clic
- Soporta múltiples formatos: JPG, PNG, GIF, BMP, TIFF
- Interfaz intuitiva y fácil de usar
- Procesamiento local (tus imágenes no salen de tu computadora)
- Sin límite de uso

## Solución de problemas

Si la aplicación no funciona:
1. Verifica que Tesseract esté instalado correctamente
2. Asegúrate de que la ruta en `app.py` sea correcta
3. Revisa la consola para mensajes de error

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## Tecnologías utilizadas 

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python con Flask
- **OCR**: Tesseract OCR
- **Diseño**: Responsivo y accesible

## Instalación local 

Si deseas ejecutar Textify en tu máquina local, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/textify.git
   cd textify
   ```

2. Crea y activa un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: .\venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Asegúrate de tener Tesseract OCR instalado:
   - **Windows**: Descarga e instala desde [aquí](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux (Ubuntu/Debian)**: `sudo apt install tesseract-ocr`

5. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

6. Abre tu navegador y ve a `http://127.0.0.1:5000`

## Contribuir 🤝

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar Textify, por favor:

1. Haz un fork del proyecto
2. Crea una rama con tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Licencia 📄

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Soporte 🆘

Si encuentras algún problema o tienes alguna pregunta, por favor [abre un issue](https://github.com/tuusuario/textify/issues).

## Agradecimientos 🙏

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) por la potente herramienta de OCR
- [Flask](https://flask.palletsprojects.com/) por el framework web minimalista
- [Font Awesome](https://fontawesome.com/) por los increíbles iconos

---

Desarrollado con ❤️ por Gamaliel Herrera - [2025]
