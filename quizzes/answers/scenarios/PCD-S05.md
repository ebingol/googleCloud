# PCD-S05 — Türkçe açıklamalı cevap anahtarı

**İlk denemeden sonra aç.** 25 Eylül 2026. Bu dosya kullanıcı yanıtı veya başarı kaydı değildir.

Kaynaklar **ek resmî web belgeleridir**; ders PDF sayfaları olarak gösterilmez. Ürün davranışları resmî belgelerle kontrol edildi; senaryolar ve bunlardan çıkarılan tasarım kararları özgündür. Gerçek sınav sorusu veya zorluk kalibrasyonu iddiası yok.

## Hızlı anahtar

| Soru | Cevap | Soru | Cevap |
|---|---|---|---|
| 1 | C | 11 | D |
| 2 | A | 12 | B |
| 3 | D | 13 | C |
| 4 | B | 14 | A |
| 5 | C | 15 | D |
| 6 | D | 16 | B, E |
| 7 | A | 17 | A |
| 8 | C | 18 | C, D |
| 9 | B | 19 | B |
| 10 | A | 20 | C |

Her soru 1 puan; Q16/Q18 tam küme gerektirir. Bilinmeyen kavram, kararsız doğru, yanlış gerekçe ve İngilizce yorumlama ayrı kaydedilir. Kaynakla/rehberle çözüm bağımsız puana eklenmez.

## Kapsam

[Güncel resmî rehber](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) ağırlıkları %32/%23/%24/%21. Birincil alan örneklemi: tasarım Q1/5/9/13/17/20 (6), geliştirme-test Q2/6/10/14/18 (5), deployment Q3/7/11/15/19 (5), entegrasyon Q4/8/12/16 (4). Q19 entegrasyonla da ilişkilidir, iki kez sayılmadı.

Bu sette geliştirme alanı ağırlıklı olarak ortam/AI araçları ve build verimliliğine ayrıldı; 2.3 test alt alanı bağımsız yeni soruyla ölçülmedi. Vision adı rehberde açık listelenmez; Q4 genel API performansı 4.2 uygulamasıdır. **Airflow/Composer adı da listelenmez:** Q13 ek orkestrasyon karşılaştırmasıdır. Rehberdeki tüm güvenlik, MCP, datastore, messaging, networking ve test alt başlıkları bu 20 soruyla tamamlanmış sayılmaz. Ürün sıklıkları hakkında kullanıcıdan gelen sınav deneyimi doğrulanmış dağılım olarak kullanılmadı.

## 1 — C

**Karar:** Memorystore cache-aside, tenant key ve kontrollü fallback. **Rehber:** 1.1.

Cache-aside, ortak cache ve tenant ayrımı koşullarını birlikte karşılar. TTL entry ömrünü sınırlar; kesin transaction-level freshness garantisi değildir. A instance-local durumu paylaşılan sanır ve tenant çakışmasını korur. B cache’i kayıt otoritesi yapar. D normal miss durumunu bile kesintiye dönüştürür. Fallback sınırsız olmamalı; rate limit/admission control veritabanını korur. Tasarım, ürünün cache kullanımından yapılan mühendislik çıkarımıdır.

**Ayırıcı İngilizce koşul:** database must remain authoritative; two tenants; reduced rate.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview).

## 2 — A

**Karar:** Cloud Workstations servis seçimi ve merkezi ortam. **Rehber:** 2.1.

Cloud Workstations merkezi yapılandırma, özelleştirilmiş container ortamı ve bireysel geliştirme alanı gereksinimlerini birlikte karşılar. B yapılabilir bir VM yaklaşımıdır ama istenmeyen filo/kurulum bakımını bırakır. C paylaşılan hesap ve oturum izolasyon şartını bozuyor. D session affinity’yi kalıcı çalışma alanı sanıyor; container dosya sistemi kalıcılık çözümü değildir.

**Ayırıcı İngilizce koşul:** centrally maintained container image; isolated workspace; no fleet-management portal.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/workstations/docs/overview).

## 3 — D

**Karar:** Canary ortak şema, expand-contract ve rollback. **Rehber:** 3.1.

