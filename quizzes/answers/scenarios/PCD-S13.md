# PCD-S13 — Türkçe cevap anahtarı ve kaynak eşlemesi

**İlk denemeden önce açma: doğru cevapları içerir.**

5 Ekim 2026. 49 SkillCertPro uyarlaması + 1 resmî Eventarc tamamlayıcısı. Rehber dağılımı 16/12/12/10; 47 tek + 3 çift seçim. Her soru 1 puan; çift seçimde tam küme gerekir. Platformdaki kaynak anahtarı son otorite sayılmadı. İlk kullanıcı cevapları sonradan açıklanan doğru cevaplarla değiştirilmeyecek.

Kaynak sorular yerel `skillcertpro-questions.json` içinde SCPxx-Qyy kimliğiyle korunur. Buradaki resmî kaynaklar PDF ders notlarına ek web kaynaklarıdır. Çalışan cloud kaynakları üzerinde laboratuvar testi yapılmadı; teknik kararlar doküman ve senaryo koşullarıyla kontrol edildi. Benzer eski kararlar bilinçli pekiştirme/karma olarak listelenir; hiçbir soru yalnız hazırlanmış olduğu için öğrenilmiş sayılmaz.

| Soru | Cevap | Rehber | Kaynak |
|---|---|---|---|
| 1 | C | 2.2 | SCP14-Q20 |
| 2 | A | 2.1 | SCP17-Q07 |
| 3 | B | 3.1 | SCP16-Q60 |
| 4 | C | 4.2 | SCP13-Q06 |
| 5 | A | 2.1 | SCP14-Q51 |
| 6 | D | 4.3 | SCP17-Q51 |
| 7 | D | 1.2 | SCP14-Q58 |
| 8 | A | 3.1 | SCP14-Q60 |
| 9 | B | 1.1 | SCP14-Q17 |
| 10 | C | 1.1 | SCP15-Q09 |
| 11 | B | 3.2 | SCP14-Q23 |
| 12 | D | 3.1 | SCP16-Q22 |
| 13 | A | 4.3 | SCP15-Q05 |
| 14 | B | 1.3 | SCP16-Q19 |
| 15 | B | 1.1 | SCP14-Q27 |
| 16 | A | 4.3 | SCP15-Q12 |
| 17 | D | 1.3 | SCP14-Q19 |
| 18 | A | 1.3 | SCP14-Q52 |
| 19 | C | 1.2 | SCP18-Q26 |
| 20 | C | 2.1 | SCP14-Q50 |
| 21 | B | 2.3 | SCP18-Q25 |
| 22 | A + C | 3.1 | OFFICIAL-EVENTARC |
| 23 | B | 3.2 | SCP14-Q35 |
| 24 | B | 4.2 | SCP15-Q25 |
| 25 | A | 4.3 | SCP16-Q58 |
| 26 | C | 1.1 | SCP14-Q06 |
| 27 | C | 4.1 | SCP17-Q40 |
| 28 | A | 4.1 | SCP15-Q31 |
| 29 | D | 1.2 | SCP17-Q33 |
| 30 | D | 2.3 | SCP16-Q05 |
| 31 | A | 1.3 | SCP16-Q31 |
| 32 | D | 2.1 | SCP18-Q20 |
| 33 | A | 2.3 | SCP15-Q06 |
| 34 | A | 2.2 | SCP16-Q16 |
| 35 | D | 3.2 | SCP17-Q20 |
| 36 | C | 3.1 | SCP13-Q33 |
| 37 | C | 1.3 | SCP17-Q05 |
| 38 | C | 1.3 | SCP16-Q53 |
| 39 | A + D | 1.2 | SCP15-Q10 |
| 40 | A | 3.2 | SCP14-Q55 |
| 41 | D + E | 2.2 | SCP16-Q02 |
| 42 | B | 2.1 | SCP17-Q23 |
| 43 | B | 3.2 | SCP16-Q06 |
| 44 | D | 2.2 | SCP15-Q26 |
| 45 | B | 4.1 | SCP18-Q05 |
| 46 | C | 3.2 | SCP16-Q40 |
| 47 | D | 3.2 | SCP17-Q54 |
| 48 | D | 1.1 | SCP16-Q27 |
| 49 | C | 1.2 | SCP18-Q07 |
| 50 | B | 4.2 | SCP17-Q44 |

## Q01 — C

**Karar:** İlk lint adımı başlar; unit-test waitFor:[-] ile bağımsız başlar. Integration iki IDye bağlı olduğu için ikisinin başarıyla bitmesini bekler.

**Yakın seçenek ve sınır:** Üçüne de [-] vermek gatei kaldırır; waitFor olmadan default sıra paralellik sağlamaz. Uzun yaşayan DB readiness bu sorunun konusu değildir.

**Belirleyici İngilizce koşul:** `only after both checks succeed`

**Doğru seçenek metni:** Configure the lint step with id: 'lint', unit test step with id: 'unit-test' and waitFor: ['-'], and the integration test step with waitFor: ['lint', 'unit-test'].

**Kaynak:** SCP14-Q20; rehber 2.2. [Ek resmî kaynak](https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order).

**Önceki ilişki:** S11-06 / S04-02; bilinçli pekiştirme.

## Q02 — A

**Karar:** Skaffold manual sync kuralları eşleşen dosyaları container hedef yoluna taşır. Static server yeni içeriği diskten okuyabilir.

**Yakın seçenek ve sınır:** watch değişiklik algılar; hangi dosyanın image rebuild yerine sync edileceğini tek başına tanımlamaz.

**Belirleyici İngilizce koşul:** `serve changed files directly from disk`

**Doğru seçenek metni:** Add a sync section with manual rules specifying source HTML files and their destination paths in the container for the artifact you want to configure.

