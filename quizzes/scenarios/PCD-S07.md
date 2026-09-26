# PCD-S07 — Uzun senaryolarla mimari karar denemesi

26 Eylül 2026 · **20 özgün İngilizce soru: 18 tek seçim, 2 çift seçim (Q6/Q11).**

Birincil kapsam güncel resmî exam guide: dört ana alan 6/5/5/4 dağılımıyla örneklenir. Her alt konu bu sette ölçülmez; sorular gerçek sınavdan alınmamıştır ve gerçek sınav zorluğuyla kalibre edilmiş değildir.

**Süreyi kaydet; bu tur zorunlu bitiş sınırı yok.** Önceki S06 süren 73 dakikaydı. İlk turda anahtarı açma. Tek seçimde bir harf, çift seçimde iki harf yaz; çoklu seçimde yalnız tam doğru küme 1 puandır. Toplam 20 puan.

Cevabına E/K/T (emin/kararsız/tahmin) ekleyebilirsin. Özellikle kararsız kaldığın sorularda ikinci düşündüğün şıkkı ve kararı belirleyen koşulu bir cümleyle yaz. Bilmediğin terimi **Bilmediğim: …** olarak belirt; İngilizce anlam ile teknik bilgiyi ayrı değerlendireceğiz.

## 1

A product service running on many application instances caches expensive database query results in Memorystore for Redis. Database capacity is adequate for normal cache misses, but a popular campaign causes hundreds of instances to request the same product immediately after its cached entry expires. Each instance independently executes the same query before writing an identical result back to Redis. Redis latency and memory usage remain healthy, while database load spikes sharply at these expiration boundaries. The business permits requests to wait briefly for a refresh, but does not permit serving values beyond the approved freshness limit. Duplicate refreshes during rare failures are acceptable; the cache is not used to enforce payment correctness or durable ownership. The team wants to reduce concurrent rebuilds of the same entry across instances without serializing refreshes for unrelated products. Which application change best addresses the observed problem?

**Select one.**

- A. Increase Redis capacity and keep independent cache-miss queries, relying on additional memory to prevent popular entries from reaching their configured expiration times.
- B. Put a mutex around refreshes inside each application process, allowing every other instance to refresh the same expired product independently.
- C. Coordinate refreshes across instances per product using a bounded, ownership-safe lease; waiting requests recheck the cache within a deadline before a controlled fallback.
- D. Extend every entry's lifetime beyond the approved freshness limit and serve its previous value until any instance eventually replaces it.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 2

A Cloud Build integration test must call an internal test API running on a Compute Engine VM that has only a private address in the team's VPC network. The API uses application authentication, and the build service account already has every required application permission. Tests pass from an approved VM in that VPC but time out from the current Cloud Build default pool before any request reaches the API logs. Security policy prohibits adding a public endpoint, and the team wants to keep managed build workers rather than maintain its own build servers. The API is directly in this VPC, with no additional peered network or on-premises hop involved. The team can configure the required private connectivity and narrowly scoped firewall rules. Which change most directly enables the tests while preserving the stated network and operational requirements?

**Select one.**

- A. Run the build in a Cloud Build private pool connected to the VPC, and permit the necessary worker-to-API network path while retaining application authentication.
- B. Keep the default pool and grant its service account a broader project role, using successful IAM authorization to establish the missing private route.
- C. Keep the default pool and publish the API's private address in public DNS, allowing the workers to reach that address without a VPC connection.
- D. Move the test API to an authenticated public endpoint restricted to the build identity, preserving identity controls while avoiding private-pool connectivity.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 3

A developer deploys a service with `gcloud run deploy --source .` from a local directory containing a Dockerfile. A code-generation command has already produced the required `generated/` directory on that machine, and a local Docker build includes it successfully. The remote source build fails at the Dockerfile's COPY instruction because the same directory is absent. Inspection shows that `.dockerignore` permits the directory, while `.gcloudignore` includes `.gitignore`, which excludes generated output. The team deliberately keeps generated files out of Git, and this release process requires uploading the locally generated files rather than regenerating them in the remote build. Credentials, build permissions, and the target project have already been verified. Which correction addresses the failed deployment without committing generated files or broadly uploading unrelated local files that should remain excluded from the build context?

