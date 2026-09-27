# PCD-S08 — Türkçe açıklamalar ve kapsam

[Soru dosyasına dön](../../scenarios/PCD-S08.md)

**Çözüm sonrası aç.** İlk seçimleri değiştirme; açıklama sonrası kavrayışı ayrı değerlendir. Hazırlanma: 27 Eylül 2026. Henüz kullanıcı sonucu veya zorluk kalibrasyonu yok.

## Tasarım ve kaynak yaklaşımı

50 soru; 16 tasarım, 12 geliştirme/test, 12 deployment, 10 entegrasyon. Bu dağılım rehberdeki yaklaşık %32/%23/%24/%21 ağırlıklarına yakın bir çalışma dağılımıdır. Her sorunun birincil alanı bir kez sayılır; yan konular ikinci kez soru olarak sayılmaz.

[Resmî exam guide](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) 27 Eylül 2026’da kontrol edildi. Dört ana alanın 11 numaralı alt başlığının her birinde doğrudan soru vardır. Ürün örneklerinin bir kısmı tamamlayıcı açıklamalarda öğretilir; her ürünün her ayarı bağımsız ölçülmüş değildir. Sondaki harita bu ayrımı gösterir.

Kullanıcının hedefi “sample’dan biraz zor ve öğretici”dir. [Resmî sample formu](https://docs.google.com/forms/d/e/1FAIpQLSfFeB8zBNi2q-ar0V7iIguhk2e6P-UkrJ8OJfg6n0k6HcYLDQ/viewform) soru sayfalarından önce kayıt bilgisi istediği için bu oturumda sorularına erişilip doğrudan kıyas yapılmadı; bilgi girilmedi veya sınav gönderilmedi. Bu nedenle zorluk bir tasarım hedefidir. Niş syntax/limit ezberi yerine temel karar ve küçük bir ek koşul kullanıldı.

Kaynaklar ek resmî web dokümanlarıdır; ders PDF’lerindeki belirli sayfalara dayandırılmış sorular gibi sunulmaz. Önceki kararların tekrarlandığı yerler açıkça pekiştirme olarak işaretlendi.

## Hızlı anahtar

| Soru | Doğru | Birincil rehber maddesi | Öğrenme konusu |
|---|---|---|---|
| 01 | D | 1.1 | Platform seçimi ve işletim yükü |
| 02 | B | 2.1 | Lokal ADC ile gcloud kimliği |
| 03 | B | 3.2 | Deployment, Pod ve Service |
| 04 | A | 4.1 | Cloud SQL bağlantı havuzu |
| 05 | B | 1.1 | Session affinity ve paylaşılan durum |
| 06 | B | 2.1 | Gemini Code Assist ve repository bağlamı |
| 07 | A + E | 3.2 | Startup, readiness ve liveness |
| 08 | C | 1.2 | Çalışan erişimi ve müşteri kimliği |
| 09 | A | 4.1 | Pub/Sub fan-out ve iş paylaşımı |
| 10 | C | 3.1 | Cloud Run source deployment |
| 11 | C | 2.1 | Workstations, Cloud Shell ve lokal IDE |
| 12 | A | 1.1 | Zonal HA ve regional disaster recovery |
| 13 | C | 3.2 | HPA ve cluster autoscaler |
| 14 | D | 4.1 | Firestore transaction ve tekrar |
| 15 | A + D | 1.2 | GKE uygulama kimliği ve ağ izni |
| 16 | D | 2.1 | Emulator ile production doğrulaması sınırı |
| 17 | A + C | 3.1 | Cloud Run servis çağrısı |
| 18 | D | 1.3 | Firestore büyüyen listeyi modelleme |
| 19 | B | 4.1 | Cloud Storage resumable upload |
| 20 | B | 2.2 | Build once ve aynı artifactı terfi ettirme |
| 21 | C | 3.2 | Requests ve limits |
| 22 | B | 1.2 | Secret saklama, rotation ve KMS rolü |
| 23 | C | 2.2 | Multi-stage image ve build cache |
| 24 | B + D | 4.2 | API enablement ve service account yetkisi |
| 25 | D | 1.3 | Spanner ve ilişkisel veri ihtiyacı |
| 26 | B | 3.1 | Eventarc alıcısı ve teslimat |
| 27 | B | 2.1 | MCP tool erişimi ve least privilege |
| 28 | C | 1.1 | Scheduler, Workflows, Tasks görev ayrımı |
| 29 | B | 4.2 | Pagination, field selection ve cache |
| 30 | A | 3.1 | Cloud Run Jobs tasks ve parallelism |
| 31 | C | 1.2 | Retention, lifecycle ve organization policy |
| 32 | C + E | 2.2 | Cloud Build ortak dosya ve step sırası |
| 33 | B | 3.2 | Rolling update ve PDB ayrımı |
| 34 | A | 4.2 | Vision API asynchronous batch |
| 35 | A | 2.2 | Provenance neyi kanıtlar? |
| 36 | C | 1.3 | Bigtable row key ve erişim paterni |
| 37 | D | 3.2 | GKE NetworkPolicy ve IAM sınırı |
| 38 | D | 1.3 | Geçici object erişimi ve signed URL |
| 39 | A | 2.3 | AI unit test ve doğru oracle |
| 40 | A | 4.2 | Retry, backoff ve deadline |
| 41 | C | 1.1 | Global load balancer ve API yönetimi ayrımı |
| 42 | D | 2.1 | Cloud Assist ile kanıta dayalı inceleme |
| 43 | D | 3.1 | Canary, rollback ve uyumlu schema |
| 44 | B + E | 4.3 | Metrics, logs, traces ve Error Reporting |
| 45 | A | 1.2 | Statik image taraması ve çalışan web uygulaması |
| 46 | D | 2.3 | Integration test izolasyonu ve sonuç koruma |
| 47 | A | 1.2 | Artifact onayı ve deployment enforcement |
| 48 | C | 4.2 | Generative AI API çıktısını uygulamaya bağlama |
| 49 | D | 1.3 | BigQuery batch analytics ve ham veri |
| 50 | A | 3.1 | Apigee API versioning ve güvenlik |

## Açıklamalar

### Q01 — Platform seçimi ve işletim yükü

**Doğru: D.**

**Sorunun sade Türkçesi:** HTTP uygulaması için ihtiyacı karşılayan, yönetimi az platformu seç.

**Kararı belirleyen kural:** HTTP istekleri, stateless çalışma ve request-driven scaling Cloud Run service ile örtüşür. GKE Kubernetes gereksinimi olduğunda, Compute Engine host kontrolü gerektiğinde anlamlıdır.

**Şıklardaki tuzak:** GKE Autopilot node yönetimini azaltır ama verilen basit service için Kubernetes workload yönetimi ekler. Job sürekli HTTP sunucusu değildir; peak-sized VM boş kapasite maliyeti taşır.

**Küçük örnek:** Sepet API’si service olabilir; gece rapor üretimi job olabilir.

**Önceki çalışma ilişkisi:** Pekiştirme; S02-01 job seçiminin ters kullanım koşulları, platform karşılaştırması.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/run/docs/overview).

---

### Q02 — Lokal ADC ile gcloud kimliği

**Doğru: B.**

**Sorunun sade Türkçesi:** gcloud çalışıyor ama uygulamanın kendi credential kaynağı eksik.

**Kararı belirleyen kural:** Lokal ADC kurulumu client library içindir. gcloud auth login ile ADC aynı credential deposu olmak zorunda değildir. Production’da attached identity kullanılabilir.

**Şıklardaki tuzak:** Project seçmek kimlik oluşturmaz. Password/key gömmek gereksiz ve keyless akışa aykırıdır. CLI kullanıcısı ile uygulama kimliğini ayrı düşün.

**Küçük örnek:** Terminalin giriş yapmış olması IDE’deki programın da giriş yaptığı anlamına gelmez.

**Önceki çalışma ilişkisi:** Pekiştirme; S01-11/S06-02, environment precedence yerine temel ADC ayrımı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

---

### Q03 — Deployment, Pod ve Service

**Doğru: B.**

**Sorunun sade Türkçesi:** Pod yeniden yaratılınca ayarlar kaybolmasın; istemci her seferinde yeni IP aramasın.

**Kararı belirleyen kural:** Deployment istenen Pod şablonunu ve replica sayısını yönetir. Service değişen Pod’ların önünde kararlı bir erişim noktası sağlar.

**Şıklardaki tuzak:** Service yapılandırma kaynağı değildir. Node artırmak veya mevcut Pod’u elle değiştirmek kalıcı uygulama tanımının yerini tutmaz.

