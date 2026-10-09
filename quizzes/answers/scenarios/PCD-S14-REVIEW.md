# PCD-S14 — 20 soru, seçenekler ve açıklamalı cevaplar

9 Ekim 2026. **Anahtarlı tekrar içindir.** Özgün İngilizce sorular ve tüm seçenekler korunmuştur. İlk sonuç **17/20 (%85), 54 dakika**; yanlışlar Q07/Q08/Q19. Q04/Q19 çift seçimdir. Bu tekrar yeni bağımsız sınav puanı veya kalıcılık ölçümü değildir.

Kullanıcı yoğun sorularda bir noktadan sonra konsantrasyonunun yetişmediğini belirtti. Okumayı kolaylaştırmak için dört bölümde beşer soru sunulur; bölümler arasında mola verilebilir, bu anahtarlı turda süre hedefi yoktur. Soru metinleri kısaltılmamıştır.

## Bölüm 1 — Sorular 1–5

### Soru 01

A team is adding document summarization to an existing application on Google Cloud. Evaluation has shown that an available Google publisher Gemini model meets the requirements using ordinary prompts. No custom weights or task-specific training are needed. The team wants to avoid operating model-serving infrastructure while keeping application requests associated with its Google Cloud project. Which implementation should it choose?

**Select ONE answer.**

**A.** Upload the publisher model to a private model registry and deploy a dedicated prediction endpoint before making any request.

**B.** Call the available publisher Gemini model through the Gemini API on Vertex AI using the application project and credentials.

**C.** Create a supervised tuning job for the publisher model and use its output even though the base model already meets the requirements.

**D.** Run the publisher model in a GPU-equipped Cloud Workstation and expose that workstation as the production prediction server.

**Doğru cevap: B**

**Karar:** İhtiyacı hazır model karşılıyor; uygulama API üzerinden publisher modelini çağırır.

**Yakın seçenek / sınır:** A custom model serving akışını hazır publisher çağrısına gereksiz önkoşul yapar.

**Belirleyici İngilizce koşul:** `No custom weights or task-specific training are needed`

**Kaynak:** PDF s.7,10–11; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart)

---

### Soru 02

A developer runs a Gemini integration test inside Cloud Workstations. The process uses ADC, but GOOGLE_APPLICATION_CREDENTIALS points to a valid credential file for a restricted test identity. The developer then creates user ADC with sufficient access and restarts the process without changing its environment. Requests still authenticate as the restricted identity. Network access and API configuration are correct. What should the developer change to make this process use the intended user ADC?

**Select ONE answer.**

**A.** Grant the workstation service agent the developer's project roles while preserving the process environment.

**B.** Change only the active gcloud account because this replaces every credential source used by client libraries.

**C.** Remove the explicit credential-file environment setting from this process so ADC can discover the intended local user credentials.

**D.** Create user ADC again in the same home directory while leaving the explicit credential-file setting in place.

**Doğru cevap: C**

**Karar:** Ortam değişkeniyle belirtilen dosya yerel ADC’den önce gelir.

**Yakın seçenek / sınır:** D aynı düşük öncelikli dosyayı tekrar oluşturur; kaynak seçimi değişmez.

**Belirleyici İngilizce koşul:** `without changing its environment`

**Kaynak:** Ek resmî kaynak; rehber 2.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/docs/authentication/application-default-credentials) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workstations/docs/authentication)

---

### Soru 03

Uploaded images arrive in bursts, and a Cloud Run worker makes one Vision API request per image. Processing can wait in a queue, but operations must independently control the rate of new worker calls and the number of worker calls in progress. Workers are idempotent, complete within the dispatch deadline, and return only after processing. Which configuration provides both controls without building a custom dispatcher?

**Select ONE answer.**

**A.** Put work in Cloud Tasks and configure both maxDispatchesPerSecond and maxConcurrentDispatches for the queue.

**B.** Put work in Cloud Tasks and configure only maxConcurrentDispatches, treating it as a requests-per-second limit.

**C.** Limit Cloud Run concurrency per instance and let the service create any number of instances when bursts arrive.

**D.** Use Eventarc delivery retries as the only mechanism for enforcing both the desired dispatch rate and concurrent-call ceiling.

**Doğru cevap: A**

**Karar:** Tasks kuyruğunda hız ve eşzamanlı dispatch iki ayrı ayardır.

