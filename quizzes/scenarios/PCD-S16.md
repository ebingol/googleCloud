# PCD-S16 Cumartesi karma deneme

50 soru · 120 dakika kişisel çalışma hedefi · 47 tek seçim + 3 çift seçim.

17 Ekim 2026 Cumartesi için hazırlandı. İngilizce senaryolar, karışık konu sırası ve ayrı Türkçe cevap anahtarı. 30 SkillCertPro kaynak uyarlaması + kaynakta sınırlı kalan konuları tamamlayan 20 resmî belge temelli soru. Önceki konuların bilinçli pekiştirmeleri bulunur; bu setin bütün kararlarının daha önce hiç görülmediği veya gerçek sınavla aynı zorlukta olduğu iddia edilmez.

GKE 20; CI/CD 8; veri 4; Workflows 4; Workstations 3; Buildpacks 3; Eventarc 3; Gemini 2; Identity Platform 1; Cloud Tasks 2. GKE sayımı GKE bağlamındaki geliştirici araçları ve gözlemlenebilirliği içerir. Bu özel çalışma dağılımı gerçek sınav ağırlığı tahmini değildir.

Çift seçim: Q07, Q28, Q43. Tam doğru küme 1 puan; kısmi puan yok. Diğer sorularda tek cevap seç.

Cumartesi ilk turda anahtarı açmadan çöz; cevapları bitirdikten sonra birlikte değerlendirelim. Mola veya yardım olursa kaydet. 120 dakika kişisel hedefi aşarsan o andaki cevapları koru, ek süreyi ayrıca yaz.

Başlangıç: ____ · Bitiş: ____ · Mola: ____ · Ek süre/yardım: ____

## Bölüm 1 Sorular 1 ile 10

### Question 01

A GKE service already writes application logs to standard output, and managed workload logging is enabled. Investigators can search the message text but cannot reliably filter by order ID or distinguish application severity. You want those values available as structured fields without operating an additional log collector. Which change best meets the requirement?

**Select ONE answer.**

**A.** Write one JSON log entry per line to stdout, including severity, message, and orderId fields.

**B.** Put the fields into the message string only and configure log retention to extract them.

**C.** Write JSON only to a private file in the container and rely on stdout collection to discover that file automatically.

**D.** Keep text logs and add severity as a Deployment annotation, expecting per-entry JSON fields.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 02

A Cloud Build execution is terminated after its configured 20-minute build timeout. The integration-test step needs 25 minutes, and all steps together normally finish within 35 minutes. The queue wait is short and no step-specific timeout is configured. You want tests to remain mandatory while allowing up to 40 minutes for the running build. What should you change?

**Select ONE answer.**

**A.** Increase queueTtl to 2400s and leave the running build timeout unchanged.

**B.** Set the top-level build timeout to 2400s and keep any step timeout within that build budget.

**C.** Set allowFailure on integration tests so the deployment proceeds when testing is interrupted.

**D.** Set only the test step timeout to 2400s while retaining the 20-minute build timeout.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 03

A Firestore backend transfers funds between two account documents. Before writing, it must verify the current source balance, and concurrent requests can modify either account. No external payment API is called during the database operation. You need both balances to remain consistent with the values used for the decision. Which implementation should you use?

**Select ONE answer.**

**A.** Read both accounts outside a transaction, then place the two updates in a WriteBatch.

**B.** Update the debit first and use a document trigger to credit the destination eventually.

**C.** Read and validate the balances, then update both documents inside a Firestore transaction that can retry on conflicts.

**D.** Read from a local cache and submit independent writes with Promise.all.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 04

A GKE application must connect to Cloud SQL using a private address. The private network route is already verified, and its workload identity has the required Cloud SQL permissions. The team requires proxy-managed connection authentication and encryption without managing database TLS certificates in application code. Which deployment arrangement best satisfies those requirements?

**Select ONE answer.**

**A.** Add a Cloud SQL Admin role to the node and remove connection authentication from the application.

**B.** Connect directly to the database private IP because network privacy alone satisfies the authentication and encryption requirements.

**C.** Run one proxy on a developer laptop and expose it to every production Pod.

**D.** Run the Cloud SQL Auth Proxy as a sidecar using private-IP connectivity and have the application connect through localhost.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 05

