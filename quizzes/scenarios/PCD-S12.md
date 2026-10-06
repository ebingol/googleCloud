# PCD-S12 — Udemy seçkisinden 50 soruluk sınav

**50 soru · 120 dakika kişisel çalışma hedefi · 47 tek seçim + 3 çift seçim**

5 Ekim 2026. Satın aldığın Priya Dw/CertShield paketinden seçilen 50 senaryonun düzenlenmiş İngilizce uyarlamalarıdır. Kaynakların karar konuları korunmuştur; belirsizlikleri gidermek, hatalı genellemeleri çıkarmak ve seçenekleri düzenlemek için metinler yeniden yazılmıştır. Udemy sorularının kelimesi kelimesine kopyası veya 50 tamamen yeni konu değildir. Gerçek sınavla zorluk eşdeğerliği iddiası yoktur.

| Ana alan | Resmî ağırlık | Bu set |
|---|---:|---:|
| Uygulama tasarımı | ~%32 | 16 |
| Geliştirme ve test | ~%23 | 12 |
| Deployment yapılandırması | ~%24 | 12 |
| Google Cloud servisleriyle entegrasyon | ~%21 | 10 |

%23 ve %21, 50 soruda 11,5 ve 10,5 eder; eşit yuvarlama payı geliştirme/test alanına verildi. Konular karışık sıradadır. Dört ana alan ve 11 numaralı alt başlık örneklenir; rehberdeki her ürün/özellik ölçülmez. Bu kaynak seçkisinde güçlü bir Gemini senaryosu bulunmadığından Gemini sorusu eklenmedi.

[Resmî exam guide](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf)

**Çift seçim: Q24, Q27, Q34.** Diğer sorularda bir seçenek işaretle. Çift seçimde tam doğru küme 1 puandır.

İlk turda cevap anahtarını açma. Cevapları `1-b, 2-a+c` biçiminde gönderebilirsin. Eminlik ve gerekçe isteğe bağlıdır. 120. dakikada mevcut cevapları sabitle; devam edersen ek süreyi ayrıca yaz. Yardım/açıklama sonrası seçimler ilk deneme sonucuna eklenmez.

Başlangıç: ____ · Bitiş: ____ · Mola: ____ · Ek süre / yardım: ____

## Bölüm 1 — Sorular 1–10

### Question 01

A Cloud Build pipeline requires an internal compiler that is absent from the standard builders. Several repositories need the same compiler version, and the team wants reproducible builds without installing it from an external site during every build. Which implementation should you use?

**Select ONE answer.**

**A.** Install the compiler on a developer laptop and assume Cloud Build can execute its local binary.

**B.** Move every repository to a permanently managed Jenkins VM solely to obtain this compiler.

**C.** Put the compiler name in the Cloud Build substitutions and rely on automatic tool installation.

**D.** Package the compiler in a versioned custom builder image and reference that image in the build steps.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 02

A container passes testing in staging. The release process must promote the identical bytes to production, even if another build later reuses the same human-readable tag. Which image reference should the deployment record retain to identify the tested artifact unambiguously?

**Select ONE answer.**

**A.** A reusable environment tag such as staging.

**B.** Only the image repository name, without a tag or digest.

**C.** The image digest.

**D.** The latest tag.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 03

A read-heavy application uses a replicated Bigtable instance with clusters in two regions. It currently routes requests to one cluster and requires an operator to change routing during outages. The application accepts eventual consistency and does not require single-row transactions. Which app-profile change enables managed routing to an available cluster?

**Select ONE answer.**

**A.** Add a Dataflow export job and continue sending online reads to the same failed cluster.

**B.** Increase the client connection pool but keep single-cluster routing.

**C.** Keep single-cluster routing and add more nodes only to the currently selected cluster.

**D.** Use a multi-cluster routing app profile with both clusters eligible.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 04

