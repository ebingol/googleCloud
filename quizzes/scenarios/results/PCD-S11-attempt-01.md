# PCD-S11 — İlk gönderilen 50 cevap

2 Ekim 2026. Kullanıcı seti “s10” diye adlandırarak 50 cevap ve **1 saat 49 dakika (109 dakika)** bildirdi. S10 20 soruluk ve önceki 19/20 sonucu kayıtlıdır. Bu gönderimin 50 soru olması, Q6/Q19/Q21 çift seçim yerleri ve cevap dizisinin S11 ile örtüşmesi nedeniyle **S11 olarak değerlendirildi; set kimliği kullanıcıdan ayrıca teyit edilmedi**. Ham set etiketi “s10” korunur; S10 sonucu değiştirilmedi.

Mevcut S11 anahtarına göre **43/50 (%86)**; 7 yanlış: **Q6, Q14, Q21, Q24, Q25, Q39, Q50**. Çift seçimde tam küme 1 puan; kısmi puan yok. Q19 A+B doğru; Q6 ve Q21 C+E yerine D+E olmalı.

120 dakikalık kişisel hedefin **11 dakika altında**; ortalama **2 dakika 10,8 saniye/soru**. Başlangıç/bitiş, mola, yardım/kaynak kullanımı, güven ve gerekçe bildirilmedi. Kesintisiz yardımsız deneme veya kalıcılık varsayılmaz. Yanlış nedenleri yalnız harften sınıflandırılmadı. Soru dosyasındaki cevap alanları değiştirilmedi; açıklama sonrası cevaplar ilk puana yazılmaz.

| Soru | İlk cevap | Anahtar | Sonuç |
|---|---|---|---|
| 1 | A | A | Doğru |
| 2 | D | D | Doğru |
| 3 | D | D | Doğru |
| 4 | C | C | Doğru |
| 5 | C | C | Doğru |
| 6 | C+E | D+E | Yanlış |
| 7 | A | A | Doğru |
| 8 | D | D | Doğru |
| 9 | C | C | Doğru |
| 10 | B | B | Doğru |
| 11 | B | B | Doğru |
| 12 | B | B | Doğru |
| 13 | A | A | Doğru |
| 14 | D | A | Yanlış |
| 15 | B | B | Doğru |
| 16 | A | A | Doğru |
| 17 | C | C | Doğru |
| 18 | A | A | Doğru |
| 19 | A+B | A+B | Doğru |
| 20 | C | C | Doğru |
| 21 | C+E | D+E | Yanlış |
| 22 | D | D | Doğru |
| 23 | D | D | Doğru |
| 24 | D | B | Yanlış |
| 25 | B | A | Yanlış |
| 26 | A | A | Doğru |
| 27 | C | C | Doğru |
| 28 | B | B | Doğru |
| 29 | D | D | Doğru |
| 30 | D | D | Doğru |
| 31 | B | B | Doğru |
| 32 | C | C | Doğru |
| 33 | A | A | Doğru |
| 34 | C | C | Doğru |
| 35 | D | D | Doğru |
| 36 | C | C | Doğru |
| 37 | A | A | Doğru |
| 38 | C | C | Doğru |
| 39 | D | C | Yanlış |
| 40 | A | A | Doğru |
| 41 | C | C | Doğru |
| 42 | D | D | Doğru |
| 43 | D | D | Doğru |
| 44 | A | A | Doğru |
| 45 | C | C | Doğru |
| 46 | B | B | Doğru |
| 47 | A | A | Doğru |
| 48 | A | A | Doğru |
| 49 | B | B | Doğru |
| 50 | B | C | Yanlış |

## Yanlışların kısa karşılaştırması

- **Q6: C+E → D+E.** C yayınlamayı beklemeden başlatır. D iki kontrolü beklemeyi korur; E başarısız güvenlik kontrolünün build’i başarısız yapmasını sağlar.
- **Q14: D → A.** D’de image içine yazılan /home dosyaları persistent home mount altında gizli kalır. A template dosyalarını /home dışında tutup mevcut kullanıcı dosyalarını ezmeden başlangıçta kopyalar.
- **Q21: C+E → D+E.** C’deki IAM rolü DNS paketlerine izin vermez. D veritabanı için dar 5432 iznini korur; E gerçek DNS endpointine gerekli UDP/TCP 53 erişimini ekler.
- **Q24: D → B.** D browser kontrolüne güvenir; iletilen signed URL başka kişide de çalışır. B backend’de her indirmeyi doğrular/yetkilendirir ve dosyayı stream eder.
- **Q25: B → A.** B batch dışındaki eski limit kontrolünü transaction ile doğrulamaz. A her transaction denemesinde karar verisini içeride yeniden okur.
- **Q39: D → C.** D’de Always çalışan container’ın image’ını kendiliğinden değiştirmez. C Pod template’ini onaylı digest’e güncelleyip rollout başlatır.
- **Q50: B → C.** B yeni operation ID ile aynı siparişin ikinci kez oluşmasına yol açabilir. C aynı ID ve uniqueness korumasıyla belirsiz commit sonucunu çözer veya güvenli tekrar yapar.

## Devam

Yanlış incelemesi için ilk üç aday: Q6 (beklemek/başarılı olmak), Q21 (DNS/veritabanı/IAM akışları), Q50 (belirsiz commit ve aynı işlem kimliği). Kullanıcının tercihine göre tek tek ilerle. Açıklama sonrası kavrayış ve gecikmeli kalıcılık henüz ölçülmedi. Yeni set kendiliğinden üretilmez; sonraki yeni set S12. Otomasyon/bildirim kurulmadı.

[Sorular](../PCD-S11.md) · [Türkçe anahtar](../../answers/scenarios/PCD-S11.md).

## Deneme yaklaşımı ve hata örüntüsü — 2 Ekim

Kullanıcı sonucu “fena değil” olarak değerlendirdi; daha çok en makul cevabı seçtiğini ve ilk 10 sorudan sonra mükemmeliyetçi davranmadığını belirtti. İlk 10 soru 9/10; kalan 40 soru 34/40 (%85). Bu dağılım belirgin performans çöküşü göstermez; strateji değişiminin yanlışlara neden olduğu sonucuna varılmaz. İlk sonuç 43/50 ve 109 dakika korunur.

Seçeneklerin bozduğu koşullara göre hazırlayanın hata örüntüsü yorumu: Q14/Q39 mekanizmanın ne zaman devreye girdiği (mount/image, pull/rollout); Q6/Q21/Q24 kontrolün doğru aşama veya katmanda uygulanması (release gate, network/IAM, backend/browser); Q25/Q50 eşzamanlılık ve tekrar sırasında doğruluk (transaction içi okuma, aynı operation ID). Ortak örüntü, makul görünen işlemin sorunun istediği garantiyi gerçekten sağlayıp sağlamaması. Bu yorum kullanıcının teknik bilgi/dil/dikkat hata nedeni olarak kesin sınıflandırılması değildir; bireysel gerekçeler henüz alınmadı. Kısa değerlendirme yöntemi: seçilen şık için “Sorudaki hangi şartı sağlıyor, hangi şartı açıkta bırakıyor?” kontrolü. Rehberli yorum bağımsız öğrenme ölçümü değildir.