A workflow starts a supported Google Cloud API operation that returns a long-running operation. Later steps must execute only after that operation completes successfully. The associated Workflows connector supports waiting for this operation, and the workflow service account already has the necessary permissions. You want to minimize custom token handling and polling loops. What should you use?

**Select ONE answer.**

**A.** Start a continuously running VM whose only task is to poll the operation for the workflow.

**B.** Send an OIDC token to every Google API and assume it makes operations synchronous.

**C.** Use a raw HTTP request and proceed as soon as the operation name is returned.

**D.** Use the supported connector with its operation-waiting behavior and an appropriate connector timeout.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 06

A Java service is built with Google Cloud buildpacks and no Dockerfile. The repository compiles successfully with a supported JDK, but the team must consistently build with a different supported JDK major version. It wants to retain the managed buildpacks path rather than maintain a custom build image. Where should the runtime-version selection be supplied?

**Select ONE answer.**

**A.** Install the desired JDK in a pre-build shell session but let the buildpack select its runtime independently.

**B.** Change only the local developer JDK and assume remote source builds inherit it.

**C.** Supply GOOGLE_RUNTIME_VERSION to the buildpacks build environment with the supported JDK version constraint.

**D.** Set GOOGLE_RUNTIME_VERSION only on the deployed service after the build has completed.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 07

A Deployment references an immutable ConfigMap named payment-config-v1. A configuration change has been approved, and the old configuration must remain available for rollback. The team wants the new Pods to start with the revised values through its normal declarative release process. Which TWO actions should it take?

**Select TWO answers.**

**A.** Change the Deployment Pod template to reference the new ConfigMap and roll out that template.

**B.** Create a new immutable ConfigMap with a different name containing the approved values.

**C.** Patch the data of payment-config-v1 in place while leaving immutable set to true.

**D.** Delete all running Pods without changing their existing ConfigMap reference.

**E.** Set immutable to false on payment-config-v1 before editing its data.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 08

A container build compiles a Go service using a compiler toolchain and then deploys the resulting image to production. Security review finds compilers and source files in the runtime image, although the service only needs its compiled executable and a small set of runtime files. You want a smaller image without changing the application behavior. What should you do?

**Select ONE answer.**

**A.** Use a multi-stage Dockerfile and copy only the required executable and runtime files into the final stage.

**B.** Delete the compiler in a later layer of the same final image and assume earlier layers no longer contain it.

**C.** Increase Cloud Build machine memory so it automatically removes unused packages.

**D.** Push the builder stage to a private repository and deploy that image unchanged.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 09

A document service on Cloud Run should run when a new object is finalized in one specific Cloud Storage bucket. Objects in other buckets must not start the service. The destination service, source bucket, locations, and required identities are already valid. You want managed event routing rather than scheduled bucket scans. What should you configure?

**Select ONE answer.**

**A.** Configure a trigger for object-deleted events and infer new uploads from deletion absence.

**B.** Create only a topic named after the bucket, with no Storage event publishing or trigger configuration.

**C.** An Eventarc Standard trigger filtered by the object-finalized event type and the source bucket, targeting the Cloud Run service.

**D.** Configure only a destination runtime service account and assume source bucket events are routed automatically.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 10

A service team frequently updates a GKE Deployment from CI. During incidents, engineers struggle to determine which resource settings changed because some updates are made with interactive edits. The team wants reviewed, reproducible desired configuration with a history outside the cluster. It is not introducing a GitOps controller. Which approach should it adopt?

**Select ONE answer.**

**A.** Record only the image tag and leave resource and probe settings out of version control.

**B.** Keep Deployment manifests in version control, review changes, and create or update resources with kubectl apply.

**C.** Delete the Deployment before each release and recreate it from an imperative command.

**D.** Use kubectl edit for every change and rely on shell history as the release record.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 2 Sorular 11 ile 20

### Question 11

Cloud Workstations users sometimes leave their development environments running overnight. The platform team wants inactive workstations to stop after an idle interval but does not want an active debugging session stopped merely because a fixed total running duration has elapsed. Which configuration distinction matters for this requirement?

**Select ONE answer.**

**A.** Configure an idle timeout with the stop action and avoid imposing a conflicting running timeout.

