# Scraping Egzersizi — Python ile Web Sitesinden Kitap Verisi Çekme

Bu alıştırmada, derste ele alınan Scraping tekniklerini pratiğe dökeceğiz. Amacımız, Python kullanarak bir web sitesinden otomatik olarak bilgi çıkarmak olacaktır.

Scraping yapacağımız web sitesi: [books.toscrape.com](http://books.toscrape.com/). Bu site tam olarak bizim amacımız için oluşturulmuştur — scraping nasıl yapılır öğrenmek için!

Hedefimiz, satılan kitaplar hakkında isimleri, fiyatları, rating değerleri vb. bilgileri otomatik olarak elde etmektir. İşin püf noktası ise web sitesinin **paginated** olmasıdır. Bunu fark edebiliyor musun? Bunun bir zorluk yaratacağını öngörüyor musun?

## Setup

Amaç, web sitesini scrape etmek **ve** ardından elde edilen bilgileri `pandas` kullanarak görselleştirmektir. Bu alıştırma için Notebook içinde çalışmak hâlâ mantıklıdır.

```bash
jupyter notebook
```

`~/code/<user.github_nickname>/{{local_path_to("02-Data-Toolkit/02-Data-Sourcing/02-Scraping")}}` klasöründeki yeni Python Notebook dosyasını aç.

Python dünyasında scraping için kullanımı kolay bir library olan `BeautifulSoup` mevcuttur. Kurulum sırasında bunu yüklemiştik, dolayısıyla doğrudan import edebiliriz.

Bunu `requests` library’si ile birlikte kullanacağız: `requests` HTML sayfasını çekmemize yardımcı olacak, `BeautifulSoup` ise bu sayfadan bilgileri extract etmemizi sağlayacaktır.

Notebook’un ilk code cell’ine aşağıdaki import’ları ekleyerek başla:

```python
import requests
from bs4 import BeautifulSoup

import numpy as np
import pandas as pd

%matplotlib inline
import matplotlib.pyplot as plt
```

## First request

Yeni bir cell ekle ve aşağıdaki `TODO` alanları üzerinde çalış (başlangıç kodu derste kullanılan slaytlardakiyle aynıdır!):

```python
url = "http://books.toscrape.com/"

# TODO: Use `requests` to do an HTTP request to fetch data located at that URL
# TODO: Create a `BeautifulSoup` instance with that data
```

<details><summary markdown='span'>Çözümü görüntüle
</summary>

Bu kod oldukça geneldir ve derste gördüğümüzle aynı olmalıdır! Eğer zaten bir scraping projen varsa, genellikle yaptığın şey projeyi açıp bu ilk satırları kopyalayıp yapıştırmaktır!

```python
url = "http://books.toscrape.com/"

# This is where we do an HTTP request to get the HTML from the website
response = requests.get(url)

# And this is where we feed that HTML to the parser
soup = BeautifulSoup(response.content, "html.parser")
```

</details>

Yeni bir code cell içinde `soup` değişkenini incele. Tipi nedir? İlk bakışta string gibi görünebilir, fakat gerçekten öyle mi? `type(soup)` ile kontrol et.

`soup` artık HTML üzerinde sorgular çalıştırabileceğimiz parser içeren bir BeautifulSoup object’idir. Hangi HTML elementlerini extract etmek istediğini belirlemek için, *Books to Scrape* web sitesinin HTML yapısını browser inspector ile analiz etmen gerekir.

Browser inspector kullanmak için, incelemek istediğin elemente sağ tıkla ve menüden `Inspect` seçeneğini belirle.

![Website ve inspector ekran görüntüsü](img dosyasında)

Tek bir kitabı içeren HTML yapısını fark edebiliyor musun? Her kitap için bu yapı aynı mı?

<details><summary markdown='span'>Çözümü görüntüle
</summary>

Aradığımız yapı, `product_pod` class’ına sahip `<article />` elementidir! Sayfadaki tüm kitaplar birebir aynı structure’a sahiptir, parsing için tam olarak ihtiyacımız olan da budur.

```html
<article class="product_pod">
  <!-- [...] -->
</article>
```

</details>

Artık ilgili HTML’yi tespit ettiğimize göre, `soup` Python değişkenini kullanarak document üzerinde sorgu yapabiliriz. [searching by CSS class](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class) yaklaşımını kullanalım. Yeni bir cell ekleyerek HTML içindeki **tüm** kitapları seçmeyi dene ve bunu `books_html` değişkenine ata.

<details><summary markdown='span'>Çözümü görüntüle
</summary>

```python
books_html = soup.find_all("article", class_="product_pod")
len(books_html)
```

</details>

Artık tüm `<article />` elementlerini içeren bir `books_html` değişkenimiz var, şimdi **tek bir** kitap (ilk kitap!) üzerinde odaklanalım ve bu HTML parçasından ihtiyacımız olan tüm bilgileri extract etmeye çalışalım.

## Parsing *one* book

Bu noktada bir **Markdown cell** ekleyip şunu yazman iyi olacaktır:

```markdown
## Parsing _one_ book
```

Elbette daha fazla metin de yazabilirsin! Buradaki amaç, Notebook içinde düşünce sürecini dokümante ederek iyi yapılandırılmış bir Notebook elde etmektir.

İlk kitabın HTML parçasına bakalım. Yeni bir code cell ekle ve şunu yaz:

```python
books_html[0]
```

Harika! Artık uğraşacağımız daha küçük bir HTML parçamız var.

String gibi görünüyor, değil mi? Ama artık daha iyisini biliyoruz! `type()` ile kontrol et. Tekrar daha gelişmiş bir object olduğunu göreceksin.

Bu HTML parçası üzerinde [`.find()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find) method’unu zincirleme kullanarak 3 farklı bilgiyi extract edebiliriz.

### Kitap başlığını bulmak — attribute içinden text almak

Kitap *title*’ı ile başlayalım. Bu bilgiyi `books_html[0]` içinden elde etmeye çalış ve `book_title` değişkenine ata.

Başlığı Notebook’ta gösterdiğin HTML kodu içinde bulmayı deneyebilirsin. Alternatif olarak browser’a dönüp tekrar Inspect fonksiyonunu kullanarak başlığı içeren elementi bulabilir ve oradan `<article>` seviyesine kadar yukarı çıkabilirsin.

<details><summary markdown='span'>Çözümü görüntüle (sadece <strong>kendin denedikten sonra</strong>!)
</summary>

Başlık `<h3 />` tag’inin içindeki `<a />` link tag’inde yer alır. Önce `h3`, ardından `a` elementini bulmamız gerekir:

```python
books_html[0].find("h3").find("a")
```

Neredeyse tamam. Şimdi `<a />` tag’inin **attributes** alanındaki title değerini seçmeliyiz:

```python
books_html[0].find("h3").find("a").attrs
```

Bu satır bir `dict` döndürür. Artık doğru key’i seçebilirsin:

```python
book_title = books_html[0].find("h3").find("a").attrs["title"]
book_title
```

</details>

### Kitap fiyatını bulmak — element içinden sayıya dönüştürmek

Harika! Şimdi kitap fiyatını elde etmeye çalışalım. Browser’daki element incelemesinden fiyatın `<p class="price_color"></p>` içinde olduğunu görebilirsin. Bu değeri `book_price` değişkenine ata ve dikkat et, `float` tipinde olmalı!

<details><summary markdown='span'>Çözümü görüntüle (sadece <strong>kendin denedikten sonra</strong>!)
</summary>

Kitapları seçerken yaptığımız gibi burada da CSS class ile seçme yaklaşımını kullanacağız ve [`.string`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#string) method’undan faydalanacağız:

```python
books_html[0].find("p", class_="price_color").string
```

Burada amacımız sadece text değil, **sayı** (Python `float`) elde etmektir. Bunun için ilk karakter olan `£` işaretini slice yöntemiyle kaldırmalı ve ardından `float()` method’una göndermeliyiz:

```python
book_price = float(books_html[0].find("p", class_="price_color").string[1:])
book_price
```

</details>

### Kitap rating bilgisini bulmak

Son olarak kitabın **rating** bilgisini (kaç sarı yıldızı olduğu) elde etmeliyiz. Browser inspector’da `<p class="star-rating TEXT"></p>` şeklinde bir yapı göreceksin. Buradaki `TEXT` şu değerlerden biri olabilir: "One", "Two", "Three", "Four" veya "Five". Bu biraz daha karmaşık olsa da yapılabilir. Yeni bir cell aç ve aşağıdaki kodu kopyala/yapıştır:

```python
book_stars_html = books_html[0].find("p", class_="star-rating")
book_stars_html
```

```python
book_stars_html.attrs['class']
```

Python’da `in` keyword’ü bir öğenin bir `list` içinde olup olmadığını kontrol etmek için kullanılır. Örneğin:

```python
cities = [ 'paris', 'london', 'brussels' ]

if 'berlin' in cities:
    print("Berlin is available")
else:
    print("Sorry, Berlin is not available")
```

:question: `<p />` içinden gelen class list’ini alıp 1 ile 5 arasında rating döndüren bir `parse_rating` method’u tanımla:

```python
def parse_rating(rating_classes):
    # TODO: Look at `rating_classes` and return the correct rating
    # e.g. of an argument for `rating_classes`: [ 'star-rating', 'Three' ]
    # "One" => 1
    # "Two" => 2
    # "Three" => 3
    # "Four" => 4
    # "Five" => 5
    return 0
```

<details><summary markdown='span'>Çözümü görüntüle (sadece <strong>kendin denedikten sonra</strong>!)
</summary>

```python
def parse_rating(rating_classes):
    """
    Parses the rating classes and returns the rating

    Parameters
    ----------
    rating_classes : str
        The rating classes of the book: these are the classes of the stars element in the HTML

    Examples
    --------
    >>> rating_classes = ['star-rating', 'Three']
    >>> parse_rating(rating_classes)
    3
    """
    # Define the ratings: mapping from English to numerical
    ratings = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    # For each of the 5 possible ratings, check if it's in the rating classes
    for rating in ratings:
        if rating in rating_classes:
            return ratings[rating] # Found the rating, return the numerical value
```

</details>

Bu method’u implement ettikten sonra kitabın rating değerini okuyabilirsin! Yeni bir cell aç ve aşağıdaki kodu yapıştır:

```python
book_rating = parse_rating(books_html[0].find("p", class_="star-rating").attrs['class'])
```

## Parsing *all* books

Bir kez daha, yeni bir **Markdown cell** ekleyip şunu yazmanın zamanı:

```markdown
## Parsing _all_ books
```

Şimdiye kadar yalnızca **ilk** kitap için parsing kodu yazdık. Artık bu kodu `books_html` değişkenindeki tüm kitaplar üzerinde çalışacak bir `for` loop içine yerleştirmemiz gerekiyor!

Toplanan kitap bilgilerini bir **Python `dict`** içinde saklayacağız. Bu dictionary üç key’e sahip olacak: `Title`, `Price` ve `Rating`. Bu key’lerin values kısmı ise tüm kitapların values’larını içeren `list`’ler olacaktır:

* `Title` => `["A light in the attic", "Tipping the Velvet", ...]`
* `Price` => `[51.77, 53.74, ...]`
* `Rating` => `[3, 1, ...]`

Bu yapıyı seçiyoruz çünkü bu format Pandas’a doğrudan veri aktarmamızı ve kolaylıkla bir Dataframe oluşturmamızı sağlar.

Yeni bir cell ekleyerek dictionary’i başlat:

```python
books_dict = { 'Title': [], 'Price': [], 'Rating': [] }
```

:question: `books_html` üzerinde iterate ederek `books_dict` içini dolduracak bir loop yaz ve yukarıdaki tüm kodu tekrar kullan.

<details><summary markdown='span'>Çözümü görüntüle (sadece <strong>kendin denedikten sonra</strong>!)
</summary>

```python
for book in books_html:
    title = book.find("h3").find("a").attrs["title"]
    price = float(book.find("p", class_="price_color").text[1:])
    rating = parse_rating(book.find("p", class_="star-rating").attrs['class'])
    books_dict["Title"].append(title)
    books_dict["Price"].append(price)
    books_dict["Rating"].append(rating)
```

</details>

Sonuçları kontrol etmek için aşağıdaki cell’leri çalıştır:

```python
books_dict
```

```python
len(books_dict)          # 3 key:value çifti olmalı
```

```python
len(books_dict["Title"]) # Her listede 20 kitap olmalı
```

## Pandas'a Veri Yükleme

Yeni bir section! Süreci dokümante etmek için yeni bir **Markdown cell** oluşturmayı unutma.

`books_dict` iyi görünüyor, şimdi bu veriyi Pandas’a yükleyelim:

```python
books_df = pd.DataFrame(books_dict)
books_df
```

Harika görünüyor! Küçük bir plot oluşturarak kutlayalım. Bu grafik her **Rating** değeri için kaç kitap olduğunu gösterecek:

```python
books_df.groupby("Rating").count()["Title"].plot(kind="bar")
```

### Kodunu test et!

Test etmek için aşağıdaki cell’i ekle ve çalıştır:

```python
from nbresult import ChallengeResult

result = ChallengeResult('books',
    columns=books_df.columns,
    title=str(books_df.loc[0,'Title']),
    price=books_df.loc[0,'Price'],
    rating=books_df.loc[0,'Rating']
)
result.write()
print(result.check())
```

Ardından kodunu `commit` ve `push` edebilirsin 🚀

Oldukça fazla kitabın düşük rating (1) aldığını görebilirsin. Belki de bu sadece ilk sayfadaki kitaplara özgüdür? Peki ya **diğer** sayfalar?

## Tüm katalog sayfalarını gezmek

Yeni bir bölüm! **Markdown cell** eklemeyi unutma.

[books.toscrape.com](http://books.toscrape.com/) sitesinde en alta in ve "Next" butonuna tıkla. Tekrar tıkla. Farklı sayfalar için URL pattern’ını görebiliyor musun?

<details><summary markdown='span'>Çözümü görüntüle
</summary>

```python
page = 1
url = f"http://books.toscrape.com/catalogue/page-{page}.html"
url
```

</details>

Bir `for` loop daha gerekiyor! Bu loop 1’den 50’ye kadar tüm sayfaları gezerek scraping yapacak. Şimdilik test için 1–3 arası sayfaları alalım:

```python
MAX_PAGE = 3
for page in range(1, MAX_PAGE + 1):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    print(url)
```

Loop çalışıyor gibi görünüyor! Artık `print` yerine gerçek scraping kodunu yazabiliriz.

<details><summary markdown='span'>Çözümü görüntüle
</summary>

```python
all_books_dict = { 'Title': [], 'Price': [], 'Rating': [] }

MAX_PAGE = 50
for page in range(1, MAX_PAGE + 1):
    print(f"Parsing page {page}...")
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for book in soup.find_all("article", class_="product_pod"):
        title = book.find("h3").find("a").attrs["title"]
        price = float(book.find("p", class_="price_color").text[1:])
        rating = parse_rating(book.find("p", class_="star-rating").attrs["class"])
        all_books_dict["Title"].append(title)
        all_books_dict["Price"].append(price)
        all_books_dict["Rating"].append(rating)

print("Done!")
```

</details>

Şimdi gerçekten `MAX_PAGE * 20` kitap parse edildi mi kontrol et:

```python
len(all_books_dict["Title"])
```

Şimdi `all_books_dict` verisini Pandas DataFrame’e dönüştürelim:

```python
all_books_df = pd.DataFrame.from_dict(all_books_dict)
all_books_df.tail()
```

Kitapların fiyat dağılımını inceleyelim:

```python
all_books_df["Price"].hist()
```

Ve rating dağılımını görelim:

```python
all_books_df.groupby("Rating").count()["Title"].plot(kind="bar")
```

## Veriyi daha sonra kullanmak için kaydetmek

Şu anda tüm scraped data Notebook’un memory’si içinde yer almakta ve kernel yeniden başlatıldığında kaybolacaktır. Bu nedenle, scraping işlemi sonrası veriyi bir dosyaya kaydetmek iyi bir pratiktir.

Pandas’ın sunduğu [writers](https://pandas.pydata.org/docs/user_guide/io.html) yardımıyla DataFrame’i diske yazabiliriz:

```python
all_books_df.to_csv("books.csv")
```

Excel formatında da kaydedebilirsin:

```bash
pip install XlsxWriter
```

```python
all_books_df.to_excel('books.xlsx', sheet_name='Books')
```

İyi bir pratik, **Data Pipeline** oluşturarak bir sürecin veriyi scrape edip CSV’ye yazması, diğer bir sürecin ise bu veriyi CSV’den okuyarak analiz etmesidir.

💡 Kodunu GitHub’a **push** etmeyi unutma

## Refactoring hakkında

Birbirinden farklı işler yapan oldukça fazla kod yazdık. Bu kodu daha okunabilir ve tekrar kullanılabilir hale getirmek için daha küçük function’lara bölmek iyi bir pratiktir:

* `fetch_page` → Tek bir sayfayı alır ve `soup` oluşturur
* `add_books_to_dict` → Tek bir sayfadaki kitap bilgilerini dictionary’e ekler
* `create_books_df` → Belirli sayıda sayfayı gezer, önceki iki function’ı kullanarak DataFrame oluşturur

Zamanın varsa bir sonraki aşamaya geçmeden önce kodunu bu şekilde refactor etmeyi dene.

Eğer vaktin yoksa, çözüm yayınlandığında göz atarak kodun okunabilirliğinin nasıl iyileştiğini inceleyebilirsin!