Your organization already produces signed test attestations for approved image digests. A Cloud Run service must reject ordinary deployments that lack this approval, including deployments submitted outside the usual CI pipeline. Which control should enforce this requirement at deployment time?

**Select ONE answer.**

**A.** Add a test step to the usual pipeline but allow every other deployment path without admission checks.

**B.** Use only an Artifact Registry retention policy to control which images can be deployed.

**C.** Enable an enforcing Binary Authorization policy requiring the trusted attestation for the service.

**D.** Require the image tag to contain the word approved, without verifying signed evidence.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 05

Developers use different laptops and IDEs, but their builds require approved tools and private access to services inside the company VPC. Security wants centrally maintained development environments with controlled network access and reproducible tool versions. Which approach provides an appropriate managed foundation?

**Select ONE answer.**

**A.** Install Cloud Code on every laptop and assume the extension creates private connectivity and a common OS toolchain.

**B.** Give each developer Cloud Shell and assume its default network is the company VPC.

**C.** Give developers unrestricted custom VM images and depend on verbal instructions to keep the tools identical.

**D.** Use Cloud Workstations in the approved network with centrally maintained custom images and the required perimeter configuration.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 06

The first step of a Cloud Build job produces a manifest. A later step in the same build must read it, and the dependency order is already correct. The first step currently writes into its container's temporary directory. Which change shares the manifest without introducing a storage service?

**Select ONE answer.**

**A.** Bake it into the first step image after that container has already started.

**B.** Store its path in a substitution and expect the file contents to be transferred automatically.

**C.** Write the manifest under /workspace and have the dependent step read that path.

**D.** Keep it in the first step container and only increase the later step timeout.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 07

An Autopilot cluster has no existing Arm nodes. You are deploying an arm64-compatible image and want GKE to provision appropriate capacity from the workload requirements. The cluster version and region support Arm. Which manifest choice explicitly requests the CPU architecture without managing node pools yourself?

**Select ONE answer.**

**A.** Switch to a Standard cluster solely to create an Arm node pool manually.

**B.** Set an appropriate nodeSelector including kubernetes.io/arch: arm64.

**C.** Add only an Arm-related toleration and rely on it to require Arm nodes.

**D.** Label the Pod metadata with kubernetes.io/arch: arm64 without a scheduling selector.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 08

A chat product uses Firestore. A room can accumulate an unbounded message history, but clients fetch messages in pages and create messages independently. You want to avoid rewriting a large room document whenever a message arrives. Which document model is the best fit?

**Select ONE answer.**

**A.** Store room metadata in a document and each message in a document within its messages subcollection.

**B.** Store every message in one array field on the room document.

**C.** Store only the latest message in the room document and use document versions as the application history.

**D.** Create one project-wide document containing a map of every room and all its messages.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 09

A Workflow must start a Cloud Run job, wait for its execution to complete, and then continue with a reporting step. The job is a batch workload with no application HTTP server. Which integration should the Workflow use?

**Select ONE answer.**

**A.** Call the Cloud Run services invoke endpoint using the job name as a service name.

**B.** Create a Pub/Sub subscription on the job and expect the job itself to listen continuously.

**C.** Use the Cloud Run Admin API connector to run the job and handle its long-running operation.

**D.** Send an HTTP request to an assumed public application URL on the job.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 10

The same workload runs in three GKE clusters in one project. Container stdout is already collected in Cloud Logging. During an incident, you need one query covering the relevant workload across all three clusters. Which approach avoids manually changing kubectl contexts and inspecting replicas individually?

**Select ONE answer.**

**A.** Use the Cloud Trace span list as a complete replacement for container stdout logs.

**B.** Run kubectl logs in one current context and assume it automatically queries the other clusters.

**C.** Query Cloud Logging, for example with gcloud logging read, using container resource and workload-label filters across the clusters.

**D.** Use journalctl on a single worker node and assume it contains all cluster logs.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 2 — Sorular 11–20

