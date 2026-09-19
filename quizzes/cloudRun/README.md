# Cloud Run — 26 quiz / 130 soru

Üç ana modüle ait 13 PDF dosyası korundu. İki dosya diğerleriyle SHA-256 düzeyinde birebir aynı olduğundan sorular 11 benzersiz ders (131 sayfa) üzerinden hazırlandı. Kopya dosyalar için tekrar quiz üretilmedi. İngilizce sorular beşlik setlerde, Türkçe açıklamalar ve PDF sayfa referansları ayrı cevap anahtarlarındadır.

## Çalışma sırası

| Ders | Konu | Set / soru | Kaynak |
|---|---|---|---|
| R01 | Resource model | 2 / 10 | [PDF](../../cloudRun/T-DVCRUN-B-m1-l2-file-en-3.en.pdf) |
| R02 | Container lifecycle | 3 / 15 | [PDF](../../cloudRun/T-DVCRUN-B-m1-l3-file-en-4.en.pdf) |
| R03 | Autoscaling | 2 / 10 | [PDF](../../cloudRun/T-DVCRUN-B-m1-l4-file-en-5-new.en.pdf) |
| R04 | Access control | 3 / 15 | [PDF](../../cloudRun/T-DVCRUN-B-m1-l5-file-en-6.en.pdf) |
| R05 | Service accounts and identity | 2 / 10 | [PDF](../../cloudRun/T-DVCRUN-B-m2-l1-file-en-8-new.en.pdf) |
| R06 | Resource hierarchy | 1 / 5 | [PDF](../../cloudRun/T-DVCRUN-B-m2-l2-file-en-9.en.pdf) |
| R07 | Least privilege | 1 / 5 | [PDF](../../cloudRun/T-DVCRUN-B-m2-l3-file-en-10.en.pdf) |
| R08 | Secrets and environment variables | 2 / 10 | [PDF](../../cloudRun/T-DVCRUN-B-m2-l5-file-en-11.en.pdf) |
| R09 | Development and testing | 3 / 15 | [PDF](../../cloudRun/T-DVCRUN-B-m3-l1-file-en-13-new.en.pdf) |
| R10 | Deployments and revisions | 4 / 20 | [PDF](../../cloudRun/T-DVCRUN-B-m3-l2-file-en-14.en.pdf) |
| R11 | Google Cloud integrations | 3 / 15 | [PDF](../../cloudRun/T-DVCRUN-B-m3-l3-file-en-15.en.pdf) |

Önerilen sıra R01 → R11. R01–R04 fundamentals, R05–R08 identity/authentication, R09–R11 development/testing/integration kapsamındadır. Her setten sonra ayrı cevap anahtarını aç. Çok seçimli soruda doğru seçeneklerin tümü ve yalnız onlar işaretlendiyse 1 puan ver. [Takip tablosuna](../progress.csv) puan ve kararsız sorularını kaydet. Bu bölüme ait çözüm sonucu henüz paylaşılmadığından yeni satırlar boş bırakıldı.

## Setler

