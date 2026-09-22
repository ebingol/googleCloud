# PCD-S01 — İlk deneme sonucu

Tarih: 20 Eylül 2026. Kaynak: soru başlıklarına kaydedilen kullanıcı cevapları.

**Sonuç: 11/15 (%73,3).** Çoklu seçimde tam doğru küme esas alındı. Çözüm süresi: **20 dakika** (kullanıcı beyanı); soru başına ortalama 80 saniye. Güven düzeyi ve soru bazında gerekçe belirtilmedi; bunlar değerlendirilmedi.

| Soru | Cevabın | Anahtar | Sonuç |
|---|---|---|---|
| 1 | D | C | Yanlış |
| 2 | A | A | Doğru |
| 3 | B | D | Yanlış |
| 4 | B | B | Doğru |
| 5 | C | C | Doğru |
| 6 | C | A, D | Yanlış |
| 7 | D | B | Yanlış |
| 8 | D | D | Doğru |
| 9 | A | A | Doğru |
| 10 | C | C | Doğru |
| 11 | B, C | B, C | Doğru |
| 12 | A | A | Doğru |
| 13 | D | D | Doğru |
| 14 | B | B | Doğru |
| 15 | C | C | Doğru |

## Tekrar öncelikleri

1. Soru 1: Secret Manager Viewer metadata görmeyi sağlar; secret değerini okumak için Secret Accessor gerekir.
2. Soru 3: Sıralı çalışmak dosya paylaşmaz. Aynı build adımları arasında /workspace veya ortak volume kullanılır.
3. Soru 6: A, B’yi çağırırken B üzerinde A kimliğine invoker verilir; B audience değerli ID token gönderilir. İki seçenek istenmiş, yalnız C seçilmiş.
4. Soru 7: Session affinity isteğin nereye gideceğini etkiler; paralel işlemeyi engellemez. Verilen senaryoda instance concurrency 1 gerekir.

## Alan sonuçları

| Alan | Doğru |
|---|---|
| IAM / ADC | 1/3 |
| Cloud Run | 2/3 |
| Build / CI/CD | 2/3 |
| Veri | 3/3 |
| Event / koordinasyon | 3/3 |

Sonuç yalnız bu pilotu gösterir; gerçek sınav geçme tahmini değildir. Kullanıcının soru dosyasındaki cevapları korunmuştur.

[Ayrıntılı açıklamalar](../../answers/scenarios/PCD-S01.md)

## Kullanıcı geri bildirimi

Sorular faydalı bulundu. Karmaşık İngilizce senaryoları okuyup anlamakta zorlanıldığı ve Google soru diline alışma ihtiyacı belirtildi. Sonraki çalışmada gereksinimleri ve kısıtları metinden çıkarma pratiğine odaklanılacak. Bu sorular özgündür; resmî Google soruları değildir.