### Question 11

Terraform Cloud currently runs your infrastructure plans and applies. Security prohibits storing long-lived Google service account keys in external systems. The team wants to keep its existing Terraform Cloud execution environment and obtain temporary Google Cloud credentials for each run. Which authentication approach best fits?

**Select ONE answer.**

**A.** Store a service account key in Terraform Cloud and rotate the key every month.

**B.** Create a Google Workspace user for the pipeline and store its password as a sensitive variable.

**C.** Configure Workload Identity Federation for Terraform Cloud and scope access to the required resources.

**D.** Move Terraform execution to GKE and use a Kubernetes service account.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 12

You have a small Python HTTP service in a local source directory and need to test it behind an existing Apigee proxy. The language is supported by buildpacks, no Dockerfile is present, and cloud build permissions are ready. Which deployment path minimizes local container-tool setup?

**Select ONE answer.**

**A.** Deploy from the source directory with gcloud run deploy --source, then test the deployed service through Apigee.

**B.** Point the production Apigee proxy at localhost on the developer laptop without configuring reachability.

**C.** Install a local Docker daemon, build and push an image manually, then deploy it.

**D.** Run only local unit tests and treat them as proof that the hosted Apigee route works.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 13

A staging Cloud SQL instance has only a private IP. A developer has no VPN route from the laptop but is authorized to use IAP TCP forwarding. A small VM can be placed on the database's reachable VPC. Which arrangement allows secure development access without assigning a public IP to the VM or database?

**Select ONE answer.**

**A.** Run Cloud SQL Auth Proxy on the VPC VM and reach its appropriately restricted listener through an IAP TCP tunnel.

**B.** Add the laptop public IP to authorized networks and keep all routing unchanged.

**C.** Run Cloud SQL Auth Proxy only on the laptop and assume it creates a private network route.

**D.** Grant the developer Project Owner and connect directly to the private IP over the internet.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 14

A stateless GKE service has ten replicas. During voluntary node drains that use the Kubernetes Eviction API, at least eight replicas must remain available. You are configuring disruption protection rather than changing an application rollout strategy. Which setting expresses this requirement?

**Select ONE answer.**

**A.** A HorizontalPodAutoscaler with minReplicas: 8, without a disruption budget.

**B.** A Deployment with maxSurge: 8, without a disruption budget.

**C.** A PodDisruptionBudget with maxUnavailable: 8.

**D.** A PodDisruptionBudget with minAvailable: 8 and a selector matching the workload.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 15

A market-data API reads from an existing authoritative database. Most requests repeatedly access a small subset of records, and those responses may be a few seconds old. You need to reduce database load without moving the full dataset or making cache eviction cause permanent data loss. Which design should you choose?

**Select ONE answer.**

**A.** Move the entire database into Redis and delete the original records after loading them.

**B.** Place each API read in a Pub/Sub queue and wait for a subscriber to answer.

**C.** Create a BigQuery copy and run an analytical query for every incoming API request.

**D.** Cache frequently requested records in Memorystore; read the database on a cache miss and populate the cache.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 16

Images uploaded to a bucket must be checked with the Vision API and then passed through several processing services. More steps will be added later. You want a managed event-driven entry point and a central definition of the processing sequence, without adding orchestration logic to every worker. Which design best fits?

**Select ONE answer.**

**A.** Route object-finalized events through Eventarc to Workflows, and orchestrate the processing services there.

**B.** Schedule a periodic bucket listing and put all sequencing logic into each image-processing worker.

**C.** Send the event independently to every worker and assume delivery order enforces the processing sequence.

**D.** Use a Cloud Tasks queue as the sole state machine for the entire multi-step process.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 17

Your policy requires a verification build whenever an image is uploaded to Artifact Registry, including approved uploads made directly from developer machines. The project is not using VPC Service Controls. You want an event-driven solution with no polling and no custom relay service. What should trigger verification?

