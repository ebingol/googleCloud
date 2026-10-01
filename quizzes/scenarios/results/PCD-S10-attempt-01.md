# PCD-S10 — İlk deneme sonucu

1 Ekim 2026. Kullanıcı 20 cevabını ve **42 dakika** çözüm süresini sohbette bildirdi. Mevcut ayrı cevap anahtarıyla karşılaştırma: **19/20 (%95)**. 45 dakikalık kişisel hedefin 3 dakika altında; ortalama **2 dakika 6 saniye/soru**. Q6 A+C ve Q18 B+E çift seçimleri tam doğru; kısmi puan verilmedi.

İlk cevaplar aşağıda korunur. Eminlik, gerekçe, mola ve kaynak/yardım koşulları bildirilmedi; yardımsız kesintisiz sınav veya kalıcı öğrenme sonucu varsayılmaz. Açıklama sonrası cevaplar ilk puanın yerine geçmez. Soru dosyasındaki cevap alanları değiştirilmedi.

| Soru | İlk cevap | Anahtar | Sonuç |
|---|---|---|---|
| 1 | C | C | Doğru |
| 2 | D | D | Doğru |
| 3 | C | C | Doğru |
| 4 | C | C | Doğru |
| 5 | D | D | Doğru |
| 6 | A+C | A+C | Doğru |
| 7 | A | A | Doğru |
| 8 | C | C | Doğru |
| 9 | A | A | Doğru |
| 10 | D | D | Doğru |
| 11 | B | B | Doğru |
| 12 | C | C | Doğru |
| 13 | C | B | Yanlış |
| 14 | D | D | Doğru |
| 15 | A | A | Doğru |
| 16 | A | A | Doğru |
| 17 | B | B | Doğru |
| 18 | B+E | B+E | Doğru |
| 19 | B | B | Doğru |
| 20 | B | B | Doğru |

## Q13 — ilk C, doğru B

Senaryo: Browser Firebase ID token ve değiştirilebilir userId gönderiyor; backend token doğrulamadan userId ile kayıt seçiyor. C, kontrolü browser'a bırakıp backend'in userId'ye güvenmesini sürdürüyor. İstemci saldırganın kontrolünde olabilir. B, backend'de doğru project için yapılandırılmış Admin SDK ile ID token'ı doğrular, UID'yi doğrulanmış token'dan çıkarır ve bu kimliğin erişebileceği hesap kayıtlarını sınırlar.

Kısa geri bildirim verildi; yanlışın teknik bilgi, İngilizce anlam veya başka nedenden kaynaklandığı kullanıcı gerekçesi olmadan sınıflandırılmadı. Açıklama sonrası kavrayış veya bağımsız tekrar henüz doğrulanmadı.

## Devam

S10'un tüm soruları cevaplandı. Kullanıcı isterse Q13 mekanizmasını derinleştir veya seçtiği başka soruya geç. Sonraki yeni set ID'si S11; henüz hazırlanmadı. Otomasyon/bildirim kurulmadı.

[Sorular](../PCD-S10.md) · [Türkçe anahtar](../../answers/scenarios/PCD-S10.md).

## Kullanıcının deneme sonrası geri bildirimi

1 Ekim: Kullanıcı tek yanlışla bitirmeyi olumlu değerlendirdi. Paragraf uzunluklarının zorlamadığını, sette hem kolay hem zor sorular bulunduğunu söyledi. Genel yorgunluk ve sona doğru odaklanma problemi bildirdi; önceki günden bir miktar uykusuzluk da vardı. Bu, kullanıcı beyanıdır; Q13 yanlışının sebebinin yorgunluk/uykusuzluk olduğu doğrulanmadı. İlk sonuç 19/20 ve 42 dakika korunur. Uzun İngilizce paragraf tercihi değişmedi; bu geri bildirim metinleri kısaltma veya bütün soruları zorlaştırma talebi sayılmaz.

## Q13 — teknik bilgi açığı kullanıcı beyanı

Kullanıcı Q13'te teknik bilgi açığı da olduğunu ve mekanizmayı gözünde canlandıramadığını belirtti. Önceki belirsiz hata sınıfına bu doğrulanmış beyan eklenir; yalnız İngilizce veya yorgunluğa bağlanmaz. Tarayıcıda Identity Platform sign-in → Firebase ID token → backend Admin SDK doğrulaması → doğrulanmış UID → account-level authorization → backend'in kendi veritabanı erişimi akışı somut iki müşteri örneğiyle açıklanıyor. İlk C ve 19/20 korunur; açıklama sonrası kavrayış henüz teyit edilmedi.
