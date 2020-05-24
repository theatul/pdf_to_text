import os
from flask import Flask, flash, jsonify, request
import pdftotext
import tempfile


app = Flask(__name__)


@app.route('/getpdftext', methods=['POST'])
def pdf_to_text():
    """ 
    Convert pdf file to text file

    """

    response_dict = {}
    response_dict['status'] = 'failed'

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
            response_dict['error'] = str(e)
        finally:
            os.remove(filename)
    else:
        response_dict['error'] = 'Method not supported'      

    return jsonify(response_dict)
    
"""
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    os.environ["FLASK_ENV"] = "development"
    app.run()
"""