**Küçük örnek:** Deployment üç çalışanı aynı talimatla başlatır; Service müşterinin bildiği tek telefon numarasıdır.

**Tamamlayıcı bilgi — ayrıca puanlanmaz:** Hiyerarşi: Google Cloud project → GKE cluster. Cluster’da node’lar Pod çalıştırır; namespace Pod ve Service gibi kaynakları mantıksal olarak gruplar. Deployment aynı namespace’te Pod oluşturulmasını yönetir; Service onları seçer. KSA uygulama kimliği, node ise makinedir. emptyDir Pod ömrüne bağlıdır; kalıcı veri gerekiyorsa uygun PVC/PV veya yönetilen datastore seçilir.

**Önceki çalışma ilişkisi:** Temel pekiştirme; S07 Q13 sonrası kullanıcının belirttiği GKE hiyerarşi eksikliği.

**Ek resmî kaynaklar:** [Doküman 1](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/); [Doküman 2](https://kubernetes.io/docs/concepts/services-networking/service/); [Doküman 3](https://kubernetes.io/docs/concepts/overview/); [Doküman 4](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

---

### Q04 — Cloud SQL bağlantı havuzu

**Doğru: A.**

**Sorunun sade Türkçesi:** Güvenli bağlanmak yetmiyor; toplam bağlantı sayısı DB kapasitesini aşmasın.

**Kararı belirleyen kural:** Pool bağlantıyı tekrar kullanır. Instance sayısı × instance başına pool kapasitesi birlikte düşünülür; diğer kullanıcılar ve geçişler için pay bırakılır.

**Şıklardaki tuzak:** Auth Proxy/connector authentication ve güvenli bağlantı sağlar; tek başına application pooling yapmaz. Private IP için uygun network yolu ayrıca gerekir.

**Küçük örnek:** 20 instance × 5 bağlantı yaklaşık 100 application bağlantısı planıdır; DB bütçesinin tamamını buna ayırma.

**Önceki çalışma ilişkisi:** Pekiştirme; bağlantı bütçesi/autoscaling, Cloud SQL ve AlloyDB proxy ayrımı açıklamada.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/sql/docs/postgres/manage-connections); [Doküman 2](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy); [Doküman 3](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview).

---

### Q05 — Session affinity ve paylaşılan durum

**Doğru: B.**

**Sorunun sade Türkçesi:** Instance değişse bile onaylanmış sepet kaybolmasın.

**Kararı belirleyen kural:** Affinity yönlendirme kolaylığıdır; kalıcı veri garantisi değildir. Asıl kayıt durable shared store’da tutulur, cache yeniden kurulabilen hızlandırıcıdır.

**Şıklardaki tuzak:** Minimum instance belirli process’in ölümsüzlüğünü sağlamaz. Yalnız cache’e taşıma da belirtilen durability gereksinimini karşılamaz.

**Küçük örnek:** Cache silinince sepeti asıl veritabanından yeniden okuyabilmelisin.

**Önceki çalışma ilişkisi:** Karma; S05-01/05 cache tasarımı + session affinity, yeni durability birleşimi.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/run/docs/configuring/session-affinity); [Doküman 2](https://docs.cloud.google.com/memorystore/docs/redis/high-availability).

---

### Q06 — Gemini Code Assist ve repository bağlamı

**Doğru: B.**

**Sorunun sade Türkçesi:** AI’ın doğru sürüm ve gerçek interface’e göre kod önermesini sağla.

**Kararı belirleyen kural:** Bağlam hatayı azaltır; compile/test/review doğrulama sağlar. AI coding assistant kodu hızlandırır ama doğruluğu otomatik kanıtlamaz.

**Şıklardaki tuzak:** Tekrar edilen veya akıcı anlatılan cevap doğru olmak zorunda değil. Gereksinimi AI çıktısına uydurmak kapsamı değiştirir.

**Küçük örnek:** Kullandığın kütüphanenin mevcut interface’ini göster; hayali metoda güvenme.

**Önceki çalışma ilişkisi:** Pekiştirme; S05-10, bilinçli AI context temel tekrarı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini).

---

### Q07 — Startup, readiness ve liveness

**Doğru: A + E.**

**Sorunun sade Türkçesi:** Geç açılmayı hata sanma; geçici olarak hizmet veremeyen Pod’a yeni trafik gönderme.

**Kararı belirleyen kural:** Startup başlangıca zaman tanır. Readiness trafik alabilir mi sorusudur; başarısızlığı kendi başına container restart etmez. Liveness container’ın yeniden başlatılması gereken yerel arızasını izler.

**Şıklardaki tuzak:** Ortak dependency kesintisinde tüm Pod’ları restart etmek kesintiyi çözmez, yükü artırabilir.

**Küçük örnek:** Açılıştaki hazırlık=startup; kapıyı müşteriye açabilmek=readiness; kilitlenmiş kasayı yeniden başlatmak=liveness.

**Önceki çalışma ilişkisi:** Pekiştirme; S02-12 ve kullanıcının açıkça belirttiği probe eksikliği.

**Ek resmî kaynaklar:** [Doküman 1](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

---

### Q08 — Çalışan erişimi ve müşteri kimliği

**Doğru: C.**

**Sorunun sade Türkçesi:** Çalışana iç uygulama kapısı, müşteriye ürün içinde giriş sistemi gerekiyor.

**Kararı belirleyen kural:** IAP iç uygulamaya erişim kapısı; Identity Platform customer identity için uygundur. Oturum açmak uygulamadaki her kaynağa yetki demek değildir.

**Şıklardaki tuzak:** API key insan kimliği değildir. KMS encryption içindir. Browser’a ortak service-account key vermek kullanıcı ayrımını ve yetki sınırını bozar.

**Küçük örnek:** Destek ekibinin panel erişimi ile müşterinin kendi hesabına girişi farklı işlerdir.

**Önceki çalışma ilişkisi:** Yeni ölçüm; S07-05 JWT detayından daha temel ürün/kimlik amacı ayrımı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/iap/docs/concepts-overview); [Doküman 2](https://docs.cloud.google.com/identity-platform/docs/product-comparison).

---

### Q09 — Pub/Sub fan-out ve iş paylaşımı

**Doğru: A.**

**Sorunun sade Türkçesi:** İki farklı uygulama her event’i alsın; her uygulamanın kendi worker’ları işi paylaşsın.

**Kararı belirleyen kural:** Topic’e bağlı ayrı subscription’lar bağımsız tüketim sağlar. Aynı subscription üzerindeki worker’lar iş paylaşır; her biri tüm mesajların ayrı kopyasını almaz.

**Şıklardaki tuzak:** Ack deadline fan-out oluşturmaz. İşin kalıcı kabulü/işlenmesi tamamlanmadan ack vermek güvenilirliği bozabilir; duplicate güvenliği yine gerekir.

**Küçük örnek:** Bir gazetenin iki aboneliği: kargo departmanının ve analiz departmanının kopyaları ayrı.

**Önceki çalışma ilişkisi:** Pekiştirme; publish/subscribe ile competing workers temel farkı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/pubsub/docs/pubsub-basics); [Doküman 2](https://docs.cloud.google.com/pubsub/docs/subscriber).

---

### Q10 — Cloud Run source deployment

**Doğru: C.**

**Sorunun sade Türkçesi:** Desteklenen uygulamayı Dockerfile yazmadan source’tan Cloud Run’a gönder.

**Kararı belirleyen kural:** Source deployment desteklenen buildpacks ile image oluşturabilir; container ortadan kalkmaz, build işi yönetilir. Özel gereksinimde Dockerfile gerekebilir.

**Şıklardaki tuzak:** Cloud Shell üretim hosting hizmeti değildir. Source deployment runtime IAM ve API izin ihtiyacını kaldırmaz; senaryoda bunlar hazır.

**Küçük örnek:** Kaynak kodu verirsin; paketleme ve deploy zinciri image’ı üretir.

**Önceki çalışma ilişkisi:** Pekiştirme; Cloud Run source/image ayrımını temel seviyede uygulama.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/run/docs/deploying-source-code).

---

### Q11 — Workstations, Cloud Shell ve lokal IDE

**Doğru: C.**

**Sorunun sade Türkçesi:** Ortak araçları merkezi yönet; geliştiricinin dosyalarını kalıcı tut.

**Kararı belirleyen kural:** Workstations managed ortamı sağlar; image araçları, persistent home çalışma dosyalarını taşır. Cloud Shell hızlı browser CLI, Cloud Code ise IDE entegrasyonu rolündedir.

