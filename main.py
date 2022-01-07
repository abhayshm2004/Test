from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return '<b>file uploaded successfully</b><br><a href="/">Go Back</a>'

if __name__ == '__main__':
   app.run(port=8080, host='0.0.0.0')
