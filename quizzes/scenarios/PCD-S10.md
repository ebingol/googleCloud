# PCD-S10 — 20 soruluk karma deneme

**Hedef: 45 dakika · 20 soru · 18 tek seçim + 2 çift seçim.**

29 Eylül iş çıkışı çözümü için hazırlandı. Sorular özgündür; gerçek sınav sorusu veya doğrulanmış zorluk eşdeğeri değildir. İngilizce senaryoları ve seçenekleri okuyarak en uygun cevabı seç.

- Q6 ve Q18 için **iki** seçenek; diğerlerinde **bir** seçenek işaretle.
- Başlangıç ve bitiş saatini kaydet. 45 dakika dolarsa o andaki cevaplarını/boşlarını sabitle; devam edersen ek süre ve sonradan verilen cevapları ayrı belirt.
- E/K/T güven işareti isteğe bağlıdır. Kararsızsan ikinci seçeneği de yazabilirsin; her soruya gerekçe yazman gerekmiyor.
- Cevapları örneğin `1-b, 2-d, 3-a` biçiminde gönder. İlk turda cevap anahtarını açma.

Başlangıç: ____ · 45. dakika ulaşılan soru: ____ · Bitiş / ek süre: ____

---

### Question 01

A publishing company serves public product illustrations from a regional backend behind a global external Application Load Balancer. Each illustration already has a versioned URL and appropriate public cache headers, and its contents never change at that URL. Users near the backend receive images quickly, but users on other continents repeatedly download the same popular images with high latency. Backend CPU and database usage remain low. The team wants to improve delivery latency without changing the application or operating additional regional application stacks. What should you do?

**Select ONE answer.**

**A.** Add Memorystore in the backend region and cache the image bytes in the application.

**B.** Increase the backend instance count and distribute image requests across the additional instances.

**C.** Enable Cloud CDN for the supported backend and cache the eligible image responses at the edge.

**D.** Increase browser cache lifetimes while continuing to serve every new browser from the regional origin.

---

### Question 02

A developer occasionally needs to inspect Google Cloud resources and run a few gcloud commands from a company-managed laptop. Installing local development tools is prohibited, but browser access to the Google Cloud console is permitted. The tasks take about fifteen minutes, require standard command-line tools, and do not depend on access to a private VPC. The developer does not need a custom development image or a continuously running process. Which environment meets these requirements with the least provisioning and maintenance effort?

**Select ONE answer.**

**A.** Create a Cloud Workstations configuration with a custom image for these administrative sessions.

**B.** Create a Compute Engine VM and maintain the command-line tools for browser-based SSH access.

**C.** Create a Cloud Build pipeline that accepts and executes each interactive administrative command.

**D.** Use Cloud Shell to run the standard Google Cloud command-line tools from the browser.

---

### Question 03

A new GKE Deployment never starts its application container, while the previous Deployment remains healthy. The new Pods report ImagePullBackOff. Their events show that the requested image tag cannot be found in Artifact Registry. You confirm that the repository hostname is correct, network access works, and the node identity can download another image from that repository. The approved release image exists, but the Deployment specifies a different tag because of a release configuration error. What is the most appropriate corrective action?

**Select ONE answer.**

**A.** Grant the node identity Artifact Registry Administrator so it can retrieve the requested image tag.

**B.** Increase the startup probe failure threshold so that the container has more time to initialize.

**C.** Update the Deployment image reference to the existing approved release artifact and roll out the change.

**D.** Increase the container memory limit so that image initialization can complete before the first probe.

---

### Question 04

A pull subscriber processes Pub/Sub messages using a supported high-level client library. Processing normally takes several minutes and varies substantially between messages. Flow control already keeps the number of outstanding messages within the worker capacity, and processing is idempotent. However, automatic acknowledgment deadline extension was disabled, so messages are redelivered while healthy workers are still processing them. The application must acknowledge only after its result is durably stored. Which change most directly reduces these premature redeliveries without acknowledging unfinished work?

**Select ONE answer.**

**A.** Acknowledge each message when processing starts, and rely on the worker logs to identify later failures.

**B.** Reduce the maximum outstanding message count, leaving acknowledgment deadline extension disabled.

