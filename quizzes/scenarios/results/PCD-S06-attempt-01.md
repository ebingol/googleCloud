# PCD-S06 — İlk bildirilen cevapların değerlendirmesi

25 Eylül 2026. Kaynak: kullanıcının sohbette gönderdiği 20 cevap ve 73 dakika süre beyanı. Harfler büyük harfe, çoklu seçimler ayrı harflere çevrildi; ilk seçimler korunmuştur.

**Sonuç: 13/20 (%65). Süre: 73 dakika.** Soru başına ortalama 3 dakika 39 saniye. Q1/Q3/Q5/Q14/Q17/Q18/Q20 yanlış; kalan 13 soru doğru. Q6 B+D tam doğru. Q18'de B doğru, D yanlış, E eksik; tam küme kuralıyla 0 puan.

Güven, gerekçe, yardım ve mola koşulları bildirilmedi. Bağımsız koşullar ayrıca doğrulanmadı. Hata nedenleri yalnız cevap harflerinden teknik/dil/dikkat diye kesin sınıflandırılmadı.

| Soru | Kullanıcı cevabı | Anahtar | Sonuç |
|---|---|---|---|
| 1 | C | B | Yanlış |
| 2 | D | D | Doğru |
| 3 | B | A | Yanlış |
| 4 | C | C | Doğru |
| 5 | B | D | Yanlış |
| 6 | B, D | B, D | Doğru |
| 7 | B | B | Doğru |
| 8 | A | A | Doğru |
| 9 | C | C | Doğru |
| 10 | B | B | Doğru |
| 11 | D | D | Doğru |
| 12 | A | A | Doğru |
| 13 | C | C | Doğru |
| 14 | A | B | Yanlış |
| 15 | D | D | Doğru |
| 16 | A | A | Doğru |
| 17 | D | C | Yanlış |
| 18 | B, D | B, E | Yanlış |
| 19 | B | B | Doğru |
| 20 | B | D | Yanlış |

## Birincil alan örneklemi

- Tasarım/güvenlik/veri: 2/6 (Q9/Q13 doğru).
- Geliştirme/test: 3/5 (Q2/Q6/Q10 doğru).
- Deployment: 4/5 (Q7/Q11/Q15/Q19 doğru).
- Entegrasyon/gözlemlenebilirlik: 4/4 (Q4/Q8/Q12/Q16 doğru).

Bu küçük örneklem tüm alan yeterliği değildir. S05 17/20, 70–80 dakika ile karşılaştırıldığında süre aynı aralıkta, doğruluk 4 soru düşük. S06 hem konu hem metin/seçenek yükünde farklıdır; tek başına gerileme veya gerçek sınav geçme/kalma tahmini çıkarılmaz.

## Yanlış seçimlerde incelenecek ayrımlar

- Q1 C→B: Workflows execution başına concurrency sınırı, bağımsız execution'ların toplamını sınırlamaz. İstenen queue-wide scheduling/rate/concurrency; Cloud Tasks.
- Q3 B→A: Audit principal Cloud Run service agent; uygulama runtime SA'sı değil. Cross-project repository Reader grant'i doğru principal'a verilmeli.
- Q5 B→D: Normal SA OAuth token'ını tek dosya yolu ile göndermek token'ı o dosyaya kısıtlamaz. Tek object/method/expiry için signed GET URL.
- Q14 A→B: Commit label ve push log, Cloud Build-generated provenance değildir. images output + requestedVerifyOption VERIFIED.
- Q17 D→C: Retention minimum koruma süresi, expiry otomatik silme komutu değil. Lifecycle Delete korunur ve retention sonrası asenkron çalışabilir.
- Q18 B+D→B+E: Yeni fixed base ile rebuild doğru seçildi. Eski digest'i yeniden onaylamak production'ı düzeltmez; yeni artifact doğrulanıp rollout edilmeli.
- Q20 B→D: Diagnostic alanları daha fazla indexed alana bölmek gereksiz fanout'u kaldırmaz. Sorgulanmayan alanlara index exemption, gerekli query indexes'e devam.

Öncelik ilk üç ayrımda kullanıcının seçim gerekçesini ve bilmediği ifadeleri anlamak; kalan dört yanlış da kayıtta. Toplu kısa geri bildirim sonrası yeni kullanıcı yanıtı/öğrenme teyidi henüz yok. Açıklama sonrası seçimler ilk 13/20 üzerine yazılmaz. S04 için sonuç bildirilmedi.

[Sorular](../PCD-S06.md) · [Kaynaklı anahtar](../../answers/scenarios/PCD-S06.md)


### S06 sonrası kullanıcı geri bildirimi — anahtar kelimeyle seçim

Kullanıcı çok düşünemediğini, daha çok keyword yakalayıp sorudaki best practice'i bulmaya çalıştığını; soruları ayrıntılı anlamanın çok zor olduğunu belirtti. Zorluk artınca hata oranının arttığını gözlemledi. Bu kullanıcı öz değerlendirmesidir; bütün yanlışları kesin olarak dil/okuma kaynaklı sayma, teknik kavram eksikleri ayrıca kontrol edilmeli. Başka bir adayın da %65 yaptığını ve sınavda kaldığını aktardı; adayın puanının kaynağı/denemesi ve koşulları bilinmiyor, S06 ile eşdeğerlik veya geçme-kalma tahmini çıkarılmaz.

