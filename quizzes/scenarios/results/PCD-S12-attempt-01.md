# PCD-S12 — İlk gönderilen 50 cevap

8 Ekim ek çalışma: Kullanıcının isteğiyle Q7/Q8/Q24/Q29/Q30/Q38 özgün İngilizce gövde ve tüm seçenekleri, ilk seçimi ve doğru cevapla birlikte sunuldu. Bu anahtarlı incelemedir; yeni bağımsız puan/kavrayış teyidi yok. Kullanıcı bu sonuçla geçebileceğini düşündüğünü söyledi; gerçek sınav geçişi doğrulanmış sonuç olarak kaydedilmez.

**8 Ekim tamamlanma kaydı:** Q11–Q50 **36/40 (%90), 60 dakika**. İlk bölümle toplam **44/50 (%88), 72 dakika** (12+60); iki güne bölünmüş çözüm, tek kesintisiz deneme değildir. Arada Q7/Q8 öğretimi yapıldı; ilk seçimler değiştirilmedi. Toplam yanlışlar **Q7, Q8, Q24, Q29, Q30, Q38**. 120 dakikalık kişisel hedefe göre bildirilen toplam çözüm süresi 48 dakika daha kısa. Mola/yardım/kaynak kullanımı ve güven/gerekçe bildirilmedi. Aşağıdaki kısmi durum ifadeleri tarihsel kayıttır.

7 Ekim 2026. Kullanıcı S12 Q1–Q10 cevaplarını ve **12 dakika** süre bildirdi.

Ham cevaplar: `1-d,2-c,3-d,4-c,5-d,6-c,7-d,8-d,9-c,10-c`.

Mevcut S12 anahtarına göre **8/10 (%80)**. Yanlışlar Q7 ve Q8. Ortalama 1 dakika 12 saniye/soru. Q11–Q50 henüz gönderilmedi; tam deneme sonucu yok. Mola, yardım/kaynak kullanımı, güven ve gerekçe bildirilmedi; hata nedeni yalnız şıktan sınıflandırılmadı.

| Soru | İlk cevap | Anahtar | Sonuç |
|---|---|---|---|
| 1 | D | D | Doğru |
| 2 | C | C | Doğru |
| 3 | D | D | Doğru |
| 4 | C | C | Doğru |
| 5 | D | D | Doğru |
| 6 | C | C | Doğru |
| 7 | D | B | Yanlış |
| 8 | D | A | Yanlış |
| 9 | C | C | Doğru |
| 10 | C | C | Doğru |

## Değerlendirme sonrası kısa açıklama

- Q7 D→B: Pod metadata label'ı node seçme şartı değildir. `nodeSelector` içindeki `kubernetes.io/arch: arm64` yerleşim koşulunu belirtir; desteklenen Autopilot ortamı uygun kapasiteyi oluşturur.
- Q8 D→A: Oda metadata'sı bir document, her mesaj `messages` subcollection içinde ayrı document olur. Tek proje document'ında tüm oda/mesajları toplamak büyüyen document ve ortak yazım noktasını korur; bağımsız mesaj yazımı/sayfalama hedefini karşılamaz.

Bu açıklamalar sonrası kavrayış veya bağımsız kalıcılık teyidi yok; ilk cevaplar korunur. Sonraki adım Q11–Q20 cevapları ve bölüm süresi.

## 7 Ekim — mekanizma öğretimi

Kullanıcı iki sorunun mantığını, ardından subcollection ve her iki çözümün pattern'ını sordu. Firestore collection/document/subcollection hiyerarşisi, mesajların oda document alanına gömülmeyen ayrı kayıtlar olması, bağımsız yazım ve sayfalama; GKE node label ile Pod metadata label ayrımı ve Pod spec.nodeSelector üzerinden gereksinim belirtme somut yapı örnekleriyle açıklandı. Bu rehberli öğretimdir; kavrayış teyidi veya yeni bağımsız sonuç yok. İlk 8/10 ve 12 dakika korunur. Kaynaklar: https://firebase.google.com/docs/firestore/data-model ve https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/ .

## 8 Ekim — Q11–Q50 ilk cevaplar

Ham cevaplar: `11-c,12-a,13-a,14-d,15-d,16-a,17-b,18-b,19-c,20-b,21-a,22-b,23-c,24-cd,25-d,26-c,27-ae,28-a,29-a,30-d,31-a,32-c,33-b,34-bd,35-b,36-b,37-d,38-c,39-d,40-c,41-b,42-b,43-b,44-a,45-a,46-a,47-c,48-a,49-d,50-b`. Süre: **60 dakika**. Çift seçimde tam küme 1 puan, kısmi puan yok.

