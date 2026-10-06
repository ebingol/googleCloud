# Senaryo soru geçmişi

Bu dosya soru üretiminde tekrar kontrolü içindir; cevap ipuçları içerir. Öğrenci yeni seti çözerken açmamalı. Yeni set hazırlandığında satırları ekle; sadece planlanan soru çözülmüş sayılmaz.

| ID | Ölçülen karar / belirleyici koşul | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S01-01 | Tek secret payload, runtime identity, secret kapsamı | İlk tanılama | Yanlış |
| S01-02 | %5 rollout ve rollback, minimum ek altyapı | İlk tanılama | Doğru |
| S01-03 | Sıralı build'de özel /tmp çıktısı kayıp, ortak workspace | İlk tanılama | Yanlış |
| S01-04 | Google kimliği olmayan müşteriye tek nesne, geçici signed URL | İlk tanılama | Doğru |
| S01-05 | Gelecekte HTTP gönderimi ve dispatch limiti, Cloud Tasks | İlk tanılama | Doğru |
| S01-06 | A→B: B üzerinde A'ya Invoker ve B audience'lı ID token | İlk tanılama | Yanlış |
| S01-07 | Eşzamanlı shared-state bozulması, sequential güvenli, concurrency 1 | İlk tanılama | Yanlış; dil güçlüğü |
| S01-08 | Dockerfile yok, desteklenen uygulama, buildpacks | İlk tanılama | Doğru |
| S01-09 | Son koltuk rezervasyonu, read/check/write atomik transaction | İlk tanılama | Doğru |
| S01-10 | Eventarc tekrarlı event, kalıcı atomik dedup ve güncelleme | İlk tanılama | Doğru |
| S01-11 | Local ADC ile gcloud login ayrımı, runtime SA | İlk tanılama | Doğru |
| S01-12 | Idle sonrası initialization gecikmesi, min instances | İlk tanılama | Doğru |
| S01-13 | allowFailure test hatasını yutuyor, deployment gate | İlk tanılama | Doğru |
| S01-14 | Global ilişkisel transaction + yatay write ölçeği, Spanner | İlk tanılama | Doğru |
| S01-15 | Sıralı dallanan süreç, uzun callback, Workflows | İlk tanılama | Doğru |
| R01-01 | Tek secret metadata, payload yasak, Viewer | Hedefli tekrar; S01-01'in gereksinimi ters | Doğru |
| R01-02 | Çıktı workspace'te, test yanlış /tmp yolunu okuyor | Hedefli tekrar; S01-03'e yakın | Doğru; gerekçe zayıf |
| R01-03 | orders→pricing rol + token birlikte | Hedefli yakın tekrar; S01-06 | Doğru |
| R01-04 | Process-wide buffer çakışıyor, concurrency 1 | Hedefli yakın tekrar; S01-07 | Doğru |
| R01-05 | Invoker mevcut; ID token audience çağıranı gösteriyor | Hedefli tanılama; S01-06'nın tek hata ayrımı | Yanlış; sonra sözlü doğru |

Tam metinler: [S01](PCD-S01.md), [R01](PCD-R01.md). Anahtarlar `../answers/scenarios/` altında. Sonuçlar `results/` altında.

## Rehberli görülen ek kararlar

- R10-04: revision tag URL, green URL öneki, trafik yüzdesi, in-flight requests, best-effort session affinity. 20 Eylül birlikte çözüldü; D/B/D/C/C, 4/5.
- R01-01 Q2: image + configuration revision'ı tanımlar. Çeviriyle doğru cevap açıklandı; bağımsız sonuç yok.
- F06-03 Q1/Q3: kernel paylaşımı; her build step'in container içinde çalışması. Açıklandı; bağımsız sonuç yok.
- Sözlü checkout→inventory: Invoker yönü ve audience doğru; R01-05 sonrası anlık kontrol. Yeni bağımsız sınav sayılmaz.

Yeni soru eklerken format: `ID | konu/karar/belirleyici koşul | yeni/karma/gecikmeli tekrar + benzer ID | henüz çözülmedi`. Eski sorulara yakınlığı yalnız anahtar kelimelerle değil çözüm mantığıyla değerlendir.

## PCD-S02 — 22 Eylül 2026, düzeltilmiş kapsam

[Sorular](PCD-S02.md) · [Anahtar](../answers/scenarios/PCD-S02.md). Kullanıcı Cloud Run, Cloud Run functions ve GKE sorularını tamamladığını bildirdi ve sınavı bu alanlardan istedi. 5 + 5 + 5 dağılımı kullanıldı. 11 yeni + 4 karma; bu sürümde gecikmeli tekrar yok.

İlk Cloud Run ağırlıklı taslak kullanıcı cevabı yokken değiştirildi; eski S02 soru numaraları geçersizdir. İlk taslakta görülen beş Cloud Run sorusu korunup yeni sıraya taşındı (eski 1→1, 3→4, 4→7, 11→10, 12→13); bunları S03'te hiç görülmemiş soru diye sunma. Çıkarılan taslak kararları: Error Reporting, Artifact Registry service agent, idle CPU, Eventarc parser, Direct VPC, Trace, job exit/retry, SIGTERM, push ack, env önceliği. Bunlar hazırlanmıştı ama kullanıcı çözümü yok; yeniden kullanılırsa bu geçmiş belirtilmeli.

| ID | Konu / ölçülen karar / belirleyici koşul | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S02-01 | Cloud Run service/job; 80 dakika, HTTP yok, bitince çıkış | Yeni; R01-02, eski senaryoda yok | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-02 | Functions HTTP webhook; aynı istekte doğrulama yanıtı | Yeni; C01-02, S01 event koordinasyonundan farklı | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-03 | GKE Service selector yanlış; Ready Pod etiketleriyle eşleştirme | Yeni; T08-03 | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-04 | Cloud Run port açık ama initialization bitmemiş; HTTP startup | Yeni; S01-12 min instances kararından farklı | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-05 | Functions /tmp dosyaları birikiyor; hata dahil cleanup | Yeni; C05-01 | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-06 | GKE v2 rollout; tek Pod yerine Deployment template güncelleme | Karma; S01-02 rollout + T08-02 controller | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-07 | Cloud Run/Cloud SQL; process havuzu ve bağlantı iadesi | Yeni; R11-03, transaction ölçmüyor | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-08 | Functions; geçersiz olay kalıcı kaydı ve transient retry ayrımı | Karma; S01-10 event güvenilirliği + C05-04 | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-09 | GKE emptyDir kaybı; retained PVC ile Pod replacement | Yeni; T08-04 | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-10 | Cloud Run dış LB girişi, direct internet engeli; IAM korunacak | Yeni; S01-06 token kararından farklı ağ katmanı | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-11 | Functions; mevcut kayıtlı handler ile entry point uyuşmazlığı | Yeni senaryo; C01-05 kaynakları 21 Eylülde konuşuldu, bağımsız puan yok | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-12 | GKE geçici dependency kaybı; restart gerekmiyor, readiness | Yeni; T08-03 ilişkili, probe ayrıntısı ek resmî kaynak | Yanlış (kullanıcı beyanı); probe kavram eksikliği bildirildi, seçilen şık bilinmiyor |
| S02-13 | Cloud Run secret env; sürüm sabitleme ve rollback | Karma; S01-01 secret + S01-02 rollout | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-14 | Functions Firestore update; girdi değişmediyse yazmadan dön | Karma; C04-03 + S01-10 olay güvenilirliği, dedup ezberi değil | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-15 | GKE HPA CPU utilization; CPU request eksik | Yeni; HPA ek resmî kaynak | Doğru (kullanıcı beyanı); şık kaydı yok |

22 Eylül sonuç güncellemesi: 14/15, 20 dakika; kaynak kullanıcı beyanı. Soru dosyası cevapları boş, anahtar kullanıcı cevabı olarak aktarılmadı. Q12 açıklaması ilk sonucu değiştirmez.

## PCD-S03 — 23 Eylül 2026

[Sorular](PCD-S03.md) · [Anahtar](../answers/scenarios/PCD-S03.md). 5 Cloud Run + 5 Functions + 5 GKE; 9 yeni karar + 4 karma + 2 gecikmeli uygulama. Uzun İngilizce senaryolar ve koşullara göre alternatif eleme korundu. Kaynaklar güncel resmî web belgeleri; anahtarda ek kaynak etiketi var. Yeni karar etiketi hiç görülmemiş tüm kavramlar anlamına gelmez.

| ID | Konu / ölçülen karar / belirleyici koşul | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S03-01 | GKE ConfigMap; subPath güncellenmez, restart olmadan dosya projection ve yeniden okuma | Yeni; S02-06 rollout yerine canlı dosya yenilemesi | Yanlış; kullanıcı D, anahtar B |
| S03-02 | Cloud Run candidate tag destination ile normal service audience ayrımı; Invoker hazır | Gecikmeli tekrar; R01-05 + rehberli R10-04, yeni birleşik uygulama | Yanlış; kullanıcı C, anahtar D |
| S03-03 | Functions upload Promise tamamlanmadan handler dönüşü; sonucu Promise ile bağlama | Yeni; C05-01; S02-08 hata sınıflamasından farklı completion kararı | Yanlış; kullanıcı C, anahtar A |
| S03-04 | GKE dedicated KSA ve bucket üzerinde direct federated principal grant birlikte | Karma; S01-11 ADC/identity + GKE WIF | Eksik seçim; kullanıcı D, anahtar C, D |
| S03-05 | Functions gecikmiş Storage event; saklanan generation ile doğru input bytes seçme | Yeni; S01-10 dedup sorusundan farklı, dedup zaten sağlanmış | Yanlış; kullanıcı C, anahtar B |
| S03-06 | Cloud Run proxy ingress bind 0.0.0.0 ve aynı instance localhost sidecar | Yeni; R09-01 runtime contract genişletmesi | Yanlış; kullanıcı B, anahtar C |
| S03-07 | GKE voluntary eviction; 3 sağlıklı Pod, minAvailable 2; rollout ayarı yeterli değil | Yeni; S02-06 rollout mekanizmasından farklı eviction bütçesi | Yanlış; kullanıcı C, anahtar A |
| S03-08 | Cloud Run tek CPU hotspot; çok vCPU ortalaması ve concurrency ile request scaling | Gecikmeli uygulama; R01-04/S01-07 concurrency, yeni performans bağlamı | Yanlış; kullanıcı A, anahtar D |
| S03-09 | Functions sıra dışı Firestore snapshots; sürüm karşılaştırma ve atomik summary update | Karma; S01-09 transaction + S01-10 event; S02-14 self-loop kararından farklı | Doğru; kullanıcı C, anahtar C |
| S03-10 | GKE NetworkPolicy; source egress ve destination ingress izinleri birlikte | Karma; S02-10 ağ erişim katmanı + Pod selector, yeni GKE mekanizması | Doğru; kullanıcı A, B, anahtar A, B |
| S03-11 | Cloud Run 504 işlemi iptal/rollback etmez; retry öncesi sonuç belirsizliği | Yeni timeout teşhisi; S01-10 idempotency ile ilişkili, yalnız dedup tasarımı sorulmuyor | Doğru; kullanıcı B, anahtar B |
| S03-12 | Functions source build denied principal; builder/runtime ayrımı ve prod-data sınırı | Karma; S01-01 runtime kimlik + C01-06 build | Doğru; kullanıcı D, anahtar D |
| S03-13 | GKE Pending CPU; gerçek kullanım değil requests, tek node kapasitesi | Yeni; S02-15 HPA utilization değil scheduler kapasitesi | Doğru; kullanıcı A, anahtar A |
| S03-14 | Functions Pub/Sub CloudEvent adapter testi; zarf/base64/business JSON ayrımı | Yeni ölçülen adapter test kararı; S02 çıkarılan parser taslağıyla ilişkili, hiç görülmemiş konu iddiası yok | Doğru; kullanıcı C, anahtar C |
| S03-15 | Cloud Run public API static egress; private-ranges-only mevcut NAT yolunu atlıyor | Yeni ölçülen egress karar; S02 çıkarılan Direct VPC taslağıyla ilişkili | Doğru; kullanıcı B, anahtar B |

