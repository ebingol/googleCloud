# PCD-S06 — Exam guide öncelikli, uzun ve çok koşullu senaryolar

25 Eylül 2026 · **20 özgün İngilizce soru: 18 tek seçim, 2 çift seçim (Q6/Q18).**

Öncelik güncel resmî exam guide. Dört ana alan 6/5/5/4 örnekleniyor; önceki sınav deneyimi aktarımları konu ağırlığı belirlemiyor. Bu set bütün alt konuları ölçmez ve gerçek sınav zorluğuyla kalibre edilmiş değildir.

Bu tur süreyi kaydet; **50 dakikayı zorunlu bitirme sınırı olarak kullanma.** S05’te 70–80 dakika bildirmiştin; bu sette metin ve seçenek yükü daha yüksek. Süre, doğruluk ve bilinmeyen kavramlar ayrı değerlendirilecek.

Her soruda seçimini, E/K/T (emin/kararsız/tahmin) düzeyini ve belirleyici koşulu yaz. Bilmediğin kavramı **B: …** diye ayrı alana not et; bu B şıkkını seçmek değildir. Çoklu seçimde tam doğru küme 1 puan, toplam 20 puan. İlk turda anahtarı açma.

## 1

A billing platform accepts requests that require a later call to one partner endpoint. Each request includes an earliest execution time within the next day, and clients must receive an acceptance response without waiting for the partner. Jobs are independent; their execution order does not matter. The partner allows a limited dispatch rate and no more than five requests in flight at once, including retries. The application already assigns a durable operation identifier and handles repeated delivery safely. Handlers finish partner calls before acknowledging and within their dispatch deadlines. Traffic arrives in bursts, but adding more application instances must not multiply the partner's allowed rate. The team wants managed scheduling, retry behavior, and queue-wide dispatch controls, with minimal custom coordination. It does not need to broadcast each job to multiple independent consumers. Which design best satisfies the combination of timing and delivery requirements?

**Select one.**

- A. Publish immediately to Pub/Sub and give each subscriber a local five-request semaphore; store the execution time in message attributes and sleep in the handler until it arrives.
- B. Enqueue HTTP tasks with per-task schedule times in Cloud Tasks; configure queue dispatch-rate and concurrent-dispatch limits, and use the existing operation identifier in the handler.
- C. Create a Workflows execution per request with a sleep step and retries; give each execution its own five-request concurrency allowance before calling the partner endpoint.
- D. Create a Cloud Scheduler job that periodically publishes all pending work to Pub/Sub; limit the worker service to five instances and let each instance dispatch requests independently.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 2

A developer is testing a Python service locally with a Google Cloud client library that uses Application Default Credentials. The developer has run both gcloud auth login and gcloud auth application-default login using an approved user account, and command-line reads of the test bucket succeed. The application still receives a permission error, and the corresponding audit entry identifies an old service account from an earlier experiment. The IDE launches the process with GOOGLE_APPLICATION_CREDENTIALS pointing to that account's existing JSON key file. The approved user already has the necessary bucket permissions, and the team does not want to grant the old account access or create another key. The code must keep using the normal ADC mechanism so the same code can run with an attached service account in production. Which action most directly corrects the local identity selection?

**Select one.**

- A. Repeat gcloud auth login and select the approved account as active, while leaving the IDE environment and application process unchanged.
- B. Grant the old service account permission to impersonate the approved user, keeping the JSON file as the first credential source for the application.
- C. Change the default gcloud project to the bucket project and refresh the current access token, keeping GOOGLE_APPLICATION_CREDENTIALS set to the old key.
- D. Remove the stale credential-file override from the environment used by the IDE-launched process, then restart the application so ADC can use the approved local ADC file.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 3

A release pipeline deploys a Cloud Run service in project runtime-prod using a container image stored in an Artifact Registry repository in project shared-images. The pipeline's deployer account can read the repository, update the Cloud Run service, and act as the configured runtime service account. The image exists at the expected digest and was successfully built and tested. Deployment fails before the new application starts, and the repository audit log names service-RUNTIME_PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com as the principal denied artifactregistry.repositories.downloadArtifacts. The runtime account only needs database access after startup, and the build account already has the permissions required to publish images. Security policy requires repository-level grants where possible and prohibits broad project roles as a workaround. Which IAM change addresses the failing operation without extending application-runtime or build permissions unnecessarily?

