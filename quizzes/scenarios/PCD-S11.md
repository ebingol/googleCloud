# PCD-S11 — 50 soruluk karma sınav

**120 dakika çalışma hedefi · 50 soru · 47 tek seçim + 3 çift seçim.**

1 Ekim 2026. S10'dan biraz daha zor hedeflenmiştir: yakın alternatifler, ek belirleyici koşullar ve servisler arası sınırlar. Özgün pratik sorularıdır; gerçek sınavla doğrulanmış zorluk eşdeğeri değildir.

[Güncel resmî exam guide](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) dağılımına göre:

| Ana alan | Rehber ağırlığı | Soru |
|---|---:|---:|
| Tasarım: ölçeklenebilir, güvenli, güvenilir uygulamalar | ~%32 | 16 |
| Geliştirme ve test | ~%23 | 12 |
| Deployment yapılandırması | ~%24 | 12 |
| Google Cloud servisleriyle entegrasyon | ~%21 | 10 |

50 soruda %23 ve %21 sırasıyla 11,5 ve 10,5 eder; eşit yuvarlama payı geliştirme/test alanına verildi. Alt başlıkların resmî ayrı yüzdeleri yoktur; konular soru sırasına karıştırılmıştır. Bu set 11 numaralı alt başlığı örnekler, rehberdeki her ürün/özelliği tek tek ölçmez.

- **Q6, Q19 ve Q21: TWO.** Diğer bütün sorular: ONE.
- İlk turda anahtarı açma. Cevapları `1-b, 2-d, 6-a+b` biçiminde gönderebilirsin.
- Başlangıç/bitiş ve mola sürelerini kaydet. 120. dakikada mevcut cevapları sabitle; devam edersen ek süreyi belirt. Bu kişisel deneme hedefidir.
- İstersen 10'luk bölümler kullan; bölümler arasında açıklama alırsan kesintisiz bağımsız denemeden ayrı kaydedilir.
- E/K/T güven ve kısa gerekçe isteğe bağlı. Bilmediğin teknik kavramı ayrıca işaretleyebilirsin.

Başlangıç: ____ · 120. dakika ulaşılan soru: ____ · Bitiş: ____ · Molalar / ek süre: ____


## Bölüm 1 — Sorular 1–10

### Question 01

A catalog API on Cloud Run uses Memorystore as a cache in front of Cloud SQL. After a popular cache entry expires, hundreds of instances simultaneously query the database for the same product. Normal cache hits are fast, and the database has enough capacity for one refresh but not for every concurrent miss. Product descriptions may be served up to thirty seconds stale; inventory decisions use a separate authoritative path. The team wants to prevent synchronized refreshes without making a failed refresher block requests indefinitely. Which design best addresses this specific overload pattern?

**Select ONE answer.**

**A.** Use bounded per-key refresh coordination and serve acceptable stale values while one caller refreshes, with recovery after lock expiry.

**B.** Increase all entry TTLs and let every waiting caller refresh independently when those entries finally expire.

**C.** Cache inventory decisions with the descriptions so every database call can be removed.

**D.** Use per-key refresh locks without any lease expiry and wait indefinitely for the lock holder before responding.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 02

A developer uses the Firestore emulator for repository tests and user ADC for an unrelated staging diagnostic tool. Both tools are launched from the same terminal, where FIRESTORE_EMULATOR_HOST remains exported. The staging diagnostic now reports missing documents even though the documents exist in the hosted staging database. Its project ID and credentials are correct, and logs show requests reaching localhost. The team wants each tool to use its intended endpoint without deleting either dataset or broadening staging access. What is the most appropriate environment configuration?

**Select ONE answer.**

**A.** Change the diagnostic project ID to production while keeping the localhost endpoint.

**B.** Restart the emulator with a copy of all staging documents and treat it as the hosted diagnostic.

**C.** Grant the user a broader role in staging and keep the shared emulator variable.

**D.** Scope the emulator variable to the test process and remove it from the hosted staging diagnostic environment.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 03

A Cloud Run API has a maximum pool size of ten Cloud SQL connections per instance. During a planned rollout, the capacity model allows up to twelve instances of the old revision and twelve of the new revision to exist concurrently. Other applications reserve forty connections, and the database connection budget is two hundred. Tests show that a pool size of six meets request latency requirements, but lowering request concurrency alone does not change the configured pool maximum. Using the stated worst-case model, which change fits the connection budget while preserving the planned rollout capacity?

**Select ONE answer.**

**A.** Set each instance pool maximum to eight and retain the twenty-four-instance overlap model.

**B.** Set maximum request concurrency to six while leaving each connection pool maximum at ten.

**C.** Budget twelve instances at pool size ten plus forty reserved connections, treating the new revision as replacing old instances immediately.

**D.** Set each instance pool maximum to six, budget for both revisions, and monitor actual connections during rollout.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 04

A worker downloads a large Cloud Storage object in several byte ranges and combines them into one local file. Another application can replace the object under the same name during the download. The current worker requests each range by name only, so a completed file can contain bytes from different object generations. The worker may restart the whole transfer if its selected generation is unavailable, but must never silently combine versions. Object metadata includes a generation identifier, and the client supports generation-specific reads. Which approach best preserves the required consistency?

**Select ONE answer.**

**A.** Increase the delay between range requests so replacement writes are less likely to overlap.