23 Eylül: Q2 C (anahtar D), Q8 A (anahtar D); yeni uygulamalarda tam doğru yok. Q2’de audience parçası doğru, tag hedeflemesi eksik; önceki tüm bilgiyi unuttuğu çıkarılamaz. Probe tekrarı 25 Eylül; workspace ve diğer bekleyen kararlar çözülmüş sayılmadı.

S03 ilk cevaplar: 7/15 (%46,7), süre bildirilmedi. [Sonuç](results/PCD-S03-attempt-01.md). Kullanıcı soyutlama/eşleştirme güçlüğü bildirdi; hata nedenleri rehberli ayrıştırılacak.

23 Eylül S03 Q1–Q8 tekrar: 1 B, 2 B, 3 A, 4 A+D, 5 D, 6 A, 7 D, 8 A → 2/8 (Q1/Q3 doğru). İlk sonuç sütunları korunur. [Ayrı kayıt](results/PCD-S03-retry-01.md). Gerekçe ve gecikmeli kalıcılık doğrulanmadı.

## PCD-S04 — 24 Eylül 2026

[Sorular](PCD-S04.md) · [Anahtar](../answers/scenarios/PCD-S04.md). Kullanıcının tüm konulardan 20 soru talebi, eski 15 soru/5+5+5 dağılımının önüne geçti. Dört ana alan 6/5/5/4; bütün alt maddeleri ölçme iddiası yok. 13 yeni karar + 6 karma + 1 erken pekiştirme. Yeni etiketi eski ders quizlerinde kavramın hiç bulunmadığı anlamına gelmez. Kaynaklar ek resmî web belgeleri. S01/S02/S03 tam metinleri ve S03 sonuçları kontrol edildi; puanlar korunur.

| ID | Konu / ölçülen karar / belirleyici koşul | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S04-01 | Bigtable timestamp hotspot; dengeli device prefix + zaman aralığı | Yeni; F03-02/U04-06 ile ders bağlantısı | Henüz çözülmedi |
| S04-02 | Cloud Build iki bağımsız check compile sonrası; package ikisini bekler | Karma; S01-03 workspace zaten işler, S01-13 failure flag değil DAG | Henüz çözülmedi |
| S04-03 | Test edilen digest ile gcloud deploy; mutable tag race ve rebuild yasak | Yeni karar; S02-06 image rollout değil artifact kimliği | Henüz çözülmedi |
| S04-04 | Pub/Sub her takıma tüm event; bağımsız subscription ve grup içi load sharing | Yeni; S01-10 duplicate kararından farklı fan-out | Henüz çözülmedi |
| S04-05 | Cloud SQL regional HA; synchronous zonal failover, schema korunacak | Yeni; S01-14 global Spanner scale kararı değil | Henüz çözülmedi |
| S04-06 | Firestore server emulator env; yerel endpoint ve production parity sınırı | Yeni; F02-03 emulator ders bağlantısı | Henüz çözülmedi |
| S04-07 | GKE rollout dört available, bir surge; maxUnavailable 0 / surge 1 | Karma; S02-06 rollout + S03-07 eviction ayrımı | Henüz çözülmedi |
| S04-08 | Storage create-only upload; generationMatch 0 ve uncertain response doğrulama | Karma; S03-05 generation okuma yerine atomic create, S03-11 uncertain result | Henüz çözülmedi |
| S04-09 | Apigee partner interval quota; burst policy zaten var | Yeni; F01-04 genel gateway'den ayrıntı | Henüz çözülmedi |
| S04-10 | Gemini test generation; contract oracle, time/API kontrolü, boundary tests | Yeni; AI destekli test değerlendirmesi | Henüz çözülmedi |
| S04-11 | Eventarc Storage finalized + doğru bucket; metadata event ayrımı | Yeni; S03-14 payload parser değil trigger filter | Henüz çözülmedi |
| S04-12 | Servisler arası trace context propagation ve span parent | Yeni ölçülen karar; S02 çıkarılmış Trace taslağıyla konu ilişkisi | Henüz çözülmedi |
| S04-13 | External CI WIF; repo claim restriction + repository IAM | Karma; S03-04 GKE KSA yerine external OIDC trust boundary | Henüz çözülmedi |
| S04-14 | Test onayı digest attestation; Binary Authorization admission gate | Yeni; S01-13 pipeline failure gate yerine cluster enforcement | Henüz çözülmedi |
| S04-15 | Cloud Run idle CPU, disposable refresh; min instance zaten var, billing değişimi | Yeni ölçülen karar; S02 çıkarılan idle CPU taslağı, S01-12 cold start değil | Henüz çözülmedi |
| S04-16 | Firestore retried callback dış ödeme; durable pending record + provider key | Karma; S01-09/10 atomik dedup'tan dış sistem crash penceresine genişleme | Henüz çözülmedi |
| S04-17 | Storage retention lock; admin süreyi azaltamamalı | Yeni; U04-01 lifecycle/versioning ayrımı | Henüz çözülmedi |
| S04-18 | Build secret; build identity specific secret + availableSecrets/secretEnv | Karma; S01-01 runtime secret + S03-12 build identity, yeni injection kararı | Henüz çözülmedi |
| S04-19 | GKE startup liveness'ı bekletir; steady deadlock hızını koruma | Erken pekiştirme; S02-12 ve 22 Eylül probe açıklaması, 25 Eylül kontrolünden erken | Henüz çözülmedi |
| S04-20 | Compute Engine compatible custom OS/kernel ve container yasağı | Yeni; S02-01 Run job değil host OS gereksinimi | Henüz çözülmedi |

Probe, workspace veya diğer tekrar kuyruğu yalnız soru hazırlandı diye tamamlanmadı. S04 sonucu yok; yeni set ID'si S05.


## PCD-S05 — 25 Eylül 2026

[Sorular](PCD-S05.md) · [Anahtar](../answers/scenarios/PCD-S05.md). Kullanıcı uzun paragraflı yeni S05 istedi. 20 soru; 18 tek + 2 çift seçim (Q16/Q18); 50 dakika kişisel hedef. Dört ana alan 6/5/5/4; 10 yeni ölçüm + 9 karma + 1 pekiştirme. Yeni ölçüm, daha önce hiç açıklama yapılmadığı anlamına gelmez. S04 değiştirilmedi; iki set için de sonuç yok. Airflow ek ürün kapsamı, Vision genel API performansı uygulamasıdır.

| ID | Konu / ölçülen karar | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S05-01 | Memorystore cache-aside, tenant key ve kontrollü fallback | Yeni; S01-07 process shared-state hatası yerine dağıtık cache tasarımı | Doğru |
| S05-02 | Cloud Workstations servis seçimi ve merkezi ortam | Yeni | Doğru |
| S05-03 | Canary ortak şema, expand-contract ve rollback | Karma; S01-02 rollout ve rehberli R10-04 traffic migration üzerine veri uyumluluğu, eski sorunun aynısı değil | Yanlış; kullanıcı A, anahtar D |
| S05-04 | Vision API offline batching/LRO ve kısmi retry | Yeni ölçüm; 25 Eylül konuşmasında async/sync ayrımı açıklandı | Doğru |
| S05-05 | Memorystore HA ile durability ayrımı | Karma; S04-05 Cloud SQL HA bilgisini Redis’e yanlış genellememe | Doğru |
| S05-06 | Workstations persistent home ve image toolchain | Yeni; Q2 servis seçiminden farklı yaşam döngüsü kararı | Doğru |
| S05-07 | GKE HPA external backlog vs CPU/node scaling | Karma; S02-15 HPA kaynak koşullarından farklı talep metriği | Doğru |
| S05-08 | BigQuery pagination token ve streaming tüketim | Yeni | Doğru |
| S05-09 | Spanner exact timestamp vs relative staleness | Yeni ölçüm; Gemini rehberindeki staleness konusu konuşuldu | Doğru |
| S05-10 | Gemini Code Assist bağlam ve pinned API doğrulama | Karma; S04-10 test oracle yerine implementation context | Doğru |
| S05-11 | Cloud Run secret volume latest vs startup env | Karma; S02 pinned secret/rollback yerine canlı rotation gereksinimi | Doğru |
| S05-12 | Spanner Query Stats vs tracing teşhis katmanı | Karma; S04-12 propagation tamam, Gemini metninde bu ayrım görüldü | Doğru |
| S05-13 | Airflow mevcut DAG migration vs Workflows | Yeni; S01-15 yeni workflow callback tasarımından farklı migration | Doğru |
| S05-14 | Gemini Code Assist vs Cloud Assist ürün rolü | Yeni ölçüm; 25 Eylül konuşmasında ürün ayrımı açıklandı | Doğru |
| S05-15 | GKE preStop + SIGTERM ortak termination bütçesi | Karma; S03-07 PDB ve S02 çıkarılmış SIGTERM taslağı, yeni hook bütçesi | Yanlış; kullanıcı B, anahtar D |
| S05-16 | API retry jitter, deadline ve layered retry | Karma; S03-11/S04-08 uncertain write yerine idempotent GET retry orchestration | Doğru |
| S05-17 | Storage Autoclass erişim paterni vs age lifecycle | Yeni; S04-17 retention kararından farklı maliyet/erişim tasarımı | Doğru |
| S05-18 | Cloud Build Docker layer ordering ve remote cache | Yeni; S04-02 step DAG ve S04-03 artifact kimliğinden farklı cache kararı | Yanlış; kullanıcı B, D, anahtar C, D |
| S05-19 | API Gateway backend identity ve service-level Invoker | Pekiştirme; S01-06/R01-03 invoker yönü gateway üzerinde, yeni temel karar sayılmaz | Doğru |
| S05-20 | IAM inherited allow daraltma ve bucket scope | Karma; S01-01 secret least privilege üzerine inherited izin kaldırma | Doğru |

Yalnız hazırlık tamamlandı; tekrar kuyruğunda başarı/kalıcılık teyidi yok. Sonraki yeni set S06.

25 Eylül S05 ilk cevaplar: **17/20 (%85), 70–80 dakika**. [Kayıt](results/PCD-S05-attempt-01.md). Q3/Q15/Q18 yanlış; ilk seçimler korundu. Gerekçe/güven ve bağımsız koşullar bilinmiyor. Açıklama sonrası kalıcılık teyidi yok.


## PCD-S06 — 25 Eylül 2026

[Sorular](PCD-S06.md) · [Anahtar](../answers/scenarios/PCD-S06.md). Kullanıcı daha uzun paragraflar, daha çetrefilli şıklar ve öncelikli dayanak olarak exam guide istedi. 20 soru; 18 tek + Q6/Q18 çift seçim. Birincil alan örneklemi 6/5/5/4; 11 yeni ölçüm + 9 karma, gecikmeli tekrar yok. Yeni ölçüm, kavramın ders bankasında/konuşmada hiç görülmediği anlamına gelmez. S05 Q3/Q15/Q18 anlık açıklamaları isim değiştirilerek tekrarlanmadı.

