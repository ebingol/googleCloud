# PCD-S12 — 50 soru, seçenekler ve açıklamalı cevaplar

8 Ekim 2026. Udemy seçkisinin mevcut S12 uyarlamaları. **Anahtarlı tekrar içindir.** İlk sonuç **44/50 (%88), 72 dakika** korunur. Q24/Q27/Q34 çift seçimdir.

## Soru 01

A Cloud Build pipeline requires an internal compiler that is absent from the standard builders. Several repositories need the same compiler version, and the team wants reproducible builds without installing it from an external site during every build. Which implementation should you use?

**Select ONE answer.**

**A.** Install the compiler on a developer laptop and assume Cloud Build can execute its local binary.

**B.** Move every repository to a permanently managed Jenkins VM solely to obtain this compiler.

**C.** Put the compiler name in the Cloud Build substitutions and rely on automatic tool installation.

**D.** Package the compiler in a versioned custom builder image and reference that image in the build steps.

**Doğru cevap: D**

**Özel build aracı** · Rehber 2.2 · Kaynak PT2-Q4

Build step bir container image kullanır; custom builder araç ve sürümü yeniden kullanılabilir biçimde kapsar.

**Yakın alternatif neden elenir?** Jenkins çalışabilir ama sorudaki ihtiyacı karşılamak için yönetilen build sisteminden taşınmak gereksizdir.

**Belirleyici ifade:** “same compiler version; reproducible builds”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/build/docs/configuring-builds/use-community-and-custom-builders).

---

## Soru 02

A container passes testing in staging. The release process must promote the identical bytes to production, even if another build later reuses the same human-readable tag. Which image reference should the deployment record retain to identify the tested artifact unambiguously?

**Select ONE answer.**

**A.** A reusable environment tag such as staging.

**B.** Only the image repository name, without a tag or digest.

**C.** The image digest.

**D.** The latest tag.

**Doğru cevap: C**

**Aynı artifact promotion** · Rehber 2.2 · Kaynak PT5-Q9

Digest içeriğe bağlı kimliktir. Mutable tag başka içeriğe taşınabilir; production deployment test edilen digest’i kullanmalıdır.

**Yakın alternatif neden elenir?** Semantic/environment tag ancak ayrıca immutable tutulursa güvenlidir; soru tag reuse olabildiğini açıkça söylüyor.

**Belirleyici ifade:** “identical bytes; reuses the same tag”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/artifact-registry/docs/docker/names).

---

## Soru 03

A read-heavy application uses a replicated Bigtable instance with clusters in two regions. It currently routes requests to one cluster and requires an operator to change routing during outages. The application accepts eventual consistency and does not require single-row transactions. Which app-profile change enables managed routing to an available cluster?

**Select ONE answer.**

**A.** Add a Dataflow export job and continue sending online reads to the same failed cluster.

**B.** Increase the client connection pool but keep single-cluster routing.

**C.** Keep single-cluster routing and add more nodes only to the currently selected cluster.

**D.** Use a multi-cluster routing app profile with both clusters eligible.

**Doğru cevap: D**

**Bigtable failover** · Rehber 1.3 · Kaynak PT6-Q11

Multi-cluster routing uygun replicated cluster’lar arasında failover sağlar. Eventual consistency ve single-row transaction kısıtları açıkça kabul edildi.

**Yakın alternatif neden elenir?** Connection pool ağ/hedef cluster kullanılabilirliği problemini çözmez.

**Belirleyici ifade:** “accepts eventual consistency; operator to change routing”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/bigtable/docs/routing).

---

## Soru 04

Your organization already produces signed test attestations for approved image digests. A Cloud Run service must reject ordinary deployments that lack this approval, including deployments submitted outside the usual CI pipeline. Which control should enforce this requirement at deployment time?

**Select ONE answer.**

**A.** Add a test step to the usual pipeline but allow every other deployment path without admission checks.

**B.** Use only an Artifact Registry retention policy to control which images can be deployed.

**C.** Enable an enforcing Binary Authorization policy requiring the trusted attestation for the service.

**D.** Require the image tag to contain the word approved, without verifying signed evidence.

**Doğru cevap: C**

**Cloud Run admission politikası** · Rehber 3.1 · Kaynak PT5-Q48

CI dışındaki deployment yolunu da kontrol etmek için deployment admission policy gerekir. İlgili güvenilir attestation istenir; yetkili breakglass ayrı denetimli istisnadır.

**Yakın alternatif neden elenir?** Yalnız pipeline test gate’i başka deploy yollarını engellemez.

**Belirleyici ifade:** “including deployments ... outside the usual CI pipeline”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/run/docs/securing/binary-authorization).

---

## Soru 05

Developers use different laptops and IDEs, but their builds require approved tools and private access to services inside the company VPC. Security wants centrally maintained development environments with controlled network access and reproducible tool versions. Which approach provides an appropriate managed foundation?

**Select ONE answer.**

**A.** Install Cloud Code on every laptop and assume the extension creates private connectivity and a common OS toolchain.

**B.** Give each developer Cloud Shell and assume its default network is the company VPC.

**C.** Give developers unrestricted custom VM images and depend on verbal instructions to keep the tools identical.

**D.** Use Cloud Workstations in the approved network with centrally maintained custom images and the required perimeter configuration.

**Doğru cevap: D**

**Kurumsal geliştirme ortamı** · Rehber 2.1 · Kaynak PT4-Q52

Workstations yönetilen geliştirme ortamı, custom image ise standart toolchain sağlar. Ağ ve perimeter ayrıca doğru kurulmalıdır; haftalık image rebuild tüm güvenliği garanti etmez.

**Yakın alternatif neden elenir?** Cloud Code bir IDE aracı; kendi başına ortak runtime ağı veya merkezi OS imajı oluşturmaz.

**Belirleyici ifade:** “centrally maintained; private access; reproducible tool versions”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/workstations/docs/customize-container-images).

---

## Soru 06

The first step of a Cloud Build job produces a manifest. A later step in the same build must read it, and the dependency order is already correct. The first step currently writes into its container's temporary directory. Which change shares the manifest without introducing a storage service?

**Select ONE answer.**

**A.** Bake it into the first step image after that container has already started.

**B.** Store its path in a substitution and expect the file contents to be transferred automatically.

**C.** Write the manifest under /workspace and have the dependent step read that path.

**D.** Keep it in the first step container and only increase the later step timeout.

**Doğru cevap: C**

**Build step dosya paylaşımı** · Rehber 2.2 · Kaynak PT5-Q15

/workspace build adımları arasında paylaşılan alandır; her container’ın özel geçici dosya sistemi aynı paylaşımı sağlamaz.

**Yakın alternatif neden elenir?** Path bilgisini iletmek dosyanın kendisini paylaşmaz.

**Belirleyici ifade:** “same build; dependency order is already correct”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/build/docs/configuring-builds/pass-data-between-steps).

---

## Soru 07

An Autopilot cluster has no existing Arm nodes. You are deploying an arm64-compatible image and want GKE to provision appropriate capacity from the workload requirements. The cluster version and region support Arm. Which manifest choice explicitly requests the CPU architecture without managing node pools yourself?