**B.** Set an IDE debug-session timeout and assume it controls the workstation VM lifecycle.

**C.** Set a running timeout because it measures only inactivity rather than total running time.

**D.** Stop the workstation on a fixed daily schedule even when the developer is actively debugging.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 12

A Cloud Monitoring alerting policy for a production GKE service must notify an email group, an existing Slack integration, and a Pub/Sub topic used by an incident automation service. All three channel types are supported and configured. No custom payload transformation is required. You want the smallest amount of additional application infrastructure. What should you do?

**Select ONE answer.**

**A.** Attach the three notification channels to the alerting policy.

**B.** Replace all channels with a custom Cloud Run fan-out service that you operate.

**C.** Create a log sink to the Slack workspace and expect it to receive incident notifications.

**D.** Keep only email and build mail-forwarding code that publishes to Pub/Sub.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 13

An operations team monitors a GKE application using container CPU and memory metrics. It now needs supported metrics describing Kubernetes object state, including Pod phases and Deployment replica counts, in Cloud Monitoring. The cluster meets the collection prerequisites, and the team does not want to deploy its own kube-state-metrics exporter. Which managed collection capability should it enable?

**Select ONE answer.**

**A.** Keep only container CPU and memory collection enabled because resource usage metrics include every Kubernetes object state.

**B.** Enable the supported GKE kube state metrics collection packages for the required Kubernetes objects.

**C.** Create a counter of application ERROR logs and treat it as the current Deployment replica count.

**D.** Deploy a separate kube-state-metrics exporter and self-managed Prometheus server even though additional components are prohibited.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 14

A Cloud Build pipeline runs independent unit and integration tests against already available dependencies. Both test steps should begin immediately, but the packaging step must wait for both to finish successfully. Step IDs are unit and integration, and failures must stop release packaging. Which dependency configuration should you use?

**Select ONE answer.**

**A.** Omit waitFor everywhere because Cloud Build infers independence from step names.

**B.** Start packaging first and mark it allowFailure so it eventually observes completed tests.

**C.** Set waitFor: [] on every step and assume that means all steps run immediately.

**D.** Set waitFor: ["-"] on both tests and waitFor: ["unit", "integration"] on packaging.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 15

A GKE Standard cluster must keep using Kubernetes Secrets, but policy now requires an additional application-layer encryption boundary for Secret data stored in etcd using a customer-controlled Cloud KMS key. Authorized API readers are still expected to read values according to Kubernetes RBAC. Which change addresses this storage requirement?

**Select ONE answer.**

**A.** Grant KMS Decrypter to API readers but leave cluster application-layer encryption disabled.

**B.** Enable GKE application-layer secrets encryption with the Cloud KMS key and the required service-agent key access.

**C.** Use Base64 encoding and treat it as customer-controlled encryption at rest.

**D.** Restrict Secret reads with RBAC alone and treat access control as the requested additional storage encryption.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 16

A consumer web application already uses Identity Platform. The product team wants a passwordless flow where a user supplies an email address, receives a sign-in link, and completes authentication by opening that link. Users do not need a Google account, and the team wants a built-in provider flow rather than its own token service. What should it configure?

**Select ONE answer.**

**A.** Generate unsigned user IDs in email URLs and trust them when the link is opened.

**B.** Enable email-link sign-in in the email provider and implement the supported send-link and complete-sign-in client flow.

**C.** Use SMS authentication but send the SMS verification code in an email.

**D.** Enable only Google OAuth because every email address can authenticate as a Google account.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 17

A single workflow repeats the same address-normalization steps in several branches. The team wants one implementation within that workflow definition, with explicit inputs and a returned result. It does not need to share this logic across separately deployed workflows or expose it as a network service. Which mechanism should it use?

**Select ONE answer.**

**A.** Copy the normalization steps into every branch so variables are automatically shared.

**B.** Create a separate workflow execution for each expression evaluation and reconstruct all local state.

**C.** Define a parameterized subworkflow and call it from the branches.

**D.** Create a new Eventarc trigger for each repeated normalization step.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 18

A GKE container requests 512Mi of memory and has a 512Mi memory limit. Measurements show a legitimate, bounded startup requirement of 700Mi, followed by steady use below 400Mi. The container repeatedly terminates with OOMKilled, while node capacity is sufficient. The startup footprint cannot be reduced in this release. What should you change first?

