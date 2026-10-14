# PCD-S15 Türkçe cevap anahtarı

İlk çözüm bittikten sonra aç. Her soruda doğru karar, yakın yanlışın nedeni, sade İngilizce karşılığı ve teknik kaynak bulunur. Platform anahtarı koşulsuz hakem olarak kullanılmadı.

| Soru | Doğru | Konu |
|---|---|---|
| 01 | A | custom metrics adapter |
| 02 | D | rollout undo |
| 03 | D | atomic batched write |
| 04 | A | persistent reports |
| 05 | C | application investigation |
| 06 | B | build environment |
| 07 | A | first canary rollout |
| 08 | C | internal Ingress |
| 09 | A+C | parallel branch results |
| 10 | C | commit traceability |
| 11 | B | Docker layer cache |
| 12 | C | safe step retries |
| 13 | D | Redis reconnection |
| 14 | B | atomic idempotency |
| 15 | A | Secret Manager IAM audit |
| 16 | D | Ingress NEG backend |
| 17 | D | ADC impersonation |
| 18 | B | node capacity |
| 19 | D | requests limits |
| 20 | D | environment configuration |
| 21 | C | pinned secret version |
| 22 | C | central orchestration |
| 23 | A | IDE cluster explorer |
| 24 | C | managed Prometheus |
| 25 | B | Dockerfile precedence |
| 26 | A+C | home initialization |
| 27 | A | build attestation |
| 28 | A | custom image |
| 29 | D | Spanner parameters |
| 30 | B | duplicate handler transaction |
| 31 | C | execution failure after delivery |
| 32 | D | HPA behavior |
| 33 | B | callback approval |
| 34 | B | image pull identity |
| 35 | B | caller and worker identities |
| 36 | B | tenant provisioning |
| 37 | C | HPA denominator |
| 38 | A | private build pool |
| 39 | A | collection group index |
| 40 | C | ConfigMap reload |
| 41 | A | AlloyDB PITR |
| 42 | B | multidimensional autoscaling |
| 43 | A+B | trigger and workflow identity |
| 44 | C | source to image |
| 45 | B | disable secret version |
| 46 | D | Skaffold modules |
| 47 | A | deterministic test |
| 48 | D | IAP signed assertion |
| 49 | C | alert retest window |
| 50 | A | secret rotation notification |

## Q01 A

**Doğru seçenek:** Deploy the Custom Metrics Stackdriver Adapter to the cluster so the HPA controller can read the metric from Cloud Monitoring through the custom and external metrics API.

**Karar:** Cloud Monitoring metric’ini Kubernetes custom/external metrics API’ye sunan adapter gerekir.

**Eleme koşulu:** CPU metrics-server Cloud Monitoring’deki business metric’i kendiliğinden sunmaz. Adapter IAM erişimi de gerekir.

**Sade anlam:** “Metric is present, no adapter installed” → Ölçüm var ama HPA’nın okuyacağı arayüze sunulmamış.

**Kaynak:** SCP14-Q15; [teknik belge](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/autoscaling-metrics).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q02 D

**Doğru seçenek:** Run kubectl rollout undo deployment/my-app to automatically roll back to the previous revision.

**Karar:** rollout undo saklanan önceki Pod template revision’ına döner.

**Eleme koşulu:** Deployment’ı silmek veya sıfıra indirmek gereksiz kesinti yaratır; rollback başarı ve sıfır kesinti garantisi değildir.

**Sade anlam:** “Previous working version” → Çalıştığını bildiğin bir önceki Deployment sürümüne dön.

