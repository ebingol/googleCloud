# PCD-S09 — Türkçe açıklamalı cevap anahtarı

**İlk denemeden önce açma.** 28 Eylül 2026. [Sorular](../../scenarios/PCD-S09.md).

50 özgün soru; 44 tek ve Q6/18/26/36/42/50 çift seçim. Çoklu seçimde yalnız tam doğru küme 1 puan; toplam 50. İlk yanıtlar açıklama sonrası değiştirilmez. Yardımlı düzeltme ve sonraki tekrar ayrı kaydedilir.

## Kapsam ve sınırlar

[Resmî güncel rehber](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) birincil kapsam dayanağıdır. Dört alan 16/12/12/10; bütün 11 numaralı alt başlık örneklenir. Bu, rehberdeki bütün ürünlerin veya alt özelliklerin tek tek ölçüldüğü anlamına gelmez. Bu turda Apigee policy ayrıntıları, AlloyDB, BigQuery ingestion, API batching, Cloud Service Mesh, Web Security Scanner ve bazı storage/compute seçenekleri doğrudan ayrı soruyla ölçülmez. Önceki setlerde olmaları bu sette ölçülmüş sayılmaz.

Teknik referanslar aşağıda **Ek resmî web kaynakları** olarak etiketlidir; ders PDF’lerinde doğrulanmamış sayfa numarası verilmez. Google, Kubernetes, Docker, npm ve MCP birincil dokümanları kullanıldı. Aday deneyimi yorumları teknik cevap anahtarına dayanak yapılmadı. [Tarihli araştırma](../../scenarios/PCD-RESEARCH-2026-09-28.md).

Soru gövdeleri 84–103 kelime (ortalama 95.6); niş kota veya flag ezberinden çok koşul ayırma hedefi. HPA ContainerResource, quota project ve object hold gibi ek kavramlar bilinmiyorsa teknik önbilgi eksiği olarak ayrı değerlendirilmeli. Q20/Q31 açık pekiştirme; diğer benzerlikler soru bazında kaydedildi. Hazırlanmış olması yeni bir başarı/kalıcılık kaydı değildir.

| Rehber | Sorular | Adet |
|---|---|---|
| 1.1 | 1, 11, 21, 32, 41, 47 | 6 |
| 1.2 | 9, 18, 25, 35, 45 | 5 |
| 1.3 | 5, 15, 28, 38, 48 | 5 |
| 2.1 | 2, 13, 29, 42 | 4 |
| 2.2 | 6, 17, 26, 37 | 4 |
| 2.3 | 10, 22, 33, 50 | 4 |
| 3.1 | 3, 12, 20, 27, 36, 43 | 6 |
| 3.2 | 7, 16, 23, 31, 40, 46 | 6 |
| 4.1 | 4, 19, 34 | 3 |
| 4.2 | 8, 24, 39, 49 | 4 |
| 4.3 | 14, 30, 44 | 3 |

## Hızlı anahtar

| Sorular | Cevaplar |
|---|---|
| 1–10 | 1: D; 2: B; 3: B; 4: D; 5: A; 6: C+D; 7: D; 8: A; 9: A; 10: B |
| 11–20 | 11: C; 12: C; 13: A; 14: B; 15: C; 16: D; 17: A; 18: B+D; 19: C; 20: D |
| 21–30 | 21: B; 22: D; 23: A; 24: A; 25: B; 26: A+E; 27: D; 28: B; 29: C; 30: C |
| 31–40 | 31: A; 32: D; 33: A; 34: B; 35: C; 36: A+B; 37: C; 38: D; 39: B; 40: B |
| 41–50 | 41: D; 42: D+E; 43: D; 44: C; 45: B; 46: A; 47: C; 48: C; 49: A; 50: A+E |

## Q01 — D

**Sade anlam / karar:** Optional dependency: fallback + circuit breaker.

D, arızalı bağımlılığa yük bindirmeyi geçici olarak durdurur ve kontrollü iyileşme kontrolü yapar. A fallback içerdiği için yakın görünür; fakat uzun retry zinciri kapasiteyi tüketmeye devam eder. B bekleme ve yükü artırır. C breaker’ı deployment’a kadar açık tutar; istenen periyodik recovery kontrolünü sağlamaz.

**Belirleyici İngilizce koşul:** exhausting ... available concurrency / periodically detect recovery.

**Rehber:** 1.1. **Önceki ilişki:** Karma; S07-15 optional dependency, burada probe değil çağrı izolasyonu.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps)

## Q02 — B

**Sade anlam / karar:** Local ADC impersonation ile runtime yetkisini yeniden üretme.

B, kısa ömürlü impersonation ile uygulamanın hedef SA yetkisini kullanmasını sağlar. C proje seçer, kimliği değiştirmez. A incelenen izin farkını ortadan kaldırır. D uzaktaki service attachment bilgisini laptop ADC kaynağı yapmaz. Dil/kütüphane desteği soruda açıkça verilmiştir.

**Belirleyici İngilizce koşul:** same service-account identity / permissions must remain unchanged.

**Rehber:** 2.1. **Önceki ilişki:** Karma; S06-02 ADC precedence ve S08-02 temel ADC üzerine farklı kimlikle test.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment)

## Q03 — B

**Sade anlam / karar:** Cloud Tasks worker acknowledgment işin sonuna bağlanmalı.

