# PCD-S12 — Türkçe cevap anahtarı ve kaynak eşlemesi

**İlk denemeden önce açma: doğru cevapları içerir.**

5 Ekim 2026. Kullanıcının istediği Udemy seçkisi; kaynak senaryoları uyarlanmıştır. Bütün seçimler yeniden değerlendirilmiştir; kaynak açıklamaları otomatik doğru kabul edilmemiştir. Resmî dokümanlar değişebilen mekanizmalar için kontrol dayanağıdır. Uygulamalı cloud deployment/lab yapılmadı.

| Soru | Cevap | Rehber | Kaynak soru | Ölçülen karar |
|---|---|---|---|---|
| 1 | D | 2.2 | PT2-Q4 | Özel build aracı |
| 2 | C | 2.2 | PT5-Q9 | Aynı artifact promotion |
| 3 | D | 1.3 | PT6-Q11 | Bigtable failover |
| 4 | C | 3.1 | PT5-Q48 | Cloud Run admission politikası |
| 5 | D | 2.1 | PT4-Q52 | Kurumsal geliştirme ortamı |
| 6 | C | 2.2 | PT5-Q15 | Build step dosya paylaşımı |
| 7 | B | 3.2 | PT6-Q56 | Autopilot Arm yerleşimi |
| 8 | A | 1.3 | PT5-Q44 | Firestore büyüyen mesaj geçmişi |
| 9 | C | 3.1 | PT6-Q59 | Workflows Cloud Run job çağrısı |
| 10 | C | 4.3 | PT5-Q5 | Clusterlar arası log sorgusu |
| 11 | C | 1.2 | PT6-Q21 | Terraform Cloud kimliği |
| 12 | A | 3.1 | PT6-Q57 | Source deploy ile entegrasyon |
| 13 | A | 4.1 | PT6-Q50 | Private SQL yerel erişim |
| 14 | D | 3.2 | PT6-Q18 | Drain sırasında PDB |
| 15 | D | 1.1 | PT6-Q24 | Hot data cache ve kaynak veri |
| 16 | A | 1.1 | PT6-Q34 | Storage olayından çok adımlı işlem |
| 17 | B | 2.2 | PT6-Q17 | Registry olayıyla build |
| 18 | B | 2.2 | PT6-Q20 | Build ile push sınırı |
| 19 | C | 4.1 | PT5-Q54 | SQL analitik ayrımı |
| 20 | B | 4.1 | PT5-Q33 | Küçük API yazımlarını batch etme |
| 21 | A | 4.2 | PT6-Q45 | Cross-project SQL API |
| 22 | B | 3.2 | PT5-Q32 | Trafik uygunluğu |
| 23 | C | 4.2 | PT1-Q38 | İsteğe bağlı API ve arayüz |
| 24 | A+C | 1.2 | PT5-Q30 | Cross-project runtime izinleri |
| 25 | D | 2.3 | PT6-Q49 | Dayanıklılık testi |
| 26 | C | 4.2 | PT5-Q52 | 429 sonrası retry |
| 27 | A+E | 3.2 | PT5-Q34 | Deployment rollout sınırları |
| 28 | A | 1.1 | PT2-Q13 | Büyük dosya upload veri yolu |
| 29 | D | 1.2 | PT1-Q13 | Retention ve lifecycle |
| 30 | A | 1.1 | PT6-Q38 | Üçüncü taraf özelliği kapatma |
| 31 | A | 4.1 | PT5-Q36 | Atomik read-modify-write |
| 32 | C | 1.1 | PT6-Q3 | API ürününe göre kota |
| 33 | B | 1.1 | PT4-Q59 | Workflow dallanması |
| 34 | B+D | 2.2 | PT6-Q14 | Test attestation akışı |
| 35 | B | 2.3 | PT2-Q18 | Tekrarlanabilir messaging testi |
| 36 | B | 3.2 | PT5-Q27 | Yavaş başlangıç ve liveness |
| 37 | D | 3.1 | PT6-Q71 | Bucket create audit olayı |
| 38 | D | 4.3 | PT2-Q45 | CPU ve heap profili |
| 39 | D | 4.3 | PT5-Q46 | Dış servis gecikmesini izleme |
| 40 | C | 1.2 | PT5-Q26 | Namespace yetkisi |
| 41 | B | 1.2 | PT6-Q41 | API güvenliğinin katmanları |
| 42 | B | 1.2 | PT6-Q15 | AlloyDB için ağ ve kimlik ayrımı |
| 43 | B | 3.2 | PT1-Q15 | Pub/Sub backlog ile HPA |
| 44 | A | 3.1 | PT6-Q2 | Cloud Run kademeli rollout |
| 45 | A | 1.3 | PT5-Q22 | Paylaşılan dosya sistemi |
| 46 | A | 1.3 | PT5-Q41 | Bigtable row key |
| 47 | C | 2.3 | PT4-Q7 | Paralel performans testi izolasyonu |
| 48 | A | 2.1 | PT5-Q56 | Yerelde güvenli SQL bağlantısı |
| 49 | D | 3.2 | PT2-Q10 | StatefulSet kimliği |
| 50 | B | 2.1 | PT5-Q39 | Cloud Shell GKE erişim teşhisi |

