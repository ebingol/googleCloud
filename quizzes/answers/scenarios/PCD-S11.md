# PCD-S11 — Türkçe cevap anahtarı

Çözümden sonra aç. 1 Ekim 2026. Her tam doğru küme 1 puan; çift seçimde kısmi puan yok. Hazırlık, kullanıcı başarısı veya kalıcılık kanıtı değildir.

## Kısa anahtar

1 A · 2 D · 3 D · 4 C · 5 C · 6 D+E · 7 A · 8 D · 9 C · 10 B · 11 B · 12 B · 13 A · 14 A · 15 B · 16 A · 17 C · 18 A · 19 A+B · 20 C · 21 D+E · 22 D · 23 D · 24 B · 25 A · 26 A · 27 C · 28 B · 29 D · 30 D · 31 B · 32 C · 33 A · 34 C · 35 D · 36 C · 37 A · 38 C · 39 C · 40 A · 41 C · 42 D · 43 D · 44 A · 45 C · 46 B · 47 A · 48 A · 49 B · 50 C

## Rehber haritası

[Güncel resmî exam guide](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) (1 Ekim kontrolü). Birincil atama sayımı aşağıdadır; bazı sorular ikincil olarak başka alanlara da dokunur. Alt başlık dağılımı hazırlayanın örneklemesidir.

| Madde | Sorular | Sayı |
|---|---|---:|
| 1.1 | 1, 5, 11, 28, 44, 48 | 6 |
| 1.2 | 13, 21, 31, 37, 41, 47 | 6 |
| 1.3 | 8, 17, 24, 33 | 4 |
| 2.1 | 2, 14, 26, 49 | 4 |
| 2.2 | 6, 18, 22, 34 | 4 |
| 2.3 | 10, 30, 38, 42 | 4 |
| 3.1 | 3, 12, 19, 27, 36, 43 | 6 |
| 3.2 | 7, 16, 23, 32, 39, 46 | 6 |
| 4.1 | 4, 9, 25, 50 | 4 |
| 4.2 | 15, 29, 40 | 3 |
| 4.3 | 20, 35, 45 | 3 |

Ölçülmeyen örnekler: AlloyDB ayrıntılı query tuning, Spanner şema/replication seçenekleri, IAP yapılandırması, Cloud Service Mesh mTLS, API Gateway OpenAPI ayrıntıları, tüm ML API yöntemleri ve sayısal ürün kotaları. Hazırlanmış 50 soru bunların öğrenildiğini veya rehberin eksiksiz ölçüldüğünü göstermez.

Kaynaklar aşağıda **Ek resmî web kaynağı** olarak etiketlidir; ders PDF sayfası iddiası yok. Uygulama tasarımı ve test metodolojisi gerekçeleri kaynak ürün davranışıyla birlikte hazırlayan çıkarımıdır.


## Q01 — A

**Rehber:** 1.1 · **Ölçülen karar:** Cache stampede

Per-key coordination aynı anahtar için toplu miss yükünü sınırlar; bounded lease/crash recovery kalıcı kilitlenmeyi önler. İzin verilen stale pencere boyunca eski açıklama sunulabilir. Bu bir uygulama tasarımıdır; Memorystore bunu kendiliğinden garanti etmez.

**Yakın yanlış:** B yalnız dalgayı erteler; aynı TTL ile eşzamanlı expiry/refresh devam eder.

**Belirleyici İngilizce:** “enough capacity for one refresh”

**Geçmiş ilişkisi:** Karma; S05-01 cache-aside üzerine eşzamanlı expiry ve refresher crash koşulu.