**Select one.**

- A. Add another exception only to `.dockerignore`, leaving the source-upload exclusion unchanged so that the remote Docker daemon can discover the local generated directory.
- B. Change the Cloud Run runtime service account to one with Storage Object Viewer, allowing the running revision to retrieve the missing build input automatically.
- C. Remove `.gcloudignore` entirely and keep `.gitignore` unchanged, relying on the default source-upload behavior to include every generated file.
- D. Add narrowly scoped `.gcloudignore` exceptions after the included rules for `generated/` and its required contents, verify the upload file list, and redeploy.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 4

Two services update different custom metadata fields on the same Cloud Storage object. Each service reads the existing metadata map, changes its own field, and submits the resulting map. Because the read and update are separate requests, one service sometimes overwrites a change made by the other after its initial read. Object bytes are not changed during this operation, and the upload workflow guarantees that the object generation remains fixed throughout the metadata updates. The team needs optimistic concurrency control without introducing a separate database or distributed lock. A conflict should cause the losing service to read the latest metadata, merge its intended change, and attempt the update again rather than silently discard another writer's update. Which request condition and conflict-handling strategy best implements this behavior using the metadata version supplied by Cloud Storage?

**Select one.**

- A. Use `ifGenerationMatch` with the observed content generation, and retry the identical metadata map whenever another metadata-only update has succeeded.
- B. Use `ifMetagenerationMatch` with the observed metadata version; on a precondition failure, reread, merge the intended change, and retry with the new version.
- C. Use `ifMetagenerationMatch`, but retry the original map with each newly observed version so that the service's last write eventually becomes authoritative.
- D. Set `ifGenerationMatch=0` for each metadata update, allowing Cloud Storage to serialize modifications as conditional creation of the existing object.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 5

An internal support application runs behind an HTTPS load balancer protected by Identity-Aware Proxy. The application currently trusts the email value in `x-goog-authenticated-user-email` and uses it to select the user's support records. A security review asks for application-level verification that will still reject forged user identities if an unintended network path to the backend is introduced later. The network team will continue restricting backend access, but the application must provide an additional identity check rather than depend exclusively on that restriction. The expected IAP audience for this backend is known, and the framework supports verification using IAP's published signing keys. Health checks have a separate non-sensitive path. Which handling of ordinary application requests best establishes a verified user identity while rejecting assertions issued for an unrelated protected backend?

**Select one.**

- A. Verify the IAP JWT assertion's signature, issuer, time claims, and expected audience; derive the user identity from the validated claims and apply application authorization.
- B. Decode the IAP JWT assertion and compare its audience, then trust the decoded email without signature verification because IAP normally strips client-supplied headers.
- C. Verify the assertion's signature and expiration, accepting any audience so the same signed assertion can authorize access to every backend in the organization.
- D. Require both unsigned user-email and user-ID headers to be present, comparing their formats before using them as the authenticated identity.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 6

A Docker build executed in Cloud Build downloads a private dependency using a short-lived repository token. Secret Manager access is already restricted to the build identity, and the token is supplied to the build step without being committed to source control. However, the Dockerfile currently copies a token-bearing configuration file into one layer and deletes it in a later RUN instruction. The organization exports intermediate build caches for reuse, so inspecting only the final container filesystem is insufficient. The team must keep the dependency download working while preventing the credential from being embedded in image layers or exported build artifacts. BuildKit is available, and the dependency tool can read its credentials from a temporary file without copying them into its outputs. Which TWO changes together address the remaining credential-exposure paths in this build?

**Select two.**

- A. Keep the COPY and later deletion, but publish only the final image tag because deleted files cannot be recovered from an exported intermediate layer.
- B. Pass the token through a BuildKit secret mount available only to the dependency-download RUN instruction, instead of copying it or passing it as a build argument.
- C. Replace the configuration file with Dockerfile ENV values and unset them in the final stage, retaining the environment-based token in intermediate build metadata.
- D. Ensure the download command neither prints nor copies the mounted credential into outputs, and export only artifacts that do not contain secret material.
- E. Retain the existing layers and shorten the token's lifetime, treating expiration as sufficient to satisfy the requirement that credentials never enter exported artifacts.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 7

