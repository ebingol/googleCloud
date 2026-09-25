# PCD-S05 — Uzun senaryolarla karma 20 soru

25 Eylül 2026 · 20 özgün İngilizce soru · **Süre hedefi: 50 dakika.** Bu kişisel çalışma hedefidir; resmî sınav süresi değildir.

S04 değiştirilmedi. Bu set güncel rehberin dört ana alanını örnekler; bütün alt konuları kapsama veya gerçek sınavla aynı zorlukta olma iddiası taşımaz. Bazı teknik kararlar yeni olabilir. Uzun paragraflarda hedefi, zorunlu kısıtları ve zaten sağlanan koşulları ayrı düşün.

**18 Select one, 2 Select two (Q16/Q18).** Her soru 1 puan; çift seçimde tam doğru küme gerekir. İlk turda anahtarı açma. Güven: **E** emin, **K** kararsız, **T** tahmin. Bilmediğin kavramı ayrı alana **B: …** diye yaz; bu not, B şıkkını seçmek anlamına gelmez. Teknik önbilgi eksikliği ile İngilizce okuma güçlüğünü ayrı değerlendireceğiz.

## 1

A subscription platform runs a stateless account-summary API on Cloud Run. During the morning traffic peak, many instances repeatedly read the same customer preferences from Cloud SQL, although those preferences change infrequently. The database must remain authoritative, and the summary page can tolerate temporarily stale preferences; billing decisions always use a separate database path. Two tenants can have the same local customer identifier. The team wants a cache shared across instances, with bounded entry lifetimes, and must continue serving requests at a reduced rate if the cache is unavailable. Network connectivity to Memorystore already works. Which design best satisfies these requirements without making cache availability a prerequisite for correctness?

**Select one.**

- A. Use an in-process cache in each instance, key entries by customer identifier, and increase minimum instances to retain a shared cache during scaling.
- B. Write preference changes only to Memorystore, acknowledge them immediately, and periodically flush entries to Cloud SQL before their expiration time.
- C. Use cache-aside with tenant-aware keys and TTLs; fetch misses from Cloud SQL, and use bounded database fallback with load protection during cache failures.
- D. Use Memorystore with tenant-aware keys and TTLs, but return a service error on every cache miss so that database demand stays independent of cache state.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 2

A financial software team is onboarding forty developers who currently maintain different local SDK versions. They need browser-accessible development environments connected to an approved VPC, where internal package repositories and test services are reachable. Each developer must have an isolated workspace, while the platform team controls the approved operating environment and toolchain through a centrally maintained container image. Developers should be able to stop their environments outside working hours and resume work later. The team does not want to build its own fleet-management portal or maintain individual VM bootstrap scripts. Existing network and identity policies can be configured by administrators. Which approach most directly matches the development environment requirements?

**Select one.**

- A. Create a Cloud Workstations configuration using the approved image and network settings, then provision a separate workstation for each developer.
- B. Give every developer a Compute Engine VM and permission to install SDKs manually; maintain the approved versions in a shared setup document.
- C. Use one shared Cloud Shell session through a team account, with per-developer folders and a startup script that downloads the toolchain.
- D. Run the development tools as one Cloud Run service with a writable container filesystem, and use session affinity to retain each developer’s workspace.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 3

A Cloud Run service stores customer records in a shared relational database. The team wants to canary a new revision for several hours while the previous revision continues handling most requests. The new code was originally written to use a renamed database column, whereas the old code still reads and writes the original column. Product owners require a quick traffic rollback without restoring a database backup, and writes must remain enabled throughout the rollout. Both revisions will use the same database, and no automatic compatibility layer exists. The team can modify the application and sequence schema changes before deployment. Which release plan best preserves compatibility during both the canary and the rollback window?

**Select one.**

- A. Rename the column immediately before deploying the canary, then send the majority of traffic to the old revision until monitoring confirms success.
- B. Create a database copy for the canary, allow both databases to accept writes independently, and switch traffic back without reconciling their records.
- C. Keep the original code unchanged, configure session affinity, and rename the shared column once the canary receives its first requests.
- D. Use additive schema changes and a tested compatibility phase that keeps old and new representations consistent; retire the old column only after old revisions and the rollback window are gone.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 4