**Ek resmî web kaynağı:** [cache](https://docs.cloud.google.com/memorystore/docs/redis/general-best-practices).


## Q02 — D

**Rehber:** 2.1 · **Ölçülen karar:** Test endpoint isolation

Endpoint yönlendirmesi credential/proje seçimi değildir. Test process emulator host kullanır; hosted tanılama bu override olmadan gerçek staging endpointine gider.

**Yakın yanlış:** B testi bulut tanılaması yerine koyar; staging servisine erişimi ölçmez.

**Belirleyici İngilizce:** “requests reaching localhost”

**Geçmiş ilişkisi:** Karma; S04-06/S08-16 ters yön: emulator testi çalışır, hosted diagnostic yanlışlıkla emulator’a gider.

**Ek resmî web kaynağı:** [emulator](https://firebase.google.com/docs/emulator-suite/connect_firestore).


## Q03 — D

**Rehber:** 3.1 · **Ölçülen karar:** Connection budget during overlap

24×6+40=184≤200. Pool instance başınadır; overlap toplamı önemlidir. Bu verilen kapasite modeli gerçek Cloud Run instance üst sınırının kesin garantisi değildir; gerçek bağlantılar izlenir.

**Yakın yanlış:** B concurrency ile configured pool maximum aynı parametre değildir.

**Belirleyici İngilizce:** “twelve instances of the old revision and twelve of the new”

**Geçmiş ilişkisi:** Karma; S08-04 pool bütçesi; yeni iki revision overlap hesabı.

**Ek resmî web kaynağı:** [sql](https://docs.cloud.google.com/sql/docs/postgres/connect-run), [runscale](https://docs.cloud.google.com/run/docs/about-instance-autoscaling).


## Q04 — C

**Rehber:** 4.1 · **Ölçülen karar:** Consistent ranged download

Tek generation bütün range ve retry’larda aynı içerik sürümünü seçer. Eski sürüm erişilemezse karışık dosya üretmek yerine transfer kontrollü yeniden başlatılır.

**Yakın yanlış:** B her range için güncel sürüm seçerek tam olarak sürüm karışmasını sürdürür.

**Belirleyici İngilizce:** “must never silently combine versions”

**Geçmiş ilişkisi:** Karma; S03-05 generation-specific read; yeni çok parçalı transfer tutarlılığı.

**Ek resmî web kaynağı:** [gen](https://docs.cloud.google.com/storage/docs/request-preconditions).


## Q05 — C

**Rehber:** 1.1 · **Ölçülen karar:** Affinity and experiment assignment

Cross-device kalıcı grup üyeliği kullanıcı kimliğine bağlı application assignment gerektirir. Cloud Run affinity best effort instance yönlendirmesidir; deney kimliği garantisi sağlamaz.

**Yakın yanlış:** A affinity’nin garanti etmediği kalıcılığı ve cihazlar arası aynı grubu varsayar.

**Belirleyici İngilizce:** “across devices and across replacement”

**Geçmiş ilişkisi:** Karma; S08-05 durability değil kullanıcı bazlı deney üyeliği; affinity sınırı bilinçli tekrar.

**Ek resmî web kaynağı:** [affinity](https://docs.cloud.google.com/run/docs/configuring/session-affinity).


## Q06 — D+E

**Rehber:** 2.2 · **Ölçülen karar:** Build ordering and failure semantics

DAG bitiş sırasını, failure policy başarılı olma zorunluluğunu belirler. Hem iki check’i beklemek hem required failure’ı build failure yapmak gerekir. Diagnostic output tutulabilir.

**Yakın yanlış:** B bitmiş check ile başarılı check’i aynı sayar.

**Belirleyici İngilizce:** “correctly waits ... allowFailure: true”

**Geçmiş ilişkisi:** Karma; S04-02 doğru DAG varsayılır, S01-13 failure gate ile birleşir.

**Ek resmî web kaynağı:** [dag](https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order).


## Q07 — A

**Rehber:** 3.2 · **Ölçülen karar:** Surge capacity bottleneck

Zero-unavailable rollout yeni Pod için ek scheduling alanı gerektirir. Uygun node capacity ile eski dört available korunarak surge başlayabilir.

**Yakın yanlış:** B yer açar ama dört available şartını bozar.

**Belirleyici İngilizce:** “four available replicas throughout”

**Geçmiş ilişkisi:** Karma; S04-07 rollout ayarı doğru, S03-13 scheduler capacity birleşimi.

**Ek resmî web kaynağı:** [rollout](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).


## Q08 — D

**Rehber:** 1.3 · **Ölçülen karar:** Zonal HA with explicit regional limit

Cloud SQL regional HA zone arızası için synchronous standby/managed failover sunar; uygulama kesilen bağlantılardan toparlanır. Bölge kaybı ayrı DR kapsamıdır.

**Yakın yanlış:** A async lag nedeniyle aynı acknowledged-write korumasını garanti etmez.

**Belirleyici İngilizce:** “losing a zone ... separately accepted ... regional outage”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S04-05/S08-12 scope ayrımı, regional DR sorusunun ters gereksinimi.

**Ek resmî web kaynağı:** [ha](https://docs.cloud.google.com/sql/docs/postgres/high-availability).


## Q09 — C

**Rehber:** 4.1 · **Ölçülen karar:** Ordering-key blocked work

Başarısız event’in kontrollü disposition’ı çözülmelidir. Persist/quarantine ancak soruda onaylanan iş kuralıyla tamamlanmış disposition sayılır; sessiz veri atma değildir.

**Yakın yanlış:** D required customer ordering’i kaldırır.

**Belirleyici İngilizce:** “order within each customer”

**Geçmiş ilişkisi:** Yeni ölçüm; S10-04 lease değil ordering key’e bağlı failure ilerlemesi.

**Ek resmî web kaynağı:** [order](https://docs.cloud.google.com/pubsub/docs/ordering).


## Q10 — B

**Rehber:** 2.3 · **Ölçülen karar:** Property test detects implementation bug

Bağımsız business invariant implementation helper’ına bağlı değildir; real function hata yaptığında conservation/overdraft assertion yakalar. Random input tek başına oracle sağlamaz.

**Yakın yanlış:** A yalnız helper’ın kendiyle tutarlılığını ölçer.

**Belirleyici İngilizce:** “same helper used by the production function”

**Geçmiş ilişkisi:** Karma; S08-39 oracle üzerine helper kaynaklı circularity ve property/invariant uygulaması; yeni Google ürün bilgisi değil.

**Ek resmî web kaynağı:** [ai](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini).


## Q11 — B

**Rehber:** 1.1 · **Ölçülen karar:** Quota plus burst protection

Quota interval entitlement, SpikeArrest ani arrival rate kontrolüdür. İki gereksinim iki kontrol ister; partner scope ve hedef kapasite doğru ayarlanır.

**Yakın yanlış:** A contractual allowance’ları değiştirir; burst hızını bağımsız yönetmez.

**Belirleyici İngilizce:** “below that daily quota ... short burst”

**Geçmiş ilişkisi:** Karma; S04-09 ters durum: quota mevcut, burst koruması eksik.

**Ek resmî web kaynağı:** [quota](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy), [spike](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy).


## Q12 — B

**Rehber:** 3.1 · **Ölçülen karar:** Secret access at instance startup

Environment secret startup’ta runtime identity ile resolve edilir. Eski process’te yüklü değer yeni startup izninin kanıtı değildir. Secret scope grant yeterlidir.

**Yakın yanlış:** D geçici hayatta kalan instance’ları erişim onarımı yerine koyar.

**Belirleyici İngilizce:** “newly started instances fail ... permission failure”

**Geçmiş ilişkisi:** Karma; S09-09 principal teşhisi + S05-11 startup yaşam döngüsü; yeni startup failure bağlamı.

**Ek resmî web kaynağı:** [secret](https://docs.cloud.google.com/run/docs/configuring/services/secrets).


## Q13 — A

**Rehber:** 1.2 · **Ölçülen karar:** Credential rollout sequencing

Rollback hem Secret Manager version hem DB kabulüne bağımlıdır. Kontrollü overlap sonrası iki tarafta eski credential retire edilir; secret payload yeni version olarak eklenir.

**Yakın yanlış:** B eski revision’ın yeni instance startup’ını ve rollback’i kırar.

**Belirleyici İngilizce:** “rollback ... until the observation period ends”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S09-25 credential overlap, yeni temel kapsam/kalıcılık iddiası yok.

**Ek resmî web kaynağı:** [secret](https://docs.cloud.google.com/run/docs/configuring/services/secrets).


## Q14 — A

**Rehber:** 2.1 · **Ölçülen karar:** Workstations mounted home

Persistent /home mount image build time /home içeriğini örter. Image’de /opt gibi yerde template tutup startup’ta var olan user dosyalarını ezmeden initialize et.

**Yakın yanlış:** C user data koruma koşulunu bozar ve mounted-home modelini çözmez.

**Belirleyici İngilizce:** “attaches persistent home disks”

**Geçmiş ilişkisi:** Karma; S09-29 restart sorusu değil build-time home masking; ürün detayının yeni ölçümü.

**Ek resmî web kaynağı:** [workstation](https://docs.cloud.google.com/workstations/docs/customize-container-images).


## Q15 — B

**Rehber:** 4.2 · **Ölçülen karar:** Error classification before retry

400 invalid selector request düzeltmesi ister. Eligible transient 503 için bounded retry sürer; code sınıflandırması service-specific kurala dayanır.

**Yakın yanlış:** D geçici hataların recovery’sini de kaldırır.

**Belirleyici İngilizce:** “invalid field selector ... separate valid requests ... 503”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S08-40 temel sınıflama, somut two-error incident; yeni retry konu iddiası yok.

**Ek resmî web kaynağı:** [retry](https://docs.cloud.google.com/storage/docs/retry-strategy), [fields](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.ListObjectsOptions).


## Q16 — A

**Rehber:** 3.2 · **Ölçülen karar:** Probe semantics during dependency failure

Readiness traffic uygunluğu; liveness restart ile düzelecek process failure’dır. Shared dependency outage’ı process death saymak restart storm üretir.

**Yakın yanlış:** D startup probe başarılı olduktan sonraki outage’ları yönetmez.

**Belirleyici İngilizce:** “restarting ... does not accelerate recovery”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S02-12, DB failover kanıtı eklenmiş; yeni temel probe konusu değil.

**Ek resmî web kaynağı:** [probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).


## Q17 — C

**Rehber:** 1.3 · **Ölçülen karar:** Separate analytical scans

OLTP Cloud SQL’de kalır; daily export→Storage→BigQuery scan workload’unu ayırır. Partition seçimi query pattern ile yapılır; bütün BigQuery ingest streaming olmak zorunda değildir.

**Yakın yanlış:** A primary transaction contention’ı artırır; daily freshness zaten yeterlidir.

**Belirleyici İngilizce:** “Reports may be refreshed once a day”

**Geçmiş ilişkisi:** Karma; S08-49 storage analytics üzerine primary contention ve uygulama uyumu; eski temel ürün seçimi sayılmaz.

**Ek resmî web kaynağı:** [bq](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage).


## Q18 — A

**Rehber:** 2.2 · **Ölçülen karar:** Provenance is not a vulnerability waiver

Provenance origin kanıtıdır; vulnerability absence değildir. Patch yeni artifact üretir; evidence yeni digest ile yeniden eşleşir.

**Yakın yanlış:** B trusted builder ile güvenli dependency’yi karıştırır.

**Belirleyici İngilizce:** “requires ... no unresolved vulnerability”

**Geçmiş ilişkisi:** Karma; S09-17 evidence/digest doğru varsayılır, S06-18 vulnerability repair ile birleşir.

**Ek resmî web kaynağı:** [provenance](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance), [containers](https://docs.cloud.google.com/build/docs/building/build-containers).


## Q19 — A+B

**Rehber:** 3.1 · **Ölçülen karar:** Event delivery and runtime data identity

Delivery caller private Run’a invoke eder; handler runtime hesabıyla Storage okur. Runtime account delivery credential’ını miras almaz.

**Yakın yanlış:** D bucket rolünü yanlış principal’a verir; handler yine erişemez.

**Belirleyici İngilizce:** “before the handler runs ... service runs as processing-runtime”

**Geçmiş ilişkisi:** Karma; S01-06 invoker + S09-09 runtime resource identity; iki boundary doğrudan ölçülür.

**Ek resmî web kaynağı:** [event](https://docs.cloud.google.com/eventarc/docs/roles-permissions), [wif](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).


## Q20 — C

**Rehber:** 4.3 · **Ölçülen karar:** Async trace propagation

Context taşıma async sınırını bağlar; span parent/link seçimi iş modeline uyar. Queue wait event timestamp/metrics ile ayrıca analiz edilir.

**Yakın yanlış:** A bütün unrelated work’ü aynı trace’e toplayıp request correlation’ı bozar.

**Belirleyici İngilizce:** “no trace context ... message attributes”

**Geçmiş ilişkisi:** Karma; S04-12 propagation + S09-44 async wait, yeni messaging boundary.

**Ek resmî web kaynağı:** [trace](https://docs.cloud.google.com/trace/docs/trace-context).


## Q21 — D+E

**Rehber:** 1.2 · **Ölçülen karar:** NetworkPolicy DNS and backend access

DNS resolution ve DB bağlantısı farklı network akışlarıdır. Gerçek DNS deployment endpointine uygun UDP/TCP 53 ve selected DB 5432 izinleri birlikte gerekir; IAM packet allow değildir.

**Yakın yanlış:** A gerekli iki akıştan çok daha geniş erişim açar.

**Belirleyici İngilizce:** “Connecting ... IP succeeds ... blocked DNS queries”

**Geçmiş ilişkisi:** Karma; S03-10 ingress/egress üzerine DNS dependency; plugin/topology varsayımı açık.

**Ek resmî web kaynağı:** [network](https://kubernetes.io/docs/concepts/services-networking/network-policies/).


## Q22 — D

**Rehber:** 2.2 · **Ölçülen karar:** Dockerfile overrides expected buildpack flow

Source deploy root’ta Dockerfile varsa onu kullanır; yoksa supported buildpacks. Build selection runtime IAM/min instances ile belirlenmez.

**Yakın yanlış:** A image build ile application runtime kimliğini karıştırır.

**Belirleyici İngilizce:** “source root contains an old Dockerfile”

**Geçmiş ilişkisi:** Karma; S08-10 buildpack seçimi, beklenmedik Dockerfile önceliği yeni ölçüm.

**Ek resmî web kaynağı:** [source](https://docs.cloud.google.com/run/docs/deploying-source-code).


## Q23 — D

**Rehber:** 3.2 · **Ölçülen karar:** HPA cannot schedule nodes

HPA desired Pod oluşturmuş; eksik node capacity. Node pool maksimumu büyümeyi engelliyor. Cluster autoscaler/quota uygun capacity sağlayınca pending Pod yerleşir.

**Yakın yanlış:** B daha çok pending Pod ister; node sınırını kaldırmaz.

**Belirleyici İngilizce:** “node pool has reached its current maximum”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S08-13 node/Pod scaling; bu kez açık node maximum kanıtı; S10-12 ters bağlayıcı limit.

**Ek resmî web kaynağı:** [hpa](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).


## Q24 — B

**Rehber:** 1.3 · **Ölçülen karar:** Signed URL identity guarantee

Signed URL possession-based bearer erişimidir. Her download current entitlement gerektiriyorsa authenticated backend request başına authorization uygular, kendi kimliğiyle object okur/stream eder.

**Yakın yanlış:** C pencereyi kısaltır ama identity/forwarding şartını garanti etmez.

**Belirleyici İngilizce:** “every download ... anyone who merely receives a forwarded link”

**Geçmiş ilişkisi:** Karma; S01-04/S08-38 signed URL uygunluğu ters gereksinimle sınanır; yeni identity garantisi ayrımı.

**Ek resmî web kaynağı:** [signed](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).


## Q25 — A

**Rehber:** 4.1 · **Ölçülen karar:** Firestore read-dependent retry

Transaction conflict retry’da karar verisi yeniden transaction içinde okunur. Dış stale read transactional conflict kontrolüne dahil olmaz.

**Yakın yanlış:** D retry sayısı stale decision input’u doğrulamaz.

**Belirleyici İngilizce:** “reuses that value in every callback attempt”

**Geçmiş ilişkisi:** Karma; S01-09 transaction ve S04-16 retry; dış side-effect değil read placement ölçülür.

**Ek resmî web kaynağı:** [tx](https://firebase.google.com/docs/firestore/manage-data/transactions).


## Q26 — A

**Rehber:** 2.1 · **Ölçülen karar:** AI context versus tool permissions

Relevant repo/version context + supported API verification + local checks. Bu model önerisini doğru varsaymadan mevcut dependency contract’ına bağlar.

**Yakın yanlış:** B kullanıcı istediği pinned contract’ı değiştirerek hatayı gizler.

**Belirleyici İngilizce:** “respects the current dependency contract”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S05-10/S08-06 context mühendisliği; yeni AI ürün özelliği ölçümü değil.

**Ek resmî web kaynağı:** [ai](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini).


## Q27 — C

**Rehber:** 3.1 · **Ölçülen karar:** Rollback and pinned tagged endpoint

Tagged URL revision’a doğrudan gider; normal traffic percentage onu override etmez. Clients destination güncellenir; candidate investigation için korunabilir.

**Yakın yanlış:** D normal traffic split ile tagged endpoint’leri aynı sayar.

**Belirleyici İngilizce:** “directly to the tagged revision URL”

**Geçmiş ilişkisi:** Karma; S09-20 tag temelinden yeni rollback sonrası istemci hedefi teşhisi.

**Ek resmî web kaynağı:** [runroll](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration).


## Q28 — B

**Rehber:** 1.1 · **Ölçülen karar:** Fan-out plus controlled dispatch

Pub/Sub separate subscriptions fan-out/progress ayrımı; shipping adapter Tasks ile hedef HTTP dispatch rate/concurrency kontrolü kurar. Adapter/task effects idempotent olmalıdır.

**Yakın yanlış:** A tek subscription consumer’lar arasında load share eder; her takıma tüm event’i vermez.

**Belirleyici İngilizce:** “independently ... controlled ... concurrent requests”

**Geçmiş ilişkisi:** Karma; S04-04 fan-out + S01-05 Tasks dispatch; yeni ürün değil birleşik requirement.

**Ek resmî web kaynağı:** [queue](https://docs.cloud.google.com/tasks/docs/comp-pub-sub).


## Q29 — D

**Rehber:** 4.2 · **Ölçülen karar:** Partial response preserves continuation

Partial response fields içinde nextPageToken kaybolmamalı. Gerekli fields + token tüm sayfa traversal’ını korur.

**Yakın yanlış:** A page size veri sayısının veya completeness’in kanıtı değildir.

**Belirleyici İngilizce:** “accidentally omits nextPageToken”

**Geçmiş ilişkisi:** Karma; S08-29 fields/pagination üzerine continuation field kaybı; yeni teşhis koşulu.

**Ek resmî web kaynağı:** [fields](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.ListObjectsOptions).


## Q30 — D

**Rehber:** 2.3 · **Ölçülen karar:** Prove runtime IAM in integration test

Deployed runtime identity ile isolated staging integration gerçek IAM boundary’sini ölçer. Allowed staging database ve denied ayrı restricted project kontrol edilir; collection-level server IAM varsayılmaz.

**Yakın yanlış:** C gcloud project selection credential identity’yi değiştirmez.

**Belirleyici İngilizce:** “broad user ADC ... runtime service account”

**Geçmiş ilişkisi:** Karma; S08-16 emulator sınırı + S09-02 identity; yeni test execution evidence, Rules testi değil.

**Ek resmî web kaynağı:** [emulator](https://firebase.google.com/docs/emulator-suite/connect_firestore), [firestoreiam](https://docs.cloud.google.com/firestore/native/docs/security/iam).


## Q31 — B

**Rehber:** 1.2 · **Ölçülen karar:** Recover disabled KMS version

Decrypt eski ciphertext’in kullandığı key version’a bağlıdır. Disabled/not destroyed version tekrar enable edilince mevcut decrypt permission ile kurtarılır. Rotation eski ciphertext’i değiştirmez.

**Yakın yanlış:** D primary değişikliği ciphertext dependency’sini aktarmaz.

**Belirleyici İngilizce:** “disabled ... has not been destroyed”

**Geçmiş ilişkisi:** Karma; S09-45 backup retirement yerine gerçekleşmiş recoverable disable incident; aynı temel dependency açıkça korunur.

**Ek resmî web kaynağı:** [kms](https://docs.cloud.google.com/kms/docs/key-states).


## Q32 — C

**Rehber:** 3.2 · **Ölçülen karar:** Live ConfigMap file and process snapshot

Projection file update process’in parsed memory’sini kendiliğinden değiştirmez. No-replacement şartı application reload gerektirir; subPath update engeli de ekler.

**Yakın yanlış:** A env snapshot running process içinde otomatik yenilenmez.

**Belirleyici İngilizce:** “files ... update ... reads ... only once”

**Geçmiş ilişkisi:** Karma; S03-01 file projection koşulu zaten sağlanmış; yeni application cache katmanı.

**Ek resmî web kaynağı:** [config](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/).


## Q33 — A

**Rehber:** 1.3 · **Ölçülen karar:** Bigtable range locality

Dengeli device prefix yazmaları dağıtır, device+time range locality korur. Dominant device olmadığı açık olduğundan S09 hot-customer salting gerekmez.

**Yakın yanlış:** D dağıtır ama required range query locality’sini kaybeder.

**Belirleyici İngilizce:** “writes ... evenly across devices ... contiguous time interval”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S08-36 temel row key; S09-15 hot-device varsayımı açıkça yok, yeni kapsam değil.

**Ek resmî web kaynağı:** [bigtable](https://docs.cloud.google.com/bigtable/docs/schema-design).


## Q34 — C

**Rehber:** 2.2 · **Ölçülen karar:** Patch the final runtime stage

Affected final-stage package patch edilir. Builder update final runtime base layer’ını değiştirmez. Rebuild/scan/tests yeni digest üzerinde doğrulanır.

**Yakın yanlış:** A gereksiz toolchain ekler ve affected package resolution’ını güvenilir şekilde hedeflemez.

**Belirleyici İngilizce:** “from the final runtime base”

**Geçmiş ilişkisi:** Karma; S08-23 multi-stage + S06-18 patch, yeni yanlış stage onarımını ayırma.

**Ek resmî web kaynağı:** [containers](https://docs.cloud.google.com/build/docs/building/build-containers), [provenance](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance).


## Q35 — D

**Rehber:** 4.3 · **Ölçülen karar:** Report structured exception events

Severity tek başına exception report semantics değildir. Supported integration/structured error event stack ve service context sağlar; request ID correlation için ayrıca kalır.

**Yakın yanlış:** A tracing payload eksikliğini otomatik onarmaz.

**Belirleyici İngilizce:** “omits the exception stack ... structured error-event fields”

**Geçmiş ilişkisi:** Yeni ölçüm; S09-30 severity parse doğru varsayılır; Error Reporting event içeriği ölçülür.

**Ek resmî web kaynağı:** [error](https://docs.cloud.google.com/error-reporting/docs/formatting-error-messages).


## Q36 — C

**Rehber:** 3.1 · **Ölçülen karar:** Long-lived gRPC stream recovery

Cloud Run streaming HTTP request lifecycle/instance replacement kalıcı session garantisi değildir. Durable checkpoint + reconnect + command idempotency gerekir; timeout yalnız süre sınırını değiştirir.

**Yakın yanlış:** B connection replacement/deployment failure’larını çözmez.

**Belirleyici İngilizce:** “deployments can also replace instances ... resume”

**Geçmiş ilişkisi:** Karma; S10-11 streaming seçimi doğru, yeni lifecycle recovery ve durable session şartı.

**Ek resmî web kaynağı:** [grpc](https://docs.cloud.google.com/run/docs/triggering/grpc).


## Q37 — A

**Rehber:** 1.2 · **Ölçülen karar:** Direct GKE principal resource scope

Token acquisition authentication’dır, bucket read IAM authorization ayrı. Direct supported KSA principal grant target bucket scope’ta verilir; farklı project tek başına engel değildir.

**Yakın yanlış:** C project selection IAM grant değildir.

**Belirleyici İngilizce:** “token acquisition succeeds ... separate project”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S03-04/S08-15 direct WIF, cross-project scope ile mekanizma uygulanır; yeni temel konu değil.

**Ek resmî web kaynağı:** [wif](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).


## Q38 — C

**Rehber:** 2.3 · **Ölçülen karar:** Tenant authorization negative test

Valid identity account access izni değildir. Server endpoint cross-tenant negative test ownership authorization’ı ölçer; browser görünürlüğü security boundary değildir.

**Yakın yanlış:** B zaten doğru authentication’ı tekrar test eder; authorization gap’i ölçmez.

**Belirleyici İngilizce:** “authentication succeeds but account ownership is not enforced”

**Geçmiş ilişkisi:** Karma; S10-13 sonrası farklı karar: token verify doğru varsayılır, account authorization negative test. Anlık token-verification kopyası değil; kalıcılık sayılmaz.

**Ek resmî web kaynağı:** [verify](https://firebase.google.com/docs/auth/admin/verify-id-tokens), [iam](https://docs.cloud.google.com/iam/docs/overview).


## Q39 — C

**Rehber:** 3.2 · **Ölçülen karar:** Same tag does not update Pods

Pod template image digest değişimi new ReplicaSet/rollout üretir; registry tag movement existing process image’ını güncellemez. Exact digest artifact selection’ını sabitler.

**Yakın yanlış:** A Deployment registry tag update’ini controller template change saymaz.

**Belirleyici İngilizce:** “no change to the Deployment Pod template”

**Geçmiş ilişkisi:** Karma; S02-06 template rollout + S04-03 digest; new registry tag change teşhisi.

**Ek resmî web kaynağı:** [rollout](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).


## Q40 — A

**Rehber:** 4.2 · **Ölçülen karar:** Batch subrequest retry

Batch transport aggregation atomic transaction değildir. Individual status kontrolü ve conditional retries concurrent writes’ı korur; conflict request removal ile çözülmez.

**Yakın yanlış:** C outer status ile alt-operation outcome’larını karıştırır.

**Belirleyici İngilizce:** “multipart response ... individual transient failures”

**Geçmiş ilişkisi:** Karma; S07-04 metadata precondition + API batching; yeni subresponse outcome kararı.

**Ek resmî web kaynağı:** [batch](https://docs.cloud.google.com/storage/docs/batch), [gen](https://docs.cloud.google.com/storage/docs/request-preconditions).


## Q41 — C

**Rehber:** 1.2 · **Ölçülen karar:** Retention beats early lifecycle eligibility

Locked retention azaltılamaz/kaldırılamaz; lifecycle delete retention koşulu sağlanmadan silmez. Expiry sonrası da immediate deletion guarantee yok.

**Yakın yanlış:** A locked retention için geçerli bir temporary unlock yolu varsayar.

**Belirleyici İngilizce:** “locked ninety-day ... retention expiry ... later”

**Geçmiş ilişkisi:** Karma; S04-17 lock + S06-17 lifecycle; yeni conflicting eligibility hesabı, hold değil.

**Ek resmî web kaynağı:** [lock](https://docs.cloud.google.com/storage/docs/bucket-lock).


## Q42 — D

**Rehber:** 2.3 · **Ölçülen karar:** Load generation includes queueing

Open/controlled arrival workload production independent arrival’ı temsil eder; end-to-end queueing/failure dahil edilir. Bu test metodolojisi, Google ürün quota ezberi değildir.

**Yakın yanlış:** A slower revision’a daha az offered load vererek karşılaştırmayı çarpıtır.

**Belirleyici İngilizce:** “arrives independently of earlier completions”

**Geçmiş ilişkisi:** Yeni ölçüm; S09-33 cold/warm fairness yerine load-generator workload modelini ölçer.

**Ek resmî web kaynağı:** [slo](https://sre.google/workbook/alerting-on-slos/), [runscale](https://docs.cloud.google.com/run/docs/about-instance-autoscaling).


## Q43 — D

**Rehber:** 3.1 · **Ölçülen karar:** Source build identity denied

Failing principal build account’tur; runtime identity grant build’e aktarılmaz. Specific build secret access ve supported injection gerekir.

**Yakın yanlış:** C wrong principal ve aşırı scope; runtime henüz başlamamış.

**Belirleyici İngilizce:** “fails before producing ... configured Cloud Build service account”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S03-12/S04-18 build/runtime boundary, source deployment stage kanıtı.

**Ek resmî web kaynağı:** [source](https://docs.cloud.google.com/run/docs/deploying-source-code), [secret](https://docs.cloud.google.com/run/docs/configuring/services/secrets).


## Q44 — A

**Rehber:** 1.1 · **Ölçülen karar:** Regional dependency failure scope

Global frontend ve iki application region shared database region SPOF’ını kaldırmaz. Accepted nonzero RPO ile tested cross-region replica/promotion gibi DB DR gerekir; cache source of truth değil.

**Yakın yanlış:** C application layer kapasitesi database dependency’yi restore etmez.

**Belirleyici İngilizce:** “both regions depend on one Cloud SQL primary”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S08-12 regional DR + S05-05 cache durability; yeni temel scope değil.

**Ek resmî web kaynağı:** [regional](https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas), [cache](https://docs.cloud.google.com/memorystore/docs/redis/general-best-practices).


## Q45 — C

**Rehber:** 4.3 · **Ölçülen karar:** Error-budget burn rate

Allowed error fraction 0.1%; observed 0.2%; burn=0.2/0.1=2. Window tüm ay değildir; chosen alert windows/persistence urgency belirler.

**Yakın yanlış:** D kısa window’dan whole-period final result çıkarır.

**Belirleyici İngilizce:** “recent window ... rather than ... monthly final result”

**Geçmiş ilişkisi:** Karma; S10-20 doğru request denominator üzerine error-budget oranı; yeni hesap.

**Ek resmî web kaynağı:** [slo](https://sre.google/workbook/alerting-on-slos/).


## Q46 — B

**Rehber:** 3.2 · **Ölçülen karar:** Startup budget and deadlock detection

Startup probe initial window’yu ayırır; success sonrası normal liveness devreye girer. Readiness restart yapmaz.

**Yakın yanlış:** C init’i çözer ama required quick steady deadlock detection’ı zayıflatır.

**Belirleyici İngilizce:** “without weakening the steady-state liveness response”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S04-19/S08-07, farklı süreler; yeni temel probe kapsamı değil.

**Ek resmî web kaynağı:** [probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).


## Q47 — A

**Rehber:** 1.2 · **Ölçülen karar:** AI-selected resource is not authorization

Backend caller→resource authorization zorunludur; model schema formatting ve runtime DB capability end-user entitlement değildir. Reject unauthorized suggestion.

**Yakın yanlış:** D syntactic validity ile resource authorization’ı karıştırır.

**Belirleyici İngilizce:** “well-formed ... another customer’s account”

**Geçmiş ilişkisi:** Karma; S08-48 output validation + S10-13 identity, doğrulanmış kimlik varsayımıyla yeni model-resource sınırı.

**Ek resmî web kaynağı:** [schema](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output), [iam](https://docs.cloud.google.com/iam/docs/overview).


## Q48 — A

**Rehber:** 1.1 · **Ölçülen karar:** Warm capacity with finite budget

Minimum instances warm baseline sağlar; peak autoscaling sürer. Küçük min bütün peak için cold-start-free guarantee değildir; burst test explicit şarttır.

**Yakın yanlış:** C budget/baseline intent’i aşan peak reservation yapar.

**Belirleyici İngilizce:** “small warm baseline ... peak ... elastic”

**Geçmiş ilişkisi:** Bilinçli pekiştirme; S01-12 cold start, finite baseline budget ekli; tüm burst için guarantee yok.

**Ek resmî web kaynağı:** [runscale](https://docs.cloud.google.com/run/docs/about-instance-autoscaling).


## Q49 — B

**Rehber:** 2.1 · **Ölçülen karar:** Emulator success versus Storage service contract

Cloud Storage direct object write/list strong consistency contract’a sahiptir. Fake service contract’ı temsil etmelidir; arbitrary sleep false behavior’ı production’a taşır. Cache/IAM propagation farklı konulardır.

**Yakın yanlış:** C fake’in uydurduğu kuralı doğrulanmış ürün davranışı sayar.

**Belirleyici İngilizce:** “direct API object listing; no ... intermediary”

**Geçmiş ilişkisi:** Karma; S07-20 Storage consistency/cache + development fake fidelity; emulator ürün garantisi iddiası değil.

**Ek resmî web kaynağı:** [consistency](https://docs.cloud.google.com/storage/docs/consistency).


## Q50 — C

**Rehber:** 4.1 · **Ölçülen karar:** Unknown commit result

Commit ack kaybı rollback kanıtı değildir. Stable operation identity + uniqueness + transaction repeated effect’i sınırlar; matching existing result döndürülür, missing durumda aynı identity ile recovery.

**Yakın yanlış:** D unknown outcome’u definite failure sayarak duplicate riskini doğurur.

**Belirleyici İngilizce:** “cannot tell whether ... committed”

**Geçmiş ilişkisi:** Karma; S09-04 rollback doğrulanmış koşulunun tersi; S09-50 commit-before-ack uygulaması; yeni temel idempotency değil.

**Ek resmî web kaynağı:** [sql](https://docs.cloud.google.com/sql/docs/postgres/connect-run), [pg](https://www.postgresql.org/docs/current/tutorial-transactions.html), [constraints](https://www.postgresql.org/docs/current/ddl-constraints.html).
