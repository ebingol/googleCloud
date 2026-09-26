# PCD-S07 — Türkçe açıklamalı cevap anahtarı

**İlk denemeden sonra aç.** 26 Eylül 2026. Bu dosya hazırlayanın anahtarıdır; kullanıcı cevabı veya başarı kaydı değildir.

Her sorunun dayanağı aşağıdaki **ek resmî web kaynaklarıdır**; ders PDF'lerinde doğrulanmış sayfa varmış gibi gösterilmez. Senaryolar özgündür. Belgelenmiş mekanizmaların senaryoya uygulanmasından çıkan mimari öneriler ilgili açıklamalarda ayrıştırılmıştır.

## Hızlı anahtar

| Soru | Cevap | Soru | Cevap |
|---|---|---|---|
| 1 | C | 11 | A, E |
| 2 | A | 12 | A |
| 3 | D | 13 | D |
| 4 | B | 14 | B |
| 5 | A | 15 | C |
| 6 | B, D | 16 | A |
| 7 | C | 17 | B |
| 8 | D | 18 | D |
| 9 | B | 19 | A |
| 10 | C | 20 | C |

Her soru 1 puan; Q6 ve Q11 yalnız tam doğru kümeyle puanlanır. İlk cevaplar, süre ve yardım koşulları ayrı kaydedilir; açıklama sonrası düzeltmeler ilk sonucu değiştirmez.

## Rehber eşleştirmesi ve kapsam sınırı