A media archive receives fifty thousand image objects in Cloud Storage each night. A processing service must request label detection for every image and make the results available to a downstream indexing job before the next business day. No user is waiting for an individual annotation response, and the indexing job already consumes JSON files from Cloud Storage. The current implementation opens a client for each image and waits for each synchronous request before submitting the next one. Service permissions, supported image formats, and project quotas have been checked. The team wants fewer request round trips and a recoverable bulk-processing workflow, without paying to reprocess successful images after a partial failure. Which implementation is the best fit?

**Select one.**

- A. Keep synchronous single-image calls, increase each request timeout, and repeat the complete nightly input whenever any annotation fails.
- B. Reuse a client, submit asynchronous image batches within API limits, track their long-running operations, and inspect output to resubmit only failed images.
- C. Use synchronous batches of all fifty thousand images, store the inline results in Cloud Storage, and retry the complete request if it times out.
- D. Submit asynchronous batches within API limits and mark each batch complete when its operation name is returned, without waiting for output or checking image-level errors.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 5

An order-status service uses Memorystore for Redis Standard Tier to accelerate reads of data held in a durable transactional database. During a failover test, clients briefly lose connections and some recently cached status values are absent afterward. A developer proposes treating successful Redis writes as the durable acceptance record for new orders because Standard Tier includes a replica and automatic failover. The business requires that an acknowledged order remain recoverable even if the cache primary fails immediately afterward. The service can reconstruct status entries from the database, and a short period of slower reads is acceptable. Which response best addresses both the observed failover behavior and the proposed change to order acceptance?

**Select one.**

- A. Accept orders after Redis acknowledges them, because automatic failover ensures that every acknowledged write is synchronously stored on the replica.
- B. Move order acceptance to Redis Basic Tier to avoid replica lag, and rebuild the instance from the application’s local cache after a failure.
- C. Keep order acceptance in the durable database, reconnect cache clients with bounded retries, and tolerate or rebuild missing cache entries after failover.
- D. Keep order acceptance in Redis Standard Tier, but increase cache TTLs so that acknowledged writes cannot be lost during replica promotion.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 6

A developer uses Cloud Workstations with a persistent home directory configured by the platform team. To speed up a proof of concept, the developer cloned an uncommitted project into a directory under /opt and manually installed an additional compiler into the running container. After stopping and restarting the workstation, the developer finds that these changes are gone, while files previously stored under /home are still present. The organization wants to keep the normal stop-and-start policy to control cost. The compiler must also become available consistently to newly created workstations used by other developers. Which change addresses both persistence and reproducibility without depending on an individual workstation remaining continuously active?

**Select one.**

- A. Keep both changes in the running container and extend the idle timeout, using the same manual installation instructions for each new workstation.
- B. Move the project under /home, but install the compiler manually into each running container rather than updating the centrally managed image.
- C. Build the compiler into the approved custom image, but leave uncommitted project files under /opt because the image now defines the environment.
- D. Store working files under the configured persistent home directory and include the compiler in a versioned custom image used by the workstation configuration.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 7

A GKE Deployment runs workers that consume independent tasks from a queue. Each task spends most of its time waiting for a remote service, and load tests confirm that adding workers increases throughput without exceeding that service’s limits. During production bursts, the queue grows for twenty minutes while average Pod CPU usage remains below the current HPA target. Nodes have enough spare capacity for additional Pods, and the application does not need more memory per worker. The team has already exposed a reliable queue-backlog metric through the supported external metrics integration. It wants the worker replica count to respond automatically to queued demand. Which configuration change most directly addresses the scaling problem?

**Select one.**

- A. Configure the HPA to scale the Deployment using the external queue-backlog metric with a suitable per-replica target and replica bounds.
- B. Increase the cluster autoscaler’s maximum node count while keeping the current CPU-based HPA target and Deployment replica limits unchanged.
- C. Use vertical Pod autoscaling to increase CPU requests for each worker while keeping the number of replicas fixed during queue growth.
- D. Raise the CPU utilization target for the current HPA so that it tolerates more waiting tasks before requesting additional worker replicas.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 8

A reporting service retrieves rows from a BigQuery query job that has already completed successfully. The result is much larger than the service’s available memory, but each page can be transformed and written to a downstream stream before the next page is fetched. A developer requests a fixed maximum number of rows per page and stops whenever fewer rows than that maximum are returned. Tests show that one response contains fewer rows than requested but still includes a continuation token, causing the exported report to omit records. The underlying query must not be rerun between pages, because source data is changing. Which retrieval strategy preserves the complete result while keeping memory use bounded?

