Bir Python script’inin davranışını değiştirmenin (komut satırı argümanları dışında) başka bir yolu da environment variable kullanmaktır.

## Alıştırma

`flask_option.py`  dosyasını aç ve `start` function’ını implement et. Bu function, `FLASK_ENV` environment variable’ının varlığına ve değerine göre bir `String` döndürmelidir.

<details>
  <summary markdown='span'>💡 <code>FLASK_ENV</code>?</summary>

Flask, Python tabanlı bir web application framework’tür. (Evet, Python ile web uygulamaları da geliştirebilirsin.)

  Flask geliştiricileri, uygulamayı development ve production ortamlarında farklı şekilde yapılandırmak için `FLASK_ENV` environment variable’ını ayarlar.
Örneğin development modunda daha detaylı hata mesajları göstermek için.

Bu örnekte, `FLASK_ENV` değişkeninin değerine göre farklı bir mesaj yazdırarak bunu taklit ediyoruz.

</details>


Bir environment variable’ı tüm ortam için ayarlayabilir veya sadece çalıştıracağın komut için ayarlayabilirsin.
Bunu, komutun önüne `YOUR_ENV_VAR=some_value` yazarak yapabilirsin. Aşağıdaki örneklerde olduğu gibi:


Beklenen davranış şöyle:


```bash
FLASK_ENV=development python flask_option.py
# => "Starting in development mode..."

FLASK_ENV=production python flask_option.py
# => "Starting in production mode..."

python flask_option.py
# => "Starting in empty mode..."
```
 
💡 **İpucu**: os modülündeki os.getenv fonksiyonuna bir göz at.