B, başarı yanıtını kalıcı tamamlanmaya bağlar. D yakın tuzaktır: queue başarıyla onaylanmış task için sırf background thread durdu diye retry başlatmaz. A CPU ve warm kapasite sağlayabilir ama thread/iş kalıcılığını garanti etmez; C logu iş sonucunun yerine koyar. Public frontend’in enqueue sonrası kabul yanıtı ile worker’ın task ack’i farklıdır.

**Belirleyici İngilizce koşul:** Cloud Tasks to track processing failure.

**Rehber:** 3.1. **Önceki ilişki:** Karma; S08-26 durable acceptance, burada ikinci queue yok ve worker ack tamamlanma demek.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/run/docs/triggering/using-tasks)

## Q04 — D

**Sade anlam / karar:** Failover sonrası connection yenileme + transaction bütününü retry.

D, connection arızası ile transaction atomikliğini birlikte ele alır. B yakındır ama rollback önceki ifadeleri de geri almıştır; kalan parçayı çalıştırmak yeterli değildir. A bozuk bağlantıyı korur. C kaydedilmemiş sonucu başarı sayar. Commit sonucu belirsiz olsaydı ayrıca iş kimliğiyle doğrulama gerekirdi; burada rollback doğrulanmıştır.

**Belirleyici İngilizce koşul:** confirmed these transactions were rolled back.

**Rehber:** 4.1. **Önceki ilişki:** Karma; S04-05 HA ve S08-04 pool üzerine failure recovery.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/sql/docs/postgres/manage-connections)

## Q05 — A

**Sade anlam / karar:** Firestore aynı timestamp için tie-breaker cursor.

A, eşit timestamp değerlerini benzersiz ikinci alanla ayırır; cursor tüm sıralama konumunu temsil eder. B sorunu daha seyrek gösterebilir ama sınırdaki eşitliği çözmez. C cursor ile sıralamayı uyumsuz yapar. D son sayfanın kısa olabileceğini de göz ardı eder. Sabit veri varsayımı snapshot tartışmasını ayrı tutar.

**Belirleyici İngilizce koşul:** many imports share exactly the same timestamp.

**Rehber:** 1.3. **Önceki ilişki:** Yeni ölçüm; S08-18 veri modeli ve S05-08 pagination ile ilişkili, eşitlik sınırı yeni.

**Ek resmî web kaynakları:** [Kaynak 1](https://firebase.google.com/docs/firestore/query-data/query-cursors)

## Q06 — C + D

**Sade anlam / karar:** PR build trust boundary + ayrı release identity.

D+C, untrusted kodun çalıştığı kimlikten production yetkisini ayırır. E yakın tuzak: test script’i de build SA yetkileriyle çalışabilir; deploy komutunu kaldırmak yetkiyi kaldırmaz. A teknik sınır değildir. B manuel tetikleme getirse de unreviewed kodu production yetkileriyle çalıştırır. İki workflow’un tetikleme/değiştirme izinleri de korunmalıdır.

**Belirleyici İngilizce koşul:** unreviewed contributor code / separate trusted release trigger.

**Rehber:** 2.2. **Önceki ilişki:** Yeni ölçüm; S03-12 build/runtime kimliği, burada source trust boundary.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/build/docs/cloud-build-service-account)

## Q07 — D

**Sade anlam / karar:** HPA container-specific CPU metric.

D, ölçülen darboğazın container’ını hedefler. A node kapasitesi sorun yokken replica talep sinyalini düzeltmez. C daha yüksek eşik getirerek scale-out’u geciktirebilir. B paydadaki idle request’i büyütür. Bu soru request eksikliği değil geçerli fakat amaca uygun olmayan aggregate metrik sorusudur.

**Belirleyici İngilizce koşul:** without changing the sidecar’s resources / container-resource ... supported.

**Rehber:** 3.2. **Önceki ilişki:** Karma; S05-07 metrik seçimi, yeni sidecar dilution koşulu.

**Ek resmî web kaynakları:** [Kaynak 1](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)

## Q08 — A

**Sade anlam / karar:** Storage conditional delete ile yeni generation koruma.

A, karar verilen generation ile mutasyonu atomik bağlar. B backoff içerir ama yanlış generation silmeyi engellemez. C check-then-delete arasında yarış bırakır. D retry sırasında hedefi değiştirir. 412 durumunda precondition kaldırılmaz; yeni nesne için karar yeniden değerlendirilir.

**Belirleyici İngilizce koşul:** new generation that must be preserved.

**Rehber:** 4.2. **Önceki ilişki:** Karma; S04-08 create-only ve S07-04 metadata yerine delete race.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/storage/docs/request-preconditions) · [Kaynak 2](https://docs.cloud.google.com/storage/docs/retry-strategy)

## Q09 — A

**Sade anlam / karar:** Cross-project secret: denied runtime principal ve resource scope.

A, payload ihtiyacını doğru principal ve secret üzerinde karşılar. B platform kimliğini runtime kimliğiyle karıştırır. C metadata erişimidir; payload değildir. D operatörün zaten olan iznini tekrarlar. Secret’ın başka projede olması runtime SA’nın da o projeye taşınmasını gerektirmez.

**Belirleyici İngilizce koşul:** error identifies that account as missing secret payload access.

**Rehber:** 1.2. **Önceki ilişki:** Karma; S01-01, S06-03 ve R01-01 rol/kimlik ayrımlarını cross-project bağlamında birleştirir.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/run/docs/configuring/services/secrets)

