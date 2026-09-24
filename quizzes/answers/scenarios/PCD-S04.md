# PCD-S04 — Türkçe açıklamalı cevap anahtarı

**İlk denemeyi bitirmeden açma.** 24 Eylül 2026. Bunlar hazırlayanın cevaplarıdır; kullanıcı seçimi veya başarı kaydı değildir.

Kaynak standardı: Aşağıdaki bağlantılar **ek resmî web kaynaklarıdır**, 24 Eylül 2026'da kontrol edildi. Ders PDF'lerinde aynı ayrıntıların bulunduğu veya sayfalarının doğrulandığı iddia edilmez. Senaryolar özgün uygulama örnekleridir; özellikle Q10'un test tasarımı ve Q16'nın ödeme mimarisi kaynak davranışlarından yapılan mühendislik çıkarımlarıdır.

## Hızlı anahtar

| Soru | Cevap | Soru | Cevap |
|---|---|---|---|
| 1 | B | 11 | C |
| 2 | D | 12 | A |
| 3 | A | 13 | B, D |
| 4 | C | 14 | D |
| 5 | D | 15 | B |
| 6 | B | 16 | C |
| 7 | C | 17 | A |
| 8 | A | 18 | C, E |
| 9 | B | 19 | B |
| 10 | D | 20 | D |

Her soru 1 puan; Q13 ve Q18'de tam doğru küme gerekir. Teknik konu bilinmiyorsa bunu İngilizce hatası diye sınıflandırma. Kaynak/çeviri desteğini ilk bağımsız sonuçtan ayrı kaydet.

## Kapsam eşleştirmesi