**Şıklardaki tuzak:** Çalışan container’a elle kurulum yeni workstation’lara taşınmaz. Stop etmeyerek kalıcılık sağlanmaz. Cloud Shell ile workstation fleet ihtiyacı aynı değildir.

**Küçük örnek:** Compiler image’da; üzerinde çalıştığın repository persistent home’da.

**Tamamlayıcı bilgi — ayrıca puanlanmaz:** Console web yönetim arayüzü; gcloud CLI/SDK terminal ve otomasyon araçları; Cloud Shell tarayıcıdan hazır çalışma shell’i; Cloud Code lokal veya uygun uzak IDE’de cloud geliştirme entegrasyonudur. Gemini Code Assist kod üzerinde, Gemini Cloud Assist cloud kaynakları/operasyon bağlamında yardımcı olur; görev ve desteklenen entegrasyonu kontrol et.

**Önceki çalışma ilişkisi:** Pekiştirme; S05-02/06, temel ortam/persistence eşleştirmesi.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/workstations/docs/overview); [Doküman 2](https://docs.cloud.google.com/workstations/docs/customize-container-images); [Doküman 3](https://docs.cloud.google.com/code/docs/vscode/overview); [Doküman 4](https://docs.cloud.google.com/shell/docs/overview).

---

### Q12 — Zonal HA ve regional disaster recovery

**Doğru: A.**

**Sorunun sade Türkçesi:** Tek bölge tamamen giderse veritabanı ve uygulama nasıl geri gelir?

**Kararı belirleyen kural:** Zon arızası ile bölge arızasının kapsamı farklıdır. Cross-region replica ve test edilmiş recovery planı ikinci bölgeyi kullanır; replication lag RPO’ya yansır.

**Şıklardaki tuzak:** Aynı bölgedeki ek zone regional outage çözmez. Asenkron replica için koşulsuz sıfır veri kaybı söylenemez.

**Küçük örnek:** İki farklı binadaki sunucu, iki farklı şehirdeki kurtarma planıyla aynı koruma değildir.

**Tamamlayıcı bilgi — ayrıca puanlanmaz:** Consistency ile availability aynı soru değildir. Cloud SQL/AlloyDB asenkron read veya cross-region replica gecikebilir; yeni write’ı hemen görmek gerekiyorsa uygun primary/read yolu seçilir. Bigtable multi-cluster routing’de replication ve seçilen okuma yolu önemlidir; tek-cluster routing güçlü tutarlılığı koruyabilir. Spanner strong read ve bilinçli stale read ayrımı sunar. Cloud Storage object read/list işlemleri güçlü tutarlıdır; CDN/browser cache eski içerik gösterebilir. Her ürünün bütün replica türlerinin aynı davranışı gösterdiğini varsayma.

**Önceki çalışma ilişkisi:** Karma; S04-05 zonal HA ile S07-09 replica lag, yeni bölgesel recovery kararı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/sql/docs/postgres/high-availability); [Doküman 2](https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas); [Doküman 3](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication); [Doküman 4](https://docs.cloud.google.com/bigtable/docs/replication-overview); [Doküman 5](https://docs.cloud.google.com/spanner/docs/reads); [Doküman 6](https://docs.cloud.google.com/storage/docs/consistency).

---

### Q13 — HPA ve cluster autoscaler

**Doğru: C.**

**Sorunun sade Türkçesi:** HPA Pod istiyor ama onları çalıştıracak node kapasitesi yok.

**Kararı belirleyen kural:** HPA replica sayısını, cluster autoscaler node kapasitesini değiştirir. Uygun Pending Pod’lar node büyümesini tetikleyebilir; quota ve sınırlar da izin vermelidir.

**Şıklardaki tuzak:** Desired replica çalışıyor demek değildir. Readiness henüz schedule edilmemiş Pod’a makine sağlamaz.

**Küçük örnek:** Yeni çalışan almak HPA; çalışanların oturacağı masaları artırmak node autoscaler.

**Önceki çalışma ilişkisi:** Pekiştirme; önceki GKE autoscaling ayrımlarını sadeleştirme.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler); [Doküman 2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

---

### Q14 — Firestore transaction ve tekrar

**Doğru: D.**

**Sorunun sade Türkçesi:** Son ürünü iki kişiye satma; transaction tekrarında iki e-posta üretme.

**Kararı belirleyen kural:** Transaction okunan verinin eşzamanlı değişimini ele alarak atomik kararı sağlar. Callback yeniden çalışabilir; dış yan etkiyi bunun içine koyma.

**Şıklardaki tuzak:** Batched write birden çok write’ı atomik yapabilir ama daha önce yapılmış bağımsız read’i conflict kontrolüne dönüştürmez.

**Küçük örnek:** Önce rezervasyon kaydıyla stok birlikte kesinleşir. E-posta worker’ı aynı reservation ID için tekrar gönderimi önler.

**Önceki çalışma ilişkisi:** Pekiştirme; S04 transaction/retry ve dış yan etki ayrımı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/firestore/native/docs/manage-data/transactions).

---

### Q15 — GKE uygulama kimliği ve ağ izni

**Doğru: A + D.**

**Sorunun sade Türkçesi:** Pod hangi kimlikle konuşacak ve o kimlik hangi bucket’ı okuyabilir?

**Kararı belirleyen kural:** Dedicated KSA uygulamayı ayırır; WIF onu Google Cloud’a tanıtır; bucket IAM okuma yetkisini verir. Ağ kontrolü farklı bir katmandır.

**Şıklardaki tuzak:** Deployer yetkisi runtime’a taşınmaz. NetworkPolicy IAM yerine geçmez. Key dosyası verilen keyless şartını bozar.

**Küçük örnek:** Kapıya ulaşabilmek ile kapıyı açma yetkisi ayrı şeylerdir.

**Önceki çalışma ilişkisi:** Pekiştirme; S03-04 ve son hiyerarşi açıklaması; cross-cluster identity sameness ölçülmüyor.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity); [Doküman 2](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

---

### Q16 — Emulator ile production doğrulaması sınırı

**Doğru: D.**

**Sorunun sade Türkçesi:** Lokal veri davranışını hızlı test et; gerçek cloud ayarlarını ayrıca doğrula.

**Kararı belirleyen kural:** Emulator hızlı izolasyon sağlar; production parity sınırsız değildir. Ayrı cloud test ortamı IAM/network/deployment bağlantılarını sınar.

**Şıklardaki tuzak:** Production test sandbox değildir. Tamamen mock test, gerçek servis bağlantısı kanıtı olamaz. Emulator başarısı gerçek IAM iznini doğrulamaz.

**Küçük örnek:** Lokal test işlemin mantığını, staging testi gerçekten erişebildiğini gösterir.

**Önceki çalışma ilişkisi:** Pekiştirme; S04-06, emulator sınırını öğretici biçimde ölçer.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/firestore/native/docs/emulator).

---

### Q17 — Cloud Run servis çağrısı

**Doğru: A + C.**

**Sorunun sade Türkçesi:** Orders çağıran, billing alıcı. İzin alıcı üzerinde çağırana verilir; token alıcıya hitap eder.

**Kararı belirleyen kural:** Invoker authorization sağlar; doğru audience taşıyan ID token caller kimliğini doğrulatır. Network erişimi bu iki gereksinimin yerine geçmez.

**Şıklardaki tuzak:** Rol yönünü ters çevirmek çağrıyı yetkilendirmez. OAuth access token ile Cloud Run invocation ID token aynı amaçta değildir.

**Küçük örnek:** Orders’ın kartında billing kapısına giriş izni var; gösterdiği kart da billing kapısı için düzenlenmiş.

**Önceki çalışma ilişkisi:** Bilinçli pekiştirme; S01/R01 audience konusu, önceki anlık doğru kavrayış kalıcılık ölçümü değildir.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

---

### Q18 — Firestore büyüyen listeyi modelleme

**Doğru: D.**

**Sorunun sade Türkçesi:** Sürekli büyüyen mesaj geçmişini nasıl saklayıp sayfalarsın?

**Kararı belirleyen kural:** Özet parent’ta, mesajlar ayrı documents/subcollection’da olursa liste büyümesi parent’a yığılmaz; query/pagination tasarlanabilir. Index’ler gereken sorgulara göre seçilir.

**Şıklardaki tuzak:** Tek büyük array/document büyüme ve contention yaratır. İçeriği silmek history şartını bozar. Subcollection seçimi otomatik bütün maliyetleri azaltma garantisi değildir.

**Küçük örnek:** Bir dosyanın kapağı ayrı, içindeki mesaj kayıtları ayrı tutulur.