**Select ONE answer.**

**A.** Raise the container memory limit to a validated value above the startup peak and review the request against scheduling policy.

**B.** Increase only the memory request above the unchanged 512Mi limit.

**C.** Add node capacity but leave the container at its measured-insufficient limit.

**D.** Increase HPA replicas without changing the per-container memory limit.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 19

A developer asks Gemini Code Assist to generate tests for a Python function selected in the editor. The proposed tests omit important behavior implemented by helper functions in another file. Those files and an approved test example are available locally. The developer wants to improve the next request without changing assistant products or making the code public. What should the developer do?

**Select ONE answer.**

**A.** Explicitly add the relevant implementation, helper, and example-test files as prompt context and request tests covering their interactions.

**B.** Accept tests that cover only the selected lines because generated tests cannot use additional file context.

**C.** Repeat the identical request with only the selected function because repeated generation guarantees discovery of every helper.

**D.** Enable private-repository customization solely to avoid attaching these already available local files.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 20

A Cloud Build trigger uses a dedicated build service account. Its build succeeds, but pushing the image to an existing Artifact Registry Docker repository is denied. The repository location and network path are correct. The account should push and read images but must not manage repository configuration. Which repository-level role should you grant?

**Select ONE answer.**

**A.** Grant Artifact Registry Writer to the application runtime account while leaving the build account unchanged.

**B.** Artifact Registry Writer to the build service account.

**C.** Grant repository Administrator to the build account because Writer cannot push new image tags.

**D.** Grant Artifact Registry Reader to the build account because it includes upload access.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 3 Sorular 21 ile 30

### Question 21

A GKE Autopilot Pod uses an explicitly assigned Kubernetes ServiceAccount and ADC. Workload Identity Federation is available, network access is working, and a Pub/Sub publish request reaches the API but is denied for missing permission. No IAM allow binding grants this workload access to the topic. What should you do?

**Select ONE answer.**

**A.** Grant the workload principal Pub/Sub Publisher on the intended topic using an IAM allow policy.

**B.** Create and mount a service-account JSON key because Autopilot cannot use federated workload identity.

**C.** Increase the node CPU limit so the metadata server can authorize Pub/Sub requests.

**D.** Grant the Kubernetes ServiceAccount the Workstations User role.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 22

A GKE worker Deployment consumes jobs from Pub/Sub only during short daily bursts. The team wants zero worker replicas when the subscription is idle and automatic activation when messages arrive. It currently uses only a conventional CPU-utilization HPA, which cannot observe CPU when no worker exists. Installing a supported event-driven autoscaler and granting it metric access are approved. What should it configure?

**Select ONE answer.**

**A.** Keep only the CPU-utilization HPA and lower its CPU target until it can observe metrics from zero Pods.

**B.** Set the worker Deployment replicas to zero permanently and expect Pub/Sub to create Kubernetes Pods without a scaler.

**C.** Use KEDA with an appropriate Pub/Sub event-source scaler to activate workers from zero and scale them with demand.

**D.** Convert the Deployment to a StatefulSet because that change alone gives CPU HPA event-based activation from zero.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 23

A supported Python service is built by Google Cloud buildpacks without a Dockerfile. The generated image starts the wrong application module because the project uses a non-default module name. The team knows the correct server command and wants to keep the managed buildpack. How should it configure the command used by the resulting image?

**Select ONE answer.**

**A.** Change only the build worker service account and rely on it to choose the application module.

**B.** Rename the source module after the build and leave the generated image unchanged.

**C.** Set GOOGLE_ENTRYPOINT to the desired command in the build environment and rebuild the image.

**D.** Set GOOGLE_ENTRYPOINT only in the running service environment without rebuilding or explicitly overriding its command.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 24

A GKE service already exports container metrics and structured application logs to Google Cloud. The on-call team wants one custom dashboard showing Pod memory usage beside relevant application log entries. It does not need a new metrics backend or cross-dataset analytics pipeline. What should it configure?

**Select ONE answer.**

**A.** Add complete log messages as metric labels and use only a metric chart for both data types.

