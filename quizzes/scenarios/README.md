# PCD senaryo çalışmaları

[Yeni sohbet için devam notu](HANDOFF.md) · [Günlük çalışma ve soru üretme stratejisi](STRATEGY.md) · [Soru geçmişi — hazırlayan için](QUESTION-LOG.md)

**4 senaryo seti + 1 pekiştirme seti · 70 soru.** Bu seri, ana dizindeki 152 adet beş soruluk ders tekrar setinden ayrıdır. Ders bankasının JSON dosyasına veya mevcut çözüm puanlarına dahil edilmemiştir.

Sorular İngilizce; açıklamalar Türkçe ve ayrı dosyadadır. Sorular özgündür, gerçek sınav sorusu değildir. Amaç birkaç gereksinimi birlikte değerlendirmek ve makul alternatifleri elemektir. Pilotun zorluğu henüz öğrenci sonuçlarıyla kalibre edilmemiştir.

| Set | İçerik | Süre hedefi | Sorular | Cevaplar |
|---|---|---|---|---|
| PCD-S01 | IAM, Cloud Run, CI/CD, veri ve event; her alandan 3 soru | 30 dakika | [Çöz](PCD-S01.md) | [Çözüm sonrası aç](../answers/scenarios/PCD-S01.md) |
| PCD-R01 | İlk setteki dört tekrar konusu; İngilizce yorumlama, 5 soru | Süresiz | [Çöz](PCD-R01.md) | [Çözüm sonrası aç](../answers/scenarios/PCD-R01.md) |
| PCD-S02 | Cloud Run / Cloud Run functions / GKE, 5’er soru; kullanıcı beyanıyla 14/15 | 30 dakika | [Çöz](PCD-S02.md) | [Çözüm sonrası aç](../answers/scenarios/PCD-S02.md) |
| PCD-S03 | Cloud Run / Functions / GKE, 5’er soru; ilk bildirilen cevaplar 7/15 | 30 dakika | [Çöz](PCD-S03.md) | [Çözüm sonrası aç](../answers/scenarios/PCD-S03.md) |
| PCD-S04 | Dört resmî ana alandan 20 karma soru; 6 tasarım + 5 geliştirme/test + 5 deployment + 4 entegrasyon; çözüm bekleniyor | 45 dakika | [Çöz](PCD-S04.md) | [Çözüm sonrası aç](../answers/scenarios/PCD-S04.md) |

**İlk set sonrası:** [Doküman sayfaları, ilgili quizler ve bugünkü çalışma sırası](PCD-S01-review-guide.md).

## Çalışma akışı

1. İlk turda cevap anahtarını ve kaynakları açmadan çöz.
2. Her cevapta E/K/T güven düzeyi ve kararı belirleyen koşulu bir cümleyle yaz; kararsız olduğunda yakın alternatifi de belirt.
3. İstersen cevapları sohbette beşli gruplar halinde gönder; S04 için son grup 16–20.
4. Anahtarla kontrol ettikten sonra yanlışları ve tahminle doğruları tekrar listesine al.
5. İlerlemeni aşağıya kaydet; tekrar çözümündeki ezber etkisini ilk denemeden ayır.

| Set | Deneme | Tarih | Doğru / toplam | Süre | Tekrar konuları |
|---|---|---|---|---|---|
| PCD-S01 | İlk | 20 Eylül 2026 | 11 / 15 (%73,3) | 20 dakika | Secret rolleri; build adımları arasında dosya paylaşımı; servis çağrı yetkisi ve ID token; concurrency / session affinity |
| PCD-R01 | İlk | 20 Eylül 2026 | 4 / 5 (%80) | Bildirilmedi | ID token audience; custom audiences ifadesi; teknik gerekçeyi açık yazma. [Değerlendirme](results/PCD-R01-attempt-01.md) |
| PCD-S02 | İlk bildirilen; kullanıcı beyanı | 22 Eylül 2026 | 14 / 15 (%93,3) | 20 dakika | Q12 readiness/liveness; cevap alanları boş, seçilen şık bilinmiyor. [Sonuç](results/PCD-S02-attempt-01.md) |
| PCD-S03 | İlk bildirilen cevaplar | 23 Eylül 2026 | 7 / 15 (%46,7) | Bildirilmedi | Q1–Q8 yanlış/eksik; Q9–Q15 doğru. [Sonuç](results/PCD-S03-attempt-01.md) |
| PCD-S03 | Q1–Q8 tekrar; önceki geri bildirim sonrası | 23 Eylül 2026 | 2 / 8 | Bildirilmedi | Q1/Q3 düzeldi; ilk 7/15 korunur. [Tekrar](results/PCD-S03-retry-01.md) |

## Kapsam

[Resmî sınav rehberi](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) 20 Eylül 2026'da kontrol edildi. Pilot kişisel çalışma önceliklerine göre dağıtılmıştır; sınavın konu ağırlıklarını taklit etmez. Soru bazındaki rehber eşleştirmesi cevap dosyasındadır. GKE, Apigee, AI ve observability gibi eksik alanlar sonraki setlerde tamamlanmalıdır.

[Ana quiz dizini](../README.md) · [Repo ana sayfası](../../README.md)

24 Eylül: S04 dört ana alanı resmî ağırlıklara yakın örnekler; bütün alt konuları ölçtüğü iddia edilmez. Soru bazında kaynaklar ve ölçülmeyen alt kapsam cevap dosyasındadır. Önceki set puanları değişmedi.
