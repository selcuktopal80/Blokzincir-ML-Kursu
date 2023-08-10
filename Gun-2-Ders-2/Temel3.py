import streamlit as st

if st.button('Merhaba De Bakalım'):
    st.write('Neden Oradasın!')
else:
    st.write('Güle Güle')




opsiyonlar = st.multiselect(
    'Favori Rengin Nedir?',
    ['Yeşil', 'Sarı', 'Kırmızı', 'Lacivert'],
    ['Sarı', 'Lacivert'])

st.write('Seçtiklerin:', opsiyonlar)


from datetime import datetime

baslangic_zamani = st.slider(
    "Ne zaman başlayacaksın?",
    value=datetime(2023, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("baslangic_zamani:", baslangic_zamani)