## Q10 — B

**Sade anlam / karar:** Emulator server SDK success Rules kanıtı değildir.

B, gerçek yetki koşulunu kullanıcı bağlamlarıyla sınar. D server SDK ile Rules testi yaptığını varsayarak IAM ve Rules katmanlarını karıştırır; server client library Rules’ı bypass eder. A yalnız veri erişimi tekrarlar. C metin kontrolü davranışı kanıtlamaz. Backend testleri korunur, eksik authorization testi eklenir.

**Belirleyici İngilizce koşul:** uses only an administrative server SDK.

**Rehber:** 2.3. **Önceki ilişki:** Yeni ölçüm; S04-06/S08-16 emulator sınırı, bu kez rule bypass nedeniyle yanlış test kanıtı.

**Ek resmî web kaynakları:** [Kaynak 1](https://firebase.google.com/docs/firestore/security/test-rules-emulator)

## Q11 — C

**Sade anlam / karar:** Spanner write latency: application/leader locality.

C, ölçülen network mesafesini hedefler ve seçili HA modelini korur. D read-only replica’yı write leader yapmaz. A transaction commit yolunu kısaltmaz. B belirtilen dayanıklılık şartını bırakır. Region seçimi uygun read-write bölgeleriyle sınırlıdır; yakınlık fiziksel gecikmeyi tamamen yok etmez.

**Belirleyici İngilizce koşul:** preserving ... multi-region resilience / network time around writes.

**Rehber:** 1.1. **Önceki ilişki:** Karma; S08-25 ürün seçimi üzerine leader locality, S05-09 timestamp read kararı değil.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/spanner/docs/instance-configurations?hl=en)

## Q12 — C

**Sade anlam / karar:** Config-only revision, aynı digest ve no-traffic validation.

C, image ve deployment configuration’ı ayrı yönetir. A config’i düzeltir ve rollout yapabilir; fakat kaynakları yeniden build ederek koruması istenen test edilmiş artifact kimliğini bırakır. D image tag’ini config yerine koyar. B instance’a yapılan geçici müdahaleyi kalıcı revision sanır. Eski revision’ın veri/bağımlılık uyumu soruda sağlanmıştır.

**Belirleyici İngilizce koşul:** executable itself is unchanged / validate ... before moving normal traffic.

**Rehber:** 3.1. **Önceki ilişki:** Karma; rehberli revision bileşenleri + S08-20/43 artifact ve traffic.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables) · [Kaynak 2](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)

## Q13 — A

**Sade anlam / karar:** Cloud Code/kubectl context project seçiminden ayrı.

A, deploy’un gerçek hedefini doğrular. C en yakın tuzak: gcloud project seçimi mevcut kubectl current-context’i otomatik değiştirmez. D yanlış cluster üzerinde yeni namespace oluşturabilir. B yetkiyi artırır ama hedefi düzeltmez.

**Belirleyici İngilizce koşul:** current context still points to production.

**Rehber:** 2.1. **Önceki ilişki:** Yeni ölçüm; S08-11 ortam ürün seçiminden farklı context güvenliği.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/code/docs/vscode/k8s-overview)

## Q14 — B

**Sade anlam / karar:** Canary aggregate ortalamanın gizlediği tail latency.

B, candidate’ı doğru cohort ile karşılaştırır; başarılı ama yavaş istekleri de ölçer. D yakındır ama sorunlu sürümün etkisini gereksiz büyütür. C ortalama kaynak kullanımıyla request deneyimini karıştırır. A latency sorununu yalnız exception’a indirger. Az örnekten kesin hüküm verilmez.

**Belirleyici İngilizce koşul:** stable revision serves most requests / slow successful responses.

**Rehber:** 4.3. **Önceki ilişki:** Karma; S08-44 metrics/trace, yeni canary aggregation teşhisi.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/monitoring/api/v3/aggregation) · [Kaynak 2](https://docs.cloud.google.com/run/docs/monitoring)

## Q15 — C

**Sade anlam / karar:** Bigtable hot customer: bounded salting tradeoff.

C, tek sıcak müşterinin yazmalarını birden fazla key aralığına böler; okuma fan-out maliyetini açıkça kabul eder. D shard’ı artan timestamp’in arkasına koyduğu için sıcak prefix’i çözmez. B yalnız sıcak ucu değiştirir. A dağıtır ama bounded range-read şartını bozar.

**Belirleyici İngilizce koşul:** one customer produces most new events / fixed number ... scans.

**Rehber:** 1.3. **Önceki ilişki:** Karma; S08-36 dengeli cihaz varsayımı tersine çevrildi; S07-17 shard/index ilişkisi var. Yeni temel hash kavramı diye sayılmaz.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/bigtable/docs/schema-design)

## Q16 — D

**Sade anlam / karar:** Service port/targetPort farklılığı.

D, Service’in trafiği gönderdiği backend portunu düzeltir. C yakın tuzak: client-facing port değişir fakat backend hâlâ 8080’dir. A yanlış hedef portunu çoğaltır. B TCP listener sorununu IAM ile çözmeye çalışır. Selector, readiness ve ağ soruda zaten doğrulanmıştır.

**Belirleyici İngilizce koşul:** forwards to targetPort 8080 / listens ... 9090.

