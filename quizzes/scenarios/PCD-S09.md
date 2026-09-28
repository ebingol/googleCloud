# PCD-S09 — Karma deneme

28 Eylül 2026 · **50 soru · 44 tek seçim + 6 çift seçim**

Zorluk hedefi: sample exam’den daha zor; yakın alternatifleri birden fazla gereksinimle eleme. Bu özgün çalışma seti gerçek sınavdan alınmadı ve gerçek sınav/sample ile doğrudan kalibre edilmedi. İngilizce gövdeler 84–103 kelime; uzunluk gereksiz dolgu yerine karar koşullarına ayrıldı.

**Uygulama:** Önce anahtarı açmadan çöz. Tam deneme için 120 dakikayı hedefleyebilirsin; süre aşılırsa çalışmayı bırakman gerekmez, 120. dakikadaki soru numaranı ayrıca kaydet. Önceki gibi 10’luk bölümlerle de ilerleyebiliriz. Bölümler arasında açıklama alırsan bunu kesintisiz yardımsız denemeden ayrı kaydedeceğiz.

**Select ONE:** en iyi tek seçenek. **Select TWO:** tam iki seçenek; puan için doğru kümenin tamamı gerekli. E = eminim, K = kararsızım, T = tahmin. Bilmediğin teknik kavrama B notu düşebilirsin. Her soruya uzun gerekçe gerekmiyor; özellikle iki şık arasında kaldıklarında belirleyici koşulu belirt.

Başlangıç: ___ · 120. dakikadaki soru: ___ · Toplam çözüm süresi: ___

## Bölüm 1 — Sorular 1–10

Bölüm süresi: ___ dakika · Mola/yardım: ___

### Question 01

**Select ONE.**

A Cloud Run checkout service calls a recommendations API before returning each page. Recommendations are optional, and the business accepts a page without them. During a prolonged downstream outage, every request waits through several retries, exhausting the checkout service's available concurrency even though its database remains healthy. Increasing instances helps briefly but multiplies calls to the failing dependency. The team wants to preserve checkout capacity and periodically detect recovery without permanently disabling recommendations. It can change the calling code and already has a fallback response. Which approach best addresses both the repeated failure and the requirement to restore normal behavior?

A. Return the fallback after the existing retries finish, and increase the number of retries to improve recovery detection.

B. Increase the recommendation timeout and instance limit, retaining the same retry sequence for each checkout.

C. Add a circuit breaker that stops failed calls and serves the fallback, but keep it open until the next application deployment.

D. Use bounded calls, a circuit breaker with recovery probes, and the approved fallback.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 02

**Select ONE.**

A developer must reproduce a staging authorization failure using the same service-account identity as the deployed application. Personal user ADC works locally but has broader data access and therefore hides the failure. Downloaded service-account keys are prohibited. The selected language and client library support local ADC through service-account impersonation, and an administrator can grant narrowly scoped impersonation permission. Network access and the staging account's resource permissions must remain unchanged during the investigation. Which setup best makes the local application exercise the intended identity while avoiding a permanent credential and preserving normal client-library credential discovery?

A. Grant the staging account the developer’s broader data roles, then repeat the existing local test.

B. Configure supported impersonated local ADC, granting Token Creator on the staging account.

C. Keep personal user ADC and change only the active gcloud project to the staging project.

D. Attach the staging account to a Cloud Run service and assume the laptop inherits that attachment.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 03

**Select ONE.**

A Cloud Tasks queue invokes a private Cloud Run worker to generate short reports. Invocation succeeds, and each report normally finishes within the task dispatch deadline. To reduce observed HTTP latency, the worker starts a local background thread and immediately returns HTTP 200. Some accepted reports disappear when instances are replaced. The application can already detect completed reports by a stable operation identifier, and retrying an unfinished report is safe. The team wants Cloud Tasks to track processing failure and redeliver unfinished work. Which worker change most directly restores that delivery contract without adding another queue or changing the public request path?

A. Use instance-based billing and a minimum instance, returning success when the background thread starts rather than when the report finishes.

B. Persist the completed report before returning success; report processing failures to Cloud Tasks.

C. Keep the early response but write a log entry identifying the thread before acknowledging the task.

D. Return HTTP 200 after starting the thread and configure more task retries on the queue.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 04

**Select ONE.**

A PostgreSQL application uses a bounded connection pool and Cloud SQL high availability. After a tested failover, new connections work, but requests that borrowed old connections receive errors. Some failures occur halfway through a transaction that updates two related records; the database has confirmed these transactions were rolled back. The application currently retries only the final SQL statement on the same broken connection. The business operation is safe to retry as a complete transaction. Which recovery behavior preserves the two-record consistency requirement and lets the pool recover without increasing its maximum size or changing the HA configuration?

A. Retry only the failed statement after increasing the pool size, retaining the existing borrowed connection.

B. Reconnect and execute the remaining statements without a transaction because the earlier statements already ran.

C. Return success for rolled-back transactions and allow later reads to reconstruct the missing updates.

D. Discard broken connections, reconnect with bounded backoff, and retry the entire rolled-back transaction.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 05

**Select ONE.**

An administrative screen pages through a Firestore Standard collection of completed imports. Records are ordered by completion time, but many imports share exactly the same timestamp. The current client requests the next page using only the last timestamp and sometimes skips records tied at the page boundary. For this investigation, the dataset does not change while pages are read. Required indexes can be created, and each document has a unique identifier. The team wants deterministic pagination without reading all earlier pages again. Which query and cursor design resolves the ambiguity while keeping the requested chronological ordering?