| ID | Konu / ölçülen karar | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S06-01 | Cloud Tasks schedule/rate/concurrency seçimi | Yeni; S01-15 callback workflow yerine zamanlanmış tek hedef dispatch | Yanlış; kullanıcı C, anahtar B |
| S06-02 | ADC credential-source precedence ve IDE environment | Karma; S01-11 CLI/ADC ayrımına environment precedence ekleniyor | Doğru |
| S06-03 | Cloud Run cross-project image pull kimliği | Karma; S03-12 builder/runtime ayrımına platform service agent ekleniyor; S02 çıkarılmış taslakta konu vardı | Yanlış; kullanıcı B, anahtar A |
| S06-04 | Pub/Sub ordering scope ve regional publishing | Yeni ölçüm; Gemini setinde ordering bölgesellik konusu incelendi; S04-04 fan-out değil | Doğru |
| S06-05 | Storage signed GET URL kapsam ve expiry | Yeni; S03-05 object generation ve Gemini POST policy konuşmasından farklı download yetkisi | Yanlış; kullanıcı B, anahtar D |
| S06-06 | AI IDE/MCP tool yüzeyi ve credential sınırı | Yeni; S05-10 context seçimi yerine MCP execution permissions | Doğru |
| S06-07 | GKE memory request/limit ve OOM teşhisi | Karma; S03-13 CPU scheduling üzerine per-container memory failure | Doğru |
| S06-08 | Cloud SQL Auth Proxy ile private network reachability | Karma; S02-07 connection pool değil ağ önkoşulu; Gemini private-pool topoloji incelemesiyle ilişkili | Doğru |
| S06-09 | Bigtable replicated instance app-profile consistency | Yeni; S04-01 row-key hotspot değil replicated routing; S05-09 Spanner snapshot’tan farklı | Doğru |
| S06-10 | Cloud Build integration-test isolation ve failure preservation | Karma; S01-13 gate ve S04-02 dependency sırasına eşzamanlı test isolation ekleniyor | Doğru |
| S06-11 | Apigee API contract versioning ve backend routing | Yeni; S04-09 quota parametresi değil birlikte yaşayan API contract | Doğru |
| S06-12 | Observability metric cardinality ve structured logs | Yeni; S04-12 trace propagation/S05-12 Query Stats yerine label tasarımı | Doğru |
| S06-13 | KMS rotation ile eski ciphertext migration ayrımı | Yeni; S05-11 secret rotation yerine encryption-key lifecycle | Doğru |
| S06-14 | Cloud Build provenance output ve verification gate | Karma; S04-14 admission attestation yerine builder provenance üretimi | Yanlış; kullanıcı A, anahtar B |
| S06-15 | Cloud Run HTTP/2 h2c ve TLS termination | Yeni; S03-06 bind/sidecar port yerine transport protocol sınırı | Doğru |
| S06-16 | BigQuery Storage Write API pending streams atomic commit | Yeni; S05-08 result pagination değil batch write visibility | Doğru |
| S06-17 | Storage lifecycle Delete ile retention birleşimi | Karma; S04-17 lock ve S05-17 Autoclass yerine retention/deletion etkileşimi | Yanlış; kullanıcı D, anahtar C |
| S06-18 | Artifact Analysis bulgusundan rebuild ve verified rollout | Karma; S04-03 digest kimliği yeni vulnerability-remediation bağlamında; S05-18 layer cache tekrarı değil | Yanlış; kullanıcı B, D, anahtar B, E |
| S06-19 | GKE regular init container ve shared emptyDir | Karma; S02-04 startup ve S02-09 volume lifetime üzerine process-start dependency; aynı probe sorusu değil | Doğru |
| S06-20 | Firestore index exemptions ve write fanout | Yeni; S04-06 emulator/S04-16 transaction değil schema-index tasarımı | Yanlış; kullanıcı B, anahtar D |

S06 yalnız hazırlandı; yeni kullanıcı yanıtı/süre/puan yok. Sonraki yeni set S07.

25 Eylül S06 ilk cevaplar: **13/20 (%65), 73 dakika**. [Kayıt](results/PCD-S06-attempt-01.md). Q1/Q3/Q5/Q14/Q17/Q18/Q20 yanlış. İlk seçimler korunur; güven/gerekçe/yardım bilgisi ve açıklama sonrası teyit yok.


## PCD-S07 — 26 Eylül 2026

[Sorular](PCD-S07.md) · [Anahtar](../answers/scenarios/PCD-S07.md). Kullanıcının açık yeni sınav talebiyle hazırlandı. 20 soru; 18 tek + Q6/Q11 çift seçim. Gövdeler 128–142 kelime (ortalama 134,5). Güncel resmî rehber dört ana alanı 6/5/5/4; 12 yeni ölçüm + 7 karma + 1 gecikmeli uygulama. Yeni ölçüm tüm kavramların hiç görülmediği anlamına gelmez. Teknik dayanaklar ek resmî web kaynakları; anahtarda soru bazında eşleştirme var.

| ID | Konu / ölçülen karar | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S07-01 | Memorystore cache stampede; instance çapında per-key bounded refresh lease | Yeni; S05-01 cache-aside/tenant key değil aynı miss için eşzamanlı refresh | Doğru; kullanıcı C |
| S07-02 | Cloud Build private pool ile private VM integration-test endpoint ağı | Karma; S06-08 private reachability ve S06-10 integration test, farklı build network kararı | Doğru; kullanıcı A |
| S07-03 | Cloud Run source upload .gcloudignore ile .dockerignore ayrımı | Yeni; S05-18 Docker cache değil source pakete giriş katmanı | Doğru; kullanıcı D |
| S07-04 | Storage metadata metageneration precondition + conflict sonrası merge | Karma; S04-08 content create-only yerine sabit generation üzerinde metadata concurrency | Doğru; kullanıcı B |
| S07-05 | IAP signed assertion validation ve backend audience sınırı | Yeni; önceki service-to-service ID token sorularından farklı IAP end-user assertion | Doğru; kullanıcı A |
| S07-06 | BuildKit secret mount ve command output/cache secret sızıntısı | Karma; S04-18 Secret Manager injection sonrası Docker layers sınırı | Yanlış; kullanıcı D,E; anahtar B,D |
| S07-07 | HPA scaleDown stabilization; hızlı scale-up ve geçici demand dip | Yeni; S05-07 metric seçimi yerine scale yönü/pencere davranışı | Yanlış; kullanıcı B; anahtar C |
| S07-08 | Storage partial response fields pagination tokenını da içermeli | Karma; S05-08 pagination loop doğruyken field projection kontrol alanını eliyor | Doğru; kullanıcı D |
| S07-09 | Cloud SQL read replica lag; confirmation primary, toleranslı reads replica | Yeni; S04-05 HA/failover değil read routing ve freshness | Doğru; kullanıcı B |
| S07-10 | Workstations User resource scope; Creator/Admin/Policy Admin ayrımı | Yeni; S05-02/06 ürün seçimi/persistence yerine existing-resource access | Doğru; kullanıcı C |
| S07-11 | Cloud Run job task index/count partition + retry-safe output | Karma; S02-01 job seçimi ve S01-10 idempotency üzerine task/parallelism ayrımı | Yanlış; kullanıcı D,E; anahtar A,E; 2:26 |
| S07-12 | CPU method attribution için Profiler; Trace handlerı zaten daraltmış | Yeni; S05-12 SQL Query Stats yerine application CPU teşhisi | Doğru; kullanıcı A; 27 Eylül; süre yok |
| S07-13 | GKE WIF same-project pool name-based identity sameness | Yeni; S03-04 direct grant üzerine cross-cluster trust boundary, grant syntax ezberi değil | İlk seçim yok; doğru D açıklanmış rehberli çalışma, bağımsız puana dahil değil |
| S07-14 | Artifact Registry virtual priority + public endpoint bypass kaldırma | Yeni; S06-18 vulnerability remediation değil dependency resolution | Doğru; kullanıcı B |
| S07-15 | Optional dependency fallback readiness; required catalog korunacak | Gecikmeli uygulama; S02-12 ve 22 Eylül açıklamasından 4 gün sonra; optional/required sözleşme ayrımı | Doğru; kullanıcı C |
| S07-16 | Pub/Sub pull subscriber outstanding count/bytes flow control | Yeni; S06-04 ordering değil burst buffering/memory | Doğru; kullanıcı A |
| S07-17 | Spanner timestamp secondary-index hotspot; shard-first ve merge | Karma; S04-01 Bigtable key dağılımını ayrı Spanner index write/read tradeoffuna taşıma | Yanlış; kullanıcı D; anahtar B |
| S07-18 | Gemini-generated Jest rejection test; catch-only assertion false positive | Yeni; S04-10 test oracle değil resolve yolunda assertion yokluğu; deterministic mock zaten doğru | Yanlış; kullanıcı B; anahtar D |
| S07-19 | GKE envFrom startup snapshot; named ConfigMap reference ile rollback | Karma; S03-01 projected file/no-restart yerine startup-only process ve retained config versions | Doğru; kullanıcı A |
| S07-20 | Cloud Storage strong consistency vs CDN cache; versioned asset URLs | Yeni; S06-17 lifecycle veya S05-17 storage-class seçimi değil HTTP freshness | Doğru; kullanıcı C |

S07 Q1–Q10 ilk cevapları 8/10 (%80), 32 dakika; Q10 sonunda ara verildi. Q11 daha sonra D+E (doğru A+E), 2:26; güncel 8/11, çözüm toplamı 34:26 (kesintili). Q12–Q20 henüz çözülmedi. [Kısmi sonuç](results/PCD-S07-attempt-01.md). Q15 yalnız hazırlanmış gecikmeli uygulamadır; probe kalıcılığı henüz doğrulanmadı. S06 ilk 13/20 ve 73 dakika korunur; Q20 yanlış incelemesi bekliyor. Sonraki yeni set S08.

27 Eylül S07: Q12 A doğru; 9/12. Q13 cevap öncesi Türkçe anlam desteği istendi; yanıt yok. Q12 süresi bildirilmedi.


## PCD-S08 — 27 Eylül 2026, öğretici kapsam

Kullanıcının son isteği eski yeni/karma/tekrar kotalarının önündedir. Temel kararları pekiştiren sorular yeni bilgi ölçümü olarak sayılmaz. 50 soru, 16/12/12/10 birincil alan; 44 tek ve 6 çift seçim. Soruların tamamı henüz çözülmedi. İlk sonuç veya kavrayış doğrulaması yoktur. Önceki soru numarası ilişkileri kavramsal geçmiş içindir; cevaplar/senaryolar birebir kopya değildir.