**B.** Resolve the latest generation separately before each range and combine all successful responses.

**C.** Choose one generation before downloading and use it for every range and retry; restart deliberately if that generation becomes unavailable.

**D.** Compare object names after downloading, because equal names prove equal contents.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 05

A team uses Cloud Run traffic splitting to compare two recommendation algorithms. The experiment requires each authenticated customer to remain in the same experiment group across devices and across replacement of application instances. Sessions already use durable shared storage. An engineer suggests enabling session affinity and relying on a 50/50 traffic split to define permanent customer groups. Both revisions implement the same API, and the team can place assignment logic before selecting an algorithm. Which design most directly provides the required stable experiment membership while retaining ordinary autoscaling?

**Select ONE answer.**

**A.** Use session affinity as the only assignment mechanism and let replacement instances choose a new group.

**B.** Use a browser-local experiment cookie and assume that it provides the same assignment on every customer device.

**C.** Store or deterministically derive assignment from the authenticated customer identity and route execution according to that assignment.

**D.** Assign groups using instance-local random choices and preserve those choices until each instance is replaced.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 06

A Cloud Build pipeline runs two independent release checks after an image is built. The publish step correctly waits for both check IDs, and all steps refer to the same image digest. Recently, a failing security check still allowed publication. Investigation shows that its step uses allowFailure: true. The team wants to preserve parallel execution of the checks, retain useful diagnostics from failed runs, and prevent publishing an artifact when either required check fails. Which TWO changes or retained settings together implement the intended release gate?

**Select TWO answers.**

**A.** Replace digest references with a shared mutable release tag.

**B.** Treat waiting for the security step as sufficient even when its failure is allowed.

**C.** Start publication with waitFor: ['-'] and inspect the reports after publication.

**D.** Retain publish dependencies on both required check IDs.

**E.** Require the security check to fail the build on a failing result rather than allowing its failure.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 07

A GKE Deployment has four healthy replicas and a rolling update configured with maxUnavailable: 0 and maxSurge: 1. The new replica remains Pending because every node is full according to resource requests. Existing replicas are serving normally; image access, probes, and the Deployment selector are correct. The business requires four available replicas throughout the rollout, and there is budget and quota to add node capacity. Lowering resource requests below measured needs is prohibited. Which action advances the rollout while preserving its availability constraint?

**Select ONE answer.**

**A.** Add suitable schedulable node capacity for the surge replica, keeping the stated rollout availability settings.

**B.** Set maxUnavailable to one and remove an old healthy replica to make room.

**C.** Reduce CPU requests below measured needs to fit the surge replica while retaining the same application load.

**D.** Set maxSurge to two and keep the node pool full, expecting the additional Pending replica to free resources.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 08

An existing PostgreSQL application must continue after losing a zone in its current region. The required database design must preserve acknowledged transactions during that zonal failure, use managed failover, and avoid rewriting relational queries. The organization has separately accepted that a complete regional outage requires a different disaster-recovery plan; this task does not need to solve that broader failure scope. A same-region asynchronous read replica is available, but its replication can lag. Which database configuration best satisfies the stated availability and compatibility requirements?

**Select ONE answer.**

**A.** Use the asynchronous read replica and document that managed replication guarantees zero acknowledged-write loss.

**B.** Use a standalone zonal primary with a same-region asynchronous replica and rely on replica promotion for guaranteed zero-loss zonal recovery.

**C.** Use frequent scheduled backups of a standalone zonal primary and treat restore as the required managed failover.

**D.** Use Cloud SQL regional HA with its synchronous standby and managed failover, and handle connection recovery in the application.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 09

An ordering-enabled Pub/Sub subscription uses customer IDs as ordering keys. One customer's message handler repeatedly fails, and later messages for that customer are redelivered or delayed. Messages for unrelated ordering keys continue normally. The business still requires order within each customer, so assigning a random key to every message is unacceptable. Processing is idempotent, and the team can persist problematic events for investigation under an explicit business-approved failure policy. Which change best addresses the blocking failure without sacrificing the required per-customer ordering contract?

**Select ONE answer.**

**A.** Acknowledge every message before processing and reconstruct any missing operations from ordinary logs.

**B.** Pause and resume the affected customer's delivery without correcting the permanently failing event or changing its approved disposition.

**C.** Identify and resolve or durably handle the failing event under the approved policy, then acknowledge only that completed disposition.

**D.** Give every message a unique ordering key so the subscriber can process the affected customer's later messages immediately.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 10

An AI coding assistant generates tests for a money-transfer function. The specification requires total balance conservation and forbids overdrawing the source account. The generated expected destination balance is calculated by calling the same helper used by the production function, so a shared arithmetic defect makes both implementation and tests agree. External dependencies are already controlled, and test runs are deterministic. The team wants additional evidence that the implementation follows the business rules across many valid inputs. Which testing change most directly removes the circular oracle?

**Select ONE answer.**

**A.** Run the same shared helper twice and require its two results to match.

**B.** Derive assertions independently from conservation and overdraft rules, and exercise boundaries and varied valid inputs against the real function.

**C.** Replace independent rule assertions with exact snapshots of the current implementation outputs.

**D.** Generate many inputs but compute every expected result with the same helper used by the implementation.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---


## Bölüm 2 — Sorular 11–20

### Question 11

