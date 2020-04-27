from flask import Flask,request,jsonify
from PIL import Image

app = Flask(__name__)

@app.route("/")
def index():
    read = """For post request go /image and send file as 
    files = {'media': file}
     """
    return read

@app.route("/image", methods=["POST"])
def image():
    img = request.files['media']
    image = Image.open(img)
    
    pixels = list(image.getdata())
    width, height = image.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    
    return jsonify(pixels[0],image.size)

if __name__ == "__main__":
    app.run(debug=True)