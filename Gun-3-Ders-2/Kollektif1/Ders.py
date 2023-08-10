
#bknz golfDecisionTreepng ve kararAgacipng

from sklearn import tree

# #### eğitim ve değer dizilerimin tanımlaması ##

# X = [[0, 0], [1, 1]]
# Y = [0, 1]

# Siniflandirma = tree.DecisionTreeClassifier()
# Siniflandirma = Siniflandirma.fit(X, Y)
# ##############################################


# # Yapıyı algoritmaya uygun olarak kurduktan sonra örnek sınıfını tahmin etme
# Siniflandirma.predict([[2., 2.]])

# # Alternatif olarak aynı eğitim sınıfında olan eğitim örnekleri ile, diğer yapraklardaki değer olasılığını tahminlemeye başla
# Siniflandirma.predict_proba([[2., 2.]])

# print(Siniflandirma.predict([[2., 2.]]))
# print(Siniflandirma.predict_proba([[2., 2.]]))


# Modeli oluşturduktan sonra model eğitimi için, hazır veriler içeren iris veritabanı 
# (Genel bitki özellikleri veri bankası) üzerinden çeşitli bitki özellikleri ile oluşan genetik yapılanmayı 
# ağaç diagramı olarak kurgulayıp-yapılandırıyorum

from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True) #Train (eğitim verisi) y test verisi

Siniflandirma = tree.DecisionTreeClassifier()
Siniflandirma = Siniflandirma.fit(X, y)

#Model eğitimini tamamlayıp yapılandırmayı oluşturduktan sonra da karar ağacını çizdiriyoruz

tree.plot_tree(Siniflandirma) 

# ## Random Forest (Rassal Ormal) Sınıflandırma ### 


# # Çıktı olarak aldığımız karar ağacı modelimizin derinliği ise 6‘dır; 1 kök, 4 yaprak, 1’de son düğümden oluşmaktadır.

# '''Random Forest, bir makine öğrenimi algoritmasıdır ve genellikle sınıflandırma problemlerinde kullanılır. 
# Aşağıda Random Forest sınıflandırma algoritmasının ne yaptığını açıklamaya çalışayım:

# 1. Veri Örnekleme: Random Forest algoritması, eğitim veri setinden rastgele örneklemeler alır. 
# Bu örnekleme süreci, her bir örneklem için veri setinden aynı büyüklükte alt örneklemeler çekerek gerçekleştirilir. 
# Bu, her bir alt örneklemenin rastgele ve farklı veri noktalarına sahip olduğu anlamına gelir.

# 2.  Ağaçları Oluşturma: Random Forest, her bir alt örneklemeyi kullanarak karar ağaçları (decision trees) oluşturur. 
# Karar ağaçları, veri noktalarını sınıflandırmak için bir dizi karar kuralı kullanır. Karar ağaçları, 
# veri setindeki özelliklerin değerlerine göre dallanır ve sonunda sınıflandırma kararını verir.

# 3. Karar Ağaçlarının Oylaması: Random Forest, oluşturulan karar ağaçlarının sınıflandırma sonuçlarını birleştirir. 
# Her bir karar ağacı, giriş verisini sınıflandırır ve tahmin edilen sınıfı belirtir. Random Forest, tüm karar 
# ağaçlarının tahminlerini toplar ve en çok oy alan sınıfı genel tahmin olarak kabul eder.

# Random Forest algoritması, birden çok karar ağacının bir araya gelmesiyle oluşan bir topluluk (ensemble) öğrenme yöntemidir. 
# Bu topluluk, her bir karar ağacının kendi benzersiz özelliklere ve hatalara sahip olabileceği için genel olarak daha 
# iyi bir sınıflandırma performansı sağlar. Ayrıca, overfitting (aşırı uydurma) sorununu azaltmak için veri örnekleme ve 
# ağaçların rastgele oluşturulması gibi yöntemler kullanır.

# Random Forest sınıflandırma algoritması, bir veri setindeki özellikleri kullanarak verileri sınıflandırır ve 
# birden çok karar ağacının oylamasıyla tahminlerini birleştirir. Bu sayede, genel olarak daha iyi bir sınıflandırma 
# performansı elde eder.



# 1. Karar ağaçları, herhangi bir kontrol olmadan büyümesine izin verilirse normalde aşırı uyum sorunu yaşar.

# 2. Tek bir karar ağacı hesaplamada daha hızlıdır.

# 3. Özelliklere sahip bir veri seti, bir karar ağacı tarafından girdi olarak alındığında, tahmin yapmak için 
# bazı kurallar formüle edecektir.


# 1. Rassal ormanlar, verilerin alt kümelerinden oluşturulur ve nihai çıktı, ortalama veya çoğunluk sıralamasına dayalıdır; 
# bu nedenle overfitting sorunu halledilir.

# 2. Nispeten daha yavaştır.

# 3. Rastgele orman, gözlemleri rastgele seçer, bir karar ağacı oluşturur ve ortalama sonucu alır. 
# Herhangi bir formül seti kullanmaz. 



# Rassal Orman Algoritmasında Yer Alan Adımlar

# Adım 1: Rastgele orman modelinde, her karar ağacını oluşturmak için bir veri noktaları alt kümesi ve 
# bir özellik alt kümesi seçilir. Basitçe söylemek gerekirse, k sayıda kayda sahip veri setinden n rasgele kayıt ve m özellik alınır.