An Apigee proxy authenticates partners and enforces each partner's daily contractual request allowance. One partner remains below that daily quota but sends its entire allowance in a short burst, overloading the backend. Other partners must retain their existing contractual allowances, and legitimate steady traffic from the affected partner must remain possible. The team wants a control for short-term arrival spikes while keeping daily usage accounting. Which policy combination best matches both requirements without confusing an interval allowance with smoothing of sudden traffic?

**Select ONE answer.**

**A.** Reduce the daily quota for every partner until any possible burst fits the backend.

**B.** Retain per-partner Quota and add appropriately scoped SpikeArrest protection for burst behavior.

**C.** Replace the daily Quota with a short-term SpikeArrest policy and treat its burst control as the contractual daily allowance.

**D.** Keep only the daily Quota and increase backend capacity without adding a control for short-term arrival spikes.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 12

A Cloud Run revision reads a pinned Secret Manager version through an environment variable at instance startup. Existing instances continue serving traffic, but newly started instances fail after the runtime service account's Secret Accessor permission is removed. The secret version remains enabled, application code is unchanged, and logs identify a permission failure while resolving the secret. Security policy allows this service to read that one secret, but prohibits granting the deployer broader data access. What is the most appropriate corrective action?

**Select ONE answer.**

**A.** Change the pinned version to latest without repairing the runtime account's secret access.

**B.** Restore Secret Accessor for the revision's runtime service account on the required secret and verify that new instances start.

**C.** Grant Secret Accessor only to the human deployer, because deployment credentials are reused by every instance.

**D.** Increase minimum instances and treat surviving old instances as proof that the permission is unnecessary.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 13

A database credential is stored as version 7 in Secret Manager and pinned by the current Cloud Run revision. The team creates version 8 containing a new credential, and the database temporarily accepts both credentials. A tested candidate revision pins version 8, while rollback to the old revision must remain possible until the observation period ends. No credential compromise is suspected. Which rollout sequence best rotates the credential without breaking either newly started old instances or the explicitly required rollback path?

**Select ONE answer.**

**A.** Test and migrate to the version-8 revision, preserve both working credentials through the rollback window, then retire version 7 and its database credential.

**B.** Disable version 7 immediately after creating version 8, before any traffic migration.

**C.** Change version 7's payload in place so old and new revisions automatically share the new password.

**D.** Make the database accept only the new credential before testing the candidate revision.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 14

A team builds a custom Cloud Workstations image that includes an approved compiler under /opt/tools and a starter repository under /home/user/project. New workstations use the correct image and show the compiler, but the starter repository is missing. Their configuration attaches persistent home disks, and no user data may be discarded. The team wants to distribute the starter files while preserving each developer's existing work. Which change best accounts for the difference between image files and the persistent home mount?

**Select ONE answer.**

**A.** Keep starter assets outside /home in the image and copy missing files into the mounted home through a safe startup script.

**B.** Restart each workstation using the same image and persistent home, expecting the hidden image files to appear automatically.

**C.** Delete every developer's home disk so the files baked into the image become authoritative.

**D.** Put the starter repository in /home during each image rebuild and retain all existing persistent home mounts unchanged.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 15

A service makes idempotent Cloud Storage metadata reads. Its client currently retries every unsuccessful response with backoff. During an incident, requests using an invalid field selector repeatedly receive HTTP 400, while separate valid requests occasionally receive HTTP 503. The overall request deadline is already propagated, and the team can correct the selector. It wants to preserve recovery from transient service failures without wasting retry budgets on unchanged invalid requests. Which behavior most directly addresses both observed error categories?

**Select ONE answer.**

**A.** Retry HTTP 400 longer than HTTP 503 because invalid selectors can become valid after waiting.

**B.** Stop retrying unchanged invalid requests and correct the selector; apply bounded backoff to eligible transient failures within the deadline.

**C.** Extend the user deadline indefinitely so both error categories can eventually succeed.

**D.** Disable retries for all errors because one request type has a permanent defect.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 16

A GKE API keeps running normally during a short database failover and reconnects automatically once the database is available. While disconnected, it cannot serve valid requests, but restarting the process does not accelerate recovery. The current liveness probe checks the database and causes repeated container restarts during the outage. Startup behavior is healthy, and other replicas exhibit the same dependency failure. Which probe design most directly avoids unnecessary restart cycles while preventing new traffic from reaching replicas that cannot currently serve requests?

**Select ONE answer.**

**A.** Use readiness for current serving capability and a process-health liveness check that detects failures requiring restart.

**B.** Remove the database check from both probes and report readiness success even while requests cannot be served.

**C.** Make both readiness and liveness depend on the database, keeping fast liveness failures during the failover.

**D.** Lengthen the startup probe so it governs every database outage after initialization.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 17

A Cloud SQL PostgreSQL database serves latency-sensitive order transactions. Analysts now run large historical aggregations on that primary, causing checkout latency spikes. Reports may be refreshed once a day, original export files must remain available for reprocessing, and the team prefers managed analytical infrastructure. The operational schema and transaction code should remain unchanged. Which design best removes the historical scan workload from the transactional primary while respecting the permitted data freshness and source-retention requirements?

**Select ONE answer.**

**A.** Run the same historical scans inside checkout transactions to make all reports immediately consistent.

**B.** Replace every order transaction with a BigQuery query to eliminate Cloud SQL.