A GKE Deployment uses an HPA with a reliable external demand metric and enough available node capacity. Scaling up works as intended: new Pods become ready quickly and reduce the backlog. However, demand repeatedly drops for less than a minute between bursts, and an explicitly configured zero downscale stabilization window allows the HPA to remove most additional replicas immediately. The next burst then triggers another scale-up, producing avoidable churn and latency. The metric is accurate, and permanently keeping peak capacity would exceed the team's cost target. The goal is to retain recently needed capacity through short dips while still allowing eventual scale-down during sustained quiet periods. Scaling up in response to genuine new demand must remain prompt. Which HPA configuration change most directly targets this behavior without changing the application's resource requests or replacing the demand metric?

**Select one.**

- A. Increase the scale-up stabilization window while keeping immediate scale-down, delaying reactions to each new burst until demand remains high long enough.
- B. Raise `minReplicas` to the observed peak permanently, using the fixed minimum to eliminate all scale-down activity during both short and long quiet periods.
- C. Configure a suitable `behavior.scaleDown.stabilizationWindowSeconds`, retaining appropriate replica bounds and prompt scale-up behavior.
- D. Lower `maxReplicas` to reduce the size of each scale-up, leaving the immediate downscale policy and the repeated removal of recently added capacity unchanged.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 8

A service inventories object names and sizes from a large Cloud Storage bucket through the JSON API. It already processes one page at a time and follows the response's `nextPageToken` when that field is present. To reduce response size, a developer changes the request to use `fields=items(name,size)`. The resulting requests succeed, but the application now stops after its first page even though the bucket contains many more objects. The bucket is not changing during the inventory, the application has permission to list every object, and its existing page-token loop works correctly when the field selector is removed. The team wants to preserve the smaller responses rather than return all object metadata. Which change fixes the incomplete inventory while keeping page-by-page processing and returning only the object properties and control information the application actually needs?

**Select one.**

- A. Keep the field selector and increase the requested page size until one response is expected to contain the entire bucket, removing the need for continuation data.
- B. Keep the field selector and derive the next token from the last object name, treating object names as interchangeable with opaque API page tokens.
- C. Request only `nextPageToken`, then make a separate metadata request for every listed object to recover the names and sizes omitted from the list response.
- D. Request `fields=items(name,size),nextPageToken` and keep following returned tokens until none remains, processing each response before fetching the next page.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 9

An application writes customer profile changes to a Cloud SQL for PostgreSQL primary and sends most read traffic to a read replica to reduce primary load. After a successful commit, the application redirects the customer to a confirmation page that occasionally displays the previous profile value. Database logs confirm that the write committed, and a direct read from the primary immediately returns the updated row. Analytics dashboards can tolerate replication lag, but the customer's immediate confirmation must reflect the completed update. The team cannot rely on a fixed sleep because replication lag varies during load spikes. It wants a targeted application-routing change rather than moving all dashboard queries back to the primary or replacing the database. Which read strategy best meets both the immediate confirmation requirement and the existing goal of offloading lag-tolerant workloads?

**Select one.**

- A. Keep the confirmation read on the replica and use a stronger transaction isolation level there, forcing that replica to include every already committed primary transaction.
- B. Route the consistency-sensitive confirmation read to the primary, while retaining replica routing for dashboards and other reads that explicitly tolerate lag.
- C. Keep all reads on the replica and add a constant delay derived from yesterday's average lag, treating the average as an upper bound on future replication delay.
- D. Add another asynchronous read replica and round-robin confirmation requests between them, using the replica count to guarantee that each read observes the last write.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 10

A platform team has already created individual Cloud Workstations for a group of contractors using an approved workstation configuration. Each contractor should start, stop, and connect to only their assigned existing workstation. They must not create additional workstations, change workstation configurations, or grant access to other people. Required network connectivity and organization access are already in place, and each contractor already has the project-level Cloud Workstations Operation Viewer role needed to inspect operations. The team wants to add the narrowest appropriate predefined access on the existing workstation resource rather than grant broad project administration. No custom role is required by organizational policy, and no workstation creation workflow needs to be delegated. Which additional role assignment best enables the requested daily development workflow without introducing the explicitly excluded creation, configuration-management, or access-policy powers?

**Select one.**