**Rehber:** 3.2. **Önceki ilişki:** Karma; S02-03 selector sorusundan farklı doğru selector yanlış port.

**Ek resmî web kaynakları:** [Kaynak 1](https://kubernetes.io/docs/concepts/services-networking/service/)

## Q17 — A

**Sade anlam / karar:** Build origin ve test kanıtı aynı artifacta bağlanmalı.

A, iki farklı kanıtın aynı digest üzerinde birleşmesini sağlar. D yakın tuzak: aynı source commit aynı binary demek değildir. B tag kanıt aktarmaz. C test ile köken kanıtını karıştırır. Provenance geçerli olması business testlerinin geçtiğini göstermez.

**Belirleyici İngilizce koşul:** test report for a different digest / exact artifact.

**Rehber:** 2.2. **Önceki ilişki:** Karma; S08-35 provenance açıklaması sonrası anlık birleşik uygulama; gecikmeli başarı sayılmayacak.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance)

## Q18 — B + D

**Sade anlam / karar:** WIF authenticated issuer yetmez; repo/workflow boundary.

D+B, identity token’daki güvenilir claim’leri gerçek yetki sınırına dönüştürür. E davranış isteğidir, enforcement değildir. C issuer güveni ile bütün repos’a güveni eşit sayar. A statik ve daha geniş credential dağıtır. Claim’in gerçekten issuer tarafından doğrulanması sorunun açık varsayımıdır.

**Belirleyici İngilizce koşul:** any repository / trustworthy workflow-context claims.

**Rehber:** 1.2. **Önceki ilişki:** Karma; S04-13 repository WIF sınırına mevcut aşırı geniş production trust teşhisi.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines)

## Q19 — C

**Sade anlam / karar:** Dead-letter forwarding IAM + inceleme subscription.

C, forwarding identity yetkilerini ve inceleme tüketimini tamamlar. B doğru forwarding identity’sine kısmi izin verir; kaynak subscription üzerindeki gerekli Subscriber erişimini eksik bırakır. D veri formatını değiştirmez. A ack’lenmiş mesajı dead-letter’a otomatik aktarmaz. Attempt sayısı best-effort olduğundan tam N’inci teslimatta kesin taşıma varsayılmaz.

**Belirleyici İngilizce koşul:** service agent lacks ... forwarding permissions.

**Rehber:** 4.1. **Önceki ilişki:** Yeni ölçüm; S07-16 flow control ve S06-04 ordering’den farklı failure isolation.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics)

## Q20 — D

**Sade anlam / karar:** No-traffic candidate tag routing.

D, tag URL ile belirli revision’a gider; normal yüzde dağılımını değiştirmez. B ordinary endpoint üzerinde routing sağlamaz. A kullanıcı etkisini büyütür. C affinity’yi revision seçim mekanizması sanır. Tag erişim izni değildir, mevcut authentication korunur.

**Belirleyici İngilizce koşul:** consistently / without changing ... percentages.

**Rehber:** 3.1. **Önceki ilişki:** Bilinçli pekiştirme; S03-02 ve rehberli R10-04. Yeni kapsam veya yeni teknik karar sayılmaz.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)

## Q21 — B

**Sade anlam / karar:** Uncertain task creation: stable name + delivery idempotency.

B, creation retry’sini aynı logical task’a bağlar. D yakın tuzaktır: create dedup ile execution/delivery tekliği aynı garanti değildir. C yeni task üretir. A response kaybını kesin başarısızlık sayar. Dedup süresi soruda sınırlanmıştır; kalıcı business kayıt yerine geçmez.

**Belirleyici İngilizce koşul:** within ... deduplication window / worker is also idempotent.

**Rehber:** 1.1. **Önceki ilişki:** Karma; S06-01 Tasks dispatch yerine producer creation uncertainty.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/tasks/docs/dual-overview)

## Q22 — D

**Sade anlam / karar:** Consumer compatibility release test.

D, halen desteklenen tüketicinin sözleşmesini bağımsız oracle yapar. B yakın tuzak: beklenen sonucu yeni implementation’dan üretmek kırılmayı gizler. A yalnız yeni davranışı ölçer. C paket güvenliğiyle response contract’ını karıştırır. Çözüm eski client desteği bitmeden breaking change’i sessizce kabul etmez.

**Belirleyici İngilizce koşul:** older mobile client ... cannot be upgraded immediately.

