# PCD-R01 — Açıklamalı cevaplar

Önce [soru setini](../../scenarios/PCD-R01.md) tamamla. Kaynak kontrolü: 20 Eylül 2026. Sorular özgün çalışma sorularıdır.

## 1. B

İstenen, tek bir secret'ın metadata ve sürüm durumlarını okumak; değerini okumak veya değiştirmek değil. Secret kapsamındaki Viewer bu ihtiyaca uyar. A payload erişimi verir; C kapsamı gereksiz genişletir; D değiştirme ve payload erişimi dahil fazla yetki verir.

**Dil:** “neither … nor …” = ne … ne de …; “one known secret” = kimliği önceden bilinen tek secret. Soruda tüm secret'ları keşfetme/listeme gereksinimi yok.

**Kaynak:** [Secret Manager IAM](https://docs.cloud.google.com/secret-manager/docs/access-control).

## 2. D

Dosyalar zaten ortak `/workspace` alanında. Test yanlış dizine bakıyor; yolu düzeltmek yeterli. A beklemeyi uzatır ama dizinleri paylaşmaz. B kimlik ile dosya sistemi paylaşımını karıştırır. C çalışabilecek ek bir aktarım yolu kurar ama en küçük değişiklik değildir.

**Dil:** “a later test step” = sonraki bir test adımı; “within the same build” = aynı build çalışması içinde; “smallest change” = en küçük değişiklik. Önceki sette dosyanın yazıldığı yol yanlıştı; burada okunan yol yanlış.

**Kaynak:** [Build adımları arasında veri](https://docs.cloud.google.com/build/docs/configuring-builds/pass-data-between-steps).

## 3. A ve C

`orders` çağıran, `pricing` alıcı. A çağıranın kimliğine alıcı üzerinde çağrı izni verir. C istekte bu kimliği doğru hedefe yönelik ID token ile kanıtlar. İzin ve token birlikte gereklidir. B ters yön için yetki verir. D bu Cloud Run çağrısında gereken ID token yerine access token önerir.

**Dil:** “Which two actions … together?” = hangi iki işlem birlikte yapılmalı? “Neither account …” = iki hesabın da belirtilen izni yok. Önce çağrı yönünü `orders → pricing` olarak çiz.

**Kaynak:** [Servisten servise kimlik doğrulama](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

## 4. C

Sorun aynı instance içindeki eşzamanlı isteklerin ortak buffer'a yazması. Concurrency 1 bu isteklerin aynı instance'ta üst üste binmesini engeller. A aynı istemcinin yönlendirildiği instance ile ilgilidir; eşzamanlılığı sınırlamaz. B tek instance bıraksa da o instance birden fazla isteği birlikte işleyebilir. D daha fazla hazır instance tutar, her instance için çakışmayı engellemez.

Bu çözüm tüm servis genelinde tek istek çalışacağı anlamına gelmez; farklı instance'lar paralel çalışabilir. Soruda her istek başında sıfırlanan buffer var, instance'lar arasında paylaşılması gereken bir durum yok.

**Dil:** “one after another” = sırayla; “overlapping requests” = zaman olarak çakışan istekler; “cannot be changed before …” = belirtilen tarihten önce değiştirilemiyor.

**Kaynak:** [Cloud Run concurrency](https://docs.cloud.google.com/run/docs/about-concurrency).

## 5. A

Invoker izni zaten doğru. Eksik olan yeni bir rol değil, doğru hedef için alınmış token. Varsayılan durumda audience alıcı `pricing` servisinin URL'si olmalı. B ters yönde izin ekler. C gereksiz geniş yetki verir ve token hedefini düzeltmez. D bu çağrı için gereken token türünü yanlış değiştirir.

**Dil:** “already has” = zaten sahip; “before the application handles it” = uygulama isteği işlemeden önce. Bunlar mevcut doğru ayarı tekrar kurmak yerine hata noktasını bulmanı sağlar.

**Kaynak:** [Servisten servise kimlik doğrulama](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

## Değerlendirme

3. soru iki doğru seçeneğin birlikte seçilmesini gerektirir. Her soru 1 puan; kısmi puan yok. Teknik doğruluk dışında Türkçe özetin soruyu doğru anlayıp anlamadığını da değerlendir. Bu hedefli tekrar puanını tam deneme sonucu gibi yorumlama.
