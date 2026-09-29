# PCD — kullanıcının Google sonuçlarının taranması

Tarih: 29 Eylül 2026. Kullanıcının Chrome'daki sorgusu: `Professional Cloud Developer" "exam experience"`.

## Kapsam ve yöntem

Chrome'daki mevcut sonuç listesinin **1–22. sayfaları** sırayla tarandı; 22. sayfada Next bağlantısı olmadığı doğrulandı. Bu, o oturumda Google'ın sunduğu listenin sonudur; internetteki bütün PCD kaynakları değildir. Sonuçlar kişiselleştirilmişti ve sıralama değişebilir.

“Tarandı” başlık, özet, bağlantı ve sınav/ürün ilgisinin kontrolüdür. Aşağıdaki aday yazılarının erişilebilir metinleri ayrıca okundu. Alakasız sertifika, reklam, kurs katalogları ve soru bankalarının her sayfası baştan sona okunmadı; saatler süren soru çözüm videoları izlenmedi. Okunan yazı, kısmi erişim, video dökümü ve yalnız sonuç düzeyinde eleme ayrımları korunur. Önceki araştırma: [29 Eylül notu](PCD-RESEARCH-2026-09-29.md).

## Soruları hatırlayıp yazan var mı?

**Evet.** Adayların hatırladığı soru türleri/karar başlıkları mevcut. Bunlar tam soru gövdesi ve seçeneklerin doğrulanmış kopyası değildir.

