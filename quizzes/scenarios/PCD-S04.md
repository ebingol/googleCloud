# PCD-S04 — Sınav kapsamından karma 20 senaryo

24 Eylül 2026 · 20 özgün İngilizce soru · **Süre hedefi: 45 dakika.**

Dağılım: tasarım 6, geliştirme/test 5, deployment 5, entegrasyon 4. Dört resmî ana alanın tamamı örneklenir; 20 soru her ürünün ve alt konunun tamamını ölçmez. Bu set gerçek sınavdan alınmamıştır; zorluğu gerçek sınavla kalibre edilmemiştir. Önceki yalnız Cloud Run/functions/GKE kapsamı, bu set için genişletilmiştir.

Bazı sorular henüz çalışmadığın teknik ayrıntılar içerebilir. Bunlara **B (bu kavramı bilmiyorum)** yazabilirsin; değerlendirmede teknik önbilgi ile İngilizce anlamayı ayıracağız. İlk turda anahtarı açma. **Select one** bir, **Select two** iki seçenek demektir. Çoklu seçimde tam doğru küme 1 puan; toplam 20 puan. Her soruya cevap ve E/K/T (emin/kararsız/tahmin) yaz; belirleyici koşulu bir cümleyle belirtmen yeterli.

## 1

A telemetry platform stores measurements from hundreds of thousands of devices in Bigtable. Devices have uniformly distributed identifiers and similar write rates. Most reads retrieve a short time range for one known device; cross-device analytics runs in a separate system. The current row key starts with a monotonically increasing timestamp, and new writes concentrate in a small part of the table. You need to distribute writes while retaining efficient device-specific range reads. Which row-key design best fits these access patterns?

**Select one.**

- A. Keep timestamp first and append device ID, so measurements from every device share the same recent time range.
- B. Use device ID followed by a consistently encoded timestamp, grouping each device's measurements within its own key range.
- C. Prefix every measurement with an independently random UUID and keep device ID only in a column value.
- D. Put all measurements for all devices into a single row and create a new column for each timestamp.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 2

A Cloud Build pipeline contains steps with IDs `compile`, `unit-tests`, `security-scan`, and `package`, in that order. The two checks can run independently after compilation, but packaging must wait for both checks to pass. All steps fail normally on a nonzero exit code, and artifact sharing already works. The current configuration runs every step sequentially. Which explicit dependency configuration preserves the release gate while allowing the two checks to overlap?

**Select one.**

- A. Set both checks to `waitFor: ['-']` and package to `waitFor: ['unit-tests', 'security-scan']`.
- B. Set unit-tests to wait for compile, security-scan to wait for unit-tests, and package to wait for security-scan.
- C. Set both checks to wait for compile and package to `waitFor: ['compile']`.
- D. Set both checks to `waitFor: ['compile']` and package to `waitFor: ['unit-tests', 'security-scan']`.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 3

A pipeline builds a container once, tests it, and records its full digest. Another pipeline can update the repository's `release` tag before production deployment occurs. Production must run exactly the image that passed testing, without rebuilding it. Assume `$IMAGE_DIGEST` contains the complete reference `europe-west1-docker.pkg.dev/p/r/api@sha256:...`, and all deployment permissions are correct. Which command most directly preserves the tested artifact's identity?

**Select one.**

- A. `gcloud run deploy api --image="$IMAGE_DIGEST" --region=europe-west1`
- B. `gcloud run deploy api --image=europe-west1-docker.pkg.dev/p/r/api:release --region=europe-west1`
- C. `gcloud run deploy api --source=. --region=europe-west1`
- D. `gcloud run services update api --update-env-vars=TESTED_DIGEST="$IMAGE_DIGEST" --region=europe-west1`

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 4

An order service publishes each accepted order to a Pub/Sub topic. Billing and analytics must each receive every order, and either team must be able to pause its consumers without preventing the other team from processing messages. Each team may run multiple worker instances to share its own processing load. Currently, both teams consume from one subscription, and each sees only part of the orders. Which topology should replace the current arrangement?

**Select one.**