## Gerekçeler

### Q01 — D

**Özel build aracı** · Rehber 2.2 · Kaynak PT2-Q4

Build step bir container image kullanır; custom builder araç ve sürümü yeniden kullanılabilir biçimde kapsar.

**Yakın alternatif neden elenir?** Jenkins çalışabilir ama sorudaki ihtiyacı karşılamak için yönetilen build sisteminden taşınmak gereksizdir.

**Belirleyici ifade:** “same compiler version; reproducible builds”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/build/docs/configuring-builds/use-community-and-custom-builders).

### Q02 — C

**Aynı artifact promotion** · Rehber 2.2 · Kaynak PT5-Q9

Digest içeriğe bağlı kimliktir. Mutable tag başka içeriğe taşınabilir; production deployment test edilen digest’i kullanmalıdır.

**Yakın alternatif neden elenir?** Semantic/environment tag ancak ayrıca immutable tutulursa güvenlidir; soru tag reuse olabildiğini açıkça söylüyor.

**Belirleyici ifade:** “identical bytes; reuses the same tag”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/artifact-registry/docs/docker/names).

### Q03 — D

**Bigtable failover** · Rehber 1.3 · Kaynak PT6-Q11

Multi-cluster routing uygun replicated cluster’lar arasında failover sağlar. Eventual consistency ve single-row transaction kısıtları açıkça kabul edildi.

**Yakın alternatif neden elenir?** Connection pool ağ/hedef cluster kullanılabilirliği problemini çözmez.

**Belirleyici ifade:** “accepts eventual consistency; operator to change routing”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/bigtable/docs/routing).

### Q04 — C

**Cloud Run admission politikası** · Rehber 3.1 · Kaynak PT5-Q48

CI dışındaki deployment yolunu da kontrol etmek için deployment admission policy gerekir. İlgili güvenilir attestation istenir; yetkili breakglass ayrı denetimli istisnadır.

**Yakın alternatif neden elenir?** Yalnız pipeline test gate’i başka deploy yollarını engellemez.

**Belirleyici ifade:** “including deployments ... outside the usual CI pipeline”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/run/docs/securing/binary-authorization).

### Q05 — D

**Kurumsal geliştirme ortamı** · Rehber 2.1 · Kaynak PT4-Q52

Workstations yönetilen geliştirme ortamı, custom image ise standart toolchain sağlar. Ağ ve perimeter ayrıca doğru kurulmalıdır; haftalık image rebuild tüm güvenliği garanti etmez.

**Yakın alternatif neden elenir?** Cloud Code bir IDE aracı; kendi başına ortak runtime ağı veya merkezi OS imajı oluşturmaz.

**Belirleyici ifade:** “centrally maintained; private access; reproducible tool versions”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/workstations/docs/customize-container-images).

### Q06 — C

**Build step dosya paylaşımı** · Rehber 2.2 · Kaynak PT5-Q15

/workspace build adımları arasında paylaşılan alandır; her container’ın özel geçici dosya sistemi aynı paylaşımı sağlamaz.

**Yakın alternatif neden elenir?** Path bilgisini iletmek dosyanın kendisini paylaşmaz.

**Belirleyici ifade:** “same build; dependency order is already correct”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/build/docs/configuring-builds/pass-data-between-steps).

### Q07 — B

**Autopilot Arm yerleşimi** · Rehber 3.2 · Kaynak PT6-Q56

