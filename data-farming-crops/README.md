## 🎯 Amaçlar

Bu alıştırmada, **inheritance** (kalıtım) kavramının faydalarını keşfetmek için adım adım kodlayacağınız küçük bir çiftçilik senaryosu bulunuyor.

Ayrıca yalnızca yazdığınız kodla ilgili testleri nasıl çalıştıracağınızı da göreceksiniz.

## 📝 Şartlar

Çiftlikte iki tür **ekin** vardır: pirinç (rice) ve mısır (corn).

![Crops](https://drive.google.com/file/d/12Oz1kuBFAg7dFPFieGbzsNP3YbAbeNqQ/view?usp=drive_link)

**ÖNEMLİ:** Bu challenge’da sınıfları doğrudan `make` kullanarak yazmayın! Önce `farm/farming_diary.py` dosyasındaki arayüzü (interface) kodlayın ve programın sizi yönlendirmesine izin verin. Her bölümün sonunda arayüz beklenen çıktıyı gösterdiğinde, sınıf kodlarınızı `make` ile kontrol edin 👌

---

### 🌽 `Corn` sınıfı

Başlamak için, `farm/corn.py` içinde aşağıdaki özelliklere göre bir `Corn` sınıfı yazın:

* `grains` isimli instance variable'ı sıfırla başlatılır.
* `water` metodu her çağrıldığında 10 tane grain ekler.
* `ripe` metodu grain sayısı en az 15 ise `True`, değilse `False` döner.

`farm/farming_diary.py` dosyasını açın ve **Day One** bölümünü tamamlayın. Kodun şu çıktıyı vermesi gerekir:

```bash
📝 Day One: Corn
The corn crop produced 10 grains
The corn crop is not ripe
```

Günlüğünüzü çalıştırmak için:

```bash
python -m farm.farming_diary
```

`Corn` sınıfının testlerini çalıştırmak için:

```bash
pytest -v tests/test_corn.py
```

Tüm testleri geçtiyseniz `make` çalıştırabilirsiniz. Bu aşamada 12 failed ve 6 passed test görmelisiniz.

Şimdi commit ve push etme zamanı:

```bash
git add farm/corn.py farm/farming_diary.py
git commit -m "Completed Corn"
git push origin master
```

---

### 🌾 `Rice` sınıfı

`farm/rice.py` dosyasında bir `Rice` sınıfı oluşturun ve `Corn` sınıfındaki tüm metotları kopyalayın.

* `water` metodu yalnızca 5 grains eklemelidir.
* `ripe` metodu `Corn` ile aynı davranışı sergiler.
* `Rice` sınıfına özel `transplant` isimli bir metod ekleyin; bu metod 10 grain daha üretir.

Günlüğünüzde **Day Two** bölümünde pirinç ekerek devam edin.

Programınız sorunsuz çalıştığında testleri çalıştırabilirsiniz:

```bash
pytest -v tests/test_rice.py
```

Tüm testleri geçtiyseniz `make` çalıştırın. Bu aşamada 6 failed ve 12 passed test görmelisiniz.

Ardından bu iki dosyayı commit ve push edin (komutlar bir önceki adımla aynı mantıkta).

---

### 🔀 Refactoring

Kod kopyalayıp yapıştırırken rahatsız hissettiyseniz haklısınız! Kod tekrar etmek daha çok bakım gerektirir ve hata riskini artırır. İşte burada **inheritance** devreye girerek kodu DRY (Don't Repeat Yourself) hâline getirir.

Ekinlerin birçok ortak özelliği var, bu yüzden refactor ederek:

* `farm/crop.py` içinde `Crop` isimli bir **parent class** oluşturun ve ortak metotları buraya taşıyın.
* `Corn` ve `Rice` sınıflarını `Crop` sınıfından **inherit** edecek şekilde güncelleyin.
* `farm/corn.py` ve `farm/rice.py` içinde `Crop` sınıfını import etmeyi unutmayın.

---

## ✅ Kontroller ve Kazanımlar

Şimdi `make` çalıştırarak tüm testleri çalıştırın! Tüm testleri geçmek, mimarinizin ve sınıf arayüzlerinizin doğru olduğunu doğrular.

Tüm testleri geçtikten sonra `git status` ile değişen dosyaları kontrol edin, commit ve push edin.

Ardından stil kontrolünden de 10/10 aldığınızdan emin olun. Sonra tekrar commit ve push edin.

Tebrikler! Testleri çalıştırmadan önce *programın* sizi sınıf tasarımına yönlendirmesine izin vermek, geliştirici olarak bağımsızlık kazanmanızda önemli bir adımdır.
