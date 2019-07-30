# borsa-hisse-data
Foreks.com isimli sitenin sunmuş olduğu API aracılığıyla sitedeki döviz ve hisse bilgilerinin belirtilen tarihler arasındaki verilerinin excel dosyasına geçirilmesi.

# doviz.py
Script iki part şeklinde çalışıyor. İlk partta sitedeki dolar, euro, pound ve isviçre frangı kurlarının baslangıç ve bitiş olarak script içerisinde belirtilen 
tarihler arasındaki verilerini, ikinci partta script içerisindeki hisselerin hacimleri ile birlikte verileri alınarak en sonunda excel 
dosyasına yazılıyor.

# doviz-main.py
Önceden excel formatında yazdırılmış veriler içerisinden VAKBN hissesi ve aynı tarihli dolar verileri önce bir data framede birleştiriliyor. Ardından her bir tarih için basitçe son n günlük ortalama değer ve ortalama artış yüzdesi filtreleri her bir nümerik sütuna uygulanıyor. Bu işlem kabaca, giriş seviyesinde bir feature generating işlemi sayılabilir.
