# PCD-S02 — İlk bildirilen deneme sonucu

Tarih: 22 Eylül 2026. Kaynak: kullanıcının sohbet beyanı: yalnız 12. soru yanlış, süre 20 dakika.

**Sonuç: 14/15 (%93,3), 20 dakika.** Ortalama 80 saniye/soru. Cloud Run 5/5, Cloud Run functions 5/5, GKE 4/5; bu dağılım kullanıcı beyanından çıkarılmıştır.

Soru dosyası yeniden okundu; cevap alanları boş. Seçenek bazında kontrol yapılmadı ve kullanıcı adına cevap harfi doldurulmadı. Q12'de seçilen yanlış şık, güven düzeyleri, gerekçeler ve kaynak/destek kullanımı bildirilmedi. Sonucu doğrulanmış bağımsız seçenek değerlendirmesi olarak sunma.

## Geri bildirim ve hata ayrımı

Kullanıcı soruları uzun bulduğunu, odaklanmakta zorlandığını ve yorgun olduğunu belirtti. Bu koşullar kaydedildi; tek hatanın nedeninin yorgunluk olduğu sonucuna varılmadı. Sonraki mesajda readiness/liveness/startup probe konularına tam hakim olmadığını açıkladı. Hata sınıfı kullanıcı beyanıyla teknik kavram eksikliği olarak güncellendi; seçtiği yanlış şık hâlâ bilinmiyor. Uzun cümlelere alışmak istediğini belirterek kısaltma önerisini reddetti. Sınavı çok kolay buldu; bu sonuç gerçek sınava hazır olma ölçüsü olarak genellenmemeli.

## Q12 açıklaması

Doğru cevap C: readiness probe. İstenen, toparlanabilen sağlıklı process'i yeniden başlatmadan Pod'a yeni Service trafiğini durdurmak ve iyileşince sürdürmek. Readiness trafik almaya uygunluğu, liveness yeniden başlatma ihtiyacını, startup başlangıç tamamlanmasını kontrol eder. Belirleyici ifade: “can recover without restarting”.

[Ek resmî kaynak](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/). Bu probe ayrıntısı set hazırlanırken ek resmî kaynak olarak etiketlenmişti.

Açıklama sonrası kavrayış henüz teyit edilmedi; ilk sonuç 14/15 olarak korunur. Farklı senaryoda gecikmeli kontrol hedefi 25 Eylül, sonra başarıya göre 29 Eylül; otomasyon değil çalışma kuyruğudur.

## Sonraki set

PCD-S03: üç alanın kapsamını ve uzun İngilizce senaryoları koru. Önceki 2–3 kısa cümle önerisi kullanıcı tarafından reddedildi. Çok koşullu kararlar, birbirine yakın makul alternatifler ve servisler arası etkileşimlerle zorluğu artır. Kullanıcı henüz yeni set istemedi; geri bildirim kaydedildi. İlk sonuç 14/15 ve 20 dakika olarak değişmeden korunuyor.
