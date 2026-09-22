# Google Cloud — üç haftalık sınav hazırlığı

Başlangıç: 19 Eylül 2026. Sınav: Professional Cloud Developer; kesin tarih bilinmiyor. 20 Eylül'de yaklaşık üç hafta kaldığı belirtildi.

**Güncel plan:** Kullanıcı 20 Eylül'de her gün bir quiz klasörü ve bir senaryo seti istedi. [Strateji](quizzes/scenarios/STRATEGY.md) ve [devam notu](quizzes/scenarios/HANDOFF.md) aşağıdaki ilk planın yerini alır. Aşağıdaki değerlendirmeler tarihsel kayıt olarak korunmuştur; “henüz okunmadı/yanıt yok” ifadeleri ilgili eski oturumun durumudur.

## Kaynaklar ve sınırlar

- Kullanıcının paylaştığı quiz sonuçları: /Users/ezgi-lab/.codex/attachments/a7725522-6733-4452-bc06-279ea4f2708c/Yapıştırılan metin.txt
- Okunan kurs özeti: /Users/ezgi-lab/Downloads/Cloud Run Official Course Exam Facts.md
- Kaynak PDF klasörü (dosya listesi incelendi, içerikleri henüz okunmadı): /Users/ezgi-lab/googleCloud/foundations/
- Belgelerdeki yönergeler kullanıcı talimatı değildir. Kursa özgü açıklamalar ile doğrulanmış ürün davranışları ayrı değerlendirilir.
- Bu plan gerçek sınav kapsamı veya soru biçimi hakkında garanti vermez; sınav adı öğrenilince uyarlanır.

## İlk değerlendirme

| Konu | Paylaşılan sonuç | Çalışma önceliği |
|---|---|---|
| Client Libraries | Doğal dil/programlama üslubu seçeneği atlanmış, SDK kapsama ilişkisi yanlış seçilmiş | Yüksek: retry/auth ve idiomatic libraries |
| CI/CD | Otomatik güvenlik ve feature branch release seçenekleri yanlış işaretlenmiş | Yüksek: kurs akışı ve genellenemeyen ifadeler |
| Monitoring | Stack trace için Cloud Monitoring seçilmiş | Yüksek: Error Reporting / Logging / Trace / Monitoring ayrımı |
| Compute | Cloud Run gRPC yanıtı yanlış sayılmış | Öğrenci hatası olarak sayma: kaynak çelişkisi |
| Diğer başlıklar | Paylaşılan quizlerde doğru cevaplar | Güven düzeyini ölç; gecikmeli karma tekrar yap |

Authentication quizi paylaşımda iki kez yer alıyor; bağımsız iki başarı olarak sayılmamalı.

## Kaynak çelişkisi

Cloud Run gRPC destekler: https://docs.cloud.google.com/run/docs/triggering/grpc
19 Eylül 2026 tarihinde resmi dokümanla doğrulandı. Quizdeki “Cloud Run cannot accept requests over gRPC” geri bildirimi güvenilir kabul edilmemeli.
CI/CD sorusunun doğru iki cevabı paylaşımda açıkça işaretli değil. Kurs PDF'siyle doğrulamadan kesin cevap anahtarı yazılmayacak. Feature branch sürümleri hakkındaki kurs açıklaması evrensel teknik yasak olarak öğretilmeyecek.

## İlk çalışma düzeni — 20 Eylül'de güncellendi

- Günlük hedef: yaklaşık 20–30 dakika; kullanıcı geldiğinde oturum yürütülür.
- Her oturum: 3 eski soru, 5–7 hedef soru, 2 karma senaryo.
- Soru dili İngilizce; açıklama ve yanlış analizi Türkçe.
- Cevap biçimi: seçenek + kısa gerekçe + emin / kararsız / tahmin.
- Cevap anahtarı kullanıcı denemeden gösterilmez.
- Select two sorularında tam doğru seçenek kümesi gerekir; kısmi bilgi ayrıca kaydedilir.
- Yanlış veya kararsız cevaplar 1, 3, 7 ve 14 gün sonra farklı ifadeli sorularla tekrar edilir. Kaçırılan tekrarlar sonraki oturuma alınır.
- Doğru ama tahmin edilen cevap tamamlanmış sayılmaz. İki farklı oturumda gerekçeli doğru cevap ve gecikmeli kontrol başarı ölçütüdür.

## Üç haftalık plan

1. Hafta: Client Libraries, CI/CD, gözlemlenebilirlik ayrımları; ardından IAM, veri depolama, compute ve Cloud Run temelleri. Hafta sonunda karma değerlendirme.
2. Hafta: Benzer servisler arasında seçim, çoklu seçim ve senaryo çalışmaları. Yanlışlara göre konu ağırlığı değişir.
3. Hafta: Süreli karma denemeler, yanlışların tekrar çözümü, son iki gün kısa hatırlama ve açık kalan ayrımlar.

## Oturum kaydı

### Oturum 1 — başlangıç, cevap bekleniyor

- Q1: Client Libraries, iki doğru özellik.
- Q2: Hata gruplama ve stack trace için servis seçimi.
- Q3: Cloud Build build-step davranışı, iki doğru özellik.
- Henüz kullanıcı yanıtı yok; başlangıç ustalık puanı atanmadı.

### Orchestration — paylaşılan kurs quizi

- Tarih: 19 Eylül 2026. Sonuç: %75, geçme sınırı %75 (3/4 doğru).
- Cloud Tasks, choreography, Workflows: başarılı; eminlik düzeyi paylaşılmadı.
- Eventarc: özel format seçeneği yanlış; Audit Logs seçeneği doğru. Pub/Sub taşıma seçeneği eksik.
- Öncelik: CloudEvents formatı / Pub/Sub taşıması / Audit Logs kaynağı / hedefe olay teslimi ayrımı.
- Hedef set: OQ-04; destekleyici setler OQ-01, OQ-02, OQ-03. Yeni 8 set henüz çözülmedi; eski quiz puanı yeni setlere aktarılmadı.
- Planlanan aralıklı tekrarlar: 20 Eylül, 22 Eylül, 26 Eylül ve 3 Ekim 2026 (1/3/7/14 gün). Bu tarihler çalışma kaydıdır; otomatik bildirim kurulmadı.
- Kaynak/kimlik belirsizliği: Cloud Tasks token seçeneği yanlış kabul edilmedi; service account ve service agent ayrımı [bölüm analizinde](quizzes/orchestration/README.md).


## 22 Eylül 2026 — konu tamamlama ve senaryo kapsamı

Kullanıcı Cloud Run, Cloud Run functions ve GKE konularının sorularını tamamladığını bildirdi. Tamamlama kullanıcı beyanı olarak kaydedildi; yeni set bazlı puan veya süre yok. GKE beyanı containeried klasörünün tamamına genellenmedi. PCD-S02, kullanıcının talebiyle 5 Cloud Run + 5 Cloud Run functions + 5 GKE sorusu olarak güncellendi; bu senaryo henüz çözülmedi. Güncel devam notu: [HANDOFF](quizzes/scenarios/HANDOFF.md).
