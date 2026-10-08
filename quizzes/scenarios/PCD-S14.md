# PCD-S14 — Gemini ve Google Cloud API entegrasyonu

**20 soru · 50 dakika kişisel çalışma hedefi · 18 tek seçim + 2 çift seçim**

8 Ekim 2026. Kullanıcının seçtiği Gemini PDF’si ve Google Cloud ekosistemine entegrasyon odağı: IAM/ADC, Workstations, Cloud Tasks, Eventarc, Workflows ve Vision API yük yönetimi. Konular karışık sıradadır. Bu bir konu setidir; tam sınavın dört alan ağırlığı uygulanmaz ve tüm rehber kapsamı örneklenmez.

PDF temelli beş soru ve ek resmî kaynaklı on beş entegrasyon sorusu vardır. PDF temelli sorularda da güncel teknik ayrıntılar resmî belgelerle tamamlanmıştır. Eski Gemini 1.0 Pro/Pro Vision isimleri, PaLM/Codey listesi ve eski SDK örnekleri güncel ürün seçimi olarak ezberletilmez. Sorularda desteklenen ve kullanılabilir model varsayımı açık verilir. Önceki kararların bazıları bilinçli pekiştirmedir; 20 tamamen yeni konu veya gerçek sınavla eşdeğer zorluk iddiası yoktur.

**Çift seçim: Q04 ve Q19.** Diğer sorularda tek seçenek seç. Çift seçimde tam doğru küme 1 puan; kısmi puan yok. İlk turda ayrı anahtarı açma. Yanıtları `1-b, 2-c, 4-b+e` biçiminde ve toplam süreyle gönderebilirsin. Güven/gerekçe isteğe bağlıdır. 50 dakika kişisel hedeftir; ek süre ve yardım kullanımını ayrıca belirt.

Başlangıç: ____ · Bitiş: ____ · Mola: ____ · Ek süre / yardım: ____

## Bölüm 1 — Sorular 1–10

### Question 01

A team is adding document summarization to an existing application on Google Cloud. Evaluation has shown that an available Google publisher Gemini model meets the requirements using ordinary prompts. No custom weights or task-specific training are needed. The team wants to avoid operating model-serving infrastructure while keeping application requests associated with its Google Cloud project. Which implementation should it choose?

**Select ONE answer.**

**A.** Upload the publisher model to a private model registry and deploy a dedicated prediction endpoint before making any request.

**B.** Call the available publisher Gemini model through the Gemini API on Vertex AI using the application project and credentials.

**C.** Create a supervised tuning job for the publisher model and use its output even though the base model already meets the requirements.

**D.** Run the publisher model in a GPU-equipped Cloud Workstation and expose that workstation as the production prediction server.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 02

A developer runs a Gemini integration test inside Cloud Workstations. The process uses ADC, but GOOGLE_APPLICATION_CREDENTIALS points to a valid credential file for a restricted test identity. The developer then creates user ADC with sufficient access and restarts the process without changing its environment. Requests still authenticate as the restricted identity. Network access and API configuration are correct. What should the developer change to make this process use the intended user ADC?

**Select ONE answer.**

**A.** Grant the workstation service agent the developer's project roles while preserving the process environment.

**B.** Change only the active gcloud account because this replaces every credential source used by client libraries.

**C.** Remove the explicit credential-file environment setting from this process so ADC can discover the intended local user credentials.

**D.** Create user ADC again in the same home directory while leaving the explicit credential-file setting in place.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 03

Uploaded images arrive in bursts, and a Cloud Run worker makes one Vision API request per image. Processing can wait in a queue, but operations must independently control the rate of new worker calls and the number of worker calls in progress. Workers are idempotent, complete within the dispatch deadline, and return only after processing. Which configuration provides both controls without building a custom dispatcher?

**Select ONE answer.**

**A.** Put work in Cloud Tasks and configure both maxDispatchesPerSecond and maxConcurrentDispatches for the queue.

**B.** Put work in Cloud Tasks and configure only maxConcurrentDispatches, treating it as a requests-per-second limit.

**C.** Limit Cloud Run concurrency per instance and let the service create any number of instances when bursts arrive.

**D.** Use Eventarc delivery retries as the only mechanism for enforcing both the desired dispatch rate and concurrent-call ceiling.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 04

