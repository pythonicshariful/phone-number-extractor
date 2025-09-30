# Phone Number Extractor from Images

This Python script uses **Tesseract OCR** and **Regex** to extract phone numbers from images.  
It processes all images inside an `images` folder and saves results into a CSV file.  

- ✅ If phone numbers are found → image is moved to `success/`  
- ❌ If no phone number or error → image is moved to `failed/`  
- 📊 A `numbers.csv` file is generated with extracted numbers and source filenames.  
- 🔄 The main `images` folder will be emptied after processing.  

---

## 📂 Folder Structure

```
project/
│── main.py
│── README.md
│── numbers.csv (generated automatically)
│── images/        # put your input images here
│── success/       # created automatically
│── failed/        # created automatically
```

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pythonicshariful/phone-number-extractor.git
   cd phone-number-extractor
   ```



2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install **Tesseract OCR**:
   - Windows: [Download here](https://github.com/tesseract-ocr/tesseract/wiki)
   - Linux (Ubuntu/Debian):
     ```bash
     sudo apt install tesseract-ocr
     ```
   - macOS (Homebrew):
     ```bash
     brew install tesseract
     ```

5. Update the path to `tesseract.exe` inside `main.py` if needed:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

---

## ▶️ Usage

1. Place your images inside the `images/` folder.  
   Supported formats: `.png`, `.jpg`, `.jpeg`

2. Run the script:
   ```bash
   python main.py
   ```

3. Results:
   - Extracted phone numbers → `numbers.csv`
   - Successfully processed images → `success/`
   - Failed images → `failed/`

---

## 🛠 Requirements

- Python 3.8+
- Tesseract OCR
- Python libraries:
  ```txt
  pillow
  pytesseract
  tqdm
  ```

Install them with:
```bash
pip install pillow pytesseract tqdm
```

---

## 📜 License
MIT License