**Rehber:** 2.3. **Önceki ilişki:** Karma; S08-50 API versioning ve S08-39 independent oracle, yeni consumer test gate.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/build/docs/building/build-containers) · [Kaynak 2](https://google.aip.dev/180)

## Q23 — A

**Sade anlam / karar:** PDB mevcut unhealthy replica ile eviction budget.

A, minAvailable’ın healthy kapasiteyi koruduğunu uygular. D toplam Pod sayısını availability sanır ve direct delete ile korumayı bypass eder. B rollout ayarıdır, mevcut PDB koşulunu otomatik değiştirmez. C authorization ile beklenen availability reddini karıştırır. PDB bütün istemsiz arızaları engelleyen garanti değildir.

**Belirleyici İngilizce koşul:** leaving only two healthy replicas / minAvailable of two.

**Rehber:** 3.2. **Önceki ilişki:** Karma; S03-07 PDB, burada arıza sonrası mevcut eviction bütçesi.

**Ek resmî web kaynakları:** [Kaynak 1](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)

## Q24 — A

**Sade anlam / karar:** Pagination token query context ile bağlı.

A, yeni filtreyi yeni query yapar. B token’ı global offset sanır; API sözleşmesi buna izin vermiyor. C opaque token’ı istemci düzenler. D asıl uyumsuzluğu korur. Her Google API için aynı syntax varsayılmıyor; ilgili sözleşme soruda açık.

**Belirleyici İngilizce koşul:** keep the original filter and ordering.

**Rehber:** 4.2. **Önceki ilişki:** Yeni ölçüm; S07-08 missing token field değil token-query uyumu.

**Ek resmî web kaynakları:** [Kaynak 1](https://google.aip.dev/158)

## Q25 — B

**Sade anlam / karar:** Secret rotation rollback dependency lifecycle.

B, eski revision’ın yeniden başlayabilmesi ve dış sağlayıcıda da kimlik doğrulayabilmesi için kontrollü overlap bırakır. C sıcak instance belleğine güvenerek restart durumunu kaçırır. D pinning/rollback davranışını değiştirir. A image tek başına eski secret ve config’i korumaz. Compromise yok, rutin rotation varsayılıyor.

**Belirleyici İngilizce koşul:** old instances might need to restart / rollback window has not closed.

**Rehber:** 1.2. **Önceki ilişki:** Karma; S02-13 ve S08-22 rotation temelinden dependency retirement penceresine.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/run/docs/configuring/services/secrets) · [Kaynak 2](https://docs.cloud.google.com/secret-manager/docs/rotation-recommendations)

## Q26 — A + E

**Sade anlam / karar:** Reproducible inputs + kontrollü security updates.

A+E, base ve dependency girdilerindeki oynaklığı azaltır; patch güncellemelerini süreçle sürdürür. D daha taze olabilir ama kontrollü input hedefini sağlamaz. C dış girdileri kaydetmez. B aynı tag ile farklı artifactları eşitlemez. Pinning güvenlik güncellemelerini kendiliğinden uygulamaz.

**Belirleyici İngilizce koşul:** controlled, reviewable dependency updates.

**Rehber:** 2.2. **Önceki ilişki:** Karma; S05-18 cache ve S08-20 promotion üzerine build input yönetimi.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.docker.com/build/building/best-practices/) · [Kaynak 2](https://docs.npmjs.com/cli/v11/commands/npm-ci)

## Q27 — D

**Sade anlam / karar:** Interactive acceptance + uzun finite Cloud Run job.

D, request lifetime ile export execution’ı ayırır. A service request süre sınırı ve müşteri beklememe şartıyla uyumsuzdur. B kalıcılığı affinity’ye yükler. C hızlı kabulü bozup tekrar iş riskini artırır. Job başlatma/operation kaydı da belirsiz sonuçlara karşı reconcile edilmelidir; iki saatlik işi kabul eden instance çalıştırmaz.

**Belirleyici İngilizce koşul:** two-hour export / only ... identifier immediately.

**Rehber:** 3.1. **Önceki ilişki:** Karma; S02-01 job ve S08-01 service ayrımı; yeni asenkron kontrol/çalıştırma birleşimi.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/run/docs/create-jobs) · [Kaynak 2](https://docs.cloud.google.com/run/docs/execute/jobs)

## Q28 — B

**Sade anlam / karar:** Shared managed NFS vs object/mount/pod-local.

B, belirtilen paylaşılan NFS gereksinimine uyar. D yakın tuzak: mount edilebilir olması semantik eşdeğerlik göstermez. A Pod’a bağlı ephemeral storage’dır. C aynı path adının farklı diskleri ortak filesystem yapacağını varsayar. Kapasite/availability için uygun Filestore tier ayrıca seçilir.

**Belirleyici İngilizce koşul:** different nodes / supported NFS filesystem.

**Rehber:** 1.3. **Önceki ilişki:** Karma uygulama; 27 Eylül Filestore/Storage sözlü açıklaması, ilk senaryo ölçümü.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/filestore/docs/overview)

## Q29 — C

**Sade anlam / karar:** Workstations config rollout aktif session restart.

C, verilen config-uygulama yaşam döngüsünü izler; working files’ı silmez. D control-plane config’ini doğrular ama eski session’da çalışan toolchain’i güncellemez. A kalıcı kullanıcı verisini gereksiz siler. B source branch ile environment image’ını karıştırır.

**Belirleyici İngilizce koşul:** applies ... when it is restarted.

**Rehber:** 2.1. **Önceki ilişki:** Karma; S05-06 persistence yerine yönetilen toolchain update’ın aktif session’a alınması.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/workstations/docs/customize-container-images) · [Kaynak 2](https://docs.cloud.google.com/workstations/docs/architecture)

## Q30 — C

**Sade anlam / karar:** Structured severity ve error grouping context.

C, ingestion doğruyken log semantiğini düzeltir. D daha uzun süre yanlış sınıflandırılmış veri tutar. B trace işlevini log parser yerine koyar. A doğru hata ayrımını bozup alarm gürültüsü üretir. Severity string’in tanınan alanda olması gerekir; custom alan ismi kendiliğinden özel anlam kazanmaz.

**Belirleyici İngilizce koşul:** custom field named levelText / ingests stdout correctly.

**Rehber:** 4.3. **Önceki ilişki:** Karma; S08-44 genel araç seçimi yerine structured field teşhisi.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/logging/docs/structured-logging) · [Kaynak 2](https://docs.cloud.google.com/error-reporting/docs/formatting-error-messages)

## Q31 — A

**Sade anlam / karar:** Open listener ile semantic readiness ayrımı.

A, traffic admission’ı gerçek serving state’e bağlar. B TCP probe zaten başarılı olduğu için failure threshold artışı semantic readiness sağlamaz. C container running durumunu ready sanır. D doğru serving admission kontrolü sağlamaz. Liveness restart gerektiren local failure’ı izlemeye devam eder.

**Belirleyici İngilizce koşul:** TCP ... succeeds as soon as the listener opens.

**Rehber:** 3.2. **Önceki ilişki:** Bilinçli pekiştirme; S02-04 startup ve S02-12/S08-07 probe temeli. Yeni kapsam sayılmaz.

**Ek resmî web kaynakları:** [Kaynak 1](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

## Q32 — D

**Sade anlam / karar:** Farklı freshness contract: metadata cache ve auth.

D, stale kabul edilen veriyle güncel olması gereken yetki kararını ayırır. A gecikmeyi azaltır ama sıfır gecikme koşulunu karşılamaz. B tenant isolation sağlar, freshness sağlamaz. C stale sonucu tutarlı çoğaltır. Örnek: kapak başlığı eski olabilir; erişimi iptal edilmiş kullanıcı için allow eski kalamaz.

**Belirleyici İngilizce koşul:** revoked entitlement must not continue authorizing.

**Rehber:** 1.1. **Önceki ilişki:** Karma; S05-01 cache/tenant üzerine authorization freshness, yeni correctness boundary.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps) · [Kaynak 2](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)

## Q33 — A

**Sade anlam / karar:** Performance test confound: cold vs warm cohorts.

A, aynı koşulları karşılaştırır ve cold start etkisini ayrıca gösterir. B yakın görünür ama kullanıcıya yansıyan idle-start deneyimini dışlar. D tail latency’yi siler. C confound’u korur. Bu bir ölçüm tasarımı sorusudur; B’nin daha iyi olduğu henüz kanıtlanmış değildir.

**Belirleyici İngilizce koşul:** comparable conditions / both ... first burst ... and steady traffic.

**Rehber:** 2.3. **Önceki ilişki:** Yeni ölçüm; S01-12 cold start çözümü değil performans deneyinin doğruluğu.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/run/docs/tips/general)