A. Order by timestamp and a unique document identifier, carrying both values in the continuation cursor.

B. Increase page size and continue using only the timestamp as the exclusive cursor.

C. Order only by document identifier and keep passing a completion timestamp as the cursor value.

D. Keep the timestamp-only cursor but retry each page until the number of returned records equals the page size.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 06

**Select TWO.**

A repository accepts pull requests from external contributors. Cloud Build automatically runs the proposed test code using a service account that can deploy production services and read deployment secrets. Maintainers must continue receiving automated test results before merging, but unreviewed contributor code must not obtain production privileges. A separate trusted release trigger runs after reviewed changes reach the protected branch. The team can assign different build identities and isolated test resources to the two workflows. Which TWO changes establish the intended boundary while keeping useful presubmit testing and the existing reviewed release process?

A. Add a comment asking contributors not to read deployment secrets from their test code.

B. Require a maintainer to start each presubmit build manually, but run the unreviewed code with the unchanged production-capable build identity.

C. Reserve production permissions and secret access for the separately controlled release workflow on reviewed source.

D. Run presubmit builds with an identity limited to isolated test resources and no production secrets or deployment rights.

E. Keep the privileged identity but remove deployment commands from the default build file while allowing contributors to change test scripts.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 07

**Select ONE.**

A GKE Pod contains an API container and a lightweight logging sidecar. The API's CPU consumption rises with request demand, while the sidecar remains mostly idle. The existing HPA scales on average CPU utilization across the whole Pod, and the team has measured that the sidecar's large CPU request dilutes the signal. Both containers have valid requests; metrics collection and node capacity are healthy. The cluster supports container-resource HPA metrics. The team wants scaling to follow the API container without changing the sidecar's resources or removing it. Which HPA configuration most directly matches the measured bottleneck?

A. Increase only the maximum node count and keep the diluted Pod-level CPU target.

B. Increase the sidecar CPU request further and retain the existing aggregate utilization target.

C. Raise the Pod-level CPU utilization target so the idle sidecar contributes less to the measured value.

D. Use a ContainerResource CPU utilization metric targeting the API container, with suitable replica bounds.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 08

**Select ONE.**

A cleanup service reads the generation number of an obsolete Cloud Storage object and decides to delete that generation's live object. Before deletion reaches Storage, another service might replace the object under the same name with a new generation that must be preserved. Transient connection failures can also leave the cleanup client unsure whether its delete succeeded. The team can supply request preconditions and tolerate a conflict that requires re-evaluating the object. Which request and retry strategy prevents an old cleanup decision from deleting replacement data while still allowing recovery from eligible transient failures?

A. Keep the original generation-match precondition on deletes and retries; re-evaluate conflicts instead of removing it.

B. Delete by object name without a precondition and retry every failed request with exponential backoff.

C. Check the current generation immediately before each name-only delete and assume the two operations are atomic.

D. On every retry, fetch the latest generation and delete it automatically because it has the same object name.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 09

**Select ONE.**

A Cloud Run service in an application project references an existing Secret Manager secret in a separate security project. The deployment configuration uses the correct full secret resource name and a supported enabled version. The runtime service account is explicitly configured, and the error identifies that account as missing secret payload access. The deployment operator can already read the secret, and no network or organization-policy denial is involved. The security team allows access to this one secret but does not want application-wide administrative privileges. Which change directly fixes the identified failure at the appropriate resource scope?

A. Grant the configured runtime service account Secret Accessor on the specific secret in the security project.

B. Grant the Cloud Run service agent Secret Accessor instead of the runtime service account identified in the error.

C. Grant the runtime service account Secret Manager Viewer on the secret so it can inspect metadata.

D. Grant the deployment operator Secret Accessor again in the application project.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 10

**Select ONE.**

A team uses Firestore Standard from both a browser application and a trusted backend. New Security Rules should prevent one signed-in customer from reading another customer's documents. The current emulator test suite uses only an administrative server SDK and reports success after creating and reading records. Those tests are useful for backend logic, but reviewers want evidence that the browser-facing authorization rule actually denies the forbidden request. The team can run authenticated client tests against the emulator with synthetic identities. Which addition most directly tests the missing property without granting production access or confusing IAM-based backend access with client Security Rules?

A. Repeat the administrative reads with a second collection name and compare response times.

B. Use Rules-aware client test contexts for two users, asserting allowed own-document access and denied cross-user access.

C. Validate that the rules file contains the customer identifier string without issuing any client requests.

D. Run a second emulator suite with administrative server credentials and narrower production IAM, interpreting access failures as client Security Rules results.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

## Bölüm 2 — Sorular 11–20

Bölüm süresi: ___ dakika · Mola/yardım: ___

### Question 11

**Select ONE.**

An application already uses a multi-region Spanner configuration that satisfies its regional resilience requirement. Most write transactions originate in one supported read-write region, but the database's default leader is in another eligible region. Traces show substantial network time around writes rather than expensive SQL execution. The team wants to reduce ordinary write latency while preserving the existing multi-region resilience design. It can adjust placement and leader configuration, and it will validate the effect with measurements. Which change best targets the observed latency without replacing the database or assuming that a nearby read-only replica can independently commit writes?

A. Increase client-side result caching for write transactions and keep the current network path.

B. Change to a single-region database regardless of the stated regional resilience requirement.

C. Align the dominant write workload with an eligible default leader region and validate the latency change.

D. Add a read-only replica beside the writers and route all transaction commits to that replica.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 12