An Eventarc trigger uses event-starter to launch a workflow. The workflow runs as ai-orchestrator and calls a Gemini publisher model. All event-receiver prerequisites, API enablement, billing, network paths, and request formats are correct. Two permission checks fail: event-starter cannot create workflow executions, and ai-orchestrator lacks aiplatform.endpoints.predict. Neither identity needs model administration or broad project access. Which TWO grants address the identified boundaries?

**Select TWO answers.**

**A.** Grant event-starter the model prediction permission and expect the workflow to inherit the event sender's credentials.

**B.** Grant event-starter roles/workflows.invoker on the workflow project.

**C.** Grant ai-orchestrator roles/workflows.invoker and keep event-starter without invocation permission.

**D.** Grant the Eventarc service agent Project Editor so both user-managed identities inherit its permissions.

**E.** Grant ai-orchestrator a narrowly scoped role containing aiplatform.endpoints.predict in the model-call project.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 05

An inspection application receives a short video and a question about the sequence of actions shown in it. The question cannot be answered reliably from the filename or existing metadata. The team has selected an available Gemini model that supports video input, and the clip meets its documented format and size limits. It wants the model to reason about the actual visual content. Which request design best meets the requirement?

**Select ONE answer.**

**A.** Send only the question and filename, allowing the model to infer the missing visual sequence from its general knowledge.

**B.** Send a single extracted still frame and assume it always preserves the order of actions across the entire video.

**C.** Upload the clip to Cloud Storage but send only the object name as plain text, without a supported media input.

**D.** Send the question together with the video as a supported media part or supported media URI in the multimodal request.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 06

A Vision client sends label-detection requests in batches of ten images. The project has a configured request quota of 120 requests per minute and a label-detection feature quota of 600 images per minute. There are no other callers or retries, and all batches contain ten images. The team wants a sustained submission rate that respects both quotas. Which maximum rate follows from these configured values? These are scenario values, not default product quotas.

**Select ONE answer.**

**A.** 120 requests per minute, because each batch consumes only one unit of every quota.

**B.** 600 requests per minute, because feature quota counts batches rather than individual images.

**C.** 60 requests per minute, because each request consumes ten label-detection feature units.

**D.** 12 requests per minute, because the request quota must also be divided by the batch size.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 07

A Cloud Tasks queue invokes a private Cloud Run image-processing service. The configured task identity is task-caller, and the service runs as image-runtime. All service-agent token-creation permissions and network settings are correct. task-caller already has Cloud Run Invoker on the service. However, tasks send an OAuth access token and the Cloud Run authentication layer rejects them before the handler runs. Which change addresses the invocation failure?

**Select ONE answer.**

**A.** Grant image-runtime Cloud Run Invoker because the server's runtime identity determines which incoming tokens are accepted.

**B.** Configure an OIDC ID token representing task-caller with the destination service URL as its audience.

**C.** Grant task-caller permission to enable the Vision API while keeping the existing access token.

**D.** Set the OAuth access token's audience to the Vision API endpoint and retry the same Cloud Run request.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 08

An Eventarc Storage object-finalized event starts a document-processing workflow. The event includes the source bucket and object information. The workflow must pass the uploaded document to an OCR worker, but its developer assumes the event body contains the document bytes and forwards that body as a PDF. The worker rejects the input format. Trigger filtering, delivery, and IAM are already correct. What should the workflow and worker do?

**Select ONE answer.**

**A.** Switch to a bucket-creation event so the event body includes all bytes of every object in the bucket.

**B.** Configure Eventarc retries to convert the same metadata payload into a binary document on subsequent deliveries.

**C.** Base64-decode the entire CloudEvent envelope and treat the decoded envelope as the original uploaded document.

**D.** Use the event's object information to identify the input, and have the authorized worker fetch the document from Cloud Storage.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 09

A team repeatedly asks a Gemini model to write short descriptions in a specialized house style. A clear instruction and a few examples already meet the acceptance criteria, and the team has no curated training dataset. It wants to release the feature soon while retaining the ability to revise the style instruction without a training cycle. Which approach best matches the current requirements?

**Select ONE answer.**

**A.** Keep the effective prompt and examples, and evaluate changes before considering tuning if measured needs later justify it.

**B.** Run supervised tuning immediately because every application-specific instruction requires changes to model weights.

**C.** Deploy a dedicated prediction endpoint and treat that deployment alone as training the model in the house style.

**D.** Increase the generation length limit and remove the examples, treating a longer response as evidence of successful customization.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 10