**Select one.**

- A. Grant Artifact Registry Reader on the shared-images repository to the Cloud Run service agent belonging to runtime-prod.
- B. Grant Artifact Registry Reader on the shared-images repository to the application runtime service account selected in the Cloud Run revision.
- C. Grant Artifact Registry Writer on the shared-images repository to the pipeline deployer so its existing read permission also covers image deployment.
- D. Grant Cloud Run Service Agent on runtime-prod to the shared-images Artifact Registry service agent, leaving repository access unchanged.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 4

An inventory system publishes state-change events for individual warehouses to Pub/Sub. A warehouse has exactly one active publisher, which waits for a successful publish response before sending that warehouse's next event. Different warehouses must continue publishing and processing in parallel. A warehouse publisher may run in either of two application regions, but its ordered stream must use one designated Pub/Sub publishing region. Consumers need the service's ordering guarantee for events from the same warehouse, rather than relying on event timestamps or global serialization. They already finish processing a message before acknowledging it and handle redelivery safely. A proposed configuration assigns a new random ordering key to every message and uses each publisher's default regional routing. Which replacement configuration establishes the required ordering scope while preserving independence between warehouses?

**Select one.**

- A. Use one ordering key for the entire topic, keep regional endpoints local to each publisher, and increase subscriber concurrency to recover parallel processing across warehouses.
- B. Use warehouse ID as the ordering key and enable publisher ordering, but leave subscriber ordering disabled because acknowledgement order alone controls delivery order.
- C. Use warehouse ID as the ordering key, publish each warehouse stream through its designated regional endpoint, and enable ordering in the publisher and subscription.
- D. Keep random ordering keys, publish all messages through one regional endpoint, and sort each received batch by event timestamp before acknowledging the batch.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 5

A support portal stores generated diagnostic archives in a private Cloud Storage bucket with uniform bucket-level access. After authenticating a customer and checking ownership, the backend must let the customer's browser download one specific archive for the next ten minutes. Customers do not have Google identities, must not receive reusable service-account credentials, and must not gain permission to list other archives. The files are large, so the team wants Cloud Storage to serve the bytes directly instead of streaming them through the portal backend. The backend can sign requests using an approved service account that is authorized to read the relevant objects. Product owners accept that a customer could share the temporary link during its validity period. Which access design best meets the stated scope, delivery, and expiry requirements?

**Select one.**

- A. Grant the customer Storage Object Viewer on the bucket with a ten-minute IAM condition, and return the normal object URL after the portal ownership check.
- B. Generate a short-lived OAuth access token for the signing service account and send that token to the browser together with the requested archive path.
- C. Create a ten-minute signed upload policy restricted to the archive name, and reuse that policy to authorize the browser’s GET request for the existing object.
- D. After the ownership check, generate a V4 signed URL for GET on the specific object with a ten-minute expiry, and return that URL without changing bucket-wide access.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 6

A team is configuring an IDE coding assistant with an internally reviewed MCP server so developers can inspect staging deployment metadata while debugging. The task requires reading a small set of staging resources and proposing code changes; it does not require changing cloud resources or accessing production. The server package supports both inspection tools and tools that execute administrative commands. In the initial setup, the MCP process inherits the developer's broad cloud credentials, and the assistant is allowed to invoke every exposed tool without review. The team wants to retain useful inspection capabilities while enforcing the stated boundary even if the assistant selects an inappropriate tool. Administrators can control the server's execution environment, credential permissions, and the tools exposed to the assistant. Which TWO changes together provide a stronger boundary than adding a warning to the assistant's prompt?

**Select two.**

- A. Keep all administrative tools available, but add an instruction saying that production changes are forbidden unless the assistant considers them essential to debugging.
- B. Run the server in a restricted environment with only the required staging read permissions, without access to the developer’s broader production credentials.
- C. Keep the broad credentials but rename administrative tools with a dangerous prefix so the assistant can infer that it should normally avoid using them.
- D. Expose only the reviewed inspection tools needed for this workflow, disable administrative execution paths, and retain review of tool calls rather than blanket approval.
- E. Allow every tool automatically only for repositories owned by the organization, assuming repository ownership also restricts the server’s cloud permissions.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 7