**Yakın seçenek / sınır:** B yalnız aynı anda yürüyen çağrıları sınırlar; saniyelik hız aynı şey değildir. Token-bucket burst davranışı da ayrıca izlenir.

**Belirleyici İngilizce koşul:** `independently control the rate ... and the number ... in progress`

**Kaynak:** Ek resmî kaynak; rehber 1.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/tasks/docs/configuring-queues)

---

### Soru 04

An Eventarc trigger uses event-starter to launch a workflow. The workflow runs as ai-orchestrator and calls a Gemini publisher model. All event-receiver prerequisites, API enablement, billing, network paths, and request formats are correct. Two permission checks fail: event-starter cannot create workflow executions, and ai-orchestrator lacks aiplatform.endpoints.predict. Neither identity needs model administration or broad project access. Which TWO grants address the identified boundaries?

**Select TWO answers.**

**A.** Grant event-starter the model prediction permission and expect the workflow to inherit the event sender's credentials.

**B.** Grant event-starter roles/workflows.invoker on the workflow project.

**C.** Grant ai-orchestrator roles/workflows.invoker and keep event-starter without invocation permission.

**D.** Grant the Eventarc service agent Project Editor so both user-managed identities inherit its permissions.

**E.** Grant ai-orchestrator a narrowly scoped role containing aiplatform.endpoints.predict in the model-call project.

**Doğru cevap: B + E**

**Karar:** Trigger hesabı execution başlatır; workflow hesabı modeli çağırır.

**Yakın seçenek / sınır:** A event kimliğini runtime kimliğiyle karıştırır; C ters hesaba invocation verir.

**Belirleyici İngilizce koşul:** `Two permission checks fail`

**Kaynak:** Ek resmî kaynak; rehber 1.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/eventarc/standard/docs/workflows/roles-permissions) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workflows/docs/authentication) · [Ek resmî kaynak 3](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/access-control)

---

### Soru 05

An inspection application receives a short video and a question about the sequence of actions shown in it. The question cannot be answered reliably from the filename or existing metadata. The team has selected an available Gemini model that supports video input, and the clip meets its documented format and size limits. It wants the model to reason about the actual visual content. Which request design best meets the requirement?

**Select ONE answer.**

**A.** Send only the question and filename, allowing the model to infer the missing visual sequence from its general knowledge.

**B.** Send a single extracted still frame and assume it always preserves the order of actions across the entire video.

**C.** Upload the clip to Cloud Storage but send only the object name as plain text, without a supported media input.

**D.** Send the question together with the video as a supported media part or supported media URI in the multimodal request.

**Doğru cevap: D**

**Karar:** Soruya video içeriği desteklenen media part/URI ile bağlanır.

**Yakın seçenek / sınır:** C düz nesne adı metnini modele video girdisi olarak sağlamaz; B zamansal içeriği kaybedebilir.

**Belirleyici İngilizce koşul:** `sequence of actions shown in it`

**Kaynak:** PDF s.11–16; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/overview)

---

## Bölüm 2 — Sorular 6–10

### Soru 06

A Vision client sends label-detection requests in batches of ten images. The project has a configured request quota of 120 requests per minute and a label-detection feature quota of 600 images per minute. There are no other callers or retries, and all batches contain ten images. The team wants a sustained submission rate that respects both quotas. Which maximum rate follows from these configured values? These are scenario values, not default product quotas.

**Select ONE answer.**

**A.** 120 requests per minute, because each batch consumes only one unit of every quota.

**B.** 600 requests per minute, because feature quota counts batches rather than individual images.

**C.** 60 requests per minute, because each request consumes ten label-detection feature units.

**D.** 12 requests per minute, because the request quota must also be divided by the batch size.

**Doğru cevap: C**

**Karar:** 600 görüntü/dakika ÷ 10 = 60 batch/dakika; request kotası 120.

**Yakın seçenek / sınır:** A request sayısını sayarken feature tüketimini atlar.

**Belirleyici İngilizce koşul:** `all batches contain ten images`

**Kaynak:** Ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vision/quotas)

---

### Soru 07

A Cloud Tasks queue invokes a private Cloud Run image-processing service. The configured task identity is task-caller, and the service runs as image-runtime. All service-agent token-creation permissions and network settings are correct. task-caller already has Cloud Run Invoker on the service. However, tasks send an OAuth access token and the Cloud Run authentication layer rejects them before the handler runs. Which change addresses the invocation failure?