**Önceki çalışma ilişkisi:** Yeni ölçüm; S06 index exemption veya transaction yerine document/subcollection modelleme.

**Ek resmî kaynaklar:** [Doküman 1](https://firebase.google.com/docs/firestore/manage-data/structure-data).

---

### Q19 — Cloud Storage resumable upload

**Doğru: B.**

**Sorunun sade Türkçesi:** Büyük dosyada bağlantı kopunca baştan başlama; sunucunun aldığı yerden sürdür.

**Kararı belirleyen kural:** Resumable upload aktif session ile ilerlemeyi sürdürebilir. Yerel tahmin yerine server’ın kabul ettiği offset esas alınır; session URI gizli tutulur.

**Şıklardaki tuzak:** Upload problemi public erişimle veya list pagination ayarıyla çözülmez. Geçersiz/sona ermiş session gerektiğinde yeni upload gerektirebilir.

**Küçük örnek:** 1 GB’ın 700 MB’ı kabul edildiyse aktif session’da kalan kısmı gönder; “göndermeyi denedim” ile “server aldı” farklıdır.

**Önceki çalışma ilişkisi:** Temel storage API uygulaması; interrupted transfer kararı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/storage/docs/resumable-uploads).

---

### Q20 — Build once ve aynı artifactı terfi ettirme

**Doğru: B.**

**Sorunun sade Türkçesi:** Test ettiğin image ile production’a giden image aynı olsun.

**Kararı belirleyen kural:** Source commit ile image digest farklı kimliklerdir. Aynı artifact digest’i terfi ettirilir; environment configuration ayrı tutulur.

**Şıklardaki tuzak:** Tekrar build dependency değişimi getirebilir. Tag/label içerik eşitliği kanıtı değildir. Secret’ı image’a gömmek doğru çözüm değildir.

**Küçük örnek:** Test edilmiş paketi gönder; aynı tarifle sonradan başka paket üretme.