**Select ONE answer.**

**A.** Switch to a Standard cluster solely to create an Arm node pool manually.

**B.** Set an appropriate nodeSelector including kubernetes.io/arch: arm64.

**C.** Add only an Arm-related toleration and rely on it to require Arm nodes.

**D.** Label the Pod metadata with kubernetes.io/arch: arm64 without a scheduling selector.

**Doğru cevap: B**

**Autopilot Arm yerleşimi** · Rehber 3.2 · Kaynak PT6-Q56

nodeSelector scheduling zorunluluğunu ifade eder. Desteklenen Autopilot konfigürasyonunda GKE uygun kapasite oluşturur; yalnız toleration bir node’u zorunlu kılmaz.

**Yakın alternatif neden elenir?** Toleration belirli taint’e izin verir; başka uygun node’a yerleşmeyi engellemez.

**Belirleyici ifade:** “provision ... from workload requirements”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke).

---

## Soru 08

A chat product uses Firestore. A room can accumulate an unbounded message history, but clients fetch messages in pages and create messages independently. You want to avoid rewriting a large room document whenever a message arrives. Which document model is the best fit?

**Select ONE answer.**

**A.** Store room metadata in a document and each message in a document within its messages subcollection.

**B.** Store every message in one array field on the room document.

**C.** Store only the latest message in the room document and use document versions as the application history.

**D.** Create one project-wide document containing a map of every room and all its messages.

**Doğru cevap: A**

**Firestore büyüyen mesaj geçmişi** · Rehber 1.3 · Kaynak PT5-Q44

Alt collection mesajları bağımsız yazım ve sorgulanabilir sayfalama birimlerine ayırır; büyüyen tek document sınırına yaslanmaz.

**Yakın alternatif neden elenir?** Tek array her mesajda aynı büyüyen belgeyi değiştirmeyi gerektirir.

**Belirleyici ifade:** “unbounded message history; independently”

[Ek resmî teknik kaynak](https://firebase.google.com/docs/firestore/data-model).

---

## Soru 09

A Workflow must start a Cloud Run job, wait for its execution to complete, and then continue with a reporting step. The job is a batch workload with no application HTTP server. Which integration should the Workflow use?

**Select ONE answer.**

**A.** Call the Cloud Run services invoke endpoint using the job name as a service name.

**B.** Create a Pub/Sub subscription on the job and expect the job itself to listen continuously.

**C.** Use the Cloud Run Admin API connector to run the job and handle its long-running operation.

**D.** Send an HTTP request to an assumed public application URL on the job.

**Doğru cevap: C**

**Workflows Cloud Run job çağrısı** · Rehber 3.1 · Kaynak PT6-Q59

Job bir HTTP service değildir; Admin API jobs.run üzerinden execution başlatılır. Workflows connector long-running operation davranışını yönetir.

**Yakın alternatif neden elenir?** Job container’ının web server açması gerekmez; varsayılan request endpoint’i yoktur.

**Belirleyici ifade:** “wait ... complete; no application HTTP server”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/workflows/docs/tutorials/execute-cloud-run-jobs).

---

## Soru 10

The same workload runs in three GKE clusters in one project. Container stdout is already collected in Cloud Logging. During an incident, you need one query covering the relevant workload across all three clusters. Which approach avoids manually changing kubectl contexts and inspecting replicas individually?

**Select ONE answer.**

**A.** Use the Cloud Trace span list as a complete replacement for container stdout logs.

**B.** Run kubectl logs in one current context and assume it automatically queries the other clusters.

**C.** Query Cloud Logging, for example with gcloud logging read, using container resource and workload-label filters across the clusters.

**D.** Use journalctl on a single worker node and assume it contains all cluster logs.

**Doğru cevap: C**

**Clusterlar arası log sorgusu** · Rehber 4.3 · Kaynak PT5-Q5

Merkezî logging cluster sınırları arasında aynı query ile filtrelemeyi sağlar. resource.type=k8s_container ve workload/project filtreleri gereksiz kayıtları daraltır.

**Yakın alternatif neden elenir?** kubectl current context tek cluster hedefler; diğer cluster loglarını otomatik toplamaz.

**Belirleyici ifade:** “already collected in Cloud Logging; across all three clusters”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs).

---

## Soru 11

Terraform Cloud currently runs your infrastructure plans and applies. Security prohibits storing long-lived Google service account keys in external systems. The team wants to keep its existing Terraform Cloud execution environment and obtain temporary Google Cloud credentials for each run. Which authentication approach best fits?

**Select ONE answer.**

**A.** Store a service account key in Terraform Cloud and rotate the key every month.

**B.** Create a Google Workspace user for the pipeline and store its password as a sensitive variable.

**C.** Configure Workload Identity Federation for Terraform Cloud and scope access to the required resources.

**D.** Move Terraform execution to GKE and use a Kubernetes service account.

**Doğru cevap: C**

**Terraform Cloud kimliği** · Rehber 1.2 · Kaynak PT6-Q21

Dış iş yükü kimliği WIF ile kısa ömürlü Google kimliğine çevrilir. Mevcut execution ortamını korur ve kalıcı anahtar gerektirmez.

**Yakın alternatif neden elenir?** GKE üzerinde workload identity mümkün olsa da execution ortamını taşıma şartı gereksizdir.

**Belirleyici ifade:** “keep its existing Terraform Cloud execution environment”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines).

---

## Soru 12

You have a small Python HTTP service in a local source directory and need to test it behind an existing Apigee proxy. The language is supported by buildpacks, no Dockerfile is present, and cloud build permissions are ready. Which deployment path minimizes local container-tool setup?

**Select ONE answer.**

**A.** Deploy from the source directory with gcloud run deploy --source, then test the deployed service through Apigee.

**B.** Point the production Apigee proxy at localhost on the developer laptop without configuring reachability.

**C.** Install a local Docker daemon, build and push an image manually, then deploy it.

**D.** Run only local unit tests and treat them as proof that the hosted Apigee route works.

**Doğru cevap: A**

**Source deploy ile entegrasyon** · Rehber 3.1 · Kaynak PT6-Q57

Source deploy buildpacks/Cloud Build yolunu kullanarak local Docker kurma ihtiyacını azaltır. Hosted proxy entegrasyonu ayrıca gerçek route üzerinden sınanır.

**Yakın alternatif neden elenir?** Local unit test Apigee ağ/kimlik/routing entegrasyonunun kanıtı değildir.

**Belirleyici ifade:** “no Dockerfile; minimizes local container-tool setup”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/run/docs/deploying-source-code).

---

## Soru 13

A staging Cloud SQL instance has only a private IP. A developer has no VPN route from the laptop but is authorized to use IAP TCP forwarding. A small VM can be placed on the database's reachable VPC. Which arrangement allows secure development access without assigning a public IP to the VM or database?

**Select ONE answer.**

**A.** Run Cloud SQL Auth Proxy on the VPC VM and reach its appropriately restricted listener through an IAP TCP tunnel.

**B.** Add the laptop public IP to authorized networks and keep all routing unchanged.

