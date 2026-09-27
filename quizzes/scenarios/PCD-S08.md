# PCD-S08 — Öğretici karma deneme

**50 soru · 44 tek seçim + 6 çift seçim · 5 çalışma bölümü**

Bu set güncel Professional Cloud Developer exam guide’ın dört ana alanını ve 11 numaralı alt başlığını örnekler. Sorular özgün çalışma sorularıdır; gerçek sınav soruları değildir. Zorluk hedefi resmî sample’dan biraz daha yüksek, önceki setlerin niş ayrıntılarından daha temel bir düzeydir; resmî zorluk eşdeğerliği ölçülmüş değildir.

İngilizce paragraflar uzun tutuldu; kararlar temel kullanım kuralları ve belirgin gereksinimler üzerinden kuruluyor. Önceden görülen bazı konular bilinçli pekiştirmedir. Ayrıntılı konu ve kaynak eşleştirmesi ayrı cevap anahtarındadır.

**Çalışma biçimi:** İlk turda anahtarı açmadan çöz. İstersen her 10 soruda dur ve cevaplarını gönder. Süreni kaydet; bu öğretici turda zorunlu bitiş süresi yok. E = eminim, K = iki seçenek arasında kaldım, T = tahmin ettim. Her soruda uzun gerekçe yazman gerekmiyor; kararsızlarda bir cümle yeterli. Çeviri veya açıklama sonrası yanıtları ilk seçimden ayrı kaydedeceğiz.

Çift seçim gereken sorular açıkça **Select TWO** diye işaretlidir. Diğerlerinde en iyi tek yanıtı seç. Değerlendirmede çift seçim ancak iki doğru seçenek birlikte seçildiğinde doğru sayılır.

## Bölüm 1 — Sorular 1–10

Süre: ___ dakika

### Question 01

**Select ONE.**

A team is moving an existing HTTP application to Google Cloud. The application stores durable data in a managed database and does not depend on local files between requests. Traffic is low overnight and rises sharply during business hours. The team can package the application as a container, but has no requirement for Kubernetes APIs, privileged host access, or custom operating-system modules. It wants automatic request-driven scaling and minimal infrastructure administration. Occasional cold-start latency is acceptable, and the database is reachable from the chosen platform. Which deployment choice best meets these requirements without introducing infrastructure that the application does not currently need?

A. Run the container on one Compute Engine VM sized for peak demand and keep that capacity continuously available.

B. Use a Cloud Run job and start a new execution for each incoming interactive HTTP request.

C. Use a GKE Autopilot cluster with an HTTP Deployment and HPA, accepting Kubernetes configuration and workload management for this application.

D. Deploy the container as a Cloud Run service and configure its runtime identity, connectivity, and scaling settings.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 02

**Select ONE.**

A developer can read a test bucket with the gcloud command-line tool after signing in, but a local application using an official Google Cloud client library reports that default credentials are unavailable. No credential-file environment override is set, and the approved developer account already has the needed test-bucket permission. The same application will use an attached service account in production, so the developer wants to preserve the library's normal credential discovery instead of adding a key file or hard-coded token. Which local setup step supplies the application with credentials while keeping command-line authentication and application authentication conceptually separate?

A. Add the developer’s password to the application configuration so the client library can sign in directly.

B. Configure local Application Default Credentials with the approved account, then let the client library discover them.

C. Create and commit a service-account JSON key so both local and production code always read the same file.

D. Change only the active gcloud project and assume selecting a project creates application credentials.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 03

**Select ONE.**

A team runs an HTTP application on GKE with three identical replicas. An engineer fixes a configuration problem by editing one running Pod, but the change disappears when that Pod is replaced. Clients also use individual Pod IP addresses and lose connectivity when replacements receive new addresses. The application needs the same configuration on all replicas and a stable internal endpoint for other services in the cluster. The team already has suitable nodes and does not need to change its external ingress. Which approach best makes the configuration persistent across replacements and provides stable service discovery without assigning fixed addresses to individual Pods?

A. Create a Service for the current Pods but continue applying configuration changes only to individual running Pods.

B. Update the Deployment’s Pod template and route clients through a Service that selects the application’s Pods.

C. Edit every current Pod separately and publish their current IP addresses in the client configuration.

D. Increase node count and keep clients connected to whichever Pod IP address was created first.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 04

**Select ONE.**

A Cloud Run service connects to Cloud SQL using an approved authenticated connector. Authentication and networking work correctly, but traffic spikes create too many database connections. Each request opens a new connection and leaves it available longer than necessary. The database has a known connection budget, and the service may scale to many instances. The team wants to reuse connections while preventing the combined application instances from overwhelming the database. It can set application pool limits and a reasonable service instance limit, with headroom for administration and other clients. Which approach best addresses this problem without confusing secure connectivity with connection-capacity management?

A. Reuse a bounded connection pool per instance and size the pool and instance limits together against the database connection budget, with headroom.

B. Limit the service to one database connection globally without considering request demand or allowing application instances to reuse their own connections.

C. Keep creating connections per request and rely on the authenticated connector to provide an unlimited server-side connection budget.

D. Set every instance’s pool maximum equal to the database’s entire connection budget so each instance can use the available capacity.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 05

**Select ONE.**

A shopping application keeps each user's unfinished cart only in the memory of the Cloud Run instance that handled the first request. Session affinity improves the chance that later requests reach the same instance, but customers sometimes lose their carts after scaling or instance replacement. The cart must survive replacement of an instance, and the business cannot accept losing acknowledged cart changes when a disposable cache disappears. The team still wants low-latency reads and can use Memorystore for frequently accessed copies. Requests already contain an authenticated customer identifier. Which state-management design meets the durability requirement while allowing affinity and caching to remain optional performance optimizations?

A. Use one minimum instance and assume that Cloud Run will preserve that exact process and its memory indefinitely.

