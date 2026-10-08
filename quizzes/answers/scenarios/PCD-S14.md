# PCD-S14 — Ayrı Türkçe cevap anahtarı

8 Ekim 2026. İlk tur bitmeden açma. Hazırlık tamamlandı; kullanıcı cevabı, süre veya puan henüz yok. Rehberli çözüm ilk sonuçtan ayrı kaydedilir.

## Kaynak ve kapsam

Ana ders belgesi: `T-GEMPRO-B-m2-l1-en-file-5.en.pdf`, 19 sayfa, “Integrating Applications with Gemini 1.0 Pro on Google Cloud”; kullanıcı tarafından `/Users/ezgi-lab/Desktop/` konumundan paylaşıldı. Kaynak PDF repoya kopyalanmadı. Q01/Q05/Q09/Q13/Q17 bu belgenin temel kararlarını kullanır; diğer 15 soru kullanıcının istediği ek resmî entegrasyon kapsamıdır. Güncel kaynaklar 8 Ekim’de kontrol edildi. Bazı Vertex AI GenAI belge adresleri güncel Google belge yapısına yönlenir; set, exam guide ve dersin Vertex AI/Gemini API terminolojisini kullanır. Güncel model/SDK sürümü ezberi ölçülmez.

[Resmî sınav rehberi](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf). Eşlemeler öğrenme amaçlıdır; setin rehber maddelerini eksiksiz temsil ettiği anlamına gelmez.

| Küme | Sorular | Doğrudan ölçülen karar |
|---|---|---|
| Gemini/PDF temeli | 1, 5, 9, 13, 17 | Publisher inference, multimodal input, prompt/tuning, OCR/GenAI ve editor/runtime ayrımı |
| Kimlik ve IAM | 2, 4, 7, 10, 11, 14, 19 | ADC kaynağı, trigger/runtime, token tipi, kullanıcı/runtime, impersonation, API enablement |
| Kuyruk ve güvenilir işlem | 3, 15, 18 | Dispatch hızı/eşzamanlılık, duplicate delivery, kalıcı/transient hata |
| Olay ve orkestrasyon | 8, 16 | Event metadata ile nesne bytes ayrımı, LRO tamamlanma bağımlılığı |
| Vision yük yönetimi | 6, 12, 20 | Request/feature sayımı, in-processing backlog, ortak proje bütçesi |

Ölçülmeyen örnekler: Gemini tuning uygulama adımları, RAG/vector search, tüm model aileleri, model fiyatları/sayısal varsayılan kotalar, Code Assist lisans kurulumu, VPC Service Controls ve ağ topolojisi. Cloud lab çalıştırılmadı; belgeye dayalı soru/anahtar doğrulaması yapıldı. Kullanıcının adaydan aktardığı “12 soru” bilgisi doğrulanmış sınav dağılımı sayılmaz.

## Hızlı anahtar

1: B · 2: C · 3: A · 4: B+E · 5: D · 6: C · 7: B · 8: D · 9: A · 10: C · 11: D · 12: B · 13: C · 14: D · 15: A · 16: A · 17: B · 18: D · 19: A+C · 20: A

## Q01 — B

**Karar:** İhtiyacı hazır model karşılıyor; uygulama API üzerinden publisher modelini çağırır.

**Yakın seçenek / sınır:** A custom model serving akışını hazır publisher çağrısına gereksiz önkoşul yapar.

**Belirleyici İngilizce koşul:** `No custom weights or task-specific training are needed`

**Doğru seçenek metni:** Call the available publisher Gemini model through the Gemini API on Vertex AI using the application project and credentials.

**Kaynak:** PDF s.7,10–11; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart)

**Önceki ilişki:** Yeni ölçüm; S08-48 çıktı doğrulamasından farklı publisher/serving kararı.

## Q02 — C

**Karar:** Ortam değişkeniyle belirtilen dosya yerel ADC’den önce gelir.

**Yakın seçenek / sınır:** D aynı düşük öncelikli dosyayı tekrar oluşturur; kaynak seçimi değişmez.

**Belirleyici İngilizce koşul:** `without changing its environment`

**Doğru seçenek metni:** Remove the explicit credential-file environment setting from this process so ADC can discover the intended local user credentials.

**Kaynak:** Ek resmî kaynak; rehber 2.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/docs/authentication/application-default-credentials) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workstations/docs/authentication)

**Önceki ilişki:** Bilinçli pekiştirme; S06-02 environment precedence, Workstations uygulaması.