## Q34 — B

**Sade anlam / karar:** Exactly-once delivery vs publish/business duplication.

B, ayrı publish’leri aynı business ID altında atomik birleştirir. A en yakın tuzak: farklı message ID’ler ayrı mesajlardır; transport exactly-once bunları aynı sipariş saymaz. C crash durumunda veri kaybına yol açar. D publish duplicate’ını çözmez. Ack durable sonucun ardından gelir.

**Belirleyici İngilizce koşul:** different ... message IDs / same stable order-operation ID.

**Rehber:** 4.1. **Önceki ilişki:** Karma; S01-10 dedup üzerine service guarantee kapsamı. Yeni idempotency temeli sayılmaz.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery)

## Q35 — C

**Sade anlam / karar:** Binary Authorization iki bağımsız attestation AND.

C, her iki kontrolü aynı immutable artifact için zorunlu tutar. A iki farklı koşulu OR yaparak gereksinimi gevşetir. B label’ı test kanıtı sayar. D pipeline’da iki rapor toplar ama direct deployment yolunda ikinci onayı zorunlu tutmaz. Provenance da test attestation’ının yerine geçmez.

**Belirleyici İngilizce koşul:** neither approval should substitute for the other.

**Rehber:** 1.2. **Önceki ilişki:** Karma; S08-47 admission temeline iki ayrı approval mantığı.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/binary-authorization/docs/key-concepts) · [Kaynak 2](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference)

## Q36 — A + B

**Sade anlam / karar:** Eventarc source-specific data schema ve adapter test.

A+B, doğru envelope içindeki doğru source data’yı işler ve aynı adapter yolunu sınar. E permission çalışan aşamadır. C Pub/Sub data encoding’ini Storage CloudEvent’e uygular. D format uyumsuzluğunu çözmez. CloudEvents standardı bütün kaynakların data alanının aynı schema’da olduğu anlamına gelmez.

**Belirleyici İngilizce koşul:** Storage ... CloudEvent / written for Pub/Sub.

**Rehber:** 3.1. **Önceki ilişki:** Karma; S03-14 Pub/Sub adapter’ın ters kaynak koşulu; yeni temel CloudEvents kapsamı değil.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/run/docs/write-functions) · [Kaynak 2](https://docs.cloud.google.com/eventarc/docs/cloudevents)

## Q37 — C

**Sade anlam / karar:** Shared workspace concurrent write collision.

C, paralelliği koruyarak artifact isimlerini ayırır. B dependency zaten doğru olduğundan collision’ı çözmez. A diğer kontrolün sonucunu kaçırır. D private dosyalar packaging’e taşınmaz. Shared workspace paylaşımı sağlar; concurrent writer’ları kendiliğinden izole etmez.

**Belirleyici İngilizce koşul:** must remain parallel / needs both reports.

**Rehber:** 2.2. **Önceki ilişki:** Karma; S08-32 workspace+DAG yerine doğru DAG altında write collision.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/build/docs/configuring-builds/pass-data-between-steps)