**Select ONE answer.**

**A.** A Cloud Scheduler job that periodically compares image lists.

**B.** Artifact Registry Pub/Sub notifications consumed by an appropriately filtered Cloud Build Pub/Sub trigger.

**C.** A Git commit trigger that assumes every image upload corresponds to a new commit.

**D.** A notification step added only to the main image-building pipeline.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 18

A Cloud Build job successfully tests code and builds a container using a unique tag. Its next step deploys that tag to Cloud Run, but deployment reports that the image does not exist in Artifact Registry. The pipeline contains neither a push step nor an images output configuration. What must happen before deployment?

**Select ONE answer.**

**A.** Rename the Cloud Run service so its name matches the image repository.

**B.** Push the built image to the intended Artifact Registry repository and make deployment wait for that push.

**C.** Give the runtime service account Cloud Build Editor while leaving the image local to the build.

**D.** Remove the unique tag and deploy latest instead.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 19

Long-running analytics queries against a Cloud SQL for PostgreSQL primary are slowing customer transactions. Analysts need a continuously refreshed copy in BigQuery, while the transactional application must keep using Cloud SQL. Which managed integration best separates these workloads without building a custom dual-write path?

**Select ONE answer.**

**A.** Modify every transaction to synchronously write to Cloud SQL and BigQuery without reconciliation.

**B.** Move the analytical queries to a newly created empty BigQuery dataset without replicating data.

**C.** Use Datastream change data capture to replicate the relevant tables to BigQuery.

**D.** Export CSV files manually at the end of each month.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 20

A client uploads thousands of small rows through BigQuery's insertAll API. It currently makes one request per row, and request overhead dominates runtime. You want a small client-side improvement while staying within the API's request-size limits. What should change?

**Select ONE answer.**

**A.** Create a separate Cloud Storage object for every row before making the same individual insert calls.

**B.** Group multiple rows into bounded insertAll requests and inspect row-level errors in each response.

**C.** Increase the retry count while preserving one successful request per row.

**D.** Send all rows in one unlimited-size request and ignore individual row failures.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 3 — Sorular 21–30

### Question 21

A Cloud Run service connects to Cloud SQL in another project. The runtime account already has Cloud SQL Client on the database project, and routing and database credentials have been verified. Diagnostics show that the Cloud SQL Admin API is disabled in the Cloud Run project. What should you correct first?

**Select ONE answer.**

**A.** Enable the Cloud SQL Admin API in the Cloud Run project and ensure it is also enabled in the database project.

**B.** Move the database into the Cloud Run project.

**C.** Grant Cloud SQL Admin instead of Cloud SQL Client to avoid enabling the API.

**D.** Increase the PostgreSQL max_connections value to bypass the disabled API.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 22

A GKE application process can remain alive while it is temporarily unable to serve requests. Its /ready endpoint accurately reports this condition, and restarting the process would not help. Which probe should use that endpoint to remove an unready Pod from Service traffic while allowing it to recover?

**Select ONE answer.**

**A.** Configure a PodDisruptionBudget and use it as the request-routing health check.

**B.** Configure readinessProbe to call /ready.

**C.** Configure startupProbe to call /ready only once and rely on that result for the Pod lifetime.

**D.** Configure livenessProbe to call /ready and restart on every failure.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 23

A browser page displays core account information and an optional recommendation panel from a slower third-party API. The panel is not needed for the initial view. You want the core page to become usable without waiting for that API, while handling failures gracefully. Which client design best fits?

**Select ONE answer.**

**A.** Move the same blocking API call before every static asset request.

**B.** Reload the whole page repeatedly until the external API responds successfully.

**C.** Render the core view first, fetch recommendations asynchronously, and update the panel when the response arrives.

**D.** Block all rendering with a synchronous request until recommendations are available.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 24

