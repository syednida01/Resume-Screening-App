# 🧠 Resume Screening App

A smart, ML-powered web application that automatically classifies resumes into job categories such as Data Scientist, Java Developer, HR, etc. — built using **Streamlit**, **Scikit-learn**, **PyMuPDF**, and **NLP techniques**.

---

## 📌 Features

- 📄 Upload resumes in `.pdf` or `.txt` format
- 🔍 Automatically cleans and processes resume content
- 🤖 Predicts the most relevant job category using a trained ML model
- 💡 Supports 25+ job domains including:
  - Data Science
  - Python Developer
  - Java Developer
  - SAP Developer
  - HR, DevOps, and more

---

## 🚀 Technologies Used

| Area            | Tools & Libraries                          |
|------------------|--------------------------------------------|
| Web Interface    | Streamlit                                 |
| Text Processing  | Regex, NLTK (`stopwords`, `punkt`)         |
| ML Model         | Scikit-learn (`TfidfVectorizer`, classifier)|
| PDF Handling     | PyMuPDF (`fitz`) for robust text extraction |
| Serialization    | Pickle (`clf.pkl`, `tfidf.pkl`)            |

---

## ⚙️ How It Works

1. User uploads a `.pdf` or `.txt` resume
2. Text is extracted and cleaned (remove URLs, symbols, non-ASCII chars, etc.)
3. Resume is transformed using **TF-IDF vectorization**
4. A pre-trained ML classifier predicts the resume category
5. The result is displayed on the UI

---

## 📁 Folder Structure

.
├── app.py # Main Streamlit app
├── clf.pkl # Trained classification model
├── tfidf.pkl # TF-IDF vectorizer
├── README.md # Project documentation


---

## 📦 Requirements

Install dependencies with:
```bash
pip install -r requirements.txt
```

You can manually install:
```bash
pip install streamlit scikit-learn nltk PyMuPDF
```

▶️ Run the App
```bash
streamlit run app.py
```
Then open http://localhost:8501 in your browser.



👩‍💻 Author
Syed Nida Ali  
🔗 [GitHub](https://github.com/syednida01) | 📧 [syednidaali07861@gmail.com](mailto:syednidaali07861@gmail.com)