**C.** Run Cloud SQL Auth Proxy only on the laptop and assume it creates a private network route.

**D.** Grant the developer Project Owner and connect directly to the private IP over the internet.

**Doğru cevap: A**

**Private SQL yerel erişim** · Rehber 4.1 · Kaynak PT6-Q50

Proxy’nin çalıştığı VM private SQL’e ulaşır; IAP geliştiriciden bu VM’ye kontrollü tünel sağlar. Listener/firewall/IAM en dar kapsamda ayarlanır.

**Yakın alternatif neden elenir?** Laptop üzerindeki Auth Proxy ağ erişimi yokluğunu çözmez.

**Belirleyici ifade:** “no VPN route; only a private IP”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/sql/docs/postgres/connect-to-instance-from-outside-vpc).

---

## Soru 14

A stateless GKE service has ten replicas. During voluntary node drains that use the Kubernetes Eviction API, at least eight replicas must remain available. You are configuring disruption protection rather than changing an application rollout strategy. Which setting expresses this requirement?

**Select ONE answer.**

**A.** A HorizontalPodAutoscaler with minReplicas: 8, without a disruption budget.

**B.** A Deployment with maxSurge: 8, without a disruption budget.

**C.** A PodDisruptionBudget with maxUnavailable: 8.

**D.** A PodDisruptionBudget with minAvailable: 8 and a selector matching the workload.

**Doğru cevap: D**

**Drain sırasında PDB** · Rehber 3.2 · Kaynak PT6-Q18

PDB minAvailable=8 ilgili eviction işlemlerine kullanılabilir kopya sınırı koyar. Involuntary failure veya bütçeyi bypass eden silme için mutlak koruma değildir.

**Yakın alternatif neden elenir?** HPA kopya hedefini belirler; drain eviction kabul kontrolünün yerine geçmez.

**Belirleyici ifade:** “voluntary node drains; Eviction API; at least eight”

[Ek resmî teknik kaynak](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/).

---

## Soru 15

A market-data API reads from an existing authoritative database. Most requests repeatedly access a small subset of records, and those responses may be a few seconds old. You need to reduce database load without moving the full dataset or making cache eviction cause permanent data loss. Which design should you choose?

**Select ONE answer.**

**A.** Move the entire database into Redis and delete the original records after loading them.

**B.** Place each API read in a Pub/Sub queue and wait for a subscriber to answer.

**C.** Create a BigQuery copy and run an analytical query for every incoming API request.

**D.** Cache frequently requested records in Memorystore; read the database on a cache miss and populate the cache.

**Doğru cevap: D**

**Hot data cache ve kaynak veri** · Rehber 1.1 · Kaynak PT6-Q24

Hot subset + kısa staleness toleransı cache-aside için uygundur. Kalıcı doğruluk kaynağı veritabanı olarak kalır.

**Yakın alternatif neden elenir?** Tüm veriyi Redis tek kopya yapmak eviction halinde kalıcı veri kaybını önleme şartını sağlamaz.

**Belirleyici ifade:** “small subset; without moving the full dataset”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview).

---

## Soru 16

Images uploaded to a bucket must be checked with the Vision API and then passed through several processing services. More steps will be added later. You want a managed event-driven entry point and a central definition of the processing sequence, without adding orchestration logic to every worker. Which design best fits?

**Select ONE answer.**

**A.** Route object-finalized events through Eventarc to Workflows, and orchestrate the processing services there.

**B.** Schedule a periodic bucket listing and put all sequencing logic into each image-processing worker.

**C.** Send the event independently to every worker and assume delivery order enforces the processing sequence.

**D.** Use a Cloud Tasks queue as the sole state machine for the entire multi-step process.

**Doğru cevap: A**

**Storage olayından çok adımlı işlem** · Rehber 1.1 · Kaynak PT6-Q34

Eventarc olay yönlendirmeyi, Workflows sıra ve durum yönetimini yapar. Worker servisler görevlerine odaklanır. Olay tekrarı için işleme idempotent tasarlanmalıdır.

**Yakın alternatif neden elenir?** Bağımsız abonelere dağıtım bir işlem sırası ve sonuç bağımlılığı kurmaz.

**Belirleyici ifade:** “central definition of the processing sequence”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-storage).

---

## Soru 17

Your policy requires a verification build whenever an image is uploaded to Artifact Registry, including approved uploads made directly from developer machines. The project is not using VPC Service Controls. You want an event-driven solution with no polling and no custom relay service. What should trigger verification?

**Select ONE answer.**

**A.** A Cloud Scheduler job that periodically compares image lists.

**B.** Artifact Registry Pub/Sub notifications consumed by an appropriately filtered Cloud Build Pub/Sub trigger.

**C.** A Git commit trigger that assumes every image upload corresponds to a new commit.

**D.** A notification step added only to the main image-building pipeline.

**Doğru cevap: B**

**Registry olayıyla build** · Rehber 2.2 · Kaynak PT6-Q17

Registry kaynağındaki bildirim hem pipeline hem manuel upload yolunu kapsar. Cloud Build Pub/Sub trigger doğrudan tüketebilir. VPC-SC sınırı soru kökünde dışlandı.

**Yakın alternatif neden elenir?** Yalnız ana pipeline içindeki bildirim manuel upload’ı kaçırır.

**Belirleyici ifade:** “including ... directly from developer machines”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/build/docs/automate-builds-pubsub-events).

---

## Soru 18

A Cloud Build job successfully tests code and builds a container using a unique tag. Its next step deploys that tag to Cloud Run, but deployment reports that the image does not exist in Artifact Registry. The pipeline contains neither a push step nor an images output configuration. What must happen before deployment?

**Select ONE answer.**

**A.** Rename the Cloud Run service so its name matches the image repository.

**B.** Push the built image to the intended Artifact Registry repository and make deployment wait for that push.

**C.** Give the runtime service account Cloud Build Editor while leaving the image local to the build.

**D.** Remove the unique tag and deploy latest instead.

**Doğru cevap: B**

**Build ile push sınırı** · Rehber 2.2 · Kaynak PT6-Q20

Build container’ında image üretmek registry’ye upload değildir. Deployment erişilebilir registry artifact’ına ihtiyaç duyar; push’ın tamamlanması beklenir.

**Yakın alternatif neden elenir?** Service adıyla repository adının aynı olması gerekmez.

**Belirleyici ifade:** “neither a push step nor an images output configuration”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/build/docs/building/build-containers).

---

## Soru 19

Long-running analytics queries against a Cloud SQL for PostgreSQL primary are slowing customer transactions. Analysts need a continuously refreshed copy in BigQuery, while the transactional application must keep using Cloud SQL. Which managed integration best separates these workloads without building a custom dual-write path?

**Select ONE answer.**

**A.** Modify every transaction to synchronously write to Cloud SQL and BigQuery without reconciliation.

**B.** Move the analytical queries to a newly created empty BigQuery dataset without replicating data.

**C.** Use Datastream change data capture to replicate the relevant tables to BigQuery.

**D.** Export CSV files manually at the end of each month.

**Doğru cevap: C**

**SQL analitik ayrımı** · Rehber 4.1 · Kaynak PT5-Q54

