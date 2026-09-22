# PCD-S01 — Karma senaryo pilotu

15 özgün soru · İngilizce sorular · ayrı Türkçe açıklamalar.

**Önerilen süre:** 30 dakika (çalışma hedefidir, resmî süre veya başarı eşiği değildir). İlk turda kaynak kullanma. Her cevap için **E** (emin), **K** (kararsız) veya **T** (tahmin) yaz; en yakın alternatifini neden elediğini bir cümleyle belirt.

Her soruda dört seçenek vardır. `Select two` sorularında yalnızca iki seçenek seç. Sorular gerçek sınavdan alınmamıştır; bu pilot tam sınav kapsamını veya gerçek sınav zorluğunu garanti etmez.

## 1 - D

A Cloud Run service in project A reads a single Secret Manager secret in project B. It uses Google Cloud Client Libraries with Application Default Credentials. Downloaded service-account keys are prohibited. The service must not read other secrets in project B. Which configuration best meets these requirements?

**Select one.**

- A. Grant Secret Manager Secret Accessor on the secret to the build service account, keeping a different runtime identity.
- B. Attach a dedicated runtime service account and grant it Secret Manager Secret Accessor on project B.
- C. Attach a dedicated runtime service account and grant it Secret Manager Secret Accessor on the specific secret in project B.
- D. Attach a dedicated runtime service account and grant it Secret Manager Viewer on the specific secret in project B.

## 2 - A

Revision R1 of a Cloud Run service is serving all production traffic. You want to evaluate R2 with 5% of requests and restore traffic to R1 if errors increase. Both revisions are compatible with the current database schema, and session affinity is disabled. You want the fewest additional infrastructure components. What should you do?

**Select one.**

- A. Deploy R2 without production traffic, then configure a 95/5 revision traffic split and move traffic back to R1 if needed.
- B. Deploy R2 with all traffic and limit its maximum instances to 5% of R1's instance limit.
- C. Create a second service and use weighted DNS records to allocate exactly 5% of incoming requests to it.
- D. Replace R1's container image in place, then rebuild the old source code if rollback is required.

## 3 - B

A Cloud Build pipeline compiles an application in one step and packages it in a later step. Compilation succeeds, but the packaging container cannot find the binary written to `/tmp/output/app` in the compilation container. The steps already run sequentially. You want to transfer the file within this build without using an external storage service. What should you do?

**Select one.**

- A. Run both steps with the same service account so that their `/tmp` directories are shared.
- B. Add a longer `waitFor` dependency before packaging to allow filesystem synchronization.
- C. Upload the binary to Artifact Registry in a third step and download it in the packaging step.
- D. Write the binary to `/workspace/output/app` and read that path from the packaging step.

## 4 -B

An authenticated customer may download one private Cloud Storage object for the next ten minutes. The customer has no Google identity. Your application must authorize the customer, but you do not want it to proxy the file bytes. Anyone possessing the temporary link may use it during that period, which is acceptable for this use case. What should you implement?

**Select one.**

- A. Add the customer's application user ID to the bucket's IAM policy with Object Viewer.
- B. After authorization, issue a short-lived signed GET URL for the specific object.
- C. Grant `allUsers` Object Viewer on the bucket and remove the binding ten minutes later.
- D. Return the application's OAuth access token and the object's regular URL to the customer.

## 5 -C

After a customer schedules a reminder, your application must send an HTTP request to a specific Cloud Run handler no earlier than the requested time, usually a few hours later. Delivery may be retried, and the queue must limit the dispatch rate to protect the downstream system. Which design is the most direct fit?

**Select one.**

- A. Publish to a Pub/Sub topic and rely on the acknowledgment deadline to schedule the first delivery.
- B. Create an Eventarc trigger for each customer and configure the trigger's event filter with the requested time.
- C. Create a Cloud Task with a scheduled delivery time and HTTP target; configure queue dispatch limits and an idempotent handler.
- D. Keep a request open on Cloud Run until the scheduled time, then invoke the handler from that request.

## 6 -C

Cloud Run service A calls service B at B's default `run.app` URL. B requires IAM authentication. Network ingress already permits this request. A uses a dedicated runtime service account; no custom audience is configured on B. Which TWO actions are required for an authenticated, authorized call without a downloaded key?

**Select two.**

- A. Grant A's runtime service account `roles/run.invoker` on B.
- B. Send an OAuth access token with a Cloud Platform scope as the invocation credential.
- C. Grant B's runtime service account `roles/run.invoker` on A.
- D. Obtain a Google-signed ID token for A's runtime identity with B's service URL as the audience, and send it in the Authorization header.

## 7 -D 

A Cloud Run service uses a third-party library that stores request-specific data in process-global mutable state. Testing confirms that simultaneous requests in one instance corrupt results. The library cannot be changed before the next release, and sequential requests are safe. You can accept additional instances and cost. Which immediate configuration change directly addresses the demonstrated problem?

**Select one.**

- A. Set maximum instances to one while keeping the current concurrency.
- B. Set maximum concurrent requests per instance to one, and load-test the resulting capacity and cost.
- C. Increase the number of vCPUs while keeping the current concurrency.
- D. Enable session affinity so that requests from the same client usually reach the same instance.

## 8 - D

A team has a standard Node.js HTTP application with supported dependencies and a valid start script. It has no custom operating-system packages and no Dockerfile. The team wants to deploy to Cloud Run while minimizing maintenance of container build instructions. Which approach best fits?