**Select ONE.**

A Cloud Run application image has passed release testing and is deployed in production. An incident is traced to a non-secret environment setting that selects an incorrect downstream endpoint; the executable itself is unchanged. A previous revision has the correct configuration, but the team also wants to validate a corrected candidate before moving normal traffic. All database changes are compatible with both configurations. Which deployment plan preserves the tested artifact, creates a reviewable configuration change, and retains a practical rollback target without rebuilding identical application code simply to change an environment value?

A. Deploy from the same source with corrected settings, test the rebuilt candidate without traffic, and retain the previous revision for rollback.

B. Change the environment in one running instance and expect the change to persist across replacements.

C. Deploy the tested digest with corrected configuration and no traffic; validate, then migrate traffic while retaining rollback.

D. Move the existing image tag and assume this edits the environment of every deployed revision.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 13

**Select ONE.**

A developer's workstation has authenticated access to two GKE clusters: production and staging. Cloud Code uses the local Kubernetes configuration for a development deployment. The current context still points to production after an earlier troubleshooting session, although the developer has selected the staging Google Cloud project in the command-line configuration. The development namespace has the same name in both clusters. The team wants to run its existing local development loop against staging and verify the target before applying changes. Which action most directly corrects this environment-selection problem without changing application manifests or broadening permissions?

A. Select and verify the staging Kubernetes context, endpoint, and namespace before running the development deployment.

B. Grant the developer cluster-admin in both clusters so either context can complete the deployment.

C. Keep the current Kubernetes context because changing the active gcloud project automatically retargets all existing contexts.

D. Rename the namespace in the manifest and keep the production cluster endpoint selected.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 14

**Select ONE.**

A team sends a small fraction of Cloud Run traffic to a candidate revision. The service-wide average latency remains nearly unchanged because the stable revision serves most requests. A few customers report very slow successful responses after the rollout. Logs identify the revision and request path, and latency distributions are already available. The team needs to decide whether to stop the canary without mistaking the stable revision's larger traffic volume for evidence that the candidate is healthy. Which analysis provides the most relevant evidence while keeping sample size and differences in request mix in view?

A. Count only exception groups because successful requests cannot represent a latency regression.

B. Compare high-percentile latency and errors by revision and comparable route; investigate representative slow traces.

C. Compare only total service CPU before and after deployment, ignoring the request distributions.

D. Wait until all traffic reaches the candidate so the service average can represent that revision.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 15

**Select ONE.**

A Bigtable telemetry table leads each row key with customer ID and then event time. Most customers write modest volumes, but one customer produces most new events and overloads a narrow key range. Adding capacity has not removed the concentration. Queries need a time range for one customer, and the application accepts a small fixed number of parallel range scans followed by a merge. Each event has a stable identifier that can determine a balanced shard. Which key and query change addresses the unusually hot customer while preserving a bounded way to retrieve that customer's events?

A. Use a completely random key and scan the entire table for each customer request.

B. Reverse the timestamp while retaining the same single advancing range for the hot customer.

C. Lead with a balanced shard, then customer and timestamp; query each shard’s customer range and merge.

D. Keep customer ID and increasing time first, then append a shard after the timestamp.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 16

**Select ONE.**

A GKE Service selects the correct Pods, and all selected Pods are Ready. The application listens on TCP port 9090, while the Service exposes port 80 and forwards to targetPort 8080. Requests to a Pod's IP on 9090 succeed from the caller namespace, but requests through the Service fail. NetworkPolicy permits the required traffic, and DNS resolves the Service name correctly. The readiness probe already checks the actual listener. Which change repairs the application path with the smallest relevant adjustment while preserving the stable Service address and avoiding unrelated changes to replica count or application identity?

A. Increase replicas and keep the current Service port mapping.

B. Grant the Pod’s service account additional Google Cloud IAM roles and retain the current port mapping.

C. Change only the Service port to 9090 while retaining targetPort 8080.

D. Change the Service targetPort to the application’s actual listener on 9090, keeping the desired client-facing port.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 17

**Select ONE.**

A release reviewer receives a Cloud Build provenance record for an image digest and a passing integration-test report for a different digest built from the same source commit. The difference arose because the images were built at separate times. The deployment policy requires both trusted build origin and successful tests for the exact artifact being released. The team can access both images and rerun tests, but cannot waive either requirement. Which next action creates sufficient evidence for the candidate without assuming that a common commit label, a provenance record, or a successful test report proves more than it actually does?

A. Test the candidate digest and associate its passing result with validated provenance for that same digest.

B. Add the tested image’s tag to the candidate and treat the tag as transferring the test result.

C. Discard the provenance requirement because integration testing alone verifies the builder identity.

D. Combine the two records by source commit and approve the candidate without testing its digest.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 18

**Select TWO.**

An external CI system already authenticates through Workload Identity Federation without service-account keys. Its provider accepts tokens from the expected issuer and organization, but jobs from any repository in that organization can obtain the production deployment identity. Only one repository's protected release workflow should be authorized. The issuer supplies stable repository identifiers and trustworthy workflow-context claims that administrators can validate. The team wants to narrow the trust boundary while keeping short-lived credentials and the existing production role scope. Which TWO configuration actions address the excessive acceptance without relying on a repository name typed by the job itself?

A. Replace federation with a shared service-account key available to every repository.

B. Apply restrictive provider conditions and principal bindings so only the approved context can obtain the deployment identity.

C. Grant the production role to every principal from the issuer and restrict only the container image tag.

D. Map and validate the trusted token claims needed to identify the approved repository and release context.