- A. Grant Cloud Workstations Creator on the approved workstation configuration, using its creation permissions as the normal way to access the already assigned workstation.
- B. Grant Cloud Workstations Admin on the project, relying on written operating procedures to prevent configuration changes and the creation of additional workstations.
- C. Grant Cloud Workstations User on the contractor's assigned workstation, keeping the existing project-level operation-viewing access.
- D. Grant Cloud Workstations Policy Admin on the assigned workstation, allowing the contractor to modify its access policy instead of directly granting workstation usage permissions.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 11

A Cloud Run job processes a fixed manifest of input records and writes one deterministic output for each record. The team increases the task count from one to twenty and sets parallelism to five to reduce completion time without overwhelming the destination. The application code still reads the entire manifest in every task, so each execution now repeats substantial work. Failed tasks can be retried, including after an output write succeeded but before the task reported success. The manifest is immutable for an execution, records have stable identifiers, and processing does not require ordering between records. The destination supports conditional writes and checking whether an expected output already exists. The team needs all records covered while making retries safe; it does not assume the platform automatically partitions application input. Which TWO application changes satisfy these requirements?

**Select two.**

- A. Use the task index and total task count to assign each manifest record deterministically to one task, keeping the assignment stable across that task's retries.
- B. Divide records using the configured parallelism value as the total number of tasks, allowing every later wave of tasks to reuse the same five partitions.
- C. Disable task retries and continue letting every task process the entire manifest, treating the lack of retries as sufficient to eliminate duplicated work.
- D. Include the retry-attempt number in each output name, ensuring that a retry always produces an additional output instead of checking the result of an earlier attempt.
- E. Make each record's output operation idempotent using its stable identity and conditional creation or equivalent validation of an already completed result.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 12

A supported Java service on GKE experiences rising latency during peak traffic while its containers approach their CPU limits. Existing distributed traces already show that most time is spent inside the service's request handler, with little time in database or downstream RPC spans. Error Reporting shows no new exception pattern, and structured logs identify the affected release but not which methods consume processor time. The team needs evidence about the production code paths responsible before changing the algorithm or purchasing more capacity. It can enable supported low-overhead instrumentation and compare data across representative load periods. Adding a span around every method would require substantial code changes and still primarily measure elapsed time rather than directly attribute sampled CPU consumption. Which next diagnostic action most directly answers the question the team is trying to resolve?

**Select one.**

- A. Collect CPU profiles with Cloud Profiler and inspect the call stacks consuming the most CPU, comparing representative profiles before selecting an optimization.
- B. Increase distributed trace sampling alone and infer which individual methods consume CPU from the same broad request-handler span boundaries.
- C. Create an Error Reporting alert for new exception groups and wait for a stack trace to identify the expensive code path in otherwise successful requests.
- D. Increase each container's CPU limit immediately and treat any latency improvement as sufficient evidence identifying the method that requires optimization.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 13

Two GKE clusters in the same Google Cloud project use Workload Identity Federation for GKE. Both clusters contain a namespace named `payments` and a Kubernetes ServiceAccount named `reader`. A Cloud Storage bucket in a different project grants access directly to the federated principal whose subject ends in `ns/payments/sa/reader` in the clusters' project workload identity pool. No cluster-specific condition is attached to that binding. The security team expected only the production cluster's workload to receive this access, but a workload using the matching namespace and service-account name in the test cluster can also read the bucket. There are no service-account keys or additional bucket grants involved. The test cluster is administered by a less-trusted team. Which explanation and boundary change most directly address the unintended access without incorrectly treating the bucket's project as the source of the workload identity?

**Select one.**

- A. The bucket project combines all external callers into one principal; moving the bucket into the production cluster's project will automatically distinguish the two clusters.
- B. Each cluster has a separate workload identity pool by default; the observed access therefore proves that a long-lived service-account key must have been copied.
- C. Different cluster names always create different name-based principals; restarting the test Pods will invalidate the shared identity and permanently remove access.
- D. Matching name-based subjects in the same project pool can represent the same IAM identity; separate the trust domains into different project pools and retain only the intended grant.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 14

