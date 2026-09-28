# PCD-S10 — Türkçe cevap anahtarı

**Çözümden sonra aç.** 20 soru; 45 dakika hedefi. Çift seçimlerde iki doğru seçeneğin de işaretlenmesi gerekir; kısmi puan yok. İlk cevaplar açıklama sonrası değişmez. Süre sonrasındaki cevaplar ayrıca kaydedilir.

Sorular özgündür. Kaynak kontrolü: 28 Eylül 2026. Soru senaryoları kaynaklardan çıkarılan uygulamalardır; gerçek sınav sorusu veya kalibre edilmiş deneme değildir.

## Hızlı anahtar

1: **C** · 2: **D** · 3: **C** · 4: **C** · 5: **D** · 6: **A+C** · 7: **A** · 8: **C** · 9: **A** · 10: **D** · 11: **B** · 12: **C** · 13: **B** · 14: **D** · 15: **A** · 16: **A** · 17: **B** · 18: **B+E** · 19: **B** · 20: **B**

## Açıklamalar

### Q01 — C

**Sade Türkçesi:** Görseller değişmeyen, sürümlü adreslerde; uzak kıtalardaki yeni istemciler aynı dosyaları bölgesel sunucudan alıyor. Sunucu kapasitesi darboğaz değil.

**Belirleyici ifade:** “without changing the application or operating additional regional application stacks”

**Neden doğru?** Cloud CDN uygun yanıtları kullanıcılara yakın edge noktalarında tutar. İlk cache miss origin’e gider; sonraki uygun istekler edge’den karşılanabilir. Her ilk isteğin hızlanacağı garantisi yoktur.

**Diğer seçenekler:**

- **A:** Bölgesel uygulama cache’i origin işini azaltır; kıtalar arası kullanıcı-origin yolunu kısaltmaz ve kod değişikliği ister.
- **B:** İşlemci darboğazı yok. Aynı bölgedeki daha fazla instance coğrafi mesafeyi çözmez.
- **D:** Tarayıcı cache’i aynı tarayıcının tekrarına yarar; farklı yeni tarayıcılar arasındaki ortak cache ihtiyacını karşılamaz.

**Rehber:** 1.1 · **Ölçülen karar:** Global edge caching.