B. Store authoritative carts in a durable shared datastore, and use customer-scoped cache entries as replaceable copies.

C. Keep carts only in instance memory and increase session-affinity duration to make the instance durable.

D. Move the only copy of every cart into a disposable cache and remove the durable datastore from the write path.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 06

**Select ONE.**

A developer uses Gemini Code Assist inside the team's approved IDE to add a small feature. The first suggestion uses a library API that is not present in the repository's pinned dependency version. The relevant interface, dependency file, coding conventions, and a working example can all be supplied without exposing prohibited data. The public application interface must stay compatible with existing callers. The developer wants assistance with implementation but remains responsible for reviewing the change. Which next step is most likely to improve the suggestion while preserving the project's actual constraints rather than changing the project merely to fit the generated code?

A. Ask for the same suggestion again without supplying missing context and treat repeated output as verification.

B. Provide the relevant repository context and compatibility constraints, then compile, test, and review the proposed change.

C. Upgrade dependencies and change public interfaces automatically to match whichever API the assistant suggested.

D. Accept the suggestion if its explanation sounds confident, postponing compilation until after production deployment.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 07

**Select TWO.**

A GKE application needs several minutes to load its local configuration before it can accept requests. Its liveness probe currently starts immediately and repeatedly restarts the container during normal initialization. After startup, a brief outage of a required downstream service should stop new traffic reaching the affected Pod, but restarting the application would not repair that downstream service. A separate local health check can detect a genuinely stuck application process. The team wants to distinguish these conditions instead of using one check for everything. Which TWO changes best address slow initialization and temporary inability to serve traffic while preserving meaningful detection of a stuck process?

A. Use readiness to remove an unavailable Pod from service traffic, while keeping liveness focused on conditions a restart can repair.

B. Use a larger replica count as the only fix and leave the premature startup restarts unchanged.

C. Remove readiness and accept traffic immediately whenever the container process exists.

D. Make liveness fail whenever the downstream service is unavailable so that every dependent Pod restarts together.

E. Configure a startup probe with enough time for normal initialization before the other probes take effect.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 08

**Select ONE.**

An organization is launching two web applications. The first is an internal operations dashboard used only by an approved employee group, and the team wants an identity-aware access gate before requests reach the application. The second is a customer application that needs end-user sign-in with supported identity providers and application-specific authorization after sign-in. Customers should not receive project IAM administration roles simply to use the product. The applications have separate audiences and access policies. Which pairing best matches these two identity problems while keeping infrastructure access for employees separate from customer authentication inside the public-facing product?

A. Use an API key as each employee’s identity and grant all customers project Viewer to enable sign-in.

B. Use a single shared service-account key in both browsers so employees and customers authenticate as the same backend identity.

C. Use IAP for the employee dashboard and Identity Platform for customer sign-in, retaining application authorization.

D. Use Identity Platform only for both applications and assume customer sign-in automatically creates the required employee-group gate before the internal backend.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 09

**Select ONE.**

An order service publishes an event after each order is committed. Both the shipping application and the analytics application need their own opportunity to process every event. Each application may run several worker instances to distribute its processing load. Currently, all workers from both applications pull from one subscription, so an event processed by shipping is often never seen by analytics. The applications already make their writes safe for redelivery. The team wants independent consumption and acknowledgment progress for the two applications while still sharing work among replicas of the same application. Which subscription arrangement best matches these requirements without changing the publisher to send duplicate events?

A. Create a separate subscription for each application on the same topic, and let workers within each application share that application’s subscription.

B. Let shipping acknowledge events before analytics reads them from the same subscription, because acknowledgments apply only to the worker that sent them.

C. Keep one subscription for both applications and increase its acknowledgment deadline so every worker receives every event.

D. Create one topic per worker and require the publisher to discover every worker before publishing each order.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 10

**Select ONE.**

A developer has a small HTTP application written in a language supported by Google Cloud buildpacks. The repository contains the required dependency manifest and a valid application entry point, but no Dockerfile. The service fits Cloud Run’s execution model, and the developer wants a managed path from source code to a deployed service without maintaining a custom container build recipe. Required APIs, build permissions, and runtime permissions are already configured. There is no need for an unsupported operating-system package or custom build process. Which deployment approach best satisfies this requirement while still producing a container image that Cloud Run can execute?

A. Run the application permanently in an interactive Cloud Shell session and use that session as the production endpoint.

B. Create a GKE cluster because Cloud Run always requires a manually authored Dockerfile even for supported source code.

C. Deploy the source to Cloud Run using its supported source deployment path, allowing buildpacks and the managed build process to produce the image.

D. Upload only the dependency manifest to Cloud Storage and use the bucket as a running HTTP application.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

## Bölüm 2 — Sorular 11–20

Süre: ___ dakika

### Question 11

**Select ONE.**

A company wants developers to use centrally maintained development environments with an approved toolchain and access to private development services. Project working files must survive normal workstation stop and start cycles, while updates to shared tools should come from a versioned environment image rather than manual installation by each developer. The organization can configure a persistent home directory and the required network access. This requirement is broader than occasionally opening a browser terminal to run administrative commands. Which arrangement best provides the managed development environment while preserving both individual working files and reproducibility of the common toolchain?

A. Use Cloud Shell as though it were the centrally configured workstation fleet, without configuring the required private development environment.

B. Use one personal laptop as the shared environment and ask every developer to copy its manually installed tool versions.

C. Use Cloud Workstations with a managed custom image and configured persistent home storage for working files.

D. Keep uncommitted work only in a running container’s temporary filesystem and avoid stopping the workstation.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 12

**Select ONE.**

