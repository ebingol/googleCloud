# PCD-S03 — Çok koşullu karma senaryolar

23 Eylül 2026 · 15 İngilizce soru · Cloud Run, Cloud Run functions ve GKE’den 5’er soru, karışık sırada.

**Süre hedefi: 30 dakika.** Bu kişisel çalışma hedefidir. Sorular özgündür; gerçek sınavdan alınmamıştır ve gerçek sınav zorluğuyla kalibre edilmemiştir. Bazı ayrıntılar ders PDF’lerine ek resmî dokümanlardan gelir; kaynaklar ayrı anahtardadır.

İlk turda kaynakları ve cevap anahtarını açma. Her soruya cevap, **E** (emin) / **K** (kararsız) / **T** (tahmin) ve kararı belirleyen koşulu tek cümleyle yaz. `Select two` için tam iki seçenek gerekir; tam doğru küme 1 puandır. Dil desteği alırsan süreyi durdur ve soru numarasını aşağıya kaydet.

## 1

A GKE application reads a non-secret routing file afresh before handling each request. The file comes from a ConfigMap and is mounted as a single file using subPath. Operators update the ConfigMap, but existing Pods keep reading the old content even after several kubelet synchronization cycles. The application can tolerate the normal projection delay, but routine routing changes must not require a Pod restart. The team can move the file into a dedicated directory that contains no application assets. Which change best meets the requirement?

**Select one.**

- A. Keep the subPath mount and increase the time between application reads so the kubelet can replace the mounted file.
- B. Mount the ConfigMap as a directory without subPath, configure the application to read the file there, and allow for eventual projection updates.
- C. Populate an environment variable from the ConfigMap and have the running process reread that environment variable for every request.
- D. Retain the subPath mount and perform a rolling restart whenever the ConfigMap content changes.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 2

A release-validation service must send authenticated requests directly to the candidate revision of a private Cloud Run service without changing its production traffic split. The candidate already has a traffic tag, the validator's runtime service account already has Cloud Run Invoker on the receiving service, and ingress permits the call. No custom audiences are configured. Which pairing of request destination and Google-signed ID-token audience should the validator use?

**Select one.**

- A. Send to the receiving service’s ordinary URL; set the audience to the candidate’s tag URL.
- B. Send to the candidate’s tag URL; set the audience to that same tag URL.
- C. Send to the receiving service’s ordinary URL; set the audience to that same ordinary URL.
- D. Send to the candidate’s tag URL; set the audience to the receiving service’s ordinary URL.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 3

A Node.js Cloud Run function processes a Pub/Sub event and starts an asynchronous upload to Cloud Storage. The event handler currently returns immediately after starting the upload, and some invocations are reported as successful even though no output object appears. The upload returns a Promise, normally completes well within the configured timeout, and is already safe to repeat. Retries are enabled. You need the invocation result to reflect the actual upload outcome while preserving retries for transient failures. What should you change?

**Select one.**

- A. Await or return the upload Promise, and allow an upload rejection to propagate as an invocation failure.
- B. Increase the timeout and keep returning immediately, allowing the outstanding Promise to run during the extra time.
- C. Await the upload Promise, catch every rejection, log it, and return successfully so the platform can retry from the log entry.
- D. Keep returning immediately and increase minimum instances so the same process can finish the upload after completion is reported.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 4

Two GKE workloads share a node pool, but only the reporting workload may read objects from a particular Cloud Storage bucket. Workload Identity Federation for GKE is enabled on the cluster and its relevant node pool, and direct federated access is supported for this operation. Downloaded keys are prohibited. The reporting Pods currently use the same Kubernetes ServiceAccount as the unrelated workload. Which TWO changes establish the intended workload-level access boundary without granting bucket access to the whole node pool?

**Select two.**

- A. Grant Storage Object Viewer on the bucket to the node service account used by the shared node pool.
- B. Grant Storage Object Viewer on the project to the existing shared Kubernetes ServiceAccount principal.
- C. Create a dedicated Kubernetes ServiceAccount for reporting and set the reporting Pod template to use it.
- D. Grant Storage Object Viewer on the specific bucket to the federated principal corresponding to that dedicated Kubernetes ServiceAccount.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 5

A Cloud Storage-triggered Cloud Run function processes each uploaded version of a daily data file. Producers intentionally reuse the same object name, and Object Versioning retains all relevant noncurrent generations until processing finishes. When delivery is delayed, the handler sometimes processes the newest file while recording the result against an older event. It currently downloads by bucket and object name only. Event deduplication already works. Which change ensures that each event is processed against the correct bytes?

