from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Asegurarse de que el directorio de subidas exista
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configurar la ruta de Tesseract (puedes ajustar esto según tu instalación)
# En Windows, podría ser algo como: r'C:\Program Files\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\GamalielHerr_p61vz\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extraer texto de la imagen
        try:
            img = Image.open(filepath)
            text = pytesseract.image_to_string(img, lang='spa')
            return render_template('result.html', 
                                image_path=filepath,
                                extracted_text=text)
        except Exception as e:
            return f"Error al procesar la imagen: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