A regional application uses Cloud SQL for PostgreSQL configured for high availability across zones in one region. The application team now needs a disaster-recovery plan for an outage affecting that entire region. The business accepts a small, documented amount of possible data loss and a controlled recovery procedure; it has not required automatic zero-loss regional failover. The team can run the application in a second region and maintain a cross-region read replica. It wants to preserve the existing PostgreSQL application and test the recovery process before relying on it. Which plan addresses the new failure scope rather than only repeating the protection already provided inside the primary region?

A. Maintain a cross-region replica and a tested promotion and application-reconnection procedure, accounting for replication lag.

B. Add another application instance in a different zone of the original region and keep the database recovery plan unchanged.

C. Treat the existing regional HA standby as protection against losing every zone in that region.

D. Use the cross-region replica but document zero data loss as guaranteed merely because it is a managed replica.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 13

**Select ONE.**

A GKE service uses a Horizontal Pod Autoscaler based on a valid CPU utilization target. During a traffic increase, the HPA raises the desired replica count as expected. Several new Pods remain Pending because their resource requests cannot fit on the existing nodes. Their images, permissions, and scheduling constraints have been checked and are correct. The node pool is allowed to grow within the project’s quota and budget, but node autoscaling is currently disabled. The team wants the application to add processing capacity automatically during these bursts. Which change best complements the existing HPA and addresses the specific reason that the additional replicas are not running?

A. Remove resource requests from all Pods so the scheduler can ignore the application’s actual capacity needs.

B. Lower readiness thresholds so that Pending Pods are considered ready before they receive a node.

C. Enable and appropriately bound cluster autoscaling for the eligible node pool so that unschedulable Pods can trigger additional node capacity.

D. Raise only the HPA maximum replica count because desired replicas automatically create nodes even without node autoscaling.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 14

**Select ONE.**

Two customers can attempt to reserve the final available item at nearly the same time. The application stores the remaining quantity in a Firestore document and currently reads the value before performing an unrelated write. This sometimes lets both requests report a successful reservation. The team wants the inventory check and decrement to behave atomically. It also sends a confirmation email, which must not be sent multiple times merely because the database transaction retries its callback after a conflict. A durable reservation identifier can be used by the notification process. Which implementation best protects inventory correctness and keeps external side effects out of a retried transaction callback?

A. Keep the separate read and write, but send the email first so customers receive a fast response even when inventory changes.

B. Use a batched write without a transactional read and assume it automatically checks that the quantity read earlier is still current.

C. Send the email inside the transaction callback and assume the callback runs only once whenever the transaction eventually commits.

D. Use a transaction to check and decrement inventory and record the reservation; process the confirmation separately with deduplication based on the durable reservation.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 15

**Select TWO.**

A GKE application needs to read one private Cloud Storage bucket using a supported client library. The cluster is already configured for Workload Identity Federation for GKE, and the network path to Google APIs works. The application currently uses a shared default Kubernetes ServiceAccount, but the team wants to distinguish this application from unrelated workloads. Downloaded service-account keys are prohibited, and no other namespace needs bucket access. Kubernetes NetworkPolicies are used separately to restrict application-to-application traffic. Which TWO actions establish the application’s Google Cloud identity and permission without assuming that network access itself authorizes reading the bucket?

A. Grant the corresponding federated workload principal the required read role on the specific bucket.

B. Grant the read role only to the developer who applied the Deployment, leaving the workload principal unauthorized.

C. Allow additional network traffic and omit bucket IAM, treating a reachable endpoint as an authorized resource.

D. Configure the Pods to use a dedicated Kubernetes ServiceAccount for this application.

E. Put a downloaded service-account key into every Pod so the existing federation configuration is unnecessary.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 16

**Select ONE.**

A Firestore service needs fast local tests for document reads, writes, and business rules around application data. Developers must be able to run these tests without modifying production records or depending on a live cloud database during every edit. The team also needs confidence that production IAM permissions, network configuration, and deployed-service integration work correctly before release. It can run a separate integration stage against isolated cloud test resources. Which testing setup uses local emulation effectively without treating the emulator as a complete replacement for validating the deployed environment and its security configuration?

A. Mock every client-library return value and remove both emulator and cloud integration tests from the release process.

B. Use the emulator for data behavior and assume every production IAM and network setting is proven by those local tests.

C. Run all local tests against the production database and delete test documents later using a name prefix.

D. Point local tests at the Firestore emulator and run separate isolated cloud integration checks for production-relevant configuration.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 17

**Select TWO.**

A private Cloud Run billing service must be called by an orders service running under its own dedicated service account. Network routing and ingress already permit the connection, but the request is rejected because application-level invocation authentication has not been configured. The team wants to grant only the required caller access and use Google-managed credentials instead of a downloaded service-account key. The receiving service uses its standard Cloud Run service URL, with no custom audience configuration. Which TWO actions establish the appropriate authorization and request authentication for this service-to-service call without making the billing service publicly invokable?

A. Have orders obtain and send an ID token whose audience is the billing service URL.

B. Grant the billing service account Invoker on orders and assume that permission authorizes calls in both directions.

C. Grant the orders runtime service account the Cloud Run Invoker role on the billing service.

D. Give all users permission to invoke billing so that internal callers no longer need authenticated requests.

E. Send an OAuth access token with the orders service URL as its audience instead of the required invocation ID token.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 18

**Select ONE.**

A Firestore application stores a support case as one document containing its title, owner, current status, and an array of every message ever added to the case. Cases can remain open for years, and users normally request only the latest twenty messages rather than the entire history. Different users may add messages concurrently. The growing array makes each case document increasingly large and turns unrelated message additions into updates to the same parent document. The team wants to keep case summaries easy to read while querying message history in pages. Which data-model change best matches those access patterns without discarding the conversation history?

A. Replace the message history with a count and delete the message contents after each summary update.

B. Keep the entire history in the parent array and fetch every message whenever the case title is displayed.

