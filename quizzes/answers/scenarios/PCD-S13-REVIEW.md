# PCD-S13 — 50 soru, cevaplar ve bilgi notları

9 Ekim 2026. **Anahtarlı çalışma içindir.** İlk sonuç **29/50 (%58), 112 dakika** korunur. Özgün İngilizce soru gövdeleri ve tüm seçenekler değiştirilmemiştir. Q22/Q39/Q41 çift seçimdir.

Her soruda ilk cevabın, doğru cevap, kısa gerekçe, bilmen gereken ürün/mekanizma bilgisi, yakın alternatifin neden elendiği ve resmî kaynak bulunur. Bilgi notları öğrenme desteğidir; o bilgiyi hiç bilmediğin veya yanlışının mutlaka bilgi eksikliğinden kaynaklandığı varsayılmaz. Bu dosyayı okumak yeni bağımsız deneme veya öğrenme teyidi değildir.

## Yarın çalışma düzeni

Süre tutmadan bir beşlik bölümle başla; sonra mola verip devam edip etmeyeceğine karar ver. Elli soruyu tek oturumda bitirmek zorunda değilsin. Önce senaryoyu ve şıkları oku; ardından cevabı ve bilgi notunu incele. Kendi kendine yalnız “Bilgi yeni miydi, koşulu mu kaçırdım, alternatifleri mi karıştırdım?” diye bak; yazılı gerekçe zorunlu değil.

Yanlış sorular: **1, 2, 7, 8, 10, 11, 12, 14, 16, 19, 21, 22, 23, 34, 35, 40, 45, 46, 47, 49, 50.**