| Soru | Rehber | Karar / belirleyici koşul | Önceki ilişki | Durum |
|---|---|---|---|---|
| S08-01 | 1.1 | Platform seçimi ve işletim yükü: HTTP uygulaması için ihtiyacı karşılayan, yönetimi az platformu seç. | Pekiştirme; S02-01 job seçiminin ters kullanım koşulları, platform karşılaştırması. | Yanlış; kullanıcı B; anahtar D |
| S08-02 | 2.1 | Lokal ADC ile gcloud kimliği: gcloud çalışıyor ama uygulamanın kendi credential kaynağı eksik. | Pekiştirme; S01-11/S06-02, environment precedence yerine temel ADC ayrımı. | Doğru; kullanıcı B |
| S08-03 | 3.2 | Deployment, Pod ve Service: Pod yeniden yaratılınca ayarlar kaybolmasın; istemci her seferinde yeni IP aramasın. | Temel pekiştirme; S07 Q13 sonrası kullanıcının belirttiği GKE hiyerarşi eksikliği. | Doğru; kullanıcı B |
| S08-04 | 4.1 | Cloud SQL bağlantı havuzu: Güvenli bağlanmak yetmiyor; toplam bağlantı sayısı DB kapasitesini aşmasın. | Pekiştirme; bağlantı bütçesi/autoscaling, Cloud SQL ve AlloyDB proxy ayrımı açıklamada. | Doğru; kullanıcı A |
| S08-05 | 1.1 | Session affinity ve paylaşılan durum: Instance değişse bile onaylanmış sepet kaybolmasın. | Karma; S05-01/05 cache tasarımı + session affinity, yeni durability birleşimi. | Doğru; kullanıcı B |
| S08-06 | 2.1 | Gemini Code Assist ve repository bağlamı: AI’ın doğru sürüm ve gerçek interface’e göre kod önermesini sağla. | Pekiştirme; S05-10, bilinçli AI context temel tekrarı. | Doğru; kullanıcı B |
| S08-07 | 3.2 | Startup, readiness ve liveness: Geç açılmayı hata sanma; geçici olarak hizmet veremeyen Pod’a yeni trafik gönderme. | Pekiştirme; S02-12 ve kullanıcının açıkça belirttiği probe eksikliği. | Doğru; kullanıcı A+E |
| S08-08 | 1.2 | Çalışan erişimi ve müşteri kimliği: Çalışana iç uygulama kapısı, müşteriye ürün içinde giriş sistemi gerekiyor. | Yeni ölçüm; S07-05 JWT detayından daha temel ürün/kimlik amacı ayrımı. | Doğru; kullanıcı C |
| S08-09 | 4.1 | Pub/Sub fan-out ve iş paylaşımı: İki farklı uygulama her event’i alsın; her uygulamanın kendi worker’ları işi paylaşsın. | Pekiştirme; publish/subscribe ile competing workers temel farkı. | Doğru; kullanıcı A |
| S08-10 | 3.1 | Cloud Run source deployment: Desteklenen uygulamayı Dockerfile yazmadan source’tan Cloud Run’a gönder. | Pekiştirme; Cloud Run source/image ayrımını temel seviyede uygulama. | Doğru; kullanıcı C |
| S08-11 | 2.1 | Workstations, Cloud Shell ve lokal IDE: Ortak araçları merkezi yönet; geliştiricinin dosyalarını kalıcı tut. | Pekiştirme; S05-02/06, temel ortam/persistence eşleştirmesi. | Doğru; kullanıcı C |
| S08-12 | 1.1 | Zonal HA ve regional disaster recovery: Tek bölge tamamen giderse veritabanı ve uygulama nasıl geri gelir? | Karma; S04-05 zonal HA ile S07-09 replica lag, yeni bölgesel recovery kararı. | Doğru; kullanıcı A |
| S08-13 | 3.2 | HPA ve cluster autoscaler: HPA Pod istiyor ama onları çalıştıracak node kapasitesi yok. | Pekiştirme; önceki GKE autoscaling ayrımlarını sadeleştirme. | Doğru; kullanıcı C |
| S08-14 | 4.1 | Firestore transaction ve tekrar: Son ürünü iki kişiye satma; transaction tekrarında iki e-posta üretme. | Pekiştirme; S04 transaction/retry ve dış yan etki ayrımı. | Doğru; kullanıcı D |
| S08-15 | 1.2 | GKE uygulama kimliği ve ağ izni: Pod hangi kimlikle konuşacak ve o kimlik hangi bucket’ı okuyabilir? | Pekiştirme; S03-04 ve son hiyerarşi açıklaması; cross-cluster identity sameness ölçülmüyor. | Doğru; kullanıcı A+D |
| S08-16 | 2.1 | Emulator ile production doğrulaması sınırı: Lokal veri davranışını hızlı test et; gerçek cloud ayarlarını ayrıca doğrula. | Pekiştirme; S04-06, emulator sınırını öğretici biçimde ölçer. | Doğru; kullanıcı D |
| S08-17 | 3.1 | Cloud Run servis çağrısı: Orders çağıran, billing alıcı. İzin alıcı üzerinde çağırana verilir; token alıcıya hitap eder. | Bilinçli pekiştirme; S01/R01 audience konusu, önceki anlık doğru kavrayış kalıcılık ölçümü değildir. | Doğru; kullanıcı A+C |
| S08-18 | 1.3 | Firestore büyüyen listeyi modelleme: Sürekli büyüyen mesaj geçmişini nasıl saklayıp sayfalarsın? | Yeni ölçüm; S06 index exemption veya transaction yerine document/subcollection modelleme. | Doğru; kullanıcı D |
| S08-19 | 4.1 | Cloud Storage resumable upload: Büyük dosyada bağlantı kopunca baştan başlama; sunucunun aldığı yerden sürdür. | Temel storage API uygulaması; interrupted transfer kararı. | Doğru; kullanıcı B |
| S08-20 | 2.2 | Build once ve aynı artifactı terfi ettirme: Test ettiğin image ile production’a giden image aynı olsun. | Pekiştirme; S04-03, farklı environment config ile temel artifact promotion. | Doğru; kullanıcı B |
| S08-21 | 3.2 | Requests ve limits: Bir task’ın gerçekten ihtiyaç duyduğu bellek, container limitini aşıyor. | Temel pekiştirme; GKE resource gereksinimi, ölçülmüş ihtiyaçtan karar. | Yanlış; kullanıcı A; anahtar C |
| S08-22 | 1.2 | Secret saklama, rotation ve KMS rolü: Parolayı image’dan çıkar; yalnız gereken uygulama okusun ve kontrollü değişsin. | Pekiştirme; S01-01/S05-11/S06-13, ayrı rotation kavramlarını temel düzeyde birleştirir. | Doğru; kullanıcı B |
| S08-23 | 2.2 | Multi-stage image ve build cache: Build araçları final image’da kalmasın; değişmeyen bağımlılık adımı tekrar kullanılabilsin. | Karma; S05-18 cache düzeni + runtime-only multi-stage kararı. | Doğru; kullanıcı C |
| S08-24 | 4.2 | API enablement ve service account yetkisi: API açık olmalı; uygulama kimliği de istediği işlemi yapabilmeli. | Bilinçli temel pekiştirme; API/ADC/IAM üç ayrı sorumluluk. | Doğru; kullanıcı B+D |
| S08-25 | 1.3 | Spanner ve ilişkisel veri ihtiyacı: Yatay büyüyen, bölgeler arası ilişkisel transaction sistemi seç. | Pekiştirme; S01-14, ürün seçiminin gerekçesiyle temel tekrar. | Doğru; kullanıcı D |
| S08-26 | 3.1 | Eventarc alıcısı ve teslimat: Event geldiğini doğru anla; iş kalıcı kabul edilmeden tamam dememe ve tekrarı güvenli yönetme. | Pekiştirme; event formatı + güvenilir kabul, önceki idempotency konuları bilinçli tekrar. | Doğru; kullanıcı B |
| S08-27 | 2.1 | MCP tool erişimi ve least privilege: AI’ın ihtiyacı kadar tool ve gerçek yetki ver. | Pekiştirme; S06-06, kapsamı daraltılmış öğretici MCP sorusu. | Doğru; kullanıcı B |
| S08-28 | 1.1 | Scheduler, Workflows, Tasks görev ayrımı: Her sabah başlayan, sonuçlara göre sırayla ilerleyen süreç kur. | Karma; S01-15 orchestration üzerine recurring start ve fan-out/dispatch ayrımı. | Doğru; kullanıcı C |
| S08-29 | 4.2 | Pagination, field selection ve cache: Tüm sonucu al ama gereksiz alanı ve gereksiz tekrar çağrısını azalt. | Bilinçli pekiştirme; S07-08 field selection/pagination ve önceki stale kavramı. | Doğru; kullanıcı B |
| S08-30 | 3.1 | Cloud Run Jobs tasks ve parallelism: Toplam 12 parça iş var; aynı anda en çok 3’ü çalışsın. | Pekiştirme; S07-11 sonrası task/parallelism temelini ayrı öğretme. | Doğru; kullanıcı A |
| S08-31 | 1.2 | Retention, lifecycle ve organization policy: Silme koruması, sonradan temizlik ve public erişim yasağını birlikte kur. | Pekiştirme; S04-17/S06-17 üzerine üç kontrolün rolleri; öğretici tekrar, yeni bilgi sayılmaz. | Doğru; kullanıcı C |
| S08-32 | 2.2 | Cloud Build ortak dosya ve step sırası: Çıktı sonraki step’lere ulaşsın; iki kontrol bitmeden paketleme başlamasın. | Pekiştirme; S01-03 + S04-02, bilinçli iki temel build mekanizması birleşimi. | Doğru; kullanıcı C+E |
| S08-33 | 3.2 | Rolling update ve PDB ayrımı: Uygulama sürümünü değiştirirken üç hazır replica kalsın; bir yenisine yer var. | Pekiştirme; S05-15 sonrası bakım/rollout karışıklığı, termination saniye hesabı yok. | Doğru; kullanıcı B |
| S08-34 | 4.2 | Vision API asynchronous batch: Kullanıcı beklemiyor; çok görseli toplu ve asenkron işle, başarısız alt kümeyi ayır. | Pekiştirme; S05/S06 API throughput, numeric quota ezberi olmadan Vision uygulaması. | Doğru; kullanıcı A |
| S08-35 | 2.2 | Provenance neyi kanıtlar?: Bu image hangi build’den çıktı, doğrulanabilir şekilde göster. | Pekiştirme; S06-14, flag ezberi yerine provenance amacı. | Yanlış; kullanıcı D; anahtar A |
| S08-36 | 1.3 | Bigtable row key ve erişim paterni: Yazmaları dağıt, aynı cihazın zaman aralığını kolay oku. | Pekiştirme; S04-01 ile aynı temel karar, öğretim amacıyla açık tekrar. | Yanlış; kullanıcı A; anahtar C |
| S08-37 | 3.2 | GKE NetworkPolicy ve IAM sınırı: Payments’a ağdan yalnız frontend ulaşsın; kimlik kontrolü yine devam etsin. | Temel güvenli GKE deployment; S03 WIF/IAM’den ayrı network katmanı, açık pekiştirme. | Yanlış; kullanıcı C; anahtar D |
| S08-38 | 1.3 | Geçici object erişimi ve signed URL: Google hesabı olmayan müşteriye yalnız bir dosya için kısa erişim ver. | Pekiştirme; S01-04/S06-05, bilerek temel yetki kapsamı tekrarı. | Doğru; kullanıcı D |
| S08-39 | 2.3 | AI unit test ve doğru oracle: Test hatalı kodu onaylamasın; iş kuralını gerçekten sınasın. | Pekiştirme; S04-10, kullanıcı isteğiyle temel test mantığına dönüş. | Doğru; kullanıcı A |
| S08-40 | 4.2 | Retry, backoff ve deadline: Geçici arızada kontrollü tekrar; yanlış istekte parametreyi düzelt. | Pekiştirme; API tüketiminde temel transient/permanent ayrımı, örnek kaynağın service-specific kuralları genellenmez. | Doğru; kullanıcı A |
| S08-41 | 1.1 | Global load balancer ve API yönetimi ayrımı: İki bölge için müşteriye tek HTTPS giriş noktası sağla. | Yeni ölçüm; S02 ingress sorusundan farklı global front-end ihtiyacı. | Doğru; kullanıcı C |
| S08-42 | 2.1 | Cloud Assist ile kanıta dayalı inceleme: AI incelemeyi hızlandırsın; önerinin kanıtını yine kontrol et. | Karma; S05-14 ürün rolü + 4.3 AI-assisted troubleshooting uygulaması. | Doğru; kullanıcı D |
| S08-43 | 3.1 | Canary, rollback ve uyumlu schema: Yeni kod denenirken eski kod hâlâ çalışabilsin; trafik geri dönünce veritabanı yüzünden kırılmasın. | Bilinçli pekiştirme; S05-03, kullanıcının additive schema ve rollback soruları. | Doğru; kullanıcı D |
| S08-44 | 4.3 | Metrics, logs, traces ve Error Reporting: Genel grafiği görüyorsun; şimdi tek isteğin nerede yavaşladığını ve tekrar eden hatayı bul. | Pekiştirme; S06/S07 observability ayrımları, temel araç amacına odaklı. | Doğru; kullanıcı B+E |
| S08-45 | 1.2 | Statik image taraması ve çalışan web uygulaması: Image içindeki paketlerin yanında çalışan web davranışını da kontrol et. | Yeni ölçüm; S06-18 paket düzeltme yerine runtime scanning kapsamı. | Doğru; kullanıcı A |
| S08-46 | 2.3 | Integration test izolasyonu ve sonuç koruma: Build’ler birbirinin verisini bozmasın; cleanup test hatasını gizlemesin. | Pekiştirme; S06-10, kısa temel isolation ve release-gate açıklaması. | Doğru; kullanıcı D |
| S08-47 | 1.2 | Artifact onayı ve deployment enforcement: Pipeline dışından gelen deploy da onay kuralına uysun. | Pekiştirme; S04-14, bilinçli temel release-gate tekrarı. | Doğru; kullanıcı A |
| S08-48 | 4.2 | Generative AI API çıktısını uygulamaya bağlama: AI çıktısı parse edilebilsin ama doğru formatı doğru karar sanma. | GenAI API uygulama temeli; Gemini Code Assist ile uygulamanın model API çağrısı farklı sorumluluklar. | Doğru; kullanıcı C |
| S08-49 | 1.3 | BigQuery batch analytics ve ham veri: Ham dosya kalsın; geçmiş veri SQL ile analiz edilsin; günlük yükleme yeterli. | Yeni ölçüm; S06 pending-stream atomicity yerine temel batch analytics mimarisi. | Doğru; kullanıcı D |
| S08-50 | 3.1 | Apigee API versioning ve güvenlik: Eski mobil uygulamayı kırmadan v2 sun; iki sürümde de güvenlik devam etsin. | Pekiştirme; S06 API versioning ve S07 API management konularını temel karar düzeyine çekme. | Doğru; kullanıcı A |