| Quiz | Konu | Sorular | Cevaplar |
|---|---|---|---|
| R01-01 | Regional services, revisions and instances | [Çöz](R01-01.md) | [Kontrol et](../answers/cloudRun/R01-01.md) |
| R01-02 | Jobs, executions and task outcomes | [Çöz](R01-02.md) | [Kontrol et](../answers/cloudRun/R01-02.md) |
| R02-01 | Startup, probes and internal image storage | [Çöz](R02-01.md) | [Kontrol et](../answers/cloudRun/R02-01.md) |
| R02-02 | Idle behavior, CPU allocation and warm instances | [Çöz](R02-02.md) | [Kontrol et](../answers/cloudRun/R02-02.md) |
| R02-03 | SIGTERM, cleanup and abrupt failures | [Çöz](R02-03.md) | [Kontrol et](../answers/cloudRun/R02-03.md) |
| R03-01 | Scale to zero, queuing and instance boundaries | [Çöz](R03-01.md) | [Kontrol et](../answers/cloudRun/R03-01.md) |
| R03-02 | Concurrency and load testing | [Çöz](R03-02.md) | [Kontrol et](../answers/cloudRun/R03-02.md) |
| R04-01 | API authorization and IAM bindings | [Çöz](R04-01.md) | [Kontrol et](../answers/cloudRun/R04-01.md) |
| R04-02 | Invocation permissions and network ingress | [Çöz](R04-02.md) | [Kontrol et](../answers/cloudRun/R04-02.md) |
| R04-03 | Private VPC connectivity and connectors | [Çöz](R04-03.md) | [Kontrol et](../answers/cloudRun/R04-03.md) |
| R05-01 | Service identity and API access tokens | [Çöz](R05-01.md) | [Kontrol et](../answers/cloudRun/R05-01.md) |
| R05-02 | Synchronous calls and caller authorization | [Çöz](R05-02.md) | [Kontrol et](../answers/cloudRun/R05-02.md) |
| R06-01 | Hierarchy and inherited allow policies | [Çöz](R06-01.md) | [Kontrol et](../answers/cloudRun/R06-01.md) |
| R07-01 | Least privilege and IAM role types | [Çöz](R07-01.md) | [Kontrol et](../answers/cloudRun/R07-01.md) |
| R08-01 | Environment variables and configuration precedence | [Çöz](R08-01.md) | [Kontrol et](../answers/cloudRun/R08-01.md) |
| R08-02 | Secret versions, mounts and IAM | [Çöz](R08-02.md) | [Kontrol et](../answers/cloudRun/R08-02.md) |
| R09-01 | Workload fit and the container runtime contract | [Çöz](R09-01.md) | [Kontrol et](../answers/cloudRun/R09-01.md) |
| R09-02 | Execution environments and storage lifetime | [Çöz](R09-02.md) | [Kontrol et](../answers/cloudRun/R09-02.md) |
| R09-03 | Cloud Code, emulation and local testing | [Çöz](R09-03.md) | [Kontrol et](../answers/cloudRun/R09-03.md) |
| R10-01 | Image builds, source deployment and repositories | [Çöz](R10-01.md) | [Kontrol et](../answers/cloudRun/R10-01.md) |
| R10-02 | Revision creation and retained configuration | [Çöz](R10-02.md) | [Kontrol et](../answers/cloudRun/R10-02.md) |
| R10-03 | Readiness, no-traffic deployment and revision pinning | [Çöz](R10-03.md) | [Kontrol et](../answers/cloudRun/R10-03.md) |
| R10-04 | Revision tags, traffic percentages and session affinity | [Çöz](R10-04.md) | [Kontrol et](../answers/cloudRun/R10-04.md) |
| R11-01 | Memorystore networking and integration setup | [Çöz](R11-01.md) | [Kontrol et](../answers/cloudRun/R11-01.md) |
| R11-02 | Authenticated Pub/Sub push and acknowledgements | [Çöz](R11-02.md) | [Kontrol et](../answers/cloudRun/R11-02.md) |
| R11-03 | Cloud SQL paths, credentials and connection pools | [Çöz](R11-03.md) | [Kontrol et](../answers/cloudRun/R11-03.md) |

## Aynı içeriğe sahip dosyalar

- `fil5bL-T-DVCRUN-B-m3-l1-file-en-13-new.en.pdf` = `T-DVCRUN-B-m3-l1-file-en-13-new.en.pdf` (dosya içeriği birebir aynı).
- `tHifym-T-DVCRUN-B-m3-l2-file-en-14.en.pdf` = `T-DVCRUN-B-m3-l2-file-en-14.en.pdf` (dosya içeriği birebir aynı).

## Kaynak kapsamı

Sorular PDF ayrıntılarını esas alır. Belirli sayfadaki sayısal değerler açıkça ders sürümüne bağlıdır. Varsayılan Editor rolü, idle billing, allow-policy inheritance, tek-image ifadesi ve Cloud SQL bağlantı sayısındaki kapsam sorunları [kaynak notlarında](../SOURCE-NOTES.md) ayrıca açıklanır. Resmî web kaynakları bu ayrımları doğrulamak içindir; dosyalarda bulunmayan yeni bir ders modülü oluşturulmadı.

[Tüm quizler](../README.md) · [Kapsam haritası](../COVERAGE.md)
