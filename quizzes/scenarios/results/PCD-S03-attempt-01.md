# PCD-S03 — İlk bildirilen cevapların değerlendirmesi

23 Eylül 2026. Kaynak: kullanıcının sohbette gönderdiği 15 cevap. Soru ve güncel anahtar yeniden okundu; soru dosyasındaki cevap alanları boş. Kullanıcı seçimleri aşağıda aynen korunmuştur (harfler büyük harfe, HTML karakterleri okunur biçime çevrildi).

**Sonuç: 7/15 (%46,7).** Q1–Q8 tam doğru değil; Q9–Q15 tamamı doğru. Q4’te D doğru kümenin bir parçası, ancak C eksik; iki seçimde tam küme gerektiğinden 0 puan. Süre, güven, gerekçeler ve dış kaynak kullanımı bildirilmedi; bağımsız/süreli koşullar ayrıca doğrulanmadı.

| Soru | Kullanıcı cevabı | Anahtar | Sonuç |
|---|---|---|---|
| 1 | D | B | Yanlış |
| 2 | C | D | Yanlış |
| 3 | C | A | Yanlış |
| 4 | D | C, D | Eksik seçim |
| 5 | C | B | Yanlış |
| 6 | B | C | Yanlış |
| 7 | C | A | Yanlış |
| 8 | A | D | Yanlış |
| 9 | C | C | Doğru |
| 10 | A, B | A, B | Doğru |
| 11 | B | B | Doğru |
| 12 | D | D | Doğru |
| 13 | A | A | Doğru |
| 14 | C | C | Doğru |
| 15 | B | B | Doğru |

Alanlar: Cloud Run 2/5, Functions 3/5, GKE 2/5.

## Kullanıcı geri bildirimi ve yorum sınırları

Kullanıcı çok zorlandığını ve okuduğunu soyutlayıp doğru pattern’a eşleyemediğini belirtti; cevapların aslında basit olduğunu düşündüğünü söyledi. Bu, kullanıcının öz değerlendirmesidir. Yalnız cevap harflerinden bütün yanlışları İngilizceye, dikkate veya teknik bilgi eksikliğine bağlayamayız. İlk sekiz yanlış/eksik ve son yedi doğru dağılımı tek başına yorgunluk, ısınma veya kavrayış düzeyinin nedeni olarak yorumlanmamalı.

Hazırlayanın payı: S03, S02’ye göre yalnız seçenekleri zorlaştırmadı; ConfigMap subPath, WIF ve PDB gibi ek resmî kaynak ayrıntılarıyla kapsamı da genişletti. Yeni teknik ayrıntı ile İngilizce/karar yükü birlikte değişti. Sonuç, S02’deki 14/15 ile doğrudan bilgi kaybı veya gerçek sınava hazır olmama kanıtı olarak karşılaştırılamaz.

## Yanlışlarda incelenecek ayrımlar — kesin hata tanısı değil

- Q1 D: Restart önerisi, restart gerektirmeme koşuluyla çelişiyor. Koşulu fark etme/anlama ve subPath bilgisi ayrı kontrol edilecek.
- Q2 C: Seçenekte audience doğru; candidate revision’a doğrudan gitme hedefi eksik. Audience kuralının tamamen unutulduğu sonucu çıkarılamaz.
- Q3 C: Upload’ı bekleme parçası doğru; hatayı yakalayıp başarı döndürme retry şartını bozar. Hata/başarı sinyalinin anlamı kontrol edilecek.
- Q4 yalnız D: Bucket scope seçimi doğru kümede; dedicated KSA oluşturup Pod’a bağlayan C eksik. İki seçim yönergesini atlama mı, iki adımın gerekliliği mi bilinmiyor. Q10’da iki seçenek doğru verilmiş.
- Q5 C: Generation kullanma fikri var; current metadata ile event’in generation’ı ayrımı kaçmış olabilir.
- Q6 B: Outbound VPC egress ile ingress listener/bind ayrımı kontrol edilecek.
- Q7 C: Rollout ve bakım eviction mekanizmaları ayrımı; PDB ek kaynak konusuydu.
- Q8 A: Instance limitinde headroom olduğu koşulu; ölçekleme tavanı ile ölçekleme sinyali ayrımı kontrol edilecek.

## Sonraki öğretim adımı

Uzun İngilizce senaryolar korunacak. Soruyu okurken önce hedef / değiştirilemez koşul / zaten sağlanmış durum çıkarılacak; sonra seçenekler tüm koşullara göre elenecek. İlk kısa rehberli çalışma Q1 üzerinden yalnız restart kısıtını anlamayı kontrol edecek. Birlikte çözümde tek soru sor ve yanıtı bekle; sekiz yanlışı tek uzun derse dönüştürme. Teknik ayrıntı bilinmiyorsa bunu ayrı açıkla, tüm sorunu okuma becerisine yükleme.

Henüz rehberli kullanıcı yanıtı veya açıklama sonrası kavrayış teyidi yok. İlk sonuç 7/15 korunacak. Yeni kontrol tarihi, açıklama/pekiştirme yapıldıktan sonra belirlenecek; yalnız puanlamayla öğrenildi işareti koyma.

[Sorular](../PCD-S03.md) · [Anahtar](../../answers/scenarios/PCD-S03.md)
