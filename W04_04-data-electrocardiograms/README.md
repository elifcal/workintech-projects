# Electrocardiograms

## Veri setini indirin

Veri seti [buradan](https://d32aokrjazspmn.cloudfront.net/materials/ML_Electrocardiograms_dataset.csv) edinilebilir. Aşağıdaki komutlarla indirip `02-Electrocardiograms` dizinindeki `data` klasörüne kaydedelim:

```bash
curl https://d32aokrjazspmn.cloudfront.net/materials/ML_Electrocardiograms_dataset.csv > data/electrocardiograms.csv
```

## Veri seti

- Veri setinin her gözlemi, bir hastanın electrocardiogram (ECG)'ından alınan sayısal olarak temsil edilmiş kalp atışıdır.
- `target` ikili değerlidir ve kalp atışının kardiyovasküler hastalık riski altında olup olmadığını tanımlar [1] veya değildir [0].

## Alıştırma

🎯 Göreviniz kardiyovasküler hastalık riski altındaki kalp atışlarını işaretlemektir. Şunları yapacaksınız:

- Veri setinin sınıf dengesini araştırın
- İki modeli değerlendirin ve karşılaştırın: KNN ve LogisticRegression
- Modellerin performansları hakkında içgörü elde etmek için Confusion matrix ve Classification report kullanın
- Uygun metriğe dayalı olarak optimal modeli seçin

Alıştırmaya başlamak için `jupyter notebook`'ta `Electrocardiograms.ipynb`'yi açın ve talimatları takip edin.

🚀 Sıra sizde!

