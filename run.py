from model import *
from flask import Flask, render_template


# LOAD MODEL TRAINED

app = Flask(__name__)

@app.route( '/', methods=["GET", "POST"] )
def index( ):

    print( pred('croc.jpg') )

    return render_template( 'index.html' )

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port, debug = False)
    app.run(debug=True)