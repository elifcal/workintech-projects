
# Linear Regression

## Dataset’i indirin

Dataset’e [buradan](https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/NBA.csv) ulaşabilirsiniz.  
Challenge notebook’unuzdan yalnızca pandas kullanarak bir DataFrame içine yükleyebilirsiniz 😉


## Dataset 🏀

Dataset, 4000 NBA oyuncusunun istatistiklerini içerir, bunlar arasında:

- `season`: Oyuncunun oynadığı sezon (yıl)
- `poss`: Oynanan possession sayısı
- `mp`: Oynanan dakika sayısı
- `do_ratio`: Oyuncunun savunma ve hücumda geçirdiği sürenin oranı; negatif değerler daha fazla savunma pozisyonunu ifade eder
- `pacing`: Oyuncunun, 48 dakika başına takım possession’larına etkisi
- `win_rating`: *Wins Above Replacement* rating’i; bir oyuncunun, aynı seviyedeki bir yedeğe kıyasla takıma kazandırdığı ek galibiyet sayısı


## Egzersiz

Bu egzersizde, oyuncuların win rating’i ile oynadıkları dakika sayısı arasındaki ilişkiyi modelleyeceksiniz.

Bu süreçte şunları yapacaksınız:

- Win rating, oynanan dakika sayısı ve diğer istatistikler arasındaki ilişkiyi görselleştirmek
- K-Fold cross-validation kullanarak bir Linear Regression modelini değerlendirmek
- Bir Linear Regression modeli eğitmek
- Eğitilmiş modeli görselleştirmek
- Modeli kullanarak yeni veriler için tahmin yapmak


## Hadi Başlayalım!

Egzersize başlamak için `jupyter notebook` içinde `Linear_Regression.ipynb` dosyasını açın ve talimatları takip edin.

🚀 Sıra sizde!