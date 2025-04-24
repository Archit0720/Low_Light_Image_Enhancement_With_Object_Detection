# detector.py
from PIL import Image, ImageEnhance
from ultralytics import YOLO
import os

def enhance_image(img_path):
    img = Image.open(img_path).convert("RGB")
    img = ImageEnhance.Brightness(img).enhance(1.8)
    img = ImageEnhance.Contrast(img).enhance(1.5)
    img = ImageEnhance.Sharpness(img).enhance(1.2)
    img = ImageEnhance.Color(img).enhance(1.1)
    enhanced_path = os.path.join("static/uploads", "enhanced.jpg")
    img.save(enhanced_path)
    return enhanced_path

def detect_objects(img_path):
    model = YOLO("yolov8n.pt")  # or yolov8s.pt, etc.
    results = model(img_path)
    result_path = os.path.join("static/uploads", "detection_result.jpg")
    results[0].save(filename=result_path)
    return result_path
