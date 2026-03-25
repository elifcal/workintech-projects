## Bayes Teoremi - elle ispat

Bu challenge’da elimizde bir ‘Weather’ (Hava Durumu) veri seti (Rain, Sunny, Overcast) ve bunlara karşılık gelen ‘Play’ (Oyun) verisi (Yes veya No) var. Bu veri, hava durumuna göre spor etkinliğinin yapılıp yapılmaması gerektiğini gösteriyor.

```python
weather_data= ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
play_data   =['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
```
Burada `weather` içindeki indeks `i` , `play` içindeki indeks i ile eşleşiyor. Örneğin, 2. maçta hava durumu 'Overcast' ve maç oynanmış (Play = Yes).

Amacımız bir maçın oynanma veya oynanmama olasılığını anlamak.

Daha net ifade edersek, yeni bir hava durumu verildiğinde ertesi gün maçın yapılıp yapılmayacağını tahmin etmek için **$P(play \mid weather)$** olasılığını hesaplamak istiyoruz.

Bunu yaparken, aynı zamanda aşağıdaki 4 olasılığı kendimiz hesaplayarak **Bayes Teoremini** de göstermiş olacağız:

<img src='https://wagon-public-datasets.s3.amazonaws.com/data-science-images/math/bayes-theorem.png'>


Burada:
- $P(play)$ o ana kadar gördüğümüz tüm verilere göre sınıfın (Play = Yes veya No) olasılığı hakkındaki **prior** (öncül) inancımızdır.
- $P(weather \mid play)$ maçın oynanıp oynanmadığı verildiğinde, bu tip hava durumunu görmenin **likelihood**’ıdır (olasılığıdır).
- $P(play \mid weather)$ hava durumu verildiğinde maçın gerçekten oynanıp oynanmayacağına dair  **posterior**  (soncül) olasılıktır.
- $P(weather)$ problemimiz açısından sabit bir değerdir: oynama/oynamama seçimine bağlı değildir.

🚀 Haydi başlayalım!

`bayes_theorem.ipynb`notebook’unu aç:

> jupyter notebook