nodeSelector scheduling zorunluluğunu ifade eder. Desteklenen Autopilot konfigürasyonunda GKE uygun kapasite oluşturur; yalnız toleration bir node’u zorunlu kılmaz.

**Yakın alternatif neden elenir?** Toleration belirli taint’e izin verir; başka uygun node’a yerleşmeyi engellemez.

**Belirleyici ifade:** “provision ... from workload requirements”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke).

### Q08 — A

**Firestore büyüyen mesaj geçmişi** · Rehber 1.3 · Kaynak PT5-Q44

Alt collection mesajları bağımsız yazım ve sorgulanabilir sayfalama birimlerine ayırır; büyüyen tek document sınırına yaslanmaz.

**Yakın alternatif neden elenir?** Tek array her mesajda aynı büyüyen belgeyi değiştirmeyi gerektirir.

**Belirleyici ifade:** “unbounded message history; independently”

[Ek resmî teknik kaynak](https://firebase.google.com/docs/firestore/data-model).

### Q09 — C

**Workflows Cloud Run job çağrısı** · Rehber 3.1 · Kaynak PT6-Q59

Job bir HTTP service değildir; Admin API jobs.run üzerinden execution başlatılır. Workflows connector long-running operation davranışını yönetir.

**Yakın alternatif neden elenir?** Job container’ının web server açması gerekmez; varsayılan request endpoint’i yoktur.

**Belirleyici ifade:** “wait ... complete; no application HTTP server”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/workflows/docs/tutorials/execute-cloud-run-jobs).

### Q10 — C

**Clusterlar arası log sorgusu** · Rehber 4.3 · Kaynak PT5-Q5

Merkezî logging cluster sınırları arasında aynı query ile filtrelemeyi sağlar. resource.type=k8s_container ve workload/project filtreleri gereksiz kayıtları daraltır.

**Yakın alternatif neden elenir?** kubectl current context tek cluster hedefler; diğer cluster loglarını otomatik toplamaz.

**Belirleyici ifade:** “already collected in Cloud Logging; across all three clusters”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs).

### Q11 — C

**Terraform Cloud kimliği** · Rehber 1.2 · Kaynak PT6-Q21

Dış iş yükü kimliği WIF ile kısa ömürlü Google kimliğine çevrilir. Mevcut execution ortamını korur ve kalıcı anahtar gerektirmez.

**Yakın alternatif neden elenir?** GKE üzerinde workload identity mümkün olsa da execution ortamını taşıma şartı gereksizdir.

**Belirleyici ifade:** “keep its existing Terraform Cloud execution environment”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines).

### Q12 — A

**Source deploy ile entegrasyon** · Rehber 3.1 · Kaynak PT6-Q57

Source deploy buildpacks/Cloud Build yolunu kullanarak local Docker kurma ihtiyacını azaltır. Hosted proxy entegrasyonu ayrıca gerçek route üzerinden sınanır.

**Yakın alternatif neden elenir?** Local unit test Apigee ağ/kimlik/routing entegrasyonunun kanıtı değildir.

**Belirleyici ifade:** “no Dockerfile; minimizes local container-tool setup”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/run/docs/deploying-source-code).

### Q13 — A

**Private SQL yerel erişim** · Rehber 4.1 · Kaynak PT6-Q50

Proxy’nin çalıştığı VM private SQL’e ulaşır; IAP geliştiriciden bu VM’ye kontrollü tünel sağlar. Listener/firewall/IAM en dar kapsamda ayarlanır.

**Yakın alternatif neden elenir?** Laptop üzerindeki Auth Proxy ağ erişimi yokluğunu çözmez.

**Belirleyici ifade:** “no VPN route; only a private IP”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/sql/docs/postgres/connect-to-instance-from-outside-vpc).

### Q14 — D

**Drain sırasında PDB** · Rehber 3.2 · Kaynak PT6-Q18

PDB minAvailable=8 ilgili eviction işlemlerine kullanılabilir kopya sınırı koyar. Involuntary failure veya bütçeyi bypass eden silme için mutlak koruma değildir.

**Yakın alternatif neden elenir?** HPA kopya hedefini belirler; drain eviction kabul kontrolünün yerine geçmez.

**Belirleyici ifade:** “voluntary node drains; Eviction API; at least eight”

[Ek resmî teknik kaynak](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/).

### Q15 — D

**Hot data cache ve kaynak veri** · Rehber 1.1 · Kaynak PT6-Q24

