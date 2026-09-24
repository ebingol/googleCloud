# PCD-S03 — İlk sekiz sorunun tekrar çözümü

23 Eylül 2026. Kullanıcı yalnız ilk denemede yanlış/eksik olan Q1–Q8’i tekrar çözüp seçimlerini sohbette gönderdi. İlk değerlendirme ve kısmi açıklamalar sonrasındaki aynı-soru tekrarıdır; yeni bağımsız sınav veya gecikmeli kalıcılık ölçümü değildir. Süre, güven, gerekçe ve bu tekrar sırasında kaynak kullanımı bildirilmedi.

**Tekrar sonucu: 2/8 (%25). Q1 ve Q3 düzeldi.** Q2/Q4/Q5/Q6/Q7/Q8 hâlâ yanlış. İlk 7/15 sonucu aynen korunur; bu tekrar ile birleştirilerek yeni bağımsız 9/15 sonucu üretilmez.

| Soru | Tekrar cevabı | Anahtar | Sonuç |
|---|---|---|---|
| 1 | B | B | Doğru |
| 2 | B | D | Yanlış |
| 3 | A | A | Doğru |
| 4 | A, D | C, D | Yanlış |
| 5 | D | B | Yanlış |
| 6 | A | C | Yanlış |
| 7 | D | A | Yanlış |
| 8 | A | D | Yanlış |

## Gözlemler

- Q1 D→B, Q3 C→A: Doğru seçime geçildi; gerekçe verilmediğinden kavrayış/kalıcılık ayrıca doğrulanmalı.
- Q2 C→B: İlk seçimde normal service audience doğruydu, tag hedeflemesi eksikti; tekrarda tag hedefi doğru, audience tag URL yapılmış. İki URL’nin görevlerini birlikte ayırma ihtiyacı var; gerekçe henüz bilinmiyor.
- Q4 D→A+D: Artık iki seçenek var; sorunu yalnız seçim sayısı yönergesine bağlama. Node kimliği ile dedicated workload kimliği ayrımı kontrol edilmeli.
- Q5 C→D: Event’in generation’ı yerine concurrency seçildi; sırayla işleme ile doğru object sürümünü okuma ayrı açıklanmalı.
- Q6 B→A: Loopback bind ve ingress container ayrımı hâlâ kontrol edilmeli.
- Q7 C→D: Rollout yerine HPA seçildi; voluntary eviction/PDB ayrımı henüz doğrulanmadı.
- Q8 A→A: Instance tavanı ile ölçekleme sinyali ayrımı kontrol edilmeli.

Bu seçimlerden sorunun yalnız İngilizce veya yalnız teknik bilgi olduğu kesinleştirilmez. Kullanıcının önceki “yapamayacağım” ifadesi bağlamında sonuç açık ve yargısız aktarılacak; yanlışları sekiz uzun açıklamayla yığma.

## Öğretim adımı

Önce Q2 için kısa çözümlü örnek: “Nereye?” candidate tag URL; “token hangi servis için?” alıcı servisin normal URL’si; sonuç D. Bu açıklama kullanıcı kavrayış teyidi değildir. Sonra Q4 kimlik kapsamı ve Q5 generation gerektiğinde ayrı çalışılabilir. Yeni quiz talep edilmedi. İlk cevaplar ve puan değiştirilmedi.

[İlk deneme](PCD-S03-attempt-01.md) · [Sorular](../PCD-S03.md) · [Anahtar](../../answers/scenarios/PCD-S03.md)

## Açıklama talebi

Kullanıcı Q2’de teknik kuralı bilmek gerektiğini belirtti ve tüm cevapların açıklanmasını istedi. İlk sekiz soruda teknik önbilgiyi açık ederek, son yedi doğru soruda kısa gerekçelerle toplu açıklama sağlanacak. Bu talep önceki tek soru ilerleme önerisini geçersiz kılar. Puan değişmez; açıklama sonrası kullanıcı yanıtı/kavrayış teyidi yok.

## Kullanıcı tarafından netleştirilen eksik

Q7: PDB/eviction kavramlarını bilmediğini açıkça belirtti; teknik kavram eksikliği doğrulandı. Eğitimde bulunmadığı kullanıcı beyanıdır; soru ek resmî kaynak kapsamındaydı. Q8 single-threaded/concurrency açıklaması sonrası “anladım” beyanı var; bağımsız/gerekçeli seçim veya gecikmeli kontrol yok. İngilizce nedeniyle bildiğini tanıyamama da kullanıcı tarafından bildirildi; bütün yanlışlara tek neden atanmaz. İlk ve tekrar puanları korunur.
