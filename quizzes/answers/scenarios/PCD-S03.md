# PCD-S03 — Türkçe açıklamalı cevap anahtarı

**Çözümden sonra aç.** Hazırlanma ve resmî web kaynaklarını kontrol tarihi: 23 Eylül 2026. Kullanıcı henüz çözmedi; bu dosya kullanıcı cevabı veya sonuç kaydı değildir.

Bu setteki bütün kaynaklar **ek resmî kaynak** olarak verilmiştir; PDF sayfası doğrulanmış gibi gösterilmez. Özellikle GKE ConfigMap, Workload Identity Federation, NetworkPolicy ve PodDisruptionBudget ayrıntıları ders kapsamını genişletir. Senaryolardaki uygulama tasarımları, belgelenmiş davranışlardan yapılan gerekçeli çıkarımlardır; resmî sınav sorusu değildir.

[Resmî sınav rehberi](https://cloud.google.com/learn/certification/guides/cloud-developer) ile aşağıdaki alan eşleştirmeleri hazırlayanın sınıflandırmasıdır; konu ağırlıkları taklit edilmemiştir.

| Soru | Cevap | Alan | Rehber eşleştirmesi |
|---|---|---|---|
| 1 | B | GKE | 3.2 GKE deployment |
| 2 | D | Cloud Run | 3.1 Cloud Run deployment; güvenli çağrı |
| 3 | A | Functions | 3.1 event receivers; 4.1 storage integration |
| 4 | C, D | GKE | 3.2 GKE; 4.2 service accounts/API access |
| 5 | B | Functions | 4.1 storage integration |
| 6 | C | Cloud Run | 3.1 Cloud Run deployment |
| 7 | A | GKE | 3.2 GKE; 1 güvenilir tasarım |
| 8 | D | Cloud Run | 1.1 performans; 4.3 troubleshooting |
| 9 | C | Functions | 4.1 Firestore; 1 güvenilir tasarım |
| 10 | A, B | GKE | 3.2 GKE; 1 güvenli tasarım |
| 11 | B | Cloud Run | 4.3 troubleshooting; 1 güvenilir tasarım |
| 12 | D | Functions | 2.2 build; 3.1 source deployment |
| 13 | A | GKE | 3.2 GKE deployment |
| 14 | C | Functions | 2.3 testing; 3.1 event receivers |
| 15 | B | Cloud Run | 3.1 deployment; 4.2 API integration |

## 1 — B

**Gerekçe:** ConfigMap’in normal volume yansıtması zamanla güncellenir; `subPath` ile bağlanan dosya bu güncellemeleri almaz. Uygulama dosyayı zaten yeniden okuyor. Ayrı dizine normal mount, hem dosya yenilenmesini hem uygulamanın yeni içeriği görmesini sağlar.

**Yakın alternatif D:** Restart yeni içeriği aldırabilir, ancak rutin değişiklikler için restart yasak. A’da beklemek subPath kısıtını kaldırmaz; C’de çalışan process’in environment değeri kendiliğinden güncellenmez.

**Belirleyici ifade:** “routine routing changes must not require a Pod restart” ve “reads ... afresh”. *Afresh* = yeniden.

**Ek resmî kaynak:** [Kubernetes ConfigMaps — mounted updates, environment variables ve subPath notu](https://kubernetes.io/docs/concepts/configuration/configmap/).

## 2 — D

**Gerekçe:** Tag URL hangi revision’a gidileceğini belirler; varsayılan kabul edilen audience ise alıcı servisin normal URL’sidir. Invoker ve ingress zaten doğru. Böylece production trafik yüzdeleri değişmeden candidate sınanır.

**Yakın alternatif B:** İstek tag URL’ye gider, fakat custom audience yokken tag URL’yi token audience’ı yapmak doğru değildir. C kimlik doğrulamayı sağlayabilir ama candidate revision’ı hedefleme şartını sağlamaz; A iki URL’nin rollerini ters çevirir.

**Belirleyici ifade:** “directly to the candidate revision” ve “No custom audiences”.

**Ek resmî kaynak:** [Cloud Run service-to-service authentication — Acquire and configure the ID token](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

## 3 — A

**Gerekçe:** Handler’ın tamamlanma sinyali upload’ın gerçek sonucuna bağlı olmalı. Promise beklenir veya döndürülür; başarısızlık başarıya çevrilmez. Retry zaten açık ve işlem tekrar güvenli olduğundan geçici hata yeniden denenebilir.

**Yakın alternatif C:** Upload’ı bekler ama rejection’ı yutar; log kaydı invocation’ı başarısız yapmaz. B’de handler erken bitmeye devam eder; D instance’ın sıcak kalmasını işin tamamlanma garantisiyle karıştırır.

**Belirleyici ifade:** “invocation result to reflect the actual upload outcome”. *Propagate* = hatanın üst katmana iletilmesine izin vermek.

**Ek resmî kaynak:** [Functions best practices — Do not start background activities](https://docs.cloud.google.com/run/docs/tips/functions-best-practices).

## 4 — C, D

**Gerekçe:** Önce reporting workload’unun ayrı Kubernetes kimliği olmalı; ardından bu federated principal’a yalnız hedef bucket üzerinde okuma izni verilir. Küme/node pool tarafındaki WIF hazırlığı ve API desteği soruda sağlanmış.

**Yakın alternatif B:** Ortak KSA’yı yetkilendirmek diğer workload’u da yetkilendirir; ayrıca proje kapsamı gereğinden geniştir. A node kimliğiyle workload sınırını kurmaz. C tek başına izin vermez, D tek başına Pod’un kullanılan kimliğini değiştirmez.

**Belirleyici ifade:** “only the reporting workload” ve “currently use the same Kubernetes ServiceAccount”.

**Ek resmî kaynak:** [Authenticate to Google Cloud APIs from GKE workloads — direct principal grants ve bucket örneği](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

## 5 — B

**Gerekçe:** Bucket içindeki object name ve generation birlikte belirli içerik sürümünü tanımlar. Gecikmiş olay işlenirken yalnız adla indirmek güncel sürümü seçebilir. Olayın generation’ını download isteğine taşımak gerekir; eski sürümlerin tutulduğu açıkça verilmiştir.

**Yakın alternatif C:** Güncel metadata’dan alınan generation yeni dosyaya ait olabilir; olayın sürümünü korumaz. A çıktı çakışmasını, D invocation eşzamanlılığını değiştirir; ikisi de yanlış input bytes sorununu çözmez. Generation, metageneration ile aynı değildir.

**Belirleyici ifade:** “each uploaded version” ve “retains all relevant noncurrent generations”.

**Ek resmî kaynaklar:** [Object identity](https://docs.cloud.google.com/storage/docs/objects), [Objects get — generation parametresi](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get).

## 6 — C

**Gerekçe:** Ingress container, yapılandırılan portta `0.0.0.0` üzerinde dinlemelidir. Aynı Cloud Run instance’ındaki container’lar localhost üzerinden haberleşebilir; application’ın 9000 portunu dış ingress yapmak gerekmez.

**Yakın alternatif A:** Proxy’yi devreden çıkarır ve loopback bind sorununu korur. B outbound ağ ayarını değiştirir. D shared network namespace içinde aynı ingress portunu iki süreç için kullanmaya çalışır ve istenen proxy mimarisini bozar.

**Belirleyici ifade:** “proxy designated as the ingress container” ve “keeping the application behind the proxy”.

**Ek resmî kaynaklar:** [Container runtime contract — listening port](https://docs.cloud.google.com/run/docs/container-contract), [Cloud Run sidecars — local communication](https://docs.cloud.google.com/run/docs/deploying#sidecars).

## 7 — A

**Gerekçe:** Üç sağlıklı Pod’dan biri gönüllü eviction ile çıkarılabilir; iki sağlıklı Pod kalınca bütçe başka sağlıklı Pod’un eviction’ını durdurur. Yeni Pod sağlıklı olduğunda süreç devam edebilir. PDB zorla silme veya beklenmedik node kaybına karşı mutlak kapasite garantisi değildir.

**Yakın alternatif C:** Deployment rollout ayarı node drain’in eviction bütçesini tanımlamaz. B üç Pod’un üçünü de gerekli kılar ve ilk eviction’ı engeller. D replica hedefini belirtir, bakım sırasında eviction sınırını uygulamaz.

**Belirleyici ifade:** “using the Kubernetes eviction API” ve “without permanently blocking the first eviction”.

**Ek resmî kaynak:** [Kubernetes — Specifying a Disruption Budget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).

## 8 — D

**Gerekçe:** Tek çekirdek doygunken çok vCPU ortalaması düşük kalabilir. Daha düşük concurrency, instance başına biriken istekleri azaltıp istek temelli ölçeklemeyi teşvik edebilir; etkin değer yük testiyle bulunur. Burada zorunlu cevap “concurrency her zaman 1” değildir.

**Yakın alternatif A:** Instance tavanında zaten yer var; tavanı artırmak ölçekleme sinyalini değiştirmez. C tek thread’i otomatik paralelleştirmez. B de CPU darboğazını çözmez.

**Belirleyici ifade:** “one core saturated, low average CPU utilization” ve “instance limit has headroom”. *Headroom* = kullanılabilir ek kapasite/pay.

**Ek resmî kaynak:** [Cloud Run concurrency — multi-vCPU instances](https://docs.cloud.google.com/run/docs/about-concurrency).

## 9 — C

**Gerekçe:** Transaction içinde mevcut applied version okunur; gelen sürüm büyükse hem snapshot hem version yazılır. Eşit veya eski sürüm yazılmaz. Böylece farklı olayların ters sırası ve aynı olayın tekrarı korunur; yarış halinde transaction yeniden değerlendirilebilir. Tam snapshot ve ara sürümlerin atlanabilmesi bu tasarımın şartlarıdır.

**Yakın alternatif B:** Okuma ve yazma ayrı olursa iki handler aynı eski sürümü okuyup daha sonra yanlış sırayla yazabilir. A duplicate’ı süzer ama ilk kez gelen eski sürümü engellemez. D geliş sırasını kaynak değişim sırasına dönüştürmez.

**Belirleyici ifade:** “complete replacement snapshot”, “older version must never overwrite” ve “even if two handlers race”.

**Ek resmî kaynaklar:** [Firestore triggers — ordering and at-least-once limitations](https://docs.cloud.google.com/run/docs/triggering/trigger-functions-with-firestore-documents), [Firestore transactions](https://docs.cloud.google.com/firestore/native/docs/manage-data/transactions). Version karşılaştırmalı çözüm bu davranışlardan çıkarılan uygulama tasarımıdır.

## 10 — A, B

**Gerekçe:** Bağlantıyı hem kaynağın egress hem hedefin ingress politikası izinli kılmalı. İki yöndeki isolation korunurken selector ve portla dar izin eklenir. NetworkPolicy izinleri birleşir; mevcut default-deny politikasının silinmesi gerekmez.

**Yakın alternatif D:** İstenen yeni bağlantının kaynağı backend değildir. İzin verilen bağlantının cevap trafiği için ters yönlü yeni bağlantı izni eklemek gerekmez. C de frontend’e gelen yeni bağlantıları açar. DNS ayrı çözülmüş olduğu için DNS kuralı eklemek cevap değildir.

**Belirleyici ifade:** “frontend ... default-deny egress” ve “backend ... default-deny ingress”.

**Ek resmî kaynak:** [Kubernetes NetworkPolicies — additive policies and both directions](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

## 11 — B

**Gerekçe:** Cloud Run request timeout bağlantıyı kapatıp 504 döndürebilir; bu, container’ın durdurulduğu veya transaction’ın geri alındığı anlamına gelmez. Aynı işin retry’ını tanımak için kalıcı işlem kimliği ve idempotent işlem protokolü gerekir. Timeout ayarını normal süreyle uyumlu yapmak yararlıdır; tek başına bağlantı kaybı sonrası tekrar güvenliğini garanti etmez.

**Yakın alternatif A:** HTTP isteğinin sonlanmasını process/işlem iptaliyle eş tutar. C concurrency’yi transaction rollback mekanizması sayar; D session affinity’ye sağlamadığı bir işlem garantisi yükler.

**Belirleyici ifade:** “original operation committing after ... the error”.

**Ek resmî kaynak:** [Cloud Run request timeout — code can continue after timeout](https://docs.cloud.google.com/run/docs/configuring/request-timeout). Kalıcı işlem kimliği tasarımı güvenli retry ihtiyacından çıkarımdır.

## 12 — D

**Gerekçe:** Hata revision oluşmadan build aşamasında; reddedilen principal build account. Eksik rol bu kimliğe verilmelidir. Runtime kimliği production-data erişim sınırını korur.

**Yakın alternatif C:** Build’i çalıştırabilse bile build sürecine production runtime yetkilerini taşır; açık ayrım şartına aykırıdır. A yanlış principal’ı yetkilendirir. B service invocation içindir, kaynak build izninin yerine geçmez.

**Belirleyici ifade:** “Audit logs identify the build account” ve “build must not inherit”. Burada rol adı senaryoda verilmiştir; ölçülen karar doğru principal ve aşamadır.

**Ek resmî kaynaklar:** [Build service account — roles/run.builder](https://docs.cloud.google.com/run/docs/configuring/services/build-service-account), [Cloud Run service identity](https://docs.cloud.google.com/run/docs/configuring/services/service-identity).

## 13 — A

**Gerekçe:** Scheduler anlık düşük CPU kullanımını değil uygun node’daki request kapasitesini dikkate alır. Tek Pod’un 2000m request’i tek uygun node’a sığmalıdır. İhtiyacın ölçülmüş olduğu verildiğinden request’i düşürmek çözüm değildir.

**Yakın alternatif D:** Düşük ölçülen kullanım mevcut rezervasyonları kaldırmaz. B request’ten düşük limit önerir ve uygun bir resource yapılandırması değildir. C bir Pod’un request’ini birden fazla Pending Pod arasında bölmez.

**Belirleyici ifade:** “after existing requests are accounted for” ve “genuinely needs its ... reservation”.

**Ek resmî kaynak:** [Kubernetes resource management — scheduling and FailedScheduling](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

## 14 — C

**Gerekçe:** CloudEvent data bölümü Pub/Sub zarfını taşır; business JSON doğrudan data kökünde değildir. `message.data` içindeki base64 içerik decode edildikten sonra UTF-8 ve JSON işlenir. Adapter testi bu katmanları içermeli; yalnız business helper’ı sınamak üretim zarfını sınamaz.

**Yakın alternatif D:** Mevcut delivery’yi değiştirmeden handler türünü değiştirmek raw order JSON üretmez. A zarfı atlamaya devam eder. B message ID’yi iş verisiyle karıştırır.

**Belirleyici ifade:** “test to exercise the same payload transformation as production”.

**Ek resmî kaynak:** [Google Cloud Pub/Sub CloudEvent sample — Python](https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-pubsub). JSON parse adımı soruda verilen publisher formatından gelir. S02’nin çıkarılan taslağında Eventarc parser konusu vardı; bu set için bütünüyle hiç karşılaşılmamış kavram sayılmaz, yeni ölçülen karar adapter testinin üretim zarfını temsil etmesidir.

## 15 — B

**Gerekçe:** Public IPv4 hedefe giden istek private-ranges-only seçimiyle yapılandırılan NAT yoluna girmez. All-traffic, bu isteği de VPC’ye yönlendirir; soruda NAT/subnet/static IP hazırlığı doğru kabul edilmiştir.

**Yakın alternatif A:** Gelen trafik için load balancer IP’si, container’ın dış API’ye giderken kullandığı kaynak IP değildir. C de ingress’i değiştirir. D instance sayısını/sıcaklığını sabit egress IP garantisiyle karıştırır.

**Belirleyici ifade:** “public IPv4 address” ve “private-ranges-only”.

**Ek resmî kaynak:** [Cloud Run static outbound IP — route all traffic through VPC](https://docs.cloud.google.com/run/docs/configuring/static-outbound-ip). S02’nin çıkarılan taslağında Direct VPC konusu vardı; burada yeni karar public destination’ın mevcut NAT yolunu atlamasıdır.

## Değerlendirme notu

Cloud Run: 2/6/8/11/15. Functions: 3/5/9/12/14. GKE: 1/4/7/10/13.

9 yeni karar + 4 karma (4/9/10/12) + 2 gecikmeli uygulama (2/8). Q2 audience/tag; Q8 concurrency’nin doğruluk yerine performans uygulamasıdır. Q8 doğru olsa bile legacy shared-state sorununun kalıcılığını tek başına kanıtlamaz. Probe kontrol tarihi 25 Eylül olarak korunur. Workspace ve diğer kuyruk başlıkları bu sette ölçülmedi.

İlk deneme sonuçları sonradan açıklanmış cevaplarla değiştirilmez. Teknik bilgi, İngilizce anlam, yönerge ve gerekçe eksikliği ayrı değerlendirilir; dil desteği veya rehberli çözüm ayrıca kaydedilir.