C. Store all cases and all messages in one global document to reduce the number of document identifiers.

D. Keep summary fields in the case document and store messages as separate documents in a messages subcollection with suitable query indexes.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 19

**Select ONE.**

A desktop application uploads large files to a private Cloud Storage bucket over an unreliable connection. The current implementation restarts an entire file whenever the network drops, wasting bandwidth and delaying completion. Authentication, permissions, and the destination bucket are already configured correctly. The application can retain upload-session information securely and query the server to determine how much data has been accepted. It does not need to make objects public or split every file into separately visible objects. Which upload strategy best supports recovery from interrupted transfers while preserving the original object and avoiding unnecessary retransmission of bytes already stored during the active upload session?

A. Repeat an ordinary full upload from byte zero after every disconnect because the bucket automatically discards all previously accepted bytes.

B. Use a resumable upload, retain its session information securely, and resume from the server-confirmed committed offset after an interruption.

C. Change the bucket to public access because public objects allow the network connection to remain available during outages.

D. Use a larger download page size to make the upload resume automatically without keeping any upload-session state.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 20

**Select ONE.**

A team builds a container, runs tests against it in staging, and later rebuilds the same source commit for production. Occasionally the production image differs because a base image tag or external dependency changed between builds. Environment-specific settings are already supplied at deployment time and do not need to be baked into the container. The team wants production to receive exactly the artifact that was tested, while still allowing different configuration values in staging and production. Which release practice best preserves artifact identity across environments without assuming that identical source code always produces identical image contents at different times?

A. Bake production credentials into the staging-tested image so that configuration changes can never occur during deployment.

B. Build once, store the image in Artifact Registry, and promote the tested immutable digest with environment-specific deployment configuration.

C. Rebuild separately for every environment and use the same mutable image tag to imply that all builds are identical.

D. Copy only the source commit label into the new production image and skip comparing the resulting artifact.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

## Bölüm 3 — Sorular 21–30

Süre: ___ dakika

### Question 21

**Select ONE.**

A batch worker on GKE repeatedly terminates with an OOMKilled status while processing supported input files. Monitoring shows that its memory use exceeds its configured memory limit, even though its node has enough allocatable memory for a larger, realistic request. The workload is not receiving HTTP traffic, and adding replicas would not reduce the memory needed by one task. The team has profiled the worker and identified a reasonable per-task memory requirement within its budget. It wants to keep memory protection while allowing valid tasks to complete. Which change best addresses the observed failure and gives the scheduler an honest view of the worker’s resource needs?

A. Keep the low memory limit and add an HTTP readiness probe so that memory-intensive tasks can complete.

B. Increase only the CPU limit because the node’s unused memory automatically overrides a container’s memory limit.

C. Set a suitable memory request and a sufficiently large memory limit based on the measured per-task requirement.

D. Increase the number of replicas without changing per-task input or each container’s memory configuration.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 22

**Select ONE.**

A service calls an external supplier using a credential that must rotate regularly. The credential is currently included in the container image, so changing it requires rebuilding the image and leaves old copies in the artifact history. The team can store the credential in Secret Manager and deploy with a dedicated runtime service account. It needs a controlled rotation process with a short overlap while clients switch, and only this service should read this particular secret. Encryption-key administration is handled separately through Cloud KMS. Which design best separates secret access and rotation from the application artifact while preserving a narrow runtime permission boundary?

A. Rotate a Cloud KMS key and assume the external supplier automatically changes its password and every running process refreshes its cached value.

B. Store credential versions in Secret Manager, grant the runtime identity access to that secret, and coordinate client refresh before retiring the old credential.

C. Put the credential in a Docker build argument and rotate only the image tag while leaving the embedded value unchanged.

D. Grant the runtime identity project-wide Owner so that it can retrieve and rotate any supplier credential without separate policies.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 23

**Select ONE.**

A compiled application is built with a large toolchain, but production needs only the resulting executable and its runtime dependencies. The current Dockerfile leaves source files and compilers in the final image. It also copies all frequently changing source files before downloading dependencies, causing expensive dependency installation to repeat after small code changes. The team can use a supported runtime base and separate build stages. It wants a smaller production image and better reuse of unchanged dependency layers without omitting required runtime libraries. Which Dockerfile structure best addresses both concerns while keeping the actual application build and tests reproducible?

A. Copy the entire build-stage filesystem into the final stage so that no runtime dependency analysis is needed.

B. Move source copying before every dependency step and disable layer caching to improve incremental build speed.

C. Install dependencies from their manifests before copying changing source, build in one stage, and copy required runtime outputs into a separate final stage.

D. Remove all runtime libraries from the final image without checking whether the compiled application needs them.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 24

**Select TWO.**

A backend will call a Google Cloud API using its dedicated runtime service account and Application Default Credentials. The target API has not been enabled in the project used for the request, and the service account has not been granted the resource permission required by the intended operation. The client library and request format are otherwise correct. The team wants an application identity with the minimum required access, without distributing a developer’s personal credentials or a downloaded service-account key. Which TWO setup actions address the explicitly identified configuration gaps while keeping API availability and authorization as separate parts of the integration?

A. Add an API key to the request and treat it as a replacement for service-account authorization on the protected resource.

B. Grant the runtime service account the narrow role or permissions needed for the target operation at an appropriate resource scope.

C. Use a developer’s long-lived downloaded credentials in every production instance so project configuration no longer matters.

D. Have an authorized administrator or deployment process enable the required API in the applicable project.

E. Grant the runtime service account permission only to enable APIs and assume that also authorizes every data operation.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 25

**Select ONE.**

