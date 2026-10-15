# PCD-S16 Türkçe cevap anahtarı

İlk çözüm tamamlandıktan sonra aç. Kaynak, doğru seçenek, karar ve yakın yanlışın nedeni her sorunun altında bulunur. Kaynak platform anahtarı bağımsız doğruluk kanıtı sayılmamıştır.

| Soru | Doğru | Konu |
|---|---|---|
| 01 | A | structured application logs |
| 02 | B | build versus step timeout |
| 03 | C | transactional read modify write |
| 04 | D | Cloud SQL proxy sidecar |
| 05 | D | Google API connector |
| 06 | C | Java runtime selection |
| 07 | A+B | versioned immutable configuration |
| 08 | A | multi stage runtime image |
| 09 | C | bucket event routing |
| 10 | B | declarative release configuration |
| 11 | A | idle versus running timeout |
| 12 | A | multiple notification channels |
| 13 | B | managed Kubernetes object state metrics |
| 14 | D | parallel build dependency graph |
| 15 | B | application layer encryption boundary |
| 16 | B | email link authentication |
| 17 | C | subworkflow reuse scope |
| 18 | A | OOMKilled versus node capacity |
| 19 | A | unit test prompt context |
| 20 | B | repository push identity |
| 21 | A | workload principal resource access |
| 22 | C | event driven scale to zero |
| 23 | C | Python startup entrypoint |
| 24 | D | metrics and logs dashboard |
| 25 | D | developer access role |
| 26 | D | cleanup keep versus delete |
| 27 | C | IDE target Kubernetes context |
| 28 | C+D | Firestore cache metadata |
| 29 | C | OIDC audience boundary |
| 30 | A | readiness versus liveness |
| 31 | C | independent consumers and triggers |
| 32 | C | canary phase advancement |
| 33 | C | bounded batch Job execution |
| 34 | A | task creation deduplication |
| 35 | C | Firestore emulator test scope |
| 36 | A | planned disruption budget |
| 37 | B | Cloud Code debugger setup |
| 38 | B | images build result provenance |
| 39 | B | persistent home versus VM lifecycle |
| 40 | B | Service selector endpoints |
| 41 | D | catch failure versus success |
| 42 | D | namespace scoped IAM principal set |
| 43 | C+E | reproducible source build inputs |
| 44 | B | rolling update capacity |
| 45 | A | investigation follow up |
| 46 | A | environment build substitutions |
| 47 | D | source trigger location |
| 48 | D | zone topology distribution |
| 49 | D | HTTP acknowledgment boundary |
| 50 | B | Bigtable key range heatmap |

## Q01 A

**Doğru seçenek:** Write one JSON log entry per line to stdout, including severity, message, and orderId fields.

**Karar:** JSON stdout girdileri yapılandırılmış log alanları sağlar; orderId üzerinden filtrelenir.

**Eleme koşulu:** Pod label uygulama isteğinin değişen metadata alanı değildir.

**Sade anlam:** JSON stdout girdileri yapılandırılmış log alanları sağlar; orderId üzerinden filtrelenir.