| Kaynak | Hatırladığı soru türleri / somut gözlem | Sınırı |
|---|---|---|
| [Josh Laird, 9 Mart 2019](https://medium.com/@joshlaird/google-cloud-certified-professional-cloud-developer-exam-tips-6cbc5ddb9fb8) | Senaryoya uygun depolama seçimi; SQL hata ayıklama; Kubernetes yapılandırması ve komutları; service account ile projeler arası erişim; gsutil/gcloud; Deployment Manager syntax sorunları. Resmî örneklerden üç soruyla karşılaştığını iddia ediyor. | Tam metin Chrome'da okundu. Çok eski sürüm; bugünkü ürün kapsamı/soru sıklığı olarak kullanılamaz. |
| [Jonathan Reynolds, 26 Ekim 2022](https://medium.com/google-cloud/2022-google-cloud-professional-cloud-developer-certification-review-c6a1e27767dc) | 7 Ekim 2022 sınavı: deployment stratejileri, feature flags, API geriye uyumluluk, emülatörlerle yerel test, Cloud Operations ile troubleshooting, compute/storage kullanım senaryoları. | Tam metin okundu. Konu ve karar listesi; kelimesi kelimesine sorular değil. |
| [Joe Holbrook, 13 Aralık 2018 video](https://www.youtube.com/watch?v=FtOdgkNv-AU) | Aynı günkü beta sınavını anlatıyor. BigQuery performans/erişim rolleri; on-prem veriyi Cloud SQL/Spanner'a taşıma; maliyet-performans kısıtı; servis entegrasyonu; build süresini azaltma; script hatası teşhisi. | İngilizce otomatik dökümün tamamı okundu. 102 soruluk eski beta! Güncel sınav dağılımı veya syntax gereksinimi diye alınmaz. |
| [The Cloud Pilot, 22 Ocak 2024 video](https://www.youtube.com/watch?v=EDMpQ9hkiew&t=149s) | 2:29–2:45: 50 soru beklerken 60 ile karşılaşma; birbirine benzeyen seçenekleri dikkatle değerlendirme. 2:06–2:26: CI/CD, GKE, Cloud Build ve servis entegrasyonu, Cloud Run–Cloud SQL bağlantısı örneği. | İngilizce otomatik dökümün tamamı okundu; tam soru kopyası yok. Video tarihi sınav tarihi değildir. |
| [Reddit quigath, 15 Ağustos 2023](https://www.reddit.com/r/googlecloud/comments/15s1b94/i_took_the_google_cloud_professional_developer/) | Test/emülasyon soruları; iki ayrı bilgiyi birleştirme; ilk tur 105 dk, yaklaşık 12 işaretli soru, incelemede süre bitmesi. | Önceki turda tam metin incelendi. Geçtiğini bildiren tek adayın deneyimi. |

[ExamTopics soru 189 tartışması](https://www.examtopics.com/discussions/google/view/92053-exam-professional-cloud-developer-topic-1-question-189/) de sonuçlarda var. Metin erişimi web aracında başarısız; Google özetinde eski case-study yönergesi görünüyor. Gerçek/güncel sınav sorusu olarak doğrulanmadı. Bankaların “real exam” iddiaları ve aday anlatımları birbirine eşitlenmedi.

## Soru yorumlama ve süre için en yararlı bulgular

### Pavel Gulin — 2 Ocak 2024

[LinkedIn yazısı](https://www.linkedin.com/pulse/google-cloud-certified-professional-developer-exam-pavel-gulin-tt98e) Chrome'da tam metin okundu. 60 soru/iki saat bildiriyor. Soruları çok karmaşık bulmadığını, fakat soru ve cevapları okuyup bağlamı anlamanın zaman aldığını söylüyor. Bu, teknik karmaşıklık ile okuma/yorumlama süresinin ayrı olabileceğine doğrudan aday kanıtı. Kendi bitirme süresini vermiyor.

Resmî örneklerde doğru yaptığı soruları da gözden geçirmiş; tahminle tutturduklarının gerekçesini araştırmış. Kişisel eksiklerine göre yaklaşık 60 soru ve 10 geniş konu çıkarıp dokümantasyondan çalışmış. Bu sayılar gerçek sınavdan hatırlanan soruların sayısı değil, hazırlık notlarının sayısıdır.

### Jonathan Reynolds — 2022

60 soruluk sınavı **22 saniye kala** teslim etmiş. Genellikle en az iki seçeneği eleyebildiğini; yaklaşık 90 saniyede çözemediği soruyu işaretleyip dönme yaklaşımını anlatıyor. Bu kişisel strateji, her soruya uygulanacak Google kuralı değil. Seçeneklerin avantaj/dezavantaj ve uygun kullanım alanını anlamayı vurguluyor.

4 Ekim 2022'de yenilenen formda Cloud Run/GKE/serverless ağırlığının arttığını ve vaka çalışması olmadığını bildiriyor. Eski başlangıç ekranında case study ifadesinin kalmış olduğunu ayrıca söylüyor. Güncel ürün kapsamının kanıtı için bugünkü resmî rehber esas alınmalı.

### Diğer aday yazıları

| Aday / yayın | İnceleme ve katkı |
|---|---|
| [Amanda Ruzza, 2 Ocak 2024](https://dev.to/amandaruzza/my-approach-to-passing-the-professional-cloud-developer-exam-first-try-4pel) | Önceki turda tam metin okundu. Sınav 28 Aralık 2023. Deploy/modernize/troubleshoot yaklaşımları; gerekçeyi sesli anlatma, çizim ve lab. |
| [Aimee Knight, 1 Eylül 2025](https://www.aimeemarieknight.com/Passing-the-Google-Professional-Cloud-Developer-Exam/) | Önceki turda tam metin okundu. Deneyime rağmen üç ay hazırlık; senaryoları gerçek deneyimlerle ilişkilendirme. İngilizce veya bitirme süresine sayısal veri yok. |
| [Yusuke Enami, 23 Ocak 2024](https://medium.com/@bigface00/journey-of-a-professional-google-cloud-developer-eb70e33c1f78) | Önceki turda tam metin okundu. Yönetilen servis gereksinimi, maliyet/erişilebilirlik dengesi üzerinden seçenek eleme. |
| [Darren Lester, 2 Kasım 2024](https://medium.com/google-cloud/tips-for-passing-the-google-professional-developer-pcd-exam-c2b6d2253d17) | Önceki turda tam metin okundu. Hedef sözcükleri: en kolay/hızlı/ucuz/az karmaşık. Tecrübeli kişinin kolaylık değerlendirmesi herkese aktarılmaz. |
| [Sabuj Jana, 17 Ağustos 2023](https://medium.com/@SabujJanaCodes/clearing-gcp-professional-cloud-developer-certification-38c4de5e1865) | Tam metin okundu. GKE/networking tecrübesiyle kısa hazırlık; internet/proctor sorunları. Startup vaka çalışması iddiası Jonathan'ın 2022 sonrası gözlemiyle çelişiyor; güncel form kanıtı sayılmadı. |
| [Jaroslav Pantsjoha / Contino, 25 Mart 2020](https://www.contino.io/insights/google-professional-cloud-developer-certification) | Tam metin okundu. Üç yıllık GCP deneyimine rağmen orta zorluk; uygulamada öğrenilen spesifik ayrıntılar, ürünleri use case'e göre ayırma. Stackdriver/HipLocal ve eski servis listeleri güncel kapsam diye alınmadı. |
| [Alexander Darby / osintalex, 28 Mart 2022](https://medium.com/@alexanderdarby/how-to-pass-gcp-professional-cloud-developer-c057fbd2cb9c) | Tam metin okundu. Production monitoring, rollback, IAM, GKE; eğitimden fazla Kubernetes ağırlığı gözlemi. Yıl sayısından çok uygulamanın kapsamını önemsiyor. |
| [Ivam Luz, 11 Aralık 2019](https://medium.com/ci-t/how-to-pass-the-google-professional-cloud-developer-certification-2e89e5aaa31f) | Tam metin okundu. PCA'ya göre daha dar ve derin bulmuş; benzer ürünlerin farkını öğrenme ve belirsiz soruya sonra dönme. |
| [Ivam Luz / freeCodeCamp, 15 Haziran 2020](https://www.freecodecamp.org/news/how-to-pass-almost-every-google-cloud-professional-certification-exam/) | Tam metin okundu. Aynı adayın birden çok sertifikayı kapsayan rehberi; bağımsız ikinci aday sayılmaz. 2020 beta süreleri güncel süre diye kullanılmaz. |
| [Sangita Mahala, 24 Ocak 2023](https://medium.com/@sangitamahala/becoming-a-google-cloud-certified-professional-cloud-developer-your-ultimate-exam-guide-3861b7e40f72) | Tam metin okundu; sertifika beyanı ve çalışma kaynakları var. Belirli yakın şık/süre olayı yok; PCD yanında PCA kurs bağlantısı da bulunduğundan öneriler ayrıştırılmalı. |
| [Udesh Udayakumar, 17 Ekim 2022](https://pilotudesh.medium.com/pass-the-gcp-cloud-developer-exam-2022-9f58b4a511e9) | Üyelik duvarına kadar okundu. Başlık 2023, yayın 2022. İki yıllık GCP/DevOps geçmişi; hazırlık bölümü erişilemedi. The Cloud Pilot aynı yazar; videosu ayrı aday sayılmaz. |

## Deneyim gibi görünüp farklı çıkanlar

- [Tistory journal0767, 23 Nisan 2025](https://journal0767.tistory.com/1): Chrome'da tamamı okundu. Altı haftalık hazırlık iddiası var; tek yazılı blog, Study4Exam tanıtımı, doğrulanabilir sınav ayrıntısı az. Düşük ağırlıklı; Korece alan adı yazının Korece olduğu anlamına gelmez, metin İngilizce.
- [NoCramming forumu](https://forum.nocramming.com/threads/prepare-for-google-cloud-developer-exam-practice-tests-resources.96/): tamamı okundu. Study4Exam bağlantılı genel hazırlık tanıtımı; sınava girip soru hatırlayan aday anlatımı değil.
- [Anil Kumar, 15 Şubat 2024](https://medium.com/@gcp.akp/pass-the-google-cloud-professional-cloud-developer-certification-53ef0a312a23): tamamı okundu. Udemy yönlendirmeli tanıtım/genel rehber; somut sınav günü anlatımı yok. 2026 yazısı önceki notta ayrı değerlendirildi.
- [Harshad, 20 Mart 2024](https://medium.com/the-cloud-factory/professional-cloud-developer-exam-preparation-guide-part-1-0e7a3959fd52): üyelik duvarına kadar; hazırlık serisi, kişisel sınav deneyimi doğrulanmadı.
- [TheServerSide / Cameron McKenzie, 19 Şubat 2025](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Google-Cloud-Developer-Certification-Practice-Exams): hazırlık yaklaşımı ve kendi test ürününün tanıtımı incelendi. Sonraki uzun soru bankası tek tek çözülmedi; bir adayın hatırladığı gerçek sorular diye sayılmadı. Aynı sitedeki Mayıs tarihli sample/dump başlıklı sonuçlar da pratik içerik olarak ayrıldı.
- [Reddit “15 days”, Aralık 2025](https://www.reddit.com/r/googlecloud/comments/1pn1yf7/i_need_to_pass_the_google_professional_cloud/): erişilebilir ana metin ve yorumlar okundu; OP sonraki yorumda tamamlamadığını ve ek süre verildiğini söylüyor. 15 günde geçti diye kaydedilmedi. Kapalı More replies altındaki bütün yorumlar açılmış değildir.
- [Volodymyr Tarasov, 19 Ocak 2024](https://medium.com/@vptarasov/google-cloud-certification-my-experience-and-practical-advice-482fe3e95472): tam metin sınavı **Cloud Digital Leader** diye tanımlıyor; PCD kanıtından çıkarıldı.
- [The CyberSec Migrant, 22 Ocak 2026](https://www.youtube.com/watch?v=wwKp71HZKHw): Chrome'da tam başlık/açıklama kontrol edildi; **Professional Cloud Architect**, PCD değil.
- [C2C / Sebastian Moreno kaydı, 11 Mayıs 2022](https://www.c2cglobal.com/articles/tips-and-tricks-for-the-professional-cloud-developer-exam-full-recording-2753): sayfa okundu; 7:30 vaka, 24:00 zorluk bölümleri listeleniyor. Video içeriği dinlenmedi; yalnız bölüm başlıklarından cevap çıkarılmadı.

## Sayfa bazında tarama izi

Bu tablo her satırdaki sonuçların tam metin okunduğu iddiası değildir. Reklamlar tıklanmadı.

| Google sayfası | Deneyim açısından ayrıştırılan sonuçlar / diğerleri |
|---|---|
| 1 | Amanda, Yusuke, Aimee; quigath/2026 hazırlık/15 gün Reddit başlıkları; Cloud Pilot; ExamTopics ve soru çözüm videoları. |
| 2 | Sabuj Jana; Sathish kaynak dizini; resmî PCD/Skills; Codecademy/Udemy/Global prep ve satış sayfaları. |
| 3 | Ivam freeCodeCamp, Contino, NoCramming; bankalar, kurslar, genel sınav açıklamaları. |
| 4 | Josh, Pavel, C2C, Pluralsight rehberi; Pass4Success ve kataloglar; Oracle alakasız. |
| 5 | Tistory; kurs/soru bankaları, Get Certified programı; Adobe/MS/IBM sonuçları alakasız. |
| 6 | Jonathan Reynolds PCD; resmî exam-guide PDF ve voucher; soru bankaları. |
| 7 | GDG Lawrence hazırlık oturumu; genel rehberler/bankalar; IBM/AWS/Adobe. |
| 8 | Darren; TheServerSide; Udemy/CertLibrary; farklı sınav/Trailhead sonuçları. |
| 9 | Certsim/Exam-Labs; PCD başlıklı PDF; PCA/PDE/ACE/AWS/UiPath ve alakasız sosyal sonuçlar. |
| 10 | TheServerSide pratik yazısı; WebAsha/KloudExams/Whizlabs/Udemy; SAP/Hashicorp/DevOps/IBM. |
| 11 | Alexander Darby; diğerleri Databricks/OpenText/MongoDB/Adobe/Anthropic vb. |
| 12 | Soru bankaları; DevOps/ML videoları ve diğer sertifikalar; yeni PCD aday yazısı yok. |
| 13 | Udesh Medium; TheServerSide örnek sorular; kurs/banka ve PCA/AWS/Database. |
| 14 | Ivam'ın PCD'ye özel yazısı; kurs/banka ve ACE/PCA/Azure/Adobe/AWS. |
| 15 | Jonathan'ın başka sonucu DevOps; PCD pratik video ve ExamTopics tekrarı; diğerleri farklı sertifikalar. |
| 16 | Udemy PCD testi; kalanların çoğu Digital Leader/Azure/IBM/Oracle/AWS. |
| 17 | Anil 2026 (önceden incelenmiş); CyberSec Migrant başlığı açılınca PCA çıktı; diğer kurslar. |
| 18 | Sangita; PCD test/kurs videoları; diğer sertifikalar. |
| 19 | Anil 2024, Harshad, Joe Holbrook beta videosu; PCD kursları ve diğer sertifikalar. |
| 20 | PCD pratik videoları/kursları; yeni aday anlatımı yok. |
| 21 | Tarasov açılınca Digital Leader çıktı; genel sertifika rehberi, kurslar ve farklı sınavlar. |
| 22 | Udemy/SkillCertPro hazırlık içerikleri; Claude/AWS vb.; sonraki sayfa bağlantısı yok. |

## Sonuç ve çalışmaya etkisi

Kullanıcı Udemy'de yaklaşık 20 dolara soru satıldığı iddiasını aktardı; hangi kurs olduğu belli değil, fiyat doğrulanmadı. [Priya Dw / CertShield PCD practice tests](https://www.udemy.com/course/gcp-google-professional-cloud-developer-practice-exam/) sayfası ayrıca açıldı: 372 soru, altı deneme, Haziran 2026 güncellemesi, açıklamalı ve gerçek sınavın biçim/zorluğunu yansıtmak üzere hazırlanmış sorular iddiası. Sayfa bunları doğrulanmış gerçek sınav kopyaları olarak tanımlamıyor. Satıcının benzerlik iddiası bağımsız kalite doğrulaması değildir; 20 dolar bilgisi bu kursa bağlanmadı. Satın alma yapılmadı.

“Az kaynak buldum” → “az yazılmış” çıkarımı desteklenmiyor. Bu tek Google sorgusu bile önceki taramada eksik kalmış aday anlatımlarını çıkardı. Sonuç sayısının büyüklüğü de aynı sayıda bağımsız ve güncel aday deneyimi demek değil.

En somut ek kanıtlar: Pavel'de okuma/bağlam süresi; Jonathan'da son saniyelere kadar kullanılan süre; Cloud Pilot'ta benzer seçenekler; Josh/Joe'da hatırlanan soru türleri. Bunlar kullanıcının kaygısının yalnız teknik bilgi açığına indirgenemeyeceğini destekler. Hiçbiri S09'un uzunluk/zorluk eşdeğerliğini veya belli İngilizce düzeyinin yeterliliğini kanıtlamaz.

Resmî [PCD sayfası](https://cloud.google.com/learn/certification/cloud-developer): 120 dakika, 50–60 soru. [Google kayıt yardımı](https://support.google.com/cloud-certification/answer/9907651?hl=en): randevuya idari işlemler için 15 dakika eklenir; bu 135 dakika soru çözümü değildir. Önceki turda doğrulandı.

Yeni test, cevap, puan veya ustalık ölçümü yok. S10 20 soru/45 dakika tercihi korunur. Yeni oturum için bildirim/otomasyon kurulmadı.