26 Eylülde [resmî sertifika sayfası](https://cloud.google.com/learn/certification/cloud-developer) ve bağlı [exam guide PDF](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) kontrol edildi. Ana alan ağırlıkları yaklaşık %32/%23/%24/%21; bu sette %30/%25/%25/%20. Sorular birincil alanlarına bir kez sayılmıştır.

| Ana alan | Sorular | Adet |
|---|---|---|
| 1 — Tasarım/güvenlik/veri | 1, 5, 9, 13, 17, 20 | 6 |
| 2 — Geliştirme/test | 2, 6, 10, 14, 18 | 5 |
| 3 — Deployment | 3, 7, 11, 15, 19 | 5 |
| 4 — Entegrasyon/gözlemlenebilirlik | 4, 8, 12, 16 | 4 |

Alt madde örneklemi: 1.1 caching; 1.2 IAP/WIF; 1.3 replication/schema; 2.1 Workstations; 2.2 build/artifacts; 2.3 integration/AI-assisted tests; 3.1 source deployment/jobs; 3.2 HPA/probes/configuration; 4.1 storage/messaging; 4.2 partial responses; 4.3 profiling. Cloud Run jobs deployment, genel Cloud Run uygulama yapılandırması altında uygulama örneğidir; rehberde her ayarın adı tek tek geçmez.

Her alt madde yalnız bir yönüyle örneklenebilir. Gemini Cloud Assist, MCP, Apigee, API etkinleştirme, ML API tüketimi, Error Reporting yönetimi, provenance, Binary Authorization ve diğer ürün/ayarlar bu sette bağımsız olarak ölçülmedi. Bütün kapsam tamamlandı veya gerçek sınav dağılımı yakalandı iddiası yok.

12 yeni ölçüm + 7 karma + 1 gecikmeli uygulama. Q15, 22 Eylülde açıklanan probe ayrımını **opsiyonel dependency ve geçerli fallback** ile yeniden uygulatır; önceki sorunun sadece isim değişikliği değildir. S06'da yeni açıklanan yanlışlar aynı kararla hemen tekrar edilmedi. Ayrıntılı yakınlık kaydı QUESTION-LOG içindedir.

## 1 — C

**Ölçülen karar:** Cache stampede ve instance'lar arası per-key refresh koordinasyonu. **Rehber:** 1.1.

Darboğaz Redis kapasitesi değil, aynı miss için çok sayıda DB sorgusu. C her ürün için ortak refresh koordinasyonu sağlar; farklı ürünler birbirini beklemez. B yalnız process içini sınırlar. A TTL dolmasını önlemez; D freshness şartını bozar. Lease süreli olmalı; bırakma yalnız kendi sahiplik token'ıyla yapılmalı, bekleyenler cache'i yeniden okumalıdır. Failover/lease bitişi nedeniyle mutlak tek çalıştırma iddiası yok: soruda nadir mükerrer refresh kabul ediliyor. Bu bir cache performans tasarımı çıkarımıdır; finansal kilit doğruluğu garantisi değildir.

**Belirleyici koşul:** same entry across instances; freshness limit; duplicate refreshes during rare failures acceptable.

**Ek resmî kaynak:** [Redis lock sahipliği ve süre sınırları](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/) · [Memorystore best practices](https://docs.cloud.google.com/memorystore/docs/redis/general-best-practices).

## 2 — A

**Ölçülen karar:** Private integration-test endpoint'ine managed build erişimi. **Rehber:** 2.3.

Default worker'da private route yok; IAM izni bunu oluşturmaz. A private pool/VPC bağlantısı ve gereken firewall yoluyla ağ önkoşulunu sağlar, uygulama kimlik doğrulamasını korur. B IAM ile routing'i karıştırır. C DNS kaydıyla ulaşılabilirlik yaratmaz. D işlevsel bir başka mimari olabilir, ancak public endpoint yasağını ihlal eder. Soruda API doğrudan bağlı VPC'de: peering transitivity veya üçüncü ağ erişimi varsayılmıyor.

**Belirleyici koşul:** private address; timeout before API logs; managed workers; no public endpoint.

**Ek resmî kaynak:** [Cloud Build private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).

## 3 — D

**Ölçülen karar:** Source upload filtresi ile Docker build context filtresi ayrımı. **Rehber:** 3.1.

Dosya Docker'a ulaşmadan gcloud upload aşamasında eleniyor. Include satırından sonra gerekli dizin/içeriği geri alan dar istisnalar ve `gcloud meta list-files-for-upload` kontrolü doğru katmanı düzeltir. A upload'a alınmayan dosyayı geri getiremez. B runtime yetkisini build input eksikliğine uygular. C `.gitignore` varken otomatik oluşturulabilen ignore davranışını hesaba katmaz; güvenilir dar çözüm değildir. Git'e eklemek veya remote generation başka süreçlerde kullanılabilir, burada açıkça istenmiyor.

**Belirleyici koşul:** local Docker succeeds; .gcloudignore includes .gitignore; locally generated input must be uploaded.

**Ek resmî kaynak:** [gcloudignore](https://docs.cloud.google.com/sdk/gcloud/reference/topic/gcloudignore) · [gcloud run deploy source davranışı](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy).

## 4 — B

**Ölçülen karar:** Metadata için optimistic concurrency ve conflict sonrası merge. **Rehber:** 4.1.

Metageneration metadata sürümüdür. B eski sürüme dayanan update'i precondition failure ile engeller; güncel veriyi tekrar okuyup niyeti birleştirmek diğer yazarı korur. A metadata-only değişikliği content generation'dan anlayamaz. C yeni version numarasıyla eski map'i tekrar göndererek korumayı anlamsızlaştırır. D create-only anlamını mevcut metadata update'e yanlış uygular. Burada generation sabitliği açık varsayımdır; object replacement mümkünse generation koşulu da kullanılmalıdır.

**Belirleyici koşul:** generation remains fixed; read latest metadata, merge intended change.

**Ek resmî kaynak:** [Cloud Storage request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions).

## 5 — A

**Ölçülen karar:** IAP assertion doğrulaması ve audience sınırı. **Rehber:** 1.2.

Uygulama `x-goog-iap-jwt-assertion` içindeki imza ve claims'i doğrular; kimliği doğrulanmış payload'dan alır. B yalnız decode ederek sahteciliği önlemez. C başka backend için verilmiş token'ı kabul eder. D iki unsigned header'ın bulunmasını kriptografik doğrulama sanır. Geçerli kimlik application authorization'ın yerine geçmez. IAP audience biçimini Cloud Run servis çağrısındaki normal service URL audience kuralıyla karıştırma; soruda beklenen değer zaten verilmiş kabul ediliyor.

**Belirleyici koşul:** additional identity check if backend path bypasses IAP; unrelated protected backend.

**Ek resmî kaynak:** [IAP signed headers](https://docs.cloud.google.com/iap/docs/signed-headers-howto).

## 6 — B, D

**Ölçülen karar:** BuildKit secret injection ve uygulamanın secret'ı sızdırmaması. **Rehber:** 2.2; ikincil 1.2.

B secret'ı ilgili RUN'a geçici sunar; D komutun onu log veya çıktıya kopyalamasını önler. Secret mount, komutun kendi yaptığı kopyaları sihirli biçimde temizlemez. A sonraki layer'daki deletion'ın önceki layer içeriğini yok ettiğini sanır. C ENV/build metadata yoluyla kalıcılık riski yaratır. E token ömrünü azaltır ancak secret'ın artifact'a hiç girmemesi şartını karşılamaz. Secret Manager'dan güvenli alma zaten sağlanmıştır; ölçülen ikinci aşama Docker build'e güvenli aktarımdır.

**Belirleyici koşul:** exports intermediate build caches; must not embed credential; tool can consume temporary file.

**Ek resmî kaynak:** [Docker Build secrets](https://docs.docker.com/build/building/secrets/).

## 7 — C

**Ölçülen karar:** HPA downscale stabilization ve yönlere ayrı davranış. **Rehber:** 3.2.

Kısa demand düşüşleri downscale'i tetikliyor. C uygun bir geçmiş penceresindeki replica önerilerini dikkate alarak erken küçülmeyi sınırlar; uzun sakinlikte küçülmeye izin verir. A yanlış yönü yavaşlatır. B kalıcı peak kapasite maliyet şartını bozar. D talebe yetişebilecek maksimumu düşürür, downscale churn nedenini çözmez. Pencere, her scale olayından sonra sabit uyku veya kesin replica garantisi değildir; HPA recommendation geçmişini değerlendirir.

**Belirleyici koşul:** explicitly zero downscale stabilization; brief dips; prompt scale-up.

**Ek resmî kaynak:** [Kubernetes HPA behavior](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).

## 8 — D

**Ölçülen karar:** Partial response projeksiyonunda pagination kontrol alanını koruma. **Rehber:** 4.2.

`fields` yalnız object alanlarını seçerse response'taki `nextPageToken` da elenir. D gereken veriyle devam token'ını birlikte ister. A büyüklüğü sınırsız bir bucket'ı tek sayfaya sığdırma varsayımıdır. B opaque token'ı object name'den türetemez. C object listesini tamamen kaldırır; hangi nesnelere metadata isteği yapılacağı bile dönmez. Bu, S05'teki kısa page/end-of-results hatasından farklı olarak response projection'ın pagination'ı bozmasıdır.

**Belirleyici koşul:** existing token loop works without selector; retain smaller responses.

**Ek resmî kaynak:** [Storage ListObjectsOptions Fields açıklaması](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.ListObjectsOptions).

## 9 — B

**Ölçülen karar:** Read replica lag ile consistency-sensitive routing. **Rehber:** 1.3.

Commit primary'de tamamlanmış; replica aynı anda yetişmiş olmak zorunda değil. B confirmation'ı primary'ye, gecikme toleranslı işleri replica'ya gönderir. A replica üstündeki isolation'ı primary'den eksik veriyi getirmenin garantisi sanır. C ortalama gecikmeyi üst sınır yapar. D replica sayısıyla freshness garantisi oluşturmaz. Bu yönlendirme kararı, belgelenmiş replica gecikmesinin senaryoya uygulanmasıdır; replica'yı her okumada kullanma veya hiç kullanmama zorunluluğu yoktur.

**Belirleyici koşul:** immediate confirmation must reflect committed update; dashboards tolerate lag.

**Ek resmî kaynak:** [Cloud SQL replication](https://docs.cloud.google.com/sql/docs/postgres/replication) · [Replica lag troubleshooting](https://docs.cloud.google.com/sql/docs/postgres/replication/replication-lag).

## 10 — C

**Ölçülen karar:** Workstations mevcut resource kullanım yetkisi ve kapsamı. **Rehber:** 2.1.

User rolü atanmış workstation üzerinde kullanım içindir. Operation Viewer soruda zaten vardır. A Creator gereksiz oluşturma yetkisi verir; B yapılandırma dahil geniş yönetim sağlar; D policy yönetimidir ve özellikle istenmeyen erişim dağıtma yetkisini ekler. Roller birbirlerinin yerine yalnız ad benzerliğiyle seçilmez. Bu soru S05'teki ortam seçimi veya persistent home davranışını yeniden ölçmüyor.

**Belirleyici koşul:** assigned existing workstation only; no creation/configuration/access-policy changes.

**Ek resmî kaynak:** [Cloud Workstations IAM access control](https://docs.cloud.google.com/workstations/docs/access-control).

## 11 — A, E

**Ölçülen karar:** Job task partitioning ile retry-safe output birlikte. **Rehber:** 3.1; ikincil 4.1.

A, `CLOUD_RUN_TASK_INDEX` ve `CLOUD_RUN_TASK_COUNT` üzerinden sabit manifesti bölüştürür. E, başarılı write sonrası task başarısızlığı/retry penceresini güvenli kılar. B parallelism=5'i total tasks=20 yerine kullanır; parallelism aynı anda çalışabilecek task sınırıdır. C retry'ı kapatsa bile her task'ın tüm manifesti işlemesini çözmez. D retry başına farklı output üreterek duplicate'i tasarıma yerleştirir. Örnek partition `stableHash(recordId) mod taskCount == taskIndex`; random süreç hash'i değil deterministik fonksiyon gerekir. Conditional creation başarısızsa var olan output'un beklenen kayıt/çalışmaya ait olduğu doğrulanır.

**Belirleyici koşul:** twenty tasks, parallelism five; immutable manifest; retry after output write.

**Ek resmî kaynak:** [Cloud Run jobs task index/count](https://docs.cloud.google.com/run/docs/create-jobs) · [Conditional writes](https://docs.cloud.google.com/storage/docs/request-preconditions).

## 12 — A

**Ölçülen karar:** CPU tüketimini kodla ilişkilendirme için profiling. **Rehber:** 4.3.

Trace sorunu handler içine kadar daraltmış; artık hangi kod CPU harcıyor soruluyor. Profiler desteklenen Java/GKE yapılandırmasında sampled CPU call stack bilgisi sağlar. B aynı geniş span'ı daha çok örnekleyerek method CPU attribution üretmez. C exception olmayan CPU yoğunluğunu beklenen hata grubuna dönüştürmez. D kapasite artırarak etkiyi azaltabilir fakat hangi method sorusuna cevap vermez. Cloud Trace ve Profiler birbirini tamamlayabilir; biri bütün performans analizlerinin tek doğru aracı değildir.

**Belirleyici koşul:** sampled CPU consumption; traces already isolate handler; supported Java service.

**Ek resmî kaynak:** [Cloud Profiler overview ve desteklenen profiling türleri](https://docs.cloud.google.com/profiler/docs/about-profiler).

## 13 — D

**Ölçülen karar:** GKE WIF identity sameness ve project pool trust boundary. **Rehber:** 1.2.

Sorudaki grant name-based subject içindir; aynı project pool ve namespace/KSA adı cluster'lar arasında aynı IAM kimliği olabilir. D ayrı trust domain'leri ayrı proje/pool sınırına alır ve istenen principal grant'ini korur. A resource project'ini identity pool projesiyle karıştırır. B varsayılan pool'un her cluster için ayrı olduğunu sanır. C cluster adının bu subject'e dahil olduğunu varsayar. UID ile seçilen principal veya uygun cluster-specific condition alternatifleri vardır; soru bunları kullanan binding tanımlamıyor. D, bütün GKE kurulumlarında zorunlu ayrı proje iddiası değildir; daha az güvenilen cluster için seçilen güven sınırıdır.

**Belirleyici koşul:** same project pool; name-based subject; no cluster-specific condition; less-trusted administrators.

**Ek resmî kaynak:** [GKE WIF identity sameness](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#identity_sameness).

## 14 — B

**Ölçülen karar:** Artifact Registry virtual upstream priority ve client bypass. **Rehber:** 2.2.

Virtual repository tek erişim noktasıdır; private standard upstream daha yüksek priority ile seçilir. Client yalnız virtual endpoint'i kullanmalıdır. A pip için URL yazılış sırasını güvenilir repository önceliği sanır. C eşit öncelik ve direct public fallback ile hedefi bozar. D remote cache'i private package ownership/trust doğrulaması sanır. Bu düzen dependency confusion riskini azaltır; bütün dependency güvenliği veya her package sürümünün güvenilirliği garantisi değildir. Exact-version/hash kontrolleri ek önlemlerdir; sorudaki merkezi repository-selection ihtiyacını tek başlarına değiştirmezler.

**Belirleyici koşul:** prefer private upstream; one endpoint; client must not bypass policy.

**Ek resmî kaynak:** [Virtual repositories overview](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview).

## 15 — C

**Ölçülen karar:** Readiness'in gerçek hizmet sözleşmesine bağlanması. **Rehber:** 3.2. **Gecikmeli uygulama:** S02 Q12 ve 22 Eylül probe açıklaması.

Optional recommendations olmadan geçerli response verilebiliyor; bu outage bütün Pod'ları Service dışına atmamalı. C readiness'i gereken response'a, liveness'ı process sağlığına bağlar. A remote optional arızayı restart döngüsüne taşır. B required catalog kaybını da gizler. D optional/required ayrımını yapmadan her arızayı geciktirir. Readiness'te dependency kontrolü her koşulda yasak veya zorunlu değildir; belirleyici nokta Pod'un kabul edilen yanıtı verip verememesidir. Belgedeki probe etkilerinin bu sözleşmeye uygulanması mimari çıkarımdır.

**Belirleyici koşul:** successful fallback is accepted; required catalog; existing local liveness/startup correct.

**Ek resmî kaynak:** [Kubernetes probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/).

## 16 — A

**Ölçülen karar:** Pull subscriber outstanding message/byte flow control. **Rehber:** 4.1.

A subscriber'ın bitirmediği iş miktarını kapasiteye göre sınırlar; burst backlog'u hizmette kalır. B ack süresini uzatır ama sınırsız buffer'ı sınırlamaz. C iş tamamlanmadan ack ederek crash durumunda kayıp yaratır. D publisher batching ile subscriber memory sınırını karıştırır. Byte limiti gerçek process RSS'nin birebir limiti değildir; payload'ın açılmış hali, kütüphane ve worker ek yükü için pay bırakılır. Sürekli yetersiz throughput ayrı kapasite problemidir; burada kısa burst ve sonradan yetişme şartı var.

**Belirleyici koşul:** temporary backlog acceptable; bounded workers; unbounded received payloads.

**Ek resmî kaynak:** [Pub/Sub subscriber flow control](https://docs.cloud.google.com/pubsub/docs/flow-control).

## 17 — B

**Ölçülen karar:** Timestamp-leading secondary index hotspot ve sharded read tradeoff. **Rehber:** 1.3.

Base table'ın dağınık anahtarı ayrı index'in timestamp hotspot'unu düzeltmez. B index başına dengeli shard ekler; zaman aralığı her shard'da okunup global sıralama birleştirilir. A timestamp'i başta bırakarak sorunu korur. C hotspot'u diğer uca taşır. D doğru çalışan base table'a müdahale eder. Eski problemli index'i write yolunda tutup yalnız yenisini eklemek darboğazı koruyabileceği için seçenek replace diyor. Daha fazla read fan-out maliyeti soruda kabul edilmiştir; her iş yükü için ücretsiz çözüm değildir.

**Belirleyici koşul:** index is bottleneck; balanced base keys; bounded parallel scans and merge accepted.

**Ek resmî kaynak:** [Spanner timestamp sharding](https://cloud.google.com/blog/products/gcp/sharding-of-timestamp-ordered-data-in-cloud-spanner) · [Schema optimization](https://docs.cloud.google.com/spanner/docs/whitepapers/optimizing-schema-design).

## 18 — D

**Ölçülen karar:** AI-generated asynchronous test'in missing-assertion yolunu kapatma. **Rehber:** 2.3.

D, gerçek fonksiyonun reddedilmesini ve beklenen hatayı assertion yapar; resolve olursa test başarısız olur. A başarılı Promise'i bekleyerek reject'e çeviremez. B ölçülen gerçek davranışı mock'la değiştirir. C async sözcüğünü rejection şartı sanır. Alternatif doğru çözüm `expect.assertions(...)` ile catch assertion'ının çalıştığını garanti etmek veya success yolunu açıkça fail etmektir; şıklarda bunlar yok. Burada yalnız await eksikliği yok: mevcut try içinde await var, resolve yolunda assertion yok. Gemini'nin test üretmesi bu mantık kontrolünü ortadan kaldırmaz.

**Belirleyici koşul:** broken implementation resolves; assertion only inside catch; real function must remain under test.

**Ek resmî kaynak:** [Jest asynchronous tests, rejects ve assertion count](https://jestjs.io/docs/asynchronous).

## 19 — A

**Ölçülen karar:** Startup environment snapshot ve rollback edilebilir configuration referansı. **Rehber:** 3.2.

A yeni ConfigMap adını Pod template'e bağlar; rollout yeni process environment'ını oluşturur. Eski ConfigMap saklanıp değiştirilmezse önceki template referansına dönüş eski ayarı da getirir. B çalışan environment'ın canlı güncellendiğini sanır. C uygulama mounted file okumadığından işe yaramaz. D aynı mutable ConfigMap'in içeriğini Deployment geçmişinin geri getirdiğini varsayar. Image digest aynı kalabilir: config değişimi için zorunlu rebuild yok. S03 Q1'deki restart'sız projected file şartının aksine bu uygulama yalnız startup environment okuyor ve rollout kabul ediyor.

**Belirleyici koşul:** envFrom; startup-only reads; old/new maps retained; same tested image digest.

**Ek resmî kaynak:** [Kubernetes ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/) · [Deployment rollback](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment).

## 20 — C

**Ölçülen karar:** Storage strong consistency ile HTTP cache freshness ayrımı. **Rehber:** 1.1; ikincil 1.3.

Doğrudan güncel object okuması yeni bytes'ı görüyor; eski yanıt cache yolunda. C yeni URL'ye yeni bundle koyar, fresh HTML onu ister; immutable asset caching korunur. A problemi Storage eventual replication diye yanlış teşhis eder. B metadata değişiminin daha önce cache'lenmiş kopyaları anında değiştirdiğini varsayar. D Object Versioning'i cache invalidation/URL selection yerine koyar. HTML/manifest'in de fresh olması ve yeni asset'in referanstan önce yayımlanması gerekir; HTML freshness soruda verilmiştir. Açık eski sayfalardaki kodu zorla değiştirme garantisi yoktur.

**Belirleyici koşul:** direct authenticated read is new; cached path is old; fresh HTML can reference different filenames.

**Ek resmî kaynak:** [Storage consistency and cache control](https://docs.cloud.google.com/storage/docs/consistency) · [Cloud CDN invalidation](https://docs.cloud.google.com/cdn/docs/cache-invalidation-overview). Versioned URL seçimi bu mekanizmaların senaryoya uygulanmasıdır.

---

[Sorular](../../scenarios/PCD-S07.md) · [Senaryo dizini](../../scenarios/README.md)