A developer can read source images from a restricted bucket when running the application in Cloud Workstations with personal user ADC. After deployment, the same code runs on Cloud Run as image-runtime and receives a permission denial when reading that bucket. Logs confirm that Cloud Run uses image-runtime; API enablement and network paths are correct. The runtime account has no bucket-read permission. Which change preserves a dedicated production identity and grants only the required data access?

**Select ONE answer.**

**A.** Grant the developer Cloud Run Invoker and assume the developer's bucket permissions apply inside the service.

**B.** Copy the developer's user ADC file into the production container so local and deployed calls share the same credentials.

**C.** Grant image-runtime Storage Object Viewer on the source bucket and keep the service using its attached runtime identity.

**D.** Grant the Cloud Run service agent Storage Object Viewer and leave image-runtime without access to the bucket.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

## Bölüm 2 — Sorular 11–20

### Question 11

A workflow makes two raw HTTP calls: one to the Cloud Storage JSON API at storage.googleapis.com, and one to a private Cloud Run worker. The workflow service account already has the required permissions at both destinations, and network access is correct. Neither call uses a Workflows connector, and no custom Cloud Run audience is configured. Which authentication configuration should the workflow use for these two different targets?

**Select ONE answer.**

**A.** Use OIDC for both calls, with the workflow execution URL as the audience for each.

**B.** Use OAuth2 for both calls because every Google-hosted service accepts the same access token format.

**C.** Use OAuth2 for Cloud Storage and no authentication for Cloud Run because the workflow identity already has Invoker.

**D.** Use OAuth2 for the Cloud Storage API and OIDC with the service URL audience for the Cloud Run worker.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 12

A supported Vision asynchronous batch request has been accepted, but only part of its image set is currently being processed. Monitoring shows the project's in-processing quota is full; request and feature submission quotas are not exhausted. The remaining images are pending, and the returned operation has not completed. The application has no evidence of an invalid request or failed image. Which response best matches this condition?

**Select ONE answer.**

**A.** Resubmit every pending image immediately with a new request so the service cannot queue it behind the accepted batch.

**B.** Track the accepted operation and allow queued work to progress; assess a quota increase if the required completion time cannot be met.

**C.** Treat request acceptance as proof that all images have already completed and start consuming nonexistent final output.

**D.** Reduce the number of HTTP requests by combining the pending images into a larger request, assuming this removes the in-processing limit.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 13

A product must produce two kinds of output from uploaded images. One component requires conventional OCR text and coordinates from a pre-trained API. Another component must answer user questions about the meaning of the image and generate explanatory text. Existing evaluations support Vision OCR for the first requirement and a multimodal Gemini model for the second. The team wants to preserve those interfaces rather than train a custom model. Which integration is most appropriate?

**Select ONE answer.**

**A.** Use Gemini Code Assist inside the developer's editor as the production OCR and question-answering endpoint.

**B.** Replace both components with Cloud Storage object metadata because storing an image already exposes its text and meaning.

**C.** Call the Vision OCR API for the required OCR result and the Gemini API with image context for generative answers.

**D.** Route both requests to Cloud Tasks and use the queue itself to extract text and generate explanations.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 14

A developer must reproduce a Gemini authorization failure from a workstation using the production service account ai-runtime. Personal user ADC has broader permissions and hides the failure. Downloaded keys are prohibited, and the selected client library supports impersonated local ADC. ai-runtime's resource permissions and the network must remain unchanged during diagnosis. Which setup exercises the intended identity without giving the developer broader data permissions?

**Select ONE answer.**

**A.** Grant the developer ai-runtime's data roles and continue using personal user ADC as evidence of the runtime account's access.

**B.** Grant Service Account User on ai-runtime and assume actAs alone authorizes generation of impersonation access tokens.

**C.** Attach ai-runtime to the production Cloud Run service and assume that this changes the workstation process's ADC identity.

**D.** Grant the developer Service Account Token Creator on ai-runtime and configure supported impersonated ADC for that account.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 15

A Cloud Tasks worker calls Vision and stores the result durably. A task delivery completes the storage write, but the success response is lost, so the queue later delivers the task again. Each task includes a stable business operation ID, and a durable result record can be checked by that ID. The team wants retries to recover unfinished work without performing another paid API call for an already completed operation. Which worker behavior is most appropriate?

**Select ONE answer.**

**A.** Check the durable completion record before processing, return success for an already completed operation, and otherwise finish and persist the work before acknowledging.