**Kaynak:** [Cloud CDN overview](https://docs.cloud.google.com/cdn/docs/overview).

### Q02 — D

**Sade Türkçesi:** Kısa, ara sıra yapılan standart CLI işleri var. Özel image, private VPC erişimi ve sürekli çalışan ortam gerekmiyor.

**Belirleyici ifade:** “the least provisioning and maintenance effort”

**Neden doğru?** Cloud Shell tarayıcıdan kullanılabilen, araçları hazır yönetilen bir shell sağlar. Kısa yönetim işleri için ayrıca geliştirme ortamı yapılandırma yükü getirmez.

**Diğer seçenekler:**

- **A:** Workstations özel ve yönetilen geliştirme ortamlarında anlamlıdır; burada özel ortam ihtiyacı açıkça yok.
- **B:** VM ile yapılabilir fakat VM ve araç bakımını kullanıcı üstlenir.
- **C:** Cloud Build otomasyon içindir; birkaç etkileşimli komut için pipeline kurmak gereksizdir.

**Rehber:** 2.1 · **Ölçülen karar:** Cloud Shell environment fit.

**Kaynak:** [How Cloud Shell works](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works).

### Q03 — C

**Sade Türkçesi:** Container henüz başlamadı. Event kaydı olmayan image tag’ini gösteriyor; ağ ve indirme izni doğrulanmış.

**Belirleyici ifade:** “cannot be found”

**Neden doğru?** Deployment var olmayan tag’i istiyor. Doğru onaylı artifact referansını vermek kök nedeni giderir; tag yerine uygun immutable digest kullanımı da aynı artifactı sabitleyebilir.

**Diğer seçenekler:**

- **A:** Yetki mevcut; Administrator rolü hatalı tag’i düzeltmez ve gereksiz geniştir.
- **B:** Başlamamış container’ın probe süresini değiştirmek eksik image oluşturmaz.
- **D:** Uygulama bellek kullanma aşamasına gelmedi. Image bulunamaması bellek sorunu değildir.

**Rehber:** 3.2 · **Ölçülen karar:** Image pull diagnosis.

**Kaynak:** [Troubleshoot image pulls](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/image-pulls).

### Q04 — C

**Sade Türkçesi:** Worker kapasitesi yeterli; işlem bitmeden ack süresi doluyor. İş tamamlanmadan ack verilemez.

**Belirleyici ifade:** “while healthy workers are still processing them”

**Neden doğru?** Lease management işlenen mesajın ack süresini uzatır. Uygun toplam uzatma sınırı seçilir, kalıcı sonuçtan sonra ack verilir. Bu önlem tüm duplicate olasılıklarını kaldırmaz; idempotency korunur.

**Diğer seçenekler:**

- **A:** Erken ack sonrası worker ölürse iş kaybolabilir; log teslim güvencesi sağlamaz.
- **B:** Flow control kapasiteyi korur; burada tek işin süresi ack süresini aşıyor.
- **D:** Retention mesajın saklanma penceresidir; aktif işin ack lease süresini uzatmaz.

**Rehber:** 4.1 · **Ölçülen karar:** Pub/Sub acknowledgment lease.

**Kaynak:** [Lease management](https://docs.cloud.google.com/pubsub/docs/lease-management).

### Q05 — D

**Sade Türkçesi:** Kullanıcı girdisi SQL kodunun içine yapıştırılıyor. Kimlik doğrulama ve şifreli bağlantı doğru olsa da sorgunun anlamı değiştirilebiliyor.

**Belirleyici ifade:** “concatenated into the WHERE clause”

**Neden doğru?** Parametre bağlama SQL yapısını girdinin verisinden ayırır. Burada dinamik tablo/kolon adı değil, WHERE içindeki değer parametreleniyor; normal noktalama desteklenir.

**Diğer seçenekler:**

- **A:** Kara liste eksik kalabilir ve geçerli müşteri adlarını bozar; temel çözüm query parameterization’dır.
- **B:** Veritabanına kimin bağlandığını değiştirir, gönderilen SQL’in güvenli kurulmasını sağlamaz.
- **C:** Ağ erişimini sınırlar; yetkili uygulamanın güvensiz SQL göndermesini engellemez.

**Rehber:** 1.2 · **Ölçülen karar:** Parameterized SQL.

**Kaynak:** [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).

### Q06 — A + C

**Sade Türkçesi:** Build kimliği image yükleyecek; ayrı audit kimliği sadece indirecek. Başka yerden gelen izin yok ve repository yönetimi ayrı ekipte.

**Belirleyici ifade:** “Neither account has inherited access to this repository”

**Neden doğru?** Repository seviyesinde Writer yükleme ihtiyacını, Reader indirme ihtiyacını karşılar. Burada sorulan izin yalnız artifact erişimidir; diğer çalışma izinleri zaten verilmiş.

**Diğer seçenekler:**

- **B:** Repository yönetimi yetkisi gerekmez; Writer yeterlidir.
- **D:** Audit indirme yapıyor; yazma ihtiyacı yoktur.
- **E:** Project kapsamı gereksiz geniştir; ayrıca Reader build hesabının upload ihtiyacını karşılamaz.

**Rehber:** 2.2 · **Ölçülen karar:** Repository-scoped artifact access.

**Kaynak:** [Artifact Registry access control](https://docs.cloud.google.com/artifact-registry/docs/access-control).

### Q07 — A

**Sade Türkçesi:** Aynı instance her çağrıda güvenle tekrar kullanılabilen client’ı yeniden kuruyor. Client ortak olabilir ama kullanıcı verisi ve yetki kararı ortak olamaz.

**Belirleyici ifade:** “The supported client is thread-safe”

**Neden doğru?** Instance scope client yeniden kullanımını mümkün kılar; request scope ise kullanıcı durumunu ayırır. Platformun instance’ı sonsuza kadar koruyacağı varsayılmaz; yeni instance yeniden initialize olur.

**Diğer seçenekler:**

- **B:** İlk kullanıcının sonucu başka kullanıcılara sızabilir.
- **C:** Min instances cold start azaltabilir; her request’in içindeki client oluşturma kodunu ortadan kaldırmaz.
- **D:** Global mutable user identity eşzamanlı istekler arasında karışabilir; client reuse ile aynı şey değildir.

**Rehber:** 3.1 · **Ölçülen karar:** Reuse safe clients in functions.

**Kaynak:** [Functions best practices](https://docs.cloud.google.com/run/docs/tips/functions-best-practices).

### Q08 — C

**Sade Türkçesi:** Mevcut PostgreSQL uygulaması ilişkisel özelliklere dayanıyor; bölgesel kapasite yeterli ve en az değişiklik isteniyor.

**Belirleyici ifade:** “minimize changes to the existing database schema and application queries”

**Neden doğru?** Cloud SQL for PostgreSQL mevcut engine’e yakın yönetilen geçiş sağlar. HA/backups ihtiyaca göre yapılandırılır. PostgreSQL olması her extension/sürümün otomatik uyumlu olduğu anlamına gelmez; burada özel uyumsuzluk verilmemiş.

**Diğer seçenekler:**

- **A:** Belge modeline dönüşüm mevcut join ve şemayı yeniden tasarlatır.
- **B:** Dağıtık ölçek için anlamlı olabilir; burada bu ihtiyaç yok ve uyarlama gerektirir.
- **D:** Wide-column model ilişkisel sorguları en az değişiklikle taşıma hedefiyle uyuşmaz.

**Rehber:** 1.3 · **Ölçülen karar:** Managed PostgreSQL workload fit.

**Kaynak:** [Cloud SQL overview](https://docs.cloud.google.com/sql/docs/postgres/introduction).

### Q09 — A

**Sade Türkçesi:** Client’ın bekleme süresi dolmuş; server’daki işlem çalışmaya devam ediyor. İşlemin kimliği kalıcı olarak kayıtlı.

**Belirleyici ifade:** “is still running on the server and has not failed”

**Neden doğru?** Aynı operation name ile durum takibine devam edilir. Client bekleme süresi ile server operation yaşam döngüsü ayrıdır; senaryo zaten server’ın çalıştığını doğruluyor.

**Diğer seçenekler:**

- **B:** Aynı işi yeniden başlatır; kullanıcı bunu açıkça istemiyor.
- **C:** Polling deadline tek başına operation’ın iptal edildiği kanıtı değildir; status bunun tersini söylüyor.
- **D:** Quota hatası yok. Yeni operation oluşturmak mevcut işi takip etmek değildir.

**Rehber:** 4.2 · **Ölçülen karar:** Long-running operation lifecycle.

**Kaynak:** [Long-running operations](https://docs.cloud.google.com/dotnet/docs/reference/help/long-running-operations).

### Q10 — D

**Sade Türkçesi:** Test gerçek saat ve sleep nedeniyle zamanlamaya bağlı. Kural açık: tam expiration anında da token geçersiz.

**Belirleyici ifade:** “equal to or later than its expiration time”

**Neden doğru?** Clock bağımlılığı enjekte edilir; production gerçek clock, test sabit/denetimli clock kullanır. expiresAt öncesi geçerli; eşit ve sonrası geçersiz beklenir. Böylece gerçek karşılaştırma kodu çalışır.

**Diğer seçenekler:**

- **A:** Daha uzun ve tekrar edilen testler deterministik olmaz; hatayı maskeleyebilir.
- **B:** Test edilen metodu mock etmek karşılaştırma implementasyonunu ölçmez.
- **C:** Tam sınırdaki olası >= / > hatasını kaçırır.

**Rehber:** 2.3 · **Ölçülen karar:** Deterministic time-based unit tests.

**Kaynak:** [Java Clock](https://docs.oracle.com/javase/8/docs/api/java/time/Clock.html).

### Q11 — B

**Sade Türkçesi:** Her iki taraf da açık oturum boyunca bağımsız olarak çok sayıda mesaj göndermeli. Protobuf ve HTTP/2 altyapısı hazır.

**Belirleyici ifade:** “Either service must be able to send multiple messages independently”

**Neden doğru?** Bidirectional streaming her iki yönde mesaj akışını destekler; unary tek request/response, server-streaming ise tek client request karşısında server mesaj akışıdır.

**Diğer seçenekler:**

- **A:** Yeni çağrılar kurar; tek açık oturumdaki iki yönlü stream gereksinimini sağlamaz.
- **C:** Client sonradan yeni komutlar gönderemez; başlangıç isteğiyle sınırlıdır.
- **D:** Polling istemiyorlar ve mevcut typed gRPC araçlarını kullanabilirler.

**Rehber:** 1.1 · **Ölçülen karar:** Bidirectional gRPC API.

**Kaynak:** [gRPC core concepts](https://grpc.io/docs/what-is-grpc/core-concepts/).

### Q12 — C

**Sade Türkçesi:** HPA önerisi sekizin üzerinde ama üst sınırı sekiz. Metrik, node ve backend kapasitesi sorunları elenmiş.

**Belirleyici ifade:** “its calculated recommendation is above the configured maximum”

**Neden doğru?** Bağlayıcı sınır maxReplicas. Test edilmiş kapasite içinde bu üst sınırı artırmak HPA’nın daha çok replica oluşturmasına izin verir; sınırsız ölçekleme önerilmez.

**Diğer seçenekler:**

- **A:** Node büyütmek HPA’nın sekiz üst sınırını kaldırmaz; mevcut node kapasitesi zaten var.
- **B:** Hedefi yükseltmek önerilen replica sayısını azaltabilir; yük ihtiyacını çözmeden ölçeklemeyi bastırır.
- **D:** Scale-down davranışı daha fazla replica yaratılmasını engelleyen üst sınırı değiştirmez.

**Rehber:** 3.2 · **Ölçülen karar:** HPA binding maximum.

**Kaynak:** [Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).

### Q13 — B

**Sade Türkçesi:** Browser’ın gönderdiği userId değiştirilebiliyor. Backend önce token’ın geçerliliğini doğrulayıp kimliği güvenilir claim’den çıkarmalı, sonra erişimi kontrol etmeli.

**Belirleyici ifade:** “without validating the token”

**Neden doğru?** Doğru project için yapılandırılmış Admin SDK ile token doğrulanır; UID doğrulanmış token’dan alınır. Authentication tek başına bütün hesap kayıtlarına erişim vermez: ayrıca account-level authorization gerekir.

**Diğer seçenekler:**

- **A:** Decode etmek imza, issuer, audience ve süre doğrulaması değildir. Sahte payload güvenilir olmaz.
- **C:** Saldırgan kendi client’ını çalıştırabilir; güven sınırı backend’de uygulanmalıdır.
- **D:** Son kullanıcı kimliği ve uygulama yetkisi Google Cloud kaynak IAM’iyle aynı değildir; manipüle edilebilir userId de düzelmez.

**Rehber:** 1.2 · **Ölçülen karar:** Verify end-user identity.

**Kaynak:** [Verify ID tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens).

### Q14 — D

**Sade Türkçesi:** IDE içindeki tekrar eden build/deploy/debug döngüsü kısaltılacak. Doğru development cluster context’i ve Skaffold dosyası hazır.

**Belirleyici ifade:** “a shorter edit-test-debug loop inside the IDE”

**Neden doğru?** Cloud Code, Skaffold tabanlı geliştirme döngüsünü IDE’ye bağlar. Kod değişikliğine göre build/deploy ve uygun debug işlemleriyle hızlı geri bildirim sağlar; production release süreci ayrı kalır.

**Diğer seçenekler:**

- **A:** Cloud Assist’in operasyonel incelemesi local build/deploy/debug döngüsünün yerine geçmez.
- **B:** Nonproduction iterasyonu production’a taşıyor; istenen yaşam döngüsü ve hedef ortam yanlış.
- **C:** Kod önerisi almak container build/deploy/debug mekanizmasını tek başına çalıştırmaz.

**Rehber:** 2.1 · **Ölçülen karar:** Cloud Code inner development loop.

**Kaynak:** [Speed up development in Cloud Code](https://docs.cloud.google.com/code/docs/vscode/speed-up-k8s-development).

### Q15 — A

**Sade Türkçesi:** Log üretimi ve severity parse doğru; INFO kayıtlarını sink exclusion dışarıda bırakıyor. İstenen bundan sonra gelen kayıtlar.

**Belirleyici ifade:** “future INFO entries from this service”

**Neden doğru?** Exclusion filtresi ihtiyaç duyulan service INFO kayıtlarını elememelidir. Kapsamı daraltmak gelecekteki kayıtları bucket’a yönlendirir; hiç saklanmamış geçmiş kayıtları geri getirmez.

**Diğer seçenekler:**

- **B:** Retention saklanan kaydın ne kadar tutulduğudur; sink’in hiç yönlendirmediğini geri getirmez.
- **C:** Severity anlamını bozup error sinyalini kirletir; routing policy gereksinime göre düzeltilmelidir.
- **D:** Trace sampling ve log routing farklı mekanizmalardır.

**Rehber:** 4.3 · **Ölçülen karar:** Log sink exclusions.

**Kaynak:** [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

### Q16 — A

**Sade Türkçesi:** Tüm yeni değerler önceden belli; mevcut değeri okuyup hesaplama yok. Birkaç belgenin yazımı ya hep ya hiç olmalı.

**Belirleyici ifade:** “No write depends on reading a current document value”

**Neden doğru?** Batched write birden fazla yazımı atomik commit eder. Okunan güncel veriye bağlı karar olmadığı için transaction’ın read/validation/retry akışına ihtiyaç yok.

**Diğer seçenekler:**

- **B:** Atomiklik sağlayabilir fakat kullanılmayan okumalar ve gereksiz transaction akışı ekler; soru bunu önlemek istiyor.
- **C:** Bağımsız yazımlar kısmi başarı bırakabilir; çoğunluk başarı atomiklik değildir.
- **D:** Sonradan silme atomik rollback değildir; ara durum görünür olabilir ve eski belgeleri doğru şekilde geri yüklemez.

**Rehber:** 1.3 · **Ölçülen karar:** Atomic Firestore write batch.

**Kaynak:** [Transactions and batched writes](https://firebase.google.com/docs/firestore/manage-data/transactions).

### Q17 — B

**Sade Türkçesi:** Payments kendi kodu veya kullandığı ortak pricing kütüphanesi değişince build edilmeli. Alt klasörler de kapsamda; başka servis/docs değişiklikleri tek başına tetiklememeli.

**Belirleyici ifade:** “including changes in nested subdirectories”

**Neden doğru?** İki dependency path’ini recursive glob ile include etmek doğru sınırdır. Eşleşen bir dosya değişikliği tetiklemek için yeterlidir; ikisinin aynı commit’te değişmesi gerekmez.

**Diğer seçenekler:**

- **A:** Yalnız ortak kütüphane değişince gerekli build atlanır.
- **C:** Catalog/docs-only değişiklikleri de tetikler; açık gereksinimi ihlal eder.
- **D:** Tek yıldız alt dizinlerin tamamını recursive kapsamaz; ** gerekir.

**Rehber:** 2.2 · **Ölçülen karar:** Monorepo trigger dependencies.

**Kaynak:** [Create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

### Q18 — B + E

**Sade Türkçesi:** İki ayrı hata var: yalnız loopback dinleniyor ve platformun beklediği 8080 yerine 5000 kullanılıyor. Deployment portunu değiştirmeden uygulama düzeltilmeli.

**Belirleyici ifade:** “no changes to the service’s configured port are planned”

**Neden doğru?** 0.0.0.0 platformdan gelen bağlantıyı kabul eder; PORT=8080 doğru portta dinlemeyi sağlar. İki değişiklik birlikte gerekir. Sadece birini düzeltmek diğer hatayı bırakır.

**Diğer seçenekler:**

- **A:** Route eklemek loopback veya port uyumsuzluğunu çözmez.
- **C:** Dış TLS Cloud Run tarafından sonlandırılır; bu iki erişim hatasının çözümü değildir.
- **D:** Daha çok sıcak instance aynı yanlış adreste/portta dinlemeye devam eder.

**Rehber:** 3.1 · **Ölçülen karar:** Cloud Run ingress container contract.

**Kaynak:** [Container runtime contract](https://docs.cloud.google.com/run/docs/container-contract).

### Q19 — B

**Sade Türkçesi:** Uygulama hata logluyor ama process başarılı exit code 0 ile bitiyor. Platform bu yüzden retry yapmıyor.

**Belirleyici ifade:** “then exits with code 0”

**Neden doğru?** Job başarısı process exit code ile bildirilir: 0 başarı, nonzero hata. Hata durumunu doğru bildirmek mevcut retry politikasını kullanılabilir kılar; idempotency tekrar çalışmayı güvenli tutar.

**Diğer seçenekler:**

- **A:** Platform başarısızlık görmüyorsa retry sayısı artışı etkisizdir.
- **C:** Job’un task sonucu HTTP handler yanıtıyla belirlenmez; process çıkışı önemlidir.
- **D:** Timeout artırmak error logunu failed task sinyaline dönüştürmez.

**Rehber:** 3.1 · **Ölçülen karar:** Cloud Run job failure signal.

**Kaynak:** [Container runtime contract](https://docs.cloud.google.com/run/docs/container-contract); [Job retries](https://docs.cloud.google.com/run/docs/configuring/max-retries).

### Q20 — B

**Sade Türkçesi:** Ölçümde her request eşit ağırlıkta, her bölge değil. Bölgelerin trafik hacimleri farklı.

**Belirleyici ifade:** “giving every valid request equal weight”

**Neden doğru?** Toplam başarılı 900+90=990; toplam geçerli 900+100=1000. SLI 990/1000=%99. Bölgesel sorun ayrıca izlenebilir; burada istenen tanımlanmış global request oranıdır.

**Diğer seçenekler:**

- **A:** En kötü bölgeyi gösterir, tanımlanmış request-weighted global oranı değil.
- **C:** %100 ve %90 ortalaması %95; küçük bölgeye trafik payından fazla ağırlık verir.
- **D:** CPU kapasitesi isteklerin sayısı değildir; tanımlanan payda valid request sayısıdır.

**Rehber:** 4.3 · **Ölçülen karar:** Request-weighted success SLI.

**Kaynak:** [Implementing SLOs](https://sre.google/workbook/implementing-slos/).

## Kapsam ve yorum sınırı

[Resmî PCD rehberi](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) esas alınmıştır. Birincil dağılım: **6 tasarım / 5 geliştirme-test / 5 deployment / 4 entegrasyon**. 11 numaralı alt başlıktan örnek vardır; her ürün ve özellik ölçülmez.

| Rehber | Sorular |
|---|---|
| 1.1 | Q1, Q11 |
| 1.2 | Q5, Q13 |
| 1.3 | Q8, Q16 |
| 2.1 | Q2, Q14 |
| 2.2 | Q6, Q17 |
| 2.3 | Q10 |
| 3.1 | Q7, Q18, Q19 |
| 3.2 | Q3, Q12 |
| 4.1 | Q4 |
| 4.2 | Q9 |
| 4.3 | Q15, Q20 |

Bu 20 soruda örneğin CMEK, Binary Authorization, WIF trust koşulları, API quota/batching ve tracing instrumentation bağımsız ölçülmez. AI kapsamında yalnız Code Assist destekli test/development ayrımı vardır. Yanlış cevap tek başına teknik eksik kanıtı değildir; belirleyici koşulun anlaşılması ve seçim gerekçesi birlikte incelenir.

Önceki soru ilişkileri [soru günlüğünde](../../scenarios/QUESTION-LOG.md) kayıtlıdır. Q18 açık pekiştirmedir; karma sorular yeni temel konu diye sayılmaz. Hazırlanmış olması çözülmüş veya öğrenilmiş olması demek değildir.