**C.** Export suitable batches to retained Cloud Storage files and load partitioned BigQuery tables for the daily reports.

**D.** Copy the only historical dataset into Memorystore and remove retained source files.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 18

A container candidate has validated Cloud Build provenance tied to its exact digest and has passed functional integration tests. Artifact Analysis then reports a fixable high-severity vulnerability in a runtime library. Release policy requires trusted build origin, functional success, and no unresolved vulnerability of that severity. The builder identity is approved, and the report is confirmed to describe a library actually present in the final image. Which next step best satisfies the complete policy before releasing the candidate?

**Select ONE answer.**

**A.** Update the affected runtime dependency, rebuild, rescan, and validate tests and provenance for the resulting release digest.

**B.** Release immediately because validated provenance proves that every dependency is secure.

**C.** Patch the deployed filesystem after release and reuse the original digest-bound test and provenance evidence.

**D.** Keep the tested digest and wait for the next scheduled rebuild while publishing the current vulnerable candidate.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 19

An Eventarc trigger targets a private Cloud Run service. Delivery logs show HTTP 403 before the handler runs. The trigger uses delivery account event-delivery, while the service runs as processing-runtime. All Eventarc prerequisites and token configuration are correct; event-delivery lacks permission to invoke the service. Once invoked, the handler must read a particular Cloud Storage bucket, and processing-runtime currently lacks that access. Neither account needs administrative roles. Which TWO grants address the two boundaries with the intended identities?

**Select TWO answers.**

**A.** Grant processing-runtime Storage Object Viewer on the required bucket.

**B.** Grant event-delivery Cloud Run Invoker on the destination service.

**C.** Grant processing-runtime Cloud Run Invoker and assume the trigger inherits that identity.

**D.** Grant event-delivery Storage Object Viewer so the handler can use delivery credentials automatically.

**E.** Grant event-delivery Owner on the service project.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 20

A frontend publishes work to Pub/Sub and returns immediately. Workers process the messages later, and each component creates valid local spans, but the tracing view shows unrelated frontend and worker traces. Message IDs are recorded, yet no trace context is carried in message attributes. The team wants to investigate one request's asynchronous processing path without pretending queue wait is an ordinary synchronous network call. The instrumentation library supports context injection, extraction, and span links. Which change best supplies the missing correlation?

**Select ONE answer.**

**A.** Use one shared trace ID for all messages handled during an hour.

**B.** Record only the Pub/Sub message ID in logs and assume the trace backend can infer missing span context automatically.

**C.** Inject trace context into message attributes, extract it at processing, and model the worker span using an appropriate parent or link relationship.

**D.** Start an unrelated root trace for every worker and rely only on increasing trace sampling to create the causal links.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---


## Bölüm 3 — Sorular 21–30

### Question 21

A GKE workload has default-deny egress enforced by a supported network plugin. A new allow policy permits TCP connections to selected database Pods on port 5432, and database ingress already allows this client. Connecting by the verified database IP succeeds, but connecting by its Kubernetes Service name fails. Diagnostics show blocked DNS queries. The cluster's DNS endpoint and required UDP and TCP port 53 rules are known. Which TWO actions preserve least privilege while restoring name-based database access?

**Select TWO answers.**

**A.** Allow all egress to every destination because service discovery cannot work with NetworkPolicy.

**B.** Remove database ingress restrictions so DNS answers can traverse the database port.

**C.** Grant the Pod service account database IAM Administrator to enable DNS packets.

**D.** Retain the narrowly scoped database egress allowance on port 5432.

**E.** Add narrowly scoped egress for the actual cluster DNS endpoint on the required DNS transports.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 22

A team deploys a supported application from source to Cloud Run. It expects Google Cloud buildpacks to select the language runtime, but build logs show a Docker build using an obsolete base image. The submitted source root contains an old Dockerfile left from a previous experiment. Application entry points and dependency files are otherwise valid, and the team has decided to use the supported buildpack path rather than maintain a custom container recipe. Which change most directly aligns the source build with that decision?

**Select ONE answer.**

**A.** Grant the runtime service account Artifact Registry Writer so it can choose buildpacks.

**B.** Add a production environment variable naming the language after deployment completes.

**C.** Update minimum instances because Cloud Run selects the builder from runtime scaling settings.

**D.** Remove the unintended Dockerfile from the submitted source root and redeploy through the supported source build path.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 23

A GKE HPA has scaled an API Deployment from six to twelve replicas. Six additional Pods remain Pending with events stating insufficient CPU on every eligible node. Their requests are based on measured needs, metrics are healthy, and maxReplicas is twenty. The node pool has reached its current maximum size, although project quota and budget permit growth. There are no affinity or taint conflicts. Which configuration change most directly makes the requested additional replicas schedulable without misrepresenting application resource needs?

**Select ONE answer.**

**A.** Remove CPU requests so the scheduler no longer accounts for the measured requirement.

**B.** Increase only HPA maxReplicas from twenty to forty.

**C.** Reduce application replica demand until all Pods fit, treating the capacity shortage as a completed response to current load.

**D.** Increase the appropriate node pool autoscaling maximum and verify that cluster autoscaling can provision suitable capacity.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 24