A function in project A writes new output objects to one bucket in project B. It must use a dedicated runtime identity, and it does not need to read, overwrite, or delete existing objects. Which TWO actions establish the required identity and least-privilege access?

**Select TWO answers.**

**A.** Configure the function to run as a dedicated IAM service account.

**B.** Generate a runtime service account key and include it in the function source.

**C.** Grant that runtime service account Storage Object Creator on the destination bucket.

**D.** Grant the Cloud Functions service agent Project Editor in project B.

**E.** Grant the developer Storage Object Creator and leave the runtime identity unchanged.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 25

Your application passes unit, integration, and expected-load tests. The team still does not know whether retries and failover work when a dependency becomes unreachable. You want evidence about recovery behavior in a controlled staging environment. Which additional testing approach addresses this uncertainty most directly?

**Select ONE answer.**

**A.** Increase load only while keeping all dependencies healthy.

**B.** Repeat successful unit tests more frequently without changing failure conditions.

**C.** Review static code coverage and treat high coverage as proof that failover works.

**D.** Inject bounded dependency failures, observe recovery against defined expectations, and stop the experiment if guardrails are exceeded.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 26

A Cloud Storage client sees intermittent HTTP 429 responses during sudden traffic increases. Operations being retried are safe to repeat under the application's existing idempotency controls. Which client behavior best handles transient throttling while avoiding synchronized retry storms?

**Select ONE answer.**

**A.** Use the same fixed short delay in every client and retry indefinitely.

**B.** Treat every 429 as a permanent missing-object error and discard the operation.

**C.** Use bounded exponential backoff with jitter and appropriate retry limits.

**D.** Retry immediately in every client until each operation succeeds.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 27

A Deployment has four healthy replicas. During a rollout, all four must remain available until replacement Pods pass readiness. Capacity exists for one extra Pod, but no more. The Deployment uses RollingUpdate. Which TWO values implement these rollout constraints?

**Select TWO answers.**

**A.** Set maxSurge to 1.

**B.** Set maxUnavailable to 1.

**C.** Set the rollout strategy to Recreate.

**D.** Set maxSurge to 0.

**E.** Set maxUnavailable to 0.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 28

A web service authorizes users to upload large videos to Cloud Storage. Proxying every upload through the application consumes its network and compute capacity. The backend must retain control over the destination object and who can initiate an upload. Which design removes the application from the bulk-data path?

**Select ONE answer.**

**A.** After authorization, provide a narrowly scoped signed upload URL or a resumable-upload session URI to the client.

**B.** Send each video through a longer-timeout Cloud Run request and buffer the whole file in memory.

**C.** Give all authenticated users write permission on the entire bucket.

**D.** Embed the backend service account private key in the upload page.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 29

An approved compliance policy requires every stored record to remain undeletable for seven years. Records are actively queried for three years, after which retrieval is rare. The bucket design has already been reviewed for an irreversible retention lock. Which combination meets both retention and storage-cost requirements?

**Select ONE answer.**

**A.** Move objects to Archive after three years and rely on its minimum storage duration to enforce seven years.

**B.** Use lifecycle deletion after seven years without setting a retention policy.

**C.** Enable Object Versioning and give users permission to delete all object generations.

**D.** Lock the seven-year bucket retention policy and use a lifecycle transition to Archive after three years.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 30

A release includes both routine fixes and a new capability that depends on an unproven external provider. The fixes must reach all users now. You want to enable the new capability for a small group and disable only that capability immediately if the provider becomes unreliable. Which approach best separates these release decisions?

**Select ONE answer.**

**A.** Deploy the release with a feature flag controlling the external-provider capability.

**B.** Increase the provider request timeout for every user and deploy without a rollout control.

**C.** Roll back the entire release whenever the external provider fails.

**D.** Use a blue/green switch that moves every user to the new release at once.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 4 — Sorular 31–40

### Question 31