Hot subset + kısa staleness toleransı cache-aside için uygundur. Kalıcı doğruluk kaynağı veritabanı olarak kalır.

**Yakın alternatif neden elenir?** Tüm veriyi Redis tek kopya yapmak eviction halinde kalıcı veri kaybını önleme şartını sağlamaz.

**Belirleyici ifade:** “small subset; without moving the full dataset”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview).

### Q16 — A

**Storage olayından çok adımlı işlem** · Rehber 1.1 · Kaynak PT6-Q34

Eventarc olay yönlendirmeyi, Workflows sıra ve durum yönetimini yapar. Worker servisler görevlerine odaklanır. Olay tekrarı için işleme idempotent tasarlanmalıdır.

**Yakın alternatif neden elenir?** Bağımsız abonelere dağıtım bir işlem sırası ve sonuç bağımlılığı kurmaz.

**Belirleyici ifade:** “central definition of the processing sequence”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-storage).

### Q17 — B

**Registry olayıyla build** · Rehber 2.2 · Kaynak PT6-Q17

Registry kaynağındaki bildirim hem pipeline hem manuel upload yolunu kapsar. Cloud Build Pub/Sub trigger doğrudan tüketebilir. VPC-SC sınırı soru kökünde dışlandı.

**Yakın alternatif neden elenir?** Yalnız ana pipeline içindeki bildirim manuel upload’ı kaçırır.

**Belirleyici ifade:** “including ... directly from developer machines”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/build/docs/automate-builds-pubsub-events).

### Q18 — B

**Build ile push sınırı** · Rehber 2.2 · Kaynak PT6-Q20

Build container’ında image üretmek registry’ye upload değildir. Deployment erişilebilir registry artifact’ına ihtiyaç duyar; push’ın tamamlanması beklenir.

**Yakın alternatif neden elenir?** Service adıyla repository adının aynı olması gerekmez.

**Belirleyici ifade:** “neither a push step nor an images output configuration”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/build/docs/building/build-containers).

### Q19 — C

**SQL analitik ayrımı** · Rehber 4.1 · Kaynak PT5-Q54

Datastream CDC ile değişiklikler analitik hedefe aktarılır. Sıfır gecikme/sıfır kaynak yükü garantisi değil; transactional workload ile ağır analitiği ayıran yönetilen yaklaşımdır.

**Yakın alternatif neden elenir?** Dual-write iki hedef başarısızlık/tutarlılık yükünü uygulamaya ekler.

**Belirleyici ifade:** “continuously refreshed; keep using Cloud SQL”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/datastream/docs/overview).

### Q20 — B

**Küçük API yazımlarını batch etme** · Rehber 4.1 · Kaynak PT5-Q33

Bounded batching sabit request overhead’ini amorti eder. Boyut limitleri ve satır bazında kısmi başarısızlıklar ele alınmalıdır.

**Yakın alternatif neden elenir?** Sınırsız tek request API sınırlarını ihlal edebilir; bütün sonuçları başarı varsayamazsın.

**Belirleyici ifade:** “one request per row; request-size limits”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery).

### Q21 — A

**Cross-project SQL API** · Rehber 4.2 · Kaynak PT6-Q45

API enablement IAM’den ayrıdır. Cross-project Cloud Run SQL bağlantısında gerekli API her iki projede açılır.

**Yakın alternatif neden elenir?** Daha geniş IAM rolü kapalı API’yi etkinleştirmez.

**Belirleyici ifade:** “API is disabled in the Cloud Run project”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/sql/docs/postgres/connect-run).

### Q22 — B

**Trafik uygunluğu** · Rehber 3.2 · Kaynak PT5-Q32

Readiness başarısızlığı Service endpoint uygunluğunu etkiler; restart gerektirmez. Liveness process recovery için farklı amaçtadır.

**Yakın alternatif neden elenir?** Startup probe yalnız başlangıcı korur; çalışma boyunca trafik uygunluğunu takip etmez.

**Belirleyici ifade:** “restarting ... would not help; Service traffic”