**C.** Enable lease management and configure its extension limits to accommodate expected processing durations.

**D.** Increase subscription message retention, leaving the acknowledgment deadline behavior unchanged.

---

### Question 05

A Java application on Cloud Run queries Cloud SQL for PostgreSQL. The application authenticates users correctly and connects through an encrypted connection with a restricted database account. A security review finds that a search value from an HTTP request is concatenated into the WHERE clause of a SQL statement. Attackers can manipulate the value to change which rows are returned. The search feature must continue accepting ordinary punctuation in customer names. Which application change best addresses the vulnerability at its source?

**Select ONE answer.**

**A.** Reject input containing spaces, quotation marks, or SQL keywords before constructing the SQL string.

**B.** Keep the concatenated query, but replace database password authentication with IAM database authentication.

**C.** Keep the query construction, but move the database to private IP and require the Cloud SQL Auth Proxy.

**D.** Use a prepared statement with placeholders and bind the search value as a parameter.

---

### Question 06

A team uses an existing Artifact Registry repository named releases. Cloud Build runs under a dedicated service account that must upload new images to this repository. A separate audit tool uses another service account to download those images for inspection; it does not deploy workloads. Neither account has inherited access to this repository, and both already have the unrelated permissions needed for their own execution environments. Repository creation, deletion, and IAM administration are handled by another team. Which two grants meet the stated artifact access requirements with the narrowest scope?

**Select TWO answers.**

**A.** Grant the build service account Artifact Registry Writer on the releases repository.

**B.** Grant the build service account Artifact Registry Administrator on the releases repository.

**C.** Grant the audit service account Artifact Registry Reader on the releases repository.

**D.** Grant the audit service account Artifact Registry Writer on the releases repository.

**E.** Grant both service accounts Artifact Registry Reader at the project level.

---

### Question 07

An HTTP Cloud Run function creates a new database client and performs expensive connection setup on every invocation. Profiling shows that this setup contributes significantly to response latency even when the same function instance handles successive requests. The supported client is thread-safe, its connection settings are identical for all users, and its documented lifecycle allows reuse. User-specific authorization and request data must remain isolated. Which implementation change best reduces repeated setup while preserving those isolation requirements across concurrent requests?

**Select ONE answer.**

**A.** Initialize a reusable client at instance scope and keep authorization decisions and user data within each request.

**B.** Cache the first user’s database result globally and return it to subsequent requests on that instance.

**C.** Keep creating the client per request and increase minimum instances to eliminate repeated connection setup.

**D.** Keep a global client together with a global mutable variable holding the current request’s user identity.

---

### Question 08

A company is moving an existing PostgreSQL order-management application to Google Cloud. The application relies on relational joins, foreign keys, and transactions spanning several tables. Its tested capacity requirements fit within a single managed PostgreSQL instance, and all writers will remain in one region. The team needs managed backups and high availability but has no requirement for globally distributed writes. It wants to minimize changes to the existing database schema and application queries. Which database service is the best fit?

**Select ONE answer.**

**A.** Firestore, with related tables converted into document collections and transaction logic rewritten.

**B.** Spanner, with the schema and queries adapted for a distributed relational database.

**C.** Cloud SQL for PostgreSQL, configured with appropriate high availability and backups.

**D.** Bigtable, with the schema redesigned around access patterns and relational joins moved into application code.

---

### Question 09

A developer starts an asynchronous export through a Google Cloud API. The API returns a long-running operation name, which the application stores durably before polling. Later, the client’s polling deadline expires, but a separate status check shows that the operation is still running on the server and has not failed. The export must not be submitted again because another submission would create additional work. After the application restarts, what should it do to continue tracking the original export?

**Select ONE answer.**

**A.** Retrieve the saved operation and resume polling its status until completion or a reported operation error.

**B.** Submit the export request again with a longer polling deadline and discard the saved operation name.

**C.** Mark the export as failed because expiration of a client polling deadline cancels the server operation.

**D.** Increase the API request quota and create a replacement operation before inspecting the original result.

---

### Question 10