## Q03 — A

**Karar:** Tasks kuyruğunda hız ve eşzamanlı dispatch iki ayrı ayardır.

**Yakın seçenek / sınır:** B yalnız aynı anda yürüyen çağrıları sınırlar; saniyelik hız aynı şey değildir. Token-bucket burst davranışı da ayrıca izlenir.

**Belirleyici İngilizce koşul:** `independently control the rate ... and the number ... in progress`

**Doğru seçenek metni:** Put work in Cloud Tasks and configure both maxDispatchesPerSecond and maxConcurrentDispatches for the queue.

**Kaynak:** Ek resmî kaynak; rehber 1.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/tasks/docs/configuring-queues)

**Önceki ilişki:** Bilinçli pekiştirme; S06-01 / S11-28. Tek Vision worker’da iki kontrol ayrımı.

## Q04 — B + E

**Karar:** Trigger hesabı execution başlatır; workflow hesabı modeli çağırır.

**Yakın seçenek / sınır:** A event kimliğini runtime kimliğiyle karıştırır; C ters hesaba invocation verir.

**Belirleyici İngilizce koşul:** `Two permission checks fail`

**Doğru seçenek metni:** Grant event-starter roles/workflows.invoker on the workflow project. / Grant ai-orchestrator a narrowly scoped role containing aiplatform.endpoints.predict in the model-call project.

**Kaynak:** Ek resmî kaynak; rehber 1.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/eventarc/standard/docs/workflows/roles-permissions) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workflows/docs/authentication) · [Ek resmî kaynak 3](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/access-control)

**Önceki ilişki:** Karma; S11-19 iki IAM sınırı; burada Workflows execution ve Gemini prediction.

## Q05 — D

**Karar:** Soruya video içeriği desteklenen media part/URI ile bağlanır.

**Yakın seçenek / sınır:** C düz nesne adı metnini modele video girdisi olarak sağlamaz; B zamansal içeriği kaybedebilir.

**Belirleyici İngilizce koşul:** `sequence of actions shown in it`

**Doğru seçenek metni:** Send the question together with the video as a supported media part or supported media URI in the multimodal request.

**Kaynak:** PDF s.11–16; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/overview)

**Önceki ilişki:** Yeni ölçüm; multimodal input bağlama, eski Pro Vision adını ezberleme yok.

## Q06 — C

**Karar:** 600 görüntü/dakika ÷ 10 = 60 batch/dakika; request kotası 120.

**Yakın seçenek / sınır:** A request sayısını sayarken feature tüketimini atlar.

**Belirleyici İngilizce koşul:** `all batches contain ten images`

**Doğru seçenek metni:** 60 requests per minute, because each request consumes ten label-detection feature units.

**Kaynak:** Ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vision/quotas)

**Önceki ilişki:** Yeni sayısal karar; S08-34 batch seçiminden farklı request-feature bütçesi.

## Q07 — B

**Karar:** Cloud Run invocation için hedef audience’lı OIDC ID token kullanılır.

**Yakın seçenek / sınır:** A runtime hesabına izin eklemek yanlış incoming token tipini düzeltmez.

**Belirleyici İngilizce koşul:** `rejects them before the handler runs`

**Doğru seçenek metni:** Configure an OIDC ID token representing task-caller with the destination service URL as its audience.

**Kaynak:** Ek resmî kaynak; rehber 1.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks)

**Önceki ilişki:** Bilinçli pekiştirme; S01-06/R01-05, 5 Ekim Tasks token öğretimi; audience hazır değil token tipi hatalı.

## Q08 — D

**Karar:** Olay nesneyi tarif eder; worker belgeyi Storage’dan okur.

**Yakın seçenek / sınır:** C CloudEvent envelope’unu decode ederek orijinal belgeyi elde edemez.

**Belirleyici İngilizce koşul:** `assumes the event body contains the document bytes`

**Doğru seçenek metni:** Use the event's object information to identify the input, and have the authorized worker fetch the document from Cloud Storage.

**Kaynak:** Ek resmî kaynak; rehber 1.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/eventarc/standard/docs/event-format)

**Önceki ilişki:** Bilinçli pekiştirme; S13-22 event/bytes; burada bozuk OCR input teşhisi.

## Q09 — A

**Karar:** Mevcut prompt başarılı ve dataset yok; tuning zorunlu değildir.

**Yakın seçenek / sınır:** B her uygulama talimatını training ihtiyacı sayar; C deployment ile training’i karıştırır.