**B.** Create a Logs Explorer query only and assume it also creates the requested metric widget.

**C.** Export every metric and log to BigQuery before building any dashboard because Monitoring cannot show logs.

**D.** A Cloud Monitoring custom dashboard with a container-memory chart and a logs panel filtered to the workload.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 25

A workstation administrator has created a Cloud Workstations environment for a new developer. The developer should connect to and use that workstation but must not change workstation configurations or administer other users. Existing network connectivity is valid, and the developer already has project-level Workstations Operation Viewer. Which IAM approach best matches the intended access?

**Select ONE answer.**

**A.** Grant Cloud Workstations Creator on the configuration instead of the role for using an existing workstation.

**B.** Grant only Workstations Operation Viewer and expect it to authorize workstation use.

**C.** Grant Workstations Admin on the project to every workstation user.

**D.** Grant the developer the Cloud Workstations User role at the appropriate workstation scope.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 26

An Artifact Registry Docker repository accumulates old build images. The team wants images older than 90 days deleted automatically, except images with tags beginning release-, which must be retained regardless of age. It wants to preview the affected artifacts before enabling deletion. Which configuration best satisfies the policy?

**Select ONE answer.**

**A.** Use versionPrefixes to match Docker release tags and skip a separate keep policy.

**B.** Enable immutable tags because immutability automatically deletes old untagged images.

**C.** Configure only an age-based delete policy because tagged artifacts are always excluded from cleanup.

**D.** Configure a conditional delete policy for age, a keep policy matching the release- tag prefix, and validate the result in dry-run mode.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 27

A developer has both a local minikube cluster and a production GKE context in kubeconfig. Cloud Code can build the application, but the next development run must deploy only to minikube. The local cluster is running and accessible. Which action controls where the Kubernetes resources are deployed?

**Select ONE answer.**

**A.** Select a local namespace name but leave the production Kubernetes context selected.

**B.** Start minikube but leave Cloud Code explicitly targeting the production context.

**C.** Select the minikube Kubernetes context in the Cloud Code run configuration before starting the development run.

**D.** Change the image repository region and assume it selects a local Kubernetes cluster.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 28

A Firestore mobile client uses offline persistence and an active snapshot listener. The UI must identify cached results and update its status when the snapshot becomes server-confirmed, even if document contents are unchanged. Which TWO parts of the listener implementation satisfy this requirement?

**Select TWO answers.**

**A.** Treat hasPendingWrites=false as proof that the snapshot is current server data.

**B.** Compare document timestamps to the device clock and ignore snapshot metadata.

**C.** Request metadata-change events so a metadata-only transition can update the UI.

**D.** Inspect the snapshot metadata fromCache value to label cache versus server results.

**E.** Assume any available network interface proves every snapshot was read from the server.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 29

A workflow service account has Cloud Run Invoker on a private Cloud Run service. A call still fails authentication because the OIDC token audience was configured for another service. Routing and permissions are verified. The request includes an application-specific URL path. Which change addresses the authentication issue?

**Select ONE answer.**

**A.** Give the destination runtime account Workflows Invoker on the source workflow.

**B.** Replace the bearer token with a caller-controlled email header.

**C.** Configure OIDC authentication with the expected audience of the destination Cloud Run service, rather than the unrelated service.

**D.** Grant the workflow service account Project Owner and keep the wrong audience.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 30

A GKE web container starts successfully but occasionally cannot serve requests while refreshing an internal cache. Restarting it during that short interval makes recovery slower. The application exposes a health endpoint that indicates whether it can currently accept requests. You want traffic withheld temporarily while the process remains running. Which probe should use that endpoint?

**Select ONE answer.**

**A.** A readiness probe that fails while the application cannot serve traffic.

**B.** Use a liveness probe to restart the container whenever the cache refresh temporarily blocks requests.

**C.** Increase initialDelaySeconds but leave no readiness check for later cache-refresh intervals.

**D.** Use only a startup probe and expect it to keep controlling traffic after initial startup succeeds.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 4 Sorular 31 ile 40

### Question 31

An order service publishes business events to a Pub/Sub topic. A billing worker must pull messages independently, while a separate Cloud Run audit service should be invoked through Eventarc when a message is published. Both consumers must receive the events rather than compete for one shared backlog. Which design is appropriate?