A new reservation platform requires relational transactions that update several related records consistently. Its planned write workload must scale horizontally, and the architecture calls for a managed database supporting strong transactional behavior across a multi-region deployment. The application is new, so preserving existing PostgreSQL extensions or wire-level compatibility is not a constraint. The team wants to avoid building its own database sharding and cross-shard transaction layer. Reporting is secondary to the transactional reservation path. Which datastore is the most direct fit for these stated requirements, assuming the team selects an appropriate instance configuration and designs its schema for distributed workloads?

A. Use Cloud Storage objects and implement joins and multi-object transactions entirely in application code.

B. Use a single-region AlloyDB primary with additional read-pool instances to satisfy horizontally scaled multi-region transactional writes.

C. Use BigQuery as the primary low-latency row-by-row reservation transaction database.

D. Use Spanner for the distributed relational transaction workload.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 26

**Select ONE.**

An Eventarc trigger delivers Cloud Storage object-finalized events to a Cloud Run service. The trigger’s identity, destination permission, and network access are already working. The current handler expects a browser form and returns success before saving any durable record of the event. Some uploads are therefore never processed after a container stops, and redelivered events occasionally create duplicate processing records. Processing can be scheduled through an existing durable work queue. The team needs the receiver to understand the event format and acknowledge accepted work reliably. Which handler design best fits this delivery model without assuming that an event will be delivered only once?

A. Store the event only in instance memory, return success, and rely on the same instance remaining available until work finishes.

B. Parse the CloudEvent, deduplicate using a stable event or object-generation identity, durably record or enqueue the work, and then acknowledge successful acceptance.

C. Return an error after every completed operation so Eventarc repeatedly delivers the event until a human confirms completion.

D. Continue parsing only browser form fields and return success immediately so Eventarc can infer the missing object information.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 27

**Select ONE.**

An approved coding assistant can use an MCP server from the developer's IDE to retrieve internal API documentation and inspect test-system metadata. For this task, it does not need to change production resources, read production secrets, or grant IAM roles. The MCP server can expose separate read and write tools and uses credentials whose permissions are configurable. The team wants the assistant to remain useful while limiting the consequences of an incorrect tool choice or misleading retrieved text. Which configuration best enforces the intended access boundary in the available tools and credentials, rather than relying only on a sentence in the assistant's prompt?

A. Disable all documentation access but continue exposing production secret and IAM modification tools.

B. Expose only the needed read tools and use credentials restricted to the approved documentation and test resources.

C. Expose every production administration tool with Owner credentials and ask the assistant to be careful.

D. Keep broad credentials and assume a read-only label in a tool description technically blocks write operations.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 28

**Select ONE.**

Every weekday morning, a company starts a report process that calls three services in sequence. The second call depends on the first result, and a later branch depends on whether validation succeeds. Transient failures need bounded retries, and operators want to inspect the state of each execution without building a custom coordination database. The services already expose authenticated endpoints and finish their individual operations within supported limits. This is one scheduled business process, not a stream of unrelated HTTP requests that must be rate-limited against a partner. Which combination provides the recurring start and the stateful coordination with the least custom application logic?

A. Put all three HTTP calls into unrelated Cloud Tasks and use queue order as the only record of workflow state.

B. Use three independent Cloud Scheduler jobs at approximate time offsets and assume earlier calls always finish first.

C. Use Cloud Scheduler to start a Workflows execution that defines the calls, branches, and retry behavior.

D. Publish one Pub/Sub message to three independent subscribers and assume subscription delivery order enforces the dependencies.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 29

**Select ONE.**

An application lists resources through a Google Cloud API that explicitly supports pagination, a field-selection option, and normal HTTP caching rules. It needs only resource names and update times, but currently requests every field on every refresh and assumes the first response contains the complete collection. Users can accept results that are up to one minute old, provided that authorization boundaries are respected. The supported client library exposes page iteration and request options. The team wants complete results with less repeated network traffic rather than an incomplete but fast first page. Which client design best uses the capabilities described without assuming that all Google APIs offer identical options?

A. Request fewer fields and stop after the first page because partial responses automatically combine all remaining pages.

B. Follow all result pages, request only the supported fields needed by the application, and cache results within the permitted freshness and authorization boundaries.

C. Increase the page size beyond the documented maximum and repeatedly retry the invalid request until the API returns the entire collection.

D. Follow all pages but cache the results indefinitely across all users because caching eliminates the need to consider freshness or access.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 30

**Select ONE.**

A Cloud Run job processes a daily dataset that the application divides into twelve independent partitions. Each task uses its task index to select exactly one partition, and retries are already safe because writes are idempotent. A downstream system permits at most three tasks from this execution to run concurrently. The team wants all twelve partitions processed during one execution while respecting that downstream limit. Each task has sufficient CPU, memory, and timeout, and there are no other concurrent executions. Which job configuration best represents the total amount of work and the allowed simultaneous processing without changing the partitioning logic already implemented in the application?

A. Configure twelve tasks and a maximum parallelism of three.

B. Configure twelve tasks and a maximum parallelism of twelve because idempotent writes remove the downstream concurrency limit.

C. Configure one task and a maximum parallelism of three so three copies of every partition are processed automatically.

D. Configure three tasks and a maximum parallelism of twelve so the platform automatically discovers the remaining nine partitions.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

## Bölüm 4 — Sorular 31–40

Süre: ___ dakika

### Question 31

**Select ONE.**

A company stores audit files in Cloud Storage. Compliance requires each file to remain undeletable for its required retention period, and administrators must not be able to shorten that period after the policy is finalized. Files should be removed automatically after protection expires and deletion conditions are met. Separately, organization policy prohibits making these audit buckets public. The compliance team has explicitly approved making the retention commitment irreversible and understands its consequences. Which configuration combines minimum preservation, eventual automatic cleanup, and protection against public exposure without treating any one of those controls as a substitute for the other two?

A. Use Object Versioning alone and assume administrators cannot remove retained generations or expose the bucket publicly.

B. Use only a lifecycle Delete rule and treat its age threshold as protection against earlier manual deletion.