A Java service rejects a token when the current time is equal to or later than its expiration time. Gemini Code Assist generates unit tests that create a token, sleep briefly, and then call the validation method. These tests pass locally but fail intermittently in Cloud Build when the runner is busy. The team wants fast, deterministic tests that exercise the real expiration comparison, including the exact boundary. Production must continue using the actual current time. What should the developer change?

**Select ONE answer.**

**A.** Increase each sleep duration and allow the pipeline to retry failed tests several times.

**B.** Mock the validation method to return the expected Boolean value for each test case.

**C.** Remove the expiration boundary tests and retain only tokens that expire far in the future.

**D.** Inject a Clock and use controlled instants before, at, and after expiration in the tests.

---

### Question 11

Two internal services exchange a stream of commands and progress updates during a live analysis session. Either service must be able to send multiple messages independently while the session remains open. Both teams already use Protocol Buffers and generated clients, and their Cloud Run networking is configured to support the required HTTP/2 communication. They want a typed service contract without implementing repeated polling or a separate asynchronous broker workflow. Which API design most directly fits the communication pattern and existing tooling?

**Select ONE answer.**

**A.** Use unary gRPC calls, opening a new request for every progress update from either service.

**B.** Define a bidirectional streaming gRPC method for commands and progress updates.

**C.** Use a server-streaming gRPC method with all client commands fixed in the initial request.

**D.** Expose a REST status resource and have each client periodically poll for new progress updates.

---

### Question 12

A GKE application experiences sustained high CPU utilization during a traffic increase. Its HorizontalPodAutoscaler has valid metrics and correctly configured CPU requests. Eight replicas are running, maxReplicas is eight, and the HPA reports that its calculated recommendation is above the configured maximum. No Pods are pending, and existing nodes have enough allocatable resources for additional replicas. Load testing has also confirmed that the database can handle more application replicas. Which change most directly allows the HPA to respond to this demand?

**Select ONE answer.**

**A.** Increase the node pool maximum size while leaving the HPA maximum replica count unchanged.

**B.** Increase the HPA CPU utilization target so that the current replica count is considered sufficient.

**C.** Raise maxReplicas to a tested value consistent with the available application and backend capacity.

**D.** Lengthen the HPA scale-down stabilization window while keeping the current replica limits.

---

### Question 13

A customer application signs users in with Identity Platform. Its browser client sends a Firebase ID token and a userId field to a custom backend over HTTPS. The backend currently selects account records using the submitted userId without validating the token. A user can therefore change that field and request another customer’s data. The backend already has legitimate database access, and customers should not receive Google Cloud IAM roles. Which backend change establishes the correct identity boundary before applying account-level authorization?

**Select ONE answer.**

**A.** Decode the token payload without signature verification and compare its UID with the submitted userId.

**B.** Verify the ID token with the configured Admin SDK, derive the caller UID from it, and enforce access for that UID.

**C.** Keep trusting userId, but require the browser to verify its token before sending the HTTPS request.

**D.** Grant each customer a database-related Google Cloud IAM role and continue using the submitted userId.

---

### Question 14

A developer is editing a containerized service in VS Code and testing it on a nonproduction GKE cluster. The Kubernetes context and permissions are already verified, and the repository contains a working Skaffold configuration. For each small change, the developer manually builds an image, deploys it, opens logs, and attaches a debugger. The team wants a shorter edit-test-debug loop inside the IDE while keeping its existing production release pipeline. Which approach most directly addresses this local development workflow?

**Select ONE answer.**

**A.** Use Gemini Cloud Assist to investigate production incidents after each local source-code change.

**B.** Add a production Cloud Build trigger that deploys every file save directly to the production cluster.

**C.** Use Gemini Code Assist completion alone to replace the image build, deployment, and debugger lifecycle.

**D.** Use Cloud Code with the Skaffold development workflow to iterate on and debug the nonproduction service.

---

### Question 15

A Cloud Run service emits structured application logs with correctly parsed severity fields. ERROR entries appear in the project’s _Default log bucket, but INFO entries do not. You confirm that the service emits both, the ingestion path is working, and your account can view the relevant bucket. The _Default sink includes these application logs but has an exclusion matching every entry below ERROR; no other sink stores them. The team now needs future INFO entries from this service for troubleshooting. What should you change?

**Select ONE answer.**

**A.** Adjust the sink exclusion so this service’s INFO entries are routed to the log bucket.