**B.** Return success before calling Vision on every delivery, then run the operation in an untracked background thread.

**C.** Assume task delivery is exactly once and make another Vision call whenever the handler receives the same operation ID.

**D.** Assign a new operation ID to each delivery so the same business job never matches a previous completion record.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 16

A workflow submits a Vision asynchronous operation using a raw HTTP request and receives an operation name. A later Gemini step requires the OCR output, which is written to Cloud Storage only when processing finishes. No connector is waiting on the operation automatically. The workflow currently starts Gemini immediately after submission and sometimes reads missing output. Which change fixes the dependency while avoiding unnecessary duplicate OCR submissions?

**Select ONE answer.**

**A.** Store the operation name, wait or poll its status until successful completion, check errors, and then read the output for the Gemini step.

**B.** Submit the same OCR batch again whenever the output object is not yet present, and use whichever result appears first.

**C.** Treat the successful submission response as the finished OCR result and pass its operation name as the extracted text.

**D.** Increase the Gemini response length limit so Gemini reconstructs the missing OCR output from the operation name.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 17

An application owner wants customers to request a summary from text already held by the backend. The developers also use an AI assistant in their editor to understand and modify source code. The owner asks whether enabling that editor assistant automatically adds summarization to the deployed product. The backend currently contains no model API call or integration code. Which implementation correctly separates development assistance from the application's runtime capability?

**Select ONE answer.**

**A.** Give customers access to the developers' editor sessions so the existing code assistant becomes the deployed backend API.

**B.** Add a backend Gemini API integration that sends the authorized input and handles the model response; use the editor assistant separately to help develop that code.

**C.** Grant the Cloud Workstations User role to the backend service account so the deployed application automatically gains text summarization.

**D.** Install the editor extension in the container image and assume incoming customer HTTP requests are automatically forwarded to its chat interface.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 18

An idempotent Vision worker receives a mixture of transient quota-related errors and invalid-image errors. It already uses bounded exponential backoff with jitter for transient failures. A particular object has a permanently invalid image format, and repeated attempts cannot change its bytes. The queue nevertheless keeps retrying it because the handler reports every failure identically. The team needs failed-input visibility without repeatedly spending worker capacity on that object. What should the handler do?

**Select ONE answer.**

**A.** Remove backoff and retry the invalid image immediately until the format becomes acceptable to Vision.

**B.** Return success for every error without retaining any record, so both unfinished transient work and invalid inputs disappear.

**C.** Apply a longer retry delay to every invalid image and leave permanent and transient failures indistinguishable.

**D.** Record the permanent input failure durably and acknowledge that task; keep retryable failures on the retry path.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 19

A Cloud Run service must call a Gemini publisher model through Vertex AI using its attached ai-runtime service account and ADC. Billing, network access, credentials, SDK configuration, and model availability are correct. A review finds two gaps: the required aiplatform.googleapis.com API is disabled in the request project, and ai-runtime lacks the prediction permission. The deployment administrator can enable APIs. Which TWO actions close these gaps without granting runtime administration privileges?

**Select TWO answers.**

**A.** Have the authorized deployment administrator enable aiplatform.googleapis.com in the applicable project.

**B.** Grant ai-runtime only permission to enable APIs and treat this as authorization to invoke the model.

**C.** Grant ai-runtime an appropriately scoped role containing aiplatform.endpoints.predict.

**D.** Grant prediction access to the developer alone and assume those permissions carry over to the attached runtime account.

**E.** Generate a service-account key for ai-runtime and use it as a substitute for API enablement and missing IAM permission.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---

### Question 20

Two independent worker fleets call label detection in the same Vision quota project. Fleet A submits 400 images per minute, and Fleet B submits 300. The configured feature quota is 600 images per minute, and the overall request quota is not the bottleneck. Each fleet stays below 600 when measured alone, but combined traffic is throttled. The project and quota must remain unchanged. Which operational change addresses the shared constraint?

**Select ONE answer.**

**A.** Coordinate a combined image-submission budget within the available project feature quota, buffering excess work and including retry traffic in the budget.

**B.** Assign a different service account to Fleet B so it automatically receives a separate 600-image project feature quota.

**C.** Reduce each fleet's HTTP request count using larger batches while preserving the same combined images-per-minute rate.

**D.** Add more Cloud Run instances to both fleets so the project accepts more feature units without a quota change.

Cevabım: ___ · Güven (E/K/T, isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram (isteğe bağlı): ___

---