C. Use an approved locked retention policy, a compatible lifecycle Delete rule, and enforced public access prevention.

D. Use public access prevention and assume it also defines the retention period and deletes expired objects automatically.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 32

**Select TWO.**

A Cloud Build pipeline compiles a program and then runs two independent validation steps against the compiled output. Both validations must succeed before a packaging step creates the release artifact. The compiler currently writes into a private temporary directory inside its build-step container, so later steps cannot find the output. The team wants the two validations to run concurrently after compilation, without allowing packaging to bypass either check. Normal nonzero exits already fail the build. Which TWO configuration changes provide the required file sharing and execution dependencies without introducing an external artifact transfer just to communicate within this build?

A. Give all steps the same service account and assume their private /tmp directories become one shared filesystem.

B. Make packaging wait only for compilation so that it can proceed while validations are still running.

C. Make both validations wait for compilation and make packaging wait for both validation step IDs.

D. Set both validation steps to ignore all failures so their completion always permits a production artifact.

E. Write and read the compiled output through the shared /workspace directory or an explicitly shared volume.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 33

**Select ONE.**

A Deployment normally runs three replicas, and a planned application rollout must keep at least three ready replicas available throughout the update. The cluster has enough spare capacity to start one additional Pod, and readiness checks accurately indicate when a new replica can serve traffic. The application already handles shutdown correctly. An engineer proposes relying only on a PodDisruptionBudget that protects against voluntary evictions during node maintenance. The team needs a configuration that directly controls how this Deployment replaces Pods during its rolling update. Which choice best meets the rollout requirement without confusing application updates with the separate protection used for maintenance-related evictions?

A. Use the Recreate strategy so all three old replicas stop before the replacement replicas start.

B. Configure the Deployment rolling update with maxUnavailable set to 0 and maxSurge set to 1; keep an appropriate PDB for voluntary evictions.

C. Set maxUnavailable to 3 and maxSurge to 0 because readiness checks prevent any reduction in replica availability.

D. Set only a PDB and assume it overrides the Deployment’s rolling-update settings during application replacement.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 34

**Select ONE.**

A document-processing team needs text detection for a large set of images already stored in Cloud Storage. Results are needed for a later reporting job, so users are not waiting for an immediate response to each image. The relevant Vision API asynchronous batch operation supports the required image feature and can write output to Cloud Storage. The team wants to avoid holding thousands of application HTTP requests open while processing completes. It can divide submissions according to documented limits and inspect per-image results after completion. Which approach best matches this throughput-oriented workflow while avoiding unnecessary repeat processing when only a subset of images fails?

A. Submit supported asynchronous batches within documented limits, track operation completion and output, and retry only failed items when appropriate.

B. Resubmit all successful images whenever one image fails so the next report contains a completely new processing run.

C. Send every image through one oversized synchronous request and assume batch size limits do not apply to files already in Cloud Storage.

D. Keep one browser request open per image until all processing completes, even though no interactive result is required.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 35

**Select ONE.**

A security reviewer asks where a release image came from and which build produced it. The image already has a source-commit label, a test report, and a vulnerability scan result. The team also needs a verifiable build-origin record tied to the artifact, because a label can be supplied by whoever creates the image. Cloud Build is the approved builder, and the release process can generate and validate its supported provenance metadata. The reviewer is not asking whether the application's business logic is correct or whether every possible vulnerability is absent. Which additional evidence most directly addresses the specific build-origin question?

A. Generate and validate Cloud Build provenance associated with the produced artifact digest.

B. Use only the vulnerability severity count, because a clean scan proves the source and build process.

C. Replace the build-origin requirement with a passing unit-test report, because tests identify who built the artifact.

D. Add a longer human-readable commit label and treat its text as cryptographic proof of the builder.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 36

**Select ONE.**

A telemetry service stores frequent measurements from many devices in Bigtable. Devices have well-distributed identifiers and similar traffic rates. Operators usually retrieve measurements for one known device within a recent time range; separate analytics handles cross-device reports. A proposed row key begins with the measurement timestamp, followed by the device identifier. The team wants writes spread across the key space while keeping each device's time-range reads efficient. It does not need one globally ordered stream of all incoming measurements. Which row-key design best matches the stated balance between distribution and read locality, without turning every device-specific request into a scan of unrelated devices?

A. Lead with the increasing timestamp and append the device identifier so all recent writes remain adjacent.

B. Use a single row for every device and append all measurements to that shared row indefinitely.

C. Lead with the well-distributed device identifier and follow it with a consistently encoded timestamp.

D. Generate an unrelated random row key for every measurement and keep both device ID and time only as cell values.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 37

**Select ONE.**

A GKE cluster runs a frontend, a payments service, and several unrelated workloads. The team wants only the frontend Pods to initiate connections to the payments Pods on the application port. NetworkPolicy enforcement is enabled, the required labels are controlled, and the payments Pods are not already allowed by another policy. Existing Google Cloud IAM roles correctly authorize access to external cloud resources, but they do not implement this Pod-to-Pod traffic rule. The application’s own request authentication must remain enabled. Which configuration best restricts the allowed network path without granting unrelated Pods access or treating network filtering as a replacement for application authentication?

A. Apply a policy allowing the entire cluster to reach every payments port, relying only on Pod names to distinguish trusted callers.

B. Apply the correct network allow rule and remove all application authentication because an allowed connection proves every end-user action is authorized.

C. Grant the frontend’s Google Cloud service account a narrower IAM role and leave all Pod-to-Pod network traffic unchanged.

D. Apply an ingress NetworkPolicy selecting payments Pods and allowing the controlled frontend namespace and Pod selectors on the required port; retain application authentication.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 38

**Select ONE.**

