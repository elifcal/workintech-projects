Debugging, kodundaki problemleri bulma ve çözme sürecidir.

[...] interactive debugging, control flow analizi, unit testing, integration testing, log dosyası analizi, uygulama veya sistem seviyesinde monitoring, memory dump’lar ve profiling gibi işlemleri içerebilir.

Bu alıştırmada debugging’in temelleri olan interactive debugging ve control flow analysis üzerinde odaklanacağız.

## Python Debugger

Python’ın güzel özelliklerinden biri, kullanıma hazır bir built-in debugger ile gelmesidir!
Biz pdb’nin daha gelişmiş bir versiyonu olan ipdb kullanacağız—tab completion, syntax highlighting gibi kolaylıklar sunuyor.

Hemen konuya girelim. Bu alıştırmanın klasöründe hello.py isminde bir program bulacaksın. Bu programda bir bug var; Python debugger kullanarak bunu bulalım!

```bash
python hello.py john lennon
```

Programın çıktısında problem ne? Görünüşe göre birleştirilmiş full name oluşturulurken bir sorun var.
Debug edelim! def full_name satırının hemen altına şu satırı ekle: 

```python
breakpoint() # equivalent to `ipdb.set_trace()`
```

`breakpoint()` programı o satırda durdurmamızı sağlar (arka planda `ipdb.set_trace()` çağırır). 

Terminale dön ve komutu tekrar çalıştır:

```bash
python hello.py john lennon
```

Program, breakpoint() eklediğin satırda duracaktır (**pause**) :

```bash
> [...]{{local_path_to("01-Python/01-Programming-Basics/04-Debugging")}}/hello.py(8)full_name()
      7     """returns the full name"""
----> 8     name = f"{first_name.capitalize()}{last_name.capitalize()}"
      9
```

Debugger ile oynama zamanı. Buradan itibaren iki şey yapabilirsin:

Control flow yönetmek: bir sonraki satırı çalıştırmak, bir function içine girmek veya dışına çıkmak.

breakpoint()’ten önce tanımlanan değişkenlere bakmak. Program durduğu için “arka planda” ne olduğunu yakından inceleyebilirsin.

Şunu yaz:

```bash
ipdb> sys.argv
# => ['hello.py', 'john', 'lennon']
```
Nasıl çalıştığını gördün mü? Debugger’dan sys.argv’u göstermesini istedin.Bu Python scriptine verilen komut satırı argümanlarını içeren bir **list**. argv[0] her zaman script’in adıdır. 

Sorun şu ki John ve Lennon arasında boşluk yok. Bu nedenle local değişken name’e bakalım. Yazalım:

```bash
ipdb> name
# => *** NameError: name 'name' is not defined
```

Neden NameError aldık? Program tam olarak nerede durdu? Durduğu satırı görmek için şunu yazabilirsin::

```bash
ipdb> ll
#     5 def full_name(first_name, last_name):
#     6     breakpoint()
#     7     """returns the full name"""
# ----> 8     name = f"{first_name.capitalize()}{last_name.capitalize()}"
#     9
#     10     return name
#     11
```

Program ok işaretinin (->) olduğu satırın öncesinde durdu.Bu da `name`  değişkeninin henüz tanımlanmadığı anlamına geliyor.Bu yüzden “name is not defined” hatası alıyoruz. Tamam, şimdi net!

Bir function içindeyiz. Şu anki function’ın argüman listesini görmek faydalı olabilir:

```bash
ipdb> args
# => first_name = 'john'
# => last_name = 'lennon'
```

Şimdi ne yapabiliriz? Debugger’a bir sonraki satırı çalıştırmasını söyleyebiliriz:

```bash
ipdb> next
> [...]{{local_path_to("01-Python/01-Programming-Basics/04-Debugging")}}/hello.py(10)full_name()
      9
---> 10     return name
     11
```

Debugger bir satır ilerledi ve o satırı çalıştırdı. Programın şu anda nerede durduğunu görmek için:

```bash
ipdb> ll
```

Ok işaretinin  (`--->`) ilerlediğini görüyor musun? Şimdi `name`  değişkenine bakabiliriz:

```bash
ipdb> name
# => 'JohnLennon'
```

İşte bu! Hata tespit edildi! String interpolation’da boşluk eksik.

Programı bir sonraki breakpoint’e (başka yoksa sonuna kadar) çalıştırmak için:

```bash
ipdb> continue
```

`hello.py` içerisindeki full_name` method’unu düzelt ve programı tekrar çalıştır.Debugger’ı kaldırmayı unutma!(**remove the debugger**! ) Bu çok kolay unutulan bir şeydir ve yanlışlıkla commit’e eklenebilir. Bazı ekipler bu durumu önlemek için ek kurallar koyar.


## Daha İleri

Önceki bölüm debugger’ın temel komutlarını anlamaya yönelikti. Debugger’ı şu tuşlara sahip bir DVD oynatıcı gibi düşünebilirsin:

- Pause (`breakpoint()` in the source code)
- Next frame (`next`)
- Play (`continue`)

`step` veya `return` gibi daha birçok debugger komutu da vardır.


## Bu Challenge’ın Çözümü

Artık hatalı kod nasıl debug edilir biliyorsun. Şimdi bu challenge’ın testlerini çalıştırabilirsin (önce breakpoint() satırını kaldırmayı unutma (**remove the breakpoint()** first)):

```bash
make
```

İstediğimiz implementasyonun biraz daha karmaşık olduğunu fark edeceksin. `full_name` method’unun whitespace konusunda doğru davranmasını istiyoruz—hem eksik first name hem de eksik last name durumlarında. 
 