**Select one.**

- A. Rerun the SQL for every page with increasing OFFSET values, and stop when a query returns fewer rows than the requested page size.
- B. Set the requested page size equal to the estimated total row count and accumulate all responses before starting downstream processing.
- C. Continue reading the same completed job’s results using returned page tokens, processing each page incrementally until no continuation token remains.
- D. Keep using the completed job, but treat a short page as the end of the result and ignore any token to avoid exporting duplicate rows.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 9

A reconciliation application reads account balances from Spanner in several separate requests while new transactions continue to update those accounts. The application has already selected a committed read timestamp T for a report, and T will remain inside the database’s version-retention period for the duration of the export. Every section of the report must describe the database at exactly T, even if later sections are fetched several minutes after earlier ones. The application does not require the latest values, and it does not need to write during the export. A developer suggests using the same relative staleness duration on every request. Which read configuration actually preserves the required common snapshot across the independent requests?

**Select one.**

- A. Use a fresh strong read for each request, because strong consistency ensures that separate requests always observe the same database version.
- B. Use the same exact read timestamp T for every request and finish all reads before that version is outside the retention window.
- C. Use an exact staleness of thirty seconds for every request, because the same staleness duration fixes a shared timestamp for the entire export.
- D. Use a maximum staleness of thirty seconds for every request, allowing Spanner to choose an independently suitable timestamp for each section.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 10

A developer asks Gemini Code Assist to implement an adapter for an internal Java library. The generated code looks plausible but calls methods that do not exist in the repository’s pinned library version. The developer’s prompt only described the desired business behavior; the relevant interfaces, dependency manifest, and a working adapter were not included in the selected context. Those files contain no prohibited data and can be used with the organization’s approved assistant configuration. The public API of the application must remain unchanged, and replacing the library would require a separate review. Which next step is most likely to produce a useful implementation while preserving the project’s existing contract?

**Select one.**

- A. Add the relevant interfaces, pinned dependency information, and a working example to context; state the compatibility constraint, then compile and review the generated change.
- B. Ask for a longer explanation of the same generated code without adding repository context, then accept it if the explanation is internally consistent.
- C. Upgrade the library to the newest version suggested by the assistant and adjust public method signatures before running the existing compatibility checks.
- D. Remove the calls that fail compilation and replace their results with defaults so that the build passes without changing the assistant’s original design.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 11

A Cloud Run service calls a partner API using a credential stored in Secret Manager. The service currently exposes the secret as an environment variable that references latest. After rotation, newly started instances use the new credential, but long-running instances continue using the previous value. The partner permits an overlap period during rotation, and the application can be modified to reread a credential file before making outbound calls and handle read failures. The team wants later rotations to take effect in already running instances without deploying a new revision solely for each new secret value. IAM access is already correct. Which configuration and application change best meets this requirement?

**Select one.**

- A. Keep the environment variable mapped to latest and increase minimum instances so that the same processes remain available through every rotation.
- B. Pin the environment variable to a numeric secret version and increase request concurrency so that fewer instances need to retrieve the value.
- C. Mount the secret using a fixed numeric version and have the application read that file once during startup into a process-wide variable.
- D. Mount the secret with latest and have the application read the mounted file when it needs the credential, with handling for access failures and the rotation overlap.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 12

A customer-facing API has become slower after a release, and distributed tracing shows that most additional latency is inside calls to Spanner. Trace propagation across all application services is already working, so the team can identify the slow database spans and the affected endpoint. However, those spans do not explain which SQL patterns are consuming the most database CPU or why a particular query is scanning far more rows than before. Several endpoints issue related queries, and the team needs to compare aggregated query behavior over the incident interval before deciding whether to change SQL or an index. Which investigation provides the most relevant additional evidence for that decision?

**Select one.**

- A. Increase application trace sampling and infer the required index only from the duration of the longest database span.
- B. Inspect Spanner query statistics for the relevant interval, identify expensive query patterns, and examine their execution plans alongside the application traces.
- C. Increase the Cloud Run maximum instance count and compare endpoint latency before inspecting any database-specific metrics or query behavior.
- D. Group application access logs by HTTP status code and select an index based on the endpoint with the highest number of successful responses.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 13