- A. Keep one subscription and use different ordering keys for billing and analytics workers.
- B. Keep one subscription and increase its acknowledgment deadline so both teams can read before acknowledgment.
- C. Create one subscription per team on the same topic; let each team's workers share only that team's subscription.
- D. Create two topics, publish each order to only one of them, and alternate the topic for successive orders.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 5

A regional application already uses Cloud SQL for PostgreSQL and must retain its existing SQL schema and drivers. Its primary database currently runs in a single zone. The business now requires automatic recovery from a zonal failure, with acknowledged committed writes protected by synchronous replication within the region. A brief reconnection period is acceptable; cross-region disaster recovery is a separate project. Which configuration directly addresses the new requirement?

**Select one.**

- A. Enable automated backups on the standalone instance and restore the latest backup manually after a zone fails.
- B. Add a standard asynchronous read replica in another zone and direct all application writes to the replica.
- C. Keep the standalone instance and configure application connection retries with a longer timeout.
- D. Configure regional high availability with a primary and standby in different zones, and support reconnection after failover.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 6

A team wants fast, repeatable local tests for a Python repository layer that uses the Firestore server client library. Tests must create and delete synthetic documents without contacting a production database or requiring production credentials. A Firestore emulator already runs on `127.0.0.1:8080`, but the test process still attempts to reach the hosted service. Which change is appropriate, and how should the team interpret passing emulator tests?

**Select one.**

- A. Grant the developer production database access; use a test collection and treat successful tests as production-equivalence proof.
- B. Set `FIRESTORE_EMULATOR_HOST=127.0.0.1:8080` for the test process and use a test project ID; retain separate checks for production-specific behavior.
- C. Set `FIRESTORE_EMULATOR_HOST=https://firestore.googleapis.com` and use a test project ID to redirect requests to localhost.
- D. Keep the client configuration unchanged and mock only credential loading; the library will automatically discover the local emulator port.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 7

A GKE Deployment has four healthy replicas. During a planned image rollout, the application must retain at least four available replicas, and the cluster has capacity for one additional Pod. Readiness checks correctly indicate when a new Pod can serve traffic. Old Pods terminate promptly, and unrelated failures are outside this rollout requirement. The team accepts a slower rollout to preserve capacity. Which rolling-update settings express the intended behavior?

**Select one.**

- A. `maxUnavailable: 1` and `maxSurge: 0`.
- B. `maxUnavailable: 1` and `maxSurge: 1`.
- C. `maxUnavailable: 0` and `maxSurge: 1`.
- D. `maxUnavailable: 0` and `maxSurge: 0`.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 8

A report service uploads a Cloud Storage object under a unique operation name. It must create the object only if no live object with that name exists. Occasionally, the upload succeeds but the client loses the response, leaving the result uncertain. Retrying must never overwrite an existing report, whether it came from the first attempt or another authorized writer. Which upload precondition and retry behavior best preserve the requirement?

**Select one.**

- A. Use `ifGenerationMatch=0` on every attempt; after a precondition failure, verify the existing object's operation metadata rather than overwriting it.
- B. Use `ifGenerationNotMatch=0` on every attempt and interpret any upload success as proof that the name was previously unused.
- C. Check that the object is absent, then upload without a precondition; repeat both operations after every timeout.
- D. Enable Object Versioning and upload without a precondition, treating any resulting noncurrent version as a failed attempt.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 9

An API is already exposed through Apigee. Each authenticated partner has a verified application identifier, and the proxy already rejects invalid credentials. Each partner is entitled to a fixed number of requests during each quota interval, regardless of how many backend instances handle its traffic. A separate policy already protects the backend from sudden request spikes. Which addition most directly enforces the contractual per-partner allowance?

**Select one.**

- A. Add another SpikeArrest policy using one shared counter for all partners.
- B. Configure a Quota policy keyed by the verified partner identifier, using the required interval and allowance.
- C. Configure a response cache keyed only by the request path, allowing cache hits to establish each partner's allowance.
- D. Limit the maximum number of Cloud Run backend instances and derive each partner's request allowance from that limit.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 10

A developer uses Gemini Code Assist to generate unit tests for a payment-calculation module. The module reads the current time and calls an external exchange-rate API. Generated tests currently use the live API and assert values copied from the implementation, so results vary and an incorrect rounding rule remains undetected. The documented business contract specifies rounding boundaries and behavior when the rate provider times out. Which revision best makes these tests useful in CI?