E. Keep organization-wide federation and add an instruction to each job saying production deployments require review.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 19

**Select ONE.**

A Pub/Sub subscription has a dead-letter topic configured for messages that repeatedly fail processing. The consumer correctly rejects a malformed message, but the message continues returning and no corresponding message appears in the dead-letter topic. Investigation shows that the subscription project's Pub/Sub service agent lacks the required forwarding permissions. There is also no subscription on the dead-letter topic for operators to inspect forwarded messages. The team wants managed isolation and a visible investigation backlog. Which repair addresses these configuration gaps without acknowledging malformed messages as successfully processed or assuming the delivery-attempt threshold is an exact counter?

A. Acknowledge every failing message immediately and rely on the dead-letter policy to copy acknowledged messages afterward.

B. Grant the Pub/Sub service agent Publisher on the dead-letter topic and create its inspection subscription, but leave source-subscription permissions unchanged.

C. Grant forwarding permissions to the Pub/Sub service agent and subscribe to the dead-letter topic for inspection.

D. Increase the source acknowledgment deadline until malformed payloads become valid.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 20

**Select ONE.**

A Cloud Run service has a stable revision receiving all normal traffic. A candidate has been deployed with no normal traffic and a revision tag for integration testing. Testers need their requests to reach that candidate consistently, while ordinary users must remain on the stable revision until approval. Authentication is already correct, and testers know both the ordinary service URL and the tagged revision URL. Which approach provides the required test routing without changing the normal traffic percentages or treating the tag as a replacement for invocation authorization?

A. Allocate all normal traffic to the candidate temporarily and ask ordinary users not to connect.

B. Send test requests to the ordinary service URL and add the candidate tag only as an application log label.

C. Enable session affinity on the stable revision and expect it to select the candidate for new test sessions.

D. Use the candidate’s tagged URL for test requests while keeping the ordinary traffic allocation on the stable revision.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

## Bölüm 3 — Sorular 21–30

Bölüm süresi: ___ dakika · Mola/yardım: ___

### Question 21

**Select ONE.**

A request handler creates a Cloud Tasks task for a payment notification. The create call sometimes loses its response, leaving the handler unsure whether the queue accepted the task. Retrying with a newly generated task name can enqueue the same logical operation twice. Each operation already has a durable unique identifier, and all creation retries occur within the queue's supported task-name deduplication window. The worker is also idempotent because deliveries can repeat. Which producer behavior best handles the uncertain creation result without depending on task-name deduplication as a permanent guarantee that the business operation runs only once?

A. Disable creation retries and tell the caller that every lost response means the queue rejected the task.

B. Use a stable operation-derived task name for creation retries and handle the corresponding already-exists result.

C. Use a new task name for every creation attempt and rely only on a higher dispatch deadline.

D. Reuse the task name but remove worker idempotency because task-name deduplication also guarantees exactly-once execution.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 22

**Select ONE.**

A service team changes an API response field from an integer to a string. Its own unit tests and provider integration tests pass because they were updated together with the implementation. An older mobile client still expects the integer and cannot be upgraded immediately. The team wants its Cloud Build pipeline to detect this compatibility break before a release is approved. A versioned consumer expectation is available, and tests can run against the candidate service using synthetic data. Which additional check most directly closes the gap without merely increasing coverage of the provider's new interpretation of the contract?

A. Add more provider tests that assert the new string value and remove tests of the earlier representation.

B. Regenerate all expected client responses from the candidate before testing them so the contract stays synchronized.

C. Run a vulnerability scan of the container and treat a clean result as evidence of response compatibility.

D. Test the candidate against the supported older consumer contract and block release when compatibility fails.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 23

**Select ONE.**

A GKE application has three Ready replicas spread across nodes. During node maintenance, the team requires at least two replicas to remain available through voluntary evictions. A PodDisruptionBudget already specifies minAvailable of two. One replica then becomes unready because of an unrelated dependency failure, leaving only two healthy replicas. An operator's next normal eviction request for another healthy Pod is blocked. The rollout configuration is unchanged, and the team does not want to bypass its availability protection. Which interpretation and next action best match the budget's purpose?

A. Restore or add healthy capacity before evicting another healthy Pod under the existing availability budget.

B. Set the Deployment’s maxUnavailable to one while keeping the existing number of healthy replicas, then retry the same normal eviction.

C. Treat the block as an IAM failure and give the operator project Owner.

D. The budget counts only total Pods, so delete the blocked healthy Pod directly to restore normal behavior.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 24

**Select ONE.**

A client lists resources through an API whose pagination contract requires subsequent requests to keep the original filter and ordering. It stores the next-page token while a user views results. If the user changes the filter, the current client sends the old token with the new filter and receives inconsistent or rejected requests. The interface must show all pages matching the newly selected filter, and the API does not promise that tokens can be decoded or transferred between queries. Which client behavior correctly separates a new search from continuation of an existing one while keeping memory use bounded?

A. Start a fresh query when filters change; use only its returned continuation tokens with matching parameters.

B. Keep the old token because pagination tokens identify a global offset independent of filters.

C. Decode the token and edit its contents to replace the old filter with the new one.

D. Increase page size and reuse the old token until the API stops returning results.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 25

**Select ONE.**

A team rotates a supplier password used by a Cloud Run service. Old and new revisions pin different Secret Manager versions, and the supplier can temporarily accept both credentials. The deployment plan keeps the old revision as a rollback target. An engineer proposes disabling the old secret version immediately after the first successful request to the new revision. The rollback window has not closed, and old instances might need to restart during that window. Which rotation sequence preserves both controlled credential retirement and a usable rollback path without assuming that an existing instance's cached environment value is sufficient recovery protection?