A backend issues a short-lived signed URL for a private Cloud Storage document after authenticating a customer. Product management now requires every download to check the current customer entitlement and prevents access by anyone who merely receives a forwarded link. A controlled test confirms that another browser can use the unexpired signed URL. The bucket must stay private, and the application already has an authenticated download endpoint. Which access design best satisfies the stronger requirement without assuming that a signed URL establishes the downloader's identity?

**Select ONE answer.**

**A.** Keep signed URLs and add a customer ID to the query string without requiring the downloader to authenticate.

**B.** Authorize each download at the authenticated backend and stream the permitted object rather than expose a bearer download URL.

**C.** Shorten signed URL expiry to one minute and treat possession as proof of customer identity.

**D.** Continue issuing signed URLs after one entitlement check and require the browser to check entitlement before each download.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 25

A Firestore transaction reads an account limit and records a reservation only if the remaining allowance is sufficient. The client may rerun the transaction callback after a concurrent update. A proposed optimization reads the allowance once outside the transaction and reuses that value in every callback attempt. No external side effects occur inside the callback, and contention is expected during peak traffic. The reservation must respect the latest transactionally validated limit rather than a stale precheck. Which implementation best preserves this correctness requirement?

**Select ONE answer.**

**A.** Read the decision-dependent document inside each transaction attempt and base writes on that attempt's validated reads.

**B.** Use an atomic write batch with the cached allowance check performed outside the batch.

**C.** Read the allowance once inside the first attempt and retain that value when later transaction callbacks rerun.

**D.** Reuse the pre-read allowance but increase the maximum retry count.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 26

A developer asks Gemini Code Assist to implement a client integration using the repository's pinned SDK version. The assistant repeatedly suggests methods that exist only in a newer SDK, even though code compiles with the installed older version. The repository contains the lockfile, a wrapper interface, and working examples. No cloud access is needed to resolve the mismatch. The developer wants a reviewable patch that respects the current dependency contract. Which action most directly improves the implementation process?

**Select ONE answer.**

**A.** Provide the pinned version, wrapper, and working examples as context; validate suggested calls against that version and run relevant checks.

**B.** Remove the lockfile and accept whichever version makes the generated code compile first.

**C.** Grant the assistant production administrator access so it can discover newer SDK methods.

**D.** Suppress compiler diagnostics because the assistant's method names are the authoritative API contract.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 27

A Cloud Run candidate revision has a tag used by a small internal client group. After a regression, the team routes all normal service traffic to the stable revision. Ordinary clients recover, but the internal group continues seeing the candidate's error. Their configuration points directly to the tagged revision URL, not the normal service URL. The candidate must remain available for investigation, while the internal group should immediately use the stable service path. Which change most directly completes the operational rollback for that group?

**Select ONE answer.**

**A.** Restart the tagged candidate while retaining its tag and assume normal service percentages govern the internal clients too.

**B.** Remove only the candidate tag while leaving internal clients configured with the obsolete tagged URL.

**C.** Update the internal clients to the normal service URL or an explicitly stable target, and verify their effective destination.

**D.** Keep the internal clients on the tagged URL and route all normal service traffic to stable again.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 28

An order event must independently reach analytics and fraud detection. A separate shipping integration calls one HTTP partner endpoint that tolerates only a controlled number of concurrent requests and supports delayed retries. Each consumer needs its own progress, and a slow partner must not prevent analytics from consuming new events. The team can build a small adapter for shipping. Which architecture best combines independent event consumption with explicit control over the partner's HTTP dispatch workload?

**Select ONE answer.**

**A.** Use one shared Pub/Sub subscription for analytics, fraud, and shipping so each receives every event independently.

**B.** Use separate Pub/Sub subscriptions for independent consumers, with the shipping adapter creating idempotent Cloud Tasks for controlled HTTP dispatch.

**C.** Call the shipping partner synchronously before publishing each event, so partner delays govern every consumer.

**D.** Create one Cloud Tasks queue and let unrelated consumers compete for its tasks as a broadcast mechanism.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 29

A service lists Cloud Storage objects from a large bucket and needs only each object's name and size. It already follows pagination correctly when using full responses. To reduce response size, a new fields selector retains only object fields and accidentally omits nextPageToken. The service now stops after the first page although more objects exist. The query itself is unchanged, and all pages must still be processed. Which correction restores completeness while retaining the intended reduction in returned data?

**Select ONE answer.**

**A.** Increase the first-page size and stop whenever the partial response has no token, even though the selector omits tokens.

**B.** Keep the selector and repeatedly issue the initial list request until no new names appear.

**C.** Include the token only in the request and exclude it from every response to minimize payload size.

**D.** Include the continuation token along with the required object fields and keep following it until it is absent.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 30

Firestore emulator tests pass for a backend's data logic. A release review also requires evidence that the deployed Cloud Run runtime identity can read the intended staging database while remaining denied access to a separate restricted project. The current cloud smoke test runs from a developer laptop with broad user ADC and therefore succeeds even when the runtime service account has missing access. The team can invoke a deployed staging endpoint and inspect denied operations. Which test change most directly measures the identity used by the real application?

**Select ONE answer.**

**A.** Grant the runtime account the developer's broad roles, then keep testing only from the laptop.

**B.** Treat the passing emulator suite as proof of all deployed IAM permissions.

**C.** Change only the laptop's active project and assume user ADC becomes the runtime account.

**D.** Run controlled staging integration calls through the deployed service under its configured runtime identity, including expected allowed and denied operations.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---


