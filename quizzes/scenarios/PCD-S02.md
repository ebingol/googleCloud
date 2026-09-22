# PCD-S02 — Cloud Run, Cloud Run functions ve GKE

5 Cloud Run + 5 Cloud Run functions + 5 GKE · 15 özgün İngilizce soru · 30 dakika çalışma hedefi · 22 Eylül 2026.

İlk turda kaynakları ve cevap anahtarını kapat. **Select one** bir, **Select two** iki seçenek demektir. Her sorunun altına cevabını, E (emin) / K (kararsız) / T (tahmin) ve kararı belirleyen koşulu bir cümleyle yaz. Gerekçeyi Türkçe yazabilirsin. Çoklu seçimde tam doğru küme 1 puandır; toplam 15 puan.

Dil desteği istersen süreyi durdur; destek alınan soruları ayrıca kaydederiz. Bu kişisel çalışma setidir; gerçek sınav sorusu veya gerçek sınav zorluğuyla kalibre edilmiş deneme değildir.


## 1

A containerized reconciliation program reads a fixed input dataset, produces a report, and exits. Each run takes about 80 minutes. It does not serve HTTP requests, and operators need a separate execution record for each run. Which deployment is the best fit with minimal application changes?

**Select one.**

- A. A Cloud Run service that holds an HTTP request open until the report is complete.
- B. A Cloud Run service that returns immediately and relies on an in-memory background thread to finish the run.
- C. A Cloud Run job with a suitable task timeout, exiting successfully when processing finishes.
- D. A Compute Engine VM that operators create and delete manually for every run.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 2

A payment provider sends an HTTPS webhook and expects your application to return a validation result in the same HTTP response. You want to implement this using Cloud Run functions. Provider signature verification will run in your code. Which handler type fits the interaction?

**Select one.**

- A. An HTTP function that reads the request, validates it, and sends the response.
- B. A Pub/Sub-triggered CloudEvent function whose return value is automatically sent to the original webhook caller.
- C. A Firestore-triggered function that responds directly to the payment provider whenever a document changes.
- D. A scheduled function that periodically checks for requests and holds the provider's original connection.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 3

In a GKE cluster, all application Pods are Ready and labeled app: catalog. A ClusterIP Service uses selector app: catalogue. Its port and targetPort are correct, but it has no backend endpoints. Clients must continue using the existing Service name. What is the smallest appropriate fix?

**Select one.**

- A. Change the Service to type LoadBalancer without changing its selector.
- B. Hard-code the current Pod IP addresses into every client.
- C. Increase the Deployment replica count without changing labels or selectors.
- D. Change the Service selector to app: catalog so it matches the intended Pods.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 4

A Cloud Run container opens its HTTP port immediately, but loading a required lookup table takes another 40 seconds. The default TCP startup check succeeds before the table is ready, and early requests fail. You need the startup check to reflect application initialization. What should you do?

**Select one.**

- A. Increase the request timeout while leaving the TCP startup check unchanged.
- B. Increase minimum instances and assume every newly created instance is initialized.
- C. Add a liveness endpoint that always returns success once the port is open.
- D. Configure an HTTP startup probe whose endpoint succeeds only after the table is loaded, with enough time allowed for initialization.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 5

A Cloud Run function downloads a large image to a unique file under /tmp, creates a thumbnail, and uploads the result to Cloud Storage. Successful uploads are verified. Memory usage rises across invocations on a reused instance, and the temporary files are never removed. Which change directly addresses this growth?

**Select one.**

- A. Increase the function timeout so old files have more time to disappear automatically.
- B. Delete each invocation's temporary files in a cleanup block that also runs on failure, after the files are no longer needed.
- C. Move the files to another directory in the same local temporary filesystem and keep them there.
- D. Store the temporary filenames in a global list and retain every downloaded file for the life of the instance.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 6

A GKE Deployment runs three replicas of image v1. A developer changes one running Pod to use v2, but the Deployment's Pod template still specifies v1. The team needs a controlled rollout in which replacement Pods also use v2. What should it change?

**Select one.**

- A. Only the Service selector, leaving the Deployment's image unchanged.
- B. Only the image of another running Pod, leaving the Deployment template unchanged.
- C. The container image in the Deployment's Pod template, then apply the update and monitor the rollout.
- D. The desired replica count from three to six, leaving the image in the template unchanged.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 7

A Cloud Run service connects to Cloud SQL. Each container process currently creates a new connection pool for every HTTP request. During traffic bursts, database connections accumulate and reach the database limit. Authentication and network connectivity already work. Which TWO changes directly address connection management?

**Select two.**

- A. Increase every pool's connection limit so requests never wait.
- B. Initialize a bounded pool once per process and reuse it across requests.
- C. Always release checked-out connections back to the pool, including when a request fails.
- D. Grant the runtime service account a broader IAM role without changing the code.

**İki cevabım / güven:**

**Kararı belirleyen koşul:**

## 8