**Önceki çalışma ilişkisi:** Pekiştirme; S04-03, farklı environment config ile temel artifact promotion.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/artifact-registry/docs/docker/names); [Doküman 2](https://docs.cloud.google.com/run/docs/deploying).

---

### Q21 — Requests ve limits

**Doğru: C.**

**Sorunun sade Türkçesi:** Bir task’ın gerçekten ihtiyaç duyduğu bellek, container limitini aşıyor.

**Kararı belirleyen kural:** Memory limit aşıldığında OOM olabilir. Request scheduling hesabına katılır; limit runtime sınırıdır. Profil sonucuna uygun ikisini ayarlamak gerekir.

**Şıklardaki tuzak:** Node’da boş bellek olması container limitini iptal etmez. Replica sayısı tek task’ın bellek ihtiyacını küçültmez.

**Küçük örnek:** Her iş 1,5 GiB istiyorsa 512 MiB sınırındaki on worker da aynı büyük işte sorun yaşar.

**Önceki çalışma ilişkisi:** Temel pekiştirme; GKE resource gereksinimi, ölçülmüş ihtiyaçtan karar.

**Ek resmî kaynaklar:** [Doküman 1](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

---

### Q22 — Secret saklama, rotation ve KMS rolü

**Doğru: B.**

**Sorunun sade Türkçesi:** Parolayı image’dan çıkar; yalnız gereken uygulama okusun ve kontrollü değişsin.

**Kararı belirleyen kural:** Secret versions, dar IAM ve tüketicilerin yeni değere geçmesi birlikte planlanır. KMS encryption-key rotation ile supplier credential rotation farklı işlemlerdir.

**Şıklardaki tuzak:** Yeni image etiketi içeriği değiştirmez. Owner gereksiz geniştir. Secret’ın değişmesi, onu startup’ta okumuş process’in anında yenilenmesi demek değildir.

**Küçük örnek:** Yeni anahtarı etkinleştir, uygulamayı geçir, eski anahtarı sonra kapat.

**Önceki çalışma ilişkisi:** Pekiştirme; S01-01/S05-11/S06-13, ayrı rotation kavramlarını temel düzeyde birleştirir.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/secret-manager/docs/best-practices); [Doküman 2](https://docs.cloud.google.com/kms/docs/key-rotation).

---

### Q23 — Multi-stage image ve build cache

**Doğru: C.**

**Sorunun sade Türkçesi:** Build araçları final image’da kalmasın; değişmeyen bağımlılık adımı tekrar kullanılabilsin.

**Kararı belirleyen kural:** Multi-stage build runtime çıktısını ayırır. Manifest önce, sık değişen source sonra düzeni cache kullanımını iyileştirir; gereken runtime dependency korunur.

**Şıklardaki tuzak:** Tüm filesystem’i kopyalamak compiler yükünü taşır. Cache’i bozmak hız çözümü değildir. En küçük image her zaman çalışır image demek değildir.

**Küçük örnek:** Mutfak ekipmanını teslim etmiyorsun; çalışması için gerekenlerle birlikte ürünü teslim ediyorsun.

**Önceki çalışma ilişkisi:** Karma; S05-18 cache düzeni + runtime-only multi-stage kararı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.docker.com/build/building/multi-stage/); [Doküman 2](https://docs.docker.com/build/cache/optimize/).

---

### Q24 — API enablement ve service account yetkisi

**Doğru: B + D.**

**Sorunun sade Türkçesi:** API açık olmalı; uygulama kimliği de istediği işlemi yapabilmeli.

**Kararı belirleyen kural:** Enablement hizmeti projede kullanılabilir yapar. IAM hedef işlemi kimin yapabileceğini belirler. ADC credential bulma yöntemidir; otomatik yetki vermez.

**Şıklardaki tuzak:** API’yi açabilmek veriyi okuyabilmek değildir. API key çoğu korunan GCP resource için IAM principal’ın yerine geçmez.

**Küçük örnek:** Binanın açık olması ve senin o odaya giriş kartın olması iki ayrı kontrol.

**Önceki çalışma ilişkisi:** Bilinçli temel pekiştirme; API/ADC/IAM üç ayrı sorumluluk.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/service-usage/docs/enable-disable); [Doküman 2](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

---

### Q25 — Spanner ve ilişkisel veri ihtiyacı

**Doğru: D.**

**Sorunun sade Türkçesi:** Yatay büyüyen, bölgeler arası ilişkisel transaction sistemi seç.

**Kararı belirleyen kural:** Spanner dağıtık ilişkisel transaction ihtiyacına uygundur. PostgreSQL uyumu ve mevcut uygulama korunacaksa Cloud SQL/AlloyDB ayrıca değerlendirilir; soru onu istemiyor.

**Şıklardaki tuzak:** AlloyDB read pool okuma ölçeği sağlar; sorudaki multi-region dağıtık write gereksinimiyle aynı şey değildir. BigQuery analytics, object storage dosya için uygundur.

**Küçük örnek:** Aynı rezervasyonda koltuk ve ödeme durumunun tutarlı değişmesi gerekiyor.

**Tamamlayıcı bilgi — ayrıca puanlanmaz:** İlişkisel schema’da entity, primary/foreign key ve sorguya uygun index tasarlanır. AlloyDB PostgreSQL uyumu sunar; Spanner’da dağıtık key erişimi ve hotspot riski ayrıca düşünülür. “NoSQL” schema tasarımı gereksiz demek değildir; Firestore ve Bigtable da erişim desenine göre modellenir.

**Önceki çalışma ilişkisi:** Pekiştirme; S01-14, ürün seçiminin gerekçesiyle temel tekrar.

**Ek resmî kaynaklar:** [Doküman 1](https://cloud.google.com/spanner); [Doküman 2](https://docs.cloud.google.com/alloydb/docs/overview); [Doküman 3](https://docs.cloud.google.com/spanner/docs/schema-design).

---

### Q26 — Eventarc alıcısı ve teslimat

**Doğru: B.**

**Sorunun sade Türkçesi:** Event geldiğini doğru anla; iş kalıcı kabul edilmeden tamam dememe ve tekrarı güvenli yönetme.

**Kararı belirleyen kural:** CloudEvent alanları ve payload işlenir. Başarılı yanıt öncesi gerekli kalıcı kabul yapılır; tekrar teslimat duplicate yan etki oluşturmamalıdır.

**Şıklardaki tuzak:** Acknowledgment işin hafızada durduğunu kalıcı hale getirmez. Her zaman error vermek bitmeyen tekrar üretir.

**Küçük örnek:** Kargo talebini deftere kaydetmeden “aldım” deme; aynı talep tekrar gelirse iki kargo çıkarma.

**Tamamlayıcı bilgi — ayrıca puanlanmaz:** Pub/Sub push da Cloud Run’ı tetikleyebilir: push kimliğine receiver üzerinde Invoker verilir, OIDC token/audience doğru yapılandırılır, receiver beklenen mesaj envelope’unu işler. Eventarc CloudEvent ile Pub/Sub push body’sini aynı format sanma. Başarı/ack, retry ve duplicate güvenliği her ikisinde önemlidir.

**Önceki çalışma ilişkisi:** Pekiştirme; event formatı + güvenilir kabul, önceki idempotency konuları bilinçli tekrar.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/eventarc/docs/cloudevents); [Doküman 2](https://docs.cloud.google.com/eventarc/docs/retry-events); [Doküman 3](https://docs.cloud.google.com/run/docs/tutorials/pubsub).

---

### Q27 — MCP tool erişimi ve least privilege

**Doğru: B.**

**Sorunun sade Türkçesi:** AI’ın ihtiyacı kadar tool ve gerçek yetki ver.

**Kararı belirleyen kural:** Tool yüzeyi ve credential IAM kapsamı birlikte sınırlandırılır. Prompt niyet bildirir; güvenlik sınırını tek başına oluşturmaz.

**Şıklardaki tuzak:** Owner + dikkatli ol talimatı teknik kısıtlama değildir. Tool etiketi backend yetkisinin yerini tutmaz.

**Küçük örnek:** Doküman okuması gerekiyorsa production silme yetkisi gerekmez.

**Önceki çalışma ilişkisi:** Pekiştirme; S06-06, kapsamı daraltılmış öğretici MCP sorusu.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer); [Doküman 2](https://docs.cloud.google.com/iam/docs/using-iam-securely).

---

### Q28 — Scheduler, Workflows, Tasks görev ayrımı

**Doğru: C.**

**Sorunun sade Türkçesi:** Her sabah başlayan, sonuçlara göre sırayla ilerleyen süreç kur.

**Kararı belirleyen kural:** Scheduler ne zaman başlayacağını, Workflows adımların nasıl ilerleyeceğini yönetir. Tasks bağımsız hedef dispatch/rate ihtiyacına, Pub/Sub event dağıtımına uygundur.

**Şıklardaki tuzak:** Saat aralığı dependency değildir. Queue/subscription sırası çok adımlı işin durum kaydı ve branching mantığını kendiliğinden kurmaz.

**Küçük örnek:** Önce veriyi hazırla, sonuç uygunsa raporu üret, sonra bildir.

**Tamamlayıcı bilgi — ayrıca puanlanmaz:** Cloud Tasks belirli endpoint’e kontrollü gönderim/retry/rate için, Pub/Sub bağımsız abonelere olay yaymak için uygundur. Apache Airflow’un yönetilen Google Cloud hizmeti, Cloud Composer adıyla bilinen Managed Service for Apache Airflow’dur; DAG tabanlı data pipeline orchestration ihtiyacında değerlendirilir. Bu exam guide’ın Workflows/Tasks/Scheduler maddesi Composer’ın tüm operator ayrıntılarını ezberleme talebi değildir.

**Önceki çalışma ilişkisi:** Karma; S01-15 orchestration üzerine recurring start ve fan-out/dispatch ayrımı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/workflows/docs/overview); [Doküman 2](https://docs.cloud.google.com/workflows/docs/schedule-workflow); [Doküman 3](https://docs.cloud.google.com/tasks/docs/comp-pub-sub); [Doküman 4](https://docs.cloud.google.com/composer/docs/concepts/overview).

---

### Q29 — Pagination, field selection ve cache

**Doğru: B.**

**Sorunun sade Türkçesi:** Tüm sonucu al ama gereksiz alanı ve gereksiz tekrar çağrısını azalt.

**Kararı belirleyen kural:** Pagination tamlık, field selection payload boyutu, cache tekrar çağrı/freshness içindir. Destek API’ye göre kontrol edilir; client library pagination’ı kolaylaştırabilir.

**Şıklardaki tuzak:** Az alan istemek az sayfa demek değildir. Stale = güncelliğini yitirmiş/eski kalmış; izin verilen eskilik sınırını aşma veya kullanıcılar arası veri sızdırma.

**Küçük örnek:** 1000 kaydın tamamını sayfalayarak al; yalnız iki alanı tut; izin verilen 60 saniye boyunca uygun cache anahtarıyla kullan.

**Tamamlayıcı bilgi — ayrıca puanlanmaz:** Desteklenen Cloud Client Library genellikle auth, pagination ve retry kodunu azaltır. REST yaygın HTTP/JSON erişimidir; gRPC desteklenen servislerde typed RPC ve streaming gibi ihtiyaçlara uygundur. Protokolü destek ve istemci gereksinimine göre seç; gRPC her senaryoda otomatik daha iyi değildir. API Explorer tek bir çağrıyı dokümantasyon üzerinden denemeye yarar; kalıcı uygulama runtime’ı değildir.

**Önceki çalışma ilişkisi:** Bilinçli pekiştirme; S07-08 field selection/pagination ve önceki stale kavramı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/apis/docs/system-parameters); [Doküman 2](https://docs.cloud.google.com/apis/docs/client-libraries-explained); [Doküman 3](https://developers.google.com/explorer-help); [Doküman 4](https://grpc.io/docs/what-is-grpc/introduction/).

---

### Q30 — Cloud Run Jobs tasks ve parallelism

**Doğru: A.**

**Sorunun sade Türkçesi:** Toplam 12 parça iş var; aynı anda en çok 3’ü çalışsın.

**Kararı belirleyen kural:** Task count toplam task sayısıdır. Parallelism bir execution’da eşzamanlı çalışabilecek task sayısının üst sınırıdır; input bölme kodun sorumluluğudur.

**Şıklardaki tuzak:** Parallelism task sayısını artırmaz veya veriyi otomatik bölmez. Retry güvenliği kapasite sınırını kaldırmaz.

**Küçük örnek:** 12 paket, aynı anda en fazla 3 kurye. Hepsi aynı anda çıkmak zorunda değil.

**Önceki çalışma ilişkisi:** Pekiştirme; S07-11 sonrası task/parallelism temelini ayrı öğretme.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/run/docs/configuring/parallelism); [Doküman 2](https://docs.cloud.google.com/run/docs/create-jobs).

---

### Q31 — Retention, lifecycle ve organization policy

**Doğru: C.**

**Sorunun sade Türkçesi:** Silme koruması, sonradan temizlik ve public erişim yasağını birlikte kur.

**Kararı belirleyen kural:** Retention korur; lock azaltmayı engeller; lifecycle uygun olduğunda temizler; public access prevention public paylaşımı engeller. Bunlar ayrı kontrollerdir.

**Şıklardaki tuzak:** Lifecycle retention değildir. Versioning tek başına değiştirilemez saklama garantisi değildir. Public erişim kuralı otomatik silme yapmaz.

**Küçük örnek:** Kasayı kilitlemek, saklama süresini belirlemek ve süre sonunda temizlemek üç ayrı iştir.

**Önceki çalışma ilişkisi:** Pekiştirme; S04-17/S06-17 üzerine üç kontrolün rolleri; öğretici tekrar, yeni bilgi sayılmaz.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/storage/docs/bucket-lock); [Doküman 2](https://docs.cloud.google.com/storage/docs/lifecycle); [Doküman 3](https://docs.cloud.google.com/storage/docs/public-access-prevention).

---

### Q32 — Cloud Build ortak dosya ve step sırası

**Doğru: C + E.**

**Sorunun sade Türkçesi:** Çıktı sonraki step’lere ulaşsın; iki kontrol bitmeden paketleme başlamasın.

**Kararı belirleyen kural:** Shared path dosyayı paylaşır; waitFor dependency sırasını kurar. Bunlar farklı gereksinimlerdir.

**Şıklardaki tuzak:** Aynı IAM kimliği filesystem paylaşmaz. Sadece compile’ı beklemek kontrolleri atlar. Failure’ı yutmak release gate’i kaldırır.

**Küçük örnek:** Ortak masaya dosyayı koy; iki imza gelince paketle.

**Önceki çalışma ilişkisi:** Pekiştirme; S01-03 + S04-02, bilinçli iki temel build mekanizması birleşimi.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/build/docs/configuring-builds/pass-data-between-steps); [Doküman 2](https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order).

---

### Q33 — Rolling update ve PDB ayrımı

**Doğru: B.**

**Sorunun sade Türkçesi:** Uygulama sürümünü değiştirirken üç hazır replica kalsın; bir yenisine yer var.

**Kararı belirleyen kural:** Rollout’u Deployment strategy yönetir. maxUnavailable=0 hazır sayısının düşmesine izin vermez; maxSurge=1 ek Pod’a izin verir. PDB rollout stratejisinin yerine geçmez.

**Şıklardaki tuzak:** PDB gönüllü eviction içindir; doğrudan tüm Pod silmelerini veya Deployment rollout’unu engelleyen genel güvence değildir.

**Küçük örnek:** Önce dördüncüyü hazırla, sonra eskilerden birini çıkar. Kapasite veya readiness sorununda rollout bekleyebilir.

**Tamamlayıcı bilgi — ayrıca puanlanmaz:** Graceful termination ayrı katmandır: kapanan uygulama yeni iş almayı bırakır, devam eden işi tamamlar ve bağlantıları kapatır. GKE’de preStop hook süresi de terminationGracePeriodSeconds bütçesine dahildir. Süre dolunca zorla sonlandırma olabilir. Süreyi gerçek shutdown ihtiyacına göre seç; tüm uygulamalar için sabit 45 saniye kuralı yoktur.

**Önceki çalışma ilişkisi:** Pekiştirme; S05-15 sonrası bakım/rollout karışıklığı, termination saniye hesabı yok.

**Ek resmî kaynaklar:** [Doküman 1](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/); [Doküman 2](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/); [Doküman 3](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/).

---

### Q34 — Vision API asynchronous batch

**Doğru: A.**

**Sorunun sade Türkçesi:** Kullanıcı beklemiyor; çok görseli toplu ve asenkron işle, başarısız alt kümeyi ayır.

**Kararı belirleyen kural:** Desteklenen async batch işini başlatıp tamamlanmasını ve GCS çıktısını takip edersin. Operation sonucu ile item hatalarını ayrı incele.

**Şıklardaki tuzak:** Batch limits yok olmaz. Başarılı işleri gereksiz tekrar maliyet/yük üretir. Her Vision özelliğinin aynı yöntem ve limiti desteklediğini varsayma.

**Küçük örnek:** 1000 evraklık tarama işinde 5 hatalı evrak için kalan 995’i yeniden OCR’a sokma.

**Önceki çalışma ilişkisi:** Pekiştirme; S05/S06 API throughput, numeric quota ezberi olmadan Vision uygulaması.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/vision/docs/batch).

---

### Q35 — Provenance neyi kanıtlar?

**Doğru: A.**

**Sorunun sade Türkçesi:** Bu image hangi build’den çıktı, doğrulanabilir şekilde göster.

**Kararı belirleyen kural:** Provenance build kökenini kaydeder. Test davranış, scan bilinen güvenlik bulguları, attestation onay/policy süreçleri için farklı kanıtlardır.

**Şıklardaki tuzak:** Label kendi başına güvenilir köken kanıtı değildir. Provenance da hatasız uygulama veya sıfır açık garantisi değildir.

**Küçük örnek:** Ürünün üretim kaydı ile ürünün kalite testi farklı belgelerdir.

**Önceki çalışma ilişkisi:** Pekiştirme; S06-14, flag ezberi yerine provenance amacı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance).