A GKE Deployment processes compressed customer reports. Every replica occasionally receives a single valid report that requires about 400 MiB of memory while decompression is in progress, even when no other request is being processed by that replica. Profiling shows that memory is released afterward and does not grow across requests. The container currently requests 128 MiB and has a 256 MiB memory limit; its last termination reason is OOMKilled. The affected nodes have enough allocatable capacity for appropriately sized Pods, and there is no node-pressure eviction event. CPU utilization is low, and distributing traffic among more replicas does not reduce the memory required by one report. The application must continue accepting these valid reports without changing their format. Which Deployment change most directly addresses both the per-container failure and realistic scheduling of this workload?

**Select one.**

- A. Increase the HPA maximum replica count while keeping each container at a 128 MiB request and a 256 MiB limit, distributing future reports across more Pods.
- B. Set a memory request that reflects the measured working set and a limit above the observed peak with margin, then validate the revised Pod sizing under load.
- C. Raise the memory limit above the observed peak but keep the 128 MiB request, relying on low average CPU utilization to prevent overpacking of nodes.
- D. Increase the liveness failure threshold and termination grace period, keeping memory settings unchanged so the current report has more time to complete.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 8

A developer runs the Cloud SQL Auth Proxy on a laptop to test an application against a PostgreSQL instance that has only a private IP address. The proxy can authenticate to Google Cloud and obtain the required instance metadata, but attempts to establish the database connection time out. The laptop is on a home network without a VPN or another route to the instance's VPC. A colleague can connect using the same database configuration from a VM with private network reachability. The security team will not enable a public database address, and the application should continue connecting through the proxy rather than managing database TLS certificates itself. The developer wants to preserve the existing instance and credentials while correcting the missing prerequisite. Which action is the most appropriate next step?

**Select one.**

- A. Establish approved private connectivity from the laptop to the VPC, or run the proxy and test workload on a reachable development host, and use the private-IP connection path.
- B. Add the laptop’s public IP to authorized networks while retaining a private-IP-only instance and leaving the laptop without a route to the VPC.
- C. Grant the proxy identity Cloud SQL Admin instead of its current connection permissions, then retry from the same home network without a network change.
- D. Enable automatic IAM database authentication and replace the database password, keeping the same proxy placement and unreachable private-IP route.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 9

A customer-settings application uses a Bigtable instance replicated across two regions. An edit request can reach the application in either region, and the confirmation read may be handled by a different application instance from the one that performed the write. The current multi-cluster routing can send these database operations to different clusters, and customers sometimes see an older value immediately after a successful update. The product requirement is that confirmation reads observe that workload's acknowledged writes during normal operation. Analytics is a separate workload and can tolerate replication lag. For the editing workflow, the business accepts temporary unavailability during a primary-cluster outage rather than silently failing over and returning stale confirmations. There are no other writers for these settings. Which app-profile arrangement best fits these consistency and failure-handling requirements?

**Select one.**

- A. Keep multi-cluster routing for editing and confirmation reads, but increase replication capacity and insert a fixed short sleep before every confirmation read.
- B. Use one single-cluster profile for editing in each application region, routing every operation to the nearest cluster independently of the previous write.
- C. Route all editing writes and confirmation reads through a single-cluster profile targeting the same cluster; give analytics a separate profile suited to its tolerance for lag.
- D. Use multi-cluster routing for writes and a single-cluster profile for confirmation reads, selecting one fixed read cluster while leaving write destinations unrestricted.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 10

A Cloud Build pipeline runs integration tests against a dedicated test database after deploying a candidate application. Two pull requests can build concurrently, and each test suite currently creates, modifies, and deletes rows in the same schema using identical fixture identifiers. Both suites pass when run alone, but overlapping builds intermittently fail or, more dangerously, pass after reading data created by the other build. The tests intentionally exercise the real database integration, so replacing all database access with mocks would remove the behavior under test. The team wants to retain parallel builds and ensure that test failures block release even when cleanup succeeds. It can create temporary schemas and pass their names to both the candidate application and test runner. Which pipeline design best addresses isolation, useful coverage, and trustworthy failure reporting?

**Select one.**