**Select one.**

- A. Keep the live API and increase test retries until temporary failures no longer cause the build to fail.
- B. Mock the module's final return value, then assert that the test receives the same mocked value.
- C. Accept the generated assertions because they match the implementation, and use line coverage as the sole acceptance criterion.
- D. Supply the contract and test conventions as context; control time and API responses, and review assertions for boundary and failure cases.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 11

A Cloud Run function implemented as a CloudEvent handler should process an image after a new object generation has been successfully created in the `incoming-images` Cloud Storage bucket. It must not run merely because an existing object's custom metadata changes. The bucket and trigger locations are compatible, the trigger identity has the required permissions, and invocation of the destination already works. Which direct Eventarc event-filter pair selects the required events?

**Select one.**

- A. Type `google.cloud.storage.object.v1.metadataUpdated` and bucket `incoming-images`.
- B. Type `google.cloud.storage.object.v1.finalized` and bucket `processed-images`.
- C. Type `google.cloud.storage.object.v1.finalized` and bucket `incoming-images`.
- D. Type `google.cloud.storage.object.v1.deleted` and bucket `incoming-images`.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 12

A checkout request calls inventory and payment services over HTTP. Each service exports spans, but the tracing system shows three unrelated traces rather than a single end-to-end request. Logs contain useful local timestamps, yet operators cannot reliably determine which downstream call caused a slow checkout. Sampling is already configured consistently. Which change should the team make at service boundaries to preserve the causal relationship between spans?

**Select one.**

- A. Inject the active trace context into outgoing requests and extract it downstream so server spans continue the caller's trace with appropriate parent relationships.
- B. Create a new random trace ID at every service and give all spans the same display name.
- C. Increase log retention and join requests using timestamp equality, leaving HTTP headers and span parents unchanged.
- D. Reuse one constant trace ID for all checkout requests so every service's spans appear together.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 13

An external CI platform can issue OIDC tokens containing a trusted issuer and repository-specific claims. A build from one approved repository must upload artifacts to one Artifact Registry repository without storing a Google service-account key. Builds from unrelated repositories must not gain the same access. The team chooses Workload Identity Federation with direct resource access, which is supported for this operation. Which TWO configuration changes establish this boundary?

**Select two.**

- A. Grant repository write access to every identity from the external CI issuer, relying only on the issuer being trusted.
- B. Create a workload identity pool and OIDC provider, map the required claims, and restrict accepted identities to the approved repository through an attribute condition.
- C. Download a service-account key and rotate it daily through the external platform's encrypted variables.
- D. Grant Artifact Registry Writer on the target repository to the appropriately restricted federated principal or principal set.
- E. Grant Artifact Registry Writer to the account of the developer who created the workload identity pool, without authorizing the federated identity.

**İki cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 14

A Cloud Build pipeline runs integration tests against an image stored in Artifact Registry. Production runs on GKE. The organization wants an admission-time control that rejects an image unless a trusted verification process has approved that exact digest after the required tests. Developers with deployment permissions must not satisfy the requirement merely by assigning an image the tag `tested`. Cluster policy administration is controlled separately. Which design best implements this release gate?

**Select one.**

- A. Require every production image to have a tag containing the build number and let developers update the tag after testing.
- B. Enable vulnerability scanning and assume that a scan automatically proves all integration tests have passed.
- C. Record test output in Cloud Logging and ask deployers to inspect the log before each deployment.
- D. Have the trusted process create a digest-bound attestation only after checks pass, and enforce that attestation through Binary Authorization policy.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 15

A Cloud Run HTTP service maintains a disposable in-memory reference cache. While an instance exists, a background loop should occasionally refresh the cache even when no request is being handled. Missing a refresh is acceptable, and the application safely recreates the cache after an instance restart; this is not durable job processing. The service already has one minimum instance but uses request-based billing, and the loop makes little progress during idle periods. Which configuration change directly provides CPU outside request processing?

**Select one.**

- A. Increase the request timeout while retaining request-based billing.
- B. Switch the service to instance-based billing, retaining appropriate minimum instances and restart-safe cache initialization.
- C. Increase maximum instances while retaining request-based billing and the current minimum.
- D. Enable session affinity while retaining request-based billing so idle instances receive CPU.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 16