A. Delete the old revision first and retain only its image digest as a complete rollback configuration.

B. Retain both secret and supplier credential through the rollback window, then retire them after verified migration.

C. Disable the old secret immediately and rely on already-running old instances to remain alive until rollback is no longer needed.

D. Change both revisions to latest without testing and consider their previous pinned credentials preserved.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 26

**Select TWO.**

A Docker build uses a base image tag that can move and downloads application dependencies without a lockfile. The team wants controlled, reviewable dependency updates and more reproducible builds, while still receiving security fixes through its release process. It already promotes tested image digests between environments. Repeated builds currently vary even when application source has not changed. Which TWO changes address the changing build inputs without freezing vulnerable dependencies indefinitely or claiming that dependency pinning alone guarantees byte-for-byte reproducibility of every possible build output?

A. Pin the approved base image by digest and update that pin through reviewed, tested changes.

B. Rebuild separately for each environment and assign each result the same release tag.

C. Treat the application source commit as a complete record of all external dependencies.

D. Keep a floating base tag and turn off caching so every build resolves whatever version is newest.

E. Preserve and enforce a dependency lockfile, with an explicit process to update, scan, and test dependency changes.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 27

**Select ONE.**

A Cloud Run HTTP service starts a two-hour export when a customer clicks Download. The customer only needs an operation identifier immediately and can poll status later. Export processing must survive the loss of the accepting HTTP instance, and it has no need to serve HTTP requests while running. Input partitions and durable progress records already exist, and retries are safe. The team prefers a managed execution model for work that terminates when complete. Which design best separates fast acceptance from durable long-running execution while retaining a clear way to report completion or failure?

A. Increase the service request timeout and require the browser to hold the connection throughout the two-hour export.

B. Start a local thread, return the identifier, and use session affinity to preserve the exporting instance.

C. Run the entire export before returning an identifier, retrying the browser request whenever its connection closes.

D. Start a Cloud Run job, return a durable operation identifier, and expose execution status and outputs for polling.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 28

**Select ONE.**

A legacy processing application on GKE expects several Pods on different nodes to read and write the same directory tree through a supported NFS filesystem. Its libraries depend on filesystem operations that the team cannot replace with object API calls during this migration. Data must survive Pod replacement, and the team prefers managed storage rather than maintaining its own NFS server. The required network connectivity and suitable storage capacity can be provisioned. Which storage approach most directly fits the access model without assuming that every mountable storage product provides the same filesystem semantics?

A. Give every Pod its own emptyDir and synchronize only after each Pod terminates.

B. Use a managed Filestore share with the appropriate GKE integration and a suitable tier and access configuration.

C. Give each node a separate persistent disk and use identical directory names as the shared-file consistency mechanism.

D. Mount a Cloud Storage bucket and assume object storage provides all the application’s required NFS behavior unchanged.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 29

**Select ONE.**

A team uses Cloud Workstations with an approved custom container image and persistent home directories. A toolchain upgrade works for newly created workstations, but one developer still runs an older session started before the configuration change. The project files in that developer's home directory must be preserved, and the team wants to confirm that the new session actually uses the approved tool version. The configuration points to a new versioned image; the new session is confirmed to pull it on restart. Which action best completes the rollout without deleting the developer's persistent working data or relying on manually patching a single running container?

A. Delete the persistent home directory so its empty contents force the container to use a newer compiler.

B. Change only the application repository branch and assume this replaces the running development container.

C. Save work, restart with the updated configuration, and verify the tool version while retaining the persistent home.

D. Refresh the workstation configuration in the console and verify its image reference, then keep the existing session running to preserve the developer’s files.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 30

**Select ONE.**

A service writes one JSON log entry for each failed request, but every entry is classified as ordinary informational output. The JSON contains a custom field named levelText, while exception details are split across several unrelated messages. Operators need reliable severity filtering and grouping of recurring exceptions by service version. The logging platform already ingests stdout correctly, and trace propagation is functioning. Which change most directly improves interpretation of the existing application failures without increasing log volume or treating an arbitrary JSON property as a recognized logging field?

A. Write every request as CRITICAL, including successful responses, so error searches always include the failures.

B. Create more trace spans but leave the exception representation and severity mapping unchanged.

C. Emit recognized severity fields and coherent exception entries containing supported stack-trace and service-version context.

D. Increase retention and continue emitting the same custom level field and disconnected exception messages.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

## Bölüm 4 — Sorular 31–40

Bölüm süresi: ___ dakika · Mola/yardım: ___

### Question 31

**Select ONE.**

A GKE API opens its HTTP listener immediately but needs additional time to load a local search index. A TCP readiness probe succeeds as soon as the listener opens, so the Service sends requests before the index is usable. Initialization completes normally if the Pod receives enough time, and a local liveness check correctly detects later deadlocks. The application can expose an HTTP endpoint that reports whether the index has finished loading and whether it can serve searches. Which change best controls traffic admission without confusing an open socket with application readiness or weakening steady-state deadlock detection?

A. Use semantic HTTP readiness, adequate startup allowance, and the existing independent local liveness check.

B. Extend the TCP readiness failure threshold and request timeout, keeping the open listener as the signal that application traffic can be accepted.

C. Remove readiness and rely on successful container creation as the admission signal.

D. Make the HTTP response cache absorb all failures until the index eventually loads.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 32