[Ek resmî teknik kaynak](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

### Q23 — C

**İsteğe bağlı API ve arayüz** · Rehber 4.2 · Kaynak PT1-Q38

Kritik olmayan response başlangıç render’ını bloklamaz; tamamlanınca ilgili UI güncellenir. Hata veya loading durumu ayrıca gösterilebilir.

**Yakın alternatif neden elenir?** Senkron bekleme opsiyonel veriyi tüm kullanıcı deneyiminin kritik yoluna sokar.

**Belirleyici ifade:** “optional; not needed for the initial view”

[Ek resmî teknik kaynak](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest_API/Synchronous_and_Asynchronous_Requests).

### Q24 — A+C

**Cross-project runtime izinleri** · Rehber 1.2 · Kaynak PT5-Q30

Çalışan kodun kimliği runtime SA olur. Hedef bucket üzerinde objectCreator yeni nesne yazımına yeter; farklı proje olması kullanıcı veya servis ajanına yetki verme gerekçesi değildir.

**Yakın alternatif neden elenir?** Developer hesabındaki yetki kodun runtime kimliğine aktarılmaz.

**Belirleyici ifade:** “dedicated runtime identity; new output objects”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/functions/docs/securing/function-identity).

### Q25 — D

**Dayanıklılık testi** · Rehber 2.3 · Kaynak PT6-Q49

Kontrollü fault injection/chaos testi arıza altındaki gerçek retry/failover davranışını gözlemler.

**Yakın alternatif neden elenir?** Load testi kapasite davranışını gösterir; özellikle dependency arızası oluşturmuyorsa recovery kanıtı değildir.

**Belirleyici ifade:** “dependency becomes unreachable; recovery behavior”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/architecture/framework/reliability/perform-testing-for-recovery-from-failures).

### Q26 — C

**429 sonrası retry** · Rehber 4.2 · Kaynak PT5-Q52

Backoff talebi azaltır, jitter istemcileri aynı anda yeniden çağrı yapmaktan uzaklaştırır. Kalıcı quota/bottleneck ayrıca çözülmelidir; retry sonsuz değildir.

**Yakın alternatif neden elenir?** Sabit aynı zamanlama yükü yeniden senkronize edebilir.

**Belirleyici ifade:** “intermittent 429; safe to repeat”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/storage/docs/retry-strategy).

### Q27 — A+E

**Deployment rollout sınırları** · Rehber 3.2 · Kaynak PT5-Q34

maxSurge=1 bir ek Pod’a izin verir; maxUnavailable=0 rollout’un kullanılabilir kopyayı hedefin altına indirmesini önler. Readiness ve kapasite sağlanmış varsayılır; tüm arızalara mutlak uptime garantisi değildir.

**Yakın alternatif neden elenir?** maxSurge=0/maxUnavailable=1 önce eski Pod silmeye izin verir; dört hazır kopyayı korumaz.

**Belirleyici ifade:** “all four; capacity ... one extra Pod”

[Ek resmî teknik kaynak](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

### Q28 — A

**Büyük dosya upload veri yolu** · Rehber 1.1 · Kaynak PT2-Q13

Backend yetkilendirdikten sonra sınırlandırılmış yükleme yetkisini istemciye verir; byte aktarımı doğrudan Storage’a olur. Resumable session URI de bearer credential olarak korunmalıdır.

**Yakın alternatif neden elenir?** Bucket-wide genel yetki hedef nesne ve kullanıcı denetimini gereksiz genişletir.

**Belirleyici ifade:** “retain control over the destination object; bulk-data path”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

### Q29 — D

**Retention ve lifecycle** · Rehber 1.2 · Kaynak PT1-Q13

Retention policy silme/değiştirme engelini, lifecycle transition storage class değişimini sağlar. Archive minimum süre ücretlendirmesi retention garantisi değildir.

**Yakın alternatif neden elenir?** Lifecycle delete kuralı erken manuel silmeyi engellemez.

**Belirleyici ifade:** “undeletable for seven years; retrieval is rare”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/storage/docs/bucket-lock).

### Q30 — A

**Üçüncü taraf özelliği kapatma** · Rehber 1.1 · Kaynak PT6-Q38

Feature flag kodun deployment durumuyla özelliğin etkinliğini ayırır; rutin düzeltmeler kalırken ilgili özellik kapatılır.

**Yakın alternatif neden elenir?** Tam rollback düzeltmeleri de geri alır; istenen yalnız bir yeteneği kapatmaktır.

**Belirleyici ifade:** “disable only that capability”