A Firestore transaction reads an order, updates its state, and calls an external payment API inside the transaction callback. Under contention, the callback may run again, and the payment provider sometimes receives multiple charge requests for the same order. The provider supports idempotency keys. You need database updates to remain transactional while making payment execution recoverable across process crashes. Which redesign best addresses both requirements?

**Select one.**

- A. Call the provider first inside the callback, then return immediately so the transaction cannot retry.
- B. Catch all transaction conflicts and report success to the customer, even if the order state was not committed.
- C. Atomically write the order change and a pending-payment record; process that durable record separately using a stable provider idempotency key and retry-safe status updates.
- D. Move the provider call after the transaction and track completed payments only in the current process's memory.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 17

A company stores finalized audit exports in Cloud Storage. Each object must remain undeletable and nonreplaceable until its required retention period has elapsed. The organization also requires that administrators cannot later shorten or remove the bucket retention policy to bypass that protection. Legal and operational review has approved making the policy irreversible. Which configuration directly meets these requirements?

**Select one.**

- A. Configure the required bucket retention period and lock the retention policy after validating it.
- B. Enable Object Versioning and give administrators permission to delete noncurrent object generations.
- C. Configure an Object Lifecycle Management rule to delete objects when they reach the required age, without a retention policy.
- D. Configure the retention period but leave the policy unlocked so administrators can reduce it during an emergency.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 18

A Cloud Build pipeline needs a private package-registry token in exactly one dependency-download step. The token is stored in Secret Manager, and a dedicated build service account is configured for this build. The runtime application does not need the token. The team must avoid committing it, placing it in ordinary build substitutions, or persisting it in the produced image. Which TWO actions provide the required access and injection? Assume the step's script also avoids printing or persisting the secret.

**Select two.**

- A. Grant Secret Manager Secret Accessor only to the application's runtime service account.
- B. Put the plaintext token in a normal substitution variable and pass it to every build step.
- C. Grant the configured build service account Secret Manager Secret Accessor on the specific secret.
- D. Copy the token into the Docker build context and remove the file only after the image has been pushed.
- E. Map the secret version through `availableSecrets` and expose its environment variable only in the consuming step's `secretEnv` list.

**İki cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 19

A GKE application keeps restarting during startup after a release that increases initialization time to roughly two minutes. Its existing liveness probe begins checking almost immediately and restarts the container before initialization finishes. Once initialized, the liveness endpoint correctly detects deadlocks and should continue detecting them promptly. Readiness checks already prevent premature traffic. Which addition accommodates slow initialization without permanently slowing steady-state deadlock detection?

**Select one.**

- A. Replace the liveness probe with readiness only, relying on removal from traffic to restart deadlocked containers.
- B. Add a startup probe with a sufficient failure budget; let the existing liveness and readiness probes take over after startup succeeds.
- C. Increase the liveness probe's failure threshold so every deadlock, including one after hours of uptime, is tolerated for several minutes.
- D. Increase the Deployment replica count but retain the same early liveness checks on every new Pod.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 20

A vendor application must run on a vendor-certified Linux image with a custom kernel configuration and a host-level driver. Its support agreement does not permit packaging the application as a container. The vendor has confirmed that the image can run on Compute Engine's virtual hardware, and the team accepts responsibility for operating-system patching. The service must remain running to accept its own TCP protocol. Which deployment option meets these constraints most directly?

**Select one.**

- A. A Cloud Run service built from the application's source with a longer HTTP request timeout.
- B. A GKE Autopilot Deployment using an init container to replace the node's operating-system kernel.
- C. A Cloud Run job that modifies the host kernel at startup and then listens indefinitely.
- D. A Compute Engine VM created from the compatible custom image, with the required network and operating-system configuration.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

---

**Toplam süre:**

**Dil desteği alınan sorular / takıldığım ifadeler:**

**İlk defa karşılaştığım teknik konular:**

Kaydedince “bitti, kaydettim” de. [Cevap anahtarı — yalnız çözümden sonra aç](../answers/scenarios/PCD-S04.md) · [Senaryo dizini](README.md)