S08 öğrenci dosyası ve kaynaklı anahtar ayrı. Kapsam tablosu doğrudan soru ile yalnız notta anlatılan ayrıntıları ayırır. Sonraki yeni set S09. S07 Q12 A doğru sonrası 9/12; Q13 D rehberli, ilk seçim yok. S06 Q20 incelemesi hâlâ bekliyor.

27 Eylül son S07 sonucu: Q14–Q20 5/7; toplam Q13 hariç 14/19 (%73,7). Q13 rehberli, ilk cevap yok. Son bölüm süresi bildirilmedi. Q17/Q18 ayrıntılı inceleme bekliyor; S08 hâlâ çözülmedi.

27 Eylül S08 ilk Q1–Q20: 19/20, 45 dakika; yalnız Q1 B→D. E/K/T veya gerekçe yok. Q21–Q50 bekliyor; bağımsız kavrayış veya sınav eşdeğerliği iddiası yok. [Sonuç](results/PCD-S08-attempt-01.md).

S08 Q21–Q40 ilk sonuç: 16/20, 60 dakika; Q21/35/36/37 yanlış. Q1–Q40 toplam 35/40 (%87,5), bölümlerin süre toplamı 105 dakika. Q41–Q50 cevap yok. Yeni yanlışlar henüz ayrıntılı incelenmedi.

S08 tamamlandı: son on 10/10, 14 dakika; ilk cevap toplamı 45/50 (%90), 119 dakika bölümlerin toplamı. İlk yanlışlar Q1/21/35/36/37 korunur. Bölümler arasında rehberli açıklama var; kesintisiz deneme değil. Sonraki yeni set S09.


## PCD-S09 — 28 Eylül 2026

[Sorular](PCD-S09.md) · [Ayrı Türkçe anahtar](../answers/scenarios/PCD-S09.md) · [Önce yapılan son ay araştırması](PCD-RESEARCH-2026-09-28.md).

50 soru; 44 tek/6 çift seçim; dört alan 16/12/12/10, 11 alt başlık. 84–103 kelimelik gövdeler. Yakın şık ve çok koşullu karar hedefi; sample/gerçek sınavla kalibrasyon yok. S08 ilk 45/50, 119 dakika ve eski ilk puanlar korunur. Q20/Q31 temel pekiştirme; karma sorular yeni temel konu diye sayılmaz. S09 tamamlandı: ilk gönderilen 37/50, iki bölüm toplamı 128 dakika. Q9 aktarım beyanıyla 38/50 ayrı; Q19 belirsizlik notu korunur. Tüm yanlışlar açıklandı; bağımsız kalıcılık kontrolü yok. [Sonuç](results/PCD-S09-attempt-01.md).

| ID | Rehber | Ölçülen karar | Tür / önceki ilişki | Durum |
|---|---|---|---|---|
| S09-01 | 1.1 | Optional dependency: fallback + circuit breaker | Karma; S07-15 optional dependency, burada probe değil çağrı izolasyonu. | İlk doğru |
| S09-02 | 2.1 | Local ADC impersonation ile runtime yetkisini yeniden üretme | Karma; S06-02 ADC precedence ve S08-02 temel ADC üzerine farklı kimlikle test. | İlk yanlış; açıklandı, bağımsız kontrol yok |
| S09-03 | 3.1 | Cloud Tasks worker acknowledgment işin sonuna bağlanmalı | Karma; S08-26 durable acceptance, burada ikinci queue yok ve worker ack tamamlanma demek. | İlk yanlış; açıklandı, bağımsız kontrol yok |
| S09-04 | 4.1 | Failover sonrası connection yenileme + transaction bütününü retry | Karma; S04-05 HA ve S08-04 pool üzerine failure recovery. | İlk doğru |
| S09-05 | 1.3 | Firestore aynı timestamp için tie-breaker cursor | Yeni ölçüm; S08-18 veri modeli ve S05-08 pagination ile ilişkili, eşitlik sınırı yeni. | İlk doğru |
| S09-06 | 2.2 | PR build trust boundary + ayrı release identity | Yeni ölçüm; S03-12 build/runtime kimliği, burada source trust boundary. | İlk doğru |
| S09-07 | 3.2 | HPA container-specific CPU metric | Karma; S05-07 metrik seçimi, yeni sidecar dilution koşulu. | İlk doğru |
| S09-08 | 4.2 | Storage conditional delete ile yeni generation koruma | Karma; S04-08 create-only ve S07-04 metadata yerine delete race. | İlk doğru |
| S09-09 | 1.2 | Cross-project secret: denied runtime principal ve resource scope | Karma; S01-01, S06-03 ve R01-01 rol/kimlik ayrımlarını cross-project bağlamında birleştirir. | İlk B yanlış; A aktarım beyanı ayrı |
| S09-10 | 2.3 | Emulator server SDK success Rules kanıtı değildir | Yeni ölçüm; S04-06/S08-16 emulator sınırı, bu kez rule bypass nedeniyle yanlış test kanıtı. | İlk yanlış; açıklandı, bağımsız kontrol yok |
| S09-11 | 1.1 | Spanner write latency: application/leader locality | Karma; S08-25 ürün seçimi üzerine leader locality, S05-09 timestamp read kararı değil. | İlk doğru |
| S09-12 | 3.1 | Config-only revision, aynı digest ve no-traffic validation | Karma; rehberli revision bileşenleri + S08-20/43 artifact ve traffic. | İlk yanlış; açıklandı, bağımsız kontrol yok |
| S09-13 | 2.1 | Cloud Code/kubectl context project seçiminden ayrı | Yeni ölçüm; S08-11 ortam ürün seçiminden farklı context güvenliği. | İlk doğru |
| S09-14 | 4.3 | Canary aggregate ortalamanın gizlediği tail latency | Karma; S08-44 metrics/trace, yeni canary aggregation teşhisi. | İlk doğru |
| S09-15 | 1.3 | Bigtable hot customer: bounded salting tradeoff | Karma; S08-36 dengeli cihaz varsayımı tersine çevrildi; S07-17 shard/index ilişkisi var. Yeni temel hash kavramı diye sayılmaz. | İlk doğru |
| S09-16 | 3.2 | Service port/targetPort farklılığı | Karma; S02-03 selector sorusundan farklı doğru selector yanlış port. | İlk doğru |
| S09-17 | 2.2 | Build origin ve test kanıtı aynı artifacta bağlanmalı | Karma; S08-35 provenance açıklaması sonrası anlık birleşik uygulama; gecikmeli başarı sayılmayacak. | İlk doğru |
| S09-18 | 1.2 | WIF authenticated issuer yetmez; repo/workflow boundary | Karma; S04-13 repository WIF sınırına mevcut aşırı geniş production trust teşhisi. | İlk doğru |
| S09-19 | 4.1 | Dead-letter forwarding IAM + inceleme subscription | Yeni ölçüm; S07-16 flow control ve S06-04 ordering’den farklı failure isolation. | İlk B; anahtarda yanlış, soru belirsizliği var |
| S09-20 | 3.1 | No-traffic candidate tag routing | Bilinçli pekiştirme; S03-02 ve rehberli R10-04. Yeni kapsam veya yeni teknik karar sayılmaz. | İlk doğru |
| S09-21 | 1.1 | Uncertain task creation: stable name + delivery idempotency | Karma; S06-01 Tasks dispatch yerine producer creation uncertainty. | İlk doğru |
| S09-22 | 2.3 | Consumer compatibility release test | Karma; S08-50 API versioning ve S08-39 independent oracle, yeni consumer test gate. | İlk doğru |
| S09-23 | 3.2 | PDB mevcut unhealthy replica ile eviction budget | Karma; S03-07 PDB, burada arıza sonrası mevcut eviction bütçesi. | İlk doğru |
| S09-24 | 4.2 | Pagination token query context ile bağlı | Yeni ölçüm; S07-08 missing token field değil token-query uyumu. | İlk doğru |
| S09-25 | 1.2 | Secret rotation rollback dependency lifecycle | Karma; S02-13 ve S08-22 rotation temelinden dependency retirement penceresine. | İlk doğru |
| S09-26 | 2.2 | Reproducible inputs + kontrollü security updates | Karma; S05-18 cache ve S08-20 promotion üzerine build input yönetimi. | İlk yanlış; açıklandı, bağımsız kontrol yok |
| S09-27 | 3.1 | Interactive acceptance + uzun finite Cloud Run job | Karma; S02-01 job ve S08-01 service ayrımı; yeni asenkron kontrol/çalıştırma birleşimi. | İlk doğru |
| S09-28 | 1.3 | Shared managed NFS vs object/mount/pod-local | Karma uygulama; 27 Eylül Filestore/Storage sözlü açıklaması, ilk senaryo ölçümü. | İlk doğru |
| S09-29 | 2.1 | Workstations config rollout aktif session restart | Karma; S05-06 persistence yerine yönetilen toolchain update’ın aktif session’a alınması. | İlk yanlış; açıklandı, bağımsız kontrol yok |
| S09-30 | 4.3 | Structured severity ve error grouping context | Karma; S08-44 genel araç seçimi yerine structured field teşhisi. | İlk doğru |
| S09-31 | 3.2 | Open listener ile semantic readiness ayrımı | Bilinçli pekiştirme; S02-04 startup ve S02-12/S08-07 probe temeli. Yeni kapsam sayılmaz. | İlk doğru |
| S09-32 | 1.1 | Farklı freshness contract: metadata cache ve auth | Karma; S05-01 cache/tenant üzerine authorization freshness, yeni correctness boundary. | İlk doğru |
| S09-33 | 2.3 | Performance test confound: cold vs warm cohorts | Yeni ölçüm; S01-12 cold start çözümü değil performans deneyinin doğruluğu. | İlk doğru |
| S09-34 | 4.1 | Exactly-once delivery vs publish/business duplication | Karma; S01-10 dedup üzerine service guarantee kapsamı. Yeni idempotency temeli sayılmaz. | İlk doğru |
| S09-35 | 1.2 | Binary Authorization iki bağımsız attestation AND | Karma; S08-47 admission temeline iki ayrı approval mantığı. | İlk yanlış; açıklandı, bağımsız kontrol yok |
| S09-36 | 3.1 | Eventarc source-specific data schema ve adapter test | Karma; S03-14 Pub/Sub adapter’ın ters kaynak koşulu; yeni temel CloudEvents kapsamı değil. | İlk doğru |
| S09-37 | 2.2 | Shared workspace concurrent write collision | Karma; S08-32 workspace+DAG yerine doğru DAG altında write collision. | İlk doğru |
| S09-38 | 1.3 | Selective open-ended object hold | Yeni ölçüm; S08-31 bucket retention yerine object-level hold. Hukuki tavsiye değil ürün davranışı senaryosu. | İlk yanlış; açıklandı, bağımsız kontrol yok |
| S09-39 | 4.2 | Quota project serviceusage.services.use ayrı access katmanı | Yeni ölçüm; S08-24 enablement+IAM üzerine quota consumer ayrımı. | İlk doğru |
| S09-40 | 3.2 | Missing ConfigMap key vs startup health | Karma; S07-19 mutable config/rollback değil config-start failure teşhisi. | İlk doğru |
| S09-41 | 1.1 | Cloud Armor direct URL bypass ingress boundary | Karma; S02-10 ingress temelinin Cloud Armor bypass teşhisi. Yeni ingress kavramı sayılmaz. | İlk doğru |
| S09-42 | 2.1 | AI retrieved context güvenilir emir değildir | Karma; S08-27 least privilege, burada returned content instruction boundary. | İlk doğru |
| S09-43 | 3.1 | Per-request RAM concurrency kapasite planlama | Karma; S01-07 shared-state veya S08-21 tek task OOM değil eşzamanlı memory toplamı. | İlk doğru |
| S09-44 | 4.3 | End-to-end async latency: backlog waiting vs handler span | Yeni ölçüm; S07-12 CPU attribution yerine queue wait observability. | İlk doğru |
| S09-45 | 1.2 | KMS key retirement: live migration tamam ama backup bağımlılığı sürüyor | Karma; S06-13 KMS rotation/migration. Burada live migration tamam; kararı değiştiren kalan backup bağımlılığı. Yeni temel konu sayılmaz. | İlk yanlış; açıklandı, bağımsız kontrol yok |
| S09-46 | 3.2 | HPA request denominator ve desired replicas hesabı | Karma; S02-15 CPU requests ve HPA, yeni sayısal uygulama. | İlk doğru |
| S09-47 | 1.1 | Workflows saga compensation ve idempotency | Karma; S01-15 orchestration ve S04-16 external effects, yeni compensation planı. | İlk doğru |
| S09-48 | 1.3 | Firestore collection group cross-parent query scope | Karma; 27 Eylül sözlü Firestore collection group/index açıklaması; S08-18 subcollection üzerine query scope. | İlk doğru |
| S09-49 | 4.2 | GenAI optional response bounded retry/fallback | Karma; S08-40 retry + S08-48 uygulama GenAI tüketimi; yeni ürün kotası ezberi yok. | İlk yanlış; açıklandı, bağımsız kontrol yok |
| S09-50 | 2.3 | AI test: commit-before-ack failure injection invariant | Karma; S08-39 AI oracle + önceki dedup, yeni failure-injection kanıtı. | İlk yanlış; açıklandı, bağımsız kontrol yok |


