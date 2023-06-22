import pickle
import numpy as np
import streamlit as st

#load save model
model = pickle.load(open('penyakit_jantung.sav','rb'))

#judul web
st.title('Prediksi Penyakit Jantung')

col1,col2,col3 = st.columns(3)

with col1:
    age = st.number_input('Umur',min_value=0)

with col2:
    sex_input = st.selectbox(
        'Jenis Kelamin',
        ('Perempuan','Laki - Laki')
    )
    # sex = st.number_input('Jenis Kelamin')

with col3:
    cp_input = st.selectbox(
        'Tipe Nyeri Dada',
        ('Angina','Angina Atipikal','Non-Angina','asymptomatic')
    )

with col1:
    trestbps = st.number_input('Tekanan Darah')

with col2:
    chol = st.number_input('Nilai Kolesterol')

with col3:
    fbs_input = st.selectbox(
        'Gula Darah Puasa',
        ('<120mg/dl','>120mg/dl')
    )

with col1:
    restecg_input = st.selectbox(
        'Hasil Rekaman Jantung',
        ('Normal', 'Menampakkan Abnormal','Menunjukkan Kemungkinan Hipertrofi')
    )

with col2:
    thalach = st.number_input('Detak Jantung Maksimum')

with col3:
    #nyeri dada yang dipicu karena aktivitas
    exang_input = st.selectbox(
        'Latihan Induksi Angina',
        ('Tidak','Ya')
    )

with col1:
    oldpeak = st.number_input('ST Depression')

with col2:
    slope_input = st.selectbox(
        'Kemiringan Segmen',
        ('Upsloping', 'Flat', 'Downsloping')
    )

with col3:
    ca = st.number_input('Nilai Pembuluh Darah',min_value=0,max_value=3)

with col1:
    thal_input = st.selectbox(
        'Thalsemia',
        ('Normal', 'Terdeteksi', ' Cacat Reversebel')
    )

if(sex_input == 'Perempuan'):
    sex = 0
else:
    sex = 1  

if(cp_input == 'Angina'):
    cp = 0
elif(cp_input == 'Angina Atipikal'):
    cp = 1
elif(cp_input == 'Non-Angina'):
    cp = 2
else:
    cp = 3

if(fbs_input == '<120mg/dl'):
    fbs = 0
else:
    fbs = 1

if(restecg_input == 'Normal'):
    restecg = 0
elif(restecg_input == 'Menampakkan Abnormal'):
    restecg = 1
else:
    restecg = 2

if(exang_input == 'Tidak'):
    exang = 0
else:
    exang = 1


if(slope_input == 'Upsloping'):
    slope = 0
elif(slope_input == 'Flat'):
    slope = 1
else:
    slope = 2

if(thal_input == 'Normal'):
    thal = 0
elif(thal_input == 'Terdeteksi'):
    thal = 1
else:
    thal = 2

#code for prediction

heart_diagnosis = ''

#button prediction

if st.button('Prediksi Penyakit Jantung'):
    heart_prediction = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

    if (heart_prediction[0] == 1):
        heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
    else:
        heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'

st.success(heart_diagnosis)