İki revision aynı veritabanını kullanıyor: traffic split şema izolasyonu sağlamaz. Additive değişim, eski/yeni yazmaların birlikte çalışacağı senkronizasyon ve backfill planı ile doğrulanmalıdır; yalnız kolon eklemek yetmez. A/C eski kodu kırar. B ortak doğruluk yerine ayrışan iki yazma kaynağı oluşturur. Bu, Cloud Run rollout davranışından türetilen uygulama/veri uyumluluğu tasarımıdır; ürün otomatik expand-contract yapmaz.

**Ayırıcı İngilizce koşul:** same database; writes remain enabled; rollback without restoring.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration).

## 4 — B

**Karar:** Vision API offline batching/LRO ve kısmi retry. **Rehber:** 4.2.

Offline iş ve GCS çıktı tüketimi async batch/LRO yaklaşımına uyuyor. images:asyncBatchAnnotate isteği en fazla 2.000 image içerir; 50.000 görüntü bölünmelidir. Operation adının alınması tamamlanma değildir. A round-trip problemini ve gereksiz yeniden işlemeyi sürdürür. C limit dışıdır. D tamamlanma/hata kontrolünü atlar. Bu cevap online düşük gecikmeli her istekte async kullanılmalı demek değildir.

**Ayırıcı İngilizce koşul:** no user is waiting; consumes JSON files; partial failure.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/vision/docs/batch).

## 5 — C

**Karar:** Memorystore HA ile durability ayrımı. **Rehber:** 1.1.

Standard Tier HA, sıfır kayıp garantisi değildir: Redis replikasyonu asenkrondur. Durable order kaydı DB’de tutulur; bağlantılar yeniden kurulur ve cache yeniden doldurulabilir. A senkron replikasyon varsayar. B HA’yı kaldırır. D TTL ile replication lag’i karıştırır. HA ve cache doğruluk kaynağı ayrımı ölçülüyor.

**Ayırıcı İngilizce koşul:** acknowledged order remain recoverable; reconstruct status entries.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/memorystore/docs/redis/high-availability-for-memorystore-for-redis).

## 6 — D

**Karar:** Workstations persistent home ve image toolchain. **Rehber:** 2.1.

Configured persistent /home çalışma dosyaları içindir; çalışan container’a yapılan /opt değişiklikleri stop/start sonrasında güvenilir kalıcılık değildir. Ortak compiler custom image içine alınır. A uptime’a bağımlı geçici çözüm. B projeyi korur ama compiler kurulumunu tekrarlanabilir merkezi ortama taşımaz. C compiler’ı düzeltir ama uncommitted proje dosyalarını korumaz. Git commit/remote backup ayrıca iyi uygulamadır; persistent disk yedek yerine geçmez.

**Ayırıcı İngilizce koşul:** /home still present; newly created workstations; stop-and-start policy.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/workstations/docs/architecture).

## 7 — A

**Karar:** GKE HPA external backlog vs CPU/node scaling. **Rehber:** 3.2.

Talep CPU’ya yansımıyor; hazır external backlog metriği HPA’nın replica kararını talebe bağlar. B node kapasitesini artırır; mevcut boş kapasitede Pod sayısı sorununu çözmez. C Pod kaynaklarını değiştirir, bekleyen işi tüketen worker sayısını artırmaz. D CPU tetiklenmesini daha da geciktirir. Target/bounds downstream kapasitesiyle birlikte ayarlanır; sınırsız ölçek önerilmez.

**Ayırıcı İngilizce koşul:** CPU remains below target; spare capacity; external metric already exposed.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).

## 8 — C

**Karar:** BigQuery pagination token ve streaming tüketim. **Rehber:** 4.2.

maxResults her sayfanın kesin uzunluğu değildir; devam kararı token üzerinden verilir. Aynı tamamlanmış job’un sonucunu sayfalayarak değişen kaynak veriyi yeniden sorgulamayız. A yeni sorgularla farklı snapshot riski yaratır. B memory sınırını bozar. D mevcut hatayı korur.

**Ayırıcı İngilizce koşul:** short page still includes a continuation token; same completed job.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/bigquery/docs/paging-results).

## 9 — B

**Karar:** Spanner exact timestamp vs relative staleness. **Rehber:** 1.3.

Aynı exact timestamp aynı snapshot’ı seçer; retention koşulu soruda sağlanmış. A her çağrı anında güncel fakat farklı veri görebilir. C göreli süreyi her çağrının zamanından çıkarır; timestamp kayar. D üst yaş sınırıdır, ortak timestamp değildir. Çoklu read-only transaction da uygun başka tasarım olabilir; soru bağımsız çağrılar için seçilmiş T’yi soruyor.