**Select one.**

- A. Upload the source archive to an Artifact Registry Docker repository and deploy the archive as an image.
- B. Write and maintain a multi-stage Dockerfile even though the application fits the supported source deployment workflow.
- C. Configure a Cloud Run job that installs dependencies and runs an HTTP server indefinitely.
- D. Deploy from source using Cloud Run's build pipeline with Google Cloud buildpacks to create the container image.

## 9 -A 

A Firestore application stores `availableSeats` in an event document. Many customers may reserve the last seat concurrently. Each successful reservation must decrement the count and create a reservation document atomically. The count must never become negative. What should the application do?

**Select one.**

- A. Use a transaction that reads the count, verifies availability, and writes both changes; allow the client library to retry on conflicts.
- B. Read the count outside a transaction, then use a batched write to decrement it and create the reservation.
- C. Use an atomic increment of -1 and independently create a reservation document without reading the count.
- D. Serialize requests with an in-memory mutex in each Cloud Run instance, then perform the two writes separately.

## 10 -C

An Eventarc Standard trigger delivers Cloud Storage events to a Cloud Run handler. The handler updates an inventory record. You observe repeated deliveries of the same event, sometimes concurrently. You need to prevent applying the same inventory change twice, including after an instance restart. Which design best meets this requirement?

**Select one.**

- A. Cache handled event IDs in the container's memory and return success for matches.
- B. Write a processed marker before updating inventory, using two separate database operations.
- C. Use the event source and ID as a deduplication key and atomically record that key with the inventory update in a durable database transaction.
- D. Reduce the event retention period so duplicates expire before they can reach the handler.

## 11 - C, B

A developer's Python application uses Google Cloud Client Libraries without explicit credentials. Locally, it reports that default credentials cannot be found, even after `gcloud auth login`. In Cloud Run, the same code will run with a dedicated service account. Downloaded keys are prohibited. Which TWO actions provide the intended credential setup?

**Select two.**

- A. Copy the developer's local ADC credential file into the production container.
- B. Run `gcloud auth application-default login` locally, using a permitted developer identity for local testing.
- C. Attach the dedicated service account to Cloud Run and grant that identity the resource permissions needed by the application.
- D. Grant the runtime role only to the deployment identity, leaving the attached runtime identity without resource access.

## 12 - A

A Cloud Run API is fast during steady traffic but slow for the first request after long idle periods. Traces show that application initialization accounts for most of this delay; request processing itself is fast. The service currently scales to zero. You want to reduce this specific source of latency while keeping Cloud Run, and you accept some idle capacity cost. What should you do first?

**Select one.**

- A. Configure a nonzero minimum instance count sized for the normal workload, then measure first-request latency and cost again.
- B. Increase the request timeout while keeping the service scaled to zero between requests.
- C. Increase maximum instances while keeping minimum instances at zero.
- D. Enable session affinity while keeping minimum instances at zero.

## 13 - D

A sequential Cloud Build pipeline runs tests and then deploys to Cloud Run. Failed tests currently do not stop deployment because the test step sets `allowFailure: true`. The test command already exits nonzero when tests fail. Deployment must occur only if the tests pass. What is the smallest appropriate correction?

**Select one.**

- A. Keep `allowFailure: true` and add an email alert after deployment.
- B. Keep `allowFailure: true` and make deployment explicitly wait for the test step to finish.
- C. Run tests after deployment and rely on application monitoring for rollback.
- D. Remove the failure-tolerant setting from the test step and keep deployment dependent on successful completion of the preceding steps.

## 14 - B

A new global financial application needs relational schemas, SQL queries, and atomic transactions spanning account rows. It expects to grow beyond the write capacity of a single database node. The team wants a managed database with horizontal scaling and strong transactional consistency across regions, without implementing application-level sharding. Which option best matches these requirements?

**Select one.**

- A. Cloud SQL with read replicas to distribute both reads and all transaction writes.
- B. Spanner with an appropriate multi-region configuration and transactional access.
- C. BigQuery with scheduled queries that periodically reconcile account balances.
- D. Bigtable with separate account rows and application code coordinating cross-row transfers.

## 15 - C

An order process calls three services in sequence, passes each result to the next, branches on a fraud decision, and may wait hours for an external approval callback. Operators need to inspect the execution state of each order. You want managed coordination without writing and hosting a custom state machine. What should you choose?

**Select one.**

- A. Pub/Sub choreography, with each service independently publishing the next event and operators reconstructing state from logs.
- B. Cloud Tasks queues, with each handler maintaining the full process state and scheduling the next handler itself.
- C. Workflows, using explicit steps, conditions, retry policies, and an authenticated callback to resume the execution.
- D. A Cloud Run HTTP service that keeps the initial request open until all services and the external approval finish.

## Cevap formu

Her satır için örnek biçim: `1: A | K | En yakın alternatif B; çünkü …`

```text
1:  |  |
2:  |  |
3:  |  |
4:  |  |
5:  |  |
6:  |  |
7:  |  |
8:  |  |
9:  |  |
10: |  |
11: |  |
12: |  |
13: |  |
14: |  |
15: |  |
```

İlk tur bittikten sonra [ayrı cevap anahtarını](../answers/scenarios/PCD-S01.md) aç. [Senaryo dizini](README.md).