A data engineering team runs several hundred Apache Airflow DAGs on self-managed virtual machines. The DAGs use Python operators, task dependencies, scheduled runs, and operational procedures for rerunning historical intervals after source corrections. The team wants Google Cloud to manage the orchestration environment while preserving its existing DAG code and operator ecosystem as much as possible. It has a small operations team and cannot fund a rewrite of every workflow into a different definition language during this migration. Data processing will continue in external services called by the tasks; moving all computation into the orchestrator is not a goal. Which service is the closest fit for this migration?

**Select one.**

- A. Use Cloud Workflows and rewrite each Python DAG into workflow definitions, replacing existing Airflow operators and historical-run procedures.
- B. Use Cloud Scheduler with one HTTP target per existing task, rebuilding task dependencies and historical-run tracking in a custom database.
- C. Use Cloud Composer / Managed Airflow, validate DAG and dependency compatibility with the chosen environment, and migrate the orchestration workload.
- D. Use Cloud Run jobs for all tasks and develop a new coordinating service to replace Airflow scheduling, dependency handling, and run history.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 14

An engineering manager wants to introduce two distinct AI-assisted workflows without building a new customer-facing AI feature. In the first workflow, developers need help understanding repository code and proposing implementation changes from within their supported IDE. In the second, a cloud operations team needs assistance investigating resource configuration and operational issues in its Google Cloud environment. The organization will keep human review and existing permission boundaries for any proposed changes. A proposal currently treats every Gemini-branded capability as interchangeable and recommends using the same product name for both activities. Which pairing most accurately assigns the primary intended role of each assistant for these requirements?

**Select one.**

- A. Use Gemini Code Assist for repository-oriented IDE assistance and Gemini Cloud Assist for Google Cloud resource and operational assistance.
- B. Use Gemini Cloud Assist for repository-oriented code completion and Gemini Code Assist as the primary assistant for cloud resource operations.
- C. Use Gemini Code Assist for repository assistance and build a custom Vertex AI application for operations, replacing the available resource-oriented assistant.
- D. Use Gemini Cloud Assist for resource operations and build a custom Vertex AI code-generation service instead of using the available IDE-oriented assistant.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 15

A GKE service loses some in-flight requests during rolling updates even though replacement Pods become ready before old Pods are removed. Investigation shows that each terminating Pod runs a preStop hook for twenty seconds and then the application receives SIGTERM. The application already stops accepting new work and can finish its remaining requests within twenty-five additional seconds, but the Pod’s terminationGracePeriodSeconds is thirty. The team can reserve a modest amount of extra rollout time and wants normal graceful termination to complete before forced termination. Node capacity and readiness configuration are already sufficient, and the issue also occurs during a direct Pod deletion. Which change most directly fixes the measured timing mismatch?

**Select one.**

- A. Increase the readiness probe’s failure threshold while keeping the termination grace period at thirty seconds and the existing hook unchanged.
- B. Add a PodDisruptionBudget and rely on it to postpone forced termination until the application has finished every request.
- C. Increase the Deployment’s maxSurge while keeping the old Pod’s thirty-second termination budget and current shutdown sequence unchanged.
- D. Increase the termination grace period to cover both the preStop hook and application draining, with margin, while retaining the working SIGTERM handler.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 16

A service performs idempotent Cloud Storage object reads as part of a user request with a forty-five-second overall deadline. During a transient incident, many reads receive HTTP 429 or 503. The Storage client already retries, but an application wrapper also retries every failed client operation several times using fixed one-second delays. Monitoring shows synchronized retry spikes and substantially more attempts than the team expected. The same wrapper retries permission errors without any credential or policy change. The team wants transient failures to recover when possible while protecting the dependency and respecting the caller’s total deadline. Which TWO changes best address the observed behavior without treating every error as transient?

**Select two.**

- A. Retry all 4xx responses until the deadline because object reads are idempotent and therefore permission failures are automatically recoverable.
- B. Use exponential backoff with jitter for eligible transient failures, with bounded attempts and a total timeout that fits the caller’s remaining deadline.
- C. Increase the wrapper retry count and preserve client-library retries so that each layer independently maximizes its chance of completing a read.
- D. Replace jitter with a fixed common delay so all instances return to the dependency together after each failed request.
- E. Coordinate retry ownership across the wrapper and client to avoid multiplying attempts, and stop retrying unchanged permanent authorization failures.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 17