---

### Q36 — Bigtable row key ve erişim paterni

**Doğru: C.**

**Sorunun sade Türkçesi:** Yazmaları dağıt, aynı cihazın zaman aralığını kolay oku.

**Kararı belirleyen kural:** Row key sorgu yoluna göre tasarlanır. Dağınık device prefix ve timestamp bu varsayımlarda distribution ile locality’yi birleştirir.

**Şıklardaki tuzak:** Zamanı başa koymak yeni yazmaları dar alana toplar. Tamamen rastgele key okuma locality’sini kaybettirir. Tek satır da hotspot olabilir.

**Küçük örnek:** Önce cihazın çekmecesini bul, sonra o çekmecede tarih aralığını tara.

**Önceki çalışma ilişkisi:** Pekiştirme; S04-01 ile aynı temel karar, öğretim amacıyla açık tekrar.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/bigtable/docs/schema-design).

---

### Q37 — GKE NetworkPolicy ve IAM sınırı

**Doğru: D.**

**Sorunun sade Türkçesi:** Payments’a ağdan yalnız frontend ulaşsın; kimlik kontrolü yine devam etsin.

**Kararı belirleyen kural:** NetworkPolicy Pod trafiğini sınırlar; IAM Google Cloud kaynak yetkisi, uygulama authentication ise istek kimliği içindir. Selector kapsamı ve port birlikte doğru seçilir.

**Şıklardaki tuzak:** IAM rolü tek başına Pod ağ filtresi değildir. Aynı from girdisindeki namespaceSelector ve podSelector birlikte daraltır; ayrı girdiler alternatif izinler olabilir. Bu syntax ayrıntısı sorunun ön koşulu değildir.

**Küçük örnek:** Bina içindeki koridoru yalnız frontend’e aç; payments içindeki işlem yetkisini yine kontrol et.

**Tamamlayıcı bilgi — ayrıca puanlanmaz:** Cloud Run’dan private IP’li kaynağa çıkış için Direct VPC egress uygun VPC yolunu sağlayabilir; kaynak tarafı firewall ve authentication ayrıca gerekir. Private Service Connect private endpoint modelidir; Cloud Service Mesh hizmet kimliği, policy ve mTLS gibi ayrı iletişim kontrolleri sunar. Bu seçeneklerin her biri NetworkPolicy ile aynı iş değildir.

**Önceki çalışma ilişkisi:** Temel güvenli GKE deployment; S03 WIF/IAM’den ayrı network katmanı, açık pekiştirme.

**Ek resmî kaynaklar:** [Doküman 1](https://kubernetes.io/docs/concepts/services-networking/network-policies/); [Doküman 2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy); [Doküman 3](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc); [Doküman 4](https://docs.cloud.google.com/vpc/docs/private-service-connect); [Doküman 5](https://docs.cloud.google.com/service-mesh/docs/overview).

---

### Q38 — Geçici object erişimi ve signed URL

**Doğru: D.**

**Sorunun sade Türkçesi:** Google hesabı olmayan müşteriye yalnız bir dosya için kısa erişim ver.

**Kararı belirleyen kural:** Signed URL object, method ve süreye bağlı bearer erişim sağlar. Öncesinde müşteri yetkisini uygulama kontrol eder.

**Şıklardaki tuzak:** Access token yanında path göndermek token’ı o path’e kısıtlamaz. Bucket’ı public yapmak fazla geniştir. Linkin paylaşılabilirliği soruda kabul edilmiştir.

**Küçük örnek:** On dakikalık tek-dosya indirme bileti.

**Önceki çalışma ilişkisi:** Pekiştirme; S01-04/S06-05, bilerek temel yetki kapsamı tekrarı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

---

### Q39 — AI unit test ve doğru oracle

**Doğru: A.**

**Sorunun sade Türkçesi:** Test hatalı kodu onaylamasın; iş kuralını gerçekten sınasın.

**Kararı belirleyen kural:** Expected result kaynağı contract’tır. Dış dependency kontrol edilir, ölçülen gerçek fonksiyon korunur. AI üretti diye assertion doğru sayılmaz.

**Şıklardaki tuzak:** Sonuç fonksiyonunu mock’lamak kendi mock’unu test eder. Retry nondeterminism’i gizler. Coverage doğrulukla aynı değildir.

**Küçük örnek:** Yüzde 10 kuralını kodun bug’ından değil yazılı sözleşmeden hesapla.

**Önceki çalışma ilişkisi:** Pekiştirme; S04-10, kullanıcı isteğiyle temel test mantığına dönüş.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini); [Doküman 2](https://jestjs.io/docs/mock-functions).

---

### Q40 — Retry, backoff ve deadline

**Doğru: A.**

**Sorunun sade Türkçesi:** Geçici arızada kontrollü tekrar; yanlış istekte parametreyi düzelt.

**Kararı belirleyen kural:** Backoff denemeleri seyrekleştirir, jitter eşzamanlı retry yığılmasını azaltır, deadline toplam beklemeyi sınırlar. Library’nin hazır retry davranışını bilerek ayarla.

**Şıklardaki tuzak:** Read-only olmak sınırsız yük üretmeyi güvenli yapmaz. Write çağrılarında ayrıca idempotency ve kısmi başarı değerlendirilir.

**Küçük örnek:** Herkes aynı anda kapıya tekrar yüklenmesin; farklı aralıklarla ve bir son süreyle denesin.

**Önceki çalışma ilişkisi:** Pekiştirme; API tüketiminde temel transient/permanent ayrımı, örnek kaynağın service-specific kuralları genellenmez.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/storage/docs/retry-strategy).