**B.** Extend the log bucket retention period so that excluded INFO entries become available for querying.

**C.** Change every INFO entry to ERROR so the existing exclusion continues to apply without modification.

**D.** Increase trace sampling so the missing application log entries are copied into the log bucket.

---

### Question 16

A service must publish a small set of configuration documents to Firestore. The complete document IDs and replacement values are already known before the operation starts. No write depends on reading a current document value, and the business requirement is that either every document is updated or none is. The set fits comfortably within the documented batch limits. Other application checks have already validated the configuration. Which write approach meets the atomicity requirement without adding an unnecessary read-and-retry transaction workflow?

**Select ONE answer.**

**A.** Commit all of the document writes together in a single atomic write batch.

**B.** Read every document in a transaction before writing, even though the replacement values do not use those reads.

**C.** Issue independent document writes in parallel and report success if most writes complete.

**D.** Write each document separately and delete the successfully written documents if a later write fails.

---

### Question 17

A monorepo contains services/payments, services/catalog, shared/pricing, and docs directories. The payments build must run when files under services/payments or shared/pricing change, because the payments service imports that shared library. Changes limited to services/catalog or docs must not trigger this build. The Cloud Build trigger already has the correct repository, push event, and branch filter, and no ignored-file patterns are configured. Which included-file configuration correctly captures the payments build’s dependency boundary, including changes in nested subdirectories?

**Select ONE answer.**

**A.** Include only services/payments/** because library changes will be detected when the next service build runs.

**B.** Include services/payments/** and shared/pricing/** in the trigger’s included-file patterns.

**C.** Include every path with ** so that no shared dependency change can be missed.

**D.** Include services/payments/* and shared/pricing/*, covering only immediate children of those directories.

---

### Question 18

A team deploys a single-container HTTP service to Cloud Run. The service configuration sets the container port to 8080, and the platform provides PORT=8080. The application currently ignores PORT and starts its HTTP server on 127.0.0.1:5000. Startup logs show successful initialization, but Cloud Run cannot reach the application. The framework supports configurable listen addresses and ports, and no changes to the service’s configured port are planned. Which two application changes together satisfy the network listening requirements for this deployment?

**Select TWO answers.**

**A.** Keep listening on 127.0.0.1 and add a health-check route to the application.

**B.** Bind the HTTP server to 0.0.0.0 rather than the loopback address.

**C.** Terminate external HTTPS inside the container instead of letting Cloud Run terminate TLS.

**D.** Increase minimum instances while retaining the existing listen address and port.

**E.** Read PORT and configure the HTTP server to listen on that value.

---

### Question 19

A Cloud Run job imports a file into a database. Its task is configured with retries, and the import logic is idempotent so rerunning a failed task is safe. During a transient database outage, the application catches an exception, writes an error log, and then exits with code 0. Cloud Run records the task as successful, so the configured retry never occurs. The team wants failed imports to use the existing retry policy and successful imports to finish normally. What should change?

**Select ONE answer.**

**A.** Increase the retry count while leaving the application’s exit behavior unchanged.

**B.** Exit with a nonzero code when the import fails, and use exit code 0 only after successful completion.

**C.** Return an HTTP 500 response from a new endpoint after logging the import exception.

**D.** Increase the task timeout so Cloud Run interprets the logged database exception as a retryable failure.

---

### Question 20

A service runs in two regions. The agreed availability SLI is the fraction of successful valid requests across the entire service, giving every valid request equal weight. In one measurement window, region A handles 900 valid requests and all succeed; region B handles 100 valid requests and 90 succeed. A dashboard currently averages the two regional success percentages and reports 95%. Both regions use the same success definition and time window. Which aggregation correctly implements the agreed service-wide SLI?

**Select ONE answer.**

**A.** Use the lower regional success percentage as the overall service success percentage.

**B.** Divide the sum of successful valid requests by the sum of valid requests across both regions.

**C.** Average the regional success percentages equally, because both regions belong to the same service.

**D.** Weight each regional success percentage by its allocated CPU capacity rather than its request count.

---

[Ayrı Türkçe cevap anahtarı — çözüm sonrası](../answers/scenarios/PCD-S10.md)