**Select ONE answer.**

**A.** Remove Pub/Sub because Eventarc cannot receive published-message events.

**B.** Run both consumers against the same pull subscription and assume each receives every message.

**C.** Keep a dedicated pull subscription for billing and configure a separate Eventarc Pub/Sub trigger for the audit service.

**D.** Configure only a Cloud Monitoring threshold on topic size and use it as a per-message trigger.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 32

A Cloud Deploy release is rolling out to a Cloud Run production target that already has a stable revision. Its configured canary stages are 10%, 50%, and stable. The rollout has completed the 10% stage successfully and is waiting for manual progression. You want this same rollout to enter its next canary phase. Which operation fits?

**Select ONE answer.**

**A.** Create a new release from another image because an existing rollout cannot progress.

**B.** Delete the stable revision so the new revision automatically receives exactly 50% of traffic.

**C.** Advance the rollout to its next phase after checking the current phase results.

**D.** Promote the release to a different target solely to move from 10% to 50% in this target.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 33

A one-time migration runs on GKE as a Kubernetes Job. The migration is safe to retry, but a persistent failure must not create replacement Pods indefinitely. The container uses restartPolicy: Never, and the team wants the Job controller to stop retrying after its configured retry budget is exhausted. Which Job setting controls that failure budget?

**Select ONE answer.**

**A.** Set only a readiness probe and assume it limits failed Job replacements.

**B.** Set activeDeadlineSeconds only and assume it counts failed attempts rather than elapsed time.

**C.** Set an appropriate backoffLimit on the Job.

**D.** Set restartPolicy: Never alone and assume the Job controller will never create a replacement Pod.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 34

A producer calls CreateTask for a monthly subscription renewal but loses the response because of a network interruption. It cannot tell whether creation succeeded and must retry without creating a second task for the same subscription and month. Different renewal months remain separate work items. Which task-naming strategy should it use?

**Select ONE answer.**

**A.** Use a deterministic task ID derived from subscription ID and renewal month, within the supported task-name deduplication window.

**B.** Use only the subscription ID forever so all future months are treated as the same renewal.

**C.** Allow a fresh random task ID on every retry and reduce dispatch concurrency to one.

**D.** Set maxAttempts to one and assume it deduplicates CreateTask requests.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 35

A web client relies on Firestore Security Rules and document queries. The team wants local automated integration tests that exercise allow and deny rules without touching a real project database. Unit mocks do not cover these checks. Which test environment should it use?

**Select ONE answer.**

**A.** Use the server Admin SDK against production and assume it enforces client Security Rules.

**B.** Replace every database call with a stub and consider the security rules tested.

**C.** Run the Firestore emulator, load the intended rules, and connect the client or rules-testing library to it with isolated test data.

**D.** Connect a Firestore client to the Bigtable emulator because both use document-like data.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 36

A GKE service has three healthy replicas. During planned node drains, the team wants voluntary evictions to preserve at least two available replicas. It understands that this policy does not prevent every outage or constrain the Deployment controller rolling update itself. Which Kubernetes resource expresses this requirement?

**Select ONE answer.**

**A.** A PodDisruptionBudget selecting the service Pods with minAvailable set to 2.

**B.** Set the Deployment replica count to two and assume that prevents all voluntary evictions.

**C.** Use a readiness probe alone and assume it rejects voluntary eviction requests.

**D.** Set rollingUpdate.maxUnavailable to one and treat it as the node-drain eviction policy.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 37

A developer uses Cloud Code in VS Code to debug a multi-container application on GKE. The relevant container languages and images support the documented Cloud Code debugging workflow, and cluster permissions are already configured. The developer wants to avoid manually preparing each debug connection. Which setup does Cloud Code manage as part of its supported Kubernetes debugging workflow?

**Select ONE answer.**

**A.** Expose every debug port through a public LoadBalancer Service because Cloud Code cannot forward local debugger connections.

**B.** Use Skaffold debugging support to prepare supported language debug settings and handle debug-port forwarding and debugger attachment.

**C.** Use application log streaming as a replacement for attaching a language debugger, without preparing debug settings.

**D.** Grant Project Owner to the container runtime identity so a normal run automatically becomes an IDE debugging session.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 38