An event-driven Cloud Run function has retries enabled. Some events contain an unsupported schema version that retrying cannot fix; other invocations fail because a downstream API is temporarily unavailable. Invalid events must be retained for inspection, and transient failures should still be retried. What should the handler do?

**Select one.**

- A. Durably record invalid events for inspection and finish successfully after recording them; report transient processing failures as failures.
- B. Return success for every failure, including temporary API outages.
- C. Throw an error for every invalid schema event until the retry window expires, without recording it separately.
- D. Disable all retries and keep invalid events only in instance memory.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 9

A single-replica GKE application writes checkpoints to an emptyDir volume. After its Pod is deleted and a replacement Pod is scheduled on another node, the checkpoints are gone. The application must keep those files across Pod replacement. A suitable Persistent Disk CSI StorageClass is available. Which change meets the requirement?

**Select one.**

- A. Increase the emptyDir size limit while continuing to recreate the Pod.
- B. Write the checkpoints into the container's writable layer instead.
- C. Keep emptyDir and assign the Deployment a fixed replica count of one.
- D. Store checkpoints on a persistent volume provisioned through a PVC, and mount the same retained claim in replacement Pods.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 10

A Cloud Run API must accept requests through an external Application Load Balancer, but direct internet requests to its default run.app endpoint must be blocked. The load balancer path and client authentication are already working. IAM authentication must remain required. Which change enforces the network requirement?

**Select one.**

- A. Keep ingress set to all and rely on clients not knowing the run.app URL.
- B. Set ingress to internal only, which also permits any external Application Load Balancer path.
- C. Allow unauthenticated invocations and keep ingress set to all.
- D. Set ingress to internal and Cloud Load Balancing, and retain IAM authentication.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 11

A Python Cloud Run function defines and registers an HTTP handler named process_invoice. The deployment configuration instead sets the function entry point to main, and startup reports that the target cannot be found. The source file and dependencies are present, and the code passes local tests when targeting process_invoice. What should you change?

**Select one.**

- A. Rename the Google Cloud project to process_invoice.
- B. Set the function entry point to process_invoice and redeploy.
- C. Grant the caller Cloud Run Admin while keeping the target main.
- D. Increase the request timeout while keeping the target main.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 12

A GKE Pod sometimes loses access to a required downstream service for a few seconds. The application process remains healthy and can recover without restarting. During the outage, the Pod must stop receiving new traffic from its Kubernetes Service and resume when the dependency recovers. Which configuration best fits?

**Select one.**

- A. Use a liveness probe that fails whenever the dependency is unavailable, restarting the container each time.
- B. Use only a startup probe, which continues checking dependency availability throughout the Pod's life.
- C. Use a readiness probe that fails while the application cannot serve requests; keep liveness focused on failures that require a restart.
- D. Increase the Deployment replica count without configuring application readiness.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 13

A Cloud Run release receives a Secret Manager secret through an environment variable referencing latest. After rotation, newly started instances can receive a different secret value from older instances of that release. Future releases must use a tested secret version consistently, and rolling back must restore the previous release's secret version. Old secret versions will remain enabled and authorized. What should you do?

**Select one.**

- A. Keep latest and increase minimum instances to prevent all future instance replacement.
- B. Keep latest and rebuild the same image whenever the secret changes.
- C. Pin a numeric secret version in each release's configuration and deploy a new revision when adopting another version.
- D. Mount latest as a file and assume a revision fixes the file's secret value permanently.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 14

A Cloud Run function handles Firestore document updates. When a customer's displayName changes, it writes normalizedName and a new processedAt timestamp back to the same document. This write triggers the function again, even though displayName is unchanged. You must continue handling future displayName edits without generating a self-sustaining update loop. What should you do?

**Select one.**

- A. Compare displayName in the before and after snapshots, and return without writing when that input field has not changed.
- B. Switch to a document-created trigger and stop processing all later edits.
- C. Write a fresh processedAt timestamp on every invocation, even when displayName is unchanged.
- D. Increase function memory while keeping the same unconditional write.

**Cevabım / güven:**

**Kararı belirleyen koşul:**

## 15

A GKE Standard Deployment has one container per Pod and an HPA targeting average CPU utilization of 60%. The resource metrics API works, but the HPA cannot calculate CPU utilization because the running containers have no CPU requests configured. Node capacity is available. What should you do first?

**Select one.**

- A. Lower the HPA utilization target while leaving CPU requests unset.
- B. Set appropriate CPU requests in the Deployment's container resource configuration and roll out the updated Pods.
- C. Increase the maximum replica count while leaving CPU requests unset.
- D. Change the Service to type LoadBalancer while leaving resource configuration unchanged.

**Cevabım / güven:**

**Kararı belirleyen koşul:**
---

**Toplam süre:**

**Dil desteği alınan sorular / takıldığım ifadeler:**

Kaydet ve kontrol için “bitti, kaydettim” de. [Cevap anahtarı — yalnız çözümden sonra aç](../answers/scenarios/PCD-S02.md) · [Senaryo dizini](README.md)