Two workers can credit the same Datastore-mode account concurrently. Each reads the current balance, adds its own amount, and writes the result. Occasionally one credit disappears even though both writes succeed. Which change prevents the lost-update race?

**Select ONE answer.**

**A.** Read and update the account inside a transaction, allowing the transaction logic to retry on contention.

**B.** Keep the read outside the transaction and put only the final write inside it.

**C.** Read with an ancestor query but leave the read and write as separate uncoordinated operations.

**D.** Write both results faster by raising the number of worker threads.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 32

A partner API already verifies API keys in Apigee. Each key belongs to either a standard or premium API product. The business wants different daily request allowances for the two products, with usage tracked separately for each client application. Which policy design best enforces these allowances?

**Select ONE answer.**

**A.** Use one Quota counter shared by every application using the proxy.

**B.** Use a SpikeArrest policy with one shared requests-per-second value for the proxy.

**C.** Use a Quota policy with the product-specific allowance and a client-specific identifier.

**D.** Set the backend load balancer maximum request rate to the premium daily allowance.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 33

An order process calls three existing HTTP services. The response from the first service determines whether to call the second or the third, and the chosen response feeds a final update. There is no human approval or external callback to wait for. Which orchestration approach adds the least unnecessary infrastructure?

**Select ONE answer.**

**A.** Create a Cloud Tasks queue and expect the queue to evaluate response fields and choose subsequent services.

**B.** Use Workflows HTTP steps and switch conditions based on returned values.

**C.** Create an Airflow environment solely to run this short request-driven sequence.

**D.** Create a callback endpoint for every step and wait for callbacks instead of using the returned responses.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 34

Binary Authorization is enabled on production GKE clusters. Your release rule requires proof that the exact container image passed regression tests. The test pipeline is trusted to issue this proof only after successful tests. Which TWO additions make admission enforce that rule?

**Select TWO answers.**

**A.** Use the latest tag as sufficient evidence that the tests ran successfully.

**B.** Create a signed attestation for the tested image digest after the regression tests pass.

**C.** Replace the admission policy with an image-retention policy in Artifact Registry.

**D.** Configure an attestor and an enforcing policy that requires its attestation.

**E.** Create the attestation before testing so failed tests cannot delay deployment.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 35

You need local integration tests for a service that consumes Pub/Sub messages containing sensitive payment information. The tests must reproduce malformed and duplicate-message cases without accessing production data or depending on an external project. Which approach best supports those requirements?

**Select ONE answer.**

**A.** Send randomly generated bytes to the production subscription until an error occurs.

**B.** Use the Pub/Sub emulator with synthetic fixtures covering valid, malformed, and duplicate messages.

**C.** Replay unmodified production payment messages into the local test environment.

**D.** Replace the subscriber with a mock that always reports success and skip message parsing.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 36

A GKE container sometimes needs two minutes to initialize. Its liveness check is useful for detecting deadlocks after startup, but currently restarts the container before initialization finishes. You want to allow startup time without slowing steady-state deadlock detection. Which probe configuration should you add?

**Select ONE answer.**

**A.** A readiness probe alone, leaving the failing liveness timing unchanged.

**B.** A startup probe with a sufficient startup budget, while preserving the normal liveness check.

**C.** A PodDisruptionBudget that prevents liveness-triggered restarts.

**D.** A much slower liveness check that applies throughout the entire container lifetime.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 37

A Cloud Run compliance service checks the names of newly created Cloud Storage buckets. It should run automatically after bucket creation, without polling. IAM and the event delivery prerequisites can be configured. Which event route matches bucket creation rather than uploads of objects into existing buckets?

**Select ONE answer.**

**A.** Use only a direct object-finalized trigger and assume it also fires whenever an empty bucket is created.

**B.** Configure a Cloud Run CPU alert as the notification mechanism for bucket creation.

**C.** Schedule a periodic list operation and compare bucket names once per day.

**D.** Use an Eventarc Cloud Audit Logs trigger filtered for the Cloud Storage bucket-creation API method.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 38