## Bölüm 4 — Sorular 31–40

### Question 31

An application directly encrypts records with a symmetric Cloud KMS key. After rotation, new records decrypt successfully, but old records fail because an operator disabled the earlier key version. That version has not been destroyed, no compromise is suspected, and the application still has the required decrypt permission. The new primary is healthy. The team needs to restore old-record access before performing a planned re-encryption migration. Which action most directly restores access to the existing ciphertext?

**Select ONE answer.**

**A.** Grant Encrypt permission alone on the new primary and retry decrypting old records.

**B.** Enable the required earlier key version, restore decryption, and migrate dependent records before retiring it again.

**C.** Re-encrypt the old ciphertext bytes as if they were plaintext and delete the earlier version.

**D.** Rotate the key again so the old ciphertext automatically refers to the newest primary.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 32

A GKE service uses a ConfigMap projected as ordinary mounted files, without subPath. The files are observed to update after a configuration change, but the application's behavior remains unchanged. Investigation shows that the process reads the files only once during startup and keeps parsed values in memory. The team requires configuration changes to affect running instances without replacing Pods, and the application can implement a safe reload mechanism. Which change addresses the remaining gap between Kubernetes projection and application behavior?

**Select ONE answer.**

**A.** Move the values to environment variables while retaining running Pods and the startup-only parser.

**B.** Change the mount to subPath and retain the startup-only parser, avoiding application reload code.

**C.** Add a safe application reload or file reread mechanism for the updated projected configuration.

**D.** Keep the projected files and shorten their refresh interval, leaving the process memory snapshot unchanged.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 33

A Bigtable application stores measurements for millions of devices. The dominant query reads one device's measurements over a contiguous time interval; writes are distributed fairly evenly across devices. The current row key begins with a timestamp, creating concentrated writes and forcing device queries to examine broad ranges. No individual device dominates total traffic. The team wants to spread writes while preserving efficient device-specific range scans, and it does not want to scan all possible random prefixes for every request. Which row-key design best matches these access patterns?

**Select ONE answer.**

**A.** Use a well-distributed device identifier prefix followed by an appropriately encoded timestamp.

**B.** Place every measurement for every device in one growing row.

**C.** Keep the timestamp first and increase only the application connection pool.

**D.** Use a fully random prefix per measurement and search all random prefixes for every device query.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 34

A multi-stage Dockerfile compiles an application in a builder stage and copies its output into a smaller runtime stage. Artifact Analysis reports a vulnerable operating-system library from the final runtime base. An engineer updates only the builder base and rebuilds; the final image still contains the same affected runtime package. The scanner result is confirmed, and a patched compatible runtime base is available. Which change most directly removes the reported package vulnerability while retaining the useful multi-stage structure?

**Select ONE answer.**

**A.** Copy the entire newer builder filesystem into the runtime image without checking runtime dependencies.

**B.** Rebuild with the unchanged runtime base and clear all Docker cache, without changing the affected package version.

**C.** Update the final runtime base or affected runtime package, rebuild, and verify the resulting image with scanning and relevant runtime tests.

**D.** Update only the builder's package set and preserve the final runtime stage unchanged.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 35

A Cloud Run application writes ERROR-severity JSON entries to Cloud Logging when exceptions occur. The logs are visible, but expected events do not appear in Error Reporting. The payload contains only a generic message and a request ID; it omits the exception stack and the supported structured error-event fields. Routing and permissions are confirmed healthy. The team wants useful grouped exception reports while retaining request correlation. Which instrumentation change most directly supplies the missing error-event content?

**Select ONE answer.**

**A.** Increase trace sampling alone, leaving the exception payload unchanged.

**B.** Add service context alone but leave out both supported error-event typing and actual exception information.

**C.** Keep generic ERROR messages and increase their retention, expecting missing exception details to be reconstructed.

**D.** Use a supported Error Reporting integration or structured error event containing the actual exception information and service context; retain request correlation separately.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 36

A Cloud Run service uses a supported bidirectional gRPC method for interactive sessions. HTTP/2 and container protocol settings are verified. Sessions can outlive the configured request timeout, and deployments can also replace instances. The business allows clients to reconnect but requires them to resume from a confirmed sequence number without duplicating committed commands. The team has durable session state and command identifiers. Which client-service design best supports these requirements rather than assuming that one transport connection remains alive indefinitely?

**Select ONE answer.**

**A.** Increase minimum instances and hold resume state only in the memory of the instance handling each stream.

**B.** Extend the configured timeout and retain durable state, but omit reconnect and resume behavior during deployments.

**C.** Use bounded streams with reconnect and durable resume checkpoints, applying idempotent command processing across reconnections.

**D.** Reconnect after failures but assign a new command ID to every replayed command.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 37

A GKE Pod uses Workload Identity Federation for GKE with a dedicated Kubernetes service account. The cluster and metadata configuration are verified, and token acquisition succeeds. A direct grant to the Kubernetes principal is supported for the target API. Reading objects from a bucket in a separate project returns permission denied; no object-read permission has been granted on that bucket or its parent. The team prohibits service-account key files and wants the smallest resource scope. Which action most directly fixes authorization while keeping the existing identity flow?

**Select ONE answer.**

**A.** Grant the Pod's federated Kubernetes principal Storage Object Viewer on the target bucket.

