from model import *
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/upload' # Diretório que será salvo

@app.route( '/', methods=["GET", "POST"] )
def index( ):
    
    image = 'nothing'

    return render_template( 'index.html', image = image )

@app.route('/upload', methods=['POST'])
def upload():
    pic = request.files['file']
    
    if not pic:
        return 'No pic uploaded!', 400
    
    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype

    if not filename or not mimetype:
        return 'Bad upload!', 400

    pic.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(pic.filename)))

    return redirect( url_for('predict',filename = filename) )

@app.route('/predict/<filename>', methods = ['GET'] )
def predict( filename ):
    results = pred( str(filename) )
    results = {key: round(value * 100, 2) for key, value in results.items()}
    #print(results)

    image = f'/static/upload/{filename}'

    return render_template( 'predict.html', results = results, image = image )


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug = False)
    #app.run(debug=True)