- A. Keep the shared schema, randomize only the test execution order, and retry failed suites until one run succeeds before publishing the candidate release.
- B. Use a build-specific schema derived from a safely formatted BUILD_ID, configure the candidate and tests to use it, and clean it up while preserving a failed test exit status.
- C. Keep identical fixture identifiers but serialize database writes inside each test runner, allowing other build runners to continue using the shared schema concurrently.
- D. Create a build-specific schema only for the test runner while leaving the candidate application connected to the shared schema, and use cleanup success as the final step status.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 11

An organization exposes an orders API through Apigee in front of Cloud Run services. Existing mobile applications call /v1/orders and depend on the current response schema. A redesigned backend changes required fields and response meanings, and new clients will explicitly call /v2/orders. Old mobile clients cannot be updated immediately, so both contracts must remain available on the same public hostname for six months. Authentication and quota policies must continue applying to each contract, and a release of the new backend must not randomly send legacy requests to the incompatible implementation. The team can create separate API proxies and backend services, but it wants a routing boundary visible in the API configuration rather than hidden assumptions about which clients have upgraded. Which deployment approach most directly preserves both contracts during the transition?

**Select one.**

- A. Deploy the incompatible backend behind the existing /v1/orders proxy and use a weighted traffic split, gradually increasing the new backend’s percentage for every caller.
- B. Replace the /v1/orders base path with /v2/orders in the deployed proxy, retaining the old proxy revision in source control for clients that have not upgraded.
- C. Expose both backend versions under the same base path and choose between them by session affinity, allowing each client to stay on whichever version it first reaches.
- D. Keep a proxy for /v1/orders routed to the compatible backend and deploy a distinct /v2/orders proxy to the new backend, configuring required security and quota policies for both.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 12

A team creates a Cloud Logging distribution metric for API request latency. Every structured log entry contains a normalized route template such as /orders/{id}, a status class, a unique request ID, and a customer-specific object path. The initial metric extracts all four values as labels so operators can investigate individual slow requests. After a traffic increase, the number of time series grows rapidly even though the application still serves only a small set of route templates. Operations needs stable percentile dashboards and alerts by route and status class, while support engineers must still be able to locate a particular request using its identifier. The team can change instrumentation and create a replacement metric without discarding the underlying logs. Which design best preserves both aggregate monitoring and individual-request investigation with controlled metric cardinality?

**Select one.**

- A. Keep bounded route-template and status-class labels on the latency metric, retain request IDs and detailed paths in structured logs, and use those logs for individual lookups.
- B. Hash each request ID and object path before using them as metric labels, keeping one distinct hash per original value and leaving the remaining labels unchanged.
- C. Keep all four metric labels but change the dashboard to group by route and status class, relying on chart aggregation to reduce stored time-series cardinality.
- D. Remove request IDs and detailed paths from both metrics and logs, retaining only route-level totals so that support uses aggregate latency to identify individual failures.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 13

An application encrypts small confidential records by calling Cloud KMS directly with a symmetric encryption key. After a scheduled rotation, new encryption operations use the new primary key version. A security checklist proposes disabling every older version immediately, but records encrypted last month must remain readable and have not been rewritten. The team ultimately wants to retire the old version while keeping all retained records accessible. It can run a controlled migration that decrypts and re-encrypts existing records and updates their stored ciphertext, but that migration has not started. The application stores ciphertext in its own database rather than relying on a managed service's customer-managed encryption-key integration. Which plan correctly separates key rotation from data migration and avoids making still-needed records unreadable during the transition?

**Select one.**

- A. Disable the old version immediately after rotation because the key resource name is unchanged, then let decryption automatically use the new primary version for old ciphertext.
- B. Retain every old version indefinitely and stop rotating the key, because existing ciphertext cannot be migrated to a different version without changing the application’s storage system.
- C. Keep required old versions enabled, migrate and verify retained ciphertext under the new version, then retire old versions only after confirming no required data still depends on them.
- D. Promote the new version and wait one rotation interval before disabling the old version, treating elapsed time as evidence that the database’s ciphertext has been re-encrypted.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 14

A Cloud Build configuration builds a container, runs its automated tests, and pushes the image to Artifact Registry from an explicit docker push step. The image is present in the repository, and its tag and digest are recorded in the build logs. A release policy now requires Cloud Build-generated provenance for the produced artifact, and a build must not be reported as successful when that provenance cannot be generated. The team wants to use Cloud Build's supported artifact-output mechanism rather than maintain a custom provenance signer. Build and repository permissions are already sufficient, and the existing tests must remain release gates. An engineer suggests that retaining the docker push log is equivalent to generating provenance. Which configuration change most directly meets the artifact and build-success requirements?