A document portal authorizes customers through its own account system. After checking a customer's purchase, it must allow that customer to download one private Cloud Storage object for a short period. The customer's browser should download directly from Storage so that the portal does not carry the file traffic. Customers do not have Google Cloud identities. The business accepts that anyone holding the temporary link can use it until it expires, and the bucket must remain private for everyone else. Which access mechanism best provides the required object-specific, time-limited download without handing the browser the portal's general Google Cloud credentials?

A. Temporarily make the entire bucket public whenever one customer downloads a document.

B. Create a project-wide IAM role for every customer identifier from the portal’s unrelated account database.

C. Give the browser the portal runtime service account’s general access token and the object path.

D. Generate a short-lived signed GET URL for the authorized object after the portal checks the purchase.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 39

**Select ONE.**

A developer asks an AI coding assistant to create unit tests for a discount calculator. The generated tests copy expected values from the current implementation, including an existing boundary mistake. They also call a live pricing API, so results change when the remote service changes. The business specification defines the correct discount at each boundary, and the calculator can receive its external pricing dependency through an interface. The team wants fast, deterministic tests that detect incorrect business behavior rather than simply reproduce the current output. Which revision best turns the generated tests into a useful check while preserving the real calculator as the code under test?

A. Derive expected results from the business specification, control the external dependency, and test boundary and failure cases against the real calculator.

B. Accept copied implementation values as the test oracle and use line coverage as the only quality criterion.

C. Mock the calculator’s final return value and assert that the same mocked value is returned.

D. Keep the live API and add repeated retries until the tests happen to pass during a stable network period.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 40

**Select ONE.**

A service makes read-only requests to a Google Cloud API. Most calls succeed, but a burst occasionally produces quota-related transient responses or temporary service-unavailable errors. The current code retries immediately in a tight loop, increasing the load and sometimes continuing after the caller’s request deadline. Malformed requests can also occur and will not become valid without changing their parameters. The team uses a client library with configurable retry behavior and wants predictable latency during partial failures. Which retry policy best handles eligible transient failures while avoiding both a retry storm and wasted attempts on requests that require correction rather than more time?

A. Use bounded exponential backoff with jitter for retryable failures, respect the overall deadline and server guidance, and surface nonretryable request errors for correction.

B. Retry every error immediately without a limit because read-only operations cannot create duplicate writes.

C. Use the same fixed short delay on every instance and ignore the overall deadline until a successful response arrives.

D. Retry malformed requests with unchanged parameters for longer than transient failures because a larger retry budget fixes invalid input.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

## Bölüm 5 — Sorular 41–50

Süre: ___ dakika

### Question 41

**Select ONE.**

A public REST API is already deployed as equivalent Cloud Run services in two supported regions. Its authentication and per-customer API policies are implemented correctly. The next requirement is to expose the regional services through one HTTPS entry point with supported regional routing and failover behavior, rather than ask clients to choose a region-specific URL. Shared application data has already been designed for the required regional behavior. The team wants a managed front end and does not need a new API contract or another layer of customer quota management. Which component most directly provides the missing traffic-distribution function for the existing regional backends?

A. Increase maximum instances in the first region while leaving clients connected only to that region-specific endpoint.

B. Configure two independent regional load balancers and require each client to implement region selection and failover between their separate URLs.

C. Configure a global external Application Load Balancer with supported serverless backends for the regional services.

D. Add an Apigee Quota policy to one regional service and rely on the quota counter to select a healthy region.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 42

**Select ONE.**

An operator is investigating a service whose latency increased after a configuration change. The team already collects relevant logs and metrics and wants to use Gemini Cloud Assist to help summarize evidence and suggest possible causes. The service handles production traffic, so proposed changes must be checked against the observed symptoms and the team's normal change process. The operator is not asking the assistant to generate application unit tests or replace the IDE's coding workflow. Which use of the assistant best supports the investigation while keeping the distinction between a plausible suggestion and a verified explanation of the incident?

A. Grant unrestricted production write access so every suggested fix can be applied without checking its effect.

B. Use successful code completion in the IDE as proof that the cloud configuration and incident diagnosis are correct.

C. Treat the first generated explanation as confirmed root cause and remove the original logs and metrics from the investigation.

D. Use Cloud Assist to explore the available cloud evidence, then verify suggested causes and review any proposed remediation before applying it.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 43

**Select ONE.**

A team wants to release a new Cloud Run revision gradually and quickly restore the previous revision if errors increase. Both revisions use the same relational database. The new code introduces an optional database field, while the old revision still reads an existing field that will eventually be retired. No data has been migrated yet, and deleting the existing field during this release would break the old code. The team can postpone destructive cleanup until the rollback window closes. Which release plan best supports both a small initial traffic allocation and a useful rollback path while the two revisions may serve requests at the same time?

A. Delete the old field before the canary begins and rely on restoring traffic to the old revision to recreate deleted database data.

B. Send all traffic to the new revision immediately because traffic splitting cannot coexist with a shared database.

C. Rebuild the old source code after an incident and assume this alone reverses any incompatible database changes.

D. Make an additive, backward-compatible schema change, send a small traffic share to the new revision, monitor it, and postpone destructive cleanup until rollback is no longer required.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 44

**Select TWO.**

A request passes through three services before returning an intermittent error. Monitoring already shows an increased error rate and higher latency, but those aggregate metrics do not identify which downstream call was slow or connect related log entries. Each service emits unstructured messages without shared trace context, and repeated exceptions are difficult to group. The team wants to investigate individual request paths and identify recurring application failures. It can instrument service boundaries and improve log formatting without changing the business logic. Which TWO improvements best provide request-level correlation and useful error grouping while retaining the existing metrics for overall service health?

A. Remove exception details from all logs and replace them with one shared success message to reduce grouping noise.

B. Report exceptions with supported stack-trace and service information so Error Reporting can group recurring failures.