Datastream CDC ile değişiklikler analitik hedefe aktarılır. Sıfır gecikme/sıfır kaynak yükü garantisi değil; transactional workload ile ağır analitiği ayıran yönetilen yaklaşımdır.

**Yakın alternatif neden elenir?** Dual-write iki hedef başarısızlık/tutarlılık yükünü uygulamaya ekler.

**Belirleyici ifade:** “continuously refreshed; keep using Cloud SQL”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/datastream/docs/overview).

---

## Soru 20

A client uploads thousands of small rows through BigQuery's insertAll API. It currently makes one request per row, and request overhead dominates runtime. You want a small client-side improvement while staying within the API's request-size limits. What should change?

**Select ONE answer.**

**A.** Create a separate Cloud Storage object for every row before making the same individual insert calls.

**B.** Group multiple rows into bounded insertAll requests and inspect row-level errors in each response.

**C.** Increase the retry count while preserving one successful request per row.

**D.** Send all rows in one unlimited-size request and ignore individual row failures.

**Doğru cevap: B**

**Küçük API yazımlarını batch etme** · Rehber 4.1 · Kaynak PT5-Q33

Bounded batching sabit request overhead’ini amorti eder. Boyut limitleri ve satır bazında kısmi başarısızlıklar ele alınmalıdır.

**Yakın alternatif neden elenir?** Sınırsız tek request API sınırlarını ihlal edebilir; bütün sonuçları başarı varsayamazsın.

**Belirleyici ifade:** “one request per row; request-size limits”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery).

---

## Soru 21

A Cloud Run service connects to Cloud SQL in another project. The runtime account already has Cloud SQL Client on the database project, and routing and database credentials have been verified. Diagnostics show that the Cloud SQL Admin API is disabled in the Cloud Run project. What should you correct first?

**Select ONE answer.**

**A.** Enable the Cloud SQL Admin API in the Cloud Run project and ensure it is also enabled in the database project.

**B.** Move the database into the Cloud Run project.

**C.** Grant Cloud SQL Admin instead of Cloud SQL Client to avoid enabling the API.

**D.** Increase the PostgreSQL max_connections value to bypass the disabled API.

**Doğru cevap: A**

**Cross-project SQL API** · Rehber 4.2 · Kaynak PT6-Q45

API enablement IAM’den ayrıdır. Cross-project Cloud Run SQL bağlantısında gerekli API her iki projede açılır.

**Yakın alternatif neden elenir?** Daha geniş IAM rolü kapalı API’yi etkinleştirmez.

**Belirleyici ifade:** “API is disabled in the Cloud Run project”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/sql/docs/postgres/connect-run).

---

## Soru 22

A GKE application process can remain alive while it is temporarily unable to serve requests. Its /ready endpoint accurately reports this condition, and restarting the process would not help. Which probe should use that endpoint to remove an unready Pod from Service traffic while allowing it to recover?

**Select ONE answer.**

**A.** Configure a PodDisruptionBudget and use it as the request-routing health check.

**B.** Configure readinessProbe to call /ready.

**C.** Configure startupProbe to call /ready only once and rely on that result for the Pod lifetime.

**D.** Configure livenessProbe to call /ready and restart on every failure.

**Doğru cevap: B**

**Trafik uygunluğu** · Rehber 3.2 · Kaynak PT5-Q32

Readiness başarısızlığı Service endpoint uygunluğunu etkiler; restart gerektirmez. Liveness process recovery için farklı amaçtadır.

**Yakın alternatif neden elenir?** Startup probe yalnız başlangıcı korur; çalışma boyunca trafik uygunluğunu takip etmez.

**Belirleyici ifade:** “restarting ... would not help; Service traffic”

[Ek resmî teknik kaynak](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

---

## Soru 23

A browser page displays core account information and an optional recommendation panel from a slower third-party API. The panel is not needed for the initial view. You want the core page to become usable without waiting for that API, while handling failures gracefully. Which client design best fits?

**Select ONE answer.**

**A.** Move the same blocking API call before every static asset request.

**B.** Reload the whole page repeatedly until the external API responds successfully.

**C.** Render the core view first, fetch recommendations asynchronously, and update the panel when the response arrives.

**D.** Block all rendering with a synchronous request until recommendations are available.

**Doğru cevap: C**

**İsteğe bağlı API ve arayüz** · Rehber 4.2 · Kaynak PT1-Q38

Kritik olmayan response başlangıç render’ını bloklamaz; tamamlanınca ilgili UI güncellenir. Hata veya loading durumu ayrıca gösterilebilir.

**Yakın alternatif neden elenir?** Senkron bekleme opsiyonel veriyi tüm kullanıcı deneyiminin kritik yoluna sokar.

**Belirleyici ifade:** “optional; not needed for the initial view”

[Ek resmî teknik kaynak](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest_API/Synchronous_and_Asynchronous_Requests).

---

## Soru 24

A function in project A writes new output objects to one bucket in project B. It must use a dedicated runtime identity, and it does not need to read, overwrite, or delete existing objects. Which TWO actions establish the required identity and least-privilege access?

**Select TWO answers.**

**A.** Configure the function to run as a dedicated IAM service account.

**B.** Generate a runtime service account key and include it in the function source.

**C.** Grant that runtime service account Storage Object Creator on the destination bucket.

**D.** Grant the Cloud Functions service agent Project Editor in project B.

**E.** Grant the developer Storage Object Creator and leave the runtime identity unchanged.

**Doğru cevap: A+C**

**Cross-project runtime izinleri** · Rehber 1.2 · Kaynak PT5-Q30

Çalışan kodun kimliği runtime SA olur. Hedef bucket üzerinde objectCreator yeni nesne yazımına yeter; farklı proje olması kullanıcı veya servis ajanına yetki verme gerekçesi değildir.

**Yakın alternatif neden elenir?** Developer hesabındaki yetki kodun runtime kimliğine aktarılmaz.

**Belirleyici ifade:** “dedicated runtime identity; new output objects”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/functions/docs/securing/function-identity).

---

## Soru 25

Your application passes unit, integration, and expected-load tests. The team still does not know whether retries and failover work when a dependency becomes unreachable. You want evidence about recovery behavior in a controlled staging environment. Which additional testing approach addresses this uncertainty most directly?

**Select ONE answer.**

**A.** Increase load only while keeping all dependencies healthy.

**B.** Repeat successful unit tests more frequently without changing failure conditions.

**C.** Review static code coverage and treat high coverage as proof that failover works.

**D.** Inject bounded dependency failures, observe recovery against defined expectations, and stop the experiment if guardrails are exceeded.

**Doğru cevap: D**

**Dayanıklılık testi** · Rehber 2.3 · Kaynak PT6-Q49

Kontrollü fault injection/chaos testi arıza altındaki gerçek retry/failover davranışını gözlemler.

**Yakın alternatif neden elenir?** Load testi kapasite davranışını gösterir; özellikle dependency arızası oluşturmuyorsa recovery kanıtı değildir.

**Belirleyici ifade:** “dependency becomes unreachable; recovery behavior”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/architecture/framework/reliability/perform-testing-for-recovery-from-failures).

