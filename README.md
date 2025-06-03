# Textify - Extracción de texto de imágenes (OCR) Local

![Textify Logo](https://img.icons8.com/color/96/000000/text.png)

Textify es una aplicación web gratuita y de código abierto que permite extraer texto de imágenes utilizando tecnología OCR (Reconocimiento Óptico de Caracteres). Con una interfaz intuitiva y fácil de usar, Textify convierte cualquier imagen con texto en texto editable en cuestión de segundos.

## Características ✨

- **Totalmente gratuito**: Sin suscripciones ni límites de uso
- **Fácil de usar**: Interfaz intuitiva con arrastrar y soltar
- **Rápido**: Procesamiento en segundos
- **Preciso**: Soporte para múltiples idiomas
- **Privado**: Las imágenes se procesan en tu navegador
- **Sin registro**: Comienza a usar sin necesidad de crear una cuenta
- **Accesible**: Diseñado pensando en la accesibilidad

## Cómo usar 🚀

1. **Sube una imagen** arrastrándola al área designada o haciendo clic en "Seleccionar archivo"
2. **Espera** a que Textify procese la imagen (solo unos segundos)
3. **Copia** el texto extraído o **descárgalo** como archivo de texto

### Formatos soportados
- **Imágenes**: JPG, PNG, GIF, BMP, TIFF
- **Idiomas**: Soporte para múltiples idiomas (inglés, español, francés, alemán, y más)

## Tecnologías utilizadas 🛠️

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python con Flask
- **OCR**: Tesseract OCR
- **Diseño**: Responsivo y accesible

## Instalación local 💻

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