**Kaynak:** SCP13-Q18; [teknik belge](https://docs.cloud.google.com/logging/docs/structured-logging).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q02 B

**Doğru seçenek:** Set the top-level build timeout to 2400s and keep any step timeout within that build budget.

**Karar:** Top-level timeout çalışan build süresini sınırlar; step timeout bunu aşamaz.

**Eleme koşulu:** Kaynak anahtarı belirsizdi: soruda açık 20 dakika build sınırı koyuldu; timeout options altına yazılmaz.

**Sade anlam:** Top-level timeout çalışan build süresini sınırlar; step timeout bunu aşamaz.

**Kaynak:** SCP13-Q02; [teknik belge](https://docs.cloud.google.com/build/docs/build-config-file-schema).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q03 C

**Doğru seçenek:** Read and validate the balances, then update both documents inside a Firestore transaction that can retry on conflicts.

**Karar:** Karar verilen okumalar ve iki yazma aynı transaction içinde olmalı.

**Eleme koşulu:** WriteBatch iki yazmayı atomik yapar ama dışarıdaki okumaların hâlâ geçerli olduğunu doğrulamaz.

**Sade anlam:** Karar verilen okumalar ve iki yazma aynı transaction içinde olmalı.

**Kaynak:** SCP12-Q18; [teknik belge](https://firebase.google.com/docs/firestore/manage-data/transactions).

**Önceki ilişki:** S15 Q03 atomik batch ile ilişkili bilinçli ayrım: burada karar öncesi okuma da tutarlı olmalı.

## Q04 D

**Doğru seçenek:** Run the Cloud SQL Auth Proxy as a sidecar using private-IP connectivity and have the application connect through localhost.

**Karar:** Proxy sidecar uygulamayla aynı Pod network alanında localhost sunar; private IP yolu ayrıca gerekir.

**Eleme koşulu:** Private IP tek başına istenen proxy-managed auth/TLS mekanizması değildir.

**Sade anlam:** Proxy sidecar uygulamayla aynı Pod network alanında localhost sunar; private IP yolu ayrıca gerekir.

**Kaynak:** SCP13-Q37; [teknik belge](https://docs.cloud.google.com/sql/docs/mysql/connect-kubernetes-engine).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q05 D

**Doğru seçenek:** Use the supported connector with its operation-waiting behavior and an appropriate connector timeout.

**Karar:** Desteklenen connector auth ve long-running operation beklemesini yönetir.

**Eleme koşulu:** Connector kapsamı kontrol edilir; her HTTP çağrısı kendiliğinden tamamlanana kadar beklemez.

**Sade anlam:** Desteklenen connector auth ve long-running operation beklemesini yönetir.

**Kaynak:** OFFICIAL-S16-WF1; [teknik belge](https://docs.cloud.google.com/workflows/docs/connectors).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q06 C

**Doğru seçenek:** Supply GOOGLE_RUNTIME_VERSION to the buildpacks build environment with the supported JDK version constraint.

**Karar:** Java buildpack runtime seçimi build-time GOOGLE_RUNTIME_VERSION ile yapılır.

**Eleme koşulu:** Runtime env mevcut image içindeki JDK kurulumunu değiştirmez.

**Sade anlam:** Java buildpack runtime seçimi build-time GOOGLE_RUNTIME_VERSION ile yapılır.

**Kaynak:** OFFICIAL-S16-BP1; [teknik belge](https://docs.cloud.google.com/docs/buildpacks/java).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q07 A+B

**Doğru seçenek:** Change the Deployment Pod template to reference the new ConfigMap and roll out that template. / Create a new immutable ConfigMap with a different name containing the approved values.

**Karar:** Yeni immutable kaynak oluşturulur ve Pod template referansı değişir; eski kaynak rollback için korunur.

**Eleme koşulu:** Immutable data in-place değiştirilemez ve immutable true geri alınamaz.

**Sade anlam:** Yeni immutable kaynak oluşturulur ve Pod template referansı değişir; eski kaynak rollback için korunur.

**Kaynak:** SCP12-Q09; [teknik belge](https://kubernetes.io/docs/concepts/configuration/configmap/).

**Önceki ilişki:** S13 immutable ConfigMap bilgisiyle bilinçli pekiştirme; yeni kapsam sayılmaz.

## Q08 A

**Doğru seçenek:** Use a multi-stage Dockerfile and copy only the required executable and runtime files into the final stage.

**Karar:** Build toolchain builder stage’de kalır; runtime stage gerekli artifactları içerir.

**Eleme koşulu:** Sonraki layer’da silmek önceki image layer’ındaki içeriği ortadan kaldırmaz.

**Sade anlam:** Build toolchain builder stage’de kalır; runtime stage gerekli artifactları içerir.

**Kaynak:** SCP15-Q50; [teknik belge](https://docs.cloud.google.com/build/docs/optimize-builds/building-leaner-containers).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q09 C

**Doğru seçenek:** An Eventarc Standard trigger filtered by the object-finalized event type and the source bucket, targeting the Cloud Run service.

**Karar:** Kaynak olay türü + bucket filtresi ve hedef servis Eventarc trigger’da tanımlanır.

**Eleme koşulu:** Pub/Sub mesajlaşma ile bir bucket olayını hedefe bağlayan trigger aynı görev değildir.

**Sade anlam:** Kaynak olay türü + bucket filtresi ve hedef servis Eventarc trigger’da tanımlanır.

**Kaynak:** OFFICIAL-S16-EA1; [teknik belge](https://docs.cloud.google.com/run/docs/tutorials/eventarc).

**Önceki ilişki:** S15 event teslimi ve IAM sorularından farklı: burada routing/filter seçimi ölçülür.

## Q10 B

**Doğru seçenek:** Keep Deployment manifests in version control, review changes, and create or update resources with kubectl apply.

**Karar:** Declarative manifest Git geçmişi konfigürasyon değişimini görünür ve yeniden uygulanabilir yapar.

**Eleme koşulu:** apply tek başına sürekli drift reconciliation sağlamaz; soruda GitOps controller yok.

**Sade anlam:** Declarative manifest Git geçmişi konfigürasyon değişimini görünür ve yeniden uygulanabilir yapar.

**Kaynak:** SCP17-Q19; [teknik belge](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q11 A

**Doğru seçenek:** Configure an idle timeout with the stop action and avoid imposing a conflicting running timeout.

**Karar:** idleTimeout idle duruma, runningTimeout toplam çalışma süresine bağlıdır.

**Eleme koşulu:** IDE/application ayarı Workstations VM yaşam döngüsü ayarı değildir.

**Sade anlam:** idleTimeout idle duruma, runningTimeout toplam çalışma süresine bağlıdır.

**Kaynak:** OFFICIAL-S16-WS1; [teknik belge](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q12 A

**Doğru seçenek:** Attach the three notification channels to the alerting policy.

**Karar:** Policy birden fazla native notification channel kullanabilir.

**Eleme koşulu:** Custom fanout mümkün ama gerekmediği belirtilmiş; ek işletim yükü yaratır.

**Sade anlam:** Policy birden fazla native notification channel kullanabilir.

**Kaynak:** SCP15-Q48; [teknik belge](https://docs.cloud.google.com/monitoring/support/notification-options).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q13 B

**Doğru seçenek:** Enable the supported GKE kube state metrics collection packages for the required Kubernetes objects.

**Karar:** GKE managed kube state metrics koleksiyonu Pod/Deployment gibi Kubernetes nesnelerinin durum metriklerini sağlar.

**Eleme koşulu:** Container resource usage ile Kubernetes object state aynı metric grubu değildir; managed collection mevcutken kendi exporter altyapısı gerekmez.

**Sade anlam:** GKE managed kube state metrics koleksiyonu Pod/Deployment gibi Kubernetes nesnelerinin durum metriklerini sağlar.

**Kaynak:** SCP12-Q22; [teknik belge](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics).

**Önceki ilişki:** Önceki seçki kayıtlarında kaynak ID kullanılmamış; S13/S15 gövde ve kararlarıyla karşılaştırıldı. Benzer temel kavramlar yeni kapsam sayılmaz.

## Q14 D

**Doğru seçenek:** Set waitFor: ["-"] on both tests and waitFor: ["unit", "integration"] on packaging.

**Karar:** waitFor [-] başlangıcı, step id listesi bağımlılıkları tanımlar.

**Eleme koşulu:** Alanı kaldırmak otomatik paralel dependency inference değildir.

**Sade anlam:** waitFor [-] başlangıcı, step id listesi bağımlılıkları tanımlar.

**Kaynak:** SCP16-Q24; [teknik belge](https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q15 B

**Doğru seçenek:** Enable GKE application-layer secrets encryption with the Cloud KMS key and the required service-agent key access.

**Karar:** GKE application-layer encryption etcd Secret verisini KMS ile korur; yetkili API okumaları ayrı RBAC konusudur.

**Eleme koşulu:** Kaynak hatalı API-reader tehdidiyle encryption çözümünü karıştırıyordu; kapsam storage olarak düzeltildi.

**Sade anlam:** GKE application-layer encryption etcd Secret verisini KMS ile korur; yetkili API okumaları ayrı RBAC konusudur.

**Kaynak:** SCP16-Q50; [teknik belge](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets).

**Önceki ilişki:** S15 Secret Manager sorusundan farklı koşul: Kubernetes Secrets korunacak ve customer-controlled etcd encryption isteniyor.

## Q16 B

**Doğru seçenek:** Enable email-link sign-in in the email provider and implement the supported send-link and complete-sign-in client flow.

**Karar:** Email link yerleşik passwordless kimlik doğrulama akışıdır.

**Eleme koşulu:** Email sahibi olmak Google OAuth hesabı sahibi olmakla aynı değil.

**Sade anlam:** Email link yerleşik passwordless kimlik doğrulama akışıdır.

**Kaynak:** SCP12-Q21; [teknik belge](https://firebase.google.com/docs/auth/web/email-link-auth).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q17 C

**Doğru seçenek:** Define a parameterized subworkflow and call it from the branches.

**Karar:** Subworkflow aynı tanım içinde yeniden kullanılabilir parametreli rutin sağlar.

**Eleme koşulu:** Subworkflow ayrı workflow tanımları arasında global library değildir.

**Sade anlam:** Subworkflow aynı tanım içinde yeniden kullanılabilir parametreli rutin sağlar.

**Kaynak:** OFFICIAL-S16-WF2; [teknik belge](https://docs.cloud.google.com/workflows/docs/reference/syntax/subworkflows).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q18 A

**Doğru seçenek:** Raise the container memory limit to a validated value above the startup peak and review the request against scheduling policy.

**Karar:** Container memory limit aşımı OOMKilled nedeni; node boşluğu limit’i kaldırmaz.

**Eleme koşulu:** S15 Pending/insufficient CPU’dan farklı: burada Pod yerleşmiş, container kendi memory limit’ine çarpıyor.

**Sade anlam:** Container memory limit aşımı OOMKilled nedeni; node boşluğu limit’i kaldırmaz.

**Kaynak:** OFFICIAL-S16-GKE1; [teknik belge](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q19 A

**Doğru seçenek:** Explicitly add the relevant implementation, helper, and example-test files as prompt context and request tests covering their interactions.

**Karar:** İlgili dosyaları açık context olarak eklemek eksik helper/test örneğini modele verir.

**Eleme koşulu:** Enterprise repo indexing gerekmeden yerel prompt context kullanılabilir; testler ayrıca incelenir.

**Sade anlam:** İlgili dosyaları açık context olarak eklemek eksik helper/test örneğini modele verir.

**Kaynak:** SCP12-Q04; [teknik belge](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini).

**Önceki ilişki:** Kaynak ID önceki seçkilerde kullanılmamış; benzer temel konular önceki çalışmalarda bulunabilir.

## Q20 B

**Doğru seçenek:** Artifact Registry Writer to the build service account.

**Karar:** Image push yapan build SA repository üzerinde Writer ister.

**Eleme koşulu:** Runtime identity ve build identity farklı; Reader push izni vermez.

**Sade anlam:** Image push yapan build SA repository üzerinde Writer ister.

**Kaynak:** SCP17-Q24; [teknik belge](https://docs.cloud.google.com/artifact-registry/docs/access-control).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q21 A

**Doğru seçenek:** Grant the workload principal Pub/Sub Publisher on the intended topic using an IAM allow policy.

**Karar:** Kimlik oluşması kaynak iznini kendiliğinden vermez; workload principal topic publisher olmalı.

**Eleme koşulu:** KSA atamak tek başına Pub/Sub IAM izni sağlamaz.

**Sade anlam:** Kimlik oluşması kaynak iznini kendiliğinden vermez; workload principal topic publisher olmalı.

**Kaynak:** SCP15-Q44; [teknik belge](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

**Önceki ilişki:** Önceki IAM zincirlerinin bilinçli pekiştirmesi; farklı hedef Pub/Sub.

## Q22 C

**Doğru seçenek:** Use KEDA with an appropriate Pub/Sub event-source scaler to activate workers from zero and scale them with demand.

**Karar:** KEDA event source metriğiyle sıfır replica durumundan aktivasyon ve tekrar idle durumda sıfıra iniş sağlar.

**Eleme koşulu:** CPU metriği sıfır Pod durumunda yoktur; Kubernetes HPA scale-to-zero hakkında tüm yapılandırmalara genelleme yapılmaz, soru conventional CPU HPA ile sınırlandırıldı.

**Sade anlam:** KEDA event source metriğiyle sıfır replica durumundan aktivasyon ve tekrar idle durumda sıfıra iniş sağlar.

**Kaynak:** SCP14-Q25; [teknik belge](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-zero-using-keda).

**Önceki ilişki:** Önceki seçki kayıtlarında kaynak ID kullanılmamış; S13/S15 gövde ve kararlarıyla karşılaştırıldı. Benzer temel kavramlar yeni kapsam sayılmaz.

## Q23 C

**Doğru seçenek:** Set GOOGLE_ENTRYPOINT to the desired command in the build environment and rebuild the image.

**Karar:** GOOGLE_ENTRYPOINT buildpack tarafından startup command üretiminde kullanılır.

**Eleme koşulu:** Builder customization ile runtime IAM birbirinin alternatifi değildir.

**Sade anlam:** GOOGLE_ENTRYPOINT buildpack tarafından startup command üretiminde kullanılır.

**Kaynak:** OFFICIAL-S16-BP2; [teknik belge](https://docs.cloud.google.com/docs/buildpacks/python).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q24 D

**Doğru seçenek:** A Cloud Monitoring custom dashboard with a container-memory chart and a logs panel filtered to the workload.

**Karar:** Custom dashboard native metric chart ve logs panel içerebilir.

**Eleme koşulu:** Kaynak iframe/customize UI varsayımı yerine belgelenmiş logs panel kullanıldı.

**Sade anlam:** Custom dashboard native metric chart ve logs panel içerebilir.

**Kaynak:** SCP15-Q55; [teknik belge](https://docs.cloud.google.com/monitoring/charts/view-logs).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q25 D

**Doğru seçenek:** Grant the developer the Cloud Workstations User role at the appropriate workstation scope.

**Karar:** Workstations User workstation kullanım erişimidir; config yönetimi ayrıdır.

**Eleme koşulu:** Workstations User workstation kapsamındadır; gerekli project-level Operation Viewer soruda zaten verilmiştir.

**Sade anlam:** Workstations User workstation kullanım erişimidir; config yönetimi ayrıdır.

**Kaynak:** OFFICIAL-S16-WS2; [teknik belge](https://docs.cloud.google.com/workstations/docs/access-control).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q26 D

**Doğru seçenek:** Configure a conditional delete policy for age, a keep policy matching the release- tag prefix, and validate the result in dry-run mode.

**Karar:** Delete age koşulu ile keep tagPrefixes birlikte kullanılır; keep eşleşmesi korunur, dry-run önizler.

**Eleme koşulu:** Kaynak versionPrefixes’i Docker tag prefix ile karıştırıyordu; tagPrefixes doğru alan.

**Sade anlam:** Delete age koşulu ile keep tagPrefixes birlikte kullanılır; keep eşleşmesi korunur, dry-run önizler.

**Kaynak:** SCP17-Q08; [teknik belge](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy).

**Önceki ilişki:** Kaynak ID önceki seçkilerde kullanılmamış; benzer temel konular önceki çalışmalarda bulunabilir.

## Q27 C

**Doğru seçenek:** Select the minikube Kubernetes context in the Cloud Code run configuration before starting the development run.

**Karar:** Kubernetes context hedef cluster/kimlik/namespace bağlamını seçer.

**Eleme koşulu:** Namespace veya image tag fiziksel hedef cluster’ı değiştirmez.

**Sade anlam:** Kubernetes context hedef cluster/kimlik/namespace bağlamını seçer.

**Kaynak:** SCP16-Q04; [teknik belge](https://docs.cloud.google.com/code/docs/vscode/deploying-a-k8-app).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q28 C+D

**Doğru seçenek:** Request metadata-change events so a metadata-only transition can update the UI. / Inspect the snapshot metadata fromCache value to label cache versus server results.

**Karar:** fromCache kaynağı belirtir; includeMetadataChanges metadata-only değişimi bildirir.

**Eleme koşulu:** hasPendingWrites local write durumudur; network bağlantısı snapshot kaynağını kanıtlamaz.

**Sade anlam:** fromCache kaynağı belirtir; includeMetadataChanges metadata-only değişimi bildirir.

**Kaynak:** SCP17-Q15; [teknik belge](https://firebase.google.com/docs/firestore/query-data/listen).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q29 C

**Doğru seçenek:** Configure OIDC authentication with the expected audience of the destination Cloud Run service, rather than the unrelated service.

**Karar:** Invoker IAM hakkı doğru olsa da token audience hedefle uyuşmalı.

**Eleme koşulu:** S15 sorusunda audience doğru kabul edilmişti; burada hata özellikle audience.

**Sade anlam:** Invoker IAM hakkı doğru olsa da token audience hedefle uyuşmalı.

**Kaynak:** OFFICIAL-S16-WF3; [teknik belge](https://docs.cloud.google.com/workflows/docs/authenticate-from-workflow).

**Önceki ilişki:** S15 Q35 kimlik zincirinden farklı: IAM yeterli, token audience hatalı.

## Q30 A

**Doğru seçenek:** A readiness probe that fails while the application cannot serve traffic.

**Karar:** Readiness trafik almayı, liveness restart kararını yönetir.

**Eleme koşulu:** Geçici trafik dışına alma için process restart gerekmiyor.

**Sade anlam:** Readiness trafik almayı, liveness restart kararını yönetir.

**Kaynak:** OFFICIAL-S16-GKE2; [teknik belge](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q31 C

**Doğru seçenek:** Keep a dedicated pull subscription for billing and configure a separate Eventarc Pub/Sub trigger for the audit service.

**Karar:** Bağımsız tüketim için ayrı subscription/trigger teslim yolları gerekir; Eventarc Pub/Sub kaynağı destekler.

**Eleme koşulu:** Aynı subscription tüketicileri işi paylaşır; her biri bütün mesajları almaz.

**Sade anlam:** Bağımsız tüketim için ayrı subscription/trigger teslim yolları gerekir; Eventarc Pub/Sub kaynağı destekler.

**Kaynak:** OFFICIAL-S16-EA2; [teknik belge](https://docs.cloud.google.com/eventarc/standard/docs/overview).

**Önceki ilişki:** S15 sonrası konuşulan Eventarc/PubSub ayrımına bilinçli uygulama; yeni kapsam değil.

## Q32 C

**Doğru seçenek:** Advance the rollout to its next phase after checking the current phase results.

**Karar:** Rollout phase advance aynı hedefte canary aşamasını ilerletir; promote sonraki hedefe geçer.

**Eleme koşulu:** Automatic traffic control aşama trafiğini yönetir; her fazın kendi kendine ilerlemesi ayrı automation konusudur.

**Sade anlam:** Rollout phase advance aynı hedefte canary aşamasını ilerletir; promote sonraki hedefe geçer.

**Kaynak:** SCP18-Q10; [teknik belge](https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q33 C

**Doğru seçenek:** Set an appropriate backoffLimit on the Job.

**Karar:** Job backoffLimit başarısızlık retry bütçesidir; restartPolicy Never yalnız aynı Pod container restart davranışını belirler.

**Eleme koşulu:** restartPolicy Never Job controller’ın replacement Pod oluşturmasını tek başına durdurmaz.

**Sade anlam:** Job backoffLimit başarısızlık retry bütçesidir; restartPolicy Never yalnız aynı Pod container restart davranışını belirler.

**Kaynak:** OFFICIAL-S16-GKE3; [teknik belge](https://kubernetes.io/docs/concepts/workloads/controllers/job/).

**Önceki ilişki:** Kaynak ID önceki seçkilerde kullanılmamış; benzer temel konular önceki çalışmalarda bulunabilir.

## Q34 A

**Doğru seçenek:** Use a deterministic task ID derived from subscription ID and renewal month, within the supported task-name deduplication window.

**Karar:** Stable business işlem anahtarı aynı creation retry’sinde aynı task adı üretir.

**Eleme koşulu:** Bu creation dedup; handler redelivery idempotency hâlâ ayrı gereksinimdir.

**Sade anlam:** Stable business işlem anahtarı aynı creation retry’sinde aynı task adı üretir.

**Kaynak:** SCP16-Q47; [teknik belge](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks).

**Önceki ilişki:** S15 Q14 ile bilinçli ayrım: orada handler redelivery, burada CreateTask belirsizliği.

## Q35 C

**Doğru seçenek:** Run the Firestore emulator, load the intended rules, and connect the client or rules-testing library to it with isolated test data.

**Karar:** Firestore emulator + rules-aware client/test library izin/red testlerini yerelde çalıştırır.

**Eleme koşulu:** Server Admin SDK Security Rules’ı bypass eder; kaynak Node backend varsayımı bu yüzden düzeltildi.

**Sade anlam:** Firestore emulator + rules-aware client/test library izin/red testlerini yerelde çalıştırır.

**Kaynak:** SCP16-Q44; [teknik belge](https://firebase.google.com/docs/rules/unit-tests).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q36 A

**Doğru seçenek:** A PodDisruptionBudget selecting the service Pods with minAvailable set to 2.

**Karar:** PDB voluntary eviction için availability bütçesi belirler.

**Eleme koşulu:** PDB her arızayı engellemez; rollout availability rollingUpdate ile ayrı yönetilir.

**Sade anlam:** PDB voluntary eviction için availability bütçesi belirler.

**Kaynak:** OFFICIAL-S16-GKE4; [teknik belge](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q37 B

**Doğru seçenek:** Use Skaffold debugging support to prepare supported language debug settings and handle debug-port forwarding and debugger attachment.

**Karar:** Cloud Code skaffold debug üzerinden desteklenen runtime debug ayarları, port forwarding ve debugger bağlantısını yönetir.

**Eleme koşulu:** Kaynakta gereğinden geniş tüm container/source mapping iddiası vardı; desteklenen runtime ve dokümante workflow ile sınırlandırıldı.

**Sade anlam:** Cloud Code skaffold debug üzerinden desteklenen runtime debug ayarları, port forwarding ve debugger bağlantısını yönetir.

**Kaynak:** SCP16-Q48; [teknik belge](https://docs.cloud.google.com/code/docs/vscode/debug).

**Önceki ilişki:** Önceki seçki kayıtlarında kaynak ID kullanılmamış; S13/S15 gövde ve kararlarıyla karşılaştırıldı. Benzer temel kavramlar yeni kapsam sayılmaz.

## Q38 B

**Doğru seçenek:** Declare the built image under the top-level images field and request verified provenance using options.requestedVerifyOption: VERIFIED.

**Karar:** images alanı Cloud Build’in image artifact yönetimini sağlar; VERIFIED provenance gereksinimini doğrular.

**Eleme koşulu:** Binary Authorization kanıtı denetler; build provenance üretiminin yerine geçmez.

**Sade anlam:** images alanı Cloud Build’in image artifact yönetimini sağlar; VERIFIED provenance gereksinimini doğrular.

**Kaynak:** SCP13-Q07; [teknik belge](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q39 B

**Doğru seçenek:** The persistent home disk retains the project across stop/start; the development container image need not contain the changed project files.

**Karar:** Persistent home kullanıcı verisini image’dan ayrı tutar; aynı diskle stop/start korunur.

**Eleme koşulu:** VM yaşam döngüsü ile persistent disk/image yaşam döngüsü aynı değildir.

**Sade anlam:** Persistent home kullanıcı verisini image’dan ayrı tutar; aynı diskle stop/start korunur.

**Kaynak:** OFFICIAL-S16-WS3; [teknik belge](https://docs.cloud.google.com/workstations/docs/architecture).

**Önceki ilişki:** S15 Q26 home mount konusunun bilinçli pekiştirmesi.

## Q40 B

**Doğru seçenek:** Align the Service selector with the intended Pod labels and verify that the corresponding endpoints appear.

**Karar:** Service selector hedef Pod kümesini belirler; yanlış label endpoint oluşturmaz.

**Eleme koşulu:** Ingress veya replica sayısı düzeltmek yanlış selector eşleşmesini çözmez.

**Sade anlam:** Service selector hedef Pod kümesini belirler; yanlış label endpoint oluşturmaz.

**Kaynak:** OFFICIAL-S16-GKE5; [teknik belge](https://kubernetes.io/docs/concepts/services-networking/service/).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q41 D

**Doğru seçenek:** Log the context and re-raise the caught error, or raise an explicit failure, rather than return a normal completion result.

**Karar:** Caught error normal return ile yutulursa execution başarılı bitebilir; raise failure durumunu korur.

**Eleme koşulu:** Log severity workflow execution sonucunu kendiliğinden değiştirmez.

**Sade anlam:** Caught error normal return ile yutulursa execution başarılı bitebilir; raise failure durumunu korur.

**Kaynak:** OFFICIAL-S16-WF4; [teknik belge](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q42 D

**Doğru seçenek:** Grant the bucket read role to the Workload Identity Federation namespace principalSet for reporting in the project workload identity pool.

**Karar:** Namespace principalSet aynı project workload identity pool içindeki o namespace workload kümesine tek IAM binding ile izin verir.

**Eleme koşulu:** Namespace principalSet cluster ayrımı yapmaz; bu kapsam soruda açıkça onaylandı. Kubernetes RBAC Cloud Storage IAM izninin yerine geçmez.

**Sade anlam:** Namespace principalSet aynı project workload identity pool içindeki o namespace workload kümesine tek IAM binding ile izin verir.

**Kaynak:** SCP17-Q13; [teknik belge](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity).

**Önceki ilişki:** Önceki seçki kayıtlarında kaynak ID kullanılmamış; S13/S15 gövde ve kararlarıyla karşılaştırıldı. Benzer temel kavramlar yeni kapsam sayılmaz.

## Q43 C+E

**Doğru seçenek:** Commit an appropriately pinned dependency manifest or supported lockfile used by the selected package manager. / Review dependency updates in version control and rebuild the image through the normal pipeline.

**Karar:** Versiyonlanmış pinned dependency input ve kontrollü rebuild bağımlılık değişimini görünür yapar.

**Eleme koşulu:** Scale veya live container değişikliği build input reproducibility sağlamaz.

**Sade anlam:** Versiyonlanmış pinned dependency input ve kontrollü rebuild bağımlılık değişimini görünür yapar.

**Kaynak:** OFFICIAL-S16-BP3; [teknik belge](https://docs.cloud.google.com/docs/buildpacks/python).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q44 B

**Doğru seçenek:** Set maxUnavailable to 0 and maxSurge to 1.

**Karar:** 0 unavailable mevcut availability’yi korur; 1 surge önce yeni Pod için yer sağlar.

**Eleme koşulu:** PDB Deployment rolling update stratejisinin yerine geçmez.

**Sade anlam:** 0 unavailable mevcut availability’yi korur; 1 surge önce yeni Pod için yer sağlar.

**Kaynak:** OFFICIAL-S16-GKE6; [teknik belge](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q45 A

**Doğru seçenek:** Use Gemini Cloud Assist chat to ask contextual follow-up questions about the findings and verify the proposed explanation against the evidence.

**Karar:** Chat bulguları takip sorularıyla incelemeyi sağlar; öneri insan tarafından kanıtla değerlendirilir.

**Eleme koşulu:** AI hypothesis kesin kök neden veya otomatik değişiklik yetkisi değildir.

**Sade anlam:** Chat bulguları takip sorularıyla incelemeyi sağlar; öneri insan tarafından kanıtla değerlendirilir.

**Kaynak:** SCP14-Q41; [teknik belge](https://docs.cloud.google.com/cloud-assist/chat-panel).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q46 A

**Doğru seçenek:** Use a user-defined substitution such as _REPOSITORY in the build configuration and set its value per trigger.

**Karar:** User-defined substitutions aynı build recipe’ye ortam değeri geçirir.

**Eleme koşulu:** Nonsecret config için secret mekanizması veya duplicate recipe gereksizdir.

**Sade anlam:** User-defined substitutions aynı build recipe’ye ortam değeri geçirir.

**Kaynak:** SCP15-Q41; [teknik belge](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q47 D

**Doğru seçenek:** Create the trigger in the location matching the regional source bucket, europe-west1.

**Karar:** Direct Storage event trigger konumu bucket konumuyla eşleşmeli.

**Eleme koşulu:** Hedef region ile kaynak trigger location aynı kavram değildir; IAM region kuralını kaldırmaz.

**Sade anlam:** Direct Storage event trigger konumu bucket konumuyla eşleşmeli.

**Kaynak:** OFFICIAL-S16-EA3; [teknik belge](https://docs.cloud.google.com/eventarc/standard/docs/workflows/route-trigger-cloud-storage).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q48 D

**Doğru seçenek:** Pod topology spread constraints using topology.kubernetes.io/zone and an appropriate skew and scheduling policy.

**Karar:** Topology spread zone label üzerinden replica yerleşimini yönlendirir.

**Eleme koşulu:** Regional cluster tek başına her workload için istenen dağılımı garanti etmez.

**Sade anlam:** Topology spread zone label üzerinden replica yerleşimini yönlendirir.

**Kaynak:** OFFICIAL-S16-GKE7; [teknik belge](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q49 D

**Doğru seçenek:** Return a 2xx response for the completed task; use an appropriate non-2xx response such as 429 when the task has not been successfully completed and should be retried.

**Karar:** 2xx task başarısıdır; non-2xx veya deadline retry’ye gider.

**Eleme koşulu:** 429 special backoff sağlar ama success acknowledgment değildir.

**Sade anlam:** 2xx task başarısıdır; non-2xx veya deadline retry’ye gider.

**Kaynak:** SCP18-Q16; [teknik belge](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues.tasks).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.

## Q50 B

**Doğru seçenek:** Key Visualizer to inspect heatmaps for hot row-key ranges over time.

**Karar:** Key Visualizer erişim örüntülerini key range/zaman ısı haritasında gösterir.

**Eleme koşulu:** Kaynak ListHotTablets de ilgili diagnostic olabilirdi; görsel tarih ihtiyacı tek doğruyu belirginleştiriyor.

**Sade anlam:** Key Visualizer erişim örüntülerini key range/zaman ısı haritasında gösterir.

**Kaynak:** SCP18-Q14; [teknik belge](https://docs.cloud.google.com/bigtable/docs/keyvis-overview).

**Önceki ilişki:** Konu tanıdık olabilir; bu soru yeni bir karar koşulu içerir. Tam semantik yenilik iddiası yok.
