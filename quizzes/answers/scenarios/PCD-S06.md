# PCD-S06 — Türkçe açıklamalı cevap anahtarı

**İlk denemeden sonra aç.** 25 Eylül 2026. Bu dosya hazırlayanın anahtarıdır; kullanıcı cevabı veya başarı kaydı değildir.

Kaynak standardı: Her soru güncel exam guide maddesine eşlendi ve **ek resmî web belgeleriyle** kontrol edildi. Ders PDF sayfaları doğrulanmış gibi gösterilmedi. Senaryolar özgündür; mimari/test tasarımı çıkarımları ilgili açıklamalarda belirtilir. Yanlış seçenekler koşullar üzerinden elenir; bir çözümün her bağlamda yanlış olduğu iddia edilmez.

## Hızlı anahtar

| Soru | Cevap | Soru | Cevap |
|---|---|---|---|
| 1 | B | 11 | D |
| 2 | D | 12 | A |
| 3 | A | 13 | C |
| 4 | C | 14 | B |
| 5 | D | 15 | D |
| 6 | B, D | 16 | A |
| 7 | B | 17 | C |
| 8 | A | 18 | B, E |
| 9 | C | 19 | B |
| 10 | B | 20 | D |

Her soru 1 puan; Q6 ve Q18 tam doğru küme gerektirir. İlk cevap, güven, süre ve yardım koşulları ayrı kaydedilir. Açıklama sonrası doğru cevap bağımsız başarı sayılmaz.

## Rehber eşleştirmesi