**B.** Create a downloaded service-account key and use it instead of the working federation flow.

**C.** Set the container's active gcloud project to the bucket project and assume this grants object access.

**D.** Grant the human who deployed the Pod project Owner and leave the workload principal unchanged.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 38

A custom backend verifies Firebase ID tokens correctly and derives the caller UID from the verified token. Its database client runs under a legitimate runtime service account. A new endpoint accepts an account ID in the URL, and existing tests only confirm that a signed-in user can read their own account. Reviewers worry that authentication succeeds but account ownership is not enforced. Two synthetic users own different accounts in isolated test data. Which additional test most directly checks the missing security property?

**Select ONE answer.**

**A.** Issue the cross-account request using the backend database administrator rather than the authenticated customer's endpoint path.

**B.** Add more own-account success cases for both users and validate each token signature.

**C.** Call the real endpoint as one authenticated user requesting the other user's account, and assert denial without exposing that account's data.

**D.** Assert that the browser hides the other account's URL, without sending a modified request.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 39

A GKE Deployment uses the image reference app:release. A pipeline publishes a new image under that same tag but makes no change to the Deployment Pod template. Existing Pods continue running the earlier image, and no new ReplicaSet appears. The approved new digest is available and tested. The team requires a reviewable rollout of exactly that artifact, without depending on mutable-tag lookup timing or manually deleting individual Pods. Which deployment change most directly provides that behavior?

**Select ONE answer.**

**A.** Push the same tag again until the Deployment notices the registry update automatically.

**B.** Update only Deployment metadata outside the Pod template, retaining the same mutable image reference.

**C.** Update the Deployment Pod template to the approved digest and monitor the resulting rollout.

**D.** Set imagePullPolicy to Always without changing the Pod template and wait for currently running containers to replace their image.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 40

A Cloud Storage JSON API client batches independent metadata updates. The outer HTTP exchange succeeds, but the multipart response contains successful updates and several individual transient failures. Each update uses a recorded metageneration-match precondition. The API documentation permits batching these operations, and the team must preserve concurrent writers' changes. The current code treats outer success as success for all subrequests. Which response-handling strategy best recovers unfinished updates without turning batching into an assumed atomic transaction?

**Select ONE answer.**

**A.** Inspect each subresponse, retry only eligible unfinished updates with their preconditions, and re-evaluate conflicts.

**B.** Retry the full batch and assume its successful outer response means all updates committed atomically.

**C.** Treat every subrequest as successful whenever the outer HTTP status is successful.

**D.** Retry only failed subrequests, but omit their metageneration preconditions so concurrent updates never block recovery.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---


## Bölüm 5 — Sorular 41–50

### Question 41

A Cloud Storage bucket has a locked ninety-day retention policy and a lifecycle rule requesting deletion at object age thirty days. A thirty-five-day-old object remains present. No object hold exists, and the object's retention expiry is confirmed to be later than the current time. A developer suspects the lifecycle rule is broken and proposes temporarily shortening retention to force cleanup. Compliance requires the locked protection to remain effective. Which explanation and action best fit the configured controls?

**Select ONE answer.**

**A.** Unlock the bucket, shorten retention, and relock it after deleting the object.

**B.** Enable object versioning because version history is the control preventing this object's deletion.

**C.** Retention prevents deletion until expiry; keep the protection and plan cleanup eligibility after retention is satisfied, allowing asynchronous lifecycle processing.

**D.** Lifecycle deletion takes precedence over locked retention, so grant a service account Owner to force it.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 42

A team compares two API revisions using a load generator that sends a new request only after the previous request finishes. The slow revision therefore receives fewer requests per second, and its report excludes time waiting before request submission. Production traffic arrives independently of earlier completions and queues under overload. The team wants a test that evaluates the required arrival rate and user-visible latency, with a safe isolated environment and an explicit resource budget. Which testing approach best measures the production-relevant behavior?

**Select ONE answer.**

**A.** Keep one sequential client and compare only handler execution time, ignoring achieved request rate.

**B.** Replay the same total request count but let completion speed determine the arrival rate for each revision.

**C.** Use the sequential generator and compare latency percentiles without checking the different offered arrival rates.

**D.** Use controlled arrival-rate load within the test budget and measure complete latency and achieved throughput, including queueing and failures.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 43

A Cloud Run source deployment fails before producing its container image. Logs identify the configured Cloud Build service account and show a denied read of a required build-time secret. The application runtime service account already has its own correct production-secret access, and no runtime instance has started. The deployment's human caller has the required deployment permissions. The build-time secret contains a read-only package credential and is approved for this builder. Which permission change most directly fixes the observed stage while preserving the separation of build and runtime identities?

**Select ONE answer.**

**A.** Grant the human deployer broad production database access so the builder inherits it.

**B.** Change the service ingress to public because private ingress prevents secret reads during builds.

**C.** Grant the runtime account project Owner because all source-build steps run as the final application.

**D.** Grant the configured build service account access to the specific build-time secret through the approved secret-injection configuration.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 44

An API is deployed in two regions behind a global load balancer. Each region uses its own disposable Memorystore cache, but both regions depend on one Cloud SQL primary in region A. The team observes that losing region A stops writes from both API regions despite healthy instances in region B. Cache contents can be reconstructed, but acknowledged orders require durable recovery. The business accepts a documented nonzero regional recovery point and a controlled failover procedure. Which design change most directly addresses the remaining regional dependency?

