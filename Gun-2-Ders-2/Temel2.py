## Metin Öğeleri ##


import streamlit as st
import pandas as pd
st.write('Merhaba, *Dunya!* :sunglasses:')


Veri_Cercevesi= pd.DataFrame({
    'Birinci Kolon': [1, 2, 3, 4],
    'İkinci Kolon': [10, 20, 30, 40],
})



st.write(1234)

st.write(Veri_Cercevesi)


st.write('1 + 1 = ', 2)

st.write('Veri Cercevesi aşağıda:', Veri_Cercevesi, 'Veri Cercevesi yukarıda.')



#pip install altair
#pip install numpy

import numpy as np
import altair as alt

Veri_Cercevesi2= pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(Veri_Cercevesi2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)




import pandas as pd

cizelge_verisi = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(cizelge_verisi)

#pip install plotly

import plotly.figure_factory as ff

# Histogram verisi ekle
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Verileri birlikte gruplandırma
hist_verisi = [x1, x2, x3]

grup_etiketleri = ['Grup 1', 'Grup 2', 'Grup 3']

# Özel bin_size ile dağıtım grafiği oluşturma
sekil = ff.create_distplot(
        hist_verisi, grup_etiketleri, bin_size=[.1, .25, .5])

# Çiz!
st.plotly_chart(sekil, use_container_width=True)