**Ayırıcı İngilizce koşul:** exactly T; independent requests; inside version-retention period.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/spanner/docs/timestamp-bounds).

## 10 — A

**Karar:** Gemini Code Assist bağlam ve pinned API doğrulama. **Rehber:** 2.1.

Eksik local context, yanlış API önerisinin somut kaynağı. İlgili dosyalar + açık contract kısıtı + derleme/review döngüsü uygundur. A doğruluğu otomatik garanti etmez; doğrulama bu yüzden var. B bilgi eksikliğini çözmez. C review ve compatibility sınırını bozar. D derlenebilir ama yanlış iş davranışı üretir. Prompt/validation yaklaşımı resmî context davranışından mühendislik çıkarımıdır.

**Ayırıcı İngilizce koşul:** pinned library version; files not included; public API unchanged.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/gemini/docs/discover/works).

## 11 — D

**Karar:** Cloud Run secret volume latest vs startup env. **Rehber:** 3.1.

Secret environment variable instance başlangıcında çözülür. latest volume ve yeniden okuyan uygulama çalışan instance’ın yeni değeri almasını sağlar. Mevcut yapılandırmadan volume’a geçiş bir revision gerektirir; sonraki her rotation için revision gerekmemesi isteniyor. A eski süreçteki değeri yenilemez. B/C versiyonu sabitler; C ayrıca yalnız startup’ta okur.

**Ayırıcı İngilizce koşul:** already running instances; reread credential file; later rotations.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/run/docs/configuring/services/secrets).

## 12 — B

**Karar:** Spanner Query Stats vs tracing teşhis katmanı. **Rehber:** 4.3.

Trace gecikmenin servis içindeki yerini gösterdi; şimdi query aggregate ve plan ile nedenini araştırmak gerekiyor. Query statistics expensive pattern’ları belirlemeye yardım eder; execution plan tarama/erişim yolunu inceletir. A örnek sayısını artırır ama SQL planını sağlamaz. C ölçmeden yükü artırabilir. D başarı sayısı scan/CPU nedeni değildir.

**Ayırıcı İngilizce koşul:** trace propagation already working; SQL patterns; execution plans.

**Ek resmî kaynak:** [Query statistics](https://docs.cloud.google.com/spanner/docs/introspection/query-statistics) ve [execution plans](https://docs.cloud.google.com/spanner/docs/query-execution-plans).

## 13 — C

**Karar:** Airflow mevcut DAG migration vs Workflows. **Rehber:** 1.1 — ek ürün.

Mevcut Airflow DAG/operator ekosistemini koruma ve yönetim yükünü azaltma şartları managed Airflow’a götürür. Compatibility yine doğrulanmalı; sürümler arası sıfır değişiklik garantisi yok. A geçerli farklı orchestrator ama rewrite gerektirir. B/D orchestration özelliklerini yeniden geliştirmeyi bırakır. **Ek kapsam:** Airflow/Composer adı güncel rehberde açık listelenmiyor; 1.1 orkestrasyon karşılaştırmasına hazırlayanın eşleştirmesidir.

**Ayırıcı İngilizce koşul:** existing DAG code and operator ecosystem; cannot fund a rewrite.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview).

## 14 — A

**Karar:** Gemini Code Assist vs Cloud Assist ürün rolü. **Rehber:** 2.1.

Code Assist IDE/code odaklı, Cloud Assist cloud ortamını tasarlama/işletme/optimizasyon/troubleshooting odaklıdır. B temel rolleri ters çevirir. C/D bir tarafı doğru eşler, diğerinde mevcut amaca uygun yardımcı yerine özel uygulama geliştirir; böyle bir ürün geliştirme gereksinimi verilmedi. Uygulamanın kendi Gemini API entegrasyonu ayrı bir ihtiyaçtır; tüm AI kapsamı bu iki addan ibaret değildir.

**Ayırıcı İngilizce koşul:** two distinct workflows; supported IDE; resource and operational issues.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/gemini/docs/overview).

## 15 — D

**Karar:** GKE preStop + SIGTERM ortak termination bütçesi. **Rehber:** 3.2.