## PCD-S10 — 28 Eylül 2026 hazırlık

[Sorular](PCD-S10.md) · [Ayrı Türkçe anahtar](../answers/scenarios/PCD-S10.md). Kullanıcının son düzeltmesiyle **20 soru / 45 dakika**; 29 Eylül iş çıkışı çözüm planı, henüz cevap yok. 18 tek + Q6/Q18 çift seçim; dört alan 6/5/5/4, 11 alt başlık. Dengeli uygulama ve yakın seçenekler; gerçek sınava göre kalibrasyon yok. S09 yanlışlarının anlık kopyası hazırlanmadı. Eski temel kararlar yeni konu diye sayılmaz.

| ID | Rehber | Ölçülen karar | Tür / önceki ilişki | Durum |
|---|---|---|---|---|
| S10-01 | 1.1 | Global edge caching | Karma; S07-20 sürümlü URL ile invalidation ölçüyordu. Burada URL doğru; karar cache’in coğrafi konumu. | Henüz çözülmedi |
| S10-02 | 2.1 | Cloud Shell environment fit | Karma; S05-02/S08-11 Workstations ihtiyacından farklı olarak kısa standart shell ihtiyacı; yeni temel ürün sayılmaz. | Henüz çözülmedi |
| S10-03 | 3.2 | Image pull diagnosis | Karma; S09-40 ConfigMap nedeniyle başlamama idi. Burada event kanıtı image referansına işaret ediyor. | Henüz çözülmedi |
| S10-04 | 4.1 | Pub/Sub acknowledgment lease | Karma; S07-16 flow control yerine aynı kapasite altında mesaj başına ack lease süresi. | Henüz çözülmedi |
| S10-05 | 1.2 | Parameterized SQL | Yeni ölçüm; önceki bağlantı/IAM senaryolarından farklı uygulama query injection sınırı. | Henüz çözülmedi |
| S10-06 | 2.2 | Repository-scoped artifact access | Karma; S03-12 build/runtime kimlik ayrımı üzerine repository kapsamı. Audit hesabı runtime image-pull agent değildir. | Henüz çözülmedi |
| S10-07 | 3.1 | Reuse safe clients in functions | Karma; önceki pool/shared state ilkelerinin function initialization yaşam döngüsüne uygulanması. | Henüz çözülmedi |
| S10-08 | 1.3 | Managed PostgreSQL workload fit | Karma; S08-25 global Spanner gereksiniminin aksine mevcut bölgesel PostgreSQL uyumu; temel ürün seçimi pekişir. | Henüz çözülmedi |
| S10-09 | 4.2 | Long-running operation lifecycle | Yeni ölçüm; S05-04 asenkron API seçimi üzerine kalıcı operation kimliği ve client polling yaşam süresi. | Henüz çözülmedi |
| S10-10 | 2.3 | Deterministic time-based unit tests | Karma; S08-39 AI test oracle üzerine zaman bağımlılığını kontrol etme. S09-50 failure injection tekrarı değil. | Henüz çözülmedi |
| S10-11 | 1.1 | Bidirectional gRPC API | Karma; S06-15 h2c yapılandırmasından farklı API streaming türü seçimi. | Henüz çözülmedi |
| S10-12 | 3.2 | HPA binding maximum | Karma; önceki metrik/request/stabilization sorularından farklı bağlayıcı maxReplicas sınırı. | Henüz çözülmedi |
| S10-13 | 1.2 | Verify end-user identity | Karma; S08-08 Identity Platform ürün seçimi üzerine backend token doğrulama; S07 signed identity ilkesiyle ilişkili. | Henüz çözülmedi |
| S10-14 | 2.1 | Cloud Code inner development loop | Karma; S09-13 context güvenliği zaten sağlanmış; bu kez IDE inner-loop araç seçimi. | Henüz çözülmedi |
| S10-15 | 4.3 | Log sink exclusions | Karma; S09-30 severity parse doğru varsayılıyor. Yeni karar sink exclusion aşamasında. | Henüz çözülmedi |
| S10-16 | 1.3 | Atomic Firestore write batch | Karma; S08-14 read-dependent transaction koşulunun tersine önceden bilinen atomik yazımlar. | Henüz çözülmedi |
| S10-17 | 2.2 | Monorepo trigger dependencies | Yeni ölçüm; build DAG/cache yerine monorepo trigger kaynak bağımlılığı ve file filter kapsamı. | Henüz çözülmedi |
| S10-18 | 3.1 | Cloud Run ingress container contract | Bilinçli pekiştirme; S03-06 listen address temeline açık PORT uyumsuzluğu eklenir. Yeni temel kapsam sayılmaz. | Henüz çözülmedi |
| S10-19 | 3.1 | Cloud Run job failure signal | Karma; önceki job/service seçimi üzerine task exit sonucu. S09-03 service ack protokolünden farklı. | Henüz çözülmedi |
| S10-20 | 4.3 | Request-weighted success SLI | Yeni ölçüm; S09-14 cohort görünürlüğünden farklı, açık tanımlanmış global request SLI pay/payda hesabı. | Henüz çözülmedi |


## PCD-S11 — 1 Ekim 2026

Kullanıcı S10’dan biraz daha zor, exam guide ağırlıklarıyla 50 soru istedi. 16/12/12/10 ana alan; 47 tek + Q6/Q19/Q21 çift seçim; 120 dakika kişisel hedef. Uzun İngilizce ve ayrı Türkçe kaynaklı anahtar. Yeni temel kapsam yerine karma uygulama ve bilinçli pekiştirmeler açıkça kaydedilir; yalnız soru hazırlandı, çözüm/kalıcılık yok.

[Sorular](PCD-S11.md) · [Anahtar](../answers/scenarios/PCD-S11.md)

