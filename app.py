import os
from flask import Flask, flash, jsonify, request
#, redirect, url_for
#from werkzeug.utils import secure_filename

import pdftotext
import tempfile

#UPLOAD_FOLDER = '/tmp'
#ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
#app.config['JSON_SORT_KEYS'] = False
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def dummy():
    response_dict = {}
    response_dict['status'] = 'ok'
    #response_dict['msg'] = 'POST on /upload'
    return jsonify(response_dict)


@app.route('/upload', methods=['POST'])
def pdf_to_text():
    """ 
    Convert pdf file to text file

    """

    response_dict = {}

    if request.method == 'POST':
        (fd, filename) = tempfile.mkstemp()
        try:
            with os.fdopen(fd, "wb") as fp:
                fp.write(request.data)
                
            # Read pdf text, Load your PDF
            with open(filename, "rb") as fp:
                pdf = pdftotext.PDF(fp)

                response_dict["page_count"] = len(pdf)
                response_dict["pages"] = []
                for page in pdf:
                    response_dict["pages"].append(page)

            response_dict['status'] = 'ok'
        except Exception as e:
            print(str(e))
        finally:
            os.remove(filename)
    else:
        response_dict['status'] = 'failed'      

    return jsonify(response_dict)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    os.environ["FLASK_ENV"] = "development"
    app.run()
