import base64
import streamlit as st
import pickle
from PIL import Image

MODEL_FILE = "modelKualitasUdaraRFC.pkl" #Random Forest Classifier dengan akurasi 99%
pickle_in = open(MODEL_FILE, 'rb')
classifier = pickle.load(pickle_in)

st.set_page_config(
    page_title="Identifikasi Pencemaran Udara ",
)

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("d.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 180%;
background-position: center;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: right; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

}}
</style>
"""
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Identifikasi Pencemaran Udara")
st.markdown('<div style="text-align:justify">Selamat datang di website yang dibuat untuk memberikan informasi mengenai identifikasi pencemaran udara dengan metode random forest. Di sini, Anda akan menemukan identifikasi tingkat pencemaran udara dengan kategori baik, sedang, dan tidak sehat. Bertujuan untuk meningkatkan kesadaran dalam mengambil tindakan mencegah guna melindungi kesehatan dan lingkungan. Mari bersama-sama menjaga udara bersih untuk masa depan yang lebih sehat.</div>', unsafe_allow_html=True)
st.write("TUTORIAL : klik sidebar yang ada di kiri atas, kemudian input komponen, Selanjutnya akan muncul hasil identifikasi pencemaran udara pada bagian tengah website")
st.write("Hasil Identifikasi Pencemaran Udara :")


st.sidebar.markdown('## Input Komponen ')
pm10 = st.sidebar.slider('pm10: Partikulat', 0, 150, 30) 
pm25 = st.sidebar.slider('pm25: Partikulat', 0, 150, 48) 
so2 = st.sidebar.slider('so2: Sulfida', 0, 150, 24)
co = st.sidebar.slider('co: Carbon Monoksida', 0, 150, 4)
o3 = st.sidebar.slider('o3: Ozon', 0, 150, 32)
no2 = st.sidebar.slider('no2: Nitrogen dioksida', 0, 150, 7)

prediction = classifier.predict([[pm10, pm25, so2, co, o3, no2]])
if (prediction[0] == 0) :
    st.success("Baik")
elif (prediction[0] == 1) :
    st.success("Sedang")
elif (prediction[0] == 2) :
    st.success("Tidak Sehat")

st.write("Berikut ini tabel rentang tingkat pencemaran udara")
img = Image.open('ISPU.jpg')
img = img.resize((700, 418))
st.image(img, use_column_width=False)