---

## Soru 26

A Cloud Storage client sees intermittent HTTP 429 responses during sudden traffic increases. Operations being retried are safe to repeat under the application's existing idempotency controls. Which client behavior best handles transient throttling while avoiding synchronized retry storms?

**Select ONE answer.**

**A.** Use the same fixed short delay in every client and retry indefinitely.

**B.** Treat every 429 as a permanent missing-object error and discard the operation.

**C.** Use bounded exponential backoff with jitter and appropriate retry limits.

**D.** Retry immediately in every client until each operation succeeds.

**Doğru cevap: C**

**429 sonrası retry** · Rehber 4.2 · Kaynak PT5-Q52

Backoff talebi azaltır, jitter istemcileri aynı anda yeniden çağrı yapmaktan uzaklaştırır. Kalıcı quota/bottleneck ayrıca çözülmelidir; retry sonsuz değildir.

**Yakın alternatif neden elenir?** Sabit aynı zamanlama yükü yeniden senkronize edebilir.

**Belirleyici ifade:** “intermittent 429; safe to repeat”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/storage/docs/retry-strategy).

---

## Soru 27

A Deployment has four healthy replicas. During a rollout, all four must remain available until replacement Pods pass readiness. Capacity exists for one extra Pod, but no more. The Deployment uses RollingUpdate. Which TWO values implement these rollout constraints?

**Select TWO answers.**

**A.** Set maxSurge to 1.

**B.** Set maxUnavailable to 1.

**C.** Set the rollout strategy to Recreate.

**D.** Set maxSurge to 0.

**E.** Set maxUnavailable to 0.

**Doğru cevap: A+E**

**Deployment rollout sınırları** · Rehber 3.2 · Kaynak PT5-Q34

maxSurge=1 bir ek Pod’a izin verir; maxUnavailable=0 rollout’un kullanılabilir kopyayı hedefin altına indirmesini önler. Readiness ve kapasite sağlanmış varsayılır; tüm arızalara mutlak uptime garantisi değildir.

**Yakın alternatif neden elenir?** maxSurge=0/maxUnavailable=1 önce eski Pod silmeye izin verir; dört hazır kopyayı korumaz.

**Belirleyici ifade:** “all four; capacity ... one extra Pod”

[Ek resmî teknik kaynak](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

---

## Soru 28

A web service authorizes users to upload large videos to Cloud Storage. Proxying every upload through the application consumes its network and compute capacity. The backend must retain control over the destination object and who can initiate an upload. Which design removes the application from the bulk-data path?

**Select ONE answer.**

**A.** After authorization, provide a narrowly scoped signed upload URL or a resumable-upload session URI to the client.

**B.** Send each video through a longer-timeout Cloud Run request and buffer the whole file in memory.

**C.** Give all authenticated users write permission on the entire bucket.

**D.** Embed the backend service account private key in the upload page.

**Doğru cevap: A**

**Büyük dosya upload veri yolu** · Rehber 1.1 · Kaynak PT2-Q13

Backend yetkilendirdikten sonra sınırlandırılmış yükleme yetkisini istemciye verir; byte aktarımı doğrudan Storage’a olur. Resumable session URI de bearer credential olarak korunmalıdır.

**Yakın alternatif neden elenir?** Bucket-wide genel yetki hedef nesne ve kullanıcı denetimini gereksiz genişletir.

**Belirleyici ifade:** “retain control over the destination object; bulk-data path”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

---

## Soru 29

An approved compliance policy requires every stored record to remain undeletable for seven years. Records are actively queried for three years, after which retrieval is rare. The bucket design has already been reviewed for an irreversible retention lock. Which combination meets both retention and storage-cost requirements?

**Select ONE answer.**

**A.** Move objects to Archive after three years and rely on its minimum storage duration to enforce seven years.

**B.** Use lifecycle deletion after seven years without setting a retention policy.

**C.** Enable Object Versioning and give users permission to delete all object generations.

**D.** Lock the seven-year bucket retention policy and use a lifecycle transition to Archive after three years.

**Doğru cevap: D**

**Retention ve lifecycle** · Rehber 1.2 · Kaynak PT1-Q13

Retention policy silme/değiştirme engelini, lifecycle transition storage class değişimini sağlar. Archive minimum süre ücretlendirmesi retention garantisi değildir.

**Yakın alternatif neden elenir?** Lifecycle delete kuralı erken manuel silmeyi engellemez.

**Belirleyici ifade:** “undeletable for seven years; retrieval is rare”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/storage/docs/bucket-lock).

---

## Soru 30

A release includes both routine fixes and a new capability that depends on an unproven external provider. The fixes must reach all users now. You want to enable the new capability for a small group and disable only that capability immediately if the provider becomes unreliable. Which approach best separates these release decisions?

**Select ONE answer.**

**A.** Deploy the release with a feature flag controlling the external-provider capability.

**B.** Increase the provider request timeout for every user and deploy without a rollout control.

**C.** Roll back the entire release whenever the external provider fails.

**D.** Use a blue/green switch that moves every user to the new release at once.

**Doğru cevap: A**

**Üçüncü taraf özelliği kapatma** · Rehber 1.1 · Kaynak PT6-Q38

Feature flag kodun deployment durumuyla özelliğin etkinliğini ayırır; rutin düzeltmeler kalırken ilgili özellik kapatılır.

**Yakın alternatif neden elenir?** Tam rollback düzeltmeleri de geri alır; istenen yalnız bir yeteneği kapatmaktır.

**Belirleyici ifade:** “disable only that capability”

[Ek resmî teknik kaynak](https://cloud.google.com/architecture/application-deployment-and-testing-strategies).

---

## Soru 31

Two workers can credit the same Datastore-mode account concurrently. Each reads the current balance, adds its own amount, and writes the result. Occasionally one credit disappears even though both writes succeed. Which change prevents the lost-update race?

**Select ONE answer.**

**A.** Read and update the account inside a transaction, allowing the transaction logic to retry on contention.

**B.** Keep the read outside the transaction and put only the final write inside it.

**C.** Read with an ancestor query but leave the read and write as separate uncoordinated operations.

**D.** Write both results faster by raising the number of worker threads.

**Doğru cevap: A**

**Atomik read-modify-write** · Rehber 4.1 · Kaynak PT5-Q36

Read ve ona bağlı write aynı transaction denemesinde olmalı. Conflict retry güncel bakiye üzerinden yeniden hesaplar.

**Yakın alternatif neden elenir?** Güçlü tutarlı okuma tek başına okuma ile yazma arasındaki yarışmayı engellemez.

**Belirleyici ifade:** “one credit disappears; both writes succeed”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/datastore/docs/concepts/transactions).

---

## Soru 32

A partner API already verifies API keys in Apigee. Each key belongs to either a standard or premium API product. The business wants different daily request allowances for the two products, with usage tracked separately for each client application. Which policy design best enforces these allowances?

**Select ONE answer.**

**A.** Use one Quota counter shared by every application using the proxy.

**B.** Use a SpikeArrest policy with one shared requests-per-second value for the proxy.

