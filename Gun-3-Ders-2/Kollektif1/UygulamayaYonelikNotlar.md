
veri setimiz iki özellikten oluşuyor ve iki sınıfa ait örnekler içeriyor.

Genişlik    Uzunluk    Sınıf Etiketi
----------------------------------
   2.0        3.5            Dayanıklı
   3.2        4.1            DayaNıksız
   2.8        2.7            1
   4.5        1.9            0
   3.3        3.0            1
   2.7        3.8            0


Veriyi Eğitim ve Test Kümelerine Bölelim:

Eğitim Veri Kümesi:

Özellik 1   Özellik 2   Sınıf Etiketi
----------------------------------
   2.0        3.5            0
   3.2        4.1            1
   2.8        2.7            1
   3.3        3.0            1

Test Veri Kümesi:
Özellik 1   Özellik 2   Sınıf Etiketi
----------------------------------
   4.5        1.9            0
   2.7        3.8            0



Random Forest Oluşturma:

Random Forest algoritması, bu veri kümesi üzerinde çalışacak birden fazla karar ağacı oluşturur. Örneğin, 3 ağaçtan oluşan bir Random Forest modeli oluşturalım. Her bir ağaç, eğitim veri kümesinin rastgele bir alt kümesi üzerinde eğitilir.


Ağaç 1 Eğitimi:

Eğitim Veri Kümesi:
Özellik 1   Özellik 2   Sınıf Etiketi
----------------------------------
   2.0        3.5            0
   2.8        2.7            1
   3.3        3.0            1

Ağaç 1 tahminleri:
Test Örneği   Tahmin Edilen Sınıf
----------------------------------
   4.5                 0
   2.7                 1


Ağaç 2 Eğitimi:

Eğitim Veri Kümesi:
Özellik 1   Özellik 2   Sınıf Etiketi
----------------------------------
   3.2        4.1            1
   2.8        2.7            1
   3.3        3.0            1

Ağaç 2 tahminleri:
Test Örneği   Tahmin Edilen Sınıf
----------------------------------
   4.5                 0
   2.7                 1

Ağaç 3 Eğitimi:

Eğitim Veri Kümesi:
Özellik 1   Özellik 2   Sınıf Etiketi
----------------------------------
   2.0        3.5            0
   3.2        4.1            1
   2.7        3.8            0

Ağaç 3 tahminleri:
Test Örneği   Tahmin Edilen Sınıf
----------------------------------
   4.5                 0
   2.7                 0


Çoğunluk Oylaması ve Sınıf Olasılıkları:
Her ağacın tahminleri çoğunluk oylaması yöntemiyle birleştirilir. Sınıf etiketleri için çoğunluk oylaması yapılır ve sınıf olasılıkları içinse ağaçların olasılık değerleri ortalanarak elde edilir.

Çoğunluk Oylaması:

Test Örneği   Tahmin Edilen Sınıf
----------------------------------
   4.5                 0
   2.7                 1

Sınıf Olasılıkları (örneğin, 3 ağaçlı bir model için):

Test Örneği   Sınıf 0 Olasılığı   Sınıf 1 Olasılığı
------------------------------------------------
   4.5                   0.67                     0.33
   2.7                   0.33                     0.67



6. Model Değerlendirme (devam):
Test veri kümesi üzerinde elde edilen tahminler ile gerçek sınıf etiketleri arasında karşılaştırma yapılarak modelin performansı ölçülür. Bu değerlendirme genellikle farklı performans metrikleri kullanılarak yapılır. En yaygın kullanılan değerlendirme metriklerinden biri "doğruluk"tur (accuracy). Doğruluk, doğru tahmin edilen örneklerin toplam örnek sayısına oranını gösterir.

7. Model Ayarlamaları:
Random Forest algoritması, eğitim aşamasında bir dizi parametre ile yapılandırılabilir. Örneğin, `n_estimators` parametresi ile oluşturulacak ağaç sayısı belirlenebilir. Daha fazla ağaç, modelin daha karmaşık hale gelmesini ve daha yüksek performans sağlamasını sağlayabilir, ancak aynı zamanda daha fazla hesaplama gücü gerektirir. Ayrıca, ağaçların maksimum derinliği (`max_depth`), minimum örnekleme bölme için gerekli örnek sayısı (`min_samples_split`), minimum yaprak düğümünde gereken örnek sayısı (`min_samples_leaf`) gibi parametreler de modelin davranışını etkiler.