**Select one.**

- A. Keep downloading by name, but use the event ID as the output filename so different events cannot overwrite each other’s results.
- B. Download the object using the bucket, object name, and generation from the event, and retain that generation in the processing record.
- C. Read the current object metadata first, then download the generation reported by that metadata instead of the event.
- D. Set the function concurrency to one so delayed events automatically retrieve the object version that existed when they were generated.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 6

A Cloud Run service uses two containers in each instance: an HTTP reverse proxy designated as the ingress container, and an application container serving only the proxy. The configured ingress port is 8080. The application listens on 127.0.0.1:9000, while the proxy listens on 127.0.0.1:8080 and forwards to localhost:9000. Both processes start successfully and the application endpoint works from inside the instance, but external requests cannot reach the service. Which networking change is appropriate while keeping the application behind the proxy?

**Select one.**

- A. Configure the application as the ingress container on port 9000, keeping both listeners bound only to 127.0.0.1.
- B. Keep the proxy unchanged and configure Direct VPC egress so Cloud Run can reach its loopback listener.
- C. Bind the proxy to 0.0.0.0:8080 and retain the internal proxy-to-application connection on localhost:9000.
- D. Bind the application to 0.0.0.0:8080 and keep the proxy on 127.0.0.1:8080 so both containers receive incoming requests.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 7

A three-replica GKE application needs at least two healthy replicas to provide its required capacity. All three replicas are currently healthy, and sufficient spare capacity exists to place replacements. During planned maintenance, operators drain nodes using the Kubernetes eviction API and are willing to wait for replacement Pods to become healthy before continuing. You need to constrain these voluntary evictions without permanently blocking the first eviction. Which configuration most directly expresses this requirement?

**Select one.**

- A. A PodDisruptionBudget selecting the application Pods with minAvailable set to 2.
- B. A PodDisruptionBudget selecting the application Pods with minAvailable set to 3.
- C. A Deployment rolling-update strategy with maxUnavailable set to 1, without a PodDisruptionBudget.
- D. An HPA with minReplicas set to 2 and maxReplicas set to 3, without a PodDisruptionBudget.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 8

A Cloud Run service needs four vCPUs to obtain its required memory allocation, but its CPU-intensive request handler is effectively single-threaded. Load tests show one core saturated, low average CPU utilization across the instance, and requests waiting behind each other when concurrency is high. The code is safe under concurrent calls, so correctness is not the issue. The instance limit has headroom, and you accept more instances to reduce latency. Which change should you test first while retaining the current CPU and memory allocation?

**Select one.**

- A. Increase the maximum instance limit further while keeping the same per-instance concurrency.
- B. Enable session affinity while keeping the same per-instance concurrency.
- C. Increase per-instance concurrency so the spare cores can automatically execute the single-threaded handler in parallel.
- D. Lower per-instance concurrency and load-test whether request-driven scaling reduces waiting time.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 9

A Cloud Run function maintains a Firestore summary document from changes to a separate source document. Each source change includes a strictly increasing application version and a complete replacement snapshot. Events can arrive out of order or more than once, and function invocations can overlap. Intermediate versions may be skipped, but an older version must never overwrite a newer summary. The summary stores its applied version. Which design meets the requirement even if two handlers race?

**Select one.**

- A. Deduplicate only by event ID, then unconditionally overwrite the summary for every previously unseen event.
- B. Read the applied version, compare it with the event version, and write the new summary in a separate operation if the event is newer.
- C. Use a Firestore transaction to compare versions and atomically replace the summary and applied version only when the incoming version is newer.
- D. Set concurrency and maximum instances to one, then overwrite the summary for each event in arrival order.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 10

A GKE cluster enforces Kubernetes NetworkPolicies. A frontend Pod connects to a backend Pod in the same namespace on TCP port 8443. The frontend is selected by a default-deny egress policy, and the backend is selected by a default-deny ingress policy. DNS resolution already succeeds through a separate allow rule. There are no other rules allowing the application connection. You must enable only the intended frontend-to-backend path while preserving both isolation policies. Which TWO additions are required?

**Select two.**

- A. Add an egress allowance selecting the frontend Pods, permitting connections to backend Pods on TCP 8443.
- B. Add an ingress allowance selecting the backend Pods, permitting connections from frontend Pods on TCP 8443.
- C. Add an ingress allowance selecting the frontend Pods, permitting connections from backend Pods on TCP 8443.
- D. Add an egress allowance selecting the backend Pods, permitting connections to frontend Pods on TCP 8443.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 11