**Select ONE.**

A document API caches both public document metadata and each customer's download entitlement in Memorystore for ten minutes. Metadata may be several minutes old without harming the product, but a revoked entitlement must not continue authorizing downloads after the revocation commits. Cache keys already include tenant and customer identifiers, so cross-tenant key collisions are not the problem. The authoritative entitlement store can handle a narrow authorization lookup on each download. Which caching design preserves useful metadata caching while meeting the stricter correctness requirement for access decisions without promising an instantaneous invalidation mechanism that the system does not have?

A. Reduce entitlement TTL to one minute and describe the remaining delay as immediate revocation.

B. Keep the ten-minute entitlement TTL and treat tenant-aware keys as sufficient to enforce revocations.

C. Replicate the same cached entitlements to every instance so all instances agree on the stale authorization result.

D. Continue caching tolerant metadata, but verify current entitlement through the authoritative path before authorizing each download.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 33

**Select ONE.**

A team compares two Cloud Run configurations using a load test. Configuration A is tested immediately after deployment at a low initial request rate, while configuration B is tested after several minutes of sustained traffic. The second run has lower latency, but traces show initialization costs mainly in the first run. Both configurations need evaluation for steady traffic and the first burst after an idle period. The team wants a decision based on comparable conditions rather than attributing every difference to the configuration change. Which test design best separates these effects while retaining the user-visible cost of cold starts?

A. Repeat comparable workloads for both configurations and report idle-start and steady-state results separately.

B. Test only warm instances because initialization latency is never visible to users.

C. Increase the duration of B’s existing warm test and compare it with A’s unchanged first run.

D. Discard all slow requests from both runs and compare only each configuration’s fastest responses.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 34

**Select ONE.**

A Pub/Sub pull subscription has exactly-once delivery enabled within its supported regional configuration. Nevertheless, the consumer records two business notifications for one order. Investigation finds two successful publish calls with different Pub/Sub message IDs but the same stable order-operation ID, caused by a publisher retry after an uncertain response. The consumer database supports an atomic uniqueness constraint and transactional updates. Which change addresses this form of duplication while preserving delivery acknowledgments after durable processing and avoiding a claim that transport-level guarantees identify equivalent business operations across separate publishes?

A. Use only Pub/Sub message ID as the business uniqueness key because exactly-once delivery merges separate publish calls.

B. Atomically combine the business write with operation-ID deduplication; acknowledge after the durable outcome.

C. Acknowledge before writing so duplicate publishes cannot reach the database at the same time.

D. Increase the acknowledgment deadline and keep inserting one business record for every received message ID.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 35

**Select ONE.**

A GKE release policy currently requires a security team's attestation for an image digest. A new requirement adds independent approval from a functional-test team; neither approval should substitute for the other. The two teams control separate trusted attestors, and deployers cannot change the admission policy or use an exception path. A candidate has passed the security check but has no functional-test attestation. Which policy and release behavior enforces the new requirement at deployment time without conflating vulnerability scanning, build origin, and evidence that the required tests passed?

A. Approve the candidate when either attestor signs it, because two trusted attestors provide interchangeable evidence.

B. Accept a source-commit label as the missing functional-test approval if the security attestation is valid.

C. Require both attestors for the candidate digest and block deployment until both approvals exist.

D. Collect both teams’ reports in the release pipeline, but leave admission policy requiring only the security attestor for direct deployments.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 36

**Select TWO.**

A team moves a file-processing function to an Eventarc-triggered Cloud Run deployment. The trigger delivers a Cloud Storage object-finalized CloudEvent, but the handler was written for Pub/Sub events and tries to decode a message.data field. Invocation authentication succeeds; the function fails while parsing the body, before any object is read. The team has a captured synthetic Storage event and can run it through the Functions Framework locally. Which TWO changes best repair the integration and verify that the receiver matches the configured trigger without changing a working service-account permission or inventing a Pub/Sub envelope inside a Storage event?

A. Register the appropriate CloudEvent handler and read the bucket, object name, and generation from the Storage event data.

B. Add a representative Storage CloudEvent adapter test through the Functions Framework, with object access isolated from the parsing assertion.

C. Base64-decode the entire HTTP request regardless of its event type.

D. Change only the function timeout to allow parsing more time.

E. Grant the runtime identity additional Invoker permission and retain the existing Pub/Sub parser.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 37

**Select ONE.**

A Cloud Build pipeline runs unit tests and dependency checks concurrently after compilation. Both checks correctly wait for the compiler, and packaging waits for both. However, each check writes a different JSON report to the same path under /workspace. The build sometimes publishes the wrong report because whichever check finishes last overwrites the other output. Both checks must remain parallel, and packaging needs both reports. Which change fixes the data collision while preserving the already-correct dependency graph and avoiding a false assumption that each step receives a private copy of the shared workspace?

A. Make packaging wait only for the faster check and read the report before the slower check overwrites it.

B. Set both checks to wait for compilation again, leaving the shared report path unchanged.

C. Write reports to distinct shared-workspace paths and have packaging read both after the checks finish.

D. Move both reports to the same private /tmp path in each step and leave packaging reading /workspace.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 38

**Select ONE.**

A company stores investigation files in a Cloud Storage bucket with a normal age-based cleanup rule. Most files can be deleted after the normal period, but selected files must remain protected while an investigation is open, whose end date is unknown. The bucket has no retention policy, individual retention configuration, or hierarchical namespace enabled. Authorized investigators can explicitly release protection when a case closes, after which normal cleanup may proceed. Which object-level mechanism best fits the selective, open-ended protection without disabling cleanup for unrelated files or pretending that version history prevents deletion?