---

### Q41 — Global load balancer ve API yönetimi ayrımı

**Doğru: C.**

**Sorunun sade Türkçesi:** İki bölge için müşteriye tek HTTPS giriş noktası sağla.

**Kararı belirleyen kural:** Load balancer trafik dağıtımı içindir; API kimliği/kotası ayrı ihtiyaçtır. Serverless backend desteğine uygun yapılandırma gerekir; sırf iki servis oluşturmak failover kurmaz.

**Şıklardaki tuzak:** İki ayrı regional endpoint client tarafına seçim yükler ve tek giriş şartını karşılamaz. Quota routing yapmaz; tek bölgedeki instance artışı bölge kaybını çözmez.

**Küçük örnek:** API kapısında kimlik kontrolü başka, isteği uygun bölgeye ulaştırmak başkadır.

**Önceki çalışma ilişkisi:** Yeni ölçüm; S02 ingress sorusundan farklı global front-end ihtiyacı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/load-balancing/docs/https); [Doküman 2](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless).

---

### Q42 — Cloud Assist ile kanıta dayalı inceleme

**Doğru: D.**

**Sorunun sade Türkçesi:** AI incelemeyi hızlandırsın; önerinin kanıtını yine kontrol et.

**Kararı belirleyen kural:** Cloud Assist cloud operasyon bağlamında yardımcıdır; öneri hipotezdir. Logs/metrics ile doğrulanır, değişikliklerin etkisi değerlendirilir.

**Şıklardaki tuzak:** Akıcı açıklama root-cause kanıtı değildir. Code Assist’in kod üretmesi production teşhisini doğrulamaz.

**Küçük örnek:** AI “bağlantı havuzu olabilir” der; sen bağlantı ve latency ölçümlerine bakarsın.

**Önceki çalışma ilişkisi:** Karma; S05-14 ürün rolü + 4.3 AI-assisted troubleshooting uygulaması.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/cloud-assist/overview).

---

### Q43 — Canary, rollback ve uyumlu schema

**Doğru: D.**

**Sorunun sade Türkçesi:** Yeni kod denenirken eski kod hâlâ çalışabilsin; trafik geri dönünce veritabanı yüzünden kırılmasın.

**Kararı belirleyen kural:** Additive = mevcut yapıyı bozmadan eklemek. Geriye uyumlu schema rollout/rollback döneminde iki sürümü destekler. Traffic rollback schema veya veri silinmesini geri almaz.

**Şıklardaki tuzak:** Eski image’a dönmek silinen kolonu yaratmaz. Canary riski azaltır ama veri uyumluluğunun yerine geçmez.

**Küçük örnek:** Önce yeni kolon ekle; iki sürümle uyumlu geçişi yap; eski kolon silmeyi sonraki güvenli aşamaya bırak.

**Önceki çalışma ilişkisi:** Bilinçli pekiştirme; S05-03, kullanıcının additive schema ve rollback soruları.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration); [Doküman 2](https://docs.cloud.google.com/architecture/framework/reliability/reliable-application-design).

---

### Q44 — Metrics, logs, traces ve Error Reporting

**Doğru: B + E.**

**Sorunun sade Türkçesi:** Genel grafiği görüyorsun; şimdi tek isteğin nerede yavaşladığını ve tekrar eden hatayı bul.

**Kararı belirleyen kural:** Metrics eğilim, logs olay ayrıntısı, trace istek yolu/süreleri, Error Reporting hata gruplaması sağlar. Trace context sınırlar boyunca ilişkiyi korur.

**Şıklardaki tuzak:** Trace ID sadece ilk serviste varsa uçtan uca bağ kopar. AI önerisi de bu kanıtlarla doğrulanır; eksik telemetry’yi sihirle oluşturmaz.

**Küçük örnek:** A→B→C isteğinde B→C span’ı 2 saniye sürmüş; aynı trace ID ile o ana ait hata loguna geçersin.

**Önceki çalışma ilişkisi:** Pekiştirme; S06/S07 observability ayrımları, temel araç amacına odaklı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/trace/docs/trace-context); [Doküman 2](https://docs.cloud.google.com/logging/docs/structured-logging); [Doküman 3](https://docs.cloud.google.com/error-reporting/docs).

---

### Q45 — Statik image taraması ve çalışan web uygulaması

**Doğru: A.**

**Sorunun sade Türkçesi:** Image içindeki paketlerin yanında çalışan web davranışını da kontrol et.

**Kararı belirleyen kural:** Artifact Analysis paket/artifact, Web Security Scanner desteklenen web açıkları için kullanılır. Bulguya göre düzeltme ve tekrar doğrulama gerekir; SCC bulguları toplamada yardımcıdır.

**Şıklardaki tuzak:** Tarama geçti diye bütün güvenlik kanıtlanmaz. Trace performans aracıdır; tag değişimi uygulama açığını düzeltmez.

**Küçük örnek:** Kütüphane sürümü güvenli olabilir ama web formunun davranışı ayrıca hatalı olabilir.

**Önceki çalışma ilişkisi:** Yeni ölçüm; S06-18 paket düzeltme yerine runtime scanning kapsamı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview); [Doküman 2](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).

---

### Q46 — Integration test izolasyonu ve sonuç koruma

**Doğru: D.**

**Sorunun sade Türkçesi:** Build’ler birbirinin verisini bozmasın; cleanup test hatasını gizlemesin.

**Kararı belirleyen kural:** İzolasyon nondeterministic çakışmayı kaldırır. Cleanup ayrı sorumluluktur; başarılı temizlik başarısız testi geçirmiş saymaz.

**Şıklardaki tuzak:** Retry yarışın nedenini çözmez. Son komutun exit code’unu körlemesine kullanmak failure’ı yutabilir. Production’a test verisi yazılmaz.

**Küçük örnek:** Her sınavın ayrı çalışma masası olsun; masayı temizledin diye yanlış cevap doğru olmaz.

**Önceki çalışma ilişkisi:** Pekiştirme; S06-10, kısa temel isolation ve release-gate açıklaması.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/build/docs/build-config-file-schema); [Doküman 2](https://docs.cloud.google.com/build/docs/building/build-containers).

---

### Q47 — Artifact onayı ve deployment enforcement

**Doğru: A.**

**Sorunun sade Türkçesi:** Pipeline dışından gelen deploy da onay kuralına uysun.

**Kararı belirleyen kural:** Onay belirli digest’e bağlanır; Binary Authorization deployment aşamasında politikayı uygular. Güvenilen attestation yetkisi korunmalıdır.

**Şıklardaki tuzak:** Etiket taşınabilir; log kendiliğinden enforcement değildir; vulnerability scan işlevsel testlerin yerine geçmez.

**Küçük örnek:** Onay belgesi ürünün değişmeyen kimliğine bağlı olmalı ve girişte kontrol edilmeli.

**Önceki çalışma ilişkisi:** Pekiştirme; S04-14, bilinçli temel release-gate tekrarı.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/binary-authorization/docs/overview).

---

### Q48 — Generative AI API çıktısını uygulamaya bağlama

**Doğru: C.**

**Sorunun sade Türkçesi:** AI çıktısı parse edilebilsin ama doğru formatı doğru karar sanma.

**Kararı belirleyen kural:** Schema yapıyı sınırlar; business validation içerik ve yetkiyi kontrol eder. Hata/uygunsuz sonuç için güvenli uygulama davranışı gerekir.

**Şıklardaki tuzak:** JSON olması semantik doğruluk veya yetki kanıtı değildir. Modelin kendinden emin görünmesi bir güvenlik kontrolü olmaz.

**Küçük örnek:** {"priority":"high"} geçerli JSON olabilir; sözleşme bu müşteri için high önceliğine izin vermiyorsa uygulama bunu reddeder veya incelemeye alır.

**Önceki çalışma ilişkisi:** GenAI API uygulama temeli; Gemini Code Assist ile uygulamanın model API çağrısı farklı sorumluluklar.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output).

---

### Q49 — BigQuery batch analytics ve ham veri

**Doğru: D.**

**Sorunun sade Türkçesi:** Ham dosya kalsın; geçmiş veri SQL ile analiz edilsin; günlük yükleme yeterli.

**Kararı belirleyen kural:** GCS ham dosyayı saklar, BigQuery analytics sorgularını işler. Freshness batch’e uygunsa streaming zorunlu değildir; partitioning erişim desenine göre planlanır.

**Şıklardaki tuzak:** Cache kalıcı tarihçe değildir. OLTP veritabanını büyük dosyaları her sorguda parse etmeye zorlamak uygun tasarım değildir.