A Cloud Build pipeline builds a container image and pushes it with an explicit docker push step. The team also requires Cloud Build-generated provenance for the image and a corresponding image entry in build results. The image is stored in Artifact Registry and the build is eligible for provenance. Which configuration should it use?

**Select ONE answer.**

**A.** Keep only docker push and assume every externally pushed artifact receives Cloud Build provenance.

**B.** Declare the built image under the top-level images field and request verified provenance using options.requestedVerifyOption: VERIFIED.

**C.** Enable Binary Authorization and assume it creates missing build provenance during admission.

**D.** Put the image name in an application log line and let Cloud Logging generate the provenance.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 39

A developer stores a project under the configured persistent /home directory of a Cloud Workstation. The workstation is stopped overnight and started again with the same configuration and persistent disk. The team wants the project to survive without rebuilding the container image. Which statement correctly explains the expected behavior?

**Select ONE answer.**

**A.** Every saved file automatically becomes a new layer in the shared workstation image.

**B.** The persistent home disk retains the project across stop/start; the development container image need not contain the changed project files.

**C.** Stopping the workstation necessarily deletes its persistent home disk and all user projects.

**D.** The project survives only if its contents are copied into the workstation machine-type setting.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 40

A GKE Service returns no backend responses after a label refactor. The application Pods are Running and Ready, and direct Pod-IP requests succeed. The Service selector still matches app=checkout, but the intended Pods now have app=checkout-api. No network policy blocks the traffic. What should you correct first?

**Select ONE answer.**

**A.** Switch to LoadBalancer and assume external exposure bypasses selector matching.

**B.** Align the Service selector with the intended Pod labels and verify that the corresponding endpoints appear.

**C.** Change the Service port while leaving the selector mismatched with every intended Pod.

**D.** Increase replica count without correcting the labels used by the selector.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 5 Sorular 41 ile 50

### Question 41

A workflow catches an exception from a required payment-confirmation call, writes a diagnostic log, and then returns status=completed. Operators see successful executions even though confirmation failed. Retrying the payment is outside this workflow and must be handled by a recovery process. How should the workflow preserve an accurate failure outcome?

**Select ONE answer.**

**A.** Grant the workflow account Logging Admin so ERROR log entries terminate executions.

**B.** Increase Eventarc delivery retention so a successfully started execution is marked failed automatically.

**C.** Return status=completed with HTTP 200 and rely on the log severity to change execution state.

**D.** Log the context and re-raise the caught error, or raise an explicit failure, rather than return a normal completion result.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 42

Several GKE workloads use distinct Kubernetes ServiceAccounts in the namespace reporting. They all need the same read permission on one Cloud Storage bucket. Security explicitly approves this access for all workloads in that namespace across clusters sharing the project workload identity pool. Workload Identity Federation is configured. How can the team express the grant with one IAM binding while preserving the distinct ServiceAccounts?

**Select ONE answer.**

**A.** Grant the bucket role to the node service account and assume namespaces limit which Pods inherit that node identity.

**B.** Replace all ServiceAccounts with one shared Kubernetes ServiceAccount, despite the requirement to preserve separate identities.

**C.** Create a Kubernetes RoleBinding in reporting and expect Kubernetes RBAC alone to grant Cloud Storage bucket IAM permissions.

**D.** Grant the bucket read role to the Workload Identity Federation namespace principalSet for reporting in the project workload identity pool.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 43

A supported Python application is built with Google Cloud buildpacks. Developers report dependency drift because requirements use broad ranges and each build can resolve different versions. The runtime family is already approved, and the team wants dependency changes reviewed with source changes. Which TWO practices directly address this reproducibility requirement?

**Select TWO answers.**

**A.** Install dependency updates only inside running containers without recording or rebuilding the source inputs.

**B.** Reuse a mutable latest image tag as the only record of resolved dependency versions.

**C.** Commit an appropriately pinned dependency manifest or supported lockfile used by the selected package manager.

**D.** Select the same runtime family but leave dependency version ranges broad and assume runtime selection pins packages.

**E.** Review dependency updates in version control and rebuild the image through the normal pipeline.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 44

