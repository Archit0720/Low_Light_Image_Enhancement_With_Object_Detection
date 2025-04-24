# app.py
from flask import Flask, render_template, request, redirect, url_for
from detector import enhance_image, detect_objects
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle uploaded image
        image = request.files["image"]
        if image:
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], "original.jpg")
            image.save(image_path)

            # Enhance and detect
            enhanced_path = enhance_image(image_path)
            detection_path = detect_objects(enhanced_path)

            return render_template("index.html",
                                   original_image="uploads/original.jpg",
                                   enhanced_image="uploads/enhanced.jpg",
                                   detected_image="uploads/detection_result.jpg")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
