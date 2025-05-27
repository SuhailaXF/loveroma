import streamlit as st

st.title("romakelapa")
st.write(
    "rawrma"
)
st.image("IMG-20250519-WA0030.jpg")
st.write("so cuteeetyy")
st.title("aplikasi sederhana")
st.header("aplikasi mengecek nilai genap/ganjil")
angka = st.number_input("tulis sebuah angka:", value=0, step=1)
if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
    st.write(f"{angka} adalah bilangan ganjil")
