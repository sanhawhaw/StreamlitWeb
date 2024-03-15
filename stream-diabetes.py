import pickle

from st_on_hover_tabs import on_hover_tabs
import streamlit as st
from streamlit_back_camera_input import back_camera_input
#from streamlit_tesseract_scanner import tesseract_scanner
from streamlit_autorefresh import st_autorefresh


#membace model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))


st.set_page_config(layout="wide")
#st.header("Custom tab component for on-hover navigation bar")
st.markdown('<style>' + open('./Style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Diabetes', 'Camera','Report'], 
                         iconName=['home', 'settings_accessibility','photo_camera','dashboard'], default_choice=0)

if tabs =='Home':
    st.title("Home")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Diabetes':
    st.title("Diabetes Prediction")
    st.write('Name of option is {}'.format(tabs))
    col1,col2 = st.columns(2)

    with col1 :
        Pregnancies = st.text_input ('Pregnancies')
        Glucose = st.text_input ('Glucose')
        BloodPreasure = st.text_input ('Blood Preasure')
        SkinTickness = st.text_input ('Skin Tickness')

    with col2 :
        Insulin = st.text_input ('Insulin')
        BMI = st.text_input ('BMI')
        DiabetesPedigreeFunction = st.text_input ('Diabetes Pedigree Function')
        Age = st.text_input ('Age')

    #code untuk diagnosis
    diab_diagnosis = ''

    #tombol prediksi
    if(st.button('Predict Now')) :
        diab_diagnosis = diabetes_model.predict([[Pregnancies,Glucose,BloodPreasure,SkinTickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if(diab_diagnosis[0] == 1) :
            diab_diagnosis = "Pasien terkena diabetes"
        else : 
            diab_diagnosis = "Pasien tidak terkena diabetes"

        st.success(diab_diagnosis)




elif tabs == 'Camera':
    st.title("Camera")
    st.write('Name of option is {}'.format(tabs))

    image = back_camera_input()
    if image:
        st.image(image)



    #blacklist='@*|©_Ⓡ®¢§š'  
    #data = tesseract_scanner(showimg=False, lang='vie+eng', blacklist=blacklist, psm=3)  

    #if data is not None:  
    #    st.write(data)


    


elif tabs == 'Report':
    st.title("Report Auto Refresh")
    st.write('Name of option is {}'.format(tabs))

    # Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
    # after it's been refreshed 100 times.
    count = st_autorefresh(interval=1000, limit=100, key="fizzbuzzcounter")

    # The function returns a counter for number of refreshes. This allows the
    # ability to make special requests at different intervals based on the count

    if count == 0:
        st.write("Count is zero")
    elif count % 3 == 0 and count % 5 == 0:
        st.write("FizzBuzz")
    elif count % 3 == 0:
        st.write("Fizz")
    elif count % 5 == 0:
        st.write("Buzz")
    else:
        st.write(f"Count: {count}")


   
    