**Select one.**

- A. Keep the explicit docker push and add a custom label containing the source commit to the image, then treat the label and successful push log as the required provenance.
- B. Declare the built image in the top-level images output field instead of relying on an explicit push step, and set options.requestedVerifyOption to VERIFIED.
- C. Keep the explicit docker push and enable repository vulnerability scanning, accepting the scan report as evidence of how the image was built and which source produced it.
- D. Declare the image only as a text entry in a Cloud Storage build artifact and set the release job to require a nonempty digest string before deployment.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 15

A team is deploying a containerized API to Cloud Run with a requirement for HTTP/2 all the way to the application container. The external clients use HTTPS, and the application framework supports both TLS-enabled HTTP/2 and cleartext HTTP/2. During a local test, the server works when it terminates TLS itself, so the team initially packages a certificate and configures the container to expect an incoming TLS handshake. On Cloud Run, the service's end-to-end HTTP/2 option is enabled, but requests fail at the container protocol boundary. The application listens on the configured port, and changing its business handlers does not affect the failure. The team wants to use the standard Cloud Run frontend and keep client-to-service encryption. Which protocol configuration correctly matches this deployment model without adding a separate TLS-terminating proxy inside the container?

**Select one.**

- A. Keep container-side TLS termination and replace its certificate with the public hostname’s certificate, leaving the end-to-end HTTP/2 setting enabled.
- B. Disable end-to-end HTTP/2 and keep the container restricted to TLS-enabled HTTP/2, relying on the frontend’s protocol conversion to satisfy the container listener.
- C. Leave end-to-end HTTP/2 enabled but configure the application listener for HTTP/1.1, because the encrypted frontend connection automatically upgrades container traffic.
- D. Keep end-to-end HTTP/2 enabled and configure the container to accept h2c on the configured port, while external clients continue using HTTPS to the Cloud Run frontend.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 16

A nightly reconciliation pipeline uses several workers to append independently computed partitions of one accounting batch to a single BigQuery table through the Storage Write API. Analysts query that table directly and must never see a partially completed batch. Workers finish at different times, and a coordinator can wait until every worker has successfully appended its rows before making the batch visible. The team has already chosen the Storage Write API and can create application-managed streams; it does not want to introduce a staging-table merge or require every analyst query to filter a separate completion flag. Within this one table, the desired publication unit is all streams belonging to the batch. Which stream type and completion sequence provides the required visibility boundary while allowing the workers to upload their data independently?

**Select one.**

- A. Use a pending stream per worker, wait for successful appends, finalize each stream, and have the coordinator commit the complete stream set in one BatchCommitWriteStreams request.
- B. Use the default stream for all workers, wait for every worker to finish, and write a completion record that analysts may optionally inspect after querying the table.
- C. Use application-created committed streams per worker and finalize them together, relying on finalization to hide previously appended rows until the last worker finishes.
- D. Use a pending stream per worker and have each worker finalize and commit its own stream immediately, relying on a common batch identifier to make all commits atomic.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 17

A Cloud Storage bucket holds processing artifacts that the application no longer needs thirty days after creation. A lifecycle Delete rule therefore matches objects whose age is at least thirty days. The same bucket also has an enforced ninety-day retention policy required by compliance. An operator notices that a forty-five-day-old object still exists and proposes reducing the lifecycle age threshold to ten days so deletion will happen sooner. Object Versioning and soft delete are disabled. The object has no event-based hold or temporary hold, and the compliance team has not authorized any reduction in retention. The operational goal is to remove objects automatically once deletion is permitted, rather than manually delete them or promise deletion at an exact second. Which interpretation and action correctly account for the interaction between the two policies?

**Select one.**

- A. Reduce the lifecycle age to ten days, because a matching Delete action takes precedence over a longer retention policy once the object is no longer used by the application.
- B. Keep the policies but configure an administrator account to run scheduled deletes after thirty days, because lifecycle alone must wait while administrator deletion can bypass retention.
- C. Keep the retention requirement and a suitable lifecycle Delete rule; matching objects remain protected until retention expires, after which lifecycle deletion can occur asynchronously.
- D. Disable the lifecycle rule and rely only on the ninety-day retention policy, because expiration of retention automatically deletes the object without a deletion mechanism.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 18