A document service stores a large collection of objects in Cloud Storage. Some documents receive heavy access immediately after upload and then remain untouched, while others unexpectedly become popular years later. The product team cannot predict which objects will be accessed again, and all documents must remain available for interactive reads without a separate restore operation. A fixed lifecycle rule based only on object age has moved frequently revisited older documents into an unsuitable cost pattern. The team wants Google Cloud to adjust storage classes according to access behavior while reducing the effort of maintaining custom classification jobs. It will compare the feature’s management costs with the expected savings before enabling it. Which approach best matches that goal?

**Select one.**

- A. Use Autoclass on an eligible bucket so access behavior drives class transitions, and evaluate the associated pricing against this workload.
- B. Apply the same age-based transition rule more frequently so recently accessed old objects are automatically recognized by their creation dates.
- C. Move every object to the coldest storage class immediately after upload because all classes having online access makes their access costs equivalent.
- D. Keep the age-based rules and add a longer retention policy because a retention period automatically promotes frequently read objects to Standard storage.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 18

A Cloud Build pipeline creates a Docker image for a Node.js application. Most commits change only application source files, while the package manifest and lockfile change infrequently. The Dockerfile currently copies the entire repository before running npm ci, so ordinary source edits invalidate the dependency-install layer. Each build uses a fresh worker, and the pipeline does not fetch any previous image before invoking docker build. The team wants to reuse valid dependency layers across builds without skipping tests, changing the locked dependencies, or reusing an obsolete final application image. A compatible previous image is available in Artifact Registry. Which TWO changes together address the two independent reasons the dependency cache is not being reused?

**Select two.**

- A. Replace npm ci with an unlocked dependency update so each build can select whichever package versions already exist in a cache.
- B. Skip docker build on source-only commits and redeploy the previous complete image to preserve its installed dependency layers.
- C. Copy the dependency manifest and lockfile first, run npm ci, and copy frequently changing application source afterward.
- D. Fetch the previous compatible image and configure docker build to use it as a cache source, handling a missing first-build cache gracefully.
- E. Keep the Dockerfile unchanged and add --no-cache to ensure the dependency layer remains consistent across fresh workers.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 19

An API Gateway deployment validates external client JWTs before forwarding requests to a private Cloud Run service. Client token validation succeeds, and the gateway’s backend authentication is configured to use a dedicated service account. The backend URL and ID-token audience are correct, the gateway can reach the service, and logs show that Cloud Run rejects invocation because the gateway service account lacks permission. The Cloud Run runtime service account already has all permissions needed to access its own database. Security policy requires the backend to remain authenticated and limits invocation access to the intended gateway identity. Which change resolves this failure at the correct authorization boundary with the smallest relevant grant?

**Select one.**

- A. Grant Cloud Run Invoker on the backend service to the Cloud Run runtime service account, because that identity executes the request handler.
- B. Grant Cloud Run Invoker on the backend service to the gateway’s configured backend-authentication service account.
- C. Grant every external JWT subject a project-wide Editor role so that successful frontend authentication also authorizes backend invocation.
- D. Allow unauthenticated invocation on the backend service and rely exclusively on the gateway’s frontend JWT validation to restrict access.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 20

A batch application uses a dedicated service account to read objects from two Cloud Storage buckets. An audit finds that the account can also read objects from every other bucket in the project because it has Storage Object Viewer at project level. Uniform bucket-level access is enabled, and the audit confirms that no group membership, other allow binding, or alternate identity grants the application additional access. The security team wants to keep the existing service account but restrict it to the two required buckets, using allow-policy changes only. Other principals’ access must remain unchanged. Which policy update actually removes the excessive inherited access while preserving the application’s legitimate reads?

**Select one.**

- A. Add Storage Object Viewer for the service account on the two required buckets and leave its project-level grant in place.
- B. Remove bucket-level grants for the service account from all other buckets but retain the inherited project-level Storage Object Viewer grant.
- C. Remove that service account’s project-level Storage Object Viewer membership and grant the role only on the two required buckets, preserving other members.
- D. Add empty bucket allow policies on the other buckets so those policies override the project-level grant for this service account.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## İlk deneme kaydı

Başlangıç / bitiş / toplam süre:

Ara veya yardım alındıysa hangi sorularda:

İlk turda atladığım sorular:

İlk seçimlerimi değiştirdiysem önceki seçim ve nedeni:

Cevapları kaydettikten sonra [ayrı Türkçe anahtarı](../answers/scenarios/PCD-S05.md) açabilirsin. Açıklama sonrası değişen cevaplar ilk deneme puanının üzerine yazılmaz.