## Q38 — D

**Sade anlam / karar:** Selective open-ended object hold.

D, seçili nesnelerde silme/replace korumasını explicit release’e kadar tutar. A diğer nesneleri etkiler ve bilinmeyen bitiş tarihini düzgün modellemez. B history ile deletion protection’ı karıştırır. C geçmiş kopya tutabilir ama istenen silme/replace yasağını uygulamaz. Hold kalkınca lifecycle koşulları uygunsa cleanup asenkron ilerleyebilir.

**Belirleyici İngilizce koşul:** selected files / end date is unknown.

**Rehber:** 1.3. **Önceki ilişki:** Yeni ölçüm; S08-31 bucket retention yerine object-level hold. Hukuki tavsiye değil ürün davranışı senaryosu.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/storage/docs/object-holds)

## Q39 — B

**Sade anlam / karar:** Quota project serviceusage.services.use ayrı access katmanı.

B, error’daki consumer project kullanım iznini ve seçimini düzeltir. C gereksiz geniş yetkiyle yanlış project’e müdahale eder. D API key’in IAM’i kaldıracağını varsayar. A hedef resource’ı değiştirir. API enablement, resource permission ve quota-project usage ayrı önkoşullardır.

**Belirleyici İngilizce koşul:** client-based ... API / missing serviceusage.services.use.

**Rehber:** 4.2. **Önceki ilişki:** Yeni ölçüm; S08-24 enablement+IAM üzerine quota consumer ayrımı.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/docs/quotas/set-quota-project)

## Q40 — B

**Sade anlam / karar:** Missing ConfigMap key vs startup health.

B, container başlatılmadan önceki configuration prerequisite’ini düzeltir. D startup probe uygulama başlamadan eksik kalan config anahtarını oluşturmaz. C required sözleşmeyi sessizce bozar. A aynı eksik config’i çoğaltır. Events ile failure aşamasını ayırmak ana karardır; Ready olmaması tek başına probe hatası demek değildir.

**Belirleyici İngilizce koşul:** Events report ... required ConfigMap key ... does not exist.

**Rehber:** 3.2. **Önceki ilişki:** Karma; S07-19 mutable config/rollback değil config-start failure teşhisi.

**Ek resmî web kaynakları:** [Kaynak 1](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)

## Q41 — D

**Sade anlam / karar:** Cloud Armor direct URL bypass ingress boundary.

D, internet’ten doğrudan service yolunu sınırlar ve onaylı LB girişini korur. B sadece zaten denetlenen yolu güçlendirir. A egress ile ingress’i karıştırır. C uygulama authentication’ını korur ama doğrudan URL üzerinden LB/WAF bypass’ını kapatmaz. İç kaynakların kabul edilmesi ayrıca ağ güvenlik tasarımıdır; burada dış client bypass ölçülüyor.

**Belirleyici İngilizce koşul:** external client ... default URL / remain public through ... front end.

**Rehber:** 1.1. **Önceki ilişki:** Karma; S02-10 ingress temelinin Cloud Armor bypass teşhisi. Yeni ingress kavramı sayılmaz.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/run/docs/securing/ingress)

## Q42 — D + E

**Sade anlam / karar:** AI retrieved context güvenilir emir değildir.

D+E, içerik değerlendirmesi ve capability sınırını birlikte korur. A approved server ile her returned text’i trusted instruction sayar. C gereksiz credential erişimi açar. B kaynak bağlantısını doğruluk/izin kanıtı sanır. Bu ürün syntax ezberi değil AI context ve tool trust ayrımıdır.

**Belirleyici İngilizce koşul:** retrieved content is not equivalent to a trusted user instruction.

**Rehber:** 2.1. **Önceki ilişki:** Karma; S08-27 least privilege, burada returned content instruction boundary.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer) · [Kaynak 2](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)

## Q43 — D

**Sade anlam / karar:** Per-request RAM concurrency kapasite planlama.

D, tek request yeterliyken toplam aktif request sayısının memory etkisini yönetir. C instance üst sınırını değiştirir ama per-instance concurrency sınırını düzeltmez. B aktif RAM’i azaltmaz. A warm kapasiteyi artırır ama bir instance’a kabul edilen aktif request üst sınırını güvenli değere çekmez. Library değişene kadar ölçülen geçici config çözümüdür.

**Belirleyici İngilizce koşul:** one valid request fits / memory ... number of images.

**Rehber:** 3.1. **Önceki ilişki:** Karma; S01-07 shared-state veya S08-21 tek task OOM değil eşzamanlı memory toplamı.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/run/docs/configuring/concurrency) · [Kaynak 2](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits)

## Q44 — C

**Sade anlam / karar:** End-to-end async latency: backlog waiting vs handler span.

C, kuyrukta bekleme ile işlem süresini ayırır. A yakın tuzak: eksik zaman sınırları sadece daha fazla aynı span örneklenerek oluşmaz. B kısa handler içi span’ı yanlış darboğaz seçer. D ack süresi throughput artışı değildir. Sebep kapasite/consumer durumu ayrıca incelenir; metrik tek başına kesin root cause değildir.

**Belirleyici İngilizce koşul:** short execution times / increasing age ... unacknowledged message.