A Go service on GKE uses unexpectedly high CPU and memory under ordinary traffic. You need to identify expensive functions and allocation paths inside the running application, rather than measure latency between services. Which tool and evidence best match this investigation?

**Select ONE answer.**

**A.** Use only uptime checks to infer the functions allocating memory.

**B.** Read only load balancer access logs and group requests by status code.

**C.** Use only Cloud Trace spans around remote HTTP calls.

**D.** Instrument the supported Go application with Cloud Profiler and inspect CPU and heap profiles.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 39

An API invokes payment, shipping, and inventory services. Users report occasional slow responses, but aggregate CPU metrics look normal. You need to identify which outgoing operation consumes the request time. What instrumentation provides the most useful evidence?

**Select ONE answer.**

**A.** Increase the logging severity of every message without adding timing or correlation information.

**B.** Add a readiness probe and use its success rate as the duration of every outgoing call.

**C.** Collect only node-level CPU metrics and infer which external API is slow.

**D.** Add OpenTelemetry spans around outgoing calls and inspect the resulting distributed traces in Cloud Trace.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 40

Two application teams share a GKE cluster. Team B needs to deploy ordinary workloads for an integration, but it must not change Team A's Deployments or Services. No project-wide administrative role is required. Which access configuration provides the requested control with the least unnecessary privilege?

**Select ONE answer.**

**A.** Grant Team B Project Editor and ask it to use a separate namespace.

**B.** Grant Team B Kubernetes cluster-admin and distinguish its resources with labels.

**C.** Create a namespace for Team B and bind suitable Kubernetes workload-management permissions within that namespace.

**D.** Give Team B project Viewer and rely on that role to authorize creating Deployments.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 5 — Sorular 41–50

### Question 41

A GKE API is exposed to external partners. Requests must pass OAuth token validation and API-specific authorization before reaching the backend. The public endpoint also needs managed protection against common web exploits and volumetric attacks. Which architecture covers both requirements?

**Select ONE answer.**

**A.** Use Cloud Armor alone and treat every request that passes its WAF rules as an authenticated partner request.

**B.** Place Apigee on an ingress path protected by an external Application Load Balancer and Cloud Armor, and prevent backend bypass.

**C.** Use Apigee authentication but expose a second unrestricted public path directly to the GKE backend.

**D.** Expose an Istio ingress gateway and rely only on Kubernetes NetworkPolicy for OAuth validation and WAF protection.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 42

An application project and a database project belong to the same organization. A new private-IP AlloyDB deployment is being planned. The teams must retain separate project ownership but are permitted to use a centrally managed network. Which design provides private reachability without relying on the Auth Proxy to create a network path?

**Select ONE answer.**

**A.** Move all application resources into the database project and grant its developers Project Editor.

**B.** Attach both service projects to an approved Shared VPC and configure AlloyDB private connectivity in that network.

**C.** Keep the networks disconnected and run the AlloyDB Auth Proxy beside the application.

**D.** Keep the networks disconnected and give the application service account AlloyDB Client.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 43

GKE workers consume one Pub/Sub subscription. They spend much of their time waiting for downstream I/O, so CPU usage stays low even when the backlog grows. More worker replicas improve throughput, and node capacity is available. Which autoscaling signal best matches the processing demand?

**Select ONE answer.**

**A.** Use VPA recommendations as the mechanism for creating more worker replicas.

**B.** Configure HPA with an appropriate external Pub/Sub backlog metric.

**C.** Enable only cluster node autoscaling and expect it to increase the Deployment replica count.

**D.** Configure HPA to increase replicas only when CPU utilization reaches 90 percent.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 44

A Cloud Run service has a healthy production revision. A new revision must be tested with a small fraction of live traffic before wider rollout, and you want to use native revision management. What is the safest sequence for introducing the new revision?

**Select ONE answer.**