A Python build downloads both private company packages and public dependencies. Developers currently configure pip with a private Artifact Registry endpoint and a public package index as an additional source. A security exercise demonstrates that a public package using an internal package name can be selected unexpectedly when the client considers candidates from both locations. The platform team wants one centrally controlled read endpoint that prefers the private upstream when an internal package is available there, while still allowing approved public dependencies. It can create a standard repository for private packages and a remote repository that proxies the public index. Repository locations and access permissions are already compatible. Which arrangement most directly establishes the desired repository-selection policy without leaving the client free to bypass it by resolving packages directly from the public index?

**Select one.**

- A. Keep both client endpoints and place the private URL first in pip configuration, relying on textual ordering to enforce repository preference for every candidate.
- B. Use a virtual repository with the private upstream at higher priority than the public remote upstream, and configure the client to resolve only through that virtual endpoint.
- C. Use a virtual repository with equal upstream priorities and retain the direct public index as a fallback, allowing the client to choose the latest candidate independently.
- D. Replace the private standard repository with a public remote repository, using its cache to establish which packages were originally authored by the company.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 15

A storefront on GKE serves product pages using a required catalog dependency and an optional recommendations dependency. The business explicitly accepts pages without recommendations, and the application already returns a successful fallback page when that optional service is unavailable. Its current readiness endpoint checks both dependencies, so a recommendations outage removes every storefront Pod from the Service even though catalog access and fallback rendering remain healthy. A separate local liveness check correctly detects a stuck process, and startup handling already prevents traffic before initialization completes. The team needs to preserve useful service during optional dependency failures while still removing a Pod when it cannot serve the required catalog content. It does not want to hide process deadlocks or permanently disable health checking. Which change best aligns probe behavior with the application's actual serving contract?

**Select one.**

- A. Move the recommendations check from readiness into liveness, restarting all storefront containers whenever the optional downstream service becomes unavailable.
- B. Make readiness always succeed after startup, including when the required catalog dependency fails and the application can no longer serve the contracted response.
- C. Base readiness on the ability to serve the required response, including catalog availability; keep optional recommendations failures in fallback logic and retain local liveness checks.
- D. Increase readiness failure thresholds indefinitely while retaining both dependency checks, relying on delayed failure to cover optional and required outages identically.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 16

A Pub/Sub pull subscriber uses a high-level client library and processes messages with a bounded worker pool. During short publishing bursts, it receives substantially more messages than its workers can handle immediately. Outstanding message payloads accumulate in memory, and the process occasionally crashes before completing them. Processing itself is reliable, acknowledgments occur only after successful work, and the application's idempotency mechanism safely handles redelivery. Existing lease management is configured for the normal processing duration. The team can tolerate a temporary subscription backlog and expects its normal processing capacity to catch up after each burst. It wants to stabilize memory use without acknowledging unfinished work or permanently provisioning for the peak arrival rate. Which client-side adjustment most directly controls the amount of received but unfinished work held by each subscriber process?

**Select one.**

- A. Configure subscriber flow-control limits for outstanding message count and bytes in line with worker capacity and memory, allowing excess work to remain in the subscription backlog.
- B. Increase the acknowledgment deadline while leaving received-message buffering unbounded, using a longer processing allowance to cap the memory occupied by queued payloads.
- C. Acknowledge each message immediately when it enters the local worker queue, then rely on process memory to preserve unfinished work across subscriber crashes.
- D. Increase publisher batching size without changing subscriber flow control, assuming larger publishing batches directly enforce the subscriber's memory budget.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 17

A Spanner application stores events in a table whose primary key is a uniformly distributed event identifier. Base-table writes are well distributed, but a secondary index beginning with an increasing event timestamp develops a write hotspot. A reporting operation needs recent events across all customers, so simply removing timestamp access is not acceptable. The team has identified the index as the bottleneck rather than the base table, and additional capacity alone has not addressed the concentrated write pattern. It can modify the index and reporting query, and it accepts a bounded number of parallel range scans followed by a merge into global time order. Each event has a stable identifier suitable for deriving a shard value. Which schema-and-query change best distributes index writes while preserving the required ability to retrieve and order recent events?

**Select one.**

