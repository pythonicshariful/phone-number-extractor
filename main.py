import os
import re
import csv
import shutil
from PIL import Image
import pytesseract
from tqdm import tqdm

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

input_folder = "images"
success_folder = "success"
failed_folder = "failed"
csv_file = "numbers.csv"

os.makedirs(success_folder, exist_ok=True)
os.makedirs(failed_folder, exist_ok=True)

if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Phone Number", "Source File"])

files = [f for f in os.listdir(input_folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

for filename in tqdm(files, desc="Processing images", unit="file"):
    file_path = os.path.join(input_folder, filename)
    try:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
        numbers = re.findall(r"\+\d[\d\s-]+", text)
        numbers = [re.sub(r"[^\d+]", "", num) for num in numbers]

        if numbers:
            with open(csv_file, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                for num in numbers:
                    writer.writerow([num, filename])
            shutil.move(file_path, os.path.join(success_folder, filename))
        else:
            shutil.move(file_path, os.path.join(failed_folder, filename))
    except Exception:
        shutil.move(file_path, os.path.join(failed_folder, filename))

print("🎯 Processing complete.")