[Resmî sertifika sayfasından](https://cloud.google.com/learn/certification/cloud-developer) bağlı [güncel exam guide](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) esas alındı. Ana alan ağırlıkları yaklaşık %32/%23/%24/%21; bu 20 sorudaki karşılığı %30/%25/%25/%20. Birincil atama aşağıdadır; ikincil ilişkiler çift sayılmaz.

| Ana alan | Sorular | Adet |
|---|---|---|
| 1 — Tasarım/güvenlik/veri | 1, 5, 9, 13, 17, 20 | 6 |
| 2 — Geliştirme ve test | 2, 6, 10, 14, 18 | 5 |
| 3 — Deployment | 3, 7, 11, 15, 19 | 5 |
| 4 — Entegrasyon/gözlemlenebilirlik | 4, 8, 12, 16 | 4 |

Bu setin alt kapsamı: 1.1 orchestration; 1.2 keys/retention; 1.3 signed URLs/replication/schema; 2.1 ADC/AI-MCP; 2.2 provenance/artifact remediation; 2.3 integration tests; 3.1 image identity/API versions/protocol configuration; 3.2 container resources/init; 4.1 messaging/datastore/write integration; 4.3 metrics/logs. **4.2 genel API tüketimi bu sette bağımsız bir soruyla ölçülmedi**; S05’te batching/pagination/retry ile örneklenmişti. AI unit testing, HPA, probe ayrıntıları ve diğer listelenmeyen alt maddeler tamamlanmış sayılmaz. Ürün adı başına kota, gerçek sınavdaki soru sıklığı veya tam kapsam iddiası yok.

Az önce açıklanan S05 Q3/Q15/Q18 aynı kararlarla yeniden sorulmadı. S06’da aynı hizmetler farklı kararlarla yer alabilir; yakınlık QUESTION-LOG içinde belirtilir. Uzunluk ve yakın alternatifler bilinçli artırıldı; belirsiz iki doğru şık bırakmak amaçlanmadı.

## 1 — B

**Ölçülen karar:** Cloud Tasks schedule/rate/concurrency seçimi. **Rehber maddesi:** 1.1.

Zamanlama, queue genelinde rate ve in-flight sınırı birlikte Cloud Tasks seçtirir. A subscriber başına limit uygular ve handler bekletir; küresel sınır değildir. C execution başına concurrency, bütün işler için ortak kota sağlamaz. D instance sayısını request hızıyla eşitler ve per-task zamanlama/koordinasyonu uygulamaya bırakır. Cloud Tasks task sırası veya exactly-once yan etki garantisi varsayılmıyor. Rate kontrolü token-bucket davranışındadır; sözleşme katı kayan-pencere kotasıysa ek tasarım gerekir.

**Belirleyici İngilizce koşul:** earliest execution time; queue-wide dispatch controls; including retries.

**Ek resmî kaynak:** [Tasks/PubSub karşılaştırması](https://docs.cloud.google.com/tasks/docs/comp-pub-sub) · [Queue limits](https://docs.cloud.google.com/tasks/docs/configuring-queues).

## 2 — D

**Ölçülen karar:** ADC credential-source precedence ve IDE environment. **Rehber maddesi:** 2.1.

ADC önce GOOGLE_APPLICATION_CREDENTIALS konumuna bakar; uygulama local ADC dosyasına ulaşmadan eski key seçiliyor. D override ve çalışan süreçteki eski environment sorununu giderir. A gcloud CLI kimliğini değiştirir; ADC override sürer. B yanlış kimliğe yetki vererek gereksinimi bozar; user impersonation önerisi de bu çözüm değildir. C project/quota bağlamıyla principal seçimini karıştırır. Üretimde attached SA kullanımı kod değişikliği gerektirmez.

**Belirleyici İngilizce koşul:** audit entry identifies old account; IDE environment; normal ADC.

**Ek resmî kaynak:** [ADC search order](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

## 3 — A

**Ölçülen karar:** Cloud Run cross-project image pull kimliği. **Rehber maddesi:** 3.1.

Denied principal, Cloud Run service agent. Cross-project repository için bu principal’a repository-level Reader gerekir. B runtime kimliğini image alımından sorumlu platform kimliği sanır. C zaten okuyabilen deployer’a yazma yetkisi ekler; denied principal değişmez. D rolün yönünü/principal’ı yanlış seçer, repository download iznini çözmez.

**Belirleyici İngilizce koşul:** deployment before application starts; denied service-RUNTIME_PROJECT_NUMBER.

**Ek resmî kaynak:** [Artifact Registry ve Cloud Run](https://docs.cloud.google.com/artifact-registry/docs/integrate-cloud-run).

## 4 — C

**Ölçülen karar:** Pub/Sub ordering scope ve regional publishing. **Rehber maddesi:** 4.1.

Ordering key aynı warehouse stream’ini tanımlar; aynı key için aynı publish region ve ordering-enabled subscription gerekir. Publisher sırası soruda ayrıca sağlandı. A warehouse’ları tek key’de birleştirir, ayrıca farklı region kullanımı kalır. B delivery ordering’i açmaz. D batch dışındaki geciken mesajlar için garanti oluşturmaz. Bu, event-time sırası veya exactly-once yan etki garantisi değildir.

**Belirleyici İngilizce koşul:** one active publisher; same warehouse; designated publishing region.

**Ek resmî kaynak:** [Pub/Sub ordering](https://docs.cloud.google.com/pubsub/docs/ordering).

## 5 — D

**Ölçülen karar:** Storage signed GET URL kapsam ve expiry. **Rehber maddesi:** 1.3.

Signed URL belirli method/object ve süreyle bearer erişim verir; browser Google hesabı istemez ve backend byte proxy olmaz. A kimliği olmayan kullanıcıya IAM çözümü önerir ve bucket listing kapsamını büyütür. B service account token’ını diğer yetkileriyle paylaşır. C upload policy’yi GET yetkilendirmesi sanır. Linki bilenin süre boyunca kullanabilmesi soruda kabul edilmiştir; kişi-bağlı tek kullanım garantisi yok.

**Belirleyici İngilizce koşul:** one specific archive; no Google identities; serve bytes directly.

**Ek resmî kaynak:** [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## 6 — B, D

**Ölçülen karar:** AI IDE/MCP tool yüzeyi ve credential sınırı. **Rehber maddesi:** 2.1 / 1.2.

B erişim sınırını credential/runtime düzeyinde uygular; D gereksiz tool yüzeyini kapatıp review’u korur. A/C/E prompt, isim veya repo aidiyetini yetki sınırı sanır. MCP server yerel kod çalıştırabildiğinden yalnız tool adını gizlemek yeterli sandbox değildir; B bu yüzden ayrı şart. Çözüm Gemini MCP uyarıları ve least privilege ilkesinden mühendislik çıkarımıdır; belirli ürün toggle adları ezberletilmiyor.

**Belirleyici İngilizce koşul:** staging read only; broad inherited credentials; every exposed tool.

**Ek resmî kaynak:** [Gemini agent mode ve MCP](https://docs.cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer).

## 7 — B

**Ölçülen karar:** GKE memory request/limit ve OOM teşhisi. **Rehber maddesi:** 3.2.

Her tek iş limitin üzerinde bellek istiyor; request scheduler rezervasyonuna, limit container sınırına etki eder. B ikisini ölçüme göre düzeltir. En yakın C OOM’u azaltabilir ama düşük request ile gerçek ihtiyacın altında rezervasyon/overpacking sorununu bırakır; soru ikisini istiyor. A tek işin bellek ihtiyacını bölmez. D OOM kill’i probe veya graceful timeout sanır.

**Belirleyici İngilizce koşul:** one report even alone; OOMKilled; realistic scheduling.

**Ek resmî kaynak:** [Kubernetes resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

## 8 — A

**Ölçülen karar:** Cloud SQL Auth Proxy ile private network reachability. **Rehber maddesi:** 4.1.

Proxy authentication/TLS sağlar, özel ağa kendiliğinden yol açmaz. A erişilebilir placement veya VPN benzeri bağlantı ile private IP yolunu tamamlar. B public-IP authorized networks mekanizmasını özel route yerine koyar. C IAM’i network reachability sanır. D DB login yöntemi timeout’un ağ nedenini çözmez.

**Belirleyici İngilizce koşul:** private IP only; no VPN or route; reachable VM succeeds.

**Ek resmî kaynak:** [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy).

## 9 — C

**Ölçülen karar:** Bigtable replicated instance app-profile consistency. **Rehber maddesi:** 1.3.

Read-your-writes için bu workload’un write/read çağrıları aynı cluster’a yönlenmeli. Aynı application instance şart değil. Tek cluster unavailable olduğunda otomatik başka cluster’a geçmeme ödünleşimi soruda kabul edilmiş. A sabit sleep garanti değildir. B her bölgeyi ayrı cluster’a bağlar; ardışık istekler farklı olabilir. D okuma sabit olsa da write başka yere gidebilir.

**Belirleyici İngilizce koşul:** confirmation may run elsewhere; accepts temporary unavailability.

**Ek resmî kaynak:** [Bigtable routing](https://docs.cloud.google.com/bigtable/docs/routing).

## 10 — B

**Ölçülen karar:** Cloud Build integration-test isolation ve failure preservation. **Rehber maddesi:** 2.3.

Isolation hem test runner hem tested application’a uygulanmalı. BUILD_ID’den geçerli schema adı türetmek build’leri ayırır; cleanup başarıyla test hatasını yutmamalı. A retry ile flaky hatayı gizler. C yalnız process içini serialize eder, iki build’i ayırmaz. D uygulama ve test verisini böler; exit status’u yanlış kaynaktan üretir. Bu test mimarisi build substitutions/failure davranışından mühendislik çıkarımıdır.

**Belirleyici İngilizce koşul:** overlapping builds; real integration; failures block release.

**Ek resmî kaynak:** [Build substitutions](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values) · [Build schema](https://docs.cloud.google.com/build/docs/build-config-file-schema).

## 11 — D

**Ölçülen karar:** Apigee API contract versioning ve backend routing. **Rehber maddesi:** 3.1.

Contract version’ı path ile açık seçiliyor. D eski/yeni endpoint ve policy’leri aynı anda yaşatır. A breaking change’i rastgele legacy çağrıya verir. B source control’de eski revision tutmayı canlı endpoint erişimi sanır. C client’ın beklediği schema’yı affinity ile belirleyemez. Ayrı proxy zorunlu tek evrensel çözüm değildir; burada seçenekler içinde verilen routing/operasyon şartlarına uygun tasarımdır.

**Belirleyici İngilizce koşul:** old clients cannot update; both contracts; explicit /v2 path.

**Ek resmî kaynak:** [Apigee proxy base paths](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy).

## 12 — A

**Ölçülen karar:** Observability metric cardinality ve structured logs. **Rehber maddesi:** 4.3.

Bounded labels metric cardinality’yi kontrol eder; request ayrıntısı loglarda korunur. En yakın C ekranda gruplar ama altta yazılan time-series sayısını azaltmaz. B bire bir hash üretir, farklı değer sayısı aynı kalır. D araştırma ihtiyacını gereksiz kaybeder. Normalized route kullanımı gerçek /orders/123 path’inden farklıdır.

**Belirleyici İngilizce koşul:** small set of route templates; unique request ID; individual lookups.

**Ek resmî kaynak:** [Log-based metric labels](https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels).

## 13 — C

**Ölçülen karar:** KMS rotation ile eski ciphertext migration ayrımı. **Rehber maddesi:** 1.2.

KMS rotation yeni aktif version oluşturur; mevcut ciphertext’i yeniden şifrelemez. C erişimi koruyup gerçek migration/verification sonrası retirement yapar. A aynı key resource adını version bağımlılığını kaldırıyor sanır. B migration mümkünken süresiz tutmayı zorunlu gösterir. D beklemenin veri dönüşümü yaptığını varsayar. Direct KMS kullanımı özellikle belirtilerek managed-service CMEK davranışları ayrıldı.

**Belirleyici İngilizce koşul:** direct KMS encryption; retained ciphertext has not been rewritten.

**Ek resmî kaynak:** [KMS key rotation](https://docs.cloud.google.com/kms/docs/key-rotation).

## 14 — B

**Ölçülen karar:** Cloud Build provenance output ve verification gate. **Rehber maddesi:** 2.2.

images artifact output Cloud Build’ın provenance üretimini destekler; requestedVerifyOption VERIFIED yoksa başarıyı engelleme şartını da karşılar. A metadata beyanı ve push log’u builder provenance yerine koyar. C vulnerability scan image içeriğini inceler; nasıl build edildiği farklıdır. D digest kaydı artifact provenance üretmez. Mevcut test gate’leri korunur; provenance test başarısı veya güvenli image garantisi değildir.

**Belirleyici İngilizce koşul:** Cloud Build-generated provenance; must not report success without it.

**Ek resmî kaynak:** [Build provenance](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance).

## 15 — D

**Ölçülen karar:** Cloud Run HTTP/2 h2c ve TLS termination. **Rehber maddesi:** 3.1 / 1.1.

Cloud Run frontend TLS’i sonlandırır; container end-to-end HTTP/2 için h2c kabul etmeli. External client HTTPS kullanmaya devam eder; h2c public internet’te şifresiz client bağlantısı gerektirmez. A aynı yanlış TLS beklentisini sürdürür. B hem HTTP/2 gereksinimini hem listener uyumunu bozar. C HTTP/1.1 listener’ı HTTP/2 diye kullanır.

**Belirleyici İngilizce koşul:** HTTP/2 to application; container expects TLS handshake; standard frontend.

**Ek resmî kaynak:** [Cloud Run HTTP/2](https://docs.cloud.google.com/run/docs/configuring/http2).

## 16 — A

**Ölçülen karar:** BigQuery Storage Write API pending streams atomic commit. **Rehber maddesi:** 4.1.

Pending stream’ler commit edilene kadar görünmez; aynı table stream’leri batch commit ile birlikte görünür yapılır. Finalize stream’e yazmayı bitirir, tek başına commit değildir. B default stream partial görünürlüğü engellemez. C committed stream zaten veriyi görünür yapar. D ayrı commit’lere aynı batch ID yazmak transaction sağlamaz. Garanti bu tek table kapsamındadır; farklı table’lara genişletilmez.

**Belirleyici İngilizce koşul:** single table; never partially completed batch; coordinator.

**Ek resmî kaynak:** [Storage Write API batch](https://docs.cloud.google.com/bigquery/docs/write-api-batch).

## 17 — C

**Ölçülen karar:** Storage lifecycle Delete ile retention birleşimi. **Rehber maddesi:** 1.2.

Lifecycle rule match olmak retention engelini aşmaz. Expiry sonrası lifecycle otomatik/asenkron deletion yapabilir; tam saniye garantisi yok. A erken match’i deletion izni sanır. B admin’in retained object’i bypass ederek silebileceğini varsayar. D retention’ın silme planı olduğunu sanır; o minimum koruma süresidir.

**Belirleyici İngilizce koşul:** age 30; retention 90; no holds; automatic when permitted.

**Ek resmî kaynak:** [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle).

## 18 — B, E

**Ölçülen karar:** Artifact Analysis bulgusundan rebuild ve verified rollout. **Rehber maddesi:** 2.2 / 1.2.

B bytes’ı gerçekten değiştirir; E doğrulanan yeni artifact’ın production’a ulaşmasını sağlar. A tag değiştirir, image içeriğini değil. C paket yanlış katmanda; sorun OS package. D upstream fix/advisory güncellemesini mevcut image içeriğinin düzelmesi sanır. Compatibility test ve scan sonuçları farklı kontrol amaçlarıdır. Artifact remediation planı scanning davranışından ve immutable image kullanımından mühendislik çıkarımıdır.

**Belirleyici İngilizce koşul:** OS package inherited from base; fixed new digest; production.

**Ek resmî kaynak:** [Artifact Analysis scanning](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) · [Cloud Run image deployment](https://docs.cloud.google.com/run/docs/deploying).

## 19 — B

**Ölçülen karar:** GKE regular init container ve shared emptyDir. **Rehber maddesi:** 3.2.

Regular init container başarıyla bitmeden app container başlamaz; emptyDir aynı Pod içindeki dosyayı paylaşır. A ordinary container liste sırasını completion bağımlılığı sanır. C readiness trafik uygunluğunu belirler, process başlangıcını bekletmez. D ayrı container writable layer’larını ortak sanır. Soruda replacement’ta yeniden üretim kabul edildiğinden persistent disk şart değil. Restartable sidecar/init farklı davranışları bu finite regular init senaryosuna karıştırılmıyor.

**Belirleyici İngilizce koşul:** must not start with partial file; helper exits; lifetime of each Pod.

**Ek resmî kaynak:** [Kubernetes init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/).

## 20 — D

**Ölçülen karar:** Firestore index exemptions ve write fanout. **Rehber maddesi:** 1.3.

Index exemption veri alanını silmez; kullanılmayan index işini kaldırır. D required query indexes’i korur. A diagnostic içeriği kaybettirir. B gereksiz indexing’i koruyabilir/artırabilir. C gerçek query desteğini kaldırır ve Firestore’un index gereksinimini yok sayar. Soruda ID dağılımı ve document contention ayrılarak karar index fanout’a daraltıldı.

**Belirleyici İngilizce koşul:** never filters or sorts; retain diagnostic content; preserve list queries.

**Ek resmî kaynak:** [Firestore best practices](https://docs.cloud.google.com/firestore/native/docs/best-practices).