[Ek resmî teknik kaynak](https://cloud.google.com/architecture/application-deployment-and-testing-strategies).

### Q31 — A

**Atomik read-modify-write** · Rehber 4.1 · Kaynak PT5-Q36

Read ve ona bağlı write aynı transaction denemesinde olmalı. Conflict retry güncel bakiye üzerinden yeniden hesaplar.

**Yakın alternatif neden elenir?** Güçlü tutarlı okuma tek başına okuma ile yazma arasındaki yarışmayı engellemez.

**Belirleyici ifade:** “one credit disappears; both writes succeed”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/datastore/docs/concepts/transactions).

### Q32 — C

**API ürününe göre kota** · Rehber 1.1 · Kaynak PT6-Q3

Günlük toplam kullanım Quota ile, müşteri ayrımı counter identifier ile kurulur. API product kotası ilgili ürün seviyesini temsil eder.

**Yakın alternatif neden elenir?** SpikeArrest kısa süreli ani yükü yumuşatır; günlük müşteri bazlı kullanım hakkının yerine geçmez.

**Belirleyici ifade:** “daily request allowances; separately for each client”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy).

### Q33 — B

**Workflow dallanması** · Rehber 1.1 · Kaynak PT4-Q59

Workflows değişken, sıra ve switch ile servis dönüşlerine göre akışı yönetir. Queue kendi başına iş akışı karar motoru değildir.

**Yakın alternatif neden elenir?** Callback yalnız gerçekten dışarıdan bir devam sinyali beklendiğinde gerekir; burada sonuç zaten HTTP response içinde.

**Belirleyici ifade:** “response determines; no external callback”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions).

### Q34 — B+D

**Test attestation akışı** · Rehber 2.2 · Kaynak PT6-Q14

Attestor doğrulanan imzayı tanımlar; pipeline başarılı test sonrası digest’e attestation üretir. Enforcing admission policy bunu deployment sırasında ister.

**Yakın alternatif neden elenir?** Tag test kanıtı değildir. Binary Authorization testleri kendiliğinden çalıştırmaz.

**Belirleyici ifade:** “exact container image; only after successful tests”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/binary-authorization/docs/attestations).

### Q35 — B

**Tekrarlanabilir messaging testi** · Rehber 2.3 · Kaynak PT2-Q18

Emulator ve kontrollü sentetik fixture yerel veri akışını tekrar üretir. Bu, gerçek IAM ve bütün hosted-service davranışlarının doğrulandığı anlamına gelmez.

**Yakın alternatif neden elenir?** Sadece başarılı mock hatalı mesaj parse/dedup davranışını ölçmez.

**Belirleyici ifade:** “reproduce malformed and duplicate-message cases”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/pubsub/docs/emulator).

### Q36 — B

**Yavaş başlangıç ve liveness** · Rehber 3.2 · Kaynak PT5-Q27

Startup probe başarılı olana kadar liveness/readiness çalıştırılmaz. Başlangıç penceresi ile sonradan deadlock tespit hızı ayrılır.

**Yakın alternatif neden elenir?** Readiness tek başına liveness’ın öldürmesini önlemez.

**Belirleyici ifade:** “without slowing steady-state deadlock detection”

[Ek resmî teknik kaynak](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

### Q37 — D

**Bucket create audit olayı** · Rehber 3.1 · Kaynak PT6-Q71

Bucket oluşturma yönetim API olayı Audit Logs filtrelemesiyle yönlendirilebilir. Object finalize ise dosya/nesne olayıdır; boş bucket oluşturma değildir.

**Yakın alternatif neden elenir?** Object-finalized trigger mevcut bucket’a yüklenen nesneyi temsil eder.

**Belirleyici ifade:** “bucket creation rather than uploads of objects”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/eventarc/standard/docs/run/cal).

### Q38 — D

**CPU ve heap profili** · Rehber 4.3 · Kaynak PT2-Q45

Profiler CPU/heap dağılımını code path düzeyinde gösterir; Trace servis/request süreleri için tamamlayıcıdır.

**Yakın alternatif neden elenir?** Dış HTTP span süreleri hangi iç fonksiyonun allocation yaptığını doğrudan vermez.

**Belirleyici ifade:** “functions and allocation paths; inside the ... application”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/profiler/docs/about-profiler).

### Q39 — D

**Dış servis gecikmesini izleme** · Rehber 4.3 · Kaynak PT5-Q46

