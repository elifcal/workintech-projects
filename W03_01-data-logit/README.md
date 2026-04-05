## Logistic Regression

11% oranında orders 1-yıldız review aldığı için birçok müşterinin mutsuz olduğunu gördük.

Çoğu zaman, her order’ın tam review skorunu doğru tahmin etmekten ziyade en kötü review’ları (1 yıldız) açık şekilde tespit edebilmek daha önemlidir.

Bu challenge’da, `orders` training set’imizden `dim_is_one_star` için bir Logit model çalıştıracağız ve bunu `review_score` için yaptığımız OLS tahminiyle karşılaştıracağız.

Ayrıca `dim_is_five_star` için bir Logit modeliyle de karşılaştıracağız.

`logit.ipynb` notebook’unu açın ve talimatları takip edin.