**Kaynak:** SCP13-Q15; [teknik belge](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q03 D

**Doğru seçenek:** Use a batched write to group the update operations and commit them atomically without reading documents.

**Karar:** Read-dependent karar yoksa atomic batched write 200 update’i birlikte commit eder.

**Eleme koşulu:** BulkWriter/Promise.all tüm set için atomiklik sağlamaz. Kaynak gövdesine bu gerekli koşul eklendi.

**Sade anlam:** “All commit together or none” → Güncellemelerin bir kısmı kalıp bir kısmı başarısız olmasın.

**Kaynak:** SCP18-Q22; [teknik belge](https://firebase.google.com/docs/firestore/manage-data/transactions).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q04 A

**Doğru seçenek:** Configure the Cloud Build ‘artifacts‘ section with an ‘objects‘ block specifying a Cloud Storage bucket location and the paths to the test report XML files.

**Karar:** artifacts.objects ile rapor dosyalarının bucket konumu ve paths listesi tanımlanır.

**Eleme koşulu:** workspace ve custom volume build’ler arasında kalıcı değildir. artifacts upload başarıyla tamamlanan build için uygulanır.

**Sade anlam:** “Outside the build environment” → Rapor build makinesi kapanınca da saklansın.

**Kaynak:** SCP13-Q13; [teknik belge](https://docs.cloud.google.com/build/docs/building/store-artifacts-in-cloud-storage).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q05 C

**Doğru seçenek:** Run an application-level Gemini Cloud Assist investigation from Cloud Hub for the App Hub application.

**Karar:** App Hub application kapsamıyla Cloud Hub üzerinden tek investigation başlatılır.

**Eleme koşulu:** Proje listesi ilişkili application kapsamını yerine koymaz. İlgili preview erişimi ve izinler soruda hazırdır.

**Sade anlam:** “Across the entire application” → Tek resource yerine App Hub’daki ilişkili uygulamayı birlikte incele.

**Kaynak:** SCP13-Q47; [teknik belge](https://docs.cloud.google.com/cloud-assist/investigations).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q06 B

**Doğru seçenek:** Use the source deployment build environment configuration, such as --set-build-env-vars, when creating the new build.

**Karar:** Build env buildpacks’ın build aşamasına verilir; yeni source build bu ayarı kullanır.

**Eleme koşulu:** Runtime env hazırlanmış image’ın içindeki compiled asset’i yeniden derlemez.

**Sade anlam:** “At the required phase” → Ayar container çalışırken değil, image hazırlanırken gerekli.

**Kaynak:** OFFICIAL-BP2; [teknik belge](https://docs.cloud.google.com/run/docs/configuring/services/build-environment-variables).

**Önceki ilişki:** Ek resmî kaynak; ilgili önceki kimlik/konfigürasyon mekanizmaları pekiştirilebilir.

## Q07 A

**Doğru seçenek:** Cloud Deploy skips the canary phases and deploys directly to the stable phase at 100%, because there is no existing revision to split traffic with.

**Karar:** Mevcut stable revision yoksa ilk rollout canary aşamalarını atlayıp stable ile başlar.

**Eleme koşulu:** Placeholder revision oluşturulmaz. Kaynakta D seçeneğine yapıştırılmış açıklama kaldırıldı.

**Sade anlam:** “First deployment; no existing revision” → Trafiği paylaşacak eski sürüm yok.

**Kaynak:** SCP17-Q09; [teknik belge](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q08 C

**Doğru seçenek:** Add the annotation kubernetes.io/ingress.class: ‘gce-internal‘ to the Ingress manifest to deploy an internal Application Load Balancer.

**Karar:** GKE Ingress üzerinde kubernetes.io/ingress.class: gce-internal kullanılır.

**Eleme koşulu:** Internal LoadBalancer Service HTTP path routing ihtiyacını tek başına karşılamaz.

**Sade anlam:** “URL-based routing within the VPC” → VPC içinden erişilen HTTP path routing gerekli.

**Kaynak:** SCP15-Q21; [teknik belge](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q09 A + C

**Doğru seçenek:** Place the independent calls in branches of a parallel step and put the final decision after that parallel step. / Add both parent result variables to the parallel step shared list so the branches may assign them.

**Karar:** parallel bağımsız çağrıları eşzamanlı yapar ve tamamlanınca parent devam eder. shared parent variable’a write izni verir.

**Eleme koşulu:** Branch-local değer parent scope’dan okunmaz; shared ayrıca nested parallel scope’da da tanımlanmalıdır.

**Sade anlam:** “Both responses; parent scope” → Paralel iki işin sonucunu üst akışta kullan.

**Kaynak:** OFFICIAL-WF1; [teknik belge](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps).

**Önceki ilişki:** Ek resmî kaynak; ilgili önceki kimlik/konfigürasyon mekanizmaları pekiştirilebilir.

## Q10 C

**Doğru seçenek:** Tag the container image with the $COMMIT_SHA substitution variable in your cloudbuild.yaml file. Use the same tag when pushing to Artifact Registry and deploying to Cloud Run.

**Karar:** COMMIT_SHA tag’ini build, push ve deploy’da aynı kullanırsın.

**Eleme koşulu:** BUILD_ID commit SHA değildir. Commit tag’i değiştirilemez bytes garantisi vermez; immutable tag veya digest ayrıca düşünülebilir.

**Sade anlam:** “Traced back to its source code commit” → Hangi commit’in bu revision’ı ürettiğini bulabil.

**Kaynak:** SCP18-Q02; [teknik belge](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q11 B

**Doğru seçenek:** Configure the cloudbuild.yaml to pull a previously built image from Artifact Registry and use the --cache-from argument with docker build to reuse unchanged layers from the cached image.

**Karar:** Önceki image’ı pull edip docker build --cache-from ile uygun layer’ları yeniden kullanırsın.

**Eleme koşulu:** Dependency dosyaları source’dan önce kopyalanmalıdır; değişen önceki layer sonrası cache geçersizleşir.

**Sade anlam:** “Unchanged dependencies before source” → Kod değişse de değişmeyen paket katmanını yeniden indirip kurma.

**Kaynak:** SCP13-Q53; [teknik belge](https://docs.cloud.google.com/build/docs/optimize-builds/speeding-up-builds).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q12 C

**Doğru seçenek:** Attach a retry policy with an appropriate predicate, maximum retries, and exponential backoff to the pricing call only.

**Karar:** Retry yalnız pricing step’inde uygulanır; tamamlanan reservation yeniden yürütülmez.

**Eleme koşulu:** Workflow’un tümünü tekrar etmek non-idempotent önceki side effect’i çoğaltabilir.

**Sade anlam:** “Preserves the completed reservation” → Başarılı stok ayırmayı tekrar yapmadan yalnız pricing’i tekrar dene.

**Kaynak:** OFFICIAL-WF2; [teknik belge](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying).

**Önceki ilişki:** Ek resmî kaynak; ilgili önceki kimlik/konfigürasyon mekanizmaları pekiştirilebilir.

## Q13 D

**Doğru seçenek:** Implement retry logic with exponential backoff in your application code to handle temporary connection failures, and configure a connection pool to efficiently manage Redis connections.

**Karar:** Bounded exponential backoff, jitter ve connection pool transient bağlantı kopmalarını yönetir.

**Eleme koşulu:** AUTH/TLS erişim güvenliği sağlar; bakım sırasında kopan bağlantıyı otomatik yaşatmaz.

**Sade anlam:** “Temporary connection failures” → Geçici kopuşta kontrollü bekleyip tekrar bağlan.

**Kaynak:** SCP14-Q36; [teknik belge](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q14 B

**Doğru seçenek:** Use a stable order identifier and atomically record that identifier together with the inventory mutation in one database transaction, treating a previously committed identifier as a successful duplicate.

**Karar:** Stable order ID için duplicate kontrolü ve inventory mutation aynı DB transaction’da yapılır.

**Eleme koşulu:** Unique task name creation dedup içindir; aynı task’ın redelivery’sini engellemez.

**Sade anlam:** “Repeated executions produce the same result” → Aynı işi ikinci kez almak stoktan ikinci kez düşmesin.

**Kaynak:** SCP17-Q02; [teknik belge](https://docs.cloud.google.com/tasks/docs/common-pitfalls).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q15 A

**Doğru seçenek:** Store the secrets in Secret Manager and use Workload Identity Federation for GKE to authenticate your application to access them via the Secret Manager API. Enable the relevant Data Access audit logs for secret access.

**Karar:** Secret Manager, WIF ile workload kimliği ve secret-level IAM kullanılır; access kayıtları için Data Access logging etkinleştirilir.

**Eleme koşulu:** Base64 encryption değildir; Kubernetes RBAC, Secret Manager IAM ve access audit gereksiniminin karşılığı değildir.

**Sade anlam:** “Access controlled through IAM and audited” → Secret okuma izni ve erişim kaydı Google Cloud tarafında yönetilsin.

**Kaynak:** SCP18-Q18; [teknik belge](https://docs.cloud.google.com/secret-manager/docs/audit-logging).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q16 D

**Doğru seçenek:** Use type: ClusterIP for the backend Services when container-native load balancing is enabled.

**Karar:** NEG kullanan container-native Ingress için ClusterIP Service yeterlidir; trafik Pod IP’lerine yönlenir.

**Eleme koşulu:** NodePort bazı yapılarda kullanılabilir; burada her backend için ayrı LoadBalancer gerekmez.

**Sade anlam:** “Avoid allocating unnecessary node ports” → Pod’a doğrudan erişirken gereksiz NodePort açma.

**Kaynak:** SCP14-Q08; [teknik belge](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q17 D

**Doğru seçenek:** Create local ADC using gcloud auth application-default login --impersonate-service-account=app-runtime@PROJECT_ID.iam.gserviceaccount.com.

**Karar:** Desteklenen Python library yerel impersonated ADC ile hedef SA adına kısa ömürlü credential kullanır.

**Eleme koşulu:** gcloud CLI login ADC’yi aynı kimliğe geçirmek değildir; Workstations User workstation’a erişim içindir.

**Sade anlam:** “As app-runtime without a long-lived key” → Kod hedef servis hesabı adına çalışsın; JSON key oluşturma.

**Kaynak:** OFFICIAL-WS3; [teknik belge](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

**Önceki ilişki:** Ek resmî kaynak; ilgili önceki kimlik/konfigürasyon mekanizmaları pekiştirilebilir.

## Q18 B

**Doğru seçenek:** Enable cluster autoscaler on the node pool so that nodes are added automatically when Pods cannot be scheduled due to insufficient resources.

**Karar:** HPA replica sayısını artırmış; Pending Pod’lar için node pool cluster autoscaler kapasite ekler.

**Eleme koşulu:** İkinci HPA node kapasitesi oluşturmaz. Node limitleri ve kota yeterli olmalıdır.

**Sade anlam:** “Pending / insufficient CPU” → Replica istendi ama onu çalıştıracak node kapasitesi yok.

**Kaynak:** SCP12-Q13; [teknik belge](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q19 D

**Doğru seçenek:** Set CPU request to 250m with limit of 1000m, and set memory request to 512Mi with limit of 1Gi.

**Karar:** 250m CPU/512Mi memory request; 1000m CPU/1Gi memory limit verilen rezervasyon ve üst sınır koşullarını karşılar.

**Eleme koşulu:** Kaynak C diyor. Şartları açıklaştırılmış bu soruda A doğrudur. 512Mi limit, belirtilen 768Mi peak memory ihtiyacını karşılamaz.

**Sade anlam:** “Reserve normal requirement; impose hard limits” → Normal ihtiyacı ayır, peak için izin ver ama üst sınırı uygula.

**Kaynak:** SCP16-Q28; [teknik belge](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q20 D

**Doğru seçenek:** Change the workstation configuration machine and persistent directory settings while retaining its container image reference.

**Karar:** WorkstationConfig VM/machine ve persistent directory ayarlarını yönetir; container image araçları sağlar.

**Eleme koşulu:** Image layer boyutu kalıcı disk boyutu değildir; GKE Pod limits workstation VM’ini değiştirmez.

**Sade anlam:** “Same tools, more VM memory” → Araç image’ı aynı kalsın; workstation makine ayarı değişsin.

**Kaynak:** OFFICIAL-WS2; [teknik belge](https://docs.cloud.google.com/workstations/docs/customize-development-environment).

**Önceki ilişki:** Ek resmî kaynak; ilgili önceki kimlik/konfigürasyon mekanizmaları pekiştirilebilir.

## Q21 C

**Doğru seçenek:** Reference secrets by their specific version number in your deployment configuration and update version numbers through your existing release processes.

**Karar:** Validated numeric version deployment ile pin edilir, değişiklik release sürecinden geçer.

**Eleme koşulu:** latest veya taşınabilen alias release manifest’i değişmeden başka değere geçebilir.

**Sade anlam:** “Validated and tested versions” → Son yüklenen değere kendiliğinden geçme; onaylanmış sayısal sürümü kullan.

**Kaynak:** SCP16-Q45; [teknik belge](https://docs.cloud.google.com/secret-manager/docs/best-practices).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q22 C

**Doğru seçenek:** Define the process as a Workflows workflow that calls each HTTP service in sequence and uses conditional steps for branching.

**Karar:** Workflows sequence, conditional branch ve execution history’yi merkezi olarak sağlar.

**Eleme koşulu:** Pub/Sub fan-out veya Tasks chain ile business orchestration mantığı servislere dağılır. S13 Q15’e yakın bilinçli kaynak pekiştirmesi.

**Sade anlam:** “In a single place; execution state of every step” → İşin sırası ve dallanması merkezi tanımlı, adımları izlenebilir olsun.

**Kaynak:** SCP14-Q27; [teknik belge](https://docs.cloud.google.com/workflows/docs/overview).

**Önceki ilişki:** S13 Q15 ile aynı orchestration kararı; bilinçli pekiştirme.

## Q23 A

**Doğru seçenek:** Use the Cloud Code Kubernetes Explorer in VS Code to browse the cluster‘s resources and stream logs from the selected Pods.

**Karar:** Cloud Code Kubernetes Explorer kaynakları ve seçili Pod loglarını IDE’den gösterir.

**Eleme koşulu:** Integrated terminal kullanılabilir ama sorudaki terminale geçmeme şartını karşılamaz.

**Sade anlam:** “Without switching to a separate terminal” → Cluster kaynaklarını ve loglarını IDE panelinden gör.

**Kaynak:** SCP13-Q21; [teknik belge](https://docs.cloud.google.com/code/docs/vscode/view-logs).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q24 C

**Doğru seçenek:** Enable Managed Service for Prometheus on the GKE cluster and create a PodMonitoring custom resource that specifies the metrics endpoint and scrape interval for your application pods.

**Karar:** Managed collection ve PodMonitoring scrape endpoint/interval seçer.

**Eleme koşulu:** Self-managed Prometheus kurulabilir ama managed collection operasyon yükünü azaltır.

**Sade anlam:** “Minimal operational overhead” → Ayrı Prometheus sunucusunun bakımını üstlenmeden metric topla.

**Kaynak:** SCP16-Q55; [teknik belge](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q25 B

**Doğru seçenek:** Remove the Dockerfile from the submitted source and redeploy from source using the supported buildpacks runtime.

**Karar:** Source deploy’da Dockerfile varsa bu dosya build için kullanılır; yoksa desteklenen source buildpacks ile hazırlanır.

**Eleme koşulu:** Runtime env veya image pull izni builder seçimini değiştirmez.

**Sade anlam:** “Dockerfile instructions being executed” → Source’da Dockerfile bulunduğu için buildpacks yolu seçilmemiş.

**Kaynak:** OFFICIAL-BP1; [teknik belge](https://docs.cloud.google.com/run/docs/deploying-source-code).

**Önceki ilişki:** Ek resmî kaynak; ilgili önceki kimlik/konfigürasyon mekanizmaları pekiştirilebilir.

## Q26 A + C

**Doğru seçenek:** Store the default project files outside /home in the container image, such as under /opt/project-template. / Add an idempotent container startup script that copies missing defaults into the mounted home directory after user initialization.

**Karar:** Kalıcı /home mount’u image’daki home içeriğini örter. Default’u /opt’ta tutup startup’ta yalnız eksik dosyayı kopyalarsın.

**Eleme koşulu:** Her açılışta overwrite kullanıcı değişikliklerini kaybettirir; kalıcı disk kaldırmak preservation şartını bozar.

**Sade anlam:** “Defaults only when absent” → Başlangıç dosyasını eksikse getir; geliştiricinin mevcut dosyasını ezme.

**Kaynak:** OFFICIAL-WS1; [teknik belge](https://docs.cloud.google.com/workstations/docs/customize-container-images).

**Önceki ilişki:** S11 Q14 / Workstations home mount mekanizması; çift gereksinimli pekiştirme.

## Q27 A

**Doğru seçenek:** Enable Binary Authorization and configure a policy requiring attestations from the built-by-cloud-build attestor before allowing image deployment.

**Karar:** Enforced Binary Authorization policy built-by-cloud-build attestation ister.

**Eleme koşulu:** Private repo veya label build provenance’a dair aynı kriptografik deployment kontrolünü sağlamaz. Bu attestation tek başına test geçiş kanıtı değildir.

**Sade anlam:** “Enforce during admission” → Deployment yapılırken imzalı build kanıtını kontrol edip gerektiğinde engelle.

**Kaynak:** SCP17-Q42; [teknik belge](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q28 A

**Doğru seçenek:** Build a custom container image that extends a Cloud Workstations base image, includes the required JDK and pre-installed Cloud Code plugin, and reference that image in the workstation configuration.

**Karar:** Standart araçları custom container image içine kurup workstation configuration ile dağıtırsın.

**Eleme koşulu:** Her geliştiricinin elle kurması başlangıçta hazır ve tutarlı ortam şartını karşılamaz.

**Sade anlam:** “Already available without setup scripts” → Geliştirici açınca araçlar hazır olsun; elle kurulum yapmasın.

**Kaynak:** SCP12-Q08; [teknik belge](https://docs.cloud.google.com/workstations/docs/customize-container-images).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q29 D

**Doğru seçenek:** Rewrite the query to use bound query parameters in place of the inline literal values so Spanner can reuse the cached execution plan across requests.

**Karar:** Inline user values yerine bound parameters SQL injection riskini azaltır ve query plan reuse’a yardımcı olur.

**Eleme koşulu:** STORING index’e ek column koyar; query-result cache veya literal normalization ayarı değildir.

**Sade anlam:** “Bound query parameters” → Kullanıcı değerini SQL metnine yapıştırma; parametre olarak gönder.

**Kaynak:** SCP16-Q46; [teknik belge](https://docs.cloud.google.com/spanner/docs/sql-best-practices).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q30 B

**Doğru seçenek:** Use the CloudEvent source and id as a stable key and atomically record that key with the charge in a database transaction.

**Karar:** CloudEvent source+id aynı event’i belirler. Unique kayıt ve charge aynı transaction’da duplicate race’i önler.

**Eleme koşulu:** Local memory başka instance veya restart için yeterli değildir; filename farklı event’leri birleştirebilir.

**Sade anlam:** “Duplicate concurrently; legitimate events” → Aynı olayın yarışan kopyalarını engelle, başka gerçek olayları kaybetme.

**Kaynak:** OFFICIAL-EA3; [teknik belge](https://docs.cloud.google.com/eventarc/docs/retry-events).

**Önceki ilişki:** Ek resmî kaynak; ilgili önceki kimlik/konfigürasyon mekanizmaları pekiştirilebilir.

## Q31 C

**Doğru seçenek:** Implement appropriate step retries and error handling inside the workflow, with an explicit recovery process for terminal execution failures.

**Karar:** Workflow execution başlayınca event acknowledgment gerçekleşir. Sonraki execution failure için workflow retries/recovery gerekir.

**Eleme koşulu:** Eventarc teslim retry’si başlatılmış workflow’un business failure’ını otomatik replay etmez.

**Sade anlam:** “Delivery succeeded; workflow then fails” → Olay teslim edildi; sonra iş akışı içinde hata oluştu.

**Kaynak:** OFFICIAL-EA2; [teknik belge](https://docs.cloud.google.com/eventarc/docs/retry-events).

**Önceki ilişki:** Ek resmî kaynak; ilgili önceki kimlik/konfigürasyon mekanizmaları pekiştirilebilir.

## Q32 D

**Doğru seçenek:** Configure the HorizontalPodAutoscaler‘s behavior.scaleUp policies in autoscaling/v2 with a higher Pods or Percent rate and a short stabilization window, while leaving scaleDown conservative.

**Karar:** autoscaling/v2 behavior.scaleUp ile büyüme hızı ayarlanır; scaleDown ayrı tutulur.

**Eleme koşulu:** CPU hedefini çok düşürmek kalıcı fazla kapasite üretir; doğrudan büyüme hızını ayarlamaz.

**Sade anlam:** “More aggressively while keeping scale-down conservative” → Hızlı büyüsün, küçülürken acele etmesin.

**Kaynak:** SCP13-Q10; [teknik belge](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q33 B

**Doğru seçenek:** Create an execution-specific callback endpoint, provide it to the approval service, and use events.await_callback with an appropriate timeout.

**Karar:** Execution callback URL oluşturulur; await_callback aynı execution içinde bekler ve yetkili callback ile devam eder.

**Eleme koşulu:** Callback çağıranının workflows.callbacks.send izni gerekir; süresiz bekleme veya polling gerekmez.

**Sade anlam:** “Without repeatedly polling” → Sürekli durum sormadan callback gelmesini bekle.

**Kaynak:** OFFICIAL-WF3; [teknik belge](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints).

**Önceki ilişki:** Ek resmî kaynak; ilgili önceki kimlik/konfigürasyon mekanizmaları pekiştirilebilir.

## Q34 B

**Doğru seçenek:** Grant the Artifact Registry Reader role on the Artifact Registry repository in project-b to the Compute Engine default service account from project-a.

**Karar:** Repository üzerinde node service account’a Artifact Registry Reader verilir.

**Eleme koşulu:** Image pull’u uygulamanın KSA’sına verilen bucket veya runtime API izni çözmez; node access scope da uygun olmalıdır.

**Sade anlam:** “Pull images from project-b” → Container başlamadan image’ı hangi makine kimliği indiriyor?

**Kaynak:** SCP16-Q21; [teknik belge](https://docs.cloud.google.com/artifact-registry/docs/integrate-gke).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q35 B

**Doğru seçenek:** Grant order-orchestrator Cloud Run Invoker on the worker service.

**Karar:** Çağrı token’ı workflow SA’yı temsil eder; hedef service’in Invoker izni bu kimliğe verilir.

**Eleme koşulu:** Worker runtime bucket yetkisi inbound invocation yetkisi değildir.

**Sade anlam:** “Before worker code starts” → Hata inbound çağrı izninde; worker’ın bucket erişimine daha gelinmedi.

**Kaynak:** OFFICIAL-WF4; [teknik belge](https://docs.cloud.google.com/workflows/docs/authenticate-from-workflow).

**Önceki ilişki:** Ek resmî kaynak; ilgili önceki kimlik/konfigürasyon mekanizmaları pekiştirilebilir.

## Q36 B

**Doğru seçenek:** Use the Identity Platform tenant management API through the Admin SDK to programmatically create a new tenant and configure its identity providers during your onboarding workflow.

**Karar:** Admin SDK/tenant management API ile tenant ve provider ayarları otomatik hazırlanır.

**Eleme koşulu:** Custom claim ayrı managed user directory değildir; mevcut shared backend için yeni proje oluşturmak gereksizdir.

**Sade anlam:** “No manual console steps” → Müşterinin ayrı kimlik alanı kodla oluşturulsun.

**Kaynak:** SCP14-Q32; [teknik belge](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-managing-tenants).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q37 C

**Doğru seçenek:** 120%, because the HPA calculates utilization as a percentage of the container‘s CPU request (300m / 250m), not its limit.

**Karar:** 300m / 250m = 120%. Utilization request üzerinden hesaplanır.

**Eleme koşulu:** 1000m limit’e bölmek 30% verir ama HPA utilization’ın paydası değildir. Kaynak açıklaması başka sidecar sorusuna aittir.

**Sade anlam:** “Average CPU utilization” → Kullanılan CPU’yu request’e oranla; limit’e değil.

**Kaynak:** SCP17-Q57; [teknik belge](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q38 A

**Doğru seçenek:** Create a Cloud Build private pool with the validated private network connectivity and configure the build trigger to use that worker pool.

**Karar:** Build’i gerekli private network yoluna sahip private worker pool’da çalıştırırsın.

**Eleme koşulu:** Auth Proxy IAM ve bağlantı güvenliği sağlar; eksik network route’u yaratmaz. VPC peering transitif değildir.

**Sade anlam:** “Cannot reach internal IP addresses” → Yetki yeterli olsa bile build makinesinin network yolu eksik.

**Kaynak:** SCP14-Q01; [teknik belge](https://docs.cloud.google.com/build/docs/private-pools/use-in-private-network).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q39 A

**Doğru seçenek:** Create a single-field or composite index with collection group scope for the ‘reviews‘ collection on the rating field.

**Karar:** reviews için collection group scope’da rating index’i ve collectionGroup query kullanılır.

**Eleme koşulu:** Her tenant collection’ı için index tanımlamak cross-collection-group sorgu index’i değildir. Client security rules ayrıca uygun olmalıdır.

**Sade anlam:** “All reviews across all tenants” → Aynı isimli bütün reviews subcollection’larını birlikte sorgula.

**Kaynak:** SCP18-Q17; [teknik belge](https://firebase.google.com/docs/firestore/query-data/index-overview).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q40 C

**Doğru seçenek:** Mount the ConfigMap as a volume at the path where your application reads the configuration file. Configure your application to watch for file changes.

**Karar:** ConfigMap normal volume olarak mount edilir; uygulama değişen dosyayı yeniden okur.

**Eleme koşulu:** Env variable mevcut process’te güncellenmez; subPath mount update almaz; yayılma anlık değildir.

**Sade anlam:** “Without requiring a pod restart” → Process çalışırken güncel ayar dosyasını yeniden okusun.

**Kaynak:** SCP13-Q43; [teknik belge](https://kubernetes.io/docs/concepts/configuration/configmap/).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q41 A

**Doğru seçenek:** Use point-in-time recovery to restore the cluster‘s data to a new cluster at a timestamp just before the DELETE ran, then validate and reconcile the recovered rows.

**Karar:** DELETE öncesi timestamp’e yeni cluster restore edilir, sonra gerekli kayıtlar uzlaştırılır.

**Eleme koşulu:** Replica logical DELETE’i de kopyalar; mevcut veriyi dump etmek silinmiş satırları geri getirmez.

**Sade anlam:** “Keep the original cluster intact” → Eski durumu ayrı cluster’a çıkar; inceleme yapılan mevcut cluster’ı ezme.

**Kaynak:** SCP18-Q08; [teknik belge](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q42 B

**Doğru seçenek:** Configure Multidimensional Pod Autoscaling so the workload scales horizontally on CPU while a vertical component right-sizes memory requests.

**Karar:** MultidimPodAutoscaler CPU’ya göre replica, memory için request ayarı yapar.

**Eleme koşulu:** HPA memory request’i değiştirmez; aynı CPU utilization’ını HPA ve VPA ile birlikte yönetmek çatışabilir. Beta kullanımına izin verilmiştir.

**Sade anlam:** “Replica count on CPU; memory requests right-sized” → CPU yükünde Pod sayısı, bellek ihtiyacında Pod boyutu değişsin.

**Kaynak:** SCP17-Q58; [teknik belge](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multidimensional-pod-autoscaling).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q43 A + B

**Doğru seçenek:** Grant event-starter Workflows Invoker on the destination workflow. / Grant document-orchestrator Cloud Run Invoker on the processor service.

**Karar:** Eventarc workflow’u trigger identity ile başlatır; workflow sonraki çağrıyı kendi SA’sıyla yapar.

**Eleme koşulu:** Birinci çağırana ikinci hedef izni vermek eksik workflow-start iznini çözmez.

**Sade anlam:** “Trigger uses event-starter; workflow runs as document-orchestrator” → Başlatan kimlik ile workflow kodunun çağıran kimliği ayrı.

**Kaynak:** OFFICIAL-EA1; [teknik belge](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-storage).

**Önceki ilişki:** Ek resmî kaynak; ilgili önceki kimlik/konfigürasyon mekanizmaları pekiştirilebilir.

## Q44 C

**Doğru seçenek:** Configure Cloud Code to use Google Cloud buildpacks, which auto-detect the language and create container images from source code.

**Karar:** Google buildpacks desteklenen source dilini detect edip Dockerfile olmadan container image üretir.

**Eleme koşulu:** Kaniko mevcut Dockerfile build eder; dosya uzantısından otomatik Dockerfile üretme mekanizması değildir.

**Sade anlam:** “Without writing a Dockerfile” → Desteklenen source’dan buildpacks ile image üret.

**Kaynak:** SCP14-Q49; [teknik belge](https://docs.cloud.google.com/docs/buildpacks/overview).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q45 B

**Doğru seçenek:** Disable the previous secret version immediately after rotation. If a rollback is required within 7 days, enable the version again; otherwise destroy the version after 7 days.

**Karar:** Disable API üzerinden okumayı durdurur; enable ile rollback mümkündür, sonra destroy edilir.

**Eleme koşulu:** Secret Manager disable, dış sağlayıcıdaki gerçek credential’ı iptal etmez. Soruda yalnız Secret Manager erişimi istenir.

**Sade anlam:** “Unreadable through Secret Manager; rollback” → Değeri şimdilik okunamaz yap, gerektiğinde geri açabil.

**Kaynak:** SCP13-Q23; [teknik belge](https://docs.cloud.google.com/secret-manager/docs/disable-secret-version).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q46 D

**Doğru seçenek:** Define Skaffold modules in your skaffold.yaml file by naming each configuration with the metadata.name field, then select specific modules to build in the Cloud Code run configuration.

**Karar:** metadata.name ile named configuration/module tanımlayıp seçili modülü çalıştırırsın; requires bağımlılıkları ifade eder.

**Eleme koşulu:** VS Code workspace seçmek build/deploy bağımlılıklarını tanımlamaz. Seçili modül bağımlılıklarını da içerebilir.

**Sade anlam:** “Only the frontend while maintaining dependencies” → Frontend üzerinde çalış; gerekli backend bağımlılıklarını tanımlı tut.

**Kaynak:** SCP17-Q41; [teknik belge](https://skaffold.dev/docs/design/config/).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q47 A

**Doğru seçenek:** Ask Gemini Code Assist to refactor the function so the current time is an injected parameter, and update the test to pass a fixed timestamp.

**Karar:** Zamanı parametre veya clock dependency olarak dışarıdan verip testte sabit timestamp kullanırsın.

**Eleme koşulu:** Retry zamana bağlı koşulu çözmez; CI makinesinin saatini değiştirmek gereksiz ortam bağımlılığı yaratır.

**Sade anlam:** “Depends on the current date” → Test sonucu bugünün tarihine göre değişmesin.

**Kaynak:** SCP18-Q12; [teknik belge](https://docs.python.org/3/library/unittest.mock.html).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q48 D

**Doğru seçenek:** Verify the x-goog-iap-jwt-assertion header in your application code by validating the JWT signature using Google‘s public keys and checking the audience claim.

**Karar:** IAP JWT signature, expected audience, issuer ve süre claim’lerini doğrularsın.

**Eleme koşulu:** Düz email header’ını güvenilir kabul etmek forge edilmiş kimliği ayırt etmez.

**Sade anlam:** “Forge identity headers” → Düz header’daki kimlik iddiasına güvenme; imzalı kanıtı doğrula.

**Kaynak:** SCP12-Q15; [teknik belge](https://docs.cloud.google.com/iap/docs/signed-headers-howto).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q49 C

**Doğru seçenek:** Set the alignment period to aggregate memory utilization over a consistent time interval. Configure a retest window duration that requires the threshold to be exceeded for multiple consecutive evaluation periods.

**Karar:** Retest window, threshold ihlalinin belirlenen süre boyunca devam etmesini şart koşar.

**Eleme koşulu:** Alignment örnekleri düzenler; tek başına sustained violation koşulunun yerine geçmez.

**Sade anlam:** “For a sustained period” → Bir anlık spike değil, belirli süre devam eden ihlal alarm üretsin.

**Kaynak:** SCP16-Q26; [teknik belge](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.

## Q50 A

**Doğru seçenek:** Configure a rotation period and next rotation time on the secret in Secret Manager, and set a topic to receive rotation notifications. Configure the Cloud Run function as a Pub/Sub subscriber to the rotation topic so it adds a new secret version when triggered.

**Karar:** Secret Manager rotation schedule Pub/Sub bildirimi üretir; subscriber gerçek parolayı değiştirip yeni version yazar.

**Eleme koşulu:** Schedule tek başına credential üretmez veya DB parolasını değiştirmez; KMS key rotation da bunu yapmaz.

**Sade anlam:** “Rotation notifications” → Vakti gelince bildirim al; gerçek parolayı değiştiren işlem subscriber’da olsun.

**Kaynak:** SCP18-Q23; [teknik belge](https://docs.cloud.google.com/secret-manager/docs/rotation-recommendations).

**Önceki ilişki:** Kaynak uyarlaması/karma pekiştirme; yeni temel kapsam iddiası yok.