Span hiyerarşisi ve süreler gecikmenin hangi çağrıda toplandığını gösterir. Dış sağlayıcı iç trace sağlamasa bile client span çağrı süresini ölçebilir.

**Yakın alternatif neden elenir?** CPU normal olması dış I/O latency’sini dışlamaz.

**Belirleyici ifade:** “which outgoing operation consumes the request time”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/trace/docs/overview).

### Q40 — C

**Namespace yetkisi** · Rehber 1.2 · Kaynak PT5-Q26

Namespace kapsamlı RBAC, Team B erişimini ilgili namespace kaynaklarına sınırlar. Namespace tek başına network/host güvenlik izolasyonu değildir; burada ölçülen kaynak değiştirme yetkisidir.

**Yakın alternatif neden elenir?** Project Editor gibi geniş izinleri namespace isimlendirmesi daraltmaz.

**Belirleyici ifade:** “must not change Team A; no project-wide administrative role”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

### Q41 — B

**API güvenliğinin katmanları** · Rehber 1.2 · Kaynak PT6-Q41

Apigee API kimlik/policy katmanı; Armor dış web saldırı korumasıdır. Korunan yolu bypass eden açık backend bırakılmamalı.

**Yakın alternatif neden elenir?** Cloud Armor WAF kontrolünü geçmek uygulama kullanıcısının OAuth ile doğrulandığı anlamına gelmez.

**Belirleyici ifade:** “OAuth token validation; common web exploits”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/architecture/best-practices-securing-applications-and-apis-using-apigee).

### Q42 — B

**AlloyDB için ağ ve kimlik ayrımı** · Rehber 1.2 · Kaynak PT6-Q15

Proje ayrılığı ağ ayrılığı olmak zorunda değildir. Shared VPC ortak özel ağı, IAM ise ayrı kaynak yetkilerini sağlar. AlloyDB için gereken private services access ayrıca yapılandırılır.

**Yakın alternatif neden elenir?** Auth Proxy güvenli kimlikli bağlantı sağlar; mevcut olmayan ağ rotasını oluşturmaz.

**Belirleyici ifade:** “separate project ownership; centrally managed network”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/alloydb/docs/configure-connectivity).

### Q43 — B

**Pub/Sub backlog ile HPA** · Rehber 3.2 · Kaynak PT1-Q15

External backlog metriği iş talebini doğrudan yansıtır. HPA replica sayısını, node autoscaler ise node kapasitesini yönetir.

**Yakın alternatif neden elenir?** CPU düşük kaldığı için yalnız CPU tabanlı sinyal bu I/O bekleyen iş yükündeki birikimi kaçırabilir.

**Belirleyici ifade:** “CPU usage stays low even when the backlog grows”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/autoscaling-metrics).

### Q44 — A

**Cloud Run kademeli rollout** · Rehber 3.1 · Kaynak PT6-Q2

Yeni revision önce no-traffic deploy edilir; native traffic split ile kontrollü canlı kullanıcı etkisi sağlanır. Rollback yolu korunur.

**Yakın alternatif neden elenir?** 100% dağıtıp sonra gözlemek gradual exposure şartını karşılamaz.

**Belirleyici ifade:** “small fraction of live traffic; native revision management”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration).

### Q45 — A

**Paylaşılan dosya sistemi** · Rehber 1.3 · Kaynak PT5-Q22

NFS ve ortak read/write gereksinimi yönetilen Filestore ile karşılanabilir. Performans, erişim ve uygun tier ayrıca seçilmelidir.

**Yakın alternatif neden elenir?** Object storage mount, NFS/POSIX davranışlarının tamamının yerine geçtiği varsayımıyla kullanılmamalı.

**Belirleyici ifade:** “existing service uses NFS; shared writable access”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver).

### Q46 — A

**Bigtable row key** · Rehber 1.3 · Kaynak PT5-Q41

Account prefix aynı hesabın zaman aralığını bitişik satırlara toplar. Global artan timestamp prefix tüm yazımları bir kenara yığabilir. Tek hesabın çok sıcak olması ayrıca tasarım gerektirir.

**Yakın alternatif neden elenir?** UUID dağıtımı iyileştirebilir ama sorudaki temel account-range sorgusunu kaybettirir.

**Belirleyici ifade:** “time interval for one account; many active accounts”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/bigtable/docs/schema-design).

### Q47 — C

