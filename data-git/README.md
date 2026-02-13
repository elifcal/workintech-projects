Bu süreç boyunca challenge’lar üzerinde çalışırken hatırlaman gereken git komutlarını hızlıca gözden geçirelim.

## Durum (Status)

Önce çalışma dizinimizin **clean**: olduğundan emin olalım: 

```bash
git status
```

Aşağıdaki sonucu görüyorsan, her şey tamam, bu challenge üzerinde çalışmaya başlayabilirsin:

```text
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

Bu mesajı görmüyorsan, başlamadan önce repo’yu commit etmen veya temizlemen gerekiyor.
İlk birkaç gün bir TA’den yardım almak için ticket açmaktan çekinme. git başlangıçta zor olabilir, mutlaka sor!

## İlk commit

Bir Python dosyası oluşturalım:

```bash
touch today.py
```

Bu dosyayı text editoründe aç.
my_name_is isminde, parametre almayan ve bir str sabiti döndüren bir function yazman gerekiyor.
Bu sabitin değeri GitHub kullanıcı adın olacak.

Bir test geçene kadar make komutunu çalıştır (ikinci testin geçmesine gerek yok, onunla birazdan ilgileneceğiz).

```text
tests/test_git.py::TestGit::test_hi_my_name_is PASSED
tests/test_git.py::TestGit::test_my_buddy_is   FAILED
```

Harika, ilerleme kaydettin. Şimdi durma zamanı—ilerlemeni kaydedelim. Bir nevi checkpoint gibi!

```bash
git add today.py
git commit -m "Implement my_name_is function"
git push origin master
```

Workintech bu değişikliği fark edecek ve ilerleme durumunu %50 olarak gösterecek. Tebrikler!

## İkinci commit

Şimdi ikinci testi çözmeye başlayalım. Bunun için my_buddy_is isimli, parametre almayan ve bir str sabiti döndüren bir function yazmalısın.
Bu sabitin değeri buddy’inin GitHub kullanıcı adı olacak (bugün buddy’in yoksa seninkini yazabilirsin :disappointed:).

Dosyada nelerin değiştiğini görmek için şu komutu kullanabilirsin:

```bash
git diff
```

Her şey yolundaysa commit edip GitHub’a push edebilirsin:

```bash
git add today.py
git commit -m "Implement my_buddy_is function"
git push origin master
```

## Making `pylint` happy (`pylint` 'i mutlu yapmak)

Bu noktada, 3 tane style hatası görmen gerekir:

```text
C0114: Missing module docstring (missing-module-docstring)
C0116: Missing function or method docstring (missing-function-docstring)
C0116: Missing function or method docstring (missing-function-docstring)
```

Şu anda docstring eksik. Bir tane module için, bir tane de her function için gerekiyor.
Docstring, bir module veya function hakkında kısa açıklama sağlar.

İlk hatayı düzeltmek için today.py dosyasının ilk satırına bir docstring ekle:

```python
"""A module computing buddy pair names for the day"""
```

Tekrar make çalıştır; bir style hatasının kaybolması gerekiyor.


Aynı işlemi iki function için de yap: tek satırlık docstring ekle.


Bittiğinde, challenge’ın üçüncü commit’ini yapma zamanı:

```bash
git diff
```

```bash
git add today.py
git commit -m "Fix style issues, should get a 'Good Style' now :pray:"
git push origin master
```

## Conclusion (Sonuç)

Artık Workintech’te nasıl gezineceğini, bir challenge’a nasıl konumlanacağını, onu bir text editor ile açıp üzerinde çalışmayı, ardından terminalde make ve bazı git komutlarını çalıştırmayı biliyorsun.
Tebrikler!