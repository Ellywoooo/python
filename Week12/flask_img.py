from flask import Flask, render_template_string, request
import os # Flask app save uploaded files to the correct folder on computer

app = Flask(__name__)

# Sets the folder where uploaded images will be saved.
# The static folder is a common place to store static files like images.
UPLOAD_FOLDER = 'static/uploads'
# Check the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# Stores the upload folder path in the Flask app configuration.
# This allows the app to access the upload folder easily.
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
'''
Develop a Flask web application that allows users to upload an image
and display it on the browser. Share your GitHub link and screenshot of your result.
'''
# The main route handles both GET and POST requests.
# "/" route accepts GET and POST methods.
@app.route("/", methods=["GET", "POST"])
def img():
    
    # GET method is the default method when a user first visits the page.
    if request.method == "GET":
        # If the request method is GET, render the upload form(first time).
        # Display the form for uploading an image.
        return render_template_string("""
            <h1 style="font-family:sans-serif;color:#2c3e50;">Please upload an image</h1>
            <form method="post" enctype="multipart/form-data" style="background:#f4f4f4;padding:30px;border-radius:10px;box-shadow:0 2px 8px #ccc;display:inline-block;">
                <input type="file" name="image" accept="image/*" required style="margin-bottom:15px;padding:8px;border-radius:5px;border:1px solid #ccc;">
                <br>
                <button type="submit" style="background:#3498db;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:16px;cursor:pointer;transition:background 0.3s;">
                    &#128247; Upload Photo
                </button>
            </form>
        """)
    # If the request method is POST, it means an image has been uploaded.
    elif request.method == "POST":
        # Retrieves the uploaded file from the request.
        file = request.files['image']
        # if a file is provided, save it to the upload folder.
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            # After saving file, display a success message with the uploaded image.
            return render_template_string("""
                <h1>Image Uploaded!</h1>
                <img src="{{ url_for('static', filename='uploads/' + filename) }}" style="max-width:300px;max-height:300px;">
            """, filename=file.filename)


if __name__ == "__main__":
    app.run(debug=True)