**Paralel performans testi izolasyonu** · Rehber 2.3 · Kaynak PT4-Q7

Instance başına ayrılmış compute paralel run’ların Spanner kapasitesini paylaşmasını önler. Aynı konfigürasyon/veri ve warm-up gibi test kontrolleri yine gerekir.

**Yakın alternatif neden elenir?** Ayrı database veri izolasyonu sağlayabilir ama aynı instance compute kapasitesini paylaşır. Emulator performans eşdeğeri değildir.

**Belirleyici ifade:** “without ... competing for the same ... compute capacity”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/spanner/docs/emulator).

### Q48 — A

**Yerelde güvenli SQL bağlantısı** · Rehber 2.1 · Kaynak PT5-Q56

Auth Proxy güvenli bağlantı katmanını yönetir. Ağ yolu, IAM connectivity rolü ve database login/grant ayrı gerekliliklerdir; soru diğerlerini açıkça sağlar.

**Yakın alternatif neden elenir?** Admin REST API instance yönetir; SQL sorgu protokolünün yerine geçmez.

**Belirleyici ifade:** “reachability already exists; certificates”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy).

### Q49 — D

**StatefulSet kimliği** · Rehber 3.2 · Kaynak PT2-Q10

StatefulSet sabit ordinal kimlik ve replica başına PVC düzeni sağlar. Governing headless Service ağ kimliğini destekler.

**Yakın alternatif neden elenir?** ClusterIP Service tüm backend’ler için ortak adres sağlar; tek tek replica kimliğinin yerine geçmez.

**Belirleyici ifade:** “each replica; stable ordinal; its own persistent volume”

[Ek resmî teknik kaynak](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

### Q50 — B

**Cloud Shell GKE erişim teşhisi** · Rehber 2.1 · Kaynak PT5-Q39

Credential edinme ile Kubernetes endpoint’e paket ulaşması farklı katmanlar. Verilen bulgu authorized networks uyuşmazlığını doğrudan gösteriyor.

**Yakın alternatif neden elenir?** RBAC yetkisini büyütmek ağdan düşürülen bağlantıyı düzeltmez.

**Belirleyici ifade:** “public IP is outside those ranges”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).

## Seçim ve uyarlama notları

- 50 farklı kaynak soru seçildi; aynı kararı tekrar eden kaynak sorulardan yalnız biri alındı. 372 soruluk paketin eksiksiz doğruluk onayı değildir.
- Önceki setlerde de çalışılan mekanizmalar vardır. Bu set kaynak seçkisi/pekiştirmedir; yeni konu sayısı veya gecikmeli kalıcılık ölçümü iddiası yoktur. Soru geçmişinde bu ayrım korunur.
- PT4-Q52: haftalık rebuild'in otomatik güvenlik garantisi olduğu ifadesi çıkarıldı; merkezî image ve network kontrolü açıklaştırıldı.
- PT6-Q15: Shared VPC'ye izin verilen yeni deployment koşulu açıklandı; mevcut farklı ağların yalnız proxy kurarak bağlanacağı varsayımı kaldırıldı.
- PT6-Q17: Cloud Build Pub/Sub trigger'ın VPC Service Controls sınırı nedeniyle soru köküne perimeter kullanılmadığı koşulu eklendi.
- PT6-Q56: belirli compute-class adını ezberletmek yerine desteklenen Arm scheduling gereksinimi ölçülüyor.
- PT6-Q71: bucket create için Audit Logs event yolu açık; object-finalized olayıyla karıştırılmadı.
- PT6-Q18 PDB yalnız Eviction API kullanan voluntary drain bağlamında; rollout sorusu ayrı olarak maxSurge/maxUnavailable ile ölçülüyor.
- PT6-Q14, PT5-Q30 ve PT5-Q34 iki bağımsız gerekli ayarı ölçen çift seçimlere dönüştürüldü.
- Genel hizmet seçimini tek ipucuyla çözen bazı sorular yerine belirleyici koşulu olan örnekler tercih edildi; buna rağmen tempo için doğrudan karar soruları da var.
- Kaynak pakette güçlü Gemini sorusu yok; dış kaynaklı yeni soru eklenmedi. Eventarc ve Workflows var; Cloud Tasks doğru cevaplı bağımsız bir senaryo bu seçkide yok. Bu eksikler tamamlanmış konu olarak sayılmaz.