Öncelik yeni zor set üretmek değil mevcut sorularda hedef, belirleyici kısıt ve seçeneklerin bozduğu şartı yavaşça ayırma çalışması. Uzun İngilizce metin tercihi korunur. İlk 13/20 ve 73 dakika değişmez; rehberli çalışmada süre baskısı uygulanmaz. Q1 üzerinden execution başına concurrency ile queue genelindeki sınır ayrımını kendi cümlesiyle açıklaması sonraki kontrol olabilir. Henüz bu yeni kontrolün yanıtı yok.


### 26 Eylül — S06 Q3 rehberli incelemeye geçiş

Kullanıcı Q1 kontrol sorusunu yanıtlamadan bir sonraki yanlış soruya geçmek istedi. Q1 açıklaması verildi fakat anlama kontrolü doğrulanmadı; tamamlandı/öğrenildi sayılmıyor. Q3 B→A: Cloud Run service agent ile runtime service account ayrımı, denied principal'dan yetki verilecek kimliği bulma anlatılıyor. Sıra bundan sonra Q5→Q14→Q17→Q18→Q20. İlk 13/20 ve 73 dakika korunur.


### 26 Eylül — Q3 kimlik ayrımı henüz anlaşılmadı

Kullanıcı service agent/runtime SA açıklamasına “anlamadım” dedi. Secret Manager kontrol sorusunu yanıtlamadı; doğru uygulama kaydı yok. İki kimlik, platformun image'ı alması ve çalışan uygulamanın API çağrısı olarak sade bir açılış sırasıyla tekrar açıklanıyor. Daha çok kimlik/rol ekleme; önce bu ikisini somutlaştır. İlk S06 13/20 değişmez.


### 26 Eylül — S06 Q5 incelemesine geçiş

Kullanıcı Q3 sadeleştirilmiş açıklamasından sonra sonraki yanlış soruya geçmek istedi. Q3 için açıklama sonrası anlama/bağımsız yanıt teyidi yok; öğrenildi sayılmıyor. Q5 B→D inceleniyor: browser'a normal service-account access token göndermek token'ı verilen object path'e daraltmaz; belirli object+GET+expiry için signed URL. Linkin paylaşılabilir bearer niteliği ve süre sınırı açıklanıyor. Sonraki sıra Q14→Q17→Q18→Q20. İlk S06 13/20 ve 73 dakika korunur.


### 26 Eylül — S06 Q14 incelemesine geçiş

Kullanıcı Q5 açıklaması sonrası sonraki yanlış soruya geçmek istedi; Q5 kavrayış/bağımsız kontrol teyidi yok. Q14 A→B inceleniyor: image commit label/push log ile Cloud Build-generated provenance ayrımı; images output ve options.requestedVerifyOption: VERIFIED. Provenance'ın build kökeni kaydı olduğu, tests/vulnerability-free garantisi olmadığı açıklanıyor. Sırada Q17→Q18→Q20 var. İlk S06 13/20, 73 dakika korunur.


### 26 Eylül — S06 Q17 incelemesine geçiş

Kullanıcı Q14 açıklaması sonrası sonraki soruya geçmek istedi; Q14 kavrayış kontrolü yok. Q17 D→C anlatılıyor: retention 90 gün minimum silme koruması, lifecycle Delete age30 silme mekanizması. Gün45'te retention engeller; 90 gün dolunca koşulları sağlayan lifecycle Delete asenkron gerçekleşebilir, tam gün/saniye garantisi yok. Retention expiry kendiliğinden silmez. Sırada Q18→Q20 kaldı. İlk 13/20 ve 73 dakika korunur.


### 26 Eylül — S06 Q18 incelemesine geçiş

Kullanıcı Q17 açıklamasından sonra sonraki soruya geçmek istedi; Q17 kavrayış teyidi yok. Q18 B+D→B+E inceleniyor: fixed base ile yeni application image üretmek B doğru; eski digest'i yeniden onaylamak içeriği düzeltmez. E yeni image için scan/test doğrulaması ve production rollout gerektirir. Scanner metadata güncellemesi paket yaması değildir; package-lock.json sorudaki OS paketini yönetmiyor. Sonraki yanlış Q20. İlk S06 13/20 ve 73 dakika korunur; Q18 açıklama sonrası kavrayış henüz doğrulanmadı.


### 26 Eylül — Q18 açıklaması sonrası yeni set talebi

Q18 açıklaması verildi, kullanıcı kavrayış kontrolü yanıtı vermedi. “Stale” sözcüğü güncelliğini yitirmiş/eski kalmış olarak açıklandı; expired ile aynı olmadığı ayrıştırıldı. Ardından kullanıcı S07 hazırlamamı istedi; yeni set hazırlandı. S06 Q20 henüz incelenmedi. İlk 13/20 ve 73 dakika değişmedi.