- A. Keep timestamp as the index's leading column and append a shard value after it, relying on the trailing column to distribute the monotonically advancing leading range.
- B. Replace the index with one led by a balanced shard value followed by timestamp, then scan the relevant time range in every shard and merge the results.
- C. Reverse the timestamp ordering in the existing index, keeping timestamp first so new writes concentrate at the opposite end of one advancing key range.
- D. Randomize the already distributed base-table event identifiers again while leaving the timestamp-leading secondary index and reporting query unchanged.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 18

A developer uses Gemini Code Assist to generate Jest unit tests for an asynchronous function that must reject when a downstream request fails. The downstream client is replaced with a deterministic test double, so no live service or unpredictable network timing is involved. The generated test calls the real function inside a try block, awaits it, and checks the error message only inside catch. When a deliberately broken implementation resolves successfully instead of rejecting, the test still passes because the catch block never runs and there is no assertion outside it. Increasing the test timeout does not change the result. The team wants the test to fail reliably for this regression and to verify the expected rejection reason without replacing the function under test with a mock. Which correction most directly closes the missing-assertion path?

**Select one.**

- A. Increase the Jest timeout further and keep the same try/catch test, giving the successful Promise enough time to eventually enter the catch block.
- B. Mock the function under test to reject and keep its downstream client unchanged, proving that the chosen mock behavior matches the asserted error message.
- C. Mark the test callback async and keep assertions only in catch without checking that any assertion ran, relying on the async keyword to reject successful results.
- D. Await an `expect(realFunction()).rejects` assertion matching the required error, so an unexpected resolution fails the test rather than bypassing all assertions.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 19

A GKE Deployment reads non-secret feature settings from a ConfigMap through `envFrom`. The process reads those environment variables during startup and has no runtime reload mechanism. Updating the existing ConfigMap changes the API resource, but running Pods continue using the previous settings. The team needs a controlled release of the new configuration and an explicit way to return to the old configuration without relying on somebody remembering its previous contents. The current application image is unchanged and must remain the same tested digest. The team is willing to replace Pods through a normal Deployment rollout, and both old and new ConfigMaps can be retained. Which deployment approach makes the configuration transition and rollback part of the versioned Pod template rather than assuming that environment variables in existing processes will update automatically?

**Select one.**

- A. Create a separately named ConfigMap containing the new settings, update the Pod template's reference, and roll out; retain the old ConfigMap and template reference for rollback.
- B. Update the same ConfigMap repeatedly and leave the Pod template unchanged, relying on kubelet synchronization to rewrite the environment of every running process.
- C. Mount the same ConfigMap as a directory but leave the application reading only its startup environment variables, avoiding Pod replacement during the change.
- D. Restart Pods after changing the shared ConfigMap, then rely on Deployment rollback alone to recover the previous contents of that same mutable ConfigMap.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

## 20

A web application serves public static assets from Cloud Storage through Cloud CDN. The team overwrites `bundle.js` at the same object path for every release and allows long-lived caching to reduce download latency. After a successful upload, a direct authenticated read of the current object generation returns the new bytes, while some users still receive the previous bundle through the cached delivery path. New HTML is served through a separately controlled path with fresh release references, and the team can change the asset filenames referenced by that HTML. The goal is for each new release page to request its intended bundle while retaining efficient long-lived caching of immutable assets. The team does not require already open pages to replace code they have loaded. Which release design addresses the observed behavior without misdiagnosing it as delayed visibility of the completed Cloud Storage overwrite?

**Select one.**

- A. Keep the shared filename and wait a fixed period for Cloud Storage replicas to converge, treating the direct read's new generation as an early eventually consistent result.
- B. Reduce `Cache-Control` on the overwritten object and assume this immediately replaces all copies that browsers and intermediary caches previously stored with a longer lifetime.
- C. Publish each bundle under a new versioned or content-derived filename and update the fresh HTML to reference it, retaining long cache lifetimes for those immutable asset URLs.
- D. Enable Object Versioning while retaining the identical unqualified asset URL in every release page, relying on historical object generations to select the new bundle in existing caches.

**Cevabım / güven:**

**Kararı belirleyen koşul / bilmediğim kavram:**

---

**Toplam süre / mola / kaynak kullanımı:**

**İki şık arasında kaldığım sorular:**

[Senaryo dizini](README.md) · Cevap anahtarını ilk denemeden sonra aç.