| Soru | İlk cevap | Anahtar | Sonuç |
|---|---|---|---|
| 11 | C | C | Doğru |
| 12 | A | A | Doğru |
| 13 | A | A | Doğru |
| 14 | D | D | Doğru |
| 15 | D | D | Doğru |
| 16 | A | A | Doğru |
| 17 | B | B | Doğru |
| 18 | B | B | Doğru |
| 19 | C | C | Doğru |
| 20 | B | B | Doğru |
| 21 | A | A | Doğru |
| 22 | B | B | Doğru |
| 23 | C | C | Doğru |
| 24 | C+D | A+C | Yanlış |
| 25 | D | D | Doğru |
| 26 | C | C | Doğru |
| 27 | A+E | A+E | Doğru |
| 28 | A | A | Doğru |
| 29 | A | D | Yanlış |
| 30 | D | A | Yanlış |
| 31 | A | A | Doğru |
| 32 | C | C | Doğru |
| 33 | B | B | Doğru |
| 34 | B+D | B+D | Doğru |
| 35 | B | B | Doğru |
| 36 | B | B | Doğru |
| 37 | D | D | Doğru |
| 38 | C | D | Yanlış |
| 39 | D | D | Doğru |
| 40 | C | C | Doğru |
| 41 | B | B | Doğru |
| 42 | B | B | Doğru |
| 43 | B | B | Doğru |
| 44 | A | A | Doğru |
| 45 | A | A | Doğru |
| 46 | A | A | Doğru |
| 47 | C | C | Doğru |
| 48 | A | A | Doğru |
| 49 | D | D | Doğru |
| 50 | B | B | Doğru |

### Yeni yanlışların kısa karşılaştırması

- Q24 C+D→A+C: Runtime hesabını function'a bağlamak ve hedef bucket'ta bu hesaba Object Creator vermek gerekir; service agent'a Editor vermek runtime kimliğinin yerine geçmez.
- Q29 A→D: Archive minimum storage duration ücretlendirme koşuludur; erken silmeyi engellemez. Kilitli retention policy yedi yıllık silme engelini, lifecycle Archive geçişi maliyet hedefini karşılar.
- Q30 D→A: Feature flag yalnız yeni özelliği küçük gruba açıp kapatır; routine fix'ler tüm kullanıcılarda kalır. Tüm kullanıcıları yeni sürüme geçiren blue/green switch bu ayrımı sağlamaz.
- Q38 C→D: Cloud Profiler CPU/heap profilleri pahalı fonksiyonları ve allocation yollarını incelemek içindir; uzak HTTP çağrıları etrafındaki Trace span'leri bu kanıtı sağlamaz.

Hata nedenleri kullanıcı gerekçesi olmadan teknik/dil/dikkat diye sınıflandırılmadı. Açıklamalar sonrası kavrayış teyidi yok. Sonraki adım kullanıcı isterse Q24/Q29/Q30 mekanizmalarını somutlaştırmak, ardından Q38; yeni set kendiliğinden üretilmez.


8 Ekim — Q30 takip: Kullanıcı feature flag hedef kitleyi değiştirmez diye itiraz etti ve blue/green hatırlatması istedi. Basit global boolean ile kullanıcı/grup koşullu flag değerlendirmesi ayrıldı; aynı yeni sürümde düzeltmeler herkese, yeni özellik pilot gruba, kapatılınca yalnız özellik devre dışı örneği açıklandı. Blue/green iki paralel sürüm/ortam ve trafik geçişi olarak hatırlatıldı; Q30 D tüm kullanıcıları taşır, A hedefleme kuralı uygulanmasını gerektirir. Kavrayış teyidi yok, ilk puan değişmez.


8 Ekim — S12 aday aktarımı/Airflow: Kullanıcı geçen arkadaşının aktardığı Eventarc–Storage ve Airflow yalnız şıklarda noktalarının bu sette bulunduğunu belirtti. S12 Q16 A object-finalized→Eventarc→Workflows; Q37 D bucket creation→Audit Logs Eventarc; Q33 C Airflow çeldiricisi, doğru B Workflows olarak eşlendi (üçü de ilk doğru). Benzer konu görülmesi aynı gerçek sınav sorusu/zorluk kanıtı değildir. Airflow Python DAG ile bağımlı görevleri zamanlama/izleme/retry ve veri pipeline örneğiyle hatırlatıldı; kısa HTTP zincirinde Workflows tercihinin nedeni açıklandı. Kavrayış teyidi yok; 44/50 korunur. Önceki canary/blue-green karşılaştırması da rehberli öğretimdir, yeni ölçüm yok.


8 Ekim — S12 tam anahtarlı tekrar: Kullanıcı kafasında sabitlemek için 50 sorunun tamamını cevaplarıyla yeniden istedi. answers/scenarios/PCD-S12-REVIEW.md oluşturuldu: özgün mevcut İngilizce gövdeler/tüm seçenekler, her sorunun altında doğru cevap ve mevcut Türkçe gerekçe/eleme koşulu/kaynak. 50 soru/50 cevap eşleşmesi kontrol edildi; ilk 44/50, 72 dakika korunur. Anahtarlı çalışma öğrenme/kalıcılık teyidi değildir.