**Belirleyici İngilizce koşul:** `already meet the acceptance criteria`

**Doğru seçenek metni:** Keep the effective prompt and examples, and evaluate changes before considering tuning if measured needs later justify it.

**Kaynak:** PDF s.8 + ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models)

**Önceki ilişki:** Yeni ölçüm; PDF customization açıklamasını koşullu karar yapar.

## Q10 — C

**Karar:** Kaynak bucket erişimi gerçek runtime hesabına verilir.

**Yakın seçenek / sınır:** D platform service agent’ı uygulama runtime’ı yerine koyar.

**Belirleyici İngilizce koşul:** `Logs confirm that Cloud Run uses image-runtime`

**Doğru seçenek metni:** Grant image-runtime Storage Object Viewer on the source bucket and keep the service using its attached runtime identity.

**Kaynak:** Ek resmî kaynak; rehber 1.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/run/docs/securing/service-identity) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workstations/docs/authentication)

**Önceki ilişki:** Bilinçli pekiştirme; S12-24 ilk yanlış ve S11-30 kimlik ayrımı; upload yerine input read teşhisi.

## Q11 — D

**Karar:** Google API raw HTTP çağrısı OAuth2; Cloud Run çağrısı OIDC.

**Yakın seçenek / sınır:** B access token ile ID token hedeflerini aynılaştırır.

**Belirleyici İngilizce koşul:** `Neither call uses a Workflows connector`

**Doğru seçenek metni:** Use OAuth2 for the Cloud Storage API and OIDC with the service URL audience for the Cloud Run worker.

**Kaynak:** Ek resmî kaynak; rehber 4.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/workflows/docs/http-requests) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workflows/docs/authentication)

**Önceki ilişki:** Karma; 5 Ekim token öğretimi, iki hedefin workflow auth yapılandırması.

## Q12 — B

**Karar:** Kota doluyken fazla async iş sırada kalabilir; kabul edilen operation izlenir.

**Yakın seçenek / sınır:** A gereksiz duplicate submissions oluşturur; D aktif görüntü kotasını kaldırmaz.

**Belirleyici İngilizce koşul:** `in-processing quota is full`

**Doğru seçenek metni:** Track the accepted operation and allow queued work to progress; assess a quota increase if the required completion time cannot be met.

**Kaynak:** Ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vision/quotas) · [Ek resmî kaynak 2](https://docs.cloud.google.com/vision/docs/batch)

**Önceki ilişki:** Yeni ölçüm; S08-34 batch seçimi yerine kabul edilmiş işin beklemesi.

## Q13 — C

**Karar:** Önceden eğitilmiş OCR ve generative görsel açıklama ayrı API ihtiyaçlarıdır.

**Yakın seçenek / sınır:** A geliştirici yardımını uygulama inference API’si yerine koyar.

**Belirleyici İngilizce koşul:** `preserve those interfaces rather than train a custom model`

**Doğru seçenek metni:** Call the Vision OCR API for the required OCR result and the Gemini API with image context for generative answers.

**Kaynak:** PDF s.13,16 + ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vision/docs/ocr) · [Ek resmî kaynak 2](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/overview)

**Önceki ilişki:** Karma; S05-14 araç ayrımı, Vision/Gemini uygulama çıktıları birlikte.

## Q14 — D

**Karar:** Desteklenen local ADC impersonation + Token Creator runtime kimliğiyle test sağlar.

**Yakın seçenek / sınır:** B actAs hesabı kaynağa bağlama yetkisidir; tek başına token mint etmez.

**Belirleyici İngilizce koşul:** `resource permissions ... must remain unchanged`

**Doğru seçenek metni:** Grant the developer Service Account Token Creator on ai-runtime and configure supported impersonated ADC for that account.

**Kaynak:** Ek resmî kaynak; rehber 2.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workstations/docs/authentication)

**Önceki ilişki:** Bilinçli pekiştirme; S09-02 ilk yanlış, yeni temel konu değil.

## Q15 — A

**Karar:** Tamamlanmış durable kayıt ikinci API çağrısını atlatır; yeni iş bitmeden ack verilmez.

**Yakın seçenek / sınır:** D business ID’yi delivery’ye göre değiştirerek duplicate korumasını bozar. Eşzamanlı delivery için atomik claim ayrıca gerekir.

**Belirleyici İngilizce koşul:** `success response is lost`