| ID | Rehber | Karar | Tür / geçmiş / farklı koşul | Durum |
|---|---|---|---|---|
| S11-01 | 1.1 | Cache stampede; enough capacity for one refresh | Karma; S05-01 cache-aside üzerine eşzamanlı expiry ve refresher crash koşulu. | Henüz çözülmedi |
| S11-02 | 2.1 | Test endpoint isolation; requests reaching localhost | Karma; S04-06/S08-16 ters yön: emulator testi çalışır, hosted diagnostic yanlışlıkla emulator’a gider. | Henüz çözülmedi |
| S11-03 | 3.1 | Connection budget during overlap; twelve instances of the old revision and twelve of the new | Karma; S08-04 pool bütçesi; yeni iki revision overlap hesabı. | Henüz çözülmedi |
| S11-04 | 4.1 | Consistent ranged download; must never silently combine versions | Karma; S03-05 generation-specific read; yeni çok parçalı transfer tutarlılığı. | Henüz çözülmedi |
| S11-05 | 1.1 | Affinity and experiment assignment; across devices and across replacement | Karma; S08-05 durability değil kullanıcı bazlı deney üyeliği; affinity sınırı bilinçli tekrar. | Henüz çözülmedi |
| S11-06 | 2.2 | Build ordering and failure semantics; correctly waits ... allowFailure: true | Karma; S04-02 doğru DAG varsayılır, S01-13 failure gate ile birleşir. | Henüz çözülmedi |
| S11-07 | 3.2 | Surge capacity bottleneck; four available replicas throughout | Karma; S04-07 rollout ayarı doğru, S03-13 scheduler capacity birleşimi. | Henüz çözülmedi |
| S11-08 | 1.3 | Zonal HA with explicit regional limit; losing a zone ... separately accepted ... regional outage | Bilinçli pekiştirme; S04-05/S08-12 scope ayrımı, regional DR sorusunun ters gereksinimi. | Henüz çözülmedi |
| S11-09 | 4.1 | Ordering-key blocked work; order within each customer | Yeni ölçüm; S10-04 lease değil ordering key’e bağlı failure ilerlemesi. | Henüz çözülmedi |
| S11-10 | 2.3 | Property test detects implementation bug; same helper used by the production function | Karma; S08-39 oracle üzerine helper kaynaklı circularity ve property/invariant uygulaması; yeni Google ürün bilgisi değil. | Henüz çözülmedi |
| S11-11 | 1.1 | Quota plus burst protection; below that daily quota ... short burst | Karma; S04-09 ters durum: quota mevcut, burst koruması eksik. | Henüz çözülmedi |
| S11-12 | 3.1 | Secret access at instance startup; newly started instances fail ... permission failure | Karma; S09-09 principal teşhisi + S05-11 startup yaşam döngüsü; yeni startup failure bağlamı. | Henüz çözülmedi |
| S11-13 | 1.2 | Credential rollout sequencing; rollback ... until the observation period ends | Bilinçli pekiştirme; S09-25 credential overlap, yeni temel kapsam/kalıcılık iddiası yok. | Henüz çözülmedi |
| S11-14 | 2.1 | Workstations mounted home; attaches persistent home disks | Karma; S09-29 restart sorusu değil build-time home masking; ürün detayının yeni ölçümü. | Henüz çözülmedi |
| S11-15 | 4.2 | Error classification before retry; invalid field selector ... separate valid requests ... 503 | Bilinçli pekiştirme; S08-40 temel sınıflama, somut two-error incident; yeni retry konu iddiası yok. | Henüz çözülmedi |
| S11-16 | 3.2 | Probe semantics during dependency failure; restarting ... does not accelerate recovery | Bilinçli pekiştirme; S02-12, DB failover kanıtı eklenmiş; yeni temel probe konusu değil. | Henüz çözülmedi |
| S11-17 | 1.3 | Separate analytical scans; Reports may be refreshed once a day | Karma; S08-49 storage analytics üzerine primary contention ve uygulama uyumu; eski temel ürün seçimi sayılmaz. | Henüz çözülmedi |
| S11-18 | 2.2 | Provenance is not a vulnerability waiver; requires ... no unresolved vulnerability | Karma; S09-17 evidence/digest doğru varsayılır, S06-18 vulnerability repair ile birleşir. | Henüz çözülmedi |
| S11-19 | 3.1 | Event delivery and runtime data identity; before the handler runs ... service runs as processing-runtime | Karma; S01-06 invoker + S09-09 runtime resource identity; iki boundary doğrudan ölçülür. | Henüz çözülmedi |
| S11-20 | 4.3 | Async trace propagation; no trace context ... message attributes | Karma; S04-12 propagation + S09-44 async wait, yeni messaging boundary. | Henüz çözülmedi |
| S11-21 | 1.2 | NetworkPolicy DNS and backend access; Connecting ... IP succeeds ... blocked DNS queries | Karma; S03-10 ingress/egress üzerine DNS dependency; plugin/topology varsayımı açık. | Henüz çözülmedi |
| S11-22 | 2.2 | Dockerfile overrides expected buildpack flow; source root contains an old Dockerfile | Karma; S08-10 buildpack seçimi, beklenmedik Dockerfile önceliği yeni ölçüm. | Henüz çözülmedi |
| S11-23 | 3.2 | HPA cannot schedule nodes; node pool has reached its current maximum | Bilinçli pekiştirme; S08-13 node/Pod scaling; bu kez açık node maximum kanıtı; S10-12 ters bağlayıcı limit. | Henüz çözülmedi |
| S11-24 | 1.3 | Signed URL identity guarantee; every download ... anyone who merely receives a forwarded link | Karma; S01-04/S08-38 signed URL uygunluğu ters gereksinimle sınanır; yeni identity garantisi ayrımı. | Henüz çözülmedi |
| S11-25 | 4.1 | Firestore read-dependent retry; reuses that value in every callback attempt | Karma; S01-09 transaction ve S04-16 retry; dış side-effect değil read placement ölçülür. | Henüz çözülmedi |
| S11-26 | 2.1 | AI context versus tool permissions; respects the current dependency contract | Bilinçli pekiştirme; S05-10/S08-06 context mühendisliği; yeni AI ürün özelliği ölçümü değil. | Henüz çözülmedi |
| S11-27 | 3.1 | Rollback and pinned tagged endpoint; directly to the tagged revision URL | Karma; S09-20 tag temelinden yeni rollback sonrası istemci hedefi teşhisi. | Henüz çözülmedi |
| S11-28 | 1.1 | Fan-out plus controlled dispatch; independently ... controlled ... concurrent requests | Karma; S04-04 fan-out + S01-05 Tasks dispatch; yeni ürün değil birleşik requirement. | Henüz çözülmedi |
| S11-29 | 4.2 | Partial response preserves continuation; accidentally omits nextPageToken | Karma; S08-29 fields/pagination üzerine continuation field kaybı; yeni teşhis koşulu. | Henüz çözülmedi |
| S11-30 | 2.3 | Prove runtime IAM in integration test; broad user ADC ... runtime service account | Karma; S08-16 emulator sınırı + S09-02 identity; yeni test execution evidence, Rules testi değil. | Henüz çözülmedi |
| S11-31 | 1.2 | Recover disabled KMS version; disabled ... has not been destroyed | Karma; S09-45 backup retirement yerine gerçekleşmiş recoverable disable incident; aynı temel dependency açıkça korunur. | Henüz çözülmedi |
| S11-32 | 3.2 | Live ConfigMap file and process snapshot; files ... update ... reads ... only once | Karma; S03-01 file projection koşulu zaten sağlanmış; yeni application cache katmanı. | Henüz çözülmedi |
| S11-33 | 1.3 | Bigtable range locality; writes ... evenly across devices ... contiguous time interval | Bilinçli pekiştirme; S08-36 temel row key; S09-15 hot-device varsayımı açıkça yok, yeni kapsam değil. | Henüz çözülmedi |
| S11-34 | 2.2 | Patch the final runtime stage; from the final runtime base | Karma; S08-23 multi-stage + S06-18 patch, yeni yanlış stage onarımını ayırma. | Henüz çözülmedi |
| S11-35 | 4.3 | Report structured exception events; omits the exception stack ... structured error-event fields | Yeni ölçüm; S09-30 severity parse doğru varsayılır; Error Reporting event içeriği ölçülür. | Henüz çözülmedi |
| S11-36 | 3.1 | Long-lived gRPC stream recovery; deployments can also replace instances ... resume | Karma; S10-11 streaming seçimi doğru, yeni lifecycle recovery ve durable session şartı. | Henüz çözülmedi |
| S11-37 | 1.2 | Direct GKE principal resource scope; token acquisition succeeds ... separate project | Bilinçli pekiştirme; S03-04/S08-15 direct WIF, cross-project scope ile mekanizma uygulanır; yeni temel konu değil. | Henüz çözülmedi |
| S11-38 | 2.3 | Tenant authorization negative test; authentication succeeds but account ownership is not enforced | Karma; S10-13 sonrası farklı karar: token verify doğru varsayılır, account authorization negative test. Anlık token-verification kopyası değil; kalıcılık sayılmaz. | Henüz çözülmedi |
| S11-39 | 3.2 | Same tag does not update Pods; no change to the Deployment Pod template | Karma; S02-06 template rollout + S04-03 digest; new registry tag change teşhisi. | Henüz çözülmedi |
| S11-40 | 4.2 | Batch subrequest retry; multipart response ... individual transient failures | Karma; S07-04 metadata precondition + API batching; yeni subresponse outcome kararı. | Henüz çözülmedi |
| S11-41 | 1.2 | Retention beats early lifecycle eligibility; locked ninety-day ... retention expiry ... later | Karma; S04-17 lock + S06-17 lifecycle; yeni conflicting eligibility hesabı, hold değil. | Henüz çözülmedi |
| S11-42 | 2.3 | Load generation includes queueing; arrives independently of earlier completions | Yeni ölçüm; S09-33 cold/warm fairness yerine load-generator workload modelini ölçer. | Henüz çözülmedi |
| S11-43 | 3.1 | Source build identity denied; fails before producing ... configured Cloud Build service account | Bilinçli pekiştirme; S03-12/S04-18 build/runtime boundary, source deployment stage kanıtı. | Henüz çözülmedi |
| S11-44 | 1.1 | Regional dependency failure scope; both regions depend on one Cloud SQL primary | Bilinçli pekiştirme; S08-12 regional DR + S05-05 cache durability; yeni temel scope değil. | Henüz çözülmedi |
| S11-45 | 4.3 | Error-budget burn rate; recent window ... rather than ... monthly final result | Karma; S10-20 doğru request denominator üzerine error-budget oranı; yeni hesap. | Henüz çözülmedi |
| S11-46 | 3.2 | Startup budget and deadlock detection; without weakening the steady-state liveness response | Bilinçli pekiştirme; S04-19/S08-07, farklı süreler; yeni temel probe kapsamı değil. | Henüz çözülmedi |
| S11-47 | 1.2 | AI-selected resource is not authorization; well-formed ... another customer’s account | Karma; S08-48 output validation + S10-13 identity, doğrulanmış kimlik varsayımıyla yeni model-resource sınırı. | Henüz çözülmedi |
| S11-48 | 1.1 | Warm capacity with finite budget; small warm baseline ... peak ... elastic | Bilinçli pekiştirme; S01-12 cold start, finite baseline budget ekli; tüm burst için guarantee yok. | Henüz çözülmedi |
| S11-49 | 2.1 | Emulator success versus Storage service contract; direct API object listing; no ... intermediary | Karma; S07-20 Storage consistency/cache + development fake fidelity; emulator ürün garantisi iddiası değil. | Henüz çözülmedi |
| S11-50 | 4.1 | Unknown commit result; cannot tell whether ... committed | Karma; S09-04 rollback doğrulanmış koşulunun tersi; S09-50 commit-before-ack uygulaması; yeni temel idempotency değil. | Henüz çözülmedi |


## 5 Ekim 2026 — PCD-S12: Udemy kaynak seçkisi

Kullanıcının açık talebiyle 50 farklı kaynak sorunun uyarlaması. Tamamı seçki/pekiştirme; yeni temel kapsam veya kalıcılık kanıtı sayılmaz. Kaynak ID her sorunun kökenidir; eski set bağlantıları seçili örneklerdir, eksiksiz benzerlik listesi değildir. Henüz bağımsız cevap yok.

| Soru | Rehber | Ölçülen karar | Köken / önceki ilişki | Durum |
|---|---|---|---|---|
| S12-01 | 2.2 | Özel build aracı | Udemy PT2-Q4; seçki/pekiştirme | Hazır, çözülmedi |
| S12-02 | 2.2 | Aynı artifact promotion | Udemy PT5-Q9; seçki/pekiştirme; S04-03 | Hazır, çözülmedi |
| S12-03 | 1.3 | Bigtable failover | Udemy PT6-Q11; seçki/pekiştirme | Hazır, çözülmedi |
| S12-04 | 3.1 | Cloud Run admission politikası | Udemy PT5-Q48; seçki/pekiştirme | Hazır, çözülmedi |
| S12-05 | 2.1 | Kurumsal geliştirme ortamı | Udemy PT4-Q52; seçki/pekiştirme; S09-29 | Hazır, çözülmedi |
| S12-06 | 2.2 | Build step dosya paylaşımı | Udemy PT5-Q15; seçki/pekiştirme | Hazır, çözülmedi |
| S12-07 | 3.2 | Autopilot Arm yerleşimi | Udemy PT6-Q56; seçki/pekiştirme | Hazır, çözülmedi |
| S12-08 | 1.3 | Firestore büyüyen mesaj geçmişi | Udemy PT5-Q44; seçki/pekiştirme | Hazır, çözülmedi |
| S12-09 | 3.1 | Workflows Cloud Run job çağrısı | Udemy PT6-Q59; seçki/pekiştirme | Hazır, çözülmedi |
| S12-10 | 4.3 | Clusterlar arası log sorgusu | Udemy PT5-Q5; seçki/pekiştirme | Hazır, çözülmedi |
| S12-11 | 1.2 | Terraform Cloud kimliği | Udemy PT6-Q21; seçki/pekiştirme | Hazır, çözülmedi |
| S12-12 | 3.1 | Source deploy ile entegrasyon | Udemy PT6-Q57; seçki/pekiştirme | Hazır, çözülmedi |
| S12-13 | 4.1 | Private SQL yerel erişim | Udemy PT6-Q50; seçki/pekiştirme | Hazır, çözülmedi |
| S12-14 | 3.2 | Drain sırasında PDB | Udemy PT6-Q18; seçki/pekiştirme; S11-07 (rollout ile karşılaştırma) | Hazır, çözülmedi |
| S12-15 | 1.1 | Hot data cache ve kaynak veri | Udemy PT6-Q24; seçki/pekiştirme; S11-01 | Hazır, çözülmedi |
| S12-16 | 1.1 | Storage olayından çok adımlı işlem | Udemy PT6-Q34; seçki/pekiştirme | Hazır, çözülmedi |
| S12-17 | 2.2 | Registry olayıyla build | Udemy PT6-Q17; seçki/pekiştirme | Hazır, çözülmedi |
| S12-18 | 2.2 | Build ile push sınırı | Udemy PT6-Q20; seçki/pekiştirme | Hazır, çözülmedi |
| S12-19 | 4.1 | SQL analitik ayrımı | Udemy PT5-Q54; seçki/pekiştirme | Hazır, çözülmedi |
| S12-20 | 4.1 | Küçük API yazımlarını batch etme | Udemy PT5-Q33; seçki/pekiştirme; S10-11 | Hazır, çözülmedi |
| S12-21 | 4.2 | Cross-project SQL API | Udemy PT6-Q45; seçki/pekiştirme | Hazır, çözülmedi |
| S12-22 | 3.2 | Trafik uygunluğu | Udemy PT5-Q32; seçki/pekiştirme; S11-16 | Hazır, çözülmedi |
| S12-23 | 4.2 | İsteğe bağlı API ve arayüz | Udemy PT1-Q38; seçki/pekiştirme | Hazır, çözülmedi |
| S12-24 | 1.2 | Cross-project runtime izinleri | Udemy PT5-Q30; seçki/pekiştirme | Hazır, çözülmedi |
| S12-25 | 2.3 | Dayanıklılık testi | Udemy PT6-Q49; seçki/pekiştirme | Hazır, çözülmedi |
| S12-26 | 4.2 | 429 sonrası retry | Udemy PT5-Q52; seçki/pekiştirme | Hazır, çözülmedi |
| S12-27 | 3.2 | Deployment rollout sınırları | Udemy PT5-Q34; seçki/pekiştirme; S11-07 | Hazır, çözülmedi |
| S12-28 | 1.1 | Büyük dosya upload veri yolu | Udemy PT2-Q13; seçki/pekiştirme | Hazır, çözülmedi |
| S12-29 | 1.2 | Retention ve lifecycle | Udemy PT1-Q13; seçki/pekiştirme; S04-17 / S11-41 | Hazır, çözülmedi |
| S12-30 | 1.1 | Üçüncü taraf özelliği kapatma | Udemy PT6-Q38; seçki/pekiştirme | Hazır, çözülmedi |
| S12-31 | 4.1 | Atomik read-modify-write | Udemy PT5-Q36; seçki/pekiştirme; S10-16 (batch/transaction ayrımı) | Hazır, çözülmedi |
| S12-32 | 1.1 | API ürününe göre kota | Udemy PT6-Q3; seçki/pekiştirme; S11-11 | Hazır, çözülmedi |
| S12-33 | 1.1 | Workflow dallanması | Udemy PT4-Q59; seçki/pekiştirme | Hazır, çözülmedi |
| S12-34 | 2.2 | Test attestation akışı | Udemy PT6-Q14; seçki/pekiştirme | Hazır, çözülmedi |
| S12-35 | 2.3 | Tekrarlanabilir messaging testi | Udemy PT2-Q18; seçki/pekiştirme; S11-30 | Hazır, çözülmedi |
| S12-36 | 3.2 | Yavaş başlangıç ve liveness | Udemy PT5-Q27; seçki/pekiştirme; S11-46 | Hazır, çözülmedi |
| S12-37 | 3.1 | Bucket create audit olayı | Udemy PT6-Q71; seçki/pekiştirme | Hazır, çözülmedi |
| S12-38 | 4.3 | CPU ve heap profili | Udemy PT2-Q45; seçki/pekiştirme | Hazır, çözülmedi |
| S12-39 | 4.3 | Dış servis gecikmesini izleme | Udemy PT5-Q46; seçki/pekiştirme | Hazır, çözülmedi |
| S12-40 | 1.2 | Namespace yetkisi | Udemy PT5-Q26; seçki/pekiştirme | Hazır, çözülmedi |
| S12-41 | 1.2 | API güvenliğinin katmanları | Udemy PT6-Q41; seçki/pekiştirme | Hazır, çözülmedi |
| S12-42 | 1.2 | AlloyDB için ağ ve kimlik ayrımı | Udemy PT6-Q15; seçki/pekiştirme | Hazır, çözülmedi |
| S12-43 | 3.2 | Pub/Sub backlog ile HPA | Udemy PT1-Q15; seçki/pekiştirme; S11-23 | Hazır, çözülmedi |
| S12-44 | 3.1 | Cloud Run kademeli rollout | Udemy PT6-Q2; seçki/pekiştirme | Hazır, çözülmedi |
| S12-45 | 1.3 | Paylaşılan dosya sistemi | Udemy PT5-Q22; seçki/pekiştirme; S09-28 | Hazır, çözülmedi |
| S12-46 | 1.3 | Bigtable row key | Udemy PT5-Q41; seçki/pekiştirme; S11-33 | Hazır, çözülmedi |
| S12-47 | 2.3 | Paralel performans testi izolasyonu | Udemy PT4-Q7; seçki/pekiştirme; S09-33 (test karşılaştırılabilirliği) | Hazır, çözülmedi |
| S12-48 | 2.1 | Yerelde güvenli SQL bağlantısı | Udemy PT5-Q56; seçki/pekiştirme | Hazır, çözülmedi |
| S12-49 | 3.2 | StatefulSet kimliği | Udemy PT2-Q10; seçki/pekiştirme | Hazır, çözülmedi |
| S12-50 | 2.1 | Cloud Shell GKE erişim teşhisi | Udemy PT5-Q39; seçki/pekiştirme | Hazır, çözülmedi |