**Küçük örnek:** Her gece gelen satış dosyaları, ertesi gün BigQuery raporlarına girer.

**Önceki çalışma ilişkisi:** Yeni ölçüm; S06 pending-stream atomicity yerine temel batch analytics mimarisi.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/bigquery/docs/batch-loading-data).

---

### Q50 — Apigee API versioning ve güvenlik

**Doğru: A.**

**Sorunun sade Türkçesi:** Eski mobil uygulamayı kırmadan v2 sun; iki sürümde de güvenlik devam etsin.

**Kararı belirleyen kural:** API versioning contract değişimini açık yönetir. Apigee routing ve policies ile exposure, authentication ve trafik politikaları uygulanabilir.

**Şıklardaki tuzak:** URL aynı diye response uyumlu olmaz. Load balancer tek başına API contract dönüşümü, kimlik ve quota yönetimini otomatik çözmez.

**Küçük örnek:** /v1/orders eski alanları, /v2/orders yeni contract’ı sunar; kullanım süresi sınırı quota, ani trafik kontrolü SpikeArrest gibi farklı policy amaçlarıdır.

**Önceki çalışma ilişkisi:** Pekiştirme; S06 API versioning ve S07 API management konularını temel karar düzeyine çekme.

**Ek resmî kaynaklar:** [Doküman 1](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development); [Doküman 2](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy); [Doküman 3](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy).

---

## Rehber kapsam haritası

**Soru** doğrudan seçimle ölçülen kararı; **not** cevap anahtarındaki tamamlayıcı öğretimi ifade eder. Not okumak bağımsız soruyu doğru çözmek veya konuyu öğrenmiş olmak sayılmaz. Bu harita her ürünün bütün özellikleri için yeterlilik iddiası değildir.

| Alt başlık | Doğrudan soru numaraları |
|---|---|
| 1.1 | Q1, Q5, Q12, Q28, Q41 |
| 1.2 | Q8, Q15, Q22, Q31, Q45, Q47 |
| 1.3 | Q18, Q25, Q36, Q38, Q49 |
| 2.1 | Q2, Q6, Q11, Q16, Q27, Q42 |
| 2.2 | Q20, Q23, Q32, Q35 |
| 2.3 | Q39, Q46 |
| 3.1 | Q10, Q17, Q26, Q30, Q43, Q50 |
| 3.2 | Q3, Q7, Q13, Q21, Q33, Q37 |
| 4.1 | Q4, Q9, Q14, Q19 |
| 4.2 | Q24, Q29, Q34, Q40, Q48 |
| 4.3 | Q44 |

| Konu kümesi | İlgili sorular | Kapsam biçimi |
|---|---|---|
| Platform, container ve işletim maliyeti | Q1, Q23, Q3, Q10 | Soru; CE/GKE/Run karşılaştırması, image yapısı ve deploy. |
| Coğrafya, routing ve failover | Q12, Q41 | Soru; zon/bölge farkı, latency/routing ve replication lag. |
| Affinity ve cache | Q5 | Soru; Memorystore replaceable cache ve durable state ayrımı. |
| API contract ve trafik politikaları | Q50, Q41 | Soru; versioning/auth/routing. Quota/SpikeArrest amaçları Q50 notunda; API Gateway ayrımı aşağıdaki notta. |
| REST/gRPC ve çağrı seçenekleri | Q29 | Not; protokol desteği, client library ve API Explorer. |
| Asenkron entegrasyon ve orchestration | Q28, Q26, Q9 | Soru; Workflows/Scheduler, Eventarc, Pub/Sub. Tasks ve Airflow amaçları Q28 notunda. |
| Resource sizing ve scaling | Q21, Q13, Q30, Q4 | Soru; memory, Pod/node, task concurrency ve DB budget. |
| Trafik geçişi | Q43 | Soru; canary/rollback. Aynı split mekanizması A/B testinde farklı ölçüm amacıyla kullanılabilir; ayrıca test edilmedi. |
| Saklama ve kurum politikası | Q31 | Soru; lock/lifecycle/public access prevention. |
| Web güvenliği ve bulgu giderme | Q8, Q45 | Soru; IAP, runtime scan ve doğrulama. Artifact Analysis/SCC amaçları açıklamada. |
| Credentials, IAM ve secret rotation | Q22, Q15, Q2, Q17, Q24 | Soru; KMS ayrımı, WIF, ADC, least privilege, ID token. JWT/OAuth ayrımı aşağıdaki notta. |
| Customer identity ve DB bağlantı kimliği | Q8, Q4 | Soru; Identity Platform. Cloud SQL/AlloyDB Auth Proxy amaçları Q4 açıklamasında. |
| Güvenli servis iletişimi | Q37, Q17 | Soru; NetworkPolicy ve invocation. Mesh/Direct VPC/private connectivity Q37 notunda. |
| Artifact güven zinciri | Q47, Q20, Q35 | Soru; digest, provenance, attestation ve Binary Authorization. |
| Datastore ve schema seçimi | Q25, Q18, Q36, Q49, Q14 | Soru; relational/distributed, document, row key, analytics ve atomic read/write. AlloyDB/Spanner schema ilkeleri Q25 notunda. |
| Consistency ve replication | Q12, Q25 | Soru; asenkron lag ve güçlü transaction gereksinimi. Bigtable/Storage/Spanner read farkları Q12 notunda. |
| Object erişimi ve analytics ingestion | Q38, Q49, Q19 | Soru; signed URL, BigQuery batch, resumable upload. BigQuery ML ayrıca notta. |
| Geliştirme ortamı ve AI araçları | Q2, Q11, Q16, Q6, Q27, Q42 | Soru; ADC, Workstations, emulator, bağlam, MCP, Cloud Assist. Console/SDK/Shell/Code rolleri Q11 notunda. |
| Build ve artifact deposu | Q20, Q23, Q32, Q35 | Soru; Artifact Registry, multi-stage/cache, step dependency ve provenance. |
| Unit ve integration test | Q39, Q46 | Soru; AI test oracle ve Cloud Build test isolation/failure. |
| Cloud Run source ve receiver | Q10, Q26, Q17, Q50 | Soru; source build, Eventarc, identity, API exposure. Pub/Sub push Q26 notunda. |
| GKE deployment, health ve HPA | Q3, Q7, Q21, Q13, Q33, Q37 | Soru; template/Service, probes, requests/limits, HPA, rollout, network. |
| Data/messaging bağlantı ve erişim | Q4, Q14, Q9, Q19 | Soru; pooling, transactions, subscriptions, object transfer. |
| API erişimi ve performansı | Q24, Q29, Q34, Q40 | Soru; enablement/IAM, pages/fields/cache, batch ve backoff. Supported transports/explorer Q29 notunda. |
| Observability ve AI ile teşhis | Q44, Q42 | Soru; metrics/logs/spans, trace ID, Error Reporting, evidence-based AI investigation. |
| Generative AI uygulama entegrasyonu | Q48 | Soru; schema ile business validation ayrımı; rehberin giriş yetkinliği. |

### Kısa tamamlayıcı notlar

- **API Gateway / Apigee / load balancer:** API Gateway desteklenen API tanımı ve authentication ile yönetilen gateway sağlar. Apigee daha geniş API management/policy/lifecycle ihtiyaçlarında değerlendirilir. Load balancer trafik yönlendirir; gereksinimi okumadan her API için aynı ürünü seçme. [API Gateway](https://docs.cloud.google.com/api-gateway/docs/about-api-gateway).
- **JWT / OAuth:** JWT bir token biçimi; OAuth 2.0 bir authorization çerçevesidir. Cloud Run invocation’da beklenen ID token ile Google Cloud resource API’sinin access token ihtiyacını karıştırma. Token’ın her zaman aynı kullanım amacı ve audience’a sahip olduğunu varsayma. [Token türleri](https://docs.cloud.google.com/docs/authentication/token-types).
- **BigQuery ve ML:** Analitik veri BigQuery’de tutulabilir; BigQuery ML SQL üzerinden desteklenen model işlerini sağlar. Bu set ingestion/analytics temelini ölçer; belirli ML model syntax’ını ölçmez. [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction).

## Çalışma değerlendirmesi

Yanlışları teknik bilgi eksikliği, İngilizce anlam eksikliği ve belirleyici koşulu kaçırma olarak ayrı incele. K/T ile doğru seçilenler de kısa gerekçe kontrolüne alınır. Henüz çözülmeyen soru yanlış değildir. Bir açıklamayı okumak veya birlikte doğruya ulaşmak ilk deneme puanını değiştirmez.