A Deployment has four replicas. During an application rolling update, at least four ready replicas must remain available, and the cluster can temporarily host one additional Pod. Readiness probes accurately report readiness, and no other disruption is occurring. Which rollingUpdate settings match the requirement?

**Select ONE answer.**

**A.** Set maxUnavailable to one and maxSurge to zero.

**B.** Set maxUnavailable to 0 and maxSurge to 1.

**C.** Use a PodDisruptionBudget alone and leave the Deployment rollingUpdate settings at values that permit fewer than four available replicas.

**D.** Set maxSurge to zero and maxUnavailable to four.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 45

A Gemini Cloud Assist investigation has completed and presented observations about an application latency increase. The on-call engineer wants to ask follow-up questions about those findings in the Google Cloud console before deciding on remediation. The feature and permissions are already available. Which action best fits this interactive investigation workflow?

**Select ONE answer.**

**A.** Use Gemini Cloud Assist chat to ask contextual follow-up questions about the findings and verify the proposed explanation against the evidence.

**B.** Restart the investigation after each question instead of using the conversational interface.

**C.** Apply every proposed change automatically because ranked hypotheses are confirmed root causes.

**D.** Export all telemetry to a new warehouse solely to ask a natural-language follow-up question.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 46

A team uses one Cloud Build configuration for development and staging. The steps are identical, but the Artifact Registry repository name differs by environment. The repository value is nonsecret and must be visible in the trigger configuration. Which approach avoids duplicating the whole build file?

**Select ONE answer.**

**A.** Use a user-defined substitution such as _REPOSITORY in the build configuration and set its value per trigger.

**B.** Put the repository name in Secret Manager and have every step discover it independently.

**C.** Use the runtime Cloud Run service account email as an automatic repository-routing rule.

**D.** Create a separate hand-edited build file for every repository and compare them manually.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 47

A Cloud Storage bucket is regional in europe-west1. A team is creating an Eventarc Standard trigger for direct object-finalized events from that bucket to a supported destination. It plans to place the trigger in us-central1 because that is its usual CLI default region. The source project and permissions are otherwise correct. What should it change?

**Select ONE answer.**

**A.** Grant Project Owner to the destination runtime account to remove source-location restrictions.

**B.** Rename the bucket so its name ends in us-central1 without moving its data.

**C.** Keep the trigger in us-central1 and change only the Pub/Sub acknowledgment deadline.

**D.** Create the trigger in the location matching the regional source bucket, europe-west1.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 48

A regional GKE cluster has suitable worker capacity in three zones. An application has three replicas, but the team wants scheduling to distribute them across zones rather than place all replicas in one zone. It wants to express placement intent in the Pod specification, with suitable labels already present on the nodes. What should it configure?

**Select ONE answer.**

**A.** Increase the Deployment replica count without expressing any zone placement policy.

**B.** Use a regional cluster alone and omit any workload placement constraints.

**C.** Set required node affinity to a single zone and assume replicas spread across all zones.

**D.** Pod topology spread constraints using topology.kubernetes.io/zone and an appropriate skew and scheduling policy.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 49

A Cloud Tasks HTTP handler has durably completed its intended operation. It wants to acknowledge the task so it is removed from the queue. A developer proposes returning 429 because the service is busy after completing this request. Which response handling correctly distinguishes success from overload?

**Select ONE answer.**

**A.** Return 404 for completed tasks because all 4xx responses delete the task.

**B.** Return 429 for every completed task because Cloud Tasks treats it as successful backpressure.

**C.** Leave the connection open after completion because timeouts count as success.

**D.** Return a 2xx response for the completed task; use an appropriate non-2xx response such as 429 when the task has not been successfully completed and should be retried.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 50

A Bigtable application shows uneven latency during peak writes. The team suspects that particular row-key ranges receive most traffic and wants a visual history of access patterns across the key space before changing its schema. It does not need to export every row to an analytics system. Which diagnostic tool should it use?

**Select ONE answer.**

**A.** Add column families without examining traffic because each family automatically gets a separate compute cluster.

**B.** Key Visualizer to inspect heatmaps for hot row-key ranges over time.

**C.** Use only a table-wide average latency chart and assume it identifies individual row-key ranges.

**D.** Run a full-table export and infer hot key ranges from the number of bytes stored alone.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---