8. Model Kullanımı:
Model eğitildikten sonra, yeni veri örnekleri için sınıf etiketlerini tahmin etmek için kullanılabilir. Örnek olarak:


Eğitilmiş modelle tahmin yapma
y_pred = random_forest.predict(X_test)

Sınıf olasılıklarını tahmin etme
y_proba = random_forest.predict_proba(X_test)


Random Forest algoritması, genellikle sınıflandırma ve regresyon problemleri için başarılı sonuçlar verir. Birden fazla karar ağacının bir araya getirilmesi sayesinde, aşırı uyumu azaltabilir, genellemeyi artırabilir ve daha güvenilir tahminler elde edebilir. Bununla birlikte, modelin başarısı veri kümesine ve yapılandırmaya bağlı olarak değişebilir, bu nedenle modelin performansını farklı metriklerle değerlendirmek önemlidir.







Kollektif (Federe) öğrenme



Birleşik (Kollektif, Federe) öğrenme, birden çok katılımcının ham verilerini paylaşmadan işbirliği içinde bir modeli eğittiği merkezi olmayan bir makine öğrenimi yaklaşımıdır. Raw data yerine global bir model oluşturmak için bir araya getirilen model güncellemelerini paylaşırlar. Bu akıllı sözleşme, düğümlerin kaydını, veri paylaşımını, model güncelleme gönderimini ve model toplamayı kolaylaştırır.



Python (3.6 veya üstü sürüm)
solcx library (Solidity derleyicisi)
torch library (model training etmek için)
sklearn library (veri seti ve makine öğrenme modelleleri için)
web3 library ( Ethereum blokzincir ile etkileşim için)
numpy library (Veri işlemek için)
struct library (model güncellemelerini paketlemek için, Bu modül Python değerleri ve Python byte nesneleri olarak temsil edilen C yapıları arasında dönüşüm yapar.)
joblib library (model kalıcılığı için)



https://github.com/Revanthraja/Federated-Learning-Solidity-Contract.git


Ethereum test ağına bağlanmak için Ganache URL'sini (ganache_url değişkeni) güncelleyin.

Adım 1: Solidity kodunu derleyin: Solidity kodu solcx kütüphanesi kullanılarak derlenir ve sözleşme ABI ve bayt kodu çıkarılır.

Adım 2: Akıllı Sözleşmeyi Dağıtın: Derlenen sözleşme, web3 kitaplığı kullanılarak Ethereum blokzincirine dağıtılır. Sözleşme adresi dağıtımdan sonra alınır.

Adım 3: Dağıtılan sözleşmeyi eğitim için kullanın: Dağıtılan sözleşmenin bir örneği, sözleşme adresi kullanılarak oluşturulur.

Adım 4: Düğüm Kaydı: Bir eğitim düğümü, akıllı sözleşmenin registerNode fonksiyonunu çağırarak kendini kaydeder.

Adım 6: Veri Dağıtımı: Akıllı sözleşmenin shareData fonksiyonu çağrılarak veriler düğümlere dağıtılır. Her düğüm, adresine bağlı olarak verilerin bir bölümünü alır.

Adım 8: Model Güncelleme: Her düğüm, atanan verilerini kullanarak bir yerel modeli eğitir ve sendModelUpdate fonksiyonunu çağırarak model güncellemesini akıllı sözleşmeye gönderir.

Adım 8: Model Toplama: Akıllı sözleşme, düğümlerden alınan model güncellemelerini toplar ve agregaModelUpdates fonksiyonunu  çağırarak toplu bir model oluşturur.

Adım 9: Eğitilen modeli kaydedin: Eğitilen model, joblib kitaplığı kullanılarak bir dosyaya kaydedilir.

Adım 10: Doğruluğu hesaplayın ve yazdırın: Eğitilen modelin doğruluğu hesaplanır ve yazdırılır.

