import streamlit as st
import pickle
import re
import nltk
import fitz

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')

nltk.download('punkt')
nltk.download('stopwords')

#loading models
clf = pickle.load(open('clf.pkl', 'rb'))
tfidfd = pickle.load(open('tfidf.pkl', 'rb'))

#clean resume
def cleanResume(txt):
    cleanTxt = re.sub('http\S+\s' ,' ' , txt)
    cleanTxt = re.sub('RT|CC' ,' ' , cleanTxt)
    cleanTxt = re.sub('#\S+\s' ,' ' , cleanTxt)
    cleanTxt = re.sub('@\S+' ,' ' , cleanTxt)
    cleanTxt = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""),' ' , cleanTxt)
    cleanTxt = re.sub(r'[^\x00-\x7f]',' ' , cleanTxt)
    cleanTxt = re.sub('\s+' ,' ' , cleanTxt)

    return cleanTxt


def extract_text_from_pdf(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text


#web app
def main():
    st.title("Resume Screening App")
    uploaded_file = st.file_uploader('Upload Resume' , type=['txt','pdf'])

    if uploaded_file is not None:
        resume_txt = extract_text_from_pdf(uploaded_file)

        cleaned_resume = cleanResume(resume_txt)
        transformed_resume = tfidfd.transform([cleaned_resume])
        prediction_id = clf.predict(transformed_resume)[0]


        #map category ID to category name
        category_mapping={
            6 :'Data Science', 
            12 :'HR',
            0 :'Advocate',
            1 : 'Arts',
            24 : 'Web Designing',
            16 : 'Mechanical Engineer',
            22 : 'Sales',
            14 : 'Health and fitness',
            5 : 'Civil Engineer',
            15 : 'Java Developer',
            4 : 'Business Analyst',
            21 : 'SAP Developer',
            2 : 'Automation Testing',
            11 : 'Electrical Engineering',
            18 : 'Operations Manager',
            20 : 'Python Developer',
            8 :'DevOps Engineer',
            17 : 'Network Security Engineer',
            19 : 'PMO',
            7 : 'Database',
            13 : 'Hadoop',
            10 : 'ETL Developer',
            9 : 'DotNet Developer',
            3 : 'Blockchain',
            23 : 'Testing',
        }

        category_name = category_mapping.get(prediction_id , "unknown")
        st.write("Predicted Category:" , category_name)

#pythoon main
if __name__ == "__main__":
    main()