## Shape Challenge 📐

Shape Challenge’a hoş geldin! Haydi şekillerin heyecan verici dünyasına dalalım! 🎉

### Objective 🎯

Amacın, farklı şekiller için bir class hiyerarşisi oluşturmaktır. Üç tane class’ımız var: Shape, Rectangle ve Circle. Görevin, bu class’ları ve onlara ait method’ları implement etmektir.

### Classes and Methods 📝

#### Shape Class 🟨

Shape class, tüm şekiller için temel (base) class’tır ve aşağıdaki attribute’lara ve method’lara sahiptir:

Attributes:
- `name` 📛: Şeklin adını temsil eder.
- `color` 🌈: Şeklin rengini temsil eder.

Methods:
- `__init__(self, color, name)`: Verilen name ve color ile Shape object’ini initialize eder.
- `say_name(self)`: Şeklin adını döndürür. (ör. "My name is XYZ") 🗣️


#### Rectangle Class 🟦

Rectangle class, Shape class’tan inherit eder ve dikdörtgenlere özgü ek işlevler sunar:

Attributes:
- `width` ↔️: Dikdörtgenin genişliğini temsil eder.
- `height` ⬆️: Dikdörtgenin yüksekliğini temsil eder.

Methods:
- `__init__(self, color, name, width, height)`: Verilen name, color, width ve height ile Rectangle object’ini initialize eder.
- `say_name(self)`: Base class method’unu override ederek dikdörtgenin adını ve şekil tipini döndürür (ör. "My name is Rei and I am a rectangle"). 🗣️🟦
- `area(self)`: Dikdörtgenin alanını hesaplar ve döndürür. 📐
- `perimeter(self)`: Dikdörtgenin çevresini hesaplar ve döndürür. 📏

#### Circle Class 🟣

Circle class, Shape class’tan inherit eder ve dairelere özgü işlevler ekler:

Attributes:
- `radius` ⚪: Dairenin yarıçapını temsil eder.

Methods:
- `__init__(self, color, name, radius)`: Verilen name, color ve radius ile Circle object’ini initialize eder.
- `say_name(self)`: Base class method’unu override ederek dairenin adını ve şekil tipini döndürür (ör. "My name is Kvothe and I am a circle"). 🗣️🟣
- `area(self)`: Dairenin alanını hesaplar ve döndürür. 📐
- `perimeter(self)`: Dairenin çevresini hesaplar ve döndürür. 📏

### Testing ✅

Implementasyonunu test etmek için `tests` directory’si içinde verilen testleri çalıştırabilirsin. Terminalinde aşağıdaki komutu çalıştır:

```bash
make pytest
```