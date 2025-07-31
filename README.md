# 🌸 Iris Flower Classifier

A simple, beautiful Iris Flower Classification web app built with **FastAPI** and **vanilla HTML/CSS/JS**.  
Classify Iris species by entering **sepal** and **petal** measurements and instantly see the predicted flower along with its image!

---

## 🌐 Demo

![App Screenshot](static/Iris%20Versicolor.jpg)

---

## 🚀 Features

- ✅ **FastAPI backend** serving a trained ML model (`iris_model.pkl`)
- 🔍 Predicts between **Iris Setosa**, **Iris Versicolor**, and **Iris Virginica**
- 🌙 **Dark-themed**, modern, responsive frontend (Bootstrap-powered)
- 🖼️ Displays an image of the predicted species
- ⚡ Easy local setup and instant feedback

---

## 📁 Directory Structure

IRIS/
├── main.py # FastAPI backend
├── iris_model.pkl # Trained scikit-learn model
├── index.html # Frontend HTML page
├── static/ # Flower images directory
│ ├── Iris Setosa.jpg
│ ├── Iris Versicolor.jpg
│ └── Iris Virginica.jpg


---

## 🛠️ Setup Instructions

1. **Clone the repository** or download the files:

   ```bash
   git clone https://github.com/yourusername/iris-flower-classifier.git
   cd iris-flower-classifier

2. **Install dependencies**:

    pip install -r requirements.txt

3. **Verify file structure**:

    main.py, iris_model.pkl, and index.html are in the root directory.
    Images are inside the static/ folder with exact matching names.

4. **Run the app using --Uvicorn**:

    uvicorn main:app --reload

5. **Open in browser**:

    Go to http://localhost:8000 to access the web app.

## 🧠 Backend API

**GET /**
Serves the frontend HTML.

**POST /predict**
Accepts a JSON input like:

json
Copy
Edit
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
Returns:

json
Copy
Edit
{
  "species": "Iris Setosa",
  "image": "Iris Setosa.jpg"
}


## 📜 License

Licensed under the MIT License – free to use, modify, and share.

Happy classifying! 🌸
Made with 💜 by Shashank