**C.** Use a Quota policy with the product-specific allowance and a client-specific identifier.

**D.** Set the backend load balancer maximum request rate to the premium daily allowance.

**Doğru cevap: C**

**API ürününe göre kota** · Rehber 1.1 · Kaynak PT6-Q3

Günlük toplam kullanım Quota ile, müşteri ayrımı counter identifier ile kurulur. API product kotası ilgili ürün seviyesini temsil eder.

**Yakın alternatif neden elenir?** SpikeArrest kısa süreli ani yükü yumuşatır; günlük müşteri bazlı kullanım hakkının yerine geçmez.

**Belirleyici ifade:** “daily request allowances; separately for each client”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy).

---

## Soru 33

An order process calls three existing HTTP services. The response from the first service determines whether to call the second or the third, and the chosen response feeds a final update. There is no human approval or external callback to wait for. Which orchestration approach adds the least unnecessary infrastructure?

**Select ONE answer.**

**A.** Create a Cloud Tasks queue and expect the queue to evaluate response fields and choose subsequent services.

**B.** Use Workflows HTTP steps and switch conditions based on returned values.

**C.** Create an Airflow environment solely to run this short request-driven sequence.

**D.** Create a callback endpoint for every step and wait for callbacks instead of using the returned responses.

**Doğru cevap: B**

**Workflow dallanması** · Rehber 1.1 · Kaynak PT4-Q59

Workflows değişken, sıra ve switch ile servis dönüşlerine göre akışı yönetir. Queue kendi başına iş akışı karar motoru değildir.

**Yakın alternatif neden elenir?** Callback yalnız gerçekten dışarıdan bir devam sinyali beklendiğinde gerekir; burada sonuç zaten HTTP response içinde.

**Belirleyici ifade:** “response determines; no external callback”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions).

---

## Soru 34

Binary Authorization is enabled on production GKE clusters. Your release rule requires proof that the exact container image passed regression tests. The test pipeline is trusted to issue this proof only after successful tests. Which TWO additions make admission enforce that rule?

**Select TWO answers.**

**A.** Use the latest tag as sufficient evidence that the tests ran successfully.

**B.** Create a signed attestation for the tested image digest after the regression tests pass.

**C.** Replace the admission policy with an image-retention policy in Artifact Registry.

**D.** Configure an attestor and an enforcing policy that requires its attestation.

**E.** Create the attestation before testing so failed tests cannot delay deployment.

**Doğru cevap: B+D**

**Test attestation akışı** · Rehber 2.2 · Kaynak PT6-Q14

Attestor doğrulanan imzayı tanımlar; pipeline başarılı test sonrası digest’e attestation üretir. Enforcing admission policy bunu deployment sırasında ister.

**Yakın alternatif neden elenir?** Tag test kanıtı değildir. Binary Authorization testleri kendiliğinden çalıştırmaz.

**Belirleyici ifade:** “exact container image; only after successful tests”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/binary-authorization/docs/attestations).

---

## Soru 35

You need local integration tests for a service that consumes Pub/Sub messages containing sensitive payment information. The tests must reproduce malformed and duplicate-message cases without accessing production data or depending on an external project. Which approach best supports those requirements?

**Select ONE answer.**

**A.** Send randomly generated bytes to the production subscription until an error occurs.

**B.** Use the Pub/Sub emulator with synthetic fixtures covering valid, malformed, and duplicate messages.

**C.** Replay unmodified production payment messages into the local test environment.

**D.** Replace the subscriber with a mock that always reports success and skip message parsing.

**Doğru cevap: B**

**Tekrarlanabilir messaging testi** · Rehber 2.3 · Kaynak PT2-Q18

Emulator ve kontrollü sentetik fixture yerel veri akışını tekrar üretir. Bu, gerçek IAM ve bütün hosted-service davranışlarının doğrulandığı anlamına gelmez.

**Yakın alternatif neden elenir?** Sadece başarılı mock hatalı mesaj parse/dedup davranışını ölçmez.

**Belirleyici ifade:** “reproduce malformed and duplicate-message cases”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/pubsub/docs/emulator).

---

## Soru 36

A GKE container sometimes needs two minutes to initialize. Its liveness check is useful for detecting deadlocks after startup, but currently restarts the container before initialization finishes. You want to allow startup time without slowing steady-state deadlock detection. Which probe configuration should you add?

**Select ONE answer.**

**A.** A readiness probe alone, leaving the failing liveness timing unchanged.

**B.** A startup probe with a sufficient startup budget, while preserving the normal liveness check.

**C.** A PodDisruptionBudget that prevents liveness-triggered restarts.

**D.** A much slower liveness check that applies throughout the entire container lifetime.

**Doğru cevap: B**

**Yavaş başlangıç ve liveness** · Rehber 3.2 · Kaynak PT5-Q27

Startup probe başarılı olana kadar liveness/readiness çalıştırılmaz. Başlangıç penceresi ile sonradan deadlock tespit hızı ayrılır.

**Yakın alternatif neden elenir?** Readiness tek başına liveness’ın öldürmesini önlemez.

**Belirleyici ifade:** “without slowing steady-state deadlock detection”

[Ek resmî teknik kaynak](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

---

## Soru 37

A Cloud Run compliance service checks the names of newly created Cloud Storage buckets. It should run automatically after bucket creation, without polling. IAM and the event delivery prerequisites can be configured. Which event route matches bucket creation rather than uploads of objects into existing buckets?

**Select ONE answer.**

**A.** Use only a direct object-finalized trigger and assume it also fires whenever an empty bucket is created.

**B.** Configure a Cloud Run CPU alert as the notification mechanism for bucket creation.

**C.** Schedule a periodic list operation and compare bucket names once per day.

**D.** Use an Eventarc Cloud Audit Logs trigger filtered for the Cloud Storage bucket-creation API method.

**Doğru cevap: D**

**Bucket create audit olayı** · Rehber 3.1 · Kaynak PT6-Q71

Bucket oluşturma yönetim API olayı Audit Logs filtrelemesiyle yönlendirilebilir. Object finalize ise dosya/nesne olayıdır; boş bucket oluşturma değildir.

**Yakın alternatif neden elenir?** Object-finalized trigger mevcut bucket’a yüklenen nesneyi temsil eder.

**Belirleyici ifade:** “bucket creation rather than uploads of objects”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/eventarc/standard/docs/run/cal).

---

## Soru 38

A Go service on GKE uses unexpectedly high CPU and memory under ordinary traffic. You need to identify expensive functions and allocation paths inside the running application, rather than measure latency between services. Which tool and evidence best match this investigation?

**Select ONE answer.**

**A.** Use only uptime checks to infer the functions allocating memory.

**B.** Read only load balancer access logs and group requests by status code.

**C.** Use only Cloud Trace spans around remote HTTP calls.

**D.** Instrument the supported Go application with Cloud Profiler and inspect CPU and heap profiles.

**Doğru cevap: D**

**CPU ve heap profili** · Rehber 4.3 · Kaynak PT2-Q45

Profiler CPU/heap dağılımını code path düzeyinde gösterir; Trace servis/request süreleri için tamamlayıcıdır.

