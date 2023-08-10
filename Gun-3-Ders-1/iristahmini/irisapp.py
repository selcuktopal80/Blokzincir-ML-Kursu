import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression  
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

#pip install -r requirements.txt


# Veri setini yükleme dataframe veri çerçevesi
iris_df = pd.read_csv("iris-species.csv")

print(iris_df)

# Sayısal olmayan 'Türler' sütununu 'map()' fonksiyonun kullanılarak sayısal olarak benzetmek için Iris DataFrame'e bir sütun ekleme.

# 'Map()' kullanılarak 'iris_df' için 'Label' sayısal hedef sütunu oluşturuluyor.

iris_df['Label'] = iris_df['Species'].map({'Iris-setosa': 0, 'Iris-virginica': 1, 'Iris-versicolor':2})
print(iris_df)

# # Çiçek türlerini '0' , '1' ve '2' etiketlerine göre sınıflandırmak için Destek Vektörü sınıflandırması için bir model oluşturma.

# X ve y değişkenleri oluşturma

X = iris_df[['SepalLengthCm','SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = iris_df['Label']
print(X)
print(y)

# Verileri eğitim ve test kümelerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

print(X_train, X_test, y_train, y_test )

# SVC modelini oluşturma 
svc_model = SVC(kernel = 'linear')
svc_model.fit(X_train, y_train)

# Random Forest Classifier modelini oluşturma
rf_clf = RandomForestClassifier(n_jobs = -1, n_estimators = 100)
rf_clf.fit(X_train, y_train)


# Lojistik Regresyon modelinin oluşturulması
log_reg = LogisticRegression(n_jobs = -1)
log_reg.fit(X_train, y_train)

setosaimg= Image.open('setosa.png')
versicolorimg= Image.open('versicolor.png')
virginicaimg = Image.open('virginica.png')

# Model, SepalLength, SepalWidth, PetalLength, PetalWidth'i girdi olarak kabul eden ve tür adını döndüren bir 'prediction()' fonksyionu oluşturun.
@st.cache(suppress_st_warning=True)
def prediction(model, sepal_length, sepal_width, petal_length, petal_width):
	species = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
	species = species[0]
	if species == 0:
		st.image('setosa.png')
		return "Setosa"
	elif species == 1:
		st.image('virginica.png')
		return "Virginica"
	else:
		st.image('versicolor.png')
		return "Versicolor"



st.markdown("<h1 style='text-align: center; color: grey;'>İris Çiçek Türleri Sınıflandırma Uygulaması</h1>", unsafe_allow_html=True)

#st.title("İris çiçek türleri Sınıflandırma Uygulaması")
tanitim=Image.open('iris.png')
st.image(tanitim, width=750)




#st.sidebar.title("Iris Flower Species Prediction App")      

s_len = st.sidebar.slider("Sepal Uzunluk", float(iris_df["SepalLengthCm"].min()), float(iris_df["SepalLengthCm"].max()))
s_wid = st.sidebar.slider("Sepal Genişlik", float(iris_df["SepalWidthCm"].min()), float(iris_df["SepalWidthCm"].max()))
p_len = st.sidebar.slider("Petal Uzunluk", float(iris_df["PetalLengthCm"].min()), float(iris_df["PetalLengthCm"].max()))
p_wid = st.sidebar.slider("Petal Genişlik", float(iris_df["PetalWidthCm"].min()), float(iris_df["PetalWidthCm"].max()))


classifier = st.sidebar.selectbox("Sınıflayıcı Seçiniz", ('Destek Vektör Makinesi', 'Lojistik Regresyon', 'Rassal Forest Sınıflayıcı'))


if st.sidebar.button("Tahmin Et"):
	if classifier =='Support Vector Machine':
		species_type = prediction(svc_model, s_len, s_wid, p_len, p_wid)
		score = svc_model.score(X_train, y_train)
	
	elif classifier =='Logistic Regression':
		species_type = prediction(log_reg, s_len, s_wid, p_len, p_wid)
		score = log_reg.score(X_train, y_train)
	
	else:
		species_type = prediction(rf_clf, s_len, s_wid, p_len, p_wid)
		score = rf_clf.score(X_train, y_train)
		
	st.markdown('\n\n')
	st.markdown('\n\n')
	st.write("Tahmin Edilen Tür:", species_type)
	st.write("Bu modelin doğruluk oranı:", score)
	
		
	
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)





#streamlit run irisapp.py --server.port 8080



# #############   Tahmin app 2 #######################




# # import streamlit as st
# # import pandas as pd
# # from sklearn import datasets
# # from sklearn.ensemble import RandomForestClassifier

# # st.write("""
# # # Basit İris Çiçeği Tahmin Uygulaması
# # Bu uygulama **İris çiçeği** türünü tahmin eder!
# # """)

# # st.sidebar.header('User Input Parameters')

# # def user_input_features():
# #     sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
# #     sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
# #     petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
# #     petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
# #     data = {'sepal_length': sepal_length,
# #             'sepal_width': sepal_width,
# #             'petal_length': petal_length,
# #             'petal_width': petal_width}
# #     features = pd.DataFrame(data, index=[0])
# #     return features

# # df = user_input_features()

# # st.subheader('Kullanıcı Girdi Parametreleri')
# # st.write(df)

# # iris = datasets.load_iris()
# # X = iris.data
# # Y = iris.target

# # clf = RandomForestClassifier()
# # clf.fit(X, Y)

# # prediction = clf.predict(df)
# # prediction_proba = clf.predict_proba(df)

# # st.subheader('Sınıf etiketleri ve bunlara karşılık gelen dizin numarası')
# # st.write(iris.target_names)

# # st.subheader('Tahmin')
# # st.write(iris.target_names[prediction])
# # #st.write(prediction)

# # st.subheader('Tahmin Olasılığı')
# # st.write(prediction_proba)