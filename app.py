from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import base64
import sys
from io import BytesIO
from helpers import *
from model import *

app = Flask(__name__)
app.secret_key = "mohamed"
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
	""" Upload image only """
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in set(['png', 'jpg', 'jpeg'])
	
@app.route('/')
def upload_form():
	return render_template('base.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
			
		file = request.files['file']
		cluters_number = int(request.form['number'])
		#print(f'{type(cluters_number)}', file=sys.stderr)
		byte_file = file.read()  ## byte file
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
			
		if file and allowed_file( file.filename ):
			filename = secure_filename(file.filename)
			#flash( f"File Name {filename}" )
			image = GetImage(byte_file)
			image_colors_on_image, image_colors_pie = Model(image, cluters_number).final
			image_colors_on_image, image_colors_pie = PostImage(image_colors_on_image), PostImage(image_colors_pie)

			return render_template(
				'submit.html',
				image_colors_on_image = image_colors_on_image,
				image_colors_pie = image_colors_pie
			)
		else:
			flash( 'Allowed file types are Images' )
			return redirect(request.url)

if __name__ == "__main__":
	app.debug = True
	app.run()