**Select ONE answer.**

**A.** Add a suitable cross-region database recovery strategy with measured lag and tested promotion/reconnection, alongside the existing regional API deployments.

**B.** Replicate only the disposable cache into region B and assume it replaces the order database.

**C.** Increase the number of API instances in region B and leave database recovery unchanged.

**D.** Enable session affinity so region-B requests stop depending on the database.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 45

A service has a 99.9 percent request-success SLO. The dashboard's recent window shows two failures per one thousand valid requests, and all requests use the agreed success definition. An alert should consider how quickly this window consumes the error budget, rather than treating its percentage as a monthly final result. Traffic is sufficient for a meaningful measurement. What does this window's observed error rate imply about error-budget burn, assuming the 99.9 percent target applies to these valid requests?

**Select ONE answer.**

**A.** The service burns at half the allowed error fraction because 99.8 is close to 99.9.

**B.** The service has no budget burn because two failures are fewer than one thousand requests.

**C.** The service burns at twice the allowed error fraction during this window; use the chosen alert windows to decide urgency.

**D.** The monthly SLO is conclusively failed, regardless of every other window's traffic and outcomes.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 46

A GKE application legitimately needs up to eighty seconds to initialize after deployment. Once initialized, a process deadlock should be detected and restarted within roughly twenty seconds. The current liveness probe starts immediately and kills the container before initialization completes. Readiness correctly reports when traffic can be served. The team wants to accommodate initialization without weakening the steady-state liveness response. Which probe configuration best separates those two time requirements?

**Select ONE answer.**

**A.** Set readiness permanently successful until the first eighty seconds have passed.

**B.** Use a startup probe with a sufficient initialization budget, then retain an appropriately short steady-state liveness failure budget.

**C.** Extend the liveness failure budget beyond eighty seconds for both startup and steady-state deadlocks.

**D.** Remove liveness and assume readiness restarts a deadlocked process.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 47

A support backend verifies customer identity and asks a generative model to suggest the account resource needed for a request. Responses use a supported schema and pass JSON validation. One suggestion names another customer's account. The backend's runtime account has legitimate access to multiple customer records, but the caller must access only authorized resources. The model does not execute tools directly, and the application controls every database read. Which boundary best prevents a well-formed model suggestion from becoming an unauthorized data access?

**Select ONE answer.**

**A.** Authorize the proposed resource against the verified caller and allowed operation before performing the read, rejecting unauthorized suggestions.

**B.** Check that the proposed account exists using the backend's runtime credentials and treat existence as caller entitlement.

**C.** Repeat the model request until it names an account from the same tenant, then skip the application's authorization check.

**D.** Accept any account ID that matches the schema because formatting validation establishes ownership.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 48

A Cloud Run API must respond quickly during a predictable morning traffic increase. Load tests show that initialization causes the initial latency spike, while already warm instances meet the target. The application is stateless, supports normal autoscaling, and does not need CPU work between requests. The team accepts paying for a small warm baseline but does not want to reserve peak instance capacity all day. Which configuration approach best addresses the measured startup delay while keeping peak capacity elastic?

**Select ONE answer.**

**A.** Configure a tested small minimum-instance baseline and appropriate autoscaling bounds, validating the morning burst against the latency target.

**B.** Raise only the maximum instance limit while keeping the minimum at zero.

**C.** Set minimum instances equal to the maximum expected peak, regardless of the accepted baseline budget.

**D.** Increase the request timeout and leave zero warm instances, accepting initialization delay within the longer timeout.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 49

A developer tests an upload-and-list workflow using an in-memory fake Cloud Storage client. The fake delays newly uploaded objects in its list method, and the test suite now requires a five-second sleep after every successful upload. Before adopting that behavior in the application, the team checks the hosted Cloud Storage contract for direct API object listing; no CDN, browser cache, or intermediary is involved. It wants the fake and its assertions to reflect the real service rather than invent a timing rule. What should it change?

**Select ONE answer.**

**A.** Switch to longer signed URL expiry because it controls listing consistency.

**B.** Correct the fake and assertions to reflect strongly consistent successful direct object writes and listings; remove the artificial visibility-delay requirement.

**C.** Add five-second sleeps to all production paths and treat passing fake tests as evidence of necessity.

**D.** Keep the fake's delay because every object store uses eventual consistency for listing.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 50

A Cloud SQL transaction creates an order and records its stable operation ID under a uniqueness constraint. The database connection drops while the client waits for the COMMIT response, so the client cannot tell whether the transaction committed. The operation ID was chosen before the attempt and is durably available to the caller. The team must avoid a second order, while allowing recovery if nothing committed. Which recovery strategy best handles uncertainty rather than assuming that every lost response proves rollback?

**Select ONE answer.**

**A.** Check once for the operation ID, then create a new order without the original uniqueness-protected identity if the check times out.

**B.** Reconnect and retry the complete transaction under a newly generated operation ID.

**C.** Reconnect, resolve or retry using the same operation ID and uniqueness-protected transaction, and return an already committed matching result when found.

**D.** Treat the missing COMMIT acknowledgment as proof of rollback and retry without checking or reusing the operation ID.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

[Ayrı Türkçe cevap anahtarı — çözüm sonrası](../answers/scenarios/PCD-S11.md)
