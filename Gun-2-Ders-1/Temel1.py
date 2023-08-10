import streamlit as st

st.markdown('Streamlit  **_gercekten_ harika bir projedir**.')

st.markdown("bu yazı:red[kırmızıdır] ve bu **:blue[mavi renkli]** ve **kalın fonttadır**")
st.markdown(":red[$\sqrt{x^2+y^2}=1$] bir Pisagor eşitliiğidir. :pencil:")

st.markdown("<h1 style='text-align: center; color: grey;'>HTML kokusu alan var mı?</h1>", unsafe_allow_html=True)


st.title('Bu Bir Başlıktır')
st.title(' _italyanik_ , :blue[mavidir] ve  emoji :sunglasses: ve :whale2: olan bir başlık')



st.header('Bu header dır')

st.caption('Bu, yukarıdaki bir şeyi açıklayan bir dizedir.')




kod = '''def selam():
    print("Selam, Streamlit!")'''

st.code(kod, language='python')


st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})




st.slider("Bu bir slider", 0, 100, (25, 75))



st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')