**Kaynak:** SCP17-Q07; rehber 2.1. [Ek resmî kaynak](https://skaffold.dev/docs/filesync/).

**Önceki ilişki:** S10-14; karma, rebuild yerine file sync.

## Q03 — B

**Karar:** Cloud Deploy automated canary ile trafik aşamalarını yönetir. Ara yüzdeler 10/25/50; son stable phase 100e tamamlar.

**Yakın seçenek ve sınır:** standard strategy + özel hook çalışabilir ama istenen native traffic control değildir. Bu mevcut stable revisionlı rollout; ilk deploy farklı davranabilir.

**Belirleyici İngilizce koşul:** `rather than running custom traffic commands in hooks`

**Doğru seçenek metni:** Use strategy.canary with runtimeConfig.cloudRun.automaticTrafficControl: true and canaryDeployment.percentages: [10, 25, 50].

**Kaynak:** SCP16-Q60; rehber 3.1. [Ek resmî kaynak](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run).

**Önceki ilişki:** S12-44; karma, Cloud Deploy automation.

## Q04 — C

**Karar:** fields seçimi item name/size ile nextPageTokenı birlikte korumalıdır. Sonraki requestte token pageToken olarak gönderilir.

**Yakın seçenek ve sınır:** Sadece object alanlarını tutmak pagination bilgisini düşürebilir; daha büyük tek sayfa bütün listeyi garanti etmez.

**Belirleyici İngilizce koşul:** `Listing requires multiple pages`

**Doğru seçenek metni:** Add the fields query parameter to specify only the required object properties and include nextPageToken and items fields to preserve pagination capability.

**Kaynak:** SCP13-Q06; rehber 4.2. [Ek resmî kaynak](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters).

**Önceki ilişki:** S11-29; bilinçli pekiştirme.

## Q05 — A

**Karar:** Agent mode içinde MCP serverlar dış araçları tanıtır. Tracker ve özel doküman servisine kontrollü araç erişimi bu mekanizmayla sağlanır.

**Yakın seçenek ve sınır:** Code customization repository bağlamı sunar; herhangi bir harici sistemde işlem yapan araç entegrasyonunun yerine geçmez.

**Belirleyici İngilizce koşul:** `external project tracker and your private API documentation service`

**Doğru seçenek metni:** Enable Gemini Code Assist agent mode and configure Model Context Protocol (MCP) servers for the external services in the Gemini settings so the agent can discover and call those tools.

**Kaynak:** SCP14-Q51; rehber 2.1. [Ek resmî kaynak](https://docs.cloud.google.com/gemini/docs/codeassist/agent-mode).

**Önceki ilişki:** S06-06 / S08-27; bilinçli pekiştirme.

## Q06 — D

**Karar:** Bucket-scoped metric merkezi bucketta gelen kayıtları kaynak projelerinden bağımsız değerlendirir. Metric bucketın bulunduğu projede tanımlanır.

**Yakın seçenek ve sınır:** Central project-scoped metric varsayımı ile routed bucket kapsamı aynı değildir. Folder düzeyinde log metric yaratılmaz.

**Belirleyici İngilizce koşul:** `including entries originating in other projects`

**Doğru seçenek metni:** Create bucket-scoped log-based metrics in the project containing the central log bucket. Configure filters to match error logs from all source projects routed to the bucket.

**Kaynak:** SCP17-Q51; rehber 4.3. [Ek resmî kaynak](https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm).

**Önceki ilişki:** S12-10 / S10-15; merkezi ölçüm kapsamı.

## Q07 — D

**Karar:** Delayed destruction sürümü önce disabled yapıp kalıcı yok etmeyi ayarlanan süre sonrasına bırakır. Böylece native recovery penceresi oluşur.

**Yakın seçenek ve sınır:** Rotation yeni credential üretim süreciyle, expiration ise başka yaşam döngüsüyle ilgilidir; geri dönüşsüz destroy sonrası bildirim veriyi geri getirmez.

**Belirleyici İngilizce koşul:** `a built-in seven-day recovery window`

**Doğru seçenek metni:** Enable the delay secret version destroy feature on the secret and set the destruction delay duration to 7 days or more.

**Kaynak:** SCP14-Q58; rehber 1.2. [Ek resmî kaynak](https://docs.cloud.google.com/secret-manager/docs/delay-destruction-of-secret-versions).

**Önceki ilişki:** S11-13/31 ile ilişkili; Secret Manager version yaşam döngüsü.

## Q08 — A

**Karar:** Native secret environment variable yeni instance başlamadan çözümlenir. Erişilemeyen secretla instance startup başarısız olur. Pinned version belirli değeri seçer.

**Yakın seçenek ve sınır:** Volume okuması runtime erişim yoludur; mevcut legacy env okuyucuyu kod değişmeden beslemez.

**Belirleyici İngilizce koşul:** `without changing application code`

**Doğru seçenek metni:** Configure the secret as an environment variable in the Cloud Run service configuration.

**Kaynak:** SCP14-Q60; rehber 3.1. [Ek resmî kaynak](https://docs.cloud.google.com/run/docs/configuring/services/secrets).

**Önceki ilişki:** S11-12; bilinçli pekiştirme.

## Q09 — B

**Karar:** Queue retry config yeniden denemeleri yönetir. maxAttempts ilk çağrıyı da sayar; burada süre sınırı sıfır olduğundan beş toplam deneme hedefi açıktır.

**Yakın seçenek ve sınır:** Dispatch rate ile retry sayısı farklıdır. Backoff doubling sonrası doğrusal artabilir; kaynak açıklamasındaki eksik aralık örneği kullanılmadı.

**Belirleyici İngilizce koşul:** `maxRetryDuration is zero`

**Doğru seçenek metni:** Set the queue's retry parameters, such as the maximum number of attempts and the minimum and maximum backoff, so Cloud Tasks retries failed tasks automatically.

**Kaynak:** SCP14-Q17; rehber 1.1. [Ek resmî kaynak](https://docs.cloud.google.com/tasks/docs/configuring-queues).

**Önceki ilişki:** S11-28; Tasks pekiştirme, retry policy kararı.

## Q10 — C

**Karar:** Her region için serverless NEG, tek global backend service ve global external Application Load Balancer kullanılır. Multi-region düzeninde Premium Tier gerekir.

**Yakın seçenek ve sınır:** Bölgesel LB + DNS farklı bir tasarımdır; soru tek global LB yolu istiyor. Yakınlık veriyi kendiliğinden replike etmez.

**Belirleyici İngilizce koşul:** `rather than maintaining DNS routing rules yourself`

**Doğru seçenek metni:** Deploy the Cloud Run service in multiple regions. Create a serverless NEG in each region pointing to the regional Cloud Run service. Add all serverless NEGs to a single global backend service attached to a global external Application Load Balancer.

**Kaynak:** SCP15-Q09; rehber 1.1. [Ek resmî kaynak](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts).

**Önceki ilişki:** S11-44; karma, bağımlılıklar sağlıklı varsayılıyor.

## Q11 — B

**Karar:** CPU utilization requeste oranla hesaplanır. Limit bulunması eksik requestin yerini tutmaz; request eklenmelidir.

**Yakın seçenek ve sınır:** Node kapasitesi ve maxReplicas kökte elendi. CPU metriği için custom adapter zorunlu değildir.

**Belirleyici İngilizce koşul:** `a CPU limit but no CPU request`

**Doğru seçenek metni:** The containers in the Deployment do not define a CPU resource request, so the HPA cannot express current usage as a percentage of the request.

**Kaynak:** SCP14-Q23; rehber 3.2. [Ek resmî kaynak](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).

**Önceki ilişki:** S10-12 / S11-23; HPA farklı engel teşhisi.

## Q12 — D

**Karar:** Outlier detection gözlenen başarısız yanıtları kullanarak sağlıksız serverless backendleri geçici dışlar; aktif probe istemeyen koşula uyar.

**Yakın seçenek ve sınır:** Bu sıfır hata veya anında global failover garantisi değildir. Cloud Run service health ayrı bir seçenek olabilir; burada passive response signal istenmiştir.

**Belirleyici İngilizce koşul:** `based on observed response failures`

**Doğru seçenek metni:** Enable outlier detection on the backend service and configure it to eject endpoints after consecutive 5xx errors are detected.

**Kaynak:** SCP16-Q22; rehber 3.1. [Ek resmî kaynak](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts).

**Önceki ilişki:** S11-44; LB failure detection uygulaması.

## Q13 — A

**Karar:** Query Insights ve sqlcommenter route/controller gibi uygulama etiketlerini SQL performansıyla ilişkilendirir. Böylece benzer SQLi hangi yolun ürettiği görülebilir.

**Yakın seçenek ve sınır:** CPU grafiği sorgunun uygulama kaynağını tek başına göstermez. Etiketlerde hassas kullanıcı verisi taşımaya gerek yoktur.

**Belirleyici İngilizce koşul:** `which application route generated`

**Doğru seçenek metni:** Enable Query Insights on your Cloud SQL instance and use the sqlcommenter library in your application to automatically tag SQL queries with application information from your MVC framework.

**Kaynak:** SCP15-Q05; rehber 4.3. [Ek resmî kaynak](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights).

**Önceki ilişki:** S12-38/39 observability temeli; ORM route correlation.

## Q14 — B

**Karar:** Read-only transaction okumaları tek snapshot üzerinde toplar ve read lock almaz. Ayrı okumalarda araya yeni commit girebilir.

**Yakın seçenek ve sınır:** Ayrı strong read çağrıları kendi başlarına güncel olabilir ama aynı anı paylaşmak zorunda değildir. Aynı staleness süresi de aynı timestamp demek değildir.

**Belirleyici İngilizce koşul:** `All returned rows must reflect one database snapshot`

**Doğru seçenek metni:** Execute the reads inside a read-only transaction, which provides a consistent snapshot across all reads without acquiring locks.

**Kaynak:** SCP16-Q19; rehber 1.3. [Ek resmî kaynak](https://docs.cloud.google.com/spanner/docs/transactions).

**Önceki ilişki:** S08 Spanner temeli; snapshot kararı pekiştirme.

## Q15 — B

**Karar:** Workflows sıralamayı, koşullu dalları ve execution durumunu merkezi tanımlar. HTTP işçiler sonraki adımı bilmek zorunda kalmaz.

**Yakın seçenek ve sınır:** Tasks tekil çağrı teslimini yönetir; dallanan bütün sürecin state machine tanımını kendiliğinden sağlamaz.

**Belirleyici İngilizce koşul:** `Individual services should remain unaware of their successors`

**Doğru seçenek metni:** Define the process as a Workflows workflow that calls each HTTP service in sequence and uses conditional steps for branching.

**Kaynak:** SCP14-Q27; rehber 1.1. [Ek resmî kaynak](https://docs.cloud.google.com/workflows/docs/overview).

**Önceki ilişki:** S12-33 / S01-15; bilinçli pekiştirme.

## Q16 — A

**Karar:** Log-based alert matching entry üzerinden incident oluşturur. Sayısal trend gerekmeyen tek kritik olay için doğrudan mekanizmadır.

**Yakın seçenek ve sınır:** Log-based metric + threshold da başka gereksinimlerde yararlıdır ama burada ek ölçüm katmanı gerekmiyor; notification limits korunur.

**Belirleyici İngilizce koşul:** `do not need a trend chart or a numerical count threshold`

**Doğru seçenek metni:** Create a log-based alerting policy in Cloud Monitoring that matches the specific error message pattern in your container logs.

**Kaynak:** SCP15-Q12; rehber 4.3. [Ek resmî kaynak](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

**Önceki ilişki:** S12-10 log sorgusu üzerine matching event alert.

## Q17 — D

**Karar:** Sensor-week satırı ölçülen boyut sınırına uyuyor ve bir haftalık veriyi grupluyor. Timestamped cell geçmişi GC politikasıyla korunmalıdır.

**Yakın seçenek ve sınır:** Tek ömürlük satır sınırsız büyür. Tall-narrow da geçerli bir tasarım olabilir; burada özellikle bounded haftalık gruplama tercihinin koşulları verilmiştir.

**Belirleyici İngilizce koşul:** `fits comfortably within the recommended row-size limits`

**Doğru seçenek metni:** Use sensor_id#week_start as the row key and store measurements as timestamped cells, with garbage collection configured to retain the required history.

**Kaynak:** SCP14-Q19; rehber 1.3. [Ek resmî kaynak](https://docs.cloud.google.com/bigtable/docs/schema-design-time-series).

**Önceki ilişki:** S12-46 / S11-33; karma, row granularity değişiyor.

## Q18 — A

**Karar:** V4 X-Goog-Expires saniye cinsinden süreyi taşır; iki saat 7200 saniyedir. Yetkili signer önkoşulu soruda sağlanmıştır.

**Yakın seçenek ve sınır:** Retention verinin silinebilirliğini düzenler; link kullanım süresi değildir. Link bearer credentialdır ve indirilmiş kopyayı geri alamaz.

**Belirleyici İngilizce koşul:** `Possession of the link is an acceptable access credential`

**Doğru seçenek metni:** Generate V4 signed URLs with the X-Goog-Expires parameter set to 7200 seconds (2 hours) using a service account that has storage.objects.get permission on the bucket.

**Kaynak:** SCP14-Q52; rehber 1.3. [Ek resmî kaynak](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

**Önceki ilişki:** S11-24 / S01-04; bilinçli pekiştirme.

## Q19 — C

**Karar:** Admission kuralında iki attestor requireAttestationsBy listesine konur; image iki gerekli doğrulamayı da taşımalıdır ve enforcement mode uyumsuz imageı bloke etmelidir.

**Yakın seçenek ve sınır:** Continuous Validation sonradan bulgu üretmekle admission anında ikinci attestationı zorunlu kılmanın yerini tutmaz.

**Belirleyici İngilizce koşul:** `Images missing either attestation must be rejected at admission`

**Doğru seçenek metni:** Configure the cluster admission rule with evaluationMode: REQUIRE_ATTESTATION and enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG, listing both attestors under requireAttestationsBy.

**Kaynak:** SCP18-Q26; rehber 1.2. [Ek resmî kaynak](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference).

**Önceki ilişki:** S12-34; karma, iki bağımsız onay.

## Q20 — C

**Karar:** Cloud Workstations config merkezi custom image ve ağ ayarlarını uygular; geliştirici araçları image ile tutarlı dağıtılır. Persistent home ayrı tutulabilir.

**Yakın seçenek ve sınır:** Cloud Code eklentisi tek başına yönetilen VPC ortamı yaratmaz. Araç kurulumu Gemini lisans ve erişim izinlerini otomatik sağlamaz.

**Belirleyici İngilizce koşul:** `centrally maintain tool versions`

**Doğru seçenek metni:** Build a custom Cloud Workstations container image that extends a preconfigured base image with the required tools, and create a workstation configuration that applies the image to all developer workstations.

**Kaynak:** SCP14-Q50; rehber 2.1. [Ek resmî kaynak](https://docs.cloud.google.com/workstations/docs/customize-container-images).

**Önceki ilişki:** S12-05 / S09-29 / S11-14; bilinçli pekiştirme.

## Q21 — B

**Karar:** Client dependency olarak verilir; test double dış servisi değiştirirken business logic gerçek kalır. Network ve credential ihtiyacı kaldırılır.

**Yakın seçenek ve sınır:** Gerçek bucketla test integration testidir. Hataları yutan try/except yanlış davranışı başarılı gösterebilir.

**Belirleyici İngilizce koşul:** `an explicit dependency boundary`

**Doğru seçenek metni:** Ask Gemini Code Assist to refactor the function so the storage client is passed in as a parameter, then have it generate tests that inject a test double in place of the real client.

**Kaynak:** SCP18-Q25; rehber 2.3. [Ek resmî kaynak](https://docs.python.org/3/library/unittest.mock-examples.html).

**Önceki ilişki:** S12-35 / S11-30; bilinçli unit/integration ayrımı.

## Q22 — A + C

**Karar:** Object finalized event tipi ve bucket filtresi doğru olayı seçer. Eventarc HTTP CloudEvents teslim eder; handler event içindeki object bilgisini işler.

**Yakın seçenek ve sınır:** Bucket creation farklı olaydır. Teslim edilen event tüm object baytları değildir; gerektiğinde runtime ayrı Storage okuması yapar.

**Belirleyici İngilizce koşul:** `direct event delivery without a polling process`

**Doğru seçenek metni:** Create an Eventarc trigger filtered for google.cloud.storage.object.v1.finalized and the source bucket, with the Cloud Run service as its destination. / Configure the handler to accept the delivered CloudEvents HTTP format and process the object information from the event.

**Kaynak:** OFFICIAL-EVENTARC; rehber 3.1. [Ek resmî kaynak](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-storage).

**Önceki ilişki:** Ek resmî soru; S12-16/37 ve S11-19 ile ilişkili, IAM yerine event/receiver seçimi.

## Q23 — B

**Karar:** Manifestte replicas desired value tutmamak GitOpsun HPA sayısını tekrar üçe çekmesini önler. Deployment template yönetimi devam eder.

**Yakın seçenek ve sınır:** Manifesti maxReplicas yapmak yine iki controllerın aynı alanı yönetmesidir. Geçişte field ownership kontrollü taşınmalıdır.

**Belirleyici İngilizce koşul:** `while the HPA owns replica scaling`

**Doğru seçenek metni:** Remove the spec.replicas field from the Deployment manifest so the HorizontalPodAutoscaler is the sole controller of the replica count.

**Kaynak:** SCP14-Q35; rehber 3.2. [Ek resmî kaynak](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).

**Önceki ilişki:** S11-23 HPA temeli; desired-state ownership.

## Q24 — B

**Karar:** Bounded exponential backoff jitter ile clientların tekrarlarını dağıtır. Retry deadline sonsuz beklemeyi önler.

**Yakın seçenek ve sınır:** Sabit veya anında ortak retry yeniden yük patlaması yaratır. Geçersiz istek/kalıcı izin hataları bu geçici hata politikasına körlemesine sokulmaz.

**Belirleyici İngilizce koşul:** `immediate synchronized retries`

**Doğru seçenek metni:** Use bounded exponential backoff with randomized jitter, a maximum delay, and an overall retry deadline.

**Kaynak:** SCP15-Q25; rehber 4.2. [Ek resmî kaynak](https://docs.cloud.google.com/storage/docs/retry-strategy).

**Önceki ilişki:** S12-26 / S11-15; bilinçli pekiştirme.

## Q25 — A

**Karar:** Counterlara rate uygulanır; toplam 5xx rate / toplam request rate request ağırlıklı hata oranını verir. 0.05 üstü on dakika sürerse koşul tetiklenir.

**Yakın seçenek ve sınır:** Ayrı counter thresholdlar oran değildir. Farklı instance oranlarının ağırlıksız ortalaması farklı trafik hacimlerinde yanlış sonuç verir.

**Belirleyici İngilizce koşul:** `proportion of 5xx requests exceeds 5% continuously for ten minutes`

**Doğru seçenek metni:** Use a PromQL condition dividing the summed 5xx request rate by the summed total request rate, compare it with 0.05, and set a ten-minute retest duration.

**Kaynak:** SCP16-Q58; rehber 4.3. [Ek resmî kaynak](https://docs.cloud.google.com/monitoring/alerts/using-promql).

**Önceki ilişki:** S10-20 / S11-45; bilinçli oran/alert pekiştirmesi.

## Q26 — C

**Karar:** Mevcut v1 çalışırken response header eklemek istemciye programatik deprecation ve sunset bilgisi taşır. AssignMessage response değiştirebilir.

**Yakın seçenek ve sınır:** 410 veya sıfır kota gelecekteki kapatma tarihini duyurmak yerine bugün erişimi keser.

**Belirleyici İngilizce koşul:** `While both versions remain live`

**Doğru seçenek metni:** Use an AssignMessage policy on the v1 proxy to add Deprecation and Sunset response headers that indicate the retirement date.

**Kaynak:** SCP14-Q06; rehber 1.1. [Ek resmî kaynak](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy).

**Önceki ilişki:** S12-32 API politikasıyla ilişkili; farklı yaşam döngüsü kararı.

## Q27 — C

**Karar:** Pod başına azami 5+2=7, toplam 50×7=350 bağlantı; diğer clientlar 50 ile toplam 400. Bounded retry geçici hataya yardım eder.

**Yakın seçenek ve sınır:** 8+2 veya 7+1 seçenekleri bütçeyi aşar. Bu yalnız verilen azami sayılar altında hesap; yeni Podlar/başka poollar ayrıca sayılır.

**Belirleyici İngilizce koşul:** `at most fifty Pods, including during rollouts`

**Doğru seçenek metni:** Set pool_size=5 and max_overflow=2 in every Pod, keep the fifty-Pod maximum, and use bounded retries for transient failures.

**Kaynak:** SCP17-Q40; rehber 4.1. [Ek resmî kaynak](https://docs.cloud.google.com/sql/docs/mysql/manage-connections).

**Önceki ilişki:** S11-03; bilinçli pool bütçesi pekiştirmesi.

## Q28 — A

**Karar:** 308 incomplete ve Range yoksa server henüz byte persist etmemiştir. Aynı geçerli session URI ile byte 0dan devam edilir.

**Yakın seçenek ve sınır:** Range yokluğunu tek başına expired session veya tamamlanmış upload diye yorumlama; HTTP status ve session validity birlikte verilmiştir.

**Belirleyici İngilizce koşul:** `308 Resume Incomplete and no Range header`

**Doğru seçenek metni:** Cloud Storage has not yet persisted any bytes. Your application should start the upload from the beginning using the same session URI.

**Kaynak:** SCP15-Q31; rehber 4.1. [Ek resmî kaynak](https://docs.cloud.google.com/storage/docs/performing-resumable-uploads).

**Önceki ilişki:** S11-04 transfer temeli; upload offset kararı.

## Q29 — D

**Karar:** Identity Platform tenantları kullanıcı ve provider yapılandırmalarını ayırır. Shared backend doğruladığı tenant bağlamına göre veri authorization uygulamaya devam eder.

**Yakın seçenek ve sınır:** Identity tenant oluşturmak veritabanındaki satır erişimini otomatik ayırmaz. Kullanıcı grubu ayrı authentication tenantı değildir.

**Belirleyici İngilizce koşul:** `its own Identity Platform user directory and identity-provider configuration`

**Doğru seçenek metni:** Enable multi-tenancy in Identity Platform and create a separate tenant for each customer organization.

**Kaynak:** SCP17-Q33; rehber 1.2. [Ek resmî kaynak](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy).

**Önceki ilişki:** S10-13 / S11-38; kimlik izolasyonu pekiştirme.

## Q30 — D

**Karar:** allowExitCodes:[1] yalnız onaylı nonzero kodu kabul eder; 2 build failure olarak kalır.

**Yakın seçenek ve sınır:** allowFailure:true diğer nonzero hataları da yutar. Flaky testleri genel olarak susturma önerisi değildir; kod sözleşmesi açık verilmiştir.

**Belirleyici İngilizce koşul:** `one means an accepted nonblocking advisory`

**Doğru seçenek metni:** Add 'allowExitCodes: [1]' to the integration test build step to allow the build to continue when tests exit with code 1 while failing on code 2.

**Kaynak:** SCP16-Q05; rehber 2.3. [Ek resmî kaynak](https://docs.cloud.google.com/build/docs/build-config-file-schema).

**Önceki ilişki:** S11-06; karma, seçici failure exception.

## Q31 — A

**Karar:** JSONB değişken attribute yapısını aynı satırda tutar. Uygun GIN index JSON containment sorgularını destekler.

**Yakın seçenek ve sınır:** Her kategoriye yeni tablo/kolon açmak migration ihtiyacını sürdürür. VARCHAR içindeki JSON metnine sıradan B-tree aynı JSON sorgu desteğini vermez.

**Belirleyici İngilizce koşul:** `filter using JSON containment predicates`

**Doğru seçenek metni:** Store products in one table with a JSONB column for the variable attributes, and create a GIN index on the JSONB column to support filtering on individual attributes.

**Kaynak:** SCP16-Q31; rehber 1.3. [Ek resmî kaynak](https://www.postgresql.org/docs/current/datatype-json.html).

**Önceki ilişki:** S10-08 PostgreSQL üzerine schema kararı.

## Q32 — D

**Karar:** Enterprise code customization onaylı private repositoryleri suggestion bağlamına dahil eder. Merkezi index/repository bağlantısı gerektirir.

**Yakın seçenek ve sınır:** Prompta her seferinde snippet yapıştırmak istenen merkezi çözüm değil; sıradan completion için ayrı model fine-tuning gerekmiyor.

**Belirleyici İngilizce koşul:** `without manually pasting examples into every request`

**Doğru seçenek metni:** Subscribe to Gemini Code Assist Enterprise and configure code customization to index your private repositories through Developer Connect so suggestions reflect your internal code.

**Kaynak:** SCP18-Q20; rehber 2.1. [Ek resmî kaynak](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

**Önceki ilişki:** S11-26 context temeli; kurumsal repository özelleştirmesi.

## Q33 — A

**Karar:** Mock publisherın tam bir kez beklenen topic ve payload ile çağrıldığını assert etmek eksik side effecti yakalar. Gerçek function çalışır.

**Yakın seçenek ve sınır:** Gerçek Pub/Sub ile integration testi başka bir sınırdır. Sleep eklemek mock invocation eksikliğini ölçmez.

**Belirleyici İngilizce koşul:** `it still passes after the publish call is accidentally removed`

**Doğru seçenek metni:** Ask Gemini Code Assist to add assertions that verify the mocked publisher was called once with the expected topic and message payload.

**Kaynak:** SCP15-Q06; rehber 2.3. [Ek resmî kaynak](https://docs.python.org/3/library/unittest.mock.html).

**Önceki ilişki:** S10-10 yerine seçildi; S11-10 test oracle temeli üzerine interaction assertion.

## Q34 — A

**Karar:** Builder stage compile eder; runtime stage yalnız gerekli JAR ve runtime dosyalarını alır. Araçlar final image katmanlarına taşınmaz.

**Yakın seçenek ve sınır:** Aynı stage içinde ortam değişkeni seçmek build araçlarını image içinden çıkarmaz. İki ayrı Dockerfile mümkün ama gereksiz artifact aktarımı ekler.

**Belirleyici İngilizce koşul:** `only the compiled application and required runtime dependencies`

**Doğru seçenek metni:** Create a Dockerfile with a multi-stage build that uses a JDK image for compilation and a JRE image for the runtime stage. Configure Cloud Build to build and push the final image to Artifact Registry.

**Kaynak:** SCP16-Q16; rehber 2.2. [Ek resmî kaynak](https://docs.docker.com/build/building/multi-stage/).

**Önceki ilişki:** S11-34 / S08-23; bilinçli pekiştirme.

## Q35 — D

**Karar:** Immutable ConfigMap/Secret güncellenmeyen nesnelerde watch ihtiyacını azaltır ve accidental in-place mutationı engeller. Yeni içerik yeni nesneyle dağıtılır.

**Yakın seçenek ve sınır:** Environment variablea geçirmek aynı immutable API-object özelliği değildir. Immutable nesne sonradan tekrar mutable yapılamaz.

**Belirleyici İngilizce koşul:** `never updated in place`

**Doğru seçenek metni:** Mark the ConfigMaps and Secrets that do not need updates as immutable by setting the immutable field to true.

**Kaynak:** SCP17-Q20; rehber 3.2. [Ek resmî kaynak](https://kubernetes.io/docs/concepts/configuration/configmap/).

**Önceki ilişki:** S11-32; ters lifecycle koşulu, canlı değişim gerekmiyor.

## Q36 — C

**Karar:** internal-and-cloud-load-balancing dış internetten doğrudan run.app yolunu kapatırken external LB ve izinli internal kaynakları kabul eder.

**Yakın seçenek ve sınır:** Bu ayar IAM veya Cloud Armor politikasını tanımlamaz; internal access tamamen yasaklanmış sayılmaz.

**Belirleyici İngilizce koşul:** `current run.app URL`

**Doğru seçenek metni:** Set the Cloud Run service ingress setting to 'internal-and-cloud-load-balancing' to allow traffic only from the load balancer and VPC networks.

**Kaynak:** SCP13-Q33; rehber 3.1. [Ek resmî kaynak](https://docs.cloud.google.com/run/docs/securing/ingress).

**Önceki ilişki:** S03/Cloud Run ingress; bilinçli pekiştirme.

## Q37 — C

**Karar:** Vector alanındaki embeddingler için ScaNN approximate nearest-neighbor index uygundur; sorgu veritabanında yürür. İlgili extensionlar gerekir.

**Yakın seçenek ve sınır:** B-tree/JSONB yapıları bu vector distance aramasının yerine geçmez. Approximate sonuç exact nearest-neighbor garantisi değildir.

**Belirleyici İngilizce koşul:** `accepts approximate nearest-neighbor results`

**Doğru seçenek metni:** Store the embeddings in a vector column and create a ScaNN index on that column to accelerate approximate nearest-neighbor queries.

**Kaynak:** SCP17-Q05; rehber 1.3. [Ek resmî kaynak](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index).

**Önceki ilişki:** AI/veri temeline ek index uygulaması; yeni temel AI kapsamı iddiası yok.

## Q38 — C

**Karar:** Deterministik hash öneki monoton customer numaralarının yazılarını dağıtır; müşteri numarası ikinci key parçası olarak korunur. Lookup sırasında hash hesaplanabilir.

**Yakın seçenek ve sınır:** Secondary index base-table hotspotunu ortadan kaldırmaz. Bu senaryo çok sayıda farklı ID içindir; tek hot user için aynı user hash yeterli olmaz.

**Belirleyici İngilizce koşul:** `must continue to look up rows by the customer number`

**Doğru seçenek metni:** Compute a hash of the customer number and use that hash value as the leading column of the primary key, keeping the customer number as the next key column.

**Kaynak:** SCP16-Q53; rehber 1.3. [Ek resmî kaynak](https://docs.cloud.google.com/spanner/docs/schema-design).

**Önceki ilişki:** S07/S09 hotspot kararlarıyla ilişkili pekiştirme.

## Q39 — A + D

**Karar:** Çağrı iki perimeter sınırını geçer: kaynakta izinli egress, hedefte izinli ingress gerekir. IAM izni ayrıca zaten sağlanmıştır.

**Yakın seçenek ve sınır:** Bir sınırdaki izin diğer sınırı geçersiz kılmaz. Dar kapsam şartı geniş bir perimeter bridge alternatifini eler.

**Belirleyici İngilizce koşul:** `Both perimeters must remain enforced`

**Doğru seçenek metni:** Add an ingress rule to perimeter B allowing the required identity and operations from the permitted source. / Add an egress rule to perimeter A allowing the required identity and operations against the destination resources.

**Kaynak:** SCP15-Q10; rehber 1.2. [Ek resmî kaynak](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

**Önceki ilişki:** S09 VPCSC kapsamı; bilinçli güvenlik pekiştirmesi.

## Q40 — A

**Karar:** BackendConfig healthCheck ayarlarını Service üzerindeki backend-config annotationıyla bağlar. GKE generated health checki bu kaynaktan yönetir.

**Yakın seçenek ve sınır:** FrontendConfig bu backend health-check ayarının yeri değildir. Var olan LB checkini yalnız readiness probe değiştirerek güncelleme garantisi yoktur.

**Belirleyici İngilizce koşul:** `declaratively through GKE`

**Doğru seçenek metni:** Create a BackendConfig custom resource with a healthCheck section and reference it in the Service using the cloud.google.com/backend-config annotation.

**Kaynak:** SCP14-Q55; rehber 3.2. [Ek resmî kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration).

**Önceki ilişki:** S11-16 probe temeli; LB ve Pod check ayrımı.

## Q41 — D + E

**Karar:** Push deployment adımından önce registryde image bulunmasını sağlar. images alanı ayrıca build output kaydını oluşturur.

**Yakın seçenek ve sınır:** images son build çıktısı olarak upload sağlar; build içinde daha erken çalışan deploy için tek başına yeterli sıralama garantisi değildir.

**Belirleyici İngilizce koşul:** `before the deployment step starts`

**Doğru seçenek metni:** Add an explicit Docker push step and make the deployment step wait for that push. / List the image under the top-level images field so it is recorded as a build output.

**Kaynak:** SCP16-Q02; rehber 2.2. [Ek resmî kaynak](https://docs.cloud.google.com/build/docs/building/build-containers).

**Önceki ilişki:** S12-18; karma, build results kaydı ekli.

## Q42 — B

**Karar:** Debugger bağlı olduğundan sorun bağlantı değil, yerel kaynak ile container path eşlemesidir. Source mapping breakpointi yürüyen dosyaya bağlar.

**Yakın seçenek ve sınır:** Port açmak zaten çalışan bağlantıyı düzeltmez; eski image olasılığı da kökte elenmiştir.

**Belirleyici İngilizce koşul:** `local breakpoints remain unbound`

**Doğru seçenek metni:** Configure the source mapping in the Debug tab of the Run configuration to map local source paths to remote container paths.

**Kaynak:** SCP17-Q23; rehber 2.1. [Ek resmî kaynak](https://docs.cloud.google.com/code/docs/intellij/debug).

**Önceki ilişki:** S10-14; karma, bağlı debugger path teşhisi.

## Q43 — B

**Karar:** Metadata server hazır olana kadar bekleyen initContainer ana uygulamanın erken authentication hatasıyla çıkmasını önler. WIF ve dar IAM korunur.

**Yakın seçenek ve sınır:** SA key dosyası dağıtmak veya node identityye geçmek gerekli değil; kalıcı izin eksikliği olmadığı kanıtlanmış.

**Belirleyici İngilizce koşul:** `the same call succeeds seconds later`

**Doğru seçenek metni:** Deploy an initContainer in your pod specification that waits until the GKE metadata server is ready before the main container starts.

**Kaynak:** SCP16-Q06; rehber 3.2. [Ek resmî kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/authentication).

**Önceki ilişki:** S11-37 WIF üzerine transient startup dependency.

## Q44 — D

**Karar:** Immutable tags repo düzeyinde mevcut tagın başka digest ile değiştirilmesini engeller; yeni taglara izin verilebilir.

**Yakın seçenek ve sınır:** İsim kuralı veya yalnız CI writer yetkisi operatör hatasına karşı aynı repository enforcementını sağlamaz.

**Belirleyici İngilizce koşul:** `the repository to enforce`

**Doğru seçenek metni:** Enable the immutable tags setting on the Docker repository in Artifact Registry to prevent changing the image digest that a tag references.

**Kaynak:** SCP15-Q26; rehber 2.2. [Ek resmî kaynak](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images).

**Önceki ilişki:** S11-39 / S12-02; registry tag enforcement kararı.

## Q45 — B

**Karar:** onSnapshotın döndürdüğü unsubscribe eski room listenerını kapatır; ardından yeni room listenerı oluşturulur.

**Yakın seçenek ve sınır:** UI dedup eski subscriptionları ve gereksiz callbackleri ortadan kaldırmaz; security rules listener yaşam döngüsü yöneticisi değildir.

**Belirleyici İngilizce koşul:** `Database records are not duplicated`

**Doğru seçenek metni:** Store the unsubscribe function returned by onSnapshot() and call it before creating a new listener when users switch chat rooms.

**Kaynak:** SCP18-Q05; rehber 4.1. [Ek resmî kaynak](https://firebase.google.com/docs/firestore/query-data/listen).

**Önceki ilişki:** Firestore istemci lifecycle; temel realtime veri kullanımının uygulaması.

## Q46 — C

**Karar:** Autopilotta WIF tüm nodelarda hazırdır; Standard için kullanılan metadata-server nodeSelector kaldırılır. KSA/IAM bağlantısı korunur.

**Yakın seçenek ve sınır:** Autopilot için Pod bazında WIF enable annotationı gerekmez; Standarda dönmek gereksizdir.

**Belirleyici İngilizce koşul:** `its IAM access are already correctly configured`

**Doğru seçenek metni:** Remove the nodeSelector from the pod specification because Autopilot clusters always have Workload Identity Federation for GKE enabled and will reject pods with this nodeSelector.

**Kaynak:** SCP16-Q40; rehber 3.2. [Ek resmî kaynak](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

**Önceki ilişki:** S11-37 / S12-07; Autopilot yapılandırması.

## Q47 — D

**Karar:** ContainerResource metriği yalnız adı belirtilen application containerın CPU kullanımını izler. Sidecar Pod içinde kalır.

**Yakın seçenek ve sınır:** Pod Resource metriğinde sidecarı requestini sıfırlayarak güvenli biçimde çıkaramazsın; eksik request ölçümü bozabilir.

**Belirleyici İngilizce koşul:** `only the application container`

**Doğru seçenek metni:** Configure the HorizontalPodAutoscaler with a ContainerResource metric that targets the CPU utilization of the application container only.

**Kaynak:** SCP17-Q54; rehber 3.2. [Ek resmî kaynak](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).

**Önceki ilişki:** HPA temeli pekiştirme; container-specific ölçüm.

## Q48 — D

**Karar:** Cache-aside önce cache okur; miss olunca kaynak veriyi okuyup cache doldurur. TTL ve update invalidation ile kabul edilen staleness yönetilir.

**Yakın seçenek ve sınır:** Bu bir SQL/Redis atomik transaction garantisi değildir. Redis tek veri kaynağı yapılırsa eviction kalıcı kayıp yaratabilir.

**Belirleyici İngilizce koşul:** `The database must remain authoritative`

**Doğru seçenek metni:** Implement a cache-aside pattern where your application checks Memorystore first, queries Cloud SQL on cache miss, and writes the result to cache with a TTL. When product data is updated, invalidate the corresponding cache key.

**Kaynak:** SCP16-Q27; rehber 1.1. [Ek resmî kaynak](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview).

**Önceki ilişki:** S12-15 / S11-01; bilinçli pekiştirme.

## Q49 — C

**Karar:** Tüm namespace Podlarını seçen default-deny egress politikası outbound başlangıcını kapatır. Sonra gerekli DNS ve servis yolları ayrı allow politikalarıyla eklenir.

**Yakın seçenek ve sınır:** NetworkPolicy sıralı firewall kural listesi değildir; ingress-only politika outbound trafiği kapatmaz.

**Belirleyici İngilizce koşul:** `can initiate no outbound connections until specific destinations are approved`

**Doğru seçenek metni:** Apply a default-deny egress NetworkPolicy to the 'payments' namespace, then add NetworkPolicies that explicitly allow egress only to the required destinations.

**Kaynak:** SCP18-Q07; rehber 1.2. [Ek resmî kaynak](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

**Önceki ilişki:** S11-21 / S03-10; bilinçli pekiştirme.

## Q50 — B

**Karar:** ADC quota project ayarı doğru consumer projeyi seçer. Kullanıcı kimliği ve resource izinleri değişmeden kalır.

**Yakın seçenek ve sınır:** gcloud varsayılan projecti değiştirmek yerel ADC quota projecti ayarlamakla aynı işlem değildir; serviceusage izni zaten mevcut.

**Belirleyici İngilizce koşul:** `no quota project is set`

**Doğru seçenek metni:** Run 'gcloud auth application-default set-quota-project PROJECT_ID' to specify the project for billing and quota.

**Kaynak:** SCP17-Q44; rehber 4.2. [Ek resmî kaynak](https://docs.cloud.google.com/docs/quotas/set-quota-project).

**Önceki ilişki:** S09-39; bilinçli pekiştirme, izin zaten sağlanmış.