**A.** Deploy without immediately assigning traffic, allocate a small percentage, evaluate signals, and increase gradually.

**B.** Delete the current revision before deploying the new one to prevent version overlap.

**C.** Deploy to 100 percent of traffic and rely on rollback only after all users are exposed.

**D.** Create a second DNS name and assume DNS automatically sends a controlled percentage to each revision.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 45

Several replicas of a legacy service must read and update files on the same filesystem. You are moving the service to GKE, and changing its file operations to an object-storage API is out of scope. The existing service uses NFS and requires shared writable access. Which storage approach minimizes application changes?

**Select ONE answer.**

**A.** Use a Filestore NFS share through an appropriate GKE PersistentVolume configuration.

**B.** Give each replica a different Persistent Disk and assume writes become visible to other replicas.

**C.** Mount a Cloud Storage bucket and assume it provides every NFS filesystem behavior unchanged.

**D.** Put the writable files in a ConfigMap and mount it in every Pod.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 46

A Bigtable table stores account activity. Reads usually request a time interval for one account, and writes are spread across many active accounts. Each event has an account ID and a fixed-width timestamp. Which row-key ordering best supports these reads while avoiding a single global timestamp-leading write hotspot?

**Select ONE answer.**

**A.** Use account ID followed by the fixed-width timestamp and an event disambiguator if required.

**B.** Use timestamp followed by account ID for every event.

**C.** Use account ID alone, overwriting its row each time a new event arrives.

**D.** Use a random UUID alone and scan the whole table for account history.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 47

Several commits must run Spanner performance tests concurrently. You need comparable latency measurements without the test runs competing for the same Spanner compute capacity. The budget permits temporary managed instances in an existing test project. Which setup is most appropriate?

**Select ONE answer.**

**A.** Use the Spanner emulator as a substitute for production-service latency measurements.

**B.** Run every test against the production instance after truncating its tables.

**C.** Provision an equivalent isolated Spanner instance per run, load controlled test data, and remove it after testing.

**D.** Create a separate database per run on one shared instance and assume compute is isolated.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 48

A developer must test a PostgreSQL client against a staging Cloud SQL instance from a workstation. Approved network reachability already exists. The connection should use IAM-authorized, encrypted transport without manually managing client certificates. Database credentials and grants are handled separately. What should the developer run locally?

**Select ONE answer.**

**A.** Run Cloud SQL Auth Proxy with an authorized identity and point the application at its local listener.

**B.** Use the Cloud SQL Admin REST API as the PostgreSQL query endpoint.

**C.** Connect to a newly created local PostgreSQL database and assume it contains current staging data.

**D.** Grant Cloud SQL Editor and connect through an unencrypted raw connection without a proxy.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 49

You are deploying a stateful service on GKE. Each replica needs a stable ordinal network identity and its own persistent volume that can be reattached when that replica's Pod is replaced. Which controller and storage pattern best express those requirements?

**Select ONE answer.**

**A.** Use a Deployment whose replicas all write to one emptyDir volume.

**B.** Use a Deployment with random Pod names and assume a ClusterIP Service gives each replica a stable identity.

**C.** Use a DaemonSet and identify each replica only by its current Pod IP.

**D.** Use a StatefulSet with the required governing Service and volumeClaimTemplates.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 50

You successfully retrieve credentials for a GKE cluster from Cloud Shell. Subsequent kubectl requests time out. The cluster uses a public control-plane endpoint restricted by authorized networks, and Cloud Shell's current public IP is outside those ranges. What is the most direct correction?

**Select ONE answer.**

**A.** Run get-credentials repeatedly until it creates a network route.

**B.** Authorize the approved Cloud Shell source IP for the control-plane endpoint, following the network access policy.

**C.** Grant the caller cluster-admin while leaving the authorized network ranges unchanged.

**D.** Change the application Service from ClusterIP to LoadBalancer.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---