Grace countdown preStop öncesinde başlar; hook bitince uygulamaya sınırsız yeni süre verilmez. 20+25 saniye ve pay için örneğin 60 saniye uygundur. A readiness’i değiştirir, sonlandırma bütçesini değil. B PDB’nin rolünü yanlış genişletir; direct deletion ve termination timeout çözümü değildir. C yeni Pod kapasitesini değiştirir, eski Pod’un drain süresini değil.

**Ayırıcı İngilizce koşul:** twenty seconds then twenty-five additional; grace period thirty.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/).

## 16 — B, E

**Karar:** API retry jitter, deadline ve layered retry. **Rehber:** 4.2.

Idempotent olması her hatayı geçici yapmaz. B retry’ları dağıtır ve toplam süreyi sınırlar; E katmanlı retry çarpanını kaldırır ve kalıcı authorization hatasını ayırır. A 4xx’leri yanlış geneller (429 geçici olabilir, değişmeyen izin hatası farklıdır). C attempt patlamasını büyütür. D senkron dalgaları korur.

**Ayırıcı İngilizce koşul:** client already retries; wrapper also retries; overall deadline.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/storage/docs/retry-strategy).

## 17 — A

**Karar:** Storage Autoclass erişim paterni vs age lifecycle. **Rehber:** 1.1.

Öngörülemeyen access pattern ve otomatik class yönetimi Autoclass’a uyar. En ucuz olacağı garanti değil; yönetim/erişim maliyetleri değerlendirilir. B age ile son erişimi karıştırır. C online availability ile fiyat eşitliğini karıştırır. D retention silmeyi kontrol eder, erişime göre promotion yapmaz.

**Ayırıcı İngilizce koşul:** unexpectedly popular years later; according to access behavior.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/storage/docs/autoclass).

## 18 — C, D

**Karar:** Cloud Build Docker layer ordering ve remote cache. **Rehber:** 2.2.

İki ayrı neden var: layer invalidation ve fresh worker’da cache yokluğu. C dependency input’larını source’dan ayırır; D --cache-from gibi mekanizmaya kullanılabilir eski image sağlar. A lock gereksinimini bozar. B yeni kodu dağıtmaz. E cache’i kapatır. Cache doğrulanmış build/test yerine geçmez; lockfile değişince dependency layer yeniden üretilmeli.

**Ayırıcı İngilizce koşul:** entire repository before npm ci; fresh worker; previous image available.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/build/docs/optimize-builds/speeding-up-builds).

## 19 — B

**Karar:** API Gateway backend identity ve service-level Invoker. **Rehber:** 3.1 / 4.2.

Frontend JWT doğrulaması backend invocation IAM grant’inin yerine geçmez. Çağıran gateway backend-auth SA olduğundan service-level Invoker bu SA’ya verilir. A çalışan backend kimliğini çağıran sanır. C yanlış principal ve gereksiz geniş yetki. D backend authentication gereksinimini kaldırır. Audience/network soruda doğru verilerek hata sınırı IAM’e daraltılmıştır.

**Ayırıcı İngilizce koşul:** gateway service account lacks permission; backend remains authenticated.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/api-gateway/docs/securing-backend-services).

## 20 — C

**Karar:** IAM inherited allow daraltma ve bucket scope. **Rehber:** 1.2.

Allow izinleri hiyerarşi boyunca birleşir; alt kaynakta dar grant veya boş policy parent grant’i geri almaz. C fazla parent grant’i kaldırıp gerekli scope’ta yeniden verir, diğer principal’ları korur. A yetkiyi daraltmaz. B/D inherited grant’i geçersiz kılmaz. Sorudaki başka grant yok koşulu çözümü tekilleştirir.

**Ayırıcı İngilizce koşul:** project level; allow-policy changes only; other principals unchanged.

**Ek resmî kaynak:** [İlgili ürün belgesi](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control).

## Değerlendirme notu

Q19, önceki Invoker yönü kararının başka bir gateway sınırında pekiştirmesidir; yeni konu başarısı diye sayılmaz. Q4/Q9/Q14 daha önce paylaşılan açıklamalardaki kavramlarla ilişkilidir. Hiç görülmemiş veya tamamen bağımsız karar oldukları iddia edilmez. S04 ve S05 henüz çözülmedi; önceki ilk deneme sonuçları değişmez.