**Yakın alternatif neden elenir?** Dış HTTP span süreleri hangi iç fonksiyonun allocation yaptığını doğrudan vermez.

**Belirleyici ifade:** “functions and allocation paths; inside the ... application”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/profiler/docs/about-profiler).

---

## Soru 39

An API invokes payment, shipping, and inventory services. Users report occasional slow responses, but aggregate CPU metrics look normal. You need to identify which outgoing operation consumes the request time. What instrumentation provides the most useful evidence?

**Select ONE answer.**

**A.** Increase the logging severity of every message without adding timing or correlation information.

**B.** Add a readiness probe and use its success rate as the duration of every outgoing call.

**C.** Collect only node-level CPU metrics and infer which external API is slow.

**D.** Add OpenTelemetry spans around outgoing calls and inspect the resulting distributed traces in Cloud Trace.

**Doğru cevap: D**

**Dış servis gecikmesini izleme** · Rehber 4.3 · Kaynak PT5-Q46

Span hiyerarşisi ve süreler gecikmenin hangi çağrıda toplandığını gösterir. Dış sağlayıcı iç trace sağlamasa bile client span çağrı süresini ölçebilir.

**Yakın alternatif neden elenir?** CPU normal olması dış I/O latency’sini dışlamaz.

**Belirleyici ifade:** “which outgoing operation consumes the request time”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/trace/docs/overview).

---

## Soru 40

Two application teams share a GKE cluster. Team B needs to deploy ordinary workloads for an integration, but it must not change Team A's Deployments or Services. No project-wide administrative role is required. Which access configuration provides the requested control with the least unnecessary privilege?

**Select ONE answer.**

**A.** Grant Team B Project Editor and ask it to use a separate namespace.

**B.** Grant Team B Kubernetes cluster-admin and distinguish its resources with labels.

**C.** Create a namespace for Team B and bind suitable Kubernetes workload-management permissions within that namespace.

**D.** Give Team B project Viewer and rely on that role to authorize creating Deployments.

**Doğru cevap: C**

**Namespace yetkisi** · Rehber 1.2 · Kaynak PT5-Q26

Namespace kapsamlı RBAC, Team B erişimini ilgili namespace kaynaklarına sınırlar. Namespace tek başına network/host güvenlik izolasyonu değildir; burada ölçülen kaynak değiştirme yetkisidir.

**Yakın alternatif neden elenir?** Project Editor gibi geniş izinleri namespace isimlendirmesi daraltmaz.

**Belirleyici ifade:** “must not change Team A; no project-wide administrative role”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).

---

## Soru 41

A GKE API is exposed to external partners. Requests must pass OAuth token validation and API-specific authorization before reaching the backend. The public endpoint also needs managed protection against common web exploits and volumetric attacks. Which architecture covers both requirements?

**Select ONE answer.**

**A.** Use Cloud Armor alone and treat every request that passes its WAF rules as an authenticated partner request.

**B.** Place Apigee on an ingress path protected by an external Application Load Balancer and Cloud Armor, and prevent backend bypass.

**C.** Use Apigee authentication but expose a second unrestricted public path directly to the GKE backend.

**D.** Expose an Istio ingress gateway and rely only on Kubernetes NetworkPolicy for OAuth validation and WAF protection.

**Doğru cevap: B**

**API güvenliğinin katmanları** · Rehber 1.2 · Kaynak PT6-Q41

Apigee API kimlik/policy katmanı; Armor dış web saldırı korumasıdır. Korunan yolu bypass eden açık backend bırakılmamalı.

**Yakın alternatif neden elenir?** Cloud Armor WAF kontrolünü geçmek uygulama kullanıcısının OAuth ile doğrulandığı anlamına gelmez.

**Belirleyici ifade:** “OAuth token validation; common web exploits”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/architecture/best-practices-securing-applications-and-apis-using-apigee).

---

## Soru 42

An application project and a database project belong to the same organization. A new private-IP AlloyDB deployment is being planned. The teams must retain separate project ownership but are permitted to use a centrally managed network. Which design provides private reachability without relying on the Auth Proxy to create a network path?

**Select ONE answer.**

**A.** Move all application resources into the database project and grant its developers Project Editor.

**B.** Attach both service projects to an approved Shared VPC and configure AlloyDB private connectivity in that network.

**C.** Keep the networks disconnected and run the AlloyDB Auth Proxy beside the application.

**D.** Keep the networks disconnected and give the application service account AlloyDB Client.

**Doğru cevap: B**

**AlloyDB için ağ ve kimlik ayrımı** · Rehber 1.2 · Kaynak PT6-Q15

Proje ayrılığı ağ ayrılığı olmak zorunda değildir. Shared VPC ortak özel ağı, IAM ise ayrı kaynak yetkilerini sağlar. AlloyDB için gereken private services access ayrıca yapılandırılır.

**Yakın alternatif neden elenir?** Auth Proxy güvenli kimlikli bağlantı sağlar; mevcut olmayan ağ rotasını oluşturmaz.

**Belirleyici ifade:** “separate project ownership; centrally managed network”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/alloydb/docs/configure-connectivity).

---

## Soru 43

GKE workers consume one Pub/Sub subscription. They spend much of their time waiting for downstream I/O, so CPU usage stays low even when the backlog grows. More worker replicas improve throughput, and node capacity is available. Which autoscaling signal best matches the processing demand?

**Select ONE answer.**

**A.** Use VPA recommendations as the mechanism for creating more worker replicas.

**B.** Configure HPA with an appropriate external Pub/Sub backlog metric.

**C.** Enable only cluster node autoscaling and expect it to increase the Deployment replica count.

**D.** Configure HPA to increase replicas only when CPU utilization reaches 90 percent.

**Doğru cevap: B**

**Pub/Sub backlog ile HPA** · Rehber 3.2 · Kaynak PT1-Q15

External backlog metriği iş talebini doğrudan yansıtır. HPA replica sayısını, node autoscaler ise node kapasitesini yönetir.

**Yakın alternatif neden elenir?** CPU düşük kaldığı için yalnız CPU tabanlı sinyal bu I/O bekleyen iş yükündeki birikimi kaçırabilir.

**Belirleyici ifade:** “CPU usage stays low even when the backlog grows”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/autoscaling-metrics).

---

## Soru 44

A Cloud Run service has a healthy production revision. A new revision must be tested with a small fraction of live traffic before wider rollout, and you want to use native revision management. What is the safest sequence for introducing the new revision?

**Select ONE answer.**

**A.** Deploy without immediately assigning traffic, allocate a small percentage, evaluate signals, and increase gradually.

**B.** Delete the current revision before deploying the new one to prevent version overlap.

**C.** Deploy to 100 percent of traffic and rely on rollback only after all users are exposed.

**D.** Create a second DNS name and assume DNS automatically sends a controlled percentage to each revision.

**Doğru cevap: A**

**Cloud Run kademeli rollout** · Rehber 3.1 · Kaynak PT6-Q2

Yeni revision önce no-traffic deploy edilir; native traffic split ile kontrollü canlı kullanıcı etkisi sağlanır. Rollback yolu korunur.