## 5 Ekim 2026 — PCD-S13 SkillCertPro seçkisi

[Sorular](PCD-S13.md) · [Ayrı Türkçe anahtar](../answers/scenarios/PCD-S13.md). Kullanıcı kaynak içinden 50 soruluk tam sınav istedi. 49 SkillCertPro senaryosu + 1 açıkça etiketli resmî Eventarc tamamlayıcısı; 16/12/12/10, 11 alt başlık. Q22/Q39/Q41 çift, diğer 47 soru tek seçim. 120 dakika kişisel hedef. 44–69 kelimelik gövdeler; gerçek sınavla kalibrasyon iddiası yok. Önceki yakın kararlar bilinçli pekiştirme/karma; 50 yeni konu diye sunulmaz. Henüz kullanıcı cevabı veya puan yok.

| ID | Rehber | Karar | Kaynak ve önceki ilişki | Durum |
|---|---|---|---|---|
| S13-01 | 2.2 | build-DAG | SCP14-Q20; S11-06 / S04-02; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-02 | 2.1 | Skaffold-sync | SCP17-Q07; S10-14; karma, rebuild yerine file sync | Hazır, çözülmedi |
| S13-03 | 3.1 | Cloud-Deploy-canary | SCP16-Q60; S12-44; karma, Cloud Deploy automation | Hazır, çözülmedi |
| S13-04 | 4.2 | pagination-fields | SCP13-Q06; S11-29; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-05 | 2.1 | Gemini-MCP | SCP14-Q51; S06-06 / S08-27; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-06 | 4.3 | bucket-metrics | SCP17-Q51; S12-10 / S10-15; merkezi ölçüm kapsamı | Hazır, çözülmedi |
| S13-07 | 1.2 | delayed-secret-destroy | SCP14-Q58; S11-13/31 ile ilişkili; Secret Manager version yaşam döngüsü | Hazır, çözülmedi |
| S13-08 | 3.1 | secret-startup | SCP14-Q60; S11-12; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-09 | 1.1 | Tasks-retry | SCP14-Q17; S11-28; Tasks pekiştirme, retry policy kararı | Hazır, çözülmedi |
| S13-10 | 1.1 | multi-region-Run | SCP15-Q09; S11-44; karma, bağımlılıklar sağlıklı varsayılıyor | Hazır, çözülmedi |
| S13-11 | 3.2 | HPA-requests | SCP14-Q23; S10-12 / S11-23; HPA farklı engel teşhisi | Hazır, çözülmedi |
| S13-12 | 3.1 | outlier-detection | SCP16-Q22; S11-44; LB failure detection uygulaması | Hazır, çözülmedi |
| S13-13 | 4.3 | Query-Insights | SCP15-Q05; S12-38/39 observability temeli; ORM route correlation | Hazır, çözülmedi |
| S13-14 | 1.3 | snapshot-reads | SCP16-Q19; S08 Spanner temeli; snapshot kararı pekiştirme | Hazır, çözülmedi |
| S13-15 | 1.1 | Workflows | SCP14-Q27; S12-33 / S01-15; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-16 | 4.3 | log-alert | SCP15-Q12; S12-10 log sorgusu üzerine matching event alert | Hazır, çözülmedi |
| S13-17 | 1.3 | time-bucket | SCP14-Q19; S12-46 / S11-33; karma, row granularity değişiyor | Hazır, çözülmedi |
| S13-18 | 1.3 | signed-URL | SCP14-Q52; S11-24 / S01-04; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-19 | 1.2 | two-attestors | SCP18-Q26; S12-34; karma, iki bağımsız onay | Hazır, çözülmedi |
| S13-20 | 2.1 | Workstations | SCP14-Q50; S12-05 / S09-29 / S11-14; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-21 | 2.3 | dependency-injection | SCP18-Q25; S12-35 / S11-30; bilinçli unit/integration ayrımı | Hazır, çözülmedi |
| S13-22 | 3.1 | Storage finalized trigger and receiver | OFFICIAL-EVENTARC; Ek resmî soru; S12-16/37 ve S11-19 ile ilişkili, IAM yerine event/receiver seçimi | Hazır, çözülmedi |
| S13-23 | 3.2 | HPA-GitOps | SCP14-Q35; S11-23 HPA temeli; desired-state ownership | Hazır, çözülmedi |
| S13-24 | 4.2 | backoff | SCP15-Q25; S12-26 / S11-15; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-25 | 4.3 | PromQL-ratio | SCP16-Q58; S10-20 / S11-45; bilinçli oran/alert pekiştirmesi | Hazır, çözülmedi |
| S13-26 | 1.1 | API-deprecation | SCP14-Q06; S12-32 API politikasıyla ilişkili; farklı yaşam döngüsü kararı | Hazır, çözülmedi |
| S13-27 | 4.1 | pool-budget | SCP17-Q40; S11-03; bilinçli pool bütçesi pekiştirmesi | Hazır, çözülmedi |
| S13-28 | 4.1 | resumable-offset | SCP15-Q31; S11-04 transfer temeli; upload offset kararı | Hazır, çözülmedi |
| S13-29 | 1.2 | identity-tenants | SCP17-Q33; S10-13 / S11-38; kimlik izolasyonu pekiştirme | Hazır, çözülmedi |
| S13-30 | 2.3 | allowExitCodes | SCP16-Q05; S11-06; karma, seçici failure exception | Hazır, çözülmedi |
| S13-31 | 1.3 | JSONB-schema | SCP16-Q31; S10-08 PostgreSQL üzerine schema kararı | Hazır, çözülmedi |
| S13-32 | 2.1 | code-customization | SCP18-Q20; S11-26 context temeli; kurumsal repository özelleştirmesi | Hazır, çözülmedi |
| S13-33 | 2.3 | publisher-interaction-test | SCP15-Q06; S10-10 yerine seçildi; S11-10 test oracle temeli üzerine interaction assertion | Hazır, çözülmedi |
| S13-34 | 2.2 | multi-stage | SCP16-Q16; S11-34 / S08-23; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-35 | 3.2 | immutable-config | SCP17-Q20; S11-32; ters lifecycle koşulu, canlı değişim gerekmiyor | Hazır, çözülmedi |
| S13-36 | 3.1 | ingress | SCP13-Q33; S03/Cloud Run ingress; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-37 | 1.3 | vector-index | SCP17-Q05; AI/veri temeline ek index uygulaması; yeni temel AI kapsamı iddiası yok | Hazır, çözülmedi |
| S13-38 | 1.3 | Spanner-hash-key | SCP16-Q53; S07/S09 hotspot kararlarıyla ilişkili pekiştirme | Hazır, çözülmedi |
| S13-39 | 1.2 | cross-perimeter | SCP15-Q10; S09 VPCSC kapsamı; bilinçli güvenlik pekiştirmesi | Hazır, çözülmedi |
| S13-40 | 3.2 | BackendConfig | SCP14-Q55; S11-16 probe temeli; LB ve Pod check ayrımı | Hazır, çözülmedi |
| S13-41 | 2.2 | build-images | SCP16-Q02; S12-18; karma, build results kaydı ekli | Hazır, çözülmedi |
| S13-42 | 2.1 | debugger-source-map | SCP17-Q23; S10-14; karma, bağlı debugger path teşhisi | Hazır, çözülmedi |
| S13-43 | 3.2 | metadata-init | SCP16-Q06; S11-37 WIF üzerine transient startup dependency | Hazır, çözülmedi |
| S13-44 | 2.2 | immutable-tags | SCP15-Q26; S11-39 / S12-02; registry tag enforcement kararı | Hazır, çözülmedi |
| S13-45 | 4.1 | listener-lifecycle | SCP18-Q05; Firestore istemci lifecycle; temel realtime veri kullanımının uygulaması | Hazır, çözülmedi |
| S13-46 | 3.2 | Autopilot-WIF | SCP16-Q40; S11-37 / S12-07; Autopilot yapılandırması | Hazır, çözülmedi |
| S13-47 | 3.2 | container-HPA | SCP17-Q54; HPA temeli pekiştirme; container-specific ölçüm | Hazır, çözülmedi |
| S13-48 | 1.1 | cache-aside | SCP16-Q27; S12-15 / S11-01; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-49 | 1.2 | egress-policy | SCP18-Q07; S11-21 / S03-10; bilinçli pekiştirme | Hazır, çözülmedi |
| S13-50 | 4.2 | quota-project | SCP17-Q44; S09-39; bilinçli pekiştirme, izin zaten sağlanmış | Hazır, çözülmedi |
