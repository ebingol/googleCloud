# Udemy PCD — 372 soruluk kaynak incelemesi

İnceleme tarihi: 5 Ekim 2026. Kaynak: Priya Dw / CertShield, **GCP Professional Cloud Developer Practice Tests Updated 2026**. [Kurs](https://www.udemy.com/course/gcp-google-professional-cloud-developer-practice-exam/).

**Karar: Bu paketi güvenilir bir ana deneme/cevap anahtarı olarak önermiyorum.** Yararlı senaryolar var; ancak yanlış işaretlenmiş cevaplar, doğru şıkkın altında yanlış teknik açıklamalar, eski servisler ve tekrarlar birlikte görülüyor. Sınava yakın dönemde her açıklamayı ayrıca doğrulamak önemli ek iş çıkarır. Kullanıcının kalite beklentisi bakımından iade istemek için somut gerekçeler var; iade başvurusu yapılmadı ve kabul garantisi yok.

## Kullanıcının öğrenme amacı için ek değerlendirme

5 Ekim devamı: Ana kaynak olarak güvenilir bulmamak, paketin öğrenme değerini sıfırlamaz. Kullanıcı geçen adayın bu amaçla yararlandığını aktardı. Soru senaryoları üzerinden hizmet seçimini çalışabiliriz; asistan her işlenen sorunun anahtarını/açıklamasını doğrular ve gerekli düzeltmeyi yapar. Hatalı anahtar kullanıcı bilgi eksiği olarak puanlanmaz. İade önerisi zorunlu sonuç değildir; kontrollü öğrenme için kaynağı kullanmak makul bir seçenek. Adayın GKE, Eventarc/Tasks, geliştirme ortamı ve sample exam uzunluğu anlatımı çalışma önceliğine yardımcı olur, sınav dağılımını garanti etmez.

## Kapsam ve sınırlar

| Set | Erişilen ve taranan sorular | Öne çıkan bulgular |
|---|---|---|
| PT1 | Q1–Q60, 60/60 | Runtime kimliği, gcloud açıklamaları, yakın tekrarlar |
| PT2 | Q1–Q60, 60/60 | SQL bağlantı yetkisi/veri yetkisi ayrımı; Q1/Q5 birebir tekrar |
| PT3 | Q1–Q60, 60/60 | PDB, BigQuery view yetkisi, IAM rol adı, alakasız referans |
| PT4 | Q1–Q60, 60/60 | Desteklenmeyen push exactly-once; subscription/subscriber karışıklığı; kapatılmış Debugger |
| PT5 | Q1–Q60, 60/60 | Batch fiyat açıklaması, emulator, bozuk seçenek/kod metni |
| PT6 | Q1–Q72, 72/72 | SQL Proxy izinleri, secret rotasyonu, private SQL peering, Spot manifesti; Q52/Q53 birebir tekrar |
| **Toplam** | **372/372** | **Tam soru taraması; aşağıdaki bulgular için hedefli derin doğrulama** |

Sorular, seçenekler ve cevap anahtarları bütün setlerde tarandı. Açıklamaların şüpheli bölümleri ayrıntılı okunup aşağıdaki teknik bulgular resmî kaynaklarla karşılaştırıldı. Bu çalışma her açıklamadaki her cümlenin bağımsız doğruluk sertifikası veya bütün kodların çalıştırıldığı bir test değildir. Görsel olarak gömülü olup metin aktarımına girmeyen kod/şemalar ayrıca doğrulanmış sayılmaz. İşaretlenmemiş sorular için “kesin doğru” sonucu çıkarılmamalı; paket için güvenilir bir hata yüzdesi hesaplanmadı.

Numaralar bu oturumdaki review sırasıdır; Udemy başka denemede sıralamayı değiştirirse konu ile birlikte eşleştirilmeli. Ham erişim metinleri ve soru kimlikleri yerel `reviews/` dizininde, sonraki kontrollere yardımcı olmak üzere bulunuyor. Tam soru metinleri bu raporda yeniden yayımlanmıyor.

**Puan kaydı:** Açıklamaları görmek için altı deneme boş bitirildi. Udemy'deki 0/60 ve 0/72 sonuçları asistanın inceleme işlemleridir; kullanıcının sınav performansı değildir. Kullanıcının S10 19/20 ve S11 43/50 ilk sonuçları değişmedi.

## Teknik bulgular

“Anahtar” yanlış/eksik doğru seçenek; “açıklama” seçimin mutlaka yanlış olduğu anlamına gelmeden öğretici metindeki hata; “editoryal” metnin kendi içindeki sorun anlamındadır.

| Yer | Tür | Sorun ve doğru ayrım |
|---|---|---|
| **PT1 Q1** | Açıklama | Verilen seçeneklerde `gsutil cp` geçerli. Fakat gcloud'un Storage'a dosya kopyalayamadığı genellemesi yanlış: `gcloud storage cp` var. Hatalı `gcloud cp` sözdizimi ile ürünün yeteneği karıştırılmış. [CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) |
| **PT1 Q4** | Açıklama | `--filter` her zaman sunucu tarafında uygulanmaz; API'ye göre istemci, sunucu veya ikisi olabilir. Bu yüzden daha az veri indirileceği garanti edilemez. [Filtreler](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters) |
| **PT1 Q42** | Anahtar | Bucket yazma yetkisini `gcf-admin-robot` servis ajanına vermeyi doğru sayıyor. Fonksiyon kodunun kullandığı **runtime service account** ile platformun yönetim ajanı ayrı kimliklerdir. Hedef bucket izni runtime kimliğine verilmelidir. [Functions IAM](https://docs.cloud.google.com/functions/docs/concepts/iam) |
| **PT2 Q22** | Açıklama | Cloud SQL Client doğru bağlantı rolü; ancak açıklama bunu veri okuma/yazma yetkisi gibi anlatıyor. Proxy bağlantı izni, veritabanı içindeki kullanıcı/grant izinlerinin yerine geçmez. [Proxy kimlik modeli](https://github.com/GoogleCloudPlatform/cloud-sql-proxy#credentials) |
| **PT3 Q7** | Anahtar/açıklama | Sadece normal view'a erişim vererek temel veriye erişim sorununu çözmüş sayıyor; authorized-view adımı eksik. Üstelik authorized view seçeneğini veri kopyası oluşturduğu gerekçesiyle eliyor. Logical view veriyi kopyalamaz. Şık I'in dataset yerleşimi de sorunlu; temiz bir alternatif anahtar dayatılmamalı. [Authorized views](https://docs.cloud.google.com/bigquery/docs/create-authorized-views), [logical views](https://docs.cloud.google.com/bigquery/docs/views-intro) |
| **PT3 Q33** | Editoryal/uygulama | Doğru seçenekte `roles/iam.workloadIdentity` yazıyor; bu bağlamdaki rol `roles/iam.workloadIdentityUser`. Açıklamanın komutunda doğru ad var. KSA→IAM SA bağlama yönteminde annotation da gerekir. [GKE WIF](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) |
| **PT3 Q47** | Anahtar/açıklama | Deployment rolling update sırasında PDB'nin %80 erişilebilirliği garanti ettiğini söylüyor. Deployment/StatefulSet rollout'u PDB tarafından sınırlandırılmaz. Rollout için `maxUnavailable`, `maxSurge` ve readiness ayarları kullanılmalı. Ayrıca “PDB %80” tek başına `minAvailable` mı `maxUnavailable` mı belirtmiyor. [Kubernetes disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) |
| **PT3 Q55** | Editoryal | Cloud Run→private Cloud SQL sorusunun iki referansı da Cloud Storage customer-supplied encryption key sayfalarına gidiyor. Seçilen VPC connector yaklaşımı mümkün; yanlış referans cevap yanlışlığına tek başına kanıt değil, kaynak kontrolündeki hataya kanıt. |
| **PT4 Q1** | Anahtar | GitFlow/feature branch + change advisory board'u Google'ın önerisi olarak seçiyor; günlük main entegrasyonunu eliyor. Verilen seçeneklerde günlük küçük entegrasyon, trunk-based development önerisiyle uyumludur. [DORA](https://dora.dev/capabilities/trunk-based-development/) |
| **PT4 Q14** | Anahtar | **Push subscription + exactly-once** doğru gösterilmiş. Pub/Sub exactly-once yalnız pull/StreamingPull için desteklenir. Push için bu ayar uygulanamaz. [Pub/Sub exactly-once](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery) |
| **PT4 Q25** | Anahtar | Aynı audit işini ölçeklemek için her VM'ye ayrı subscription öneriyor. Bu, her subscription'a mesajın bir kopyasını gönderir. İş paylaşımı için aynı subscription'ı birden fazla subscriber tüketebilir; A seçeneği bu modele karşılık gelir. Açıklama subscriber ile subscription'ı karıştırıyor. [Pub/Sub veri akışı](https://docs.cloud.google.com/pubsub/docs/pubsub-basics) |
| **PT4 Q42** | Editoryal | Tek seçimli anahtarda C, açıklamanın başında C+D var. Kullanıcıya hata bildirme için C anlamlı; retry ayrıca sınır ve idempotency gerektirir. Açıklama ile puanlanan cevap tutarlı değil. |
| **PT4 Q44** | Güncellik | Stackdriver Debug Logpoints aktif bir çözüm olarak öneriliyor. Cloud Debugger **31 Mayıs 2023'te kapatıldı**. Haziran 2026 güncellemesi iddiasıyla uyuşmayan somut eski içerik. [Kapatılma duyurusu](https://docs.cloud.google.com/stackdriver/docs/deprecations/debugger-deprecation) |
| **PT4 Q45; PT5 Q2** | Açıklama | Batch query ile on-demand fiyat modelini karşıt seçeneklermiş gibi anlatıp batch'in ucuzluğunu genelliyor. Batch bir önceliktir; on-demand işlenen byte'a, capacity modeli kapasiteye göre ücretlendirilir. Batch seçmek tek başına indirim sağlamaz. [Sorgu türleri ve fiyat modelleri](https://docs.cloud.google.com/bigquery/docs/query-overview) |
| **PT5 Q31** | Anahtar/açıklama | Seçilen `${gcloud ... env-init}` komutu hatalı; macOS/Linux örneği `$(gcloud beta emulators pubsub env-init)`. `PUBSUB_EMULATOR_HOST` ayarlamak da belgelenmiş yöntemdir; açıklama IV'te bu değişken bulunmadığını söylüyor ama şıkta açıkça var. [Emulator kurulumu](https://docs.cloud.google.com/pubsub/docs/emulator) |
| **PT6 Q6** | Anahtar/açıklama | Proxy için yalnız `cloudsql.instances.connect` yeterli diyor. Resmî Proxy README'si **connect ve get** izinlerini ister; Cloud SQL Client önerilen roldür. Windows'ta Unix socket öneren diğer şık da düzgün alternatif değil. [Proxy gerekli izinler](https://github.com/GoogleCloudPlatform/cloud-sql-proxy#credentials) |
| **PT6 Q29** | Anahtar/açıklama | Secret Manager'da eski sürümün açık kalmasını, eski DB şifresinin veritabanında hâlâ geçerli olmasıyla eşitliyor. Yeni şifre + `latest` + 15 dakika cache **tek başına sıfır kesinti garantilemez**. DB tarafındaki geçiş ve eski/yeni credential kabul süresi koordine edilmeli. Google sürekli `latest` çözümlemenin yaygın kesinti riskini ayrıca belirtir. [Rotasyon önerileri](https://docs.cloud.google.com/secret-manager/docs/rotation-recommendations) |
| **PT6 Q60; PT3 Q1 açıklaması** | Anahtar/açıklama | İstemci VPC'sini SQL'e bağlı müşteri VPC'siyle peering yapınca private SQL'e erişileceğini genelliyor. PSA'da SQL'in servis üretici ağına ikinci peering geçişi vardır; **transitive peering desteklenmez**. Shared VPC, uygun PSC düzeni veya belgelenen diğer bağlantı çözümleri gerekir. [Private SQL sınırlamaları](https://docs.cloud.google.com/sql/docs/mysql/private-ip) |
| **PT6 Q69** | Açıklama/uygulama | Spot için etiketi `metadata.labels` altına koyuyor. Gerekli seçim `spec.nodeSelector` veya node affinity içindedir. Verilen manifest Spot node seçimini sağlamaz. “Autopilot varsayılanı Balanced” ifadesi de doğru değil; varsayılan genel amaçlı sınıftır. [Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods) |
| **PT6 Q42** | Açıklama | Vulnerability metadata'nın 30 günde kaybolduğunu/expired olduğunu söylüyor. Son 30 günde çekilmeyen image'ın bulguları güncellenmez ve stale olur; 90 günden uzun stale kalan metadata arşivlenir ve API üzerinden değerlendirilebilir. Image pull ile yenileme mümkün, ama anlatılan yaşam döngüsü yanlış. [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) |

## Tekrarlar ve metin kalitesi

Soru+şık metinleri boşluklar normalize edilerek karşılaştırıldığında iki birebir tekrar çifti doğrulandı: **PT2 Q1/Q5** ve **PT6 Q52/Q53**. Dolayısıyla 372 sayısı 372 farklı soru anlamına gelmiyor. Açıklamaların farklı yazılması tekrar olgusunu değiştirmiyor.

Yakın senaryo tekrarlarına örnekler: PT1 Q5/Q24 (CPU HPA), PT1 Q11/Q23 (Istio path erişimi), PT4 Q45/PT5 Q2 (BigQuery batch), PT5 Q28/PT6 Q39 (öneri algoritması A/B), PT6 Q13/Q67 (anında koltuk rezervasyonu), PT6 Q2/Q51 (Cloud Run kademeli trafik). Bunlar bütün semantik tekrarların kesin sayımı değildir. Aynı konunun farklı kısıtlarla ölçülmesiyle aynı kararın yeniden yazılması ayrılmalı.

PT4 Q1 ile PT6 Q47 aynı SCM kararında farklı yön öğretiyor: ilki CAB/feature branch'i, ikincisi günlük main entegrasyonunu savunuyor. PT5 Q30 runtime service account yaklaşımını doğru kurarken PT1 Q42 servis ajanına yetki veriyor. Paket içi tutarsızlık ezberle hazırlanmayı özellikle riskli yapıyor.

Metin aktarımında **PT5 Q24**'ün doğru seçeneğine, bucket/CDN çözümünün sonuna ilgisiz unmanaged instance group adımı eklenmiş. **PT5 Q40**'ta pip adımı, YAML liste kapatması ve substitution sözdizimleri bozuk görünüyor. Bunlar metinsel editoryal bulgular; görsel render ile ayrı teyit edilmeden teknik hata sayısına eklenmedi. **PT4 Q31**'de performans verisi toplama talebinden Cloud SQL→Firestore göç kararına atlanıyor; bu göçü gerekçelendirecek iş yükü koşulları soru kökünde yok.

## Sınav kapsamı ve pratik değeri

Güçlü taraf: Cloud Run, GKE, IAM/WIF, Pub/Sub, veri deposu seçimi, Binary Authorization, Cloud Build ve gözlemlenebilirlik üzerine çok sayıda karar sorusu var. Özellikle PT5'in son bölümü ve PT6; Artifact Registry, Workflows, workforce federation, PSC, supply-chain güvenliği gibi daha yeni başlıklar içeriyor. Ancak PT6'da da yukarıdaki ciddi hatalar bulunduğu için onu otomatik güvenilir saymıyorum.

Resmî sertifika sayfasından açılan güncel rehberde alan ağırlıkları **32/23/24/21**. Kurs açıklaması **36/23/20/21** yazıyor. Rehber AI araçları/IDE entegrasyonları, AI ile test ve gözlemlenebilirlik de içeriyor. Erişilen soru metinlerinde Gemini yalnız PT6 Q72'nin yanlış seçeneğinde bulunuyor; hedefli metin araması kapsamın bu kısmı için belirgin eksiklik işareti. Anahtar kelime araması tek başına eksiksiz konu eşlemesi değildir. [Güncel resmî rehber](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf).

PT1 ekranındaki 3 saat ve kursun %70 eşiği satıcının deneme ayarları. Resmî PCD sınavı **2 saat, 50–60 soru**; Udemy puanı veya barajı resmî geçiş ölçütü sayılmamalı. [Resmî sınav bilgisi](https://cloud.google.com/learn/certification/cloud-developer).

Bu kaynaktan yararlanılacaksa yanlışlara düşülen puan üzerinden teknik eksik teşhisi koymadan önce anahtar kontrol edilmeli. Benim önerim, kalan çalışma zamanını bu paketin anahtarını düzeltmeye ayırmak yerine güvenilir rehber ve doğrulanmış senaryolarla sürdürmek. SkillCertPro'nun ücretli sorularına erişilmedi; bu rapor onun daha iyi veya daha kötü olduğunu söylemez.