**Yakın alternatif neden elenir?** 100% dağıtıp sonra gözlemek gradual exposure şartını karşılamaz.

**Belirleyici ifade:** “small fraction of live traffic; native revision management”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration).

---

## Soru 45

Several replicas of a legacy service must read and update files on the same filesystem. You are moving the service to GKE, and changing its file operations to an object-storage API is out of scope. The existing service uses NFS and requires shared writable access. Which storage approach minimizes application changes?

**Select ONE answer.**

**A.** Use a Filestore NFS share through an appropriate GKE PersistentVolume configuration.

**B.** Give each replica a different Persistent Disk and assume writes become visible to other replicas.

**C.** Mount a Cloud Storage bucket and assume it provides every NFS filesystem behavior unchanged.

**D.** Put the writable files in a ConfigMap and mount it in every Pod.

**Doğru cevap: A**

**Paylaşılan dosya sistemi** · Rehber 1.3 · Kaynak PT5-Q22

NFS ve ortak read/write gereksinimi yönetilen Filestore ile karşılanabilir. Performans, erişim ve uygun tier ayrıca seçilmelidir.

**Yakın alternatif neden elenir?** Object storage mount, NFS/POSIX davranışlarının tamamının yerine geçtiği varsayımıyla kullanılmamalı.

**Belirleyici ifade:** “existing service uses NFS; shared writable access”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver).

---

## Soru 46

A Bigtable table stores account activity. Reads usually request a time interval for one account, and writes are spread across many active accounts. Each event has an account ID and a fixed-width timestamp. Which row-key ordering best supports these reads while avoiding a single global timestamp-leading write hotspot?

**Select ONE answer.**

**A.** Use account ID followed by the fixed-width timestamp and an event disambiguator if required.

**B.** Use timestamp followed by account ID for every event.

**C.** Use account ID alone, overwriting its row each time a new event arrives.

**D.** Use a random UUID alone and scan the whole table for account history.

**Doğru cevap: A**

**Bigtable row key** · Rehber 1.3 · Kaynak PT5-Q41

Account prefix aynı hesabın zaman aralığını bitişik satırlara toplar. Global artan timestamp prefix tüm yazımları bir kenara yığabilir. Tek hesabın çok sıcak olması ayrıca tasarım gerektirir.

**Yakın alternatif neden elenir?** UUID dağıtımı iyileştirebilir ama sorudaki temel account-range sorgusunu kaybettirir.

**Belirleyici ifade:** “time interval for one account; many active accounts”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/bigtable/docs/schema-design).

---

## Soru 47

Several commits must run Spanner performance tests concurrently. You need comparable latency measurements without the test runs competing for the same Spanner compute capacity. The budget permits temporary managed instances in an existing test project. Which setup is most appropriate?

**Select ONE answer.**

**A.** Use the Spanner emulator as a substitute for production-service latency measurements.

**B.** Run every test against the production instance after truncating its tables.

**C.** Provision an equivalent isolated Spanner instance per run, load controlled test data, and remove it after testing.

**D.** Create a separate database per run on one shared instance and assume compute is isolated.

**Doğru cevap: C**

**Paralel performans testi izolasyonu** · Rehber 2.3 · Kaynak PT4-Q7

Instance başına ayrılmış compute paralel run’ların Spanner kapasitesini paylaşmasını önler. Aynı konfigürasyon/veri ve warm-up gibi test kontrolleri yine gerekir.

**Yakın alternatif neden elenir?** Ayrı database veri izolasyonu sağlayabilir ama aynı instance compute kapasitesini paylaşır. Emulator performans eşdeğeri değildir.

**Belirleyici ifade:** “without ... competing for the same ... compute capacity”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/spanner/docs/emulator).

---

## Soru 48

A developer must test a PostgreSQL client against a staging Cloud SQL instance from a workstation. Approved network reachability already exists. The connection should use IAM-authorized, encrypted transport without manually managing client certificates. Database credentials and grants are handled separately. What should the developer run locally?

**Select ONE answer.**

**A.** Run Cloud SQL Auth Proxy with an authorized identity and point the application at its local listener.

**B.** Use the Cloud SQL Admin REST API as the PostgreSQL query endpoint.

**C.** Connect to a newly created local PostgreSQL database and assume it contains current staging data.

**D.** Grant Cloud SQL Editor and connect through an unencrypted raw connection without a proxy.

**Doğru cevap: A**

**Yerelde güvenli SQL bağlantısı** · Rehber 2.1 · Kaynak PT5-Q56

Auth Proxy güvenli bağlantı katmanını yönetir. Ağ yolu, IAM connectivity rolü ve database login/grant ayrı gerekliliklerdir; soru diğerlerini açıkça sağlar.

**Yakın alternatif neden elenir?** Admin REST API instance yönetir; SQL sorgu protokolünün yerine geçmez.

**Belirleyici ifade:** “reachability already exists; certificates”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy).

---

## Soru 49

You are deploying a stateful service on GKE. Each replica needs a stable ordinal network identity and its own persistent volume that can be reattached when that replica's Pod is replaced. Which controller and storage pattern best express those requirements?

**Select ONE answer.**

**A.** Use a Deployment whose replicas all write to one emptyDir volume.

**B.** Use a Deployment with random Pod names and assume a ClusterIP Service gives each replica a stable identity.

**C.** Use a DaemonSet and identify each replica only by its current Pod IP.

**D.** Use a StatefulSet with the required governing Service and volumeClaimTemplates.

**Doğru cevap: D**

**StatefulSet kimliği** · Rehber 3.2 · Kaynak PT2-Q10

StatefulSet sabit ordinal kimlik ve replica başına PVC düzeni sağlar. Governing headless Service ağ kimliğini destekler.

**Yakın alternatif neden elenir?** ClusterIP Service tüm backend’ler için ortak adres sağlar; tek tek replica kimliğinin yerine geçmez.

**Belirleyici ifade:** “each replica; stable ordinal; its own persistent volume”

[Ek resmî teknik kaynak](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

---

## Soru 50

You successfully retrieve credentials for a GKE cluster from Cloud Shell. Subsequent kubectl requests time out. The cluster uses a public control-plane endpoint restricted by authorized networks, and Cloud Shell's current public IP is outside those ranges. What is the most direct correction?

**Select ONE answer.**

**A.** Run get-credentials repeatedly until it creates a network route.

**B.** Authorize the approved Cloud Shell source IP for the control-plane endpoint, following the network access policy.

**C.** Grant the caller cluster-admin while leaving the authorized network ranges unchanged.

**D.** Change the application Service from ClusterIP to LoadBalancer.

**Doğru cevap: B**

**Cloud Shell GKE erişim teşhisi** · Rehber 2.1 · Kaynak PT5-Q39

Credential edinme ile Kubernetes endpoint’e paket ulaşması farklı katmanlar. Verilen bulgu authorized networks uyuşmazlığını doğrudan gösteriyor.

**Yakın alternatif neden elenir?** RBAC yetkisini büyütmek ağdan düşürülen bağlantıyı düzeltmez.

**Belirleyici ifade:** “public IP is outside those ranges”

[Ek resmî teknik kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).

---