- [Bölüm 1: 1–5](#bölüm-1)
- [Bölüm 2: 6–10](#bölüm-2)
- [Bölüm 3: 11–15](#bölüm-3)
- [Bölüm 4: 16–20](#bölüm-4)
- [Bölüm 5: 21–25](#bölüm-5)
- [Bölüm 6: 26–30](#bölüm-6)
- [Bölüm 7: 31–35](#bölüm-7)
- [Bölüm 8: 36–40](#bölüm-8)
- [Bölüm 9: 41–45](#bölüm-9)
- [Bölüm 10: 46–50](#bölüm-10)

## Bölüm 1

Sorular 1–5.

### Soru 01

A Cloud Build configuration starts with linting and unit tests, neither of which depends on the other. Integration tests must start only after both checks succeed. Failing checks must fail the build, and all required files already exist in the shared workspace. Which dependency configuration permits parallel checks while preserving the integration-test gate?

**Select ONE answer.**

**A.** Configure all three steps without any waitFor or id fields to run them in the default serial order, and rely on Cloud Build to optimize execution.

**B.** Configure all three steps with waitFor: ['-'] to run them all concurrently from the start of the build.

**C.** Configure the lint step with id: 'lint', unit test step with id: 'unit-test' and waitFor: ['-'], and the integration test step with waitFor: ['lint', 'unit-test'].

**D.** Create three separate Cloud Build triggers, each running one type of test, and use Pub/Sub to coordinate their execution order.

**İlk cevabın: D · Yanlış**

**Doğru cevap: C**

**Neden?** İlk lint adımı başlar; unit-test waitFor:[-] ile bağımsız başlar. Integration iki IDye bağlı olduğu için ikisinin başarıyla bitmesini bekler.

**Bilmen gereken bilgi:** Cloud Build’de `id` bir adıma isim verir; `waitFor` o adımın hangi başarılı adımları bekleyeceğini söyler. `waitFor: ['-']` başlangıçtan itibaren bağımsız çalıştırır. Lint ve unit test paralel başlayabilir; integration ikisinin de bitmesini bekler. Bunun için üç ayrı trigger kurmaya gerek yoktur.

**Yakın seçenek ve sınır:** Üçüne de [-] vermek gatei kaldırır; waitFor olmadan default sıra paralellik sağlamaz. Uzun yaşayan DB readiness bu sorunun konusu değildir.

**Belirleyici İngilizce koşul:** `only after both checks succeed`

**Kaynak:** SCP14-Q20; rehber 2.2. [Ek resmî kaynak](https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order).

---

### Soru 02

A Cloud Code development workflow already watches a repository and uses Docker with Skaffold. Editing a static HTML file still rebuilds and redeploys the whole image. The running development server can serve changed files directly from disk, and the team knows their destination paths inside the container. Which Skaffold change avoids rebuilding the image for these edits?

**Select ONE answer.**

**A.** Add a sync section with manual rules specifying source HTML files and their destination paths in the container for the artifact you want to configure.

**B.** Configure Cloud Build in the profiles section of skaffold.yaml to handle incremental builds of your HTML files.

**C.** Enable Buildpacks as your builder instead of Docker, which automatically configures hot reloading for HTML files without additional configuration.

**D.** Set the watch field to true in your .vscode/launch.json file to enable automatic file watching and synchronization for all file types.

**İlk cevabın: C · Yanlış**

**Doğru cevap: A**

**Neden?** Skaffold manual sync kuralları eşleşen dosyaları container hedef yoluna taşır. Static server yeni içeriği diskten okuyabilir.

**Bilmen gereken bilgi:** Skaffold file sync, değişen dosyayı image rebuild yapmadan çalışan container’a kopyalar. `sync.manual` içinde kaynak dosya deseni ve container’daki hedef yol belirtilir. Uygulamanın dosyayı diskten yeniden okuyabilmesi gerekir; derleme gerektiren her değişiklik sync ile uygulanamaz. Buildpacks seçmek tek başına HTML sync kuralı tanımlamaz.

**Yakın seçenek ve sınır:** watch değişiklik algılar; hangi dosyanın image rebuild yerine sync edileceğini tek başına tanımlamaz.

**Belirleyici İngilizce koşul:** `serve changed files directly from disk`

**Kaynak:** SCP17-Q07; rehber 2.1. [Ek resmî kaynak](https://skaffold.dev/docs/filesync/).

---

### Soru 03

A Cloud Deploy pipeline already targets a Cloud Run service with a stable revision. The next release should receive 10%, then 25%, then 50% of traffic before the final stable phase. You want Cloud Deploy to manage these traffic changes rather than running custom traffic commands in hooks. Which delivery-pipeline configuration should you use?

**Select ONE answer.**

**A.** Configure the Cloud Run service definition YAML with a traffic stanza specifying the percentage splits, and reference it in the skaffold.yaml for each canary phase.

**B.** Use strategy.canary with runtimeConfig.cloudRun.automaticTrafficControl: true and canaryDeployment.percentages: [10, 25, 50].

**C.** Configure the delivery pipeline with strategy.standard, and use predeploy hooks to call gcloud run services update-traffic with the desired percentages at each deployment phase.

**D.** Configure multiple Cloud Run services (one stable, one canary) and use Cloud Deploy to deploy to each service independently with different traffic percentages via an external load balancer.

**İlk cevabın: B · Doğru**

**Doğru cevap: B**

**Neden?** Cloud Deploy automated canary ile trafik aşamalarını yönetir. Ara yüzdeler 10/25/50; son stable phase 100e tamamlar.

**Bilmen gereken bilgi:** Canary, yeni sürüme trafiği aşamalarla artırır. Cloud Deploy bunu rollout stratejisiyle yönetebilir; sorudaki 10/25/50 yüzdelerinden sonra stable aşama 100’e geçer. Özel hook içinde trafik komutları çalıştırmak ile yerleşik automated traffic control aynı yapılandırma değildir.

**Yakın seçenek ve sınır:** standard strategy + özel hook çalışabilir ama istenen native traffic control değildir. Bu mevcut stable revisionlı rollout; ilk deploy farklı davranabilir.

**Belirleyici İngilizce koşul:** `rather than running custom traffic commands in hooks`

**Kaynak:** SCP16-Q60; rehber 3.1. [Ek resmî kaynak](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run).

---

### Soru 04

A service lists all objects in a large Cloud Storage bucket through the JSON API. It needs each object's name and size, but full metadata responses waste bandwidth. Listing requires multiple pages. Which response-field configuration reduces the payload while preserving the information required to finish the complete listing?

**Select ONE answer.**

**A.** Set the includeMetadata parameter to false in each list request to exclude all object metadata from the response payload.

**B.** Use the projection query parameter set to 'noAcl' to exclude ACL data, which automatically excludes all metadata and reduces response size.

**C.** Add the fields query parameter to specify only the required object properties and include nextPageToken and items fields to preserve pagination capability.

**D.** Configure the bucket to store metadata in a separate location and use the metadataOnly parameter to retrieve object names without metadata.

**İlk cevabın: C · Doğru**

**Doğru cevap: C**

**Neden?** fields seçimi item name/size ile nextPageTokenı birlikte korumalıdır. Sonraki requestte token pageToken olarak gönderilir.

**Bilmen gereken bilgi:** Partial response için `fields`, pagination için `pageToken` kullanılır. `nextPageToken` yanıtın alanlarından çıkarılırsa sonraki sayfaya geçmek için gereken bilgi kaybolur. Daha az veri istemek, tüm sayfaları dolaşma gereğini kaldırmaz.

**Yakın seçenek ve sınır:** Sadece object alanlarını tutmak pagination bilgisini düşürebilir; daha büyük tek sayfa bütün listeyi garanti etmez.

**Belirleyici İngilizce koşul:** `Listing requires multiple pages`

**Kaynak:** SCP13-Q06; rehber 4.2. [Ek resmî kaynak](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters).

---

### Soru 05

You are building a microservice in VS Code with the Gemini Code Assist plugin installed. You want Gemini Code Assist to autonomously perform multi-step tasks that read items from your team's external project tracker and your private API documentation service during a chat session, instead of only suggesting code. You need to follow Google's recommended way to extend the assistant with these external tools. What should you do?

**Select ONE answer.**

**A.** Enable Gemini Code Assist agent mode and configure Model Context Protocol (MCP) servers for the external services in the Gemini settings so the agent can discover and call those tools.

**B.** Write a custom VS Code extension that calls the tracker and documentation APIs, publish it to the marketplace, and reference each retrieved item with the @ symbol followed by the tool name in the chat to inject the data.

**C.** Use code completion and inline suggestions, and paste the relevant tracker items and API documentation into a code comment so that Gemini Code Assist uses the file as context.

**D.** Switch to Gemini Code Assist code customization and point it at your private source code repositories so the assistant indexes the external tracker and documentation.

**İlk cevabın: A · Doğru**

**Doğru cevap: A**

**Neden?** Agent mode içinde MCP serverlar dış araçları tanıtır. Tracker ve özel doküman servisine kontrollü araç erişimi bu mekanizmayla sağlanır.

**Bilmen gereken bilgi:** MCP bir model değildir; AI agent’ın dış araçları keşfedip çağırmasına yarayan bir protokoldür. Repository bağlamı kod önerilerine yardımcı olur; tracker’da işlem yapmak veya özel doküman servisini sorgulamak ise araç entegrasyonudur. Dış servisin kimlik ve erişim izinleri ayrıca sağlanır.

**Yakın seçenek ve sınır:** Code customization repository bağlamı sunar; herhangi bir harici sistemde işlem yapan araç entegrasyonunun yerine geçmez.

**Belirleyici İngilizce koşul:** `external project tracker and your private API documentation service`

**Kaynak:** SCP14-Q51; rehber 2.1. [Ek resmî kaynak](https://docs.cloud.google.com/gemini/docs/codeassist/agent-mode).

---

## Bölüm 2

Sorular 6–10.

### Soru 06

An aggregated sink already routes application logs from many projects into one log bucket in a central observability project. You want one log-derived error counter based on entries arriving in that bucket, including entries originating in other projects. You do not want to manage a separate metric in every source project. Where and how should you define the metric?

**Select ONE answer.**

**A.** Create organization-level log-based metrics with filters matching error logs from all projects to get a unified view across the organization.

**B.** Create project-scoped log-based metrics in each source project and aggregate the metrics in Cloud Monitoring using cross-project metrics scopes.

**C.** Create project-scoped log-based metrics in the central project with filters that specify the source projects using the logName field.

**D.** Create bucket-scoped log-based metrics in the project containing the central log bucket. Configure filters to match error logs from all source projects routed to the bucket.

**İlk cevabın: D · Doğru**

**Doğru cevap: D**

**Neden?** Bucket-scoped metric merkezi bucketta gelen kayıtları kaynak projelerinden bağımsız değerlendirir. Metric bucketın bulunduğu projede tanımlanır.

**Bilmen gereken bilgi:** Project-scoped ve bucket-scoped log metric kapsamları farklıdır. Merkezi log bucket başka projelerden yönlendirilmiş kayıtlar tutabilir; bu bucket’ın içeriği üzerinden metric üretmek için bucket-scoped metric kullanılır. Metric’in hangi veriyi sayacağı ile nerede tanımlandığını ayrı düşün.

**Yakın seçenek ve sınır:** Central project-scoped metric varsayımı ile routed bucket kapsamı aynı değildir. Folder düzeyinde log metric yaratılmaz.

**Belirleyici İngilizce koşul:** `including entries originating in other projects`

**Kaynak:** SCP17-Q51; rehber 4.3. [Ek resmî kaynak](https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm).

---

### Soru 07

Operators occasionally request destruction of the wrong Secret Manager version. You need a built-in seven-day recovery window after a version-destruction request, without running your own scheduling or backup service. This requirement applies to version destruction, not deletion of the entire secret resource. Which configuration should you apply before such a request occurs?

**Select ONE answer.**

**A.** Configure a Pub/Sub notification for SECRET_VERSION_DESTROYED events and create a Cloud Run function that restores the secret from a backup within 7 days.

**B.** Disable secret versions before destroying them, and create a Cloud Scheduler job to permanently destroy disabled versions after 7 days.

**C.** Set an expiration time of 7 days on all secret versions to prevent them from being destroyed before the expiration period ends.

**D.** Enable the delay secret version destroy feature on the secret and set the destruction delay duration to 7 days or more.

**İlk cevabın: C · Yanlış**

**Doğru cevap: D**

**Neden?** Delayed destruction sürümü önce disabled yapıp kalıcı yok etmeyi ayarlanan süre sonrasına bırakır. Böylece native recovery penceresi oluşur.

**Bilmen gereken bilgi:** Secret’ın sürümleri vardır; disable, destroy ve rotation ayrı işlemlerdir. Delayed destruction etkinse destroy isteği sürümü hemen kullanıma kapatır, kalıcı yok etmeyi sonraya bırakır. Gecikme penceresinde planlanan silme iptal edilerek sürüm geri alınabilir; kalıcı destruction sonrası veri geri getirilemez. Expiration aynı kurtarma mekanizması değildir.

**Yakın seçenek ve sınır:** Rotation yeni credential üretim süreciyle, expiration ise başka yaşam döngüsüyle ilgilidir; geri dönüşsüz destroy sonrası bildirim veriyi geri getirmez.

**Belirleyici İngilizce koşul:** `a built-in seven-day recovery window`

**Kaynak:** SCP14-Q58; rehber 1.2. [Ek resmî kaynak](https://docs.cloud.google.com/secret-manager/docs/delay-destruction-of-secret-versions).

---

### Soru 08

A legacy Cloud Run application already reads its API key from an environment variable at startup. You must supply a pinned Secret Manager version without changing application code. If Cloud Run cannot retrieve that version for a new instance, the instance must not start successfully with a missing key. Which native configuration should you use?

**Select ONE answer.**

**A.** Configure the secret as an environment variable in the Cloud Run service configuration.

**B.** Configure a startup probe that verifies the secret is accessible before accepting traffic.

**C.** Use the Secret Manager client library to fetch the secret in the application main function.

**D.** Configure the secret as a mounted volume in the Cloud Run service configuration.

**İlk cevabın: B · Yanlış**

**Doğru cevap: A**

**Neden?** Native secret environment variable yeni instance başlamadan çözümlenir. Erişilemeyen secretla instance startup başarısız olur. Pinned version belirli değeri seçer.

**Bilmen gereken bilgi:** Secret environment variable olarak bağlanınca Cloud Run instance başlamadan değeri alır; secret okunamazsa startup başarısız olur. Secret volume ise dosya okuma yoludur. Env okuyan mevcut kodu değiştirmeden dosya mount’u kullanmak aynı sonucu vermez; startup probe da secret’ı env’e enjekte etmez.

**Yakın seçenek ve sınır:** Volume okuması runtime erişim yoludur; mevcut legacy env okuyucuyu kod değişmeden beslemez.

**Belirleyici İngilizce koşul:** `without changing application code`

**Kaynak:** SCP14-Q60; rehber 3.1. [Ek resmî kaynak](https://docs.cloud.google.com/run/docs/configuring/services/secrets).

---

### Soru 09

A Cloud Tasks queue calls an idempotent HTTP worker. Some calls fail with transient HTTP 503 responses. Operations wants at most five total attempts, increasing delays between failed attempts, and no application-managed re-enqueue loop. The queue has no retry-duration limit (maxRetryDuration is zero). Which configuration most directly provides the requested retry behavior?

**Select ONE answer.**

**A.** Configure the queue's maximum dispatch rate and concurrency so failed tasks are slowed down and eventually succeed.

**B.** Set the queue's retry parameters, such as the maximum number of attempts and the minimum and maximum backoff, so Cloud Tasks retries failed tasks automatically.

**C.** Create a Cloud Scheduler job that periodically re-runs all tasks that previously failed.

**D.** In the HTTP handler, catch the error and re-enqueue a new copy of the same task with an incremented attempt counter stored in the payload, then return success so the original task is removed from the queue and you can cap retries yourself.

**İlk cevabın: B · Doğru**

**Doğru cevap: B**

**Neden?** Queue retry config yeniden denemeleri yönetir. maxAttempts ilk çağrıyı da sayar; burada süre sınırı sıfır olduğundan beş toplam deneme hedefi açıktır.

**Bilmen gereken bilgi:** Dispatch ayarları işlerin ne hızla gönderildiğini, retry ayarları başarısız işin nasıl tekrar denendiğini yönetir. `maxAttempts` ilk denemeyi de sayar. Bu soruda `maxRetryDuration=0` verilmesi önemlidir; süre ve deneme sınırlarının birlikte davranışını görmezden gelerek genel bir sayısal kural çıkarma.

**Yakın seçenek ve sınır:** Dispatch rate ile retry sayısı farklıdır. Backoff doubling sonrası doğrusal artabilir; kaynak açıklamasındaki eksik aralık örneği kullanılmadı.

**Belirleyici İngilizce koşul:** `maxRetryDuration is zero`

**Kaynak:** SCP14-Q17; rehber 1.1. [Ek resmî kaynak](https://docs.cloud.google.com/tasks/docs/configuring-queues).

---

### Soru 10

An uncached API runs on Cloud Run in North America and Europe. Each regional service can handle the complete application independently. You want one public HTTPS endpoint that uses Google's network to direct users toward an appropriate nearby regional backend, rather than maintaining DNS routing rules yourself. Which architecture should you use?

**Select ONE answer.**

**A.** Deploy the Cloud Run service in one primary region and set up Cloud CDN. Create a serverless NEG pointing to the primary Cloud Run service and enable CDN caching on the backend service.

**B.** Deploy the Cloud Run service in multiple regions. Create a regional external Application Load Balancer in each region with a serverless NEG. Use Cloud DNS with geolocation routing policies to distribute traffic across regions.

**C.** Deploy the Cloud Run service in multiple regions. Create a serverless NEG in each region pointing to the regional Cloud Run service. Add all serverless NEGs to a single global backend service attached to a global external Application Load Balancer.

**D.** Deploy the Cloud Run service in multiple regions. Create separate backend services for each region with individual serverless NEGs. Configure URL map host and path rules to direct traffic to specific regional backends.

**İlk cevabın: B · Yanlış**

**Doğru cevap: C**

**Neden?** Her region için serverless NEG, tek global backend service ve global external Application Load Balancer kullanılır. Multi-region düzeninde Premium Tier gerekir.

**Bilmen gereken bilgi:** Serverless NEG, load balancer backend’ini bölgesel Cloud Run servisine bağlar. Sorudaki tasarım bir global load balancer ve farklı bölgelerdeki NEGs üzerinden çalışır. Bölgesel load balancer’lar ile DNS yönlendirmesi başka bir tasarımdır; soru bu ek yönetimi istemiyor. Multi-region global düzen için Premium Tier koşulu da vardır.

**Yakın seçenek ve sınır:** Bölgesel LB + DNS farklı bir tasarımdır; soru tek global LB yolu istiyor. Yakınlık veriyi kendiliğinden replike etmez.

**Belirleyici İngilizce koşul:** `rather than maintaining DNS routing rules yourself`

**Kaynak:** SCP15-Q09; rehber 1.1. [Ek resmî kaynak](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts).

---

## Bölüm 3

Sorular 11–15.

### Soru 11

A GKE Deployment has a CPU-based HPA targeting 70% utilization. The metrics service is healthy, and Pod CPU usage is visible, but this HPA cannot calculate utilization and reports an undefined target. The application container has a CPU limit but no CPU request. Replicas are below maxReplicas, and sufficient cluster capacity is available. What should you change first?

**Select ONE answer.**

**A.** You must deploy and configure the Custom Metrics Stackdriver Adapter and grant it the monitoring.viewer role before the HPA controller can read CPU utilization from Cloud Monitoring for any GKE workload.

**B.** The containers in the Deployment do not define a CPU resource request, so the HPA cannot express current usage as a percentage of the request.

**C.** The Deployment's minReplicas value is set equal to its maxReplicas, which prevents the controller from adding any replicas.

**D.** The HorizontalPodAutoscaler manifest uses apiVersion autoscaling/v1, which does not support scaling on CPU metrics at all.

**İlk cevabın: A · Yanlış**

**Doğru cevap: B**

**Neden?** CPU utilization requeste oranla hesaplanır. Limit bulunması eksik requestin yerini tutmaz; request eklenmelidir.

**Bilmen gereken bilgi:** HPA CPU utilization oranında payda CPU request’tir. Örneğin 500m request ve 250m kullanım %50 eder; limit bu paydanın yerine geçmez. Soruda etkin request’in eksik olduğu açıkça verilmiştir.

**Yakın seçenek ve sınır:** Node kapasitesi ve maxReplicas kökte elendi. CPU metriği için custom adapter zorunlu değildir.

**Belirleyici İngilizce koşul:** `a CPU limit but no CPU request`

**Kaynak:** SCP14-Q23; rehber 3.2. [Ek resmî kaynak](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).

---

### Soru 12

Regional Cloud Run services sit behind a global external Application Load Balancer using serverless NEGs. One regional backend intermittently returns HTTP 5xx responses. You want the load balancer to reduce traffic to the failing backend based on observed response failures, without adding active probes to the application. Which backend-service feature should you configure?

**Select ONE answer.**

**A.** Create health check probes for each Cloud Run service endpoint and attach them to the backend service.

**B.** Configure separate backend services for each region and create a URL map with failover routing rules.

**C.** Enable Identity-Aware Proxy on the backend service to monitor and route traffic based on service health.

**D.** Enable outlier detection on the backend service and configure it to eject endpoints after consecutive 5xx errors are detected.

**İlk cevabın: B · Yanlış**

**Doğru cevap: D**

**Neden?** Outlier detection gözlenen başarısız yanıtları kullanarak sağlıksız serverless backendleri geçici dışlar; aktif probe istemeyen koşula uyar.

**Bilmen gereken bilgi:** Health check ayrı bir probe isteği gönderir; outlier detection gerçek çağrılardan gelen başarısız yanıtları gözler. Soruda aktif probe yerine gözlenen 5xx hatalarıyla geçici dışlama isteniyor. Outlier detection sıfır hata veya her yerde aynı anda failover garantisi vermez.

**Yakın seçenek ve sınır:** Bu sıfır hata veya anında global failover garantisi değildir. Cloud Run service health ayrı bir seçenek olabilir; burada passive response signal istenmiştir.

**Belirleyici İngilizce koşul:** `based on observed response failures`

**Kaynak:** SCP16-Q22; rehber 3.1. [Ek resmî kaynak](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts).

---

### Soru 13

Several API routes use an ORM to query Cloud SQL for PostgreSQL. Query latency increases under load, but normalized SQL text alone does not identify which application route generated the expensive calls. You want a supported way to correlate query performance with the application path, instead of inferring it from instance CPU graphs. Which instrumentation should you add?

**Select ONE answer.**

**A.** Enable Query Insights on your Cloud SQL instance and use the sqlcommenter library in your application to automatically tag SQL queries with application information from your MVC framework.

**B.** Run EXPLAIN ANALYZE on each slow query manually in the database console and maintain a spreadsheet documenting query performance metrics correlated with application endpoints.

**C.** Enable Cloud Monitoring for your Cloud SQL instance and create custom dashboards to track CPU and memory usage, then manually investigate queries during periods of high resource consumption.

**D.** Configure verbose logging on your ORM framework and export all logs to Cloud Logging, then use log-based queries to identify slow database operations by parsing execution times from log entries.

**İlk cevabın: A · Doğru**

**Doğru cevap: A**

**Neden?** Query Insights ve sqlcommenter route/controller gibi uygulama etiketlerini SQL performansıyla ilişkilendirir. Böylece benzer SQLi hangi yolun ürettiği görülebilir.

**Bilmen gereken bilgi:** Query Insights veritabanındaki sorgu performansını incelemeye yarar. sqlcommenter, sorguya uygulama route/controller gibi bağlam etiketleri ekleyebilir. Böylece benzer SQL metinlerinin hangi uygulama yolundan geldiği ayrılır; yalnız CPU grafiği bu ilişkiyi kurmaz.

**Yakın seçenek ve sınır:** CPU grafiği sorgunun uygulama kaynağını tek başına göstermez. Etiketlerde hassas kullanıcı verisi taşımaya gerek yoktur.

**Belirleyici İngilizce koşul:** `which application route generated`

**Kaynak:** SCP15-Q05; rehber 4.3. [Ek resmî kaynak](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights).

---

### Soru 14

A customer summary performs several related Spanner reads. All returned rows must reflect one database snapshot, although concurrent writers may update those rows while the summary is assembled. The operation never writes data. You want the simplest transaction type that provides the shared snapshot without acquiring read locks. Which approach should you use?

**Select ONE answer.**

**A.** Issue each read as a separate strong single-read call so that every individual read returns the latest committed data for that row.

**B.** Execute the reads inside a read-only transaction, which provides a consistent snapshot across all reads without acquiring locks.

**C.** Execute the reads inside a read-write transaction so that locks held during the reads guarantee all rows are observed at a consistent point in time.

**D.** Issue each read as a separate exact-staleness single read using the same staleness duration, then merge the rows together in application code afterward.

**İlk cevabın: D · Yanlış**

**Doğru cevap: B**

**Neden?** Read-only transaction okumaları tek snapshot üzerinde toplar ve read lock almaz. Ayrı okumalarda araya yeni commit girebilir.

**Bilmen gereken bilgi:** Snapshot, veritabanının belirli bir andaki görünümüdür. Read-only transaction içindeki okumalar aynı snapshot’ı paylaşır. İki ayrı çağrıda aynı staleness süresi kullanmak aynı timestamp’i seçmek değildir: ilk çağrının 'şimdi eksi 10 saniye'si ile sonraki çağrınınki farklıdır. Read-only transaction veri değiştiren transaction değildir ve read lock almaz.

**Yakın seçenek ve sınır:** Ayrı strong read çağrıları kendi başlarına güncel olabilir ama aynı anı paylaşmak zorunda değildir. Aynı staleness süresi de aynı timestamp demek değildir.

**Belirleyici İngilizce koşul:** `All returned rows must reflect one database snapshot`

**Kaynak:** SCP16-Q19; rehber 1.3. [Ek resmî kaynak](https://docs.cloud.google.com/spanner/docs/transactions).

---

### Soru 15

A loan-processing application calls six existing HTTP services in a defined order. Responses determine which branch runs next, and support staff need to inspect the state of each execution. The team wants a central, version-controlled definition of the sequence without maintaining a controller process or infrastructure that stays running between executions. Individual services should remain unaware of their successors. Which approach best fits these requirements?

**Select ONE answer.**

**A.** Chain the services together by having each service enqueue a Cloud Tasks task that targets the next service in the sequence.

**B.** Define the process as a Workflows workflow that calls each HTTP service in sequence and uses conditional steps for branching.

**C.** Deploy a Compute Engine managed instance group that runs a controller process which calls each service in order, persists the current step to a database, and evaluates branching logic from configuration files.

**D.** Publish a message to a Pub/Sub topic for each service and let each service subscribe to the previous service's topic.

**İlk cevabın: B · Doğru**

**Doğru cevap: B**

**Neden?** Workflows sıralamayı, koşullu dalları ve execution durumunu merkezi tanımlar. HTTP işçiler sonraki adımı bilmek zorunda kalmaz.

**Bilmen gereken bilgi:** Workflows adım sırasını, returned response’a göre dallanmayı ve execution durumunu yönetir. Her worker’ın kendinden sonraki servisi bilmesi gerekmez. Cloud Tasks ise tekil HTTP işinin teslimi, zamanlanması ve retry için uygundur; bütün iş sürecinin dallarını kendiliğinden oluşturmaz.

**Yakın seçenek ve sınır:** Tasks tekil çağrı teslimini yönetir; dallanan bütün sürecin state machine tanımını kendiliğinden sağlamaz.

**Belirleyici İngilizce koşul:** `Individual services should remain unaware of their successors`

**Kaynak:** SCP14-Q27; rehber 1.1. [Ek resmî kaynak](https://docs.cloud.google.com/workflows/docs/overview).

---

## Bölüm 4

Sorular 16–20.

### Soru 16

A GKE application writes a distinctive critical-error entry to Cloud Logging. On-call staff want a native alert when a matching entry arrives; they do not need a trend chart or a numerical count threshold. Normal incident and notification-rate controls are acceptable. Which alert type most directly matches this requirement?

**Select ONE answer.**

**A.** Create a log-based alerting policy in Cloud Monitoring that matches the specific error message pattern in your container logs.

**B.** Configure a Cloud Logging sink to export logs to Pub/Sub, then create a Cloud Function to parse the logs and send notifications when the error pattern is found.

**C.** Create a log-based metric that counts occurrences of the error message, then configure an alerting policy on the metric with a threshold of greater than zero.

**D.** Enable Error Reporting on your GKE cluster and configure it to send notifications for all detected errors.

**İlk cevabın: B · Yanlış**

**Doğru cevap: A**

**Neden?** Log-based alert matching entry üzerinden incident oluşturur. Sayısal trend gerekmeyen tek kritik olay için doğrudan mekanizmadır.

**Bilmen gereken bilgi:** Log-based alert, belirli log filtresine uyan bir kayıt geldiğinde bildirim akışı kurabilir. Log-based metric ise kayıtları sayısal ölçüme dönüştürür ve oran/trend gibi alert’lerde işe yarar. Tek kritik kaydı yakalamak için sink→Pub/Sub→function bildirim altyapısını baştan yazmak gerekmeyebilir.

**Yakın seçenek ve sınır:** Log-based metric + threshold da başka gereksinimlerde yararlıdır ama burada ek ölçüm katmanı gerekmiyor; notification limits korunur.

**Belirleyici İngilizce koşul:** `do not need a trend chart or a numerical count threshold`

**Kaynak:** SCP15-Q12; rehber 4.3. [Ek resmî kaynak](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

---

### Soru 17

A Bigtable application records three measurements per sensor per minute. Most reads fetch one sensor's data for a particular calendar week. A measured week of data fits comfortably within the recommended row-size limits, and writes are spread across many sensors. You want to group each sensor-week for efficient retrieval without an indefinitely growing row. Which schema is the best fit?

**Select ONE answer.**

**A.** Keep one row per sensor for its entire lifetime and append cells indefinitely.

**B.** Use timestamp#sensor_id so writes for all sensors begin with the current minute.

**C.** Create one row per measurement using sensor_id#timestamp; always assemble a week by scanning its individual rows.

**D.** Use sensor_id#week_start as the row key and store measurements as timestamped cells, with garbage collection configured to retain the required history.

**İlk cevabın: D · Doğru**

**Doğru cevap: D**

**Neden?** Sensor-week satırı ölçülen boyut sınırına uyuyor ve bir haftalık veriyi grupluyor. Timestamped cell geçmişi GC politikasıyla korunmalıdır.

**Bilmen gereken bilgi:** Bigtable time-series tasarımında her veriyi sonsuza kadar aynı satıra eklemek yerine zaman aralığıyla gruplayabilirsin. Soruda sensor-week boyutu ölçülmüş sınır içinde olduğundan haftalık satır uygundur. Timestamped cell sürümlerinin ne kadar tutulacağı GC politikasıyla uyumlu olmalıdır; schema kararı tek başına retention sağlamaz.

**Yakın seçenek ve sınır:** Tek ömürlük satır sınırsız büyür. Tall-narrow da geçerli bir tasarım olabilir; burada özellikle bounded haftalık gruplama tercihinin koşulları verilmiştir.

**Belirleyici İngilizce koşul:** `fits comfortably within the recommended row-size limits`

**Kaynak:** SCP14-Q19; rehber 1.3. [Ek resmî kaynak](https://docs.cloud.google.com/bigtable/docs/schema-design-time-series).

---

### Soru 18

A backend has already authorized a customer to download one private Cloud Storage object. The customer does not use a Google account. Possession of the link is an acceptable access credential, and new download requests should be authorized by that link for two hours. The backend has a working signer and the necessary object-read permission. Which V4 signed-URL configuration meets the requirement?

**Select ONE answer.**

**A.** Generate V4 signed URLs with the X-Goog-Expires parameter set to 7200 seconds (2 hours) using a service account that has storage.objects.get permission on the bucket.

**B.** Configure the bucket with a 2-hour retention policy and generate unsigned public URLs for the objects after temporarily setting them to public.

**C.** Generate V4 signed URLs with the X-Goog-Expires parameter set to 604800 seconds (7 days) and implement expiration validation in your application code.

**D.** Generate V2 signed URLs with the Expires parameter set to a Unix timestamp 2 hours in the future using HMAC keys for signing.

**İlk cevabın: A · Doğru**

**Doğru cevap: A**

**Neden?** V4 X-Goog-Expires saniye cinsinden süreyi taşır; iki saat 7200 saniyedir. Yetkili signer önkoşulu soruda sağlanmıştır.

**Bilmen gereken bilgi:** Signed URL, imza kapsamındaki kaynağa belirli süreyle erişim sağlar. V4 `X-Goog-Expires` saniye cinsindendir; 2 saat = 7200 saniye. URL’nin çalışması yetkili signer ve doğru imza koşullarına bağlıdır; süre belirtmek tek başına kaynak yetkisini yaratmaz.

**Yakın seçenek ve sınır:** Retention verinin silinebilirliğini düzenler; link kullanım süresi değildir. Link bearer credentialdır ve indirilmiş kopyayı geri alamaz.

**Belirleyici İngilizce koşul:** `Possession of the link is an acceptable access credential`

**Kaynak:** SCP14-Q52; rehber 1.3. [Ek resmî kaynak](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

---

### Soru 19

Your organization requires that any container image deployed to the production GKE cluster has both a 'built-by-cloud-build' attestation produced automatically by the build pipeline and a separate 'qa-approved' attestation signed by the QA team after end-to-end tests pass. Images missing either attestation must be rejected at admission. How should you configure the Binary Authorization policy?

**Select ONE answer.**

**A.** Create a single attestor whose note references both the build pipeline's KMS key and the QA team's KMS key, and require that attestor in the admission rule.

**B.** Configure two separate cluster-specific admission rules for the same cluster, each with REQUIRE_ATTESTATION and a single attestor.

**C.** Configure the cluster admission rule with evaluationMode: REQUIRE_ATTESTATION and enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG, listing both attestors under requireAttestationsBy.

**D.** Set the default admission rule to REQUIRE_ATTESTATION with the built-by-cloud-build attestor, and use Continuous Validation to flag images that lack the qa-approved attestation after deployment.

**İlk cevabın: B · Yanlış**

**Doğru cevap: C**

**Neden?** Admission kuralında iki attestor requireAttestationsBy listesine konur; image iki gerekli doğrulamayı da taşımalıdır ve enforcement mode uyumsuz imageı bloke etmelidir.

**Bilmen gereken bilgi:** Attestor, image için gerekli doğrulamayı temsil eder. İki bağımsız onay gerekiyorsa aynı admission rule içindeki `requireAttestationsBy` listesine iki attestor konur. Cluster rule, aynı cluster anahtarı altında üst üste yığılan iki bağımsız kural değildir. Dry-run yalnız kaydeder; engelleme için enforcement gerekir.

**Yakın seçenek ve sınır:** Continuous Validation sonradan bulgu üretmekle admission anında ikinci attestationı zorunlu kılmanın yerini tutmaz.

**Belirleyici İngilizce koşul:** `Images missing either attestation must be rejected at admission`

**Kaynak:** SCP18-Q26; rehber 1.2. [Ek resmî kaynak](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference).

---

### Soru 20

Fifty developers need browser-accessible development environments with the same approved JDK, gcloud CLI, Cloud Code, and Gemini Code Assist installation. The platform team must centrally maintain tool versions and place the environments in its controlled VPC. The environments must support persistent personal work without depending on each developer's laptop configuration. Which managed approach should you use?

**Select ONE answer.**

**A.** Have each developer use Cloud Shell with a customized .customize_environment script to install the JDK and required extensions on session startup.

**B.** Provide each developer with a Compute Engine VM that has a startup script to install the JDK, gcloud, and Cloud Code, and instruct them to SSH in through the Google Cloud console.

**C.** Build a custom Cloud Workstations container image that extends a preconfigured base image with the required tools, and create a workstation configuration that applies the image to all developer workstations.

**D.** Distribute a Cloud Code preconfigured VS Code Dev Container definition and have each developer run it locally on their laptop using Docker Desktop.

**İlk cevabın: C · Doğru**

**Doğru cevap: C**

**Neden?** Cloud Workstations config merkezi custom image ve ağ ayarlarını uygular; geliştirici araçları image ile tutarlı dağıtılır. Persistent home ayrı tutulabilir.

**Bilmen gereken bilgi:** Cloud Workstations configuration, geliştiricilere ortak image ve ağ ayarlarını uygular. Custom image standart toolchain’i, persistent home ise kullanıcı dosyalarını taşır. Bir geliştiricinin çalışan container’a elle araç kurması ekibin yeni workstation’larında aynı aracı otomatik sağlamaz.

**Yakın seçenek ve sınır:** Cloud Code eklentisi tek başına yönetilen VPC ortamı yaratmaz. Araç kurulumu Gemini lisans ve erişim izinlerini otomatik sağlamaz.

**Belirleyici İngilizce koşul:** `centrally maintain tool versions`

**Kaynak:** SCP14-Q50; rehber 2.1. [Ek resmî kaynak](https://docs.cloud.google.com/workstations/docs/customize-container-images).

---

## Bölüm 5

Sorular 21–25.

### Soru 21

A Python function constructs a Cloud Storage client internally and then applies business logic before uploading a file. You want Gemini Code Assist to help create isolated unit tests that exercise the real business logic without real credentials or network calls. The team prefers an explicit dependency boundary over patching global constructors. Which change best supports that design?

**Select ONE answer.**

**A.** Ask Gemini Code Assist to leave the function unchanged and instead generate an end-to-end test that provisions a temporary Cloud Storage bucket, uploads a real object, asserts the object exists, and deletes the bucket during teardown.

**B.** Ask Gemini Code Assist to refactor the function so the storage client is passed in as a parameter, then have it generate tests that inject a test double in place of the real client.

**C.** Ask Gemini Code Assist to set a longer timeout on each test so the real Cloud Storage client has enough time to respond during the test run.

**D.** Ask Gemini Code Assist to wrap the entire test in a try/except block so that any errors from the real Cloud Storage client are ignored at runtime.

**İlk cevabın: A · Yanlış**

**Doğru cevap: B**

**Neden?** Client dependency olarak verilir; test double dış servisi değiştirirken business logic gerçek kalır. Network ve credential ihtiyacı kaldırılır.

**Bilmen gereken bilgi:** Unit test, test edilen iş mantığını gerçek çalıştırıp dış servis bağımlılığını mock/fake ile değiştirebilir. Dependency injection, client’ı içeride gizlice oluşturmak yerine parametre olarak vermektir. Gerçek bucket oluşturmak integration/end-to-end sınırına geçer; sorudaki credentials ve network istemeyen unit test şartına uymaz.

**Yakın seçenek ve sınır:** Gerçek bucketla test integration testidir. Hataları yutan try/except yanlış davranışı başarılı gösterebilir.

**Belirleyici İngilizce koşul:** `an explicit dependency boundary`

**Kaynak:** SCP18-Q25; rehber 2.3. [Ek resmî kaynak](https://docs.python.org/3/library/unittest.mock-examples.html).

---

### Soru 22

An application must process each newly finalized object in a regional Cloud Storage bucket by invoking an existing private Cloud Run service. The bucket, trigger, and service are in the same project and region. Required service-agent permissions, the trigger identity, and receiver IAM are already configured. You want direct event delivery without a polling process or an intermediate orchestration workflow. Which TWO choices complete the event route?

**Select TWO answers.**

**A.** Create an Eventarc trigger filtered for google.cloud.storage.object.v1.finalized and the source bucket, with the Cloud Run service as its destination.

**B.** Use a bucket-creation Audit Logs filter and expect it to fire for every object uploaded to the existing bucket.

**C.** Configure the handler to accept the delivered CloudEvents HTTP format and process the object information from the event.

**D.** Require the event request body to contain the complete uploaded object bytes rather than its event metadata.

**E.** Configure a Cloud Scheduler job to list the bucket on a fixed interval instead of subscribing to object events.

**İlk cevabın: A+B · Yanlış**

**Doğru cevap: A + C**

**Neden?** Object finalized event tipi ve bucket filtresi doğru olayı seçer. Eventarc HTTP CloudEvents teslim eder; handler event içindeki object bilgisini işler.

**Bilmen gereken bilgi:** `object.finalized`, nesnenin yüklenmesinin tamamlanmasıyla ilgilidir; bucket creation ayrı olaydır. CloudEvents teslimi event formatını belirtir; event içindeki object bilgisi dosyanın kendisi değildir. Yeni dosyayı işleyecek handler bu bilgiyi kullanır; empty bucket creation filtresi upload için uygun değildir.

**Yakın seçenek ve sınır:** Bucket creation farklı olaydır. Teslim edilen event tüm object baytları değildir; gerektiğinde runtime ayrı Storage okuması yapar.

**Belirleyici İngilizce koşul:** `direct event delivery without a polling process`

**Kaynak:** OFFICIAL-EVENTARC; rehber 3.1. [Ek resmî kaynak](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-storage).

---

### Soru 23

A GitOps controller applies a Deployment manifest that includes spec.replicas: 3. During peak load, the HPA correctly increases the workload to twelve replicas, but every GitOps sync resets it to three. You need GitOps to continue managing the application template while the HPA owns replica scaling. Which manifest change addresses the competing desired values?

**Select ONE answer.**

**A.** Set spec.replicas in the Deployment manifest equal to the HorizontalPodAutoscaler's maxReplicas so a sync never scales the workload below peak capacity.

**B.** Remove the spec.replicas field from the Deployment manifest so the HorizontalPodAutoscaler is the sole controller of the replica count.

**C.** Increase the HorizontalPodAutoscaler's minReplicas to match the manifest's replicas value so the two settings never disagree.

**D.** Configure the GitOps tool to ignore the Deployment resource entirely, disable the HorizontalPodAutoscaler during each deployment, and add a post-sync hook that queries Cloud Monitoring to restore the previous replica count.

**İlk cevabın: A · Yanlış**

**Doğru cevap: B**

**Neden?** Manifestte replicas desired value tutmamak GitOpsun HPA sayısını tekrar üçe çekmesini önler. Deployment template yönetimi devam eder.

**Bilmen gereken bilgi:** HPA replica sayısını değiştirirken GitOps aynı alanı sabit değere çekerse çatışırlar. Replica alanı HPA’ya bırakılmalıdır. Mevcut deployment’tan alan sahipliği geçişi ayrıca planlanır; yalnız YAML satırını silmenin geçişte etkisiz olacağı garanti değildir.

**Yakın seçenek ve sınır:** Manifesti maxReplicas yapmak yine iki controllerın aynı alanı yönetmesidir. Geçişte field ownership kontrollü taşınmalıdır.

**Belirleyici İngilizce koşul:** `while the HPA owns replica scaling`

**Kaynak:** SCP14-Q35; rehber 3.2. [Ek resmî kaynak](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).

---

### Soru 24

Many application instances perform idempotent Cloud Storage reads. During a burst, some requests return HTTP 429, and immediate synchronized retries make the throttling worse. The application already distinguishes retryable errors from invalid requests. Which retry policy should the team use for the transient failures?

**Select ONE answer.**

**A.** Immediately retry any failed request without delay, as 429 errors are typically transient and resolve quickly with the next attempt.

**B.** Use bounded exponential backoff with randomized jitter, a maximum delay, and an overall retry deadline.

**C.** Catch the 429 error and switch to a different Cloud Storage region to distribute API requests across Google's infrastructure.

**D.** Implement a fixed retry interval of 1 second between each failed request to ensure consistent spacing of API calls during rate limiting events.

**İlk cevabın: B · Doğru**

**Doğru cevap: B**

**Neden?** Bounded exponential backoff jitter ile clientların tekrarlarını dağıtır. Retry deadline sonsuz beklemeyi önler.

**Bilmen gereken bilgi:** Exponential backoff, tekrarlarda bekleme süresini artırır; jitter aynı anda hata alan client’ların tekrarlarını dağıtır. Deneme ve toplam süre sınırı sonsuz beklemeyi önler. Retry yalnız uygun geçici hatalarda ve işlemin tekrarının güvenli olduğu durumda uygulanır.

**Yakın seçenek ve sınır:** Sabit veya anında ortak retry yeniden yük patlaması yaratır. Geçersiz istek/kalıcı izin hataları bu geçici hata politikasına körlemesine sokulmaz.

**Belirleyici İngilizce koşul:** `immediate synchronized retries`

**Kaynak:** SCP15-Q25; rehber 4.2. [Ek resmî kaynak](https://docs.cloud.google.com/storage/docs/retry-strategy).

---

### Soru 25

A GKE application exports monotonically increasing HTTP request counters to Managed Service for Prometheus, with status-code labels. You need an alert when the proportion of 5xx requests exceeds 5% continuously for ten minutes. Traffic volume changes significantly during the day, so a fixed error-count threshold is unsuitable. Which approach best represents the requirement?

**Select ONE answer.**

**A.** Use a PromQL condition dividing the summed 5xx request rate by the summed total request rate, compare it with 0.05, and set a ten-minute retest duration.

**B.** Create a log-based metric that counts 5xx errors from Cloud Logging, then create a separate metric-threshold alerting policy that monitors the error count against total requests.

**C.** Export all GKE request metrics to BigQuery using a log sink, then create a scheduled query to calculate the error ratio and trigger alerts using Cloud Functions when the threshold is exceeded.

**D.** Create two separate alerting policies: one to monitor 5xx error count and another to monitor total request count, then manually correlate the alerts when both trigger simultaneously.

**İlk cevabın: A · Doğru**

**Doğru cevap: A**

**Neden?** Counterlara rate uygulanır; toplam 5xx rate / toplam request rate request ağırlıklı hata oranını verir. 0.05 üstü on dakika sürerse koşul tetiklenir.

**Bilmen gereken bilgi:** Counter, zaman içinde biriken sayıdır; `rate` bunun birim zamandaki artışını ölçer. Toplam hata rate’ini toplam istek rate’ine bölmek, request ağırlıklı oran üretir. Instance oranlarının basit ortalaması az ve çok trafik alan instance’ları eşit ağırlıklandırabilir.

**Yakın seçenek ve sınır:** Ayrı counter thresholdlar oran değildir. Farklı instance oranlarının ağırlıksız ortalaması farklı trafik hacimlerinde yanlış sonuç verir.

**Belirleyici İngilizce koşul:** `proportion of 5xx requests exceeds 5% continuously for ten minutes`

**Kaynak:** SCP16-Q58; rehber 4.3. [Ek resmî kaynak](https://docs.cloud.google.com/monitoring/alerts/using-promql).

---

## Bölüm 6

Sorular 26–30.

### Soru 26

Your v1 API is exposed through an Apigee API proxy in front of a Cloud Run service and will be retired in six months in favor of v2. While both versions remain live, you need to programmatically signal to existing client applications that v1 is deprecated and communicate the planned shutdown date. What should you do?

**Select ONE answer.**

**A.** Reduce the request quota on the v1 API product to zero so that calls to the old version are gradually throttled out.

**B.** Build a separate notification service on Cloud Run that scans Apigee analytics for v1 traffic, emails each developer whose app still calls the old version, and automatically revokes their API keys after the planned retirement date passes.

**C.** Use an AssignMessage policy on the v1 proxy to add Deprecation and Sunset response headers that indicate the retirement date.

**D.** Configure a RaiseFault policy on the v1 proxy to immediately return an HTTP 410 Gone status for all requests to that version.

**İlk cevabın: C · Doğru**

**Doğru cevap: C**

**Neden?** Mevcut v1 çalışırken response header eklemek istemciye programatik deprecation ve sunset bilgisi taşır. AssignMessage response değiştirebilir.

**Bilmen gereken bilgi:** Deprecation, sürümün bırakılacağını; Sunset, kullanımın sonlanacağı zamanı istemciye bildirmeye yarar. Mevcut endpoint çalışmaya devam ederken response header eklenebilir. `410 Gone` bugün kullanılmadığını söyler; gelecekteki kapatma tarihini duyurmakla aynı davranış değildir.

**Yakın seçenek ve sınır:** 410 veya sıfır kota gelecekteki kapatma tarihini duyurmak yerine bugün erişimi keser.

**Belirleyici İngilizce koşul:** `While both versions remain live`

**Kaynak:** SCP14-Q06; rehber 1.1. [Ek resmî kaynak](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy).

---

### Soru 27

A GKE application may run at most fifty Pods, including during rollouts. Its Cloud SQL instance permits 400 connections, and other clients may use up to fifty. Each Pod currently opens a pool of ten connections. The application uses a library with pool_size and max_overflow settings. You must stay within the existing database limit even when every pool reaches its configured maximum. Which change satisfies the connection budget?

**Select ONE answer.**

**A.** Set pool_size=7 and max_overflow=1 in every Pod and rely on retries to reserve connections for other clients.

**B.** Set pool_size=8 and max_overflow=2 in every Pod and keep the fifty-Pod maximum.

**C.** Set pool_size=5 and max_overflow=2 in every Pod, keep the fifty-Pod maximum, and use bounded retries for transient failures.

**D.** Keep pool_size=10 and increase only the connection-acquisition timeout.

**İlk cevabın: C · Doğru**

**Doğru cevap: C**

**Neden?** Pod başına azami 5+2=7, toplam 50×7=350 bağlantı; diğer clientlar 50 ile toplam 400. Bounded retry geçici hataya yardım eder.

**Bilmen gereken bilgi:** Bağlantı bütçesinde pool_size ile max_overflow birlikte sayılır. Burada Pod başına 7, en çok 50 Pod için 350; diğer client’ların 50 bağlantısıyla toplam 400’dür. Rollout sırasında ek Podlar da bütçeye dahildir; ortalama kullanım azami bağlantı hesabının yerine geçmez.

**Yakın seçenek ve sınır:** 8+2 veya 7+1 seçenekleri bütçeyi aşar. Bu yalnız verilen azami sayılar altında hesap; yeni Podlar/başka poollar ayrıca sayılır.

**Belirleyici İngilizce koşul:** `at most fifty Pods, including during rollouts`

**Kaynak:** SCP17-Q40; rehber 4.1. [Ek resmî kaynak](https://docs.cloud.google.com/sql/docs/mysql/manage-connections).

---

### Soru 28

A client is resuming a large Cloud Storage upload after a connection interruption. It still has the valid session URI and sends a status query. Cloud Storage responds with 308 Resume Incomplete and no Range header. The client must decide which byte to send next. What does this response mean, and how should the client proceed?

**Select ONE answer.**

**A.** Cloud Storage has not yet persisted any bytes. Your application should start the upload from the beginning using the same session URI.

**B.** The session URI has expired. Your application should initiate a new resumable upload to get a fresh session URI.

**C.** Cloud Storage encountered an error processing the upload. Your application should delete the session and create a new resumable upload.

**D.** The upload completed successfully. Your application should proceed to finalize the object metadata.

**İlk cevabın: A · Doğru**

**Doğru cevap: A**

**Neden?** 308 incomplete ve Range yoksa server henüz byte persist etmemiştir. Aynı geçerli session URI ile byte 0dan devam edilir.

**Bilmen gereken bilgi:** Resumable upload session URI, devam edilen upload oturumunu belirtir. `308 Resume Incomplete` yüklemenin bitmediğini söyler; varsa `Range` kalıcı alınmış byte aralığını gösterir. Sorudaki geçerli session’da Range yokluğu byte 0’dan aynı session ile devam etmeyi gerektirir, yeni session açmayı değil.

**Yakın seçenek ve sınır:** Range yokluğunu tek başına expired session veya tamamlanmış upload diye yorumlama; HTTP status ve session validity birlikte verilmiştir.

**Belirleyici İngilizce koşul:** `308 Resume Incomplete and no Range header`

**Kaynak:** SCP15-Q31; rehber 4.1. [Ek resmî kaynak](https://docs.cloud.google.com/storage/docs/performing-resumable-uploads).

---

### Soru 29

A SaaS application uses one shared Cloud Run backend. Each customer organization needs its own Identity Platform user directory and identity-provider configuration. The backend already validates tokens and enforces tenant-specific data authorization. You want managed separation of authentication configuration without deploying a separate application and Google Cloud project for every customer. What should you configure?

**Select ONE answer.**

**A.** Store all users in a single Identity Platform user pool and use Cloud Identity groups to separate organizations.

**B.** Create a dedicated Google Cloud project containing its own Identity Platform configuration for every customer organization, deploy a separate Cloud Run revision per project, and synchronize the user records across projects with a scheduled Cloud Run job so that administrators can manage their own users.

**C.** Store user credentials in Firestore documents partitioned by organization and write a custom token-issuing service.

**D.** Enable multi-tenancy in Identity Platform and create a separate tenant for each customer organization.

**İlk cevabın: D · Doğru**

**Doğru cevap: D**

**Neden?** Identity Platform tenantları kullanıcı ve provider yapılandırmalarını ayırır. Shared backend doğruladığı tenant bağlamına göre veri authorization uygulamaya devam eder.

**Bilmen gereken bilgi:** Identity Platform tenant, ayrı kullanıcı dizini ve identity-provider yapılandırması sağlayabilir. Bu authentication ayrımıdır. Ortak backend yine doğrulanmış tenant bağlamını kullanarak hangi veriye erişilebildiğini kontrol eder; tenant oluşturmak database satır yetkilerini otomatik çözmez.

**Yakın seçenek ve sınır:** Identity tenant oluşturmak veritabanındaki satır erişimini otomatik ayırmaz. Kullanıcı grubu ayrı authentication tenantı değildir.

**Belirleyici İngilizce koşul:** `its own Identity Platform user directory and identity-provider configuration`

**Kaynak:** SCP17-Q33; rehber 1.2. [Ek resmî kaynak](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy).

---

### Soru 30

A build step runs a validation tool with a documented exit-code contract: zero means success, one means an accepted nonblocking advisory, and two means a blocking validation failure. Release policy explicitly permits the advisory but must stop the build on a blocking failure. There are no other accepted nonzero exit codes. Which Cloud Build step setting implements this policy most directly?

**Select ONE answer.**

**A.** Add 'allowFailure: true' to the integration test build step to allow the build to continue regardless of the exit code returned by the tests.

**B.** Add 'script: set +e' at the beginning of the integration test build step to ignore all errors and continue the build regardless of the test results.

**C.** Add 'timeout: 60s' to the integration test build step to give flaky tests sufficient time to complete successfully before marking them as failed.

**D.** Add 'allowExitCodes: [1]' to the integration test build step to allow the build to continue when tests exit with code 1 while failing on code 2.

**İlk cevabın: D · Doğru**

**Doğru cevap: D**

**Neden?** allowExitCodes:[1] yalnız onaylı nonzero kodu kabul eder; 2 build failure olarak kalır.

**Bilmen gereken bilgi:** `allowFailure: true` geniş bir hata istisnasıdır. `allowExitCodes: [1]` yalnız belirlenen exit code’u kabul eder. Soruda code 1 onaylı advisory, code 2 gerçek failure olduğu için yalnız 1 istisna olmalıdır; başarısız testleri genel olarak susturma önerisi değildir.

**Yakın seçenek ve sınır:** allowFailure:true diğer nonzero hataları da yutar. Flaky testleri genel olarak susturma önerisi değildir; kod sözleşmesi açık verilmiştir.

**Belirleyici İngilizce koşul:** `one means an accepted nonblocking advisory`

**Kaynak:** SCP16-Q05; rehber 2.3. [Ek resmî kaynak](https://docs.cloud.google.com/build/docs/build-config-file-schema).

---

## Bölüm 7

Sorular 31–35.

### Soru 31

An AlloyDB product catalog has stable relational fields and category-specific attributes that change frequently. The application must add new attribute names without schema migrations and occasionally filter using JSON containment predicates. You want to keep the attributes in the product row and use an index that supports those predicates. Which schema choice best fits?

**Select ONE answer.**

**A.** Store products in one table with a JSONB column for the variable attributes, and create a GIN index on the JSONB column to support filtering on individual attributes.

**B.** Store the variable attributes as a single delimited text string in a VARCHAR column, and parse the string in application code whenever you need to filter on an attribute.

**C.** Model the attributes with an entity-attribute-value design that stores each attribute as a key-value row in a child table, and reconstruct each product with multiple self-joins at query time.

**D.** Create a separate table for every product category with columns for that category's attributes, define a parent products table, and join the parent and category tables through a view that UNIONs all categories whenever you query the catalog.

**İlk cevabın: A · Doğru**

**Doğru cevap: A**

**Neden?** JSONB değişken attribute yapısını aynı satırda tutar. Uygun GIN index JSON containment sorgularını destekler.

**Bilmen gereken bilgi:** PostgreSQL JSONB değişken attribute’ları saklamak için kullanılabilir. Soruda JSON containment sorguları istendiğinden uygun GIN index bu erişim biçimine uyar. JSON’u VARCHAR’a koymak aynı tip ve index davranışını sağlamaz; her JSON sorgusuna tek index’in yeterli olacağı da varsayılmaz.

**Yakın seçenek ve sınır:** Her kategoriye yeni tablo/kolon açmak migration ihtiyacını sürdürür. VARCHAR içindeki JSON metnine sıradan B-tree aynı JSON sorgu desteğini vermez.

**Belirleyici İngilizce koşul:** `filter using JSON containment predicates`

**Kaynak:** SCP16-Q31; rehber 1.3. [Ek resmî kaynak](https://www.postgresql.org/docs/current/datatype-json.html).

---

### Soru 32

Developers use Gemini Code Assist for suggestions across hundreds of private repositories. They want suggestions to reflect internal libraries and coding conventions without manually pasting examples into every request. Repository access is approved, and the organization can use an Enterprise subscription. Which managed capability should the platform team configure?

**Select ONE answer.**

**A.** Paste relevant snippets from your internal libraries into the Gemini Code Assist chat prompt each time you request a code completion.

**B.** Export all of your private repositories to a Cloud Storage bucket, train a custom fine-tuned model on the source code by using Vertex AI, and then connect the resulting model endpoint to the Gemini Code Assist plugin in each developer's IDE.

**C.** Use the Gemini Code Assist Standard edition and add your internal coding standards to a project-level style guide file.

**D.** Subscribe to Gemini Code Assist Enterprise and configure code customization to index your private repositories through Developer Connect so suggestions reflect your internal code.

**İlk cevabın: D · Doğru**

**Doğru cevap: D**

**Neden?** Enterprise code customization onaylı private repositoryleri suggestion bağlamına dahil eder. Merkezi index/repository bağlantısı gerektirir.

**Bilmen gereken bilgi:** Code customization, onaylı private repository kodunu önerilere bağlam olarak katmak için kullanılır. Bu, MCP ile dış araç çağırmaktan ve uygulamanın Gemini API ile müşteriye AI özelliği sunmasından farklıdır. Sorunun istediği merkezi repository bağlamını her prompt’a örnek yapıştırmak karşılamaz.

**Yakın seçenek ve sınır:** Prompta her seferinde snippet yapıştırmak istenen merkezi çözüm değil; sıradan completion için ayrı model fine-tuning gerekmiyor.

**Belirleyici İngilizce koşul:** `without manually pasting examples into every request`

**Kaynak:** SCP18-Q20; rehber 2.1. [Ek resmî kaynak](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

---

### Soru 33

Gemini Code Assist generated a unit test for a Python function that receives an injected Pub/Sub publisher. The function returns a confirmation value and is supposed to publish exactly one event. The current test checks only the return value, so it still passes after the publish call is accidentally removed. No real Google Cloud service should be contacted by this test. What should you ask the assistant to change?

**Select ONE answer.**

**A.** Ask Gemini Code Assist to add assertions that verify the mocked publisher was called once with the expected topic and message payload.

**B.** Ask Gemini Code Assist to deploy the function to a Cloud Run test service, create a real Pub/Sub topic and subscription, publish through the deployed service, and pull the subscription to confirm the message arrived.

**C.** Ask Gemini Code Assist to remove the publisher mock so the test exercises the real Pub/Sub client and the message is actually delivered.

**D.** Ask Gemini Code Assist to add a sleep statement after the call so the message has time to reach the real Pub/Sub topic before the assertion runs.

**İlk cevabın: A · Doğru**

**Doğru cevap: A**

**Neden?** Mock publisherın tam bir kez beklenen topic ve payload ile çağrıldığını assert etmek eksik side effecti yakalar. Gerçek function çalışır.

**Bilmen gereken bilgi:** Bir function’ın dönüş değerini kontrol etmek, gerekli dış çağrıyı yaptığını kanıtlamaz. Mock için doğru topic/payload ile tam bir kez çağrıldığını da assert etmek gerekir. Bu kontrol, publish satırı silindiğinde testi başarısız yapar; gerçek Pub/Sub bağlantısı unit test için gerekli değildir.

**Yakın seçenek ve sınır:** Gerçek Pub/Sub ile integration testi başka bir sınırdır. Sleep eklemek mock invocation eksikliğini ölçmez.

**Belirleyici İngilizce koşul:** `it still passes after the publish call is accidentally removed`

**Kaynak:** SCP15-Q06; rehber 2.3. [Ek resmî kaynak](https://docs.python.org/3/library/unittest.mock.html).

---

### Soru 34

A Java service is built in Cloud Build. Its current Docker image contains Maven, a full JDK, source files, and the runtime application. You want a reproducible build that produces a smaller final image containing only the compiled application and required runtime dependencies. The build must still compile from source in the pipeline. Which Dockerfile design should you use?

**Select ONE answer.**

**A.** Create a Dockerfile with a multi-stage build that uses a JDK image for compilation and a JRE image for the runtime stage. Configure Cloud Build to build and push the final image to Artifact Registry.

**B.** Install both JDK and JRE in a single Docker image layer and use environment variables to switch between build and runtime modes when the container starts.

**C.** Build the application locally with Maven, then create a Dockerfile that only contains the COPY instruction for the JAR file. Submit the build to Cloud Build with the pre-compiled JAR included in the source.

**D.** Create two separate Dockerfiles: one for building the JAR file and one for the runtime image. Use Cloud Build to run both sequentially and upload the intermediate artifacts to Cloud Storage between builds.

**İlk cevabın: D · Yanlış**

**Doğru cevap: A**

**Neden?** Builder stage compile eder; runtime stage yalnız gerekli JAR ve runtime dosyalarını alır. Araçlar final image katmanlarına taşınmaz.

**Bilmen gereken bilgi:** Multi-stage Dockerfile’da build stage compiler ve Maven gibi araçları kullanır; runtime stage yalnız çalışacak artifact’ı alır. `COPY --from=build` bu aktarımı yapar. Böylece JDK/build araçları final image’a taşınmaz. İki Dockerfile mümkün olsa da iki aşama arasında Storage aktarımı şart değildir.

**Yakın seçenek ve sınır:** Aynı stage içinde ortam değişkeni seçmek build araçlarını image içinden çıkarmaz. İki ayrı Dockerfile mümkün ama gereksiz artifact aktarımı ekler.

**Belirleyici İngilizce koşul:** `only the compiled application and required runtime dependencies`

**Kaynak:** SCP16-Q16; rehber 2.2. [Ek resmî kaynak](https://docs.docker.com/build/building/multi-stage/).

---

### Soru 35

A large GKE deployment uses thousands of ConfigMaps and Secrets that are versioned by name. Once created, these objects are never updated in place; a release creates new objects and replaces Pods that reference them. API-server and kubelet watch overhead is significant. Which setting fits this lifecycle and can reduce the watches while preventing accidental in-place edits?

**Select ONE answer.**

**A.** Convert all ConfigMaps and Secrets to environment variables instead of volume mounts to eliminate the need for watching files.

**B.** Increase the kubelet sync frequency interval to reduce the number of API server requests for ConfigMap and Secret updates.

**C.** Store configuration in Persistent Volumes instead of ConfigMaps and Secrets to bypass the Kubernetes API for configuration access.

**D.** Mark the ConfigMaps and Secrets that do not need updates as immutable by setting the immutable field to true.

**İlk cevabın: C · Yanlış**

**Doğru cevap: D**

**Neden?** Immutable ConfigMap/Secret güncellenmeyen nesnelerde watch ihtiyacını azaltır ve accidental in-place mutationı engeller. Yeni içerik yeni nesneyle dağıtılır.

**Bilmen gereken bilgi:** ConfigMap/Secret için `immutable: true`, data’nın yerinde değiştirilmesini engeller ve izleme yükünü azaltabilir. Sonradan immutable özelliğini kapatıp aynı nesneyi güncelleyemezsin; yeni içerik için yeni nesne oluşturulur ve workload ona geçirilir. Persistent Volume bu API nesnesi özelliğinin yerine geçmez.

**Yakın seçenek ve sınır:** Environment variablea geçirmek aynı immutable API-object özelliği değildir. Immutable nesne sonradan tekrar mutable yapılamaz.

**Belirleyici İngilizce koşul:** `never updated in place`

**Kaynak:** SCP17-Q20; rehber 3.2. [Ek resmî kaynak](https://kubernetes.io/docs/concepts/configuration/configmap/).

---

## Bölüm 8

Sorular 36–40.

### Soru 36

A public Cloud Run API is served through an external Application Load Balancer with Cloud Armor. Security requires internet clients to use that load balancer rather than bypass it through the public run.app endpoint. Approved internal callers must retain access through their current run.app URL. Which ingress setting should you choose while retaining the existing load-balancer path?

**Select ONE answer.**

**A.** Configure IAM policies on the Cloud Run service to require authentication and create a service account for the load balancer to authenticate with.

**B.** Set the Cloud Run service ingress setting to 'all' and disable the default run.app URL to force all traffic through your custom domain.

**C.** Set the Cloud Run service ingress setting to 'internal-and-cloud-load-balancing' to allow traffic only from the load balancer and VPC networks.

**D.** Configure a Cloud Armor security policy on the backend service to deny all traffic that doesn't originate from the load balancer's IP address range.

**İlk cevabın: C · Doğru**

**Doğru cevap: C**

**Neden?** internal-and-cloud-load-balancing dış internetten doğrudan run.app yolunu kapatırken external LB ve izinli internal kaynakları kabul eder.

**Bilmen gereken bilgi:** Ingress ayarı hangi ağ yollarından istek kabul edildiğini; IAM ise kimin çağırabildiğini kontrol eder. `internal-and-cloud-load-balancing`, internetten doğrudan run.app erişimini kapatırken external load balancer yolunu destekler. Cloud Armor politikası ve IAM izinleri bu ayarın otomatik sonucu değildir.

**Yakın seçenek ve sınır:** Bu ayar IAM veya Cloud Armor politikasını tanımlamaz; internal access tamamen yasaklanmış sayılmaz.

**Belirleyici İngilizce koşul:** `current run.app URL`

**Kaynak:** SCP13-Q33; rehber 3.1. [Ek resmî kaynak](https://docs.cloud.google.com/run/docs/securing/ingress).

---

### Soru 37

An AlloyDB application stores millions of product embeddings in a supported vector column. Required extensions can be enabled, and the team accepts approximate nearest-neighbor results in exchange for lower query latency. The search must execute in AlloyDB alongside the product data, without transferring every vector to the application. Which indexing approach should you use?

**Select ONE answer.**

**A.** Store the embeddings in a JSONB column and rely on a standard B-tree index to speed up the nearest-neighbor searches.

**B.** Export the product rows to BigQuery, compute embeddings with a SQL model, store the vectors in a separate BigQuery table, and have the application query BigQuery for every similarity lookup before joining the results back to AlloyDB.

**C.** Store the embeddings in a vector column and create a ScaNN index on that column to accelerate approximate nearest-neighbor queries.

**D.** Store the embeddings as comma-separated text in a standard VARCHAR column, and compute the distances in the application after fetching all rows.

**İlk cevabın: C · Doğru**

**Doğru cevap: C**

**Neden?** Vector alanındaki embeddingler için ScaNN approximate nearest-neighbor index uygundur; sorgu veritabanında yürür. İlgili extensionlar gerekir.

**Bilmen gereken bilgi:** Embedding, içeriğin sayısal vektör temsilidir; benzerlik vector distance üzerinden ölçülür. AlloyDB’de sorudaki approximate nearest-neighbor araması için ScaNN index uygundur. Exact en yakın sonucu garanti etmez; B-tree/JSONB index aynı vector arama mekanizması değildir.

**Yakın seçenek ve sınır:** B-tree/JSONB yapıları bu vector distance aramasının yerine geçmez. Approximate sonuç exact nearest-neighbor garantisi değildir.

**Belirleyici İngilizce koşul:** `accepts approximate nearest-neighbor results`

**Kaynak:** SCP17-Q05; rehber 1.3. [Ek resmî kaynak](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index).

---

### Soru 38

You are migrating a table from a legacy system into Cloud Spanner. The table's primary key is a sequential, monotonically increasing customer number, and load testing shows that nearly all inserts land on the same split, creating a write hotspot. You must continue to look up rows by the customer number while distributing inserts evenly across the key space. What should you do?

**Select ONE answer.**

**A.** Increase the number of processing units so that Spanner can add more splits to absorb the concentrated insert traffic.

**B.** Place a Cloud Tasks queue in front of the database, configure a fixed dispatch rate with exponential backoff, and have a worker drain the queue so that the monotonically increasing inserts are spread out over time before they reach Spanner.

**C.** Compute a hash of the customer number and use that hash value as the leading column of the primary key, keeping the customer number as the next key column.

**D.** Create a secondary index on the customer number column so that inserts are distributed across the index instead of the base table.

**İlk cevabın: C · Doğru**

**Doğru cevap: C**

**Neden?** Deterministik hash öneki monoton customer numaralarının yazılarını dağıtır; müşteri numarası ikinci key parçası olarak korunur. Lookup sırasında hash hesaplanabilir.

**Bilmen gereken bilgi:** Spanner primary key’nin başlangıcında sürekli artan ID bulunması yazıları yakın key aralıklarında yoğunlaştırabilir. ID’den deterministik hash üretip öne koymak farklı ID’lerin yazılarını dağıtır; lookup sırasında aynı hash yeniden hesaplanabilir. Tek bir çok sıcak kullanıcıya aynı hash’i vermek o kullanıcının yükünü parçalamaz.

**Yakın seçenek ve sınır:** Secondary index base-table hotspotunu ortadan kaldırmaz. Bu senaryo çok sayıda farklı ID içindir; tek hot user için aynı user hash yeterli olmaz.

**Belirleyici İngilizce koşul:** `must continue to look up rows by the customer number`

**Kaynak:** SCP16-Q53; rehber 1.3. [Ek resmî kaynak](https://docs.cloud.google.com/spanner/docs/schema-design).

---

### Soru 39

A workload in project A inside perimeter A must read one BigQuery dataset in project B inside perimeter B. IAM permissions are already correct. Security requires narrowly scoped access for the named caller and the required BigQuery operations, without joining the perimeters through a broadly permissive bridge. Both perimeters must remain enforced. Which TWO VPC Service Controls configurations are required?

**Select TWO answers.**

**A.** Add an ingress rule to perimeter B allowing the required identity and operations from the permitted source.

**B.** Add only an ingress rule to perimeter B; a destination rule automatically overrides every source-perimeter egress restriction.

**C.** Grant BigQuery Data Viewer again and leave both perimeter policies unchanged.

**D.** Add an egress rule to perimeter A allowing the required identity and operations against the destination resources.

**E.** Add only an egress rule to perimeter A; a source rule automatically overrides every destination-perimeter ingress restriction.

**İlk cevabın: A+D · Doğru**

**Doğru cevap: A + D**

**Neden?** Çağrı iki perimeter sınırını geçer: kaynakta izinli egress, hedefte izinli ingress gerekir. IAM izni ayrıca zaten sağlanmıştır.

**Bilmen gereken bilgi:** VPC Service Controls ve IAM ayrı sınırlar koyar. İki farklı perimeter arasında işlem için kaynak tarafındaki egress ve hedef tarafındaki ingress değerlendirmeleri birlikte karşılanmalıdır. IAM izni olması perimeter geçişini otomatik açmaz; bir taraftaki kural diğer tarafın yerine geçmez.

**Yakın seçenek ve sınır:** Bir sınırdaki izin diğer sınırı geçersiz kılmaz. Dar kapsam şartı geniş bir perimeter bridge alternatifini eler.

**Belirleyici İngilizce koşul:** `Both perimeters must remain enforced`

**Kaynak:** SCP15-Q10; rehber 1.2. [Ek resmî kaynak](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

---

### Soru 40

A GKE Ingress uses a load-balancer health check that requests the wrong path. Pod readiness probes pass, and the application has a verified /health endpoint. You need to set the backend load-balancer health-check path and timeout declaratively through GKE, rather than editing the generated cloud resource manually. Which resource and association should you configure?

**Select ONE answer.**

**A.** Create a BackendConfig custom resource with a healthCheck section and reference it in the Service using the cloud.google.com/backend-config annotation.

**B.** Update the Ingress resource with a kubernetes.io/ingress.health-check annotation specifying the health check path, port, and thresholds.

**C.** Create a FrontendConfig custom resource with healthCheck parameters and add the networking.gke.io/v1beta1.FrontendConfig annotation to your Ingress manifest.

**D.** Modify the Pod readiness probe configuration to match the expected load balancer health check path and interval settings.

**İlk cevabın: D · Yanlış**

**Doğru cevap: A**

**Neden?** BackendConfig healthCheck ayarlarını Service üzerindeki backend-config annotationıyla bağlar. GKE generated health checki bu kaynaktan yönetir.

**Bilmen gereken bilgi:** Readiness probe Pod’un trafik almaya hazır olduğunu kontrol eder; load balancer health check farklı kontroldür. GKE Ingress için BackendConfig healthCheck alanı Service’e annotation ile bağlanır. Mevcut LB health check’inin yalnız readiness probe düzenlenince güncelleneceğini varsayma.

**Yakın seçenek ve sınır:** FrontendConfig bu backend health-check ayarının yeri değildir. Var olan LB checkini yalnız readiness probe değiştirerek güncelleme garantisi yoktur.

**Belirleyici İngilizce koşul:** `declaratively through GKE`

**Kaynak:** SCP14-Q55; rehber 3.2. [Ek resmî kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration).

---

## Bölüm 9

Sorular 41–45.

### Soru 41

A Cloud Build pipeline builds a uniquely tagged image and then deploys it within the same build. The image must exist in Artifact Registry before the deployment step starts, and it must also appear as an output on the Cloud Build results page. Building alone currently leaves it local to the worker. Which TWO configuration elements address these requirements?

**Select TWO answers.**

**A.** Use a mutable latest tag so deployment can locate an image that has never been pushed.

**B.** Grant Artifact Registry Reader to the application runtime identity instead of uploading the image.

**C.** Use only the images field and start deployment before the end-of-build image upload.

**D.** Add an explicit Docker push step and make the deployment step wait for that push.

**E.** List the image under the top-level images field so it is recorded as a build output.

**İlk cevabın: D+E · Doğru**

**Doğru cevap: D + E**

**Neden?** Push deployment adımından önce registryde image bulunmasını sağlar. images alanı ayrıca build output kaydını oluşturur.

**Bilmen gereken bilgi:** Cloud Build içindeki deploy adımı başlamadan önce image registry’de bulunmalıdır; explicit push ve waitFor bu sırayı kurar. Top-level `images` alanı image’ı build çıktısı olarak kaydeder ve build sonunda yükleme akışına katılır. Bu alan, daha önce çalışan deploy adımına otomatik push-before-deploy garantisi değildir.

**Yakın seçenek ve sınır:** images son build çıktısı olarak upload sağlar; build içinde daha erken çalışan deploy için tek başına yeterli sıralama garantisi değildir.

**Belirleyici İngilizce koşul:** `before the deployment step starts`

**Kaynak:** SCP16-Q02; rehber 2.2. [Ek resmî kaynak](https://docs.cloud.google.com/build/docs/building/build-containers).

---

### Soru 42

Cloud Code in IntelliJ successfully attaches to a Node.js process in a development Kubernetes cluster. The debugger can pause the process, and the debug port is reachable, but local breakpoints remain unbound. The current source files are present in the container under /workspace/app, while local files are under a different directory. The image is confirmed to contain the latest code. What should you correct first?

**Select ONE answer.**

**A.** Modify your Dockerfile to include the --inspect flag in the Node.js startup command and expose port 9229.

**B.** Configure the source mapping in the Debug tab of the Run configuration to map local source paths to remote container paths.

**C.** Add a debugger statement to your Node.js code and rebuild the container to force the debugger to pause execution.

**D.** Install the Node.js debugging extension separately in IntelliJ and configure it to connect to port 9229 on the container.

**İlk cevabın: B · Doğru**

**Doğru cevap: B**

**Neden?** Debugger bağlı olduğundan sorun bağlantı değil, yerel kaynak ile container path eşlemesidir. Source mapping breakpointi yürüyen dosyaya bağlar.

**Bilmen gereken bilgi:** Debugger bağlantısının çalışması, breakpoint’in yürüyen dosyayla eşleştiği anlamına gelmez. Laptop’taki kaynak yolu ile container’daki yol farklıysa source mapping gerekir. Bağlantı ve doğru image zaten doğrulanmışsa port açmak veya tekrar build yapmak öncelikli çözüm değildir.

**Yakın seçenek ve sınır:** Port açmak zaten çalışan bağlantıyı düzeltmez; eski image olasılığı da kökte elenmiştir.

**Belirleyici İngilizce koşul:** `local breakpoints remain unbound`

**Kaynak:** SCP17-Q23; rehber 2.1. [Ek resmî kaynak](https://docs.cloud.google.com/code/docs/intellij/debug).

---

### Soru 43

A GKE workload uses Workload Identity Federation and has correct IAM permissions. Immediately after Pod creation, its short-timeout startup call sometimes fails because the metadata server is not yet ready; the same call succeeds seconds later. The application exits on that first failure, and code changes are not currently possible. Which startup configuration handles this transient dependency while preserving the workload identity?

**Select ONE answer.**

**A.** Store a service account key as a Kubernetes Secret and mount it to the pod for immediate authentication without waiting for the metadata server.

**B.** Deploy an initContainer in your pod specification that waits until the GKE metadata server is ready before the main container starts.

**C.** Configure the pod with hostNetwork: true to bypass the GKE metadata server and authenticate directly using the node identity.

**D.** Disable Workload Identity Federation for GKE on the node pool and use the node service account instead for faster authentication.

**İlk cevabın: B · Doğru**

**Doğru cevap: B**

**Neden?** Metadata server hazır olana kadar bekleyen initContainer ana uygulamanın erken authentication hatasıyla çıkmasını önler. WIF ve dar IAM korunur.

**Bilmen gereken bilgi:** Pod başlarken GKE metadata server henüz hazır olmayabilir. Soruda aynı çağrının birkaç saniye sonra çalışması kalıcı IAM eksikliğinden farklı bir startup sinyalidir. Metadata hazır olana kadar bekleyen initContainer ana uygulamayı bu bağımlılıktan sonra başlatır; servis hesabı key’i dağıtmak gerekmez.

**Yakın seçenek ve sınır:** SA key dosyası dağıtmak veya node identityye geçmek gerekli değil; kalıcı izin eksikliği olmadığı kanıtlanmış.

**Belirleyici İngilizce koşul:** `the same call succeeds seconds later`

**Kaynak:** SCP16-Q06; rehber 3.2. [Ek resmî kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/authentication).

---

### Soru 44

Production deployments refer to version tags in an Artifact Registry Docker repository. An incident occurred when a permitted writer moved an existing release tag to a different digest. The team must keep using version tags and allow new releases to be pushed, but it wants the repository to enforce that an existing tag cannot be reassigned. What should you enable?

**Select ONE answer.**

**A.** Implement a naming convention that appends timestamps to all image tags and document the policy for your team to follow consistently.

**B.** Create a Cloud Build trigger that validates tag uniqueness before pushing images. Fail the build if the tag already exists in the repository.

**C.** Configure IAM policies to grant the Artifact Registry Writer role only to the CI/CD service account and remove push permissions from individual developers.

**D.** Enable the immutable tags setting on the Docker repository in Artifact Registry to prevent changing the image digest that a tag references.

**İlk cevabın: D · Doğru**

**Doğru cevap: D**

**Neden?** Immutable tags repo düzeyinde mevcut tagın başka digest ile değiştirilmesini engeller; yeni taglara izin verilebilir.

**Bilmen gereken bilgi:** Tag okunabilir isimdir, digest image içeriğini tanımlar. Repository’de immutable tags etkinse mevcut tag farklı digest’e taşınamaz. CI’ın tek writer olması yetkili operatörün yanlış tag overwrite yapmasını tek başına engellemez; repository enforcement farklı katmandır.

**Yakın seçenek ve sınır:** İsim kuralı veya yalnız CI writer yetkisi operatör hatasına karşı aynı repository enforcementını sağlamaz.

**Belirleyici İngilizce koşul:** `the repository to enforce`

**Kaynak:** SCP15-Q26; rehber 2.2. [Ek resmî kaynak](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images).

---

### Soru 45

A Firestore chat client adds a snapshot listener whenever a user opens a room. After switching rooms several times, it receives callbacks from both current and previous rooms and displays duplicate updates. Database records are not duplicated, and security rules are working. How should the client manage listeners so only the active room remains subscribed?

**Select ONE answer.**

**A.** Configure your Firestore security rules to only allow one active listener per user per collection to prevent duplicate subscriptions.

**B.** Store the unsubscribe function returned by onSnapshot() and call it before creating a new listener when users switch chat rooms.

**C.** Implement a client-side deduplication function that filters out duplicate messages based on document ID before displaying them in the UI.

**D.** Restart the Firestore client instance each time the user switches chat rooms to ensure only one listener is active at a time.

**İlk cevabın: C · Yanlış**

**Doğru cevap: B**

**Neden?** onSnapshotın döndürdüğü unsubscribe eski room listenerını kapatır; ardından yeni room listenerı oluşturulur.

**Bilmen gereken bilgi:** `onSnapshot` gerçek zamanlı bir listener açar ve onu kapatmak için unsubscribe işlevi döndürür. Oda değişiminde eski listener açık kalırsa birden fazla callback akışı oluşabilir. UI’da duplicate kayıtları gizlemek eski listener’ı kapatmaz; yaşam döngüsü temizliği gerekir.

**Yakın seçenek ve sınır:** UI dedup eski subscriptionları ve gereksiz callbackleri ortadan kaldırmaz; security rules listener yaşam döngüsü yöneticisi değildir.

**Belirleyici İngilizce koşul:** `Database records are not duplicated`

**Kaynak:** SCP18-Q05; rehber 4.1. [Ek resmî kaynak](https://firebase.google.com/docs/firestore/query-data/listen).

---

## Bölüm 10

Sorular 46–50.

### Soru 46

A manifest works on a GKE Standard node pool with Workload Identity Federation enabled. The team is moving it to Autopilot, where its iam.gke.io/gke-metadata-server-enabled: "true" nodeSelector is rejected. The Kubernetes service account and its IAM access are already correctly configured. What should you do to retain workload authentication on Autopilot?

**Select ONE answer.**

**A.** Add an annotation to the pod specification to explicitly enable Workload Identity Federation for GKE because Autopilot requires explicit opt-in for each workload.

**B.** Keep the nodeSelector in the pod specification to ensure the pod is scheduled on nodes with the GKE metadata server enabled.

**C.** Remove the nodeSelector from the pod specification because Autopilot clusters always have Workload Identity Federation for GKE enabled and will reject pods with this nodeSelector.

**D.** Convert the Autopilot cluster to a Standard cluster because Workload Identity Federation for GKE configuration requires manual node pool management that is not available in Autopilot.

**İlk cevabın: B · Yanlış**

**Doğru cevap: C**

**Neden?** Autopilotta WIF tüm nodelarda hazırdır; Standard için kullanılan metadata-server nodeSelector kaldırılır. KSA/IAM bağlantısı korunur.

**Bilmen gereken bilgi:** Autopilot’ta Workload Identity Federation for GKE hazırdır. Standard’daki metadata-server nodeSelector’ı Autopilot’a taşımak gerekmez ve bu selector kabul edilmez. Selector kaldırılması workload’un kaynak IAM izinlerini kaldırmak demek değildir; KSA/yetki düzeni korunur.

**Yakın seçenek ve sınır:** Autopilot için Pod bazında WIF enable annotationı gerekmez; Standarda dönmek gereksizdir.

**Belirleyici İngilizce koşul:** `its IAM access are already correctly configured`

**Kaynak:** SCP16-Q40; rehber 3.2. [Ek resmî kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

---

### Soru 47

Each GKE Pod contains an application container and a logging sidecar. Sidecar CPU spikes cause a Pod-level CPU HPA to add replicas while the application is idle. Both containers have valid resource requests, and the cluster supports autoscaling/v2 container resource metrics. You want CPU scaling to follow only the application container while preserving the sidecar in the same Pod. What should you configure?

**Select ONE answer.**

**A.** Lower the sidecar's CPU request to zero so it is excluded from the Pod-level Resource metric calculation.

**B.** Switch the HorizontalPodAutoscaler to a memory Resource metric, because Pod-level memory excludes sidecar container usage.

**C.** Move the logging sidecar into its own Deployment with a separate HorizontalPodAutoscaler, then set static CPU limits on the application container so the original Pod-level Resource metric no longer counts the sidecar's CPU when computing the scaling ratio.

**D.** Configure the HorizontalPodAutoscaler with a ContainerResource metric that targets the CPU utilization of the application container only.

**İlk cevabın: C · Yanlış**

**Doğru cevap: D**

**Neden?** ContainerResource metriği yalnız adı belirtilen application containerın CPU kullanımını izler. Sidecar Pod içinde kalır.

**Bilmen gereken bilgi:** Pod `Resource` metriği ile belirli container’ı izleyen `ContainerResource` farklıdır. `container: application` yalnız uygulama CPU’sunu hedefler. Sidecar’ı Pod’da tutarak ölçekleme hesabından ayırabilirsin; container adı doğru eşleşmelidir.

**Yakın seçenek ve sınır:** Pod Resource metriğinde sidecarı requestini sıfırlayarak güvenli biçimde çıkaramazsın; eksik request ölçümü bozabilir.

**Belirleyici İngilizce koşul:** `only the application container`

**Kaynak:** SCP17-Q54; rehber 3.2. [Ek resmî kaynak](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).

---

### Soru 48

A product API repeatedly reads a small, popular subset of a Cloud SQL catalog. The database must remain authoritative, and a short period of stale display data is acceptable. You want to add Redis incrementally, without preloading every product or treating cache loss as permanent data loss. Which pattern best reduces database reads while providing a way to refresh values after product updates?

**Select ONE answer.**

**A.** Implement a write-through pattern where every database read operation writes directly to Memorystore, and use the noeviction maxmemory policy to retain all cached data indefinitely without expiration.

**B.** Configure Cloud SQL to automatically sync all table rows to Memorystore using database triggers, and enable the allkeys-random eviction policy to randomly remove keys when memory pressure occurs.

**C.** Store product data exclusively in Memorystore without Cloud SQL backup, and configure RDB snapshots for persistence to ensure data durability across instance restarts.

**D.** Implement a cache-aside pattern where your application checks Memorystore first, queries Cloud SQL on cache miss, and writes the result to cache with a TTL. When product data is updated, invalidate the corresponding cache key.

**İlk cevabın: D · Doğru**

**Doğru cevap: D**

**Neden?** Cache-aside önce cache okur; miss olunca kaynak veriyi okuyup cache doldurur. TTL ve update invalidation ile kabul edilen staleness yönetilir.

**Bilmen gereken bilgi:** Cache-aside: önce cache oku; miss olursa database’den alıp cache’e koy. Database authoritative kalır; TTL ve değişiklikte invalidation kabul edilen bayatlığı yönetir. Cache ile SQL arasında otomatik atomik transaction garantisi yoktur.

**Yakın seçenek ve sınır:** Bu bir SQL/Redis atomik transaction garantisi değildir. Redis tek veri kaynağı yapılırsa eviction kalıcı kayıp yaratabilir.

**Belirleyici İngilizce koşul:** `The database must remain authoritative`

**Kaynak:** SCP16-Q27; rehber 1.1. [Ek resmî kaynak](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview).

---

### Soru 49

NetworkPolicy enforcement is enabled on a GKE cluster. A new payments namespace contains Pods with no existing egress policies. Security requires a default posture in which those Pods can initiate no outbound connections until specific destinations are approved. Required DNS and application destinations will be allowed separately. Which configuration establishes the requested namespace baseline?

**Select ONE answer.**

**A.** Create a single broad NetworkPolicy in the 'payments' namespace that lists every approved destination as an allow rule and sets a final rule denying all other egress traffic so the ordering guarantees a deny for anything not explicitly matched first.

**B.** Configure firewall rules in the VPC network to block egress from the nodes that run 'payments' Pods.

**C.** Apply a default-deny egress NetworkPolicy to the 'payments' namespace, then add NetworkPolicies that explicitly allow egress only to the required destinations.

**D.** Apply an ingress-only default-deny NetworkPolicy to the 'payments' namespace to restrict the Pods' traffic.

**İlk cevabın: A · Yanlış**

**Doğru cevap: C**

**Neden?** Tüm namespace Podlarını seçen default-deny egress politikası outbound başlangıcını kapatır. Sonra gerekli DNS ve servis yolları ayrı allow politikalarıyla eklenir.

**Bilmen gereken bilgi:** NetworkPolicy, sırayla işleyen allow/son deny firewall listesi değildir; izinler birleşir. Default-deny egress ile başlangıç izolasyonu sağlanır, gereken çıkışlar ayrı allow politikalarıyla açılır. DNS gibi gerekli yollar da düşünülür. Bir ingress politikası tek başına egress’i kapatmaz.

**Yakın seçenek ve sınır:** NetworkPolicy sıralı firewall kural listesi değildir; ingress-only politika outbound trafiği kapatmaz.

**Belirleyici İngilizce koşul:** `can initiate no outbound connections until specific destinations are approved`

**Kaynak:** SCP18-Q07; rehber 1.2. [Ek resmî kaynak](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

---

### Soru 50

A local application uses valid user ADC to call a client-based Google Cloud API. The intended quota project has the API enabled, and the user already has serviceusage.services.use there. A diagnostic identifies that no quota project is set in the local ADC configuration. Resource permissions are also correct. Which command should the developer use to address the missing configuration?

**Select ONE answer.**

**A.** Grant the Service Usage Consumer role (roles/serviceusage.serviceUsageConsumer) to your user account and run 'gcloud auth application-default login' again.

**B.** Run 'gcloud auth application-default set-quota-project PROJECT_ID' to specify the project for billing and quota.

**C.** Delete the local ADC file and use the gcloud CLI credentials directly.

**D.** Set GOOGLE_APPLICATION_CREDENTIALS to point to a service account key file instead.

**İlk cevabın: A · Yanlış**

**Doğru cevap: B**

**Neden?** ADC quota project ayarı doğru consumer projeyi seçer. Kullanıcı kimliği ve resource izinleri değişmeden kalır.

**Bilmen gereken bilgi:** Resource project, kimlik ve quota project aynı kavram değildir. Lokal user ADC’de eksik quota project `gcloud auth application-default set-quota-project PROJECT_ID` ile seçilir. Bu işlem kullanıcı kimliğini değiştirmez. Soruda Service Usage Consumer izni zaten var; aynı rolü tekrar vermek teşhis edilen ayar boşluğunu kapatmaz.

**Yakın seçenek ve sınır:** gcloud varsayılan projecti değiştirmek yerel ADC quota projecti ayarlamakla aynı işlem değildir; serviceusage izni zaten mevcut.

**Belirleyici İngilizce koşul:** `no quota project is set`

**Kaynak:** SCP17-Q44; rehber 4.2. [Ek resmî kaynak](https://docs.cloud.google.com/docs/quotas/set-quota-project).

---