[Resmî rehber](https://services.google.com/fh/files/misc/042426_professional_cloud_developer_exam_guide_english.pdf) ana alanları yaklaşık %32/%23/%24/%21 olarak verir. Bu setin birincil alan ataması aşağıdadır; birden fazla alanla ilişkili sorular çift sayılmadı.

| Alan | Sorular | Adet / oran |
|---|---|---|
| 1. Tasarım, güvenlik ve veri | 1, 5, 9, 13, 17, 20 | 6 / %30 |
| 2. Geliştirme ve test | 2, 6, 10, 14, 18 | 5 / %25 |
| 3. Deployment yapılandırması | 3, 7, 11, 15, 19 | 5 / %25 |
| 4. Entegrasyon ve gözlemlenebilirlik | 4, 8, 12, 16 | 4 / %20 |

Bu bir geniş kapsam örneklemidir. Spanner/AlloyDB şema ayrıntıları, BigQuery yazma, Memorystore/CDN, KMS, API pagination/batching, Workflows/Tasks/Scheduler ve tüm ağ seçenekleri bu 20 soruda bağımsız ölçülmez. Dört ana alanın kapsanması tüm alt maddelerin tamamlandığı anlamına gelmez. Q19 probe pekiştirmesidir; planlanan 25 Eylül kontrolünden erken olduğundan gecikmeli kalıcılık testi sayılmaz.

## 1 — B · Bigtable anahtar tasarımı

**Kural ve uygulama:** Row key hem erişim düzenini hem veri dağılımını etkiler. Dağılımı dengeli cihaz kimliği öne geldiğinde yazılar farklı aralıklara yayılır; ardından sıralanabilir timestamp, tek cihazın zaman aralığını okumayı kolaylaştırır. Bu senaryoda cihazların benzer hızda yazması önemli bir varsayımdır.

**Diğer seçenekler:** A, artan zaman önekindeki yoğunlaşmayı korur. C yazıları dağıtabilir ama istenen cihaz/zaman aralığını doğrudan row-key aralığıyla okumayı bozar; en yakın alternatiftir. D bütün yükü tek satırda toplar.

**Belirleyici ifade:** “one known device” + “uniformly distributed identifiers”.

**Ek resmî kaynak:** [Bigtable schema design](https://docs.cloud.google.com/bigtable/docs/schema-design). **Rehber:** 1.3.

## 2 — D · Build bağımlılık grafiği

**Kural ve uygulama:** `waitFor` belirtilen adımların başarıyla tamamlanmasını bekler. İki kontrol yalnız compile'a bağlıysa birlikte başlayabilir; package her ikisine bağlanır. Burada dosya yolu değil bağımlılık sırası ölçülüyor.

**Diğer seçenekler:** A'daki `['-']` build başlangıcından itibaren çalıştırır; compile beklenmez. B doğru sırayı korur ama kontrolleri paralelleştirmez; en yakın alternatiftir. C paketlemeyi test sonuçlarını beklemeden başlatabilir.

**Belirleyici ifade:** “independently after compilation” + “wait for both checks to pass”.

**Ek resmî kaynak:** [Build step order](https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order). **Rehber:** 2.2, 2.3.

## 3 — A · Test edilmiş image'ı deploy etme

**Kural ve uygulama:** Kaydedilmiş digest belirli image içeriğini seçer. `--image` ile bu tam referansı deploy etmek, sonradan değişebilen tag üzerinden farklı image seçme riskini kaldırır.

**Diğer seçenekler:** B'deki tag deploy anında farklı digest'e işaret edebilir. Cloud Run tag'i deploy sırasında digest'e çözer; mevcut revision sonradan tag değişince kendiliğinden değişmez. C yeni build üretir, aynı artifact garantisi değildir. D yalnız environment variable günceller; image seçmez.

**Belirleyici ifade:** “exactly the image that passed testing, without rebuilding”.

**Ek resmî kaynak:** [Deploy container images](https://docs.cloud.google.com/run/docs/deploying). **Rehber:** 3.1; ilişkili 2.2.

## 4 — C · Pub/Sub fan-out

**Kural ve uygulama:** Her subscription topic'teki mesajları bağımsız alır. Aynı subscription'ın tüketicileri ise o subscription'ın işini paylaşır. İki takımın her mesajı alması için iki subscription; takım içi ölçekleme için aynı takım subscription'ına bağlı birden fazla worker gerekir. Bu topoloji duplicate teslimatı ortadan kaldırmaz.

**Diğer seçenekler:** A ordering key ile bağımsız subscription yaratmaz. B acknowledgment süresini değiştirir; her tüketiciye ayrı kopya garantilemez. D her siparişi yalnız bir takıma yollar.

**Belirleyici ifade:** “each receive every order” + “pause ... without preventing the other”.

**Ek resmî kaynak:** [Pub/Sub overview](https://docs.cloud.google.com/pubsub/docs/pubsub-basics). **Rehber:** 4.1.

## 5 — D · Cloud SQL zonal failover

**Kural ve uygulama:** Regional HA, farklı zonelardaki primary/standby düzeniyle zonal arızaya yöneliktir; eşzamanlı veri koruması ve failover sağlar. Uygulamanın bağlantıları yeniden kurabilmesi gerekir. Bu, sıfır kesinti veya bölgeler arası felaket kurtarma garantisi değildir.

**Diğer seçenekler:** A manuel restore gerektirir. B'deki standart asynchronous read replica aynı koruma değildir ve normalde yazı hedefi olarak kullanılmaz; HA standby ile read replica'yı ayır. C yalnız retry ile kayıp primary'nin yerine veritabanı oluşturamaz.

**Belirleyici ifade:** “automatic recovery from a zonal failure” + “synchronous replication within the region”.

**Ek resmî kaynak:** [Cloud SQL high availability](https://docs.cloud.google.com/sql/docs/postgres/high-availability). **Rehber:** 1.1, 1.3.

## 6 — B · Firestore emulator

**Kural ve uygulama:** Server client library için `FIRESTORE_EMULATOR_HOST` yerel host:port biçiminde ayarlanır. Test süreci bunu gördüğünde emülatöre bağlanır. Yerel başarı; üretimdeki IAM, indeks ve bütün servis davranışlarının eşdeğerliğini kanıtlamaz.

**Diğer seçenekler:** A üretime dokunmama koşulunu bozar. C yerel endpoint değildir ve gereken host:port değerini sağlamaz. D credential mock'uyla hedef endpoint'i değiştirmez.

**Belirleyici ifade:** “without contacting a production database”.

**Ek resmî kaynak:** [Firestore emulator](https://docs.cloud.google.com/firestore/native/docs/emulator). **Rehber:** 2.1, 2.3.

## 7 — C · Rolling update kapasitesi

**Kural ve uygulama:** `maxUnavailable: 0` rollout nedeniyle kullanılabilir replica sayısını dört altına indirmemeyi; `maxSurge: 1` yeni Pod için bir ek yer kullanmayı ifade eder. Yeni Pod kullanılabilir olduğunda eski Pod azaltılabilir. Gerçek arızalara karşı dört replica garantisi değildir; terminating Pod'lar kaynak sayımını geçici etkileyebilir, soru hızlı termination varsayıyor.

**Diğer seçenekler:** A ve B bir unavailable replica'ya izin verir. D'de iki değer de sıfırdır; geçerli bir rolling-update kombinasyonu değildir. PDB voluntary eviction içindir; bu soru Deployment rollout stratejisini soruyor.

**Belirleyici ifade:** “at least four available replicas” + “one additional Pod”.

**Ek resmî kaynak:** [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/). **Rehber:** 3.2; ilişkili 1.1.

## 8 — A · Koşullu Storage upload

**Kural ve uygulama:** `ifGenerationMatch=0`, aynı isimde live object yoksa yazma koşuludur. Kontrol ve yazı servis tarafında birlikte uygulanır; check-then-upload yarışını önler. Timeout sonrası aynı koşulla retry var olan raporu ezmez. Precondition hatası ilk denemenin başarı kanıtı değildir: mevcut nesnenin bu işleme ait olduğu doğrulanmalıdır.

**Diğer seçenekler:** B gerekli yokluk koşulu değildir. C kontrol ile upload arasında başka writer'a açık yarış içerir. D versiyon tutsa da mevcut live object'i değiştirmeyi engellemez.

**Belirleyici ifade:** “only if no live object ... exists” + “result uncertain”.

**Ek resmî kaynak:** [Storage request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions). **Rehber:** 4.1, 4.2.

## 9 — B · Apigee Quota

**Kural ve uygulama:** Quota belirli dönem için kullanım hakkını sayar. Doğrulanmış partner kimliğiyle ayrı sayaç tutulur; istemcinin serbestçe değiştirebildiği doğrulanmamış bir değer güven sınırı olmamalıdır. Üretimde sayaç dağılımı/senkronizasyonu da gereken kesinliğe göre yapılandırılır.

**Diğer seçenekler:** A burst kontrolü ile dönemsel partner kotasını karıştırır; en yakın alternatiftir. C cache doğruluk/performance konusudur. D backend kapasitesini sınırlar, partner bazında hak saymaz.

**Belirleyici ifade:** “per-partner allowance” + “separate policy ... request spikes”.

**Ek resmî kaynak:** [Apigee Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy). **Rehber:** 1.1.

## 10 — D · AI destekli test tasarımı

**Kural ve uygulama:** Code Assist test üretmeye yardımcı olabilir; testin doğru davranışı ölçtüğü ayrıca değerlendirilir. Zaman ve dış API kontrol edilirse test tekrarlanabilir. Beklenen sonuç implementation'dan kopyalanmak yerine business contract'tan türetilir; rounding sınırları ve timeout davranışı kontrol edilir.

**Diğer seçenekler:** A retry ile dalgalanmayı örter ama oracle sorununu çözmez. B test edilen sonucun kendisini mock'lar. C satır kapsamını davranış doğruluğu sanır.

**Belirleyici ifade:** “assert values copied from the implementation” + “documented business contract”.

**Ek resmî kaynak:** [Code with Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/write-code-gemini). Kaynak test üretimi/context kullanımını destekler; senaryodaki test stratejisi mühendislik değerlendirmesidir. **Rehber:** 2.3; ilişkili 2.1.

## 11 — C · Storage finalize trigger

**Kural ve uygulama:** Finalized yeni object generation'ın başarıyla oluşmasını seçer. Bucket filtresi de doğru kaynağı göstermelidir. Metadata güncellenmesi farklı olay türüdür. Handler'ın CloudEvent biçimi ve IAM/region koşulları soruda zaten sağlanmış.

**Diğer seçenekler:** A metadata değişimini seçer. B doğru türü yanlış bucket'a uygular. D silinmeyi seçer.

**Belirleyici ifade:** “new object generation ... successfully created” + “must not run merely ... metadata changes”.

**Ek resmî kaynak:** [Route Cloud Storage events](https://docs.cloud.google.com/eventarc/standard/docs/run/route-trigger-cloud-storage). **Rehber:** 3.1.

## 12 — A · Dağıtık trace bağlamı

**Kural ve uygulama:** Çağıran aktif trace context'i taşır, alıcı bunu çıkarıp ilgili parent ilişkisiyle devam eder. Böylece servisler aynı request'in izinde birleşir. Instrumentation bunu otomatik yapabilir; soru propagation'ın eksik olduğu durumu anlatıyor.

**Diğer seçenekler:** B yeni trace'lerle kopukluğu korur. C timestamp korelasyonu parent-child neden ilişkisi değildir. D bütün kullanıcı isteklerini tek trace altında yanlış birleştirir.

**Belirleyici ifade:** “three unrelated traces” + “causal relationship”.

**Ek resmî kaynak:** [Trace context](https://docs.cloud.google.com/trace/docs/trace-context). **Rehber:** 4.3.

## 13 — B ve D · Haricî CI kimliği

**Kural ve uygulama:** Federation, dış OIDC kimliğini Google Cloud erişiminde kullanır. B hangi dış workload'ların kabul edileceğini sınırlar; D kabul edilen workload'a hedef repository'de gerekli yetkiyi verir. Trust yapılandırması ile kaynak yetkisi ayrı parçalardır. Soruda doğrudan erişim desteklenir; service-account impersonation zorunlu değildir.

**Diğer seçenekler:** A unrelated repository'leri de yetkilendirir. C keyless koşulunu bozar. E insan kullanıcısını yetkilendirir, çalışan CI workload'unu değil.

**Belirleyici ifade:** “one approved repository” + “without storing ... key”.

**Ek resmî kaynak:** [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation). **Rehber:** 1.2.

## 14 — D · Doğrulanmış artifact için admission gate

**Kural ve uygulama:** Güvenilen doğrulayıcı testler geçince belirli digest için attestation üretir. Binary Authorization deployment sırasında policy gereğini kontrol eder. Sadece build provenance veya scan kaydı, bütün istenen testlerin geçtiğini otomatik kanıtlamaz; onayın hangi koşulda üretildiği önemlidir.

**Diğer seçenekler:** A mutable tag'i güven kanıtı sanır. B vulnerability scan ile integration test'i eşitler. C manuel kontrol bırakır; admission-time enforcement değildir.

**Belirleyici ifade:** “admission-time control” + “approved that exact digest”.

**Ek resmî kaynak:** [Binary Authorization overview](https://docs.cloud.google.com/binary-authorization/docs/overview). **Rehber:** 2.2; ilişkili 1.2, 2.3.

## 15 — B · İstek dışında CPU

**Kural ve uygulama:** Instance-based billing, instance yaşamı boyunca request dışında da CPU sağlar. Minimum instance sayısı ile CPU allocation ayrı ayarlardır. Instance yine sonlandırılabilir; bu yüzden cache yeniden kurulabilir olmalı. Soruda kabul edilen disposable cache için uygundur, kalıcı iş teslim garantisi sağlamaz.

**Diğer seçenekler:** A request süresini uzatır; idle CPU sağlamaz. C kapasite tavanıdır. D istek yönlendirmesidir; CPU allocation değiştirmez.

**Belirleyici ifade:** “even when no request is being handled” + “not durable job processing”.

**Ek resmî kaynak:** [Cloud Run billing settings](https://docs.cloud.google.com/run/docs/configuring/billing-settings). **Rehber:** 3.1; ilişkili 1.1.

## 16 — C · Transaction callback ve dış yan etki

**Kural ve uygulama:** Firestore callback conflict nedeniyle yeniden çalışabilir; dış ödeme Firestore rollback kapsamına girmez. Transaction'da order ile durable pending-payment kaydını birlikte yazmak, yapılacak işi kaybetmemeyi sağlar. Worker sabit payment idempotency key kullanır; crash sonrası tekrar çağrı güvenli biçimde uzlaştırılır. Provider desteği soru varsayımıdır; bu tasarım Firestore ile provider arasında dağıtık transaction iddiası değildir.

**Diğer seçenekler:** A callback'i retry edilemez yapmaz. B kaydedilmeyen işi başarı sayar. D callback dışına taşımayı doğru başlatır ama yalnız memory kaydı crash aralığını kapatmaz; en yakın alternatiftir.

**Belirleyici ifade:** “callback may run again” + “recoverable across process crashes”.

**Ek resmî kaynak:** [Firestore transactions](https://docs.cloud.google.com/firestore/native/docs/manage-data/transactions). Durable pending-record/idempotency çözümü bu davranış ve soru varsayımlarından yapılan mimari çıkarımdır. **Rehber:** 4.1.

## 17 — A · Retention lock

**Kural ve uygulama:** Retention policy süre dolmadan object silme/değiştirmeyi engeller; lock ise policy'nin kaldırılmasını ve sürenin azaltılmasını engeller. Kilit geri alınamaz, süre artırılabilir. Soruda bunun onaylanmış olması kararın belirleyici koşuludur.

**Diğer seçenekler:** B eski versiyonları tutabilir ama silinmezlik sağlamaz. C lifecycle silme zamanlamasıdır, erken silmeyi engellemez. D unlocked policy ile yönetici süreyi düşürüp korumayı kaldırabilir.

**Belirleyici ifade:** “cannot later shorten or remove” + “approved ... irreversible”.

**Ek resmî kaynak:** [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock). **Rehber:** 1.2.

## 18 — C ve E · Build secret erişimi

**Kural ve uygulama:** Secret'ı okuyacak kimlik configured build service account'tur. Secret Accessor payload için bu kimliğe, yalnız ilgili secret üzerinde verilir. `availableSecrets` secret sürümünü environment adına bağlar; consuming step'in `secretEnv` alanı kullanımını tanımlar. Script'in log/image'a sızdırmaması ayrıca gerekir; soruda sağlanmış.

**Diğer seçenekler:** A runtime hesabını yetkilendirir; build'i değil. B sıradan substitution secret deposu değildir. D image üretiminden sonra kaynak dosyayı silmek image layer'ındaki secret'ı geri almaz.

**Belirleyici ifade:** “exactly one dependency-download step” + “dedicated build service account”.

**Ek resmî kaynak:** [Cloud Build secrets](https://docs.cloud.google.com/build/docs/securing-builds/use-secrets). **Rehber:** 2.2; ilişkili 1.2.

## 19 — B · Startup ile liveness'ı ayırma

**Kural ve uygulama:** Startup probe başlangıç için ayrı bir süre bütçesi sağlar. Başarıya ulaşana kadar liveness/readiness devreye girmez; sonrasında normal kontroller çalışır. Böylece initialization'a zaman verilirken steady-state deadlock tespiti gereksiz yere yavaşlatılmaz.

**Diğer seçenekler:** A readiness başarısızlığının container restart etmediğini kaçırır. C başlangıcı rahatlatabilir ama çalışma boyunca deadlock toleransını da büyütür; en yakın alternatiftir. D aynı problemi daha fazla replica'da üretir.

**Belirleyici ifade:** “without permanently slowing steady-state deadlock detection”.

**Ek resmî kaynak:** [Kubernetes probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/). **Rehber:** 3.2. Önceki S02-12 ve probe açıklamalarıyla ilişkili erken pekiştirme; yeni kavram veya gecikmeli başarı sayılmaz.

## 20 — D · Compute platformu

**Kural ve uygulama:** Uyumlu custom OS image, host driver ve kernel yönetimi VM gereksinimidir. Compute Engine OS kontrolünü kullanıcıya verir; patching sorumluluğu kabul edilmiş. Vendor uyumluluğu soruda doğrulanmış varsayılır; herhangi bir custom kernel'in otomatik desteklendiği çıkarılmamalıdır.

**Diğer seçenekler:** A ve C Cloud Run container/çalıştırma modelini host OS değiştirme imkânı sanır. B Autopilot init container'ıyla node kernel'ini değiştirmez; container yasağını da ihlal eder.

**Belirleyici ifade:** “custom kernel configuration” + “does not permit ... container”.

**Ek resmî kaynak:** [Custom OS requirements](https://docs.cloud.google.com/compute/docs/images/building-custom-os). **Rehber:** 1.1.

---

[Sorulara dön](../../scenarios/PCD-S04.md). Değerlendirmede ilk seçimleri koru; açıklama sonrası doğru cevapları bağımsız deneme puanına ekleme.
