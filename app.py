from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image, UnidentifiedImageError
import magic

# Configuración de la aplicación
app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-para-desarrollo'  # Cambia esto en producción
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}

LANGUAGE_NAMES = {
    'spa': 'Español',
    'eng': 'Inglés',
    'fra': 'Francés',
    'deu': 'Alemán',
    'ita': 'Italiano',
    'por': 'Portugués',
    # Añadir más mapeos si se agregan más idiomas al frontend
}

# Asegurarse de que el directorio de subidas exista
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configurar la ruta de Tesseract
# En Windows, la ruta típica es:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Si no funciona, el usuario deberá ajustar esta ruta

# Inicializar la verificación de tipos MIME
try:
    mime = magic.Magic(mime=True)
except Exception:
    mime = None
    print("Advertencia: No se pudo inicializar la verificación MIME. La validación de tipos de archivo estará limitada.")

def allowed_file(filename):
    """Verifica si el archivo tiene una extensión permitida."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def verify_file_type(file):
    """Verifica el tipo MIME real del archivo."""
    if not mime:
        return True  # Si no se pudo inicializar magic, omitir la verificación
    
    try:
        # Guardar la posición actual del archivo
        current_pos = file.tell()
        file.seek(0)
        
        # Leer solo los primeros bytes para la verificación MIME
        file_header = file.read(2048)
        file.seek(current_pos)  # Volver a la posición original
        
        mime_type = mime.from_buffer(file_header)
        return mime_type.startswith(('image/jpeg', 'image/png', 'image/gif', 'image/bmp', 'image/tiff'))
    except Exception:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Verificar que se haya enviado un archivo
    if 'file' not in request.files:
        flash('No se seleccionó ningún archivo', 'error')
        return redirect(request.url)
    
    file = request.files['file']
    selected_language = request.form.get('language', 'spa') # Obtener idioma, por defecto 'spa'
    
    # Verificar que el archivo tenga un nombre
    if file.filename == '':
        flash('No se seleccionó ningún archivo', 'error')
        return redirect(request.url)
    
    # Verificar que el archivo tenga una extensión permitida
    if not file or not allowed_file(file.filename):
        flash('Tipo de archivo no permitido. Solo se permiten imágenes (PNG, JPG, JPEG, GIF, BMP, TIFF).', 'error')
        return redirect(request.url)
    
    # Verificar el tipo MIME real del archivo
    if not verify_file_type(file):
        flash('El archivo no parece ser una imagen válida.', 'error')
        return redirect(request.url)
    
    try:
        # Generar un nombre de archivo seguro
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Asegurarse de que el nombre del archivo sea único
        counter = 1
        name, ext = os.path.splitext(filename)
        while os.path.exists(filepath):
            filename = f"{name}_{counter}{ext}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            counter += 1
        
        # Guardar el archivo
        file.save(filepath)
        
        # Establecer permisos seguros (solo el propietario puede leer/escribir)
        os.chmod(filepath, 0o600)
        
        # Verificar que el archivo sea una imagen válida antes de procesar
        try:
            img = Image.open(filepath)
            # Verificar que la imagen se pueda cargar correctamente
            img.verify()
            img_pil = Image.open(filepath)  # Necesario después de verify()
        except (IOError, UnidentifiedImageError) as e:
            # Eliminar el archivo si no es una imagen válida
            if os.path.exists(filepath):
                os.remove(filepath)
            flash('El archivo no es una imagen válida o está dañado.', 'error')
            return redirect(request.url)
        
        try:
            # Preprocesamiento de la imagen
            # 1. Convertir a escala de grises
            img_gray = img_pil.convert('L')

            # 2. Aplicar binarización (umbralización)
            threshold_value = 150  # Ajusta este valor (0-255) según sea necesario
            img_binarized = img_gray.point(lambda x: 0 if x < threshold_value else 255, '1')
            
            # Procesar la imagen binarizada con Tesseract
            app.logger.info(f"Procesando imagen con Tesseract. Idioma: {selected_language}, Umbral: {threshold_value}")
            text = pytesseract.image_to_string(img_binarized, lang=selected_language)
            app.logger.info(f"Texto extraído con éxito para '{filename}' en idioma '{selected_language}'.")

            language_display_name = LANGUAGE_NAMES.get(selected_language, selected_language.capitalize())

            return render_template('result.html', 
                                 image_path=os.path.join('uploads', secure_filename(filename)), 
                                 extracted_text=text,
                                 ocr_language=language_display_name)
        
        except pytesseract.TesseractNotFoundError:
            if os.path.exists(filepath):
                os.remove(filepath)
            app.logger.error('Tesseract no encontrado. Verifica la instalación y el PATH.')
            flash('Error de OCR: Tesseract no está instalado o configurado correctamente. Consulta el README para obtener ayuda.', 'error')
            return redirect(request.url)
        except pytesseract.TesseractError as te:
            if os.path.exists(filepath):
                os.remove(filepath)
            app.logger.error(f'Error de Tesseract al procesar la imagen: {str(te)}')
            flash(f'Error de OCR: {str(te)}. Asegúrate de que los datos de idioma para "{selected_language}" ({pytesseract.get_languages(config="")[selected_language] if selected_language in pytesseract.get_languages(config="") else "Nombre Desconocido"}) estén instalados.', 'error')
            return redirect(request.url)
        except Exception as e:
            if os.path.exists(filepath):
                os.remove(filepath)
            app.logger.error(f'Error inesperado al procesar la imagen: {str(e)}', exc_info=True)
            flash('Ocurrió un error inesperado al procesar la imagen. Por favor, inténtalo de nuevo.', 'error')
            return redirect(request.url)
            
    except Exception as e:
        print(f'Error en la carga del archivo: {str(e)}')
        flash('Ocurrió un error al cargar el archivo. Por favor, inténtalo de nuevo.', 'error')
        return redirect(request.url)

# Manejador de errores 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Manejador de errores 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Ejecutar la aplicación en modo desarrollo
    print("\n¡Bienvenido a Textify!")
    print("La aplicación se está ejecutando en http://127.0.0.1:5000")
    print("Presiona Ctrl+C para detener la aplicación\n")
    app.run(debug=True)