**Doğru seçenek metni:** Check the durable completion record before processing, return success for an already completed operation, and otherwise finish and persist the work before acknowledging.

**Kaynak:** Ek resmî kaynak; rehber 1.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/tasks/docs/common-pitfalls)

**Önceki ilişki:** Karma; S09-03 erken ack ve S09-21 create dedup yerine tamamlanmış delivery sonrası ücretli call atlama.

## Q16 — A

**Karar:** Raw submission başarı yanıtı işin bitişi değildir; operation ve hata izlenir.

**Yakın seçenek / sınır:** B gecikmeyi submission başarısızlığı sanıp tekrar ücretli iş üretir.

**Belirleyici İngilizce koşul:** `No connector is waiting ... automatically`

**Doğru seçenek metni:** Store the operation name, wait or poll its status until successful completion, check errors, and then read the output for the Gemini step.

**Kaynak:** Ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vision/docs/batch) · [Ek resmî kaynak 2](https://docs.cloud.google.com/workflows/docs/connectors)

**Önceki ilişki:** Karma; S12-16/33 sıralama, yeni LRO completion bağımlılığı.

## Q17 — B

**Karar:** Ürün özelliği için backend API entegrasyonu yazılır; editor desteği bunu otomatik eklemez.

**Yakın seçenek / sınır:** D extension kurulumunu request handler/inference entegrasyonu yerine koyar.

**Belirleyici İngilizce koşul:** `contains no model API call or integration code`

**Doğru seçenek metni:** Add a backend Gemini API integration that sends the authorized input and handles the model response; use the editor assistant separately to help develop that code.

**Kaynak:** PDF s.1–3,16 + ek resmî kaynak; rehber 2.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart)

**Önceki ilişki:** Bilinçli temel pekiştirme; S05-14 ve 6 Ekim araç öğretimi; ürün runtime ayrımı.

## Q18 — D

**Karar:** Kalıcı failure kayıt altına alınır ve task ack edilir; transient işler retry yolunda kalır.

**Yakın seçenek / sınır:** B görünürlüğü ve transient recovery’yi birlikte kaybeder.

**Belirleyici İngilizce koşul:** `repeated attempts cannot change its bytes`

**Doğru seçenek metni:** Record the permanent input failure durably and acknowledge that task; keep retryable failures on the retry path.

**Kaynak:** Ek resmî kaynak; rehber 1.1. [Ek resmî kaynak 1](https://docs.cloud.google.com/tasks/docs/configuring-queues) · [Ek resmî kaynak 2](https://docs.cloud.google.com/vision/docs/reference/rest/v1/images/annotate)

**Önceki ilişki:** Bilinçli pekiştirme; S02-08/S13-24. Vision invalid input ve kuyruk kararı.

## Q19 — A + C

**Karar:** API etkinleştirme ve runtime prediction yetkisi iki ayrı eksiktir.

**Yakın seçenek / sınır:** B enable yetkisini data/model işlemiyle karıştırır; D farklı kimliği yetkilendirir.

**Belirleyici İngilizce koşul:** `A review finds two gaps`

**Doğru seçenek metni:** Have the authorized deployment administrator enable aiplatform.googleapis.com in the applicable project. / Grant ai-runtime an appropriately scoped role containing aiplatform.endpoints.predict.

**Kaynak:** PDF s.16 başlangıç akışı + ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart) · [Ek resmî kaynak 2](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/access-control) · [Ek resmî kaynak 3](https://docs.cloud.google.com/run/docs/securing/service-identity)

**Önceki ilişki:** Bilinçli pekiştirme; S08-24. Gemini prediction permission somutlaştırması.

## Q20 — A

**Karar:** İki fleet aynı feature bütçesini paylaşır; toplam 700 > 600.

**Yakın seçenek / sınır:** B kimlik değişimini yeni project quota sanır; C image tüketimini azaltmaz.

**Belirleyici İngilizce koşul:** `same Vision quota project`

**Doğru seçenek metni:** Coordinate a combined image-submission budget within the available project feature quota, buffering excess work and including retry traffic in the budget.

**Kaynak:** Ek resmî kaynak; rehber 4.2. [Ek resmî kaynak 1](https://docs.cloud.google.com/vision/quotas) · [Ek resmî kaynak 2](https://docs.cloud.google.com/tasks/docs/configuring-queues)

**Önceki ilişki:** Karma; Q6 tek client hesabından farklı bağımsız fleet koordinasyonu; S11-28 dispatch temeli.