A container image was approved and deployed last week, but Artifact Analysis now reports a high-severity vulnerability in an operating-system package inherited from its base image. The source repository has not changed, and the affected package is not managed by the application's package-lock.json. The base-image maintainer has published a fixed image at a new digest. The team must produce and deploy a remediated artifact while preserving its usual compatibility tests and release evidence. A developer argues that rescanning the existing digest or assigning it a new approved tag should be enough because vulnerability metadata is updated continuously. The release system can build from a selected base digest and deploy a specific resulting application digest. Which TWO actions are necessary parts of a remediation that actually changes the vulnerable software reaching production?

**Select two.**

- A. Assign a new release tag to the existing application digest and rescan it, treating the changed tag as a fresh artifact whose installed operating-system packages are replaced.
- B. Update the build to use the fixed base-image content and build a new application image, retaining the required application functionality and compatibility checks.
- C. Change only package-lock.json to a newer application dependency version, leaving the affected operating-system package and selected base-image digest unchanged.
- D. Retain the existing application digest and renew its release approval once the scanner’s advisory feed describes an upstream fix, without rebuilding the application image.
- E. Check the new image’s vulnerability results and required tests, then roll out that resulting digest and verify that workloads have moved away from the affected artifact.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 19

A GKE Pod contains an application that reads a generated configuration file before opening its HTTP listener. A helper image can fetch approved startup configuration, validate it, write it to a shared volume, and exit successfully; if fetching fails, the application must not start with a partial file. The current manifest declares the helper and application as ordinary containers, and startup occasionally fails because the application reads the path before the helper has finished. The configuration is fixed for the lifetime of each Pod and can be generated again when a replacement Pod is created, so it does not require a persistent disk. The team wants Kubernetes to enforce the dependency rather than adding an arbitrary delay to the application. Which Pod configuration best provides the required ordering and file-sharing behavior?

**Select one.**

- A. Keep both as ordinary containers and list the helper first in the containers array, mounting an emptyDir volume into both so list order determines completion order.
- B. Run the helper as a regular init container that must complete successfully, share an emptyDir volume with the application, and let the application start afterward.
- C. Keep both as ordinary containers and add a readiness probe to the application, assuming that a failed readiness probe prevents its process from starting and reading the file.
- D. Run the helper as a regular init container, write the file only into the helper container’s writable layer, and rely on successful init completion to copy that layer into the application.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 20

A Firestore application stores device records with a large diagnostic text field, several diagnostic arrays, and a frequently updated timestamp used only when displaying a document fetched by its identifier. The application never filters or sorts on those diagnostic fields or that timestamp. Its actual list queries use status and region, with the required query indexes already defined. As writes increase, the team identifies index fanout as a significant contributor to write latency and index storage. Document identifiers are already well distributed, and no single document receives unusually concentrated updates. The team must keep all diagnostic content in the documents for identifier-based reads and preserve the existing status-and-region queries. Which schema and index change most directly reduces unnecessary indexing work without changing the application’s required access patterns or removing useful data?

**Select one.**

- A. Remove the large diagnostic fields from the documents entirely and store only their hashes, keeping all current indexes so existing query behavior remains unchanged.
- B. Keep all automatic indexes and split each diagnostic array into additional indexed fields, reducing field size while preserving the same total searchable values.
- C. Disable all indexes for the collection, including the indexes required by status-and-region queries, and replace those queries with unrestricted collection scans.
- D. Exempt the unqueried diagnostic fields and display-only timestamp from unnecessary single-field indexing, while retaining the indexes needed by the actual queries and the stored field values.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## İlk deneme kaydı

Başlangıç / bitiş / süre:

Mola veya yardım alınan sorular:

İlk turda atladıklarım:

Değiştirdiğim seçimler ve önceki seçimler:

Cevaplarını kaydettikten sonra [Türkçe anahtarı](../answers/scenarios/PCD-S06.md) aç. Açıklama sonrası düzeltmeler ilk deneme sonucunun üzerine yazılmaz.