**Select ONE answer.**

**A.** Grant image-runtime Cloud Run Invoker because the server's runtime identity determines which incoming tokens are accepted.

**B.** Configure an OIDC ID token representing task-caller with the destination service URL as its audience.

**C.** Grant task-caller permission to enable the Vision API while keeping the existing access token.

**D.** Set the OAuth access token's audience to the Vision API endpoint and retry the same Cloud Run request.

**Doğru cevap: B**

**İlk cevabın: A**

**Karar:** Cloud Run invocation için hedef audience’lı OIDC ID token kullanılır.

**Yakın seçenek / sınır:** A runtime hesabına izin eklemek yanlış incoming token tipini düzeltmez.

**Belirleyici İngilizce koşul:** `rejects them before the handler runs`

**Kaynak:** Ek resmî kaynak; rehber 1.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks)

---

### Soru 08

An Eventarc Storage object-finalized event starts a document-processing workflow. The event includes the source bucket and object information. The workflow must pass the uploaded document to an OCR worker, but its developer assumes the event body contains the document bytes and forwards that body as a PDF. The worker rejects the input format. Trigger filtering, delivery, and IAM are already correct. What should the workflow and worker do?

**Select ONE answer.**

**A.** Switch to a bucket-creation event so the event body includes all bytes of every object in the bucket.

**B.** Configure Eventarc retries to convert the same metadata payload into a binary document on subsequent deliveries.

**C.** Base64-decode the entire CloudEvent envelope and treat the decoded envelope as the original uploaded document.

**D.** Use the event's object information to identify the input, and have the authorized worker fetch the document from Cloud Storage.

**Doğru cevap: D**

**İlk cevabın: B**

**Karar:** Olay nesneyi tarif eder; worker belgeyi Storage’dan okur.

**Yakın seçenek / sınır:** C CloudEvent envelope’unu decode ederek orijinal belgeyi elde edemez.

**Belirleyici İngilizce koşul:** `assumes the event body contains the document bytes`

**Kaynak:** Ek resmî kaynak; rehber 1.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/eventarc/standard/docs/event-format)

---

### Soru 09

A team repeatedly asks a Gemini model to write short descriptions in a specialized house style. A clear instruction and a few examples already meet the acceptance criteria, and the team has no curated training dataset. It wants to release the feature soon while retaining the ability to revise the style instruction without a training cycle. Which approach best matches the current requirements?

**Select ONE answer.**

**A.** Keep the effective prompt and examples, and evaluate changes before considering tuning if measured needs later justify it.

**B.** Run supervised tuning immediately because every application-specific instruction requires changes to model weights.

**C.** Deploy a dedicated prediction endpoint and treat that deployment alone as training the model in the house style.

**D.** Increase the generation length limit and remove the examples, treating a longer response as evidence of successful customization.

**Doğru cevap: A**

**Karar:** Mevcut prompt başarılı ve dataset yok; tuning zorunlu değildir.

**Yakın seçenek / sınır:** B her uygulama talimatını training ihtiyacı sayar; C deployment ile training’i karıştırır.

**Belirleyici İngilizce koşul:** `already meet the acceptance criteria`

**Kaynak:** PDF s.8 + ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models)

---

### Soru 10

A developer can read source images from a restricted bucket when running the application in Cloud Workstations with personal user ADC. After deployment, the same code runs on Cloud Run as image-runtime and receives a permission denial when reading that bucket. Logs confirm that Cloud Run uses image-runtime; API enablement and network paths are correct. The runtime account has no bucket-read permission. Which change preserves a dedicated production identity and grants only the required data access?

**Select ONE answer.**

**A.** Grant the developer Cloud Run Invoker and assume the developer's bucket permissions apply inside the service.

**B.** Copy the developer's user ADC file into the production container so local and deployed calls share the same credentials.

**C.** Grant image-runtime Storage Object Viewer on the source bucket and keep the service using its attached runtime identity.

**D.** Grant the Cloud Run service agent Storage Object Viewer and leave image-runtime without access to the bucket.

**Doğru cevap: C**

**Karar:** Kaynak bucket erişimi gerçek runtime hesabına verilir.

**Yakın seçenek / sınır:** D platform service agent’ı uygulama runtime’ı yerine koyar.

**Belirleyici İngilizce koşul:** `Logs confirm that Cloud Run uses image-runtime`