# Adım 2: Her örnek için bireysel karar ağaçları oluşturulur.

# Adım 3: Her karar ağacı bir çıktı üretecektir.

# Adım 4: Nihai çıktı, sırasıyla Sınıflandırma ve regresyon için Çoğunluk Oylaması veya 
# Ortalamaya dayalı olarak değerlendirilir.



# Rastgele Ormanın Önemli Özellikleri

# Çeşitlilik: Tek bir ağaç yapılırken tüm nitelikler/değişkenler/özellikler dikkate alınmaz; her ağaç farklıdır.

# Boyutsallığın lanetine karşı bağışıklık: Her ağaç tüm özellikleri dikkate almadığından, özellik alanı azalır.
# (Geniş bir özellik alanı, hesaplama ve karmaşıklık sorunlarına neden olur.)

# Paralelleştirme: Her ağaç, farklı veri ve niteliklerden bağımsız olarak oluşturulur. Bu, rastgele ormanlar oluşturmak 
# için CPU'yu tamamen kullanabileceğimiz anlamına gelir.

# Train-Test ayrımı: Rastgele bir ormanda, karar ağacı tarafından görülmeyen verilerin her zaman %30'u olacağından, 
# verileri tren ve test için ayırmamız gerekmez.

# Kararlılık: Kararlılık, sonucun çoğunluk oylamasına/ortalamaya dayalı olması nedeniyle ortaya çıkar.
 
 
#  '''

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# df = pd.read_csv('heart_v2.csv')
# print(df.head())
# sns.countplot(df['heart disease'])
# plt.title('Kalp hastalığı hastalarının değer sayıları')
# plt.show()

# # Özellik (feature) Değişkenini X'e ve Hedef (target) değişkenini y'ye atama.

# # Özellik değişkenini X'e atama
# X = df.drop('heart disease',axis=1)

# # Yanıt değişkenini y'ye atama
# y = df['heart disease']

# #Train(Eğitim)-Test-Split(Ayırma) gerçekleştirme

# # Şimdi verileri trin ve test olarak ayıralım
# from sklearn.model_selection import train_test_split
# # Eğitim ve Test verilerini ayırma
# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42) #42 burada sadece ID her zaman aynı split yabilsin diye
# X_train.shape, X_test.shape

# # RandomForestClassifier'ı içe aktarma ve verileri fit etme.

# from sklearn.ensemble import RandomForestClassifier
# classifier_rf = RandomForestClassifier(random_state=42, n_jobs=-1, max_depth=5,
#                                        n_estimators=100, oob_score=True)

# classifier_rf.fit(X_train, y_train)


# # oob skorunu kontrol etme
# classifier_rf.oob_score_


# # GridSearchCV kullanarak Random Forest için hiperparametre ayarı yapalım ve verileri fit edelim.

# '''
# Modelde denenmesi istenen hiperparametreler ve değerleri için bütün kombinasyonlar ile ayrı ayrı model kurulur ve belirtilen metriğe göre en başarılı
# hiperparametre seti belirlenir.
# (+) Tüm kombinasyonları denendiği için en iyi performans gösteren hiperparametre setini belirlemeyi garanti eder. Küçük veri setlerinde ve sadece
#  birkaç tane hiperparametre denenmek istendiğinde çok iyi çalışır.

# (-) Büyük bir veri seti ile çalışıldığında ya da denenecek olan hiperparametre sayısı ve değeri arttırıldığında kombinasyon
#  sayısı da katlanarak artacaktır. Kurulan her modelin cross-validation ile test edildiği de düşünüldüğünde maaliyet korkunç
#  derecede artacaktır bu sebeple alternatif olarak RandomSearchCV yöntemi tercih edilebilir.
 
#  '''




# rf = RandomForestClassifier(random_state=42, n_jobs=-1)
# params = {
#     'max_depth': [2,3,5,10,20],
#     'min_samples_leaf': [5,10,20,50,100,200],
#     'n_estimators': [10,25,30,50,100,200]
# }
# from sklearn.model_selection import GridSearchCV
# # Grid arama modelini somutlaştıralım.abs

# grid_search = GridSearchCV(estimator=rf,
#                            param_grid=params,
#                            cv = 4,
#                            n_jobs=-1, verbose=1, scoring="accuracy")

# grid_search.fit(X_train, y_train)
# grid_search
# grid_search.best_score_
# best_score_
# rf_best = grid_search.best_estimator_
# rf_best

# # Şimdi görselleştirelim
# from sklearn.tree import plot_tree
# plt.figure(figsize=(80,40))
# plot_tree(rf_best.estimators_[5], feature_names = X.columns,class_names=['Disease', "No Disease"],filled=True);

# # estimators_[5] ve estimators_[7] tarafından oluşturulan ağaçlar farklıdır. Böylece her ağacın diğerinden bağımsız olduğunu söyleyebiliriz.

# #Şimdi verileri özellik önemi yardımıyla sıralayalım

# rf_best.feature_importances_

# imp_df = pd.DataFrame({
#     "Varname": X_train.columns,
#     "Imp": rf_best.feature_importances_
# })

# imp_df.sort_values(by="Imp", ascending=False)