C. Generate a new unrelated trace identifier at every service boundary so cross-service requests remain separated.

D. Increase only the sampling frequency of the same aggregate CPU metric and assume it reconstructs each request’s call path.

E. Propagate trace context across service calls, create useful spans, and attach the corresponding trace identifiers to structured logs.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 45

**Select ONE.**

A release pipeline already checks container images with Artifact Analysis and blocks releases that violate its package-vulnerability policy. A security review now asks the team to look for supported vulnerabilities exposed by the behavior of a running web application, such as issues discoverable through its web endpoints. The team has an authorized, representative test deployment and can configure scanning without targeting unrelated systems. It wants to keep existing image scanning because operating-system and dependency vulnerabilities still matter. Which addition addresses the new requirement, and how should findings be handled before the team concludes that the application has been remediated?

A. Use Web Security Scanner where supported, investigate relevant findings, fix the application, and verify the fixes while retaining image scanning.

B. Rename the deployed image tag and rerun Artifact Analysis, treating package metadata as a complete test of running HTTP behavior.

C. Replace all scanning with Cloud Trace, treating the absence of slow spans as proof that web vulnerabilities are absent.

D. Keep only the package scan and close every runtime finding because the image previously passed the release policy.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 46

**Select ONE.**

Several Cloud Build runs execute integration tests at the same time against a shared test database service. Each run creates records with identical names and deletes them during cleanup. Tests pass when run alone but fail intermittently when builds overlap. The database service itself is healthy, and production data must never be touched. The team can give each build an isolated test namespace or database and can remove that environment after the test. It also needs a failed test to block release even if cleanup succeeds. Which pipeline design addresses both interference between builds and the risk of cleanup hiding the original test result?

A. Run cleanup as the last successful command and report its exit code even when the integration tests failed.

B. Run tests against production so each build has more realistic data and skip cleanup to avoid deleting records.

C. Keep shared record names and increase retries so that one build eventually finishes before another deletes its data.

D. Use build-specific isolated test resources, clean them up reliably, and preserve the test failure as the build’s failure outcome.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 47

**Select ONE.**

A company requires production containers to pass its test and security checks. The checks run in a trusted pipeline, but a person with deployment access can currently bypass the pipeline and deploy an unapproved image directly to GKE. The team needs the production environment to enforce the release decision rather than rely only on a written procedure or a tag name. The trusted approval process can record approval for a specific immutable image digest, and access to that approval authority is controlled. Which design closes the bypass while allowing deployments of the exact image that passed the required checks?

A. Create a digest-bound attestation after approval and enforce the required attestation with Binary Authorization.

B. Enable package scanning and assume a scan also proves that every required business integration test passed.

C. Keep test results only in build logs and assume the cluster automatically reads those logs before admitting an image.

D. Require deployers to type an approved-looking image tag but allow them to move that tag to any digest.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 48

**Select ONE.**

An application calls a generative AI API to suggest a category and a priority for incoming support tickets. The response is consumed by application code, not displayed directly as free-form text. The selected API and model support structured output with a response schema. A syntactically valid response can still select a category that the current customer is not allowed to use or propose a priority inconsistent with business rules. The team wants reliable parsing and a controlled integration before saving a recommendation. Which approach best combines the API’s formatting capability with the application’s responsibility to validate meaning and handle unsuccessful or unusable responses?

A. Request JSON only in natural-language instructions and execute any returned action because an authenticated API response guarantees business correctness.

B. Accept only responses with confident wording and use that wording as proof that all categories are authorized for the current customer.

C. Request an appropriate supported response schema, handle API failures and unusable outputs, and validate business rules and authorization before saving the recommendation.

D. Use a response schema and remove application validation because syntactically valid output cannot violate customer-specific rules.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 49

**Select ONE.**

A business receives daily data files in Cloud Storage and wants analysts to run SQL aggregations over several years of history. The reports do not need individual records to appear within seconds of arrival; a scheduled daily load is acceptable. Original files must remain available for reprocessing, and the application does not need to turn this analytical dataset into a low-latency transactional database. The team prefers managed services and wants to avoid maintaining database servers for large historical scans. Which storage and ingestion design best separates retained source files from the query-optimized analytical dataset while matching the permitted batch freshness?

A. Choose continuous per-record streaming solely because all BigQuery data must arrive through a streaming API.

B. Keep the only copy of the historical dataset in Memorystore so that large scans execute entirely from a disposable cache.

C. Put every historical file into one Cloud SQL text column and make all analytical queries parse it on each request.

D. Keep source files in Cloud Storage and load compatible batches into appropriately partitioned BigQuery tables.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

### Question 50

**Select ONE.**

An organization exposes an API through Apigee. Existing mobile clients call version 1, and some clients cannot be upgraded immediately. A new backend introduces a breaking response change that should be available only to version 2 clients. Both versions require the same organizational authentication standard, and usage limits must continue to protect the backend. The team wants to publish the new contract without silently changing the response expected by version 1 consumers. It can maintain both contracts during a documented migration period. Which API management approach best supports this rollout while preserving access control and a clear migration path for existing consumers?

A. Expose separately versioned API contracts through appropriate proxy routing, preserve version 1 compatibility during migration, and enforce authentication and usage policies on both.

B. Disable authentication for version 2 during migration so consumers can upgrade without changing their application code.

C. Replace the version 1 response with the new contract and keep the old path because unchanged URLs guarantee client compatibility.

D. Use only a backend load balancer and assume it automatically translates every breaking response into the old API contract.

Cevabım: ___ · Güvenim (E/K/T): ___

Kararı belirleyen koşul / anlamadığım ifade (isteğe bağlı): ___

---

İlk cevaplarını kaydettikten sonra [Türkçe açıklamalı cevap anahtarını](../answers/scenarios/PCD-S08.md) açabilirsin.