**Kaynak:** Ek resmî kaynak; rehber 1.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/run/docs/securing/service-identity) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workstations/docs/authentication)

---

## Bölüm 3 — Sorular 11–15

### Soru 11

A workflow makes two raw HTTP calls: one to the Cloud Storage JSON API at storage.googleapis.com, and one to a private Cloud Run worker. The workflow service account already has the required permissions at both destinations, and network access is correct. Neither call uses a Workflows connector, and no custom Cloud Run audience is configured. Which authentication configuration should the workflow use for these two different targets?

**Select ONE answer.**

**A.** Use OIDC for both calls, with the workflow execution URL as the audience for each.

**B.** Use OAuth2 for both calls because every Google-hosted service accepts the same access token format.

**C.** Use OAuth2 for Cloud Storage and no authentication for Cloud Run because the workflow identity already has Invoker.

**D.** Use OAuth2 for the Cloud Storage API and OIDC with the service URL audience for the Cloud Run worker.

**Doğru cevap: D**

**Karar:** Google API raw HTTP çağrısı OAuth2; Cloud Run çağrısı OIDC.

**Yakın seçenek / sınır:** B access token ile ID token hedeflerini aynılaştırır.

**Belirleyici İngilizce koşul:** `Neither call uses a Workflows connector`

**Kaynak:** Ek resmî kaynak; rehber 4.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/workflows/docs/http-requests) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workflows/docs/authentication)

---

### Soru 12

A supported Vision asynchronous batch request has been accepted, but only part of its image set is currently being processed. Monitoring shows the project's in-processing quota is full; request and feature submission quotas are not exhausted. The remaining images are pending, and the returned operation has not completed. The application has no evidence of an invalid request or failed image. Which response best matches this condition?

**Select ONE answer.**

**A.** Resubmit every pending image immediately with a new request so the service cannot queue it behind the accepted batch.

**B.** Track the accepted operation and allow queued work to progress; assess a quota increase if the required completion time cannot be met.

**C.** Treat request acceptance as proof that all images have already completed and start consuming nonexistent final output.

**D.** Reduce the number of HTTP requests by combining the pending images into a larger request, assuming this removes the in-processing limit.

**Doğru cevap: B**

**Karar:** Kota doluyken fazla async iş sırada kalabilir; kabul edilen operation izlenir.

**Yakın seçenek / sınır:** A gereksiz duplicate submissions oluşturur; D aktif görüntü kotasını kaldırmaz.

**Belirleyici İngilizce koşul:** `in-processing quota is full`

**Kaynak:** Ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vision/quotas) · [Ek resmî kaynak 2](https://docs.cloud.google.com/vision/docs/batch)

---

### Soru 13

A product must produce two kinds of output from uploaded images. One component requires conventional OCR text and coordinates from a pre-trained API. Another component must answer user questions about the meaning of the image and generate explanatory text. Existing evaluations support Vision OCR for the first requirement and a multimodal Gemini model for the second. The team wants to preserve those interfaces rather than train a custom model. Which integration is most appropriate?

**Select ONE answer.**

**A.** Use Gemini Code Assist inside the developer's editor as the production OCR and question-answering endpoint.

**B.** Replace both components with Cloud Storage object metadata because storing an image already exposes its text and meaning.

**C.** Call the Vision OCR API for the required OCR result and the Gemini API with image context for generative answers.

**D.** Route both requests to Cloud Tasks and use the queue itself to extract text and generate explanations.

**Doğru cevap: C**

**Karar:** Önceden eğitilmiş OCR ve generative görsel açıklama ayrı API ihtiyaçlarıdır.

**Yakın seçenek / sınır:** A geliştirici yardımını uygulama inference API’si yerine koyar.

**Belirleyici İngilizce koşul:** `preserve those interfaces rather than train a custom model`

**Kaynak:** PDF s.13,16 + ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vision/docs/ocr) · [Ek resmî kaynak 2](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/overview)

---

### Soru 14

A developer must reproduce a Gemini authorization failure from a workstation using the production service account ai-runtime. Personal user ADC has broader permissions and hides the failure. Downloaded keys are prohibited, and the selected client library supports impersonated local ADC. ai-runtime's resource permissions and the network must remain unchanged during diagnosis. Which setup exercises the intended identity without giving the developer broader data permissions?

**Select ONE answer.**

**A.** Grant the developer ai-runtime's data roles and continue using personal user ADC as evidence of the runtime account's access.

