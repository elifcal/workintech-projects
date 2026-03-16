# Stock Market API

Bu alıştırmada, [Massive](https://massive.com/) adlı stock market API’siyle çalışacağız.

🎯 Buradaki hedef:

* API dokümantasyonunu okumaya alışmak,
* bir API’den bilgi extract etmek ve
* bu bilgiyi bir dataframe’e load ederek veriyi kolayca manipulate ve visualize etmektir.

## Intro

Veri toplamanın yaygın yollarından biri API’lerdir. Bunlar authentication gerektiren veya gerektirmeyen [public APIs](https://github.com/public-apis/public-apis), ücretsiz veya ücretli servisler, şirket içi internal APIs vb. olabilir.

API’lerle çalışırken yapacağınız bir çağrı (API call) size genellikle iki **data formatı**ndan biriyle cevap döndürür:

* [XML](https://en.wikipedia.org/wiki/XML) (uzun süredir kullanılan)
* [JSON](https://en.wikipedia.org/wiki/JSON) (günümüzde çok yaygın)

ℹ️ Modern API’lerin çoğu JSON döndürür. Bu challenge’da da böyle bir API kullanacağız.

## Reading the documentation

Yeni bir API ile karşılaştığınızda ilk refleksiniz doğrudan dokümantasyona gidip şu sorulara cevap aramak olmalıdır:

1. JSON döndürüyor mu?
2. Authentication gerekiyor mu? (API key almak için kayıt olmam gerekiyor mu? Ücretli mi?)
3. Base URI nedir?
4. Hangi endpoint’leri çağırabilirim? Bu endpoint’ler hangi veriyi döndürür?

👯‍♂️ Buddy time! 👉 **massive.com** için API dokümantasyon sayfasını bulalım. Dokümantasyonu okuyun ve bu soruları cevaplamaya çalışın. Bu API’nin ne yaptığı konusunda rahat hissettiğinizde challenge’a başlayabilirsiniz.

<details><summary markdown='span'>Dokümantasyonu bulma çözümü
</summary>
Dokümantasyon sayfaları genellikle sitenin footer’ında veya bir menü altında olur.
<br>
Google’da <i>'the_website_name API documentation'</i> araması da hızlı bir yöntemdir.
<br>
<strong>Çözüm:</strong> <a href="https://massive.com/docs">https://massive.com/docs</a>
</details>

## Apple stock the last 90 days

### API setup

Kullanacağımız API endpoint’lerinin bazıları **paywall** arkasındadır.

Neyse ki API’nin pek çok fonksiyonunu ücretsiz olarak kullanabiliriz. Sadece siteye kayıt olmanız yeterlidir ve **dakikada 5 API çağrısını ücretsiz** kullanabilirsiniz. Bu bizim için yeterli olacaktır.

👉 Şimdi **bir hesap oluşturun**. Kayıt işlemi sonrasında sitenin sağ üst köşesindeki `Dashboard` bölümünde size özel API key’inizi bulabilirsiniz.

API çağrısı yaptığınızda, bu API key’i request içinde bir key-value pair olarak göndermeniz gerekecektir.

Örneğin, belirli bir günün stock fiyatlarını almak için:

```
https://api.massive.com/v1/open-close/AAPL/2025-02-03?adjusted=true&apiKey=YOUR_API_KEY
```

### Using the API

👉 Şimdi Massive API dokümantasyonunda historical Apple stock prices için **URL**’i bulalım.

URL’i bulduğunuzda, bir tarayıcı sekmesine kopyalayıp yapıştırın ve API’den dönen veriyi inceleyin.

> Eğer Chrome kullanıyorsanız, JSON’ı daha okunaklı görmek için [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) extension’ını yüklemenizi öneririz. Sonuçta JSON sadece parse edilmesi gereken bir text’tir, extension bu işi yapacaktır.

Dönen JSON şöyle görünmelidir:

<details><summary markdown='span'>Örnek JSON göster
</summary>

```js
{
  "ticker": "AAPL",
  "queryCount": 24,
  "resultsCount": 24,
  "adjusted": true,
  "results": [
    {
      "v": 7.0790813e+07,
      "vw": 131.6292,
      "o": 130.465,
      "c": 130.15,
      "h": 133.41,
      "l": 129.89,
      "t": 1673240400000,
      "n": 645365
    },
    // [...]
  ],
  "status": "OK",
  "request_id": "edd1a3b1104cde7bba8fbe0ccaa645df",
  "count": 24
}
```

</details>

❗️ Çözümü okumadan önce kendin dene! Bir API dokümantasyonunda aradığını bulmak genellikle **10–15 dakika** sürer.

<details><summary markdown='span'>Çözüm
</summary>
Bilgi burada bulunuyor:
<a href="https://massive.com/docs/stocks/get_v2_aggs_ticker__stocksticker__range__multiplier___timespan___from___to">https://massive.com/docs/stocks/get_v2_aggs_ticker__stocksticker__range__multiplier___timespan___from___to</a>
<br>
URL:
<pre>
https://api.massive.com/v2/aggs/ticker/AAPL/range/1/day/2025-01-02/2025-02-03?adjusted=true&sort=asc&apiKey=YOUR_API_KEY
</pre>
</details>

👉 API dokümantasyonunu okuyarak şunları anlamaya çalışın:

* request formatı (URL’in farklı parçaları)
* response içinde dönen key’ler ne anlama geliyor?

🔍 Son 90 günün fiyatlarını almak için neyi değiştirmelisiniz?

---

### Making test calls to the API

Bir şey inşa etmeye başlamadan önce, API çağrısı yapabildiğimizden emin olmamız gerekir.
Bu, API’nin ihtiyaçlarımıza uygun olup olmadığını erkenden görmemizi sağlar.

Peki ilk çağrıyı nasıl yapabiliriz? Tarayıcıyı kullanarak...

Tarayıcı bir HTTP client’tır! Eğer karmaşık bir `Header` eklemeniz gerekmiyorsa ve kullanılan HTTP verb `GET` ise, tek yapmanız gereken URL’i tarayıcıya yazmaktır.

---

## Using API data in Pandas

### Setup

Bu alıştırma için Notebook’ta çalışacağız.

```sh
jupyter notebook
```

👉 `~/code/<user.github_nickname>/{{local_path_to("01-Stock-Market-API")}}` klasöründe `stocks.ipynb` adlı yeni bir Jupyter Notebook oluşturun.

👉 İlk cell’de şu import’larla başlayın:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```

Historical Apple stock prices için API URL’ini yeniden kullanacağız.<br>
API çağrısı yapmak için aşağıdaki kodu yazabilirsiniz:

```python
import requests

url = "YOUR_API_URL"    # Daha önce bulduğunuz URL ile değiştirin
api_data = requests.get(url).json()
```

👉 `.get()`’ten sonra neden `.json()` chain ediyoruz? `.json()` olmadan da çalışır mı? Intermediate adımları `print()` ederek kendinizi ikna edin. (💡 [Doc](https://requests.readthedocs.io/en/master/user/quickstart/#json-response-content))

👉 URL’i değiştirerek son 90 günün Apple stock fiyatlarını alın. End date olarak mutlaka **dünün tarihi** olmalıdır, aksi halde çalışmaz.

Kod parametre değişiklikleri sırasında kırılırsa `.json()` kısmını comment out edip `.get()` sonucunu `print()` ederek inceleyebilirsiniz.

---

### Convert the request data into a DataFrame

👉 Artık bu veriden `apple_df` adlı bir dataframe oluşturabilirsiniz. JSON formatını tarayıcıda inceleyerek extract etmeniz gereken kısmı belirleyin.

<details><summary markdown='span'>Çözüm
</summary>
<code>apple_df = pd.DataFrame(api_data['results'])</code>
</details>

Bu dataframe ile stock price’ın gelişimini plot edebiliriz.
Ancak önce birkaç hazırlık yapmamız gerekir:

* timestamp içeren kolonu datetime objesine çevirin ve `date` adlı bir kolon olarak kaydedin.
* `date` kolonunu index yapın.
* Kolon isimlerini `c`, `o`, `h`, `l` gibi anlaşılır olmayan adlardan daha kullanıcı dostu isimlere çevirin.

---

### Converting the date to a datetime object

👉 Önce API dokümantasyonunu kontrol edin:

* Dataframe’de zamanı hangi kolon temsil ediyor?
* Bu sayı neyi ifade ediyor?

<details><summary markdown='span'>Çözüm
</summary>
Zaman bilgisi dataframe’de <code>t</code> kolonundadır.
<br>
Bu sayı **Unix time** formatıdır (millisecond). Programlamada çok yaygındır — 1-1-1970’ten bu yana geçen millisecond sayısını ifade eder.
</details>

👉 Bu değeri tarihe çevirmek için `Pandas.to_datetime()` kullanabilirsiniz:

* **pd.to_datetime()** dokümantasyonu: [http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)
* Unix time’dan dönüştürmek için hangi argümanı kullanmalısınız?
* Millisecond olduğunu Pandas’a nasıl söylersiniz?

<details><summary markdown='span'>Çözüm
</summary>
<code>apple_df['date'] = pd.to_datetime(apple_df['t'], origin='unix', unit='ms')</code>
</details>

---

### Set the date column as the index

👉 Bunun için DataFrame method’u **set_index** kullanılabilir:

Dokümantasyon: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)

<details><summary markdown='span'>Çözüm
</summary>
<code>apple_df = apple_df.set_index('date')</code>
</details>

---

### Rename the columns

Kolonları rename etmek için hangi DataFrame method’unu kullanmalısınız? Çok uzağa bakmayın…

<details><summary markdown='span'>Çözüm
</summary>
<strong>pd.DataFrame.rename()</strong> dokümantasyonu: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html
</details>

👉 Kolonları şu şekilde rename edin:

```
  'o': 'open'
  'c': 'close'
  'h': 'high'
  'l': 'low'
```

<details><summary markdown='span'>Çözüm
</summary>
```python
mapping = {
    'o': 'open',
    'c': 'close',
    'h': 'high',
    'l': 'low',
    'n': 'number',
    'v': 'volume',
    'vw': 'avg_price'
}
apple_df = apple_df.rename(columns=mapping)
```
</details>

---

### Now we can plot 🎉

👉 Önce sadece **`close`** kolonunu plot edelim:

<details><summary markdown='span'>Çözüm
</summary>
<code>apple_df['close'].plot()</code>
</details>

Şimdi **open**, **close**, **high**, **low** kolonlarını birlikte plot edelim:

<details><summary markdown='span'>Çözüm
</summary>
<code>apple_df[['open', 'close', 'high', 'low']].plot()</code>
</details>

💡 Plot okunabilir değilse, `figsize` argümanıyla iyileştirebilirsiniz:

Dokümantasyon: [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)

<details><summary markdown='span'>Çözüm
</summary>
<code>apple_df[['open', 'close', 'high', 'low']].plot(figsize=(12,4))</code>
</details>

---

### Test your code!

Notebook’unuza aşağıdaki cell’i ekleyip çalıştırın:

```python
from nbresult import ChallengeResult

result = ChallengeResult('apple',
    index_name=apple_df.index.name,
    index_type=apple_df.index.dtype,
    columns=apple_df.columns
)
result.write()
print(result.check())
```

Kodunuzu `commit` ve `push` edebilirsiniz 🚀

---

## Back to the API

Bu API’den başka hangi verileri alabileceğimizi keşfedelim 🕵️‍♂️

### What is the URL to find:

1. Amazon’ın historical stock prices?
2. Meta’nın (Facebook) market cap’i?
3. Apple’ın son 4 çeyreklik gross revenues bilgisi?
4. Tesla hakkında en güncel news item?

İpucu: Bazen aradığınız bilgiyi içeren larger response döndüren farklı bir URL kullanmanız gerekebilir.

<details><summary markdown='span'>Tüm çözümler
</summary>
<ol>
    <li><code>https://api.massive.com/v2/aggs/ticker/AMZN/range/1/day/2025-01-02/2025-02-03?apiKey=YOUR_API_KEY</code></li>
    <li><code>https://api.massive.com/v3/reference/tickers/META?apiKey=YOUR_API_KEY</code></li>
    <li><code>https://api.massive.com/vX/reference/financials?ticker=AAPL&timeframe=quarterly&limit=4&apiKey=YOUR_API_KEY</code></li>
    <li><code>https://api.massive.com/v2/reference/news?ticker=TSLA&limit=1&apiKey=YOUR_API_KEY</code></li>
</ol>
</details>

❗️ Kodunuzu **GitHub’a push etmeyi unutmayın**

---

## (Optional) Plotting *multiple* line charts

GAFA stock’larının (Google, Apple, Meta, Amazon) gelişimlerini **aynı chart üzerinde** karşılaştırmak istiyoruz.

👉 Yukarıdaki kodu yeniden kullanarak her stock için bir kolon içeren ve index olarak date kullanan bir dataframe oluşturun.

💡 İşi kolaylaştırmak için önce bir function yazabilirsiniz: `create_stock_df_of_company(company_code)`.
Bu function tek bir şirketin verisini dönsün.

Daha sonra tüm şirketler için bu function’ı kullanıp verileri concatenate edin ve pivot yapın.

💡 Her bir stock’u daha iyi karşılaştırmak için belki `t = 0` noktasında normalizasyon yapabilirsiniz!

---

## (Optional) Make the dates flexible

Şu ana kadar start ve end date değerlerini hard-coded kullandık.

👉 `create_stock_df_of_company(company_code)` function’ını refactor ederek her zaman son 90 günün verisini çekecek hale getirin.