A Cloud Run service executes a database operation that normally takes 70 seconds, but its request timeout is configured to 60 seconds. The caller receives a 504 response at approximately 60 seconds and immediately submits the operation again. Logs sometimes show the original operation committing after the caller has received the error. The team proposes treating every Cloud Run 504 as proof that the original operation was cancelled and rolled back. Which assessment should guide the fix?

**Select one.**

- A. The assessment is correct; the later commit must belong to the retried request because Cloud Run terminates the original container at the request deadline.
- B. The assessment is incorrect; the request can time out while its code continues, so retries need a durable operation identity and the timeout policy should match expected processing time.
- C. The assessment is correct if concurrency is set to one, because that setting causes the original operation to be rolled back before another request starts.
- D. The assessment is incorrect only when session affinity is disabled; enabling it makes retrying after a 504 safe without changes to operation handling.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 12

A team deploys a Cloud Run function from source with a dedicated build service account and a different runtime service account. The build fails with a permission error before any new revision is created. Audit logs identify the build account as the denied principal, and the platform team confirms that it lacks the documented Cloud Run Builder role for this source-deployment workflow. Deployer permissions are already correct. The runtime account has narrowly scoped production-data permissions that the build must not inherit. What should you do?

**Select one.**

- A. Grant Cloud Run Builder to the runtime account and keep the build configured to use its current account.
- B. Grant Cloud Run Invoker to the build account on the intended function, leaving its build permissions unchanged.
- C. Configure the build to use the production runtime account and grant that account Cloud Run Builder.
- D. Grant Cloud Run Builder to the configured build account on the build project, keeping the runtime identity separate.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 13

A new GKE Standard Pod remains Pending with an Insufficient cpu scheduling event. It has one container requesting 2000 millicores and limiting CPU to 2000 millicores. Every eligible node has only 1500 millicores of allocatable CPU left after existing requests are accounted for, even though current measured CPU use is low. Cluster autoscaling is disabled, and load testing confirms that the new workload genuinely needs its 2000-millicore reservation. Which action addresses the scheduling constraint without weakening that reservation?

**Select one.**

- A. Add or resize eligible node capacity so at least one eligible node can accommodate the full 2000-millicore request.
- B. Lower the CPU limit to 1500 millicores while retaining the 2000-millicore request.
- C. Increase the HPA maximum replica count so several Pending replicas can divide the original Pod’s CPU request.
- D. Keep the cluster unchanged and wait for measured CPU utilization to drop below 20%, allowing the scheduler to ignore reserved requests.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 14

A Python Cloud Run function is registered as a CloudEvent handler for Pub/Sub messages. A local unit test passes a dictionary containing orderId directly to the business-logic helper, and the helper succeeds. In deployment, the adapter instead looks for orderId directly under cloud_event.data and fails, although the publisher sends valid UTF-8 JSON as the Pub/Sub message bytes. You want the local adapter test to exercise the same payload transformation as production. Which change is appropriate?

**Select one.**

- A. Keep reading cloud_event.data as the order dictionary and change the unit test to include a CloudEvent ID only.
- B. Parse the Pub/Sub message ID as JSON and use the event data only to distinguish retry attempts.
- C. Test with a Pub/Sub CloudEvent envelope, extract its message.data field, base64-decode it, decode the bytes as UTF-8, and then parse the order JSON.
- D. Change the function to an HTTP handler that expects raw order JSON while leaving the Eventarc Pub/Sub delivery configuration unchanged.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 15

A Cloud Run service calls a supplier’s public IPv4 API, which accepts requests only from one allowlisted source IP. The service already uses Direct VPC egress for private destinations, with private-ranges-only selected. A correctly configured Cloud NAT gateway covers the selected subnet and uses a reserved static external IPv4 address, but the supplier still observes other source addresses. The supplier hostname resolves to a public IPv4 address, and outbound firewall rules permit the call. Which change completes the intended egress path?

**Select one.**

- A. Attach the reserved address to an external Application Load Balancer in front of Cloud Run and keep private-ranges-only egress.
- B. Change Cloud Run VPC egress to all-traffic so the supplier requests traverse the configured VPC and Cloud NAT.
- C. Set Cloud Run ingress to internal and Cloud Load Balancing while keeping private-ranges-only egress.
- D. Keep private-ranges-only and raise minimum instances so the service retains the same external source IP indefinitely.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

---

**Toplam süre:**

**Dil desteği alınan sorular / takıldığım ifadeler:**

Kaydedince “bitti, kaydettim” de. [Cevap anahtarı — yalnız çözümden sonra aç](../answers/scenarios/PCD-S03.md) · [Senaryo dizini](README.md)