**B.** Grant Service Account User on ai-runtime and assume actAs alone authorizes generation of impersonation access tokens.

**C.** Attach ai-runtime to the production Cloud Run service and assume that this changes the workstation process's ADC identity.

**D.** Grant the developer Service Account Token Creator on ai-runtime and configure supported impersonated ADC for that account.

**Doğru cevap: D**

**Karar:** Desteklenen local ADC impersonation + Token Creator runtime kimliğiyle test sağlar.

**Yakın seçenek / sınır:** B actAs hesabı kaynağa bağlama yetkisidir; tek başına token mint etmez.

**Belirleyici İngilizce koşul:** `resource permissions ... must remain unchanged`

**Kaynak:** Ek resmî kaynak; rehber 2.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workstations/docs/authentication)

---

### Soru 15

A Cloud Tasks worker calls Vision and stores the result durably. A task delivery completes the storage write, but the success response is lost, so the queue later delivers the task again. Each task includes a stable business operation ID, and a durable result record can be checked by that ID. The team wants retries to recover unfinished work without performing another paid API call for an already completed operation. Which worker behavior is most appropriate?

**Select ONE answer.**

**A.** Check the durable completion record before processing, return success for an already completed operation, and otherwise finish and persist the work before acknowledging.

**B.** Return success before calling Vision on every delivery, then run the operation in an untracked background thread.

**C.** Assume task delivery is exactly once and make another Vision call whenever the handler receives the same operation ID.

**D.** Assign a new operation ID to each delivery so the same business job never matches a previous completion record.

**Doğru cevap: A**

**Karar:** Tamamlanmış durable kayıt ikinci API çağrısını atlatır; yeni iş bitmeden ack verilmez.

**Yakın seçenek / sınır:** D business ID’yi delivery’ye göre değiştirerek duplicate korumasını bozar. Eşzamanlı delivery için atomik claim ayrıca gerekir.

**Belirleyici İngilizce koşul:** `success response is lost`

**Kaynak:** Ek resmî kaynak; rehber 1.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/tasks/docs/common-pitfalls)

---

## Bölüm 4 — Sorular 16–20

### Soru 16

A workflow submits a Vision asynchronous operation using a raw HTTP request and receives an operation name. A later Gemini step requires the OCR output, which is written to Cloud Storage only when processing finishes. No connector is waiting on the operation automatically. The workflow currently starts Gemini immediately after submission and sometimes reads missing output. Which change fixes the dependency while avoiding unnecessary duplicate OCR submissions?

**Select ONE answer.**

**A.** Store the operation name, wait or poll its status until successful completion, check errors, and then read the output for the Gemini step.

**B.** Submit the same OCR batch again whenever the output object is not yet present, and use whichever result appears first.

**C.** Treat the successful submission response as the finished OCR result and pass its operation name as the extracted text.

**D.** Increase the Gemini response length limit so Gemini reconstructs the missing OCR output from the operation name.

**Doğru cevap: A**

**Karar:** Raw submission başarı yanıtı işin bitişi değildir; operation ve hata izlenir.

**Yakın seçenek / sınır:** B gecikmeyi submission başarısızlığı sanıp tekrar ücretli iş üretir.

**Belirleyici İngilizce koşul:** `No connector is waiting ... automatically`

**Kaynak:** Ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vision/docs/batch) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workflows/docs/connectors)

---

### Soru 17

An application owner wants customers to request a summary from text already held by the backend. The developers also use an AI assistant in their editor to understand and modify source code. The owner asks whether enabling that editor assistant automatically adds summarization to the deployed product. The backend currently contains no model API call or integration code. Which implementation correctly separates development assistance from the application's runtime capability?

**Select ONE answer.**

**A.** Give customers access to the developers' editor sessions so the existing code assistant becomes the deployed backend API.

**B.** Add a backend Gemini API integration that sends the authorized input and handles the model response; use the editor assistant separately to help develop that code.

**C.** Grant the Cloud Workstations User role to the backend service account so the deployed application automatically gains text summarization.

**D.** Install the editor extension in the container image and assume incoming customer HTTP requests are automatically forwarded to its chat interface.

**Doğru cevap: B**

**Karar:** Ürün özelliği için backend API entegrasyonu yazılır; editor desteği bunu otomatik eklemez.

**Yakın seçenek / sınır:** D extension kurulumunu request handler/inference entegrasyonu yerine koyar.