**Rehber:** 4.3. **Önceki ilişki:** Yeni ölçüm; S07-12 CPU attribution yerine queue wait observability.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/pubsub/docs/monitoring) · [Kaynak 2](https://docs.cloud.google.com/trace/docs/trace-context)

## Q45 — B

**Sade anlam / karar:** KMS key retirement: live migration tamam ama backup bağımlılığı sürüyor.

B, backup restore sırasında eski ciphertext’in hâlâ eski key version gerektirdiğini dikkate alır. C en yakın tuzak: yalnız live database kontrolü yeterli değildir. A metadata silmek ve D yeniden rotation yapmak backup ciphertext’ini dönüştürmez. Routine rotation ve live migration, saklanan bütün kopyaları otomatik güncellemez.

**Belirleyici İngilizce koşul:** Retained disaster-recovery backups still contain ciphertext encrypted under older versions.

**Rehber:** 1.2. **Önceki ilişki:** Karma; S06-13 KMS rotation/migration. Burada live migration tamam; kararı değiştiren kalan backup bağımlılığı. Yeni temel konu sayılmaz.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/kms/docs/key-rotation)

## Q46 — A

**Sade anlam / karar:** HPA request denominator ve desired replicas hesabı.

A: 400/500=%80; ceil(4×80/50)=ceil(6,4)=7. B request’i hard capacity eşiği sanır, target=%50’yi atlar. D/C sabit artış kuralı uydurur. Gerçek controller’da tolerance, stabilization, scaling policy, eksik metrics ve bounds etkileyebilir; soruda bunlar bilinçli dışarıda tutulmuştur.

**Belirleyici İngilizce koşul:** before stabilization or rate-limit behavior.

**Rehber:** 3.2. **Önceki ilişki:** Karma; S02-15 CPU requests ve HPA, yeni sayısal uygulama.

**Ek resmî web kaynakları:** [Kaynak 1](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)

## Q47 — C

**Sade anlam / karar:** Workflows saga compensation ve idempotency.

C, business compensation’ı açık tanımlar ve tekrarları güvenli yapar. D en yakın kavramsal tuzak: workflow state external transaction rollback değildir. A stable ID kullanır ama permanent failure sonrası gerekli compensation’ı sağlamaz. B bağlı iş adımlarını ve tamamlanma sözleşmesini bozar. Compensation da başarısız olabilir; izleme ve tekrar/manuel çözüm yolu tasarlanır.

**Belirleyici İngilizce koşul:** separate service APIs / each service commits its own state.

**Rehber:** 1.1. **Önceki ilişki:** Karma; S01-15 orchestration ve S04-16 external effects, yeni compensation planı.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/workflows/docs/best-practice)

## Q48 — C

**Sade anlam / karar:** Firestore collection group cross-parent query scope.

C, aynı collection ID altında farklı parent’lardaki review’ları hedefler. B yakın tuzak: tek parent path üzerindeki collection query kendiliğinden collection group olmaz. D parent read’in descendants’ı getireceğini varsayar. A index’i JOIN sanır. User/time alanlarının review’da bulunması ek join ihtiyacını kaldırır.

**Belirleyici İngilizce koşul:** across all products / stored directly in each review.

**Rehber:** 1.3. **Önceki ilişki:** Karma; 27 Eylül sözlü Firestore collection group/index açıklaması; S08-18 subcollection üzerine query scope.

**Ek resmî web kaynakları:** [Kaynak 1](https://firebase.google.com/docs/firestore/query-data/queries) · [Kaynak 2](https://firebase.google.com/docs/firestore/query-data/index-overview)

## Q49 — A

**Sade anlam / karar:** GenAI optional response bounded retry/fallback.

A, ürünün latency ve optional-output koşullarını uygular. D backoff getirir ama deadline’ı aşan sınırsız retry ile optional işi ana isteğe bağlamaya devam eder. C permanent input hatasını transient sanır. B kullanıcı kapsamı/validation sorunları ekler. Retry budget bitince ana işlem başarısı optional metne bağlanmaz; hata gözlemlenebilir kalır.

**Belirleyici İngilizce koşul:** optional / static fallback / request deadline.

**Rehber:** 4.2. **Önceki ilişki:** Karma; S08-40 retry + S08-48 uygulama GenAI tüketimi; yeni ürün kotası ezberi yok.

**Ek resmî web kaynakları:** [Kaynak 1](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/error-code-429) · [Kaynak 2](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps)

## Q50 — A + E

**Sade anlam / karar:** AI test: commit-before-ack failure injection invariant.

E+A, gerçek crash penceresini ve kalıcı invariant’ı birlikte ölçer. C gerçek davranışı mock’layarak bypass eder. B bağımsız oracle’ı kaldırır. D coverage artırabilir ama hedeflenen hata yolunu ölçmez. Örnek: başlangıç 100, tek operation +10 ise redelivery sonrası 110 kalmalı; 120 olmamalı.

**Belirleyici İngilizce koşul:** after ... commit but before acknowledgment / real handler.

**Rehber:** 2.3. **Önceki ilişki:** Karma; S08-39 AI oracle + önceki dedup, yeni failure-injection kanıtı.

**Ek resmî web kaynakları:** [Kaynak 1](https://firebase.google.com/docs/firestore/manage-data/transactions) · [Kaynak 2](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery)