A. Increase the lifecycle age for the entire bucket whenever one investigation starts.

B. Enable Object Versioning and assume every historical generation becomes undeletable until the case closes.

C. Enable Object Versioning and retain noncurrent generations with an age-based lifecycle rule, relying on historical copies instead of blocking deletion.

D. Apply temporary holds to the selected objects, releasing them through the authorized case-closure process.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 39

**Select ONE.**

A local application calls a client-based Google Cloud API using valid user ADC. The user can access the target resource, and the API is enabled in the intended consumer project. The request nevertheless fails with a message identifying the quota project and missing serviceusage.services.use permission. The team has an approved consumer project for this workload and wants to charge quota there without changing the user's resource-data permissions. Which configuration and permission adjustment directly addresses the reported failure rather than replacing working authentication or granting broad administration over the data project?

A. Change only the resource path to contain the consumer project even though the resource is stored elsewhere.

B. Configure the approved quota project and grant the caller service-usage permission on that consumer project.

C. Grant project Owner on the data project and leave the quota project selection unchanged.

D. Replace ADC with an API key and assume all resource authorization and quota checks are bypassed.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 40

**Select ONE.**

A new GKE Pod fails to start after a configuration rollout. Events report that a required ConfigMap key referenced by an environment variable does not exist. The image has been pulled successfully, and the previous revision still runs with its earlier valid configuration. An engineer suggests increasing liveness delays because the new Pod has not become Ready. The application cannot run correctly without this setting, and the deployment configuration is managed in source control. Which action fixes the diagnosed prerequisite while preserving an explicit configuration contract rather than hiding the missing value or treating the failure as slow application startup?

A. Increase HPA maximum replicas so at least one Pod can start without the required configuration.

B. Correct the required key or reference in managed configuration, validate it, and deploy the correction.

C. Mark the key optional and let production use an undocumented empty value.

D. Replace the readiness probe with a startup probe and give initialization a longer allowance, leaving the required ConfigMap key reference unchanged.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

## Bölüm 5 — Sorular 41–50

Bölüm süresi: ___ dakika · Mola/yardım: ___

### Question 41

**Select ONE.**

A public API runs on Cloud Run behind an external Application Load Balancer with a Cloud Armor policy. Requests through the custom domain are filtered correctly, but an external client can call the service's default URL and avoid the load-balancer policy. The application must remain public through the approved front end, and no browser-based Google IAM sign-in is required. The team needs to close the direct internet path while retaining application authentication and the existing load-balancer route. Which ingress design addresses this bypass without assuming that a WAF policy attached to one route automatically protects every route to the backend?

A. Enable Direct VPC egress and assume this filters internet requests arriving at the service.

B. Add more Cloud Armor rules to the existing load balancer while leaving unrestricted direct service ingress.

C. Keep unrestricted direct ingress but require application authentication on both URLs, assuming authenticated requests cannot bypass the load-balancer filtering policy.

D. Use the appropriate internal-and-cloud-load-balancing ingress restriction and retain the supported load-balancer path and application authentication.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 42

**Select TWO.**

A developer uses Gemini Code Assist with an approved MCP documentation server. A retrieved troubleshooting page includes instructions to upload local credentials to an unrelated endpoint before applying a code fix. The current task requires only reading SDK documentation and editing application code; no credential export is necessary. The server's documentation can contain third-party text, and the developer wants the assistant to use relevant technical facts without allowing retrieved prose to expand its authority. Which TWO practices best preserve useful assistance and the existing task boundary while recognizing that retrieved content is not equivalent to a trusted user instruction?

A. Treat every instruction in the returned page as authorized because the MCP server itself was approved.

B. Disable code review once the assistant can cite the retrieved page as evidence.

C. Give the assistant full local credential access so it can decide whether the page’s instruction is legitimate.

D. Ignore the credential-export instruction, use only task-relevant documentation facts, and verify proposed code against trusted sources and tests.

E. Keep tools and credentials restricted to the required capabilities so retrieved text cannot grant additional access.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 43

**Select ONE.**

A Cloud Run image-processing service is reliable when tested with one request per instance. Under concurrent requests, memory grows roughly with the number of images being decoded, and instances occasionally terminate. There is no growing memory use after completed requests, and one valid request fits comfortably within the configured memory. The team cannot change the image library immediately, but can increase the number of instances within a tested downstream capacity budget. It wants a near-term configuration change based on measured per-request memory rather than treating the failure as a leak or making every instance arbitrarily large. Which adjustment best targets the concurrency-related pressure?

A. Set more minimum instances and keep the existing maximum concurrency per instance, assuming extra warm capacity enforces the measured per-instance memory budget.

B. Increase the request timeout while retaining the same per-instance concurrency and memory.

C. Raise maximum instances alone and assume the platform will never send concurrent requests to an existing instance.

D. Set measured safe per-instance concurrency, then validate instance scaling and downstream capacity under load.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 44

**Select ONE.**

An order pipeline publishes messages to Pub/Sub and processes them in workers. Customer-visible completion time has increased from seconds to several minutes, but worker processing spans still show short execution times and few errors. The publisher remains healthy. Monitoring shows a growing subscription backlog and an increasing age of the oldest unacknowledged message. The team needs to explain the delay before optimizing database queries inside the worker. Which investigation best uses the evidence already available to distinguish waiting for processing from the time spent executing the handler?

A. Increase only trace sampling and ignore queue metrics because tracing automatically includes every minute before a worker receives a message.