**Belirleyici İngilizce koşul:** `contains no model API call or integration code`

**Kaynak:** PDF s.1–3,16 + ek resmî kaynak; rehber 2.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart)

---

### Soru 18

An idempotent Vision worker receives a mixture of transient quota-related errors and invalid-image errors. It already uses bounded exponential backoff with jitter for transient failures. A particular object has a permanently invalid image format, and repeated attempts cannot change its bytes. The queue nevertheless keeps retrying it because the handler reports every failure identically. The team needs failed-input visibility without repeatedly spending worker capacity on that object. What should the handler do?

**Select ONE answer.**

**A.** Remove backoff and retry the invalid image immediately until the format becomes acceptable to Vision.

**B.** Return success for every error without retaining any record, so both unfinished transient work and invalid inputs disappear.

**C.** Apply a longer retry delay to every invalid image and leave permanent and transient failures indistinguishable.

**D.** Record the permanent input failure durably and acknowledge that task; keep retryable failures on the retry path.

**Doğru cevap: D**

**Karar:** Kalıcı failure kayıt altına alınır ve task ack edilir; transient işler retry yolunda kalır.

**Yakın seçenek / sınır:** B görünürlüğü ve transient recovery’yi birlikte kaybeder.

**Belirleyici İngilizce koşul:** `repeated attempts cannot change its bytes`

**Kaynak:** Ek resmî kaynak; rehber 1.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/tasks/docs/configuring-queues) · [Ek resmî kaynak 2](https://docs.cloud.google.com/vision/docs/reference/rest/v1/images/annotate)

---

### Soru 19

A Cloud Run service must call a Gemini publisher model through Vertex AI using its attached ai-runtime service account and ADC. Billing, network access, credentials, SDK configuration, and model availability are correct. A review finds two gaps: the required aiplatform.googleapis.com API is disabled in the request project, and ai-runtime lacks the prediction permission. The deployment administrator can enable APIs. Which TWO actions close these gaps without granting runtime administration privileges?

**Select TWO answers.**

**A.** Have the authorized deployment administrator enable aiplatform.googleapis.com in the applicable project.

**B.** Grant ai-runtime only permission to enable APIs and treat this as authorization to invoke the model.

**C.** Grant ai-runtime an appropriately scoped role containing aiplatform.endpoints.predict.

**D.** Grant prediction access to the developer alone and assume those permissions carry over to the attached runtime account.

**E.** Generate a service-account key for ai-runtime and use it as a substitute for API enablement and missing IAM permission.

**Doğru cevap: A + C**

**İlk cevabın: A + B**

**Karar:** API etkinleştirme ve runtime prediction yetkisi iki ayrı eksiktir.

**Yakın seçenek / sınır:** B enable yetkisini data/model işlemiyle karıştırır; D farklı kimliği yetkilendirir.

**Belirleyici İngilizce koşul:** `A review finds two gaps`

**Kaynak:** PDF s.16 başlangıç akışı + ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart) · [Ek resmî kaynak 2](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/access-control) · [Ek resmî kaynak 3](https://docs.cloud.google.com/run/docs/securing/service-identity)

---

### Soru 20

Two independent worker fleets call label detection in the same Vision quota project. Fleet A submits 400 images per minute, and Fleet B submits 300. The configured feature quota is 600 images per minute, and the overall request quota is not the bottleneck. Each fleet stays below 600 when measured alone, but combined traffic is throttled. The project and quota must remain unchanged. Which operational change addresses the shared constraint?

**Select ONE answer.**

**A.** Coordinate a combined image-submission budget within the available project feature quota, buffering excess work and including retry traffic in the budget.

**B.** Assign a different service account to Fleet B so it automatically receives a separate 600-image project feature quota.

**C.** Reduce each fleet's HTTP request count using larger batches while preserving the same combined images-per-minute rate.

**D.** Add more Cloud Run instances to both fleets so the project accepts more feature units without a quota change.

**Doğru cevap: A**

**Karar:** İki fleet aynı feature bütçesini paylaşır; toplam 700 > 600.

**Yakın seçenek / sınır:** B kimlik değişimini yeni project quota sanır; C image tüketimini azaltmaz.

**Belirleyici İngilizce koşul:** `same Vision quota project`

**Kaynak:** Ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vision/quotas) · [Ek resmî kaynak 2](https://docs.cloud.google.com/tasks/docs/configuring-queues)

---