B. Optimize the shortest database span first because handler duration must equal end-to-end completion time.

C. Correlate publish, receive, and completion times by operation, and investigate consumer throughput and backlog age alongside handler traces.

D. Raise the acknowledgment deadline and report that as a reduction in the time messages wait before delivery.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 45

**Select ONE.**

An application directly encrypts small data values with a symmetric Cloud KMS key. After routine rotation, a completed migration re-encrypted every live database record with the new primary version and verified that the live application works. Retained disaster-recovery backups still contain ciphertext encrypted under older versions. Those backups must remain recoverable until their scheduled expiry, and no compromise has been reported. An engineer proposes disabling earlier versions because the live migration is complete. Which key-management decision preserves the full recovery requirement without confusing successful live-data migration with proof that every retained copy is independent of the old key material?

A. Delete old ciphertext metadata while keeping only the name of the CryptoKey.

B. Keep the old versions needed by retained backups until their dependencies are migrated or expire under policy.

C. Confirm every live database row uses the new version, then disable earlier versions while leaving the encrypted backups unchanged until their normal expiry.

D. Rotate the key again until older ciphertext becomes associated with the newest version.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 46

**Select ONE.**

A GKE Deployment has four Ready replicas with identical single-container Pods. Each container requests 500 millicores, and measured average CPU usage is 400 millicores per replica. The HPA uses a target CPU utilization of 50 percent. All metrics are current, there are no missing or newly starting Pods, replica bounds permit scaling, and the question asks for the basic desired-replica calculation before stabilization or rate-limit behavior. An engineer divides usage by the CPU limit instead of the request. Which result follows from the configured utilization target and the standard HPA ratio calculation under these assumptions?

A. Seven replicas, because utilization is 80 percent of the request and the result is rounded up from 4 × 80 / 50.

B. Four replicas, because each container currently uses less CPU than its request.

C. Eight replicas, because an HPA always doubles replica count whenever the utilization target is exceeded.

D. Five replicas, because any target violation adds exactly one replica per calculation.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 47

**Select ONE.**

A Workflows execution reserves inventory, charges a payment provider, and requests shipment through separate service APIs. Each service commits its own state, and there is no shared transaction manager. If charging fails permanently, the inventory reservation must be released. If a later step fails, the business defines specific compensation actions rather than requiring an impossible automatic rollback of every external side effect. Each API can accept stable operation identifiers. Which orchestration design best makes the process recoverable while recognizing that a workflow's control flow does not by itself turn independent services into one ACID transaction?

A. Retry the full workflow with the same identifiers but omit compensation after permanent payment failure, relying on retries to eventually release inventory.

B. Run all calls in parallel and report success whenever any one service commits.

C. Use explicit compensation, stable operation identifiers, and state-aware handling of retryable and permanent failures.

D. Wrap every HTTP call in one workflow step and assume a later exception rolls back completed external commits.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 48

**Select ONE.**

A Firestore Standard application stores reviews in identically named reviews subcollections beneath many product documents. A trusted backend must retrieve recent reviews written by one user across all products. Product documents are not needed in the response, and the user identifier and review timestamp are stored directly in each review. The team wants an indexed query over the existing structure rather than reading every product and issuing one query per product. It can create the required indexes, and backend IAM authorization is already correct. Which query approach most directly fits the data layout and requested cross-product scope?

A. Create a composite index on product names and treat it as a relational join into every review subcollection.

B. Query one product’s reviews subcollection and rely on the shared subcollection name to expand its scope automatically.

C. Use a collection-group query over reviews with the user and time constraints and the required collection-group indexes.

D. Read the parent products collection once and expect all nested review documents to be included automatically.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 49

**Select ONE.**

An application calls a supported generative model API to draft optional help text during an interactive request. It occasionally receives retryable capacity responses during bursts. The application currently retries immediately until it succeeds, even after the user request deadline, and generated text is not required to complete the user's main action. A static fallback is acceptable. The team wants bounded latency and reduced pressure during capacity incidents while retaining normal model responses when available. Which client strategy best handles this integration without treating all error codes as transient or allowing retries to outlive the interaction they were meant to serve?

A. Bound eligible retries by the remaining deadline; use the approved fallback and record failures when that budget ends.

B. Cache the last generated text across unrelated users indefinitely and disable application response validation.

C. Retry malformed requests unchanged for longer than capacity errors because more attempts can repair their schema.

D. Use exponential backoff for capacity errors but continue until success, allowing the optional call to exceed the interactive request deadline.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 50

**Select TWO.**

An AI coding assistant generates tests for an event handler that should increment a balance once per business operation. The handler writes the balance and a deduplication record transactionally, then acknowledges the message. Existing tests deliver each event once and assert only the final HTTP status. The team wants evidence that a crash after the database commit but before acknowledgment does not produce a second increment on redelivery. A deterministic test harness can inject that failure and query the test database. Which TWO test improvements directly exercise the required behavior while keeping the real handler and transaction logic under test?

A. Assert the stored balance changed exactly once and the same durable operation record governs both deliveries.

B. Replace the expected balance with whichever value the implementation returns after both calls.

C. Mock the entire handler to return success and assert that the mock was called twice.

D. Increase line coverage using additional unrelated valid events without exercising the crash window.

E. Deliver the same operation again after simulating a committed write followed by lost acknowledgment.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

İlk cevaplarını kaydettikten sonra [Türkçe açıklamalı anahtarı](../answers/scenarios/PCD-S09.md) açabilirsin.
