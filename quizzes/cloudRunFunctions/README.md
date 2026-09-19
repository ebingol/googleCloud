# Cloud Run Functions — 25 quiz / 125 soru

Beş kaynak PDF’nin tamamı incelendi. Konular beş soruluk setlere ayrıldı; İngilizce sorular ile Türkçe açıklamalı cevap anahtarları ayrı tutulur. Tek ve çok seçimli sorularda istenen doğru seçenek sayısı yazılıdır.

## Çalışma sırası

- C01: Giriş, handler türleri, limitler, runtime yapısı ve deployment — 6 set / 30 soru.
- C02: Trigger türleri, Workflows, VPC ve bağlantı akışları — 5 set / 25 soru.
- C03: Kimlik, IAM, ağ erişimi ve CMEK — 5 set / 25 soru.
- C04: Memorystore, environment, Firestore ve secrets — 4 set / 20 soru.
- C05: Uygulama, hata yönetimi, performans, retry ve ölçekleme — 5 set / 25 soru.

Önce bir seti çöz; ardından ayrı cevap anahtarından tüm doğru seçenekleri ve PDF sayfasını kontrol et. Çok seçimli soruda ancak doğru seçeneklerin tamamı, yanlış seçenek olmadan seçildiyse 1 puan ver. Puanı ve kararsız kaldığın soruları [takip tablosuna](../progress.csv) kaydet. Henüz çözüm sonucu paylaşılmadığı için yeni satırlar boş bırakıldı.

## Setler

| Quiz | Konu | Sorular | Cevaplar |
|---|---|---|---|
| C01-01 | Platform, benefits and use cases | [Çöz](C01-01.md) | [Kontrol et](../answers/cloudRunFunctions/C01-01.md) |
| C01-02 | HTTP, CloudEvent and background handlers | [Çöz](C01-02.md) | [Kontrol et](../answers/cloudRunFunctions/C01-02.md) |
| C01-03 | Capacity, revisions and portability | [Çöz](C01-03.md) | [Kontrol et](../answers/cloudRunFunctions/C01-03.md) |
| C01-04 | Runtime source layout, entry points and regions | [Çöz](C01-04.md) | [Kontrol et](../answers/cloudRunFunctions/C01-04.md) |
| C01-05 | Deployment permissions, flags and sources | [Çöz](C01-05.md) | [Kontrol et](../answers/cloudRunFunctions/C01-05.md) |
| C01-06 | Build pipeline and artifact storage | [Çöz](C01-06.md) | [Kontrol et](../answers/cloudRunFunctions/C01-06.md) |
| C02-01 | Trigger categories, HTTP and Pub/Sub | [Çöz](C02-01.md) | [Kontrol et](../answers/cloudRunFunctions/C02-01.md) |
| C02-02 | Cloud Storage, Firestore and Firebase events | [Çöz](C02-02.md) | [Kontrol et](../answers/cloudRunFunctions/C02-02.md) |
| C02-03 | Workflows coordination and data passing | [Çöz](C02-03.md) | [Kontrol et](../answers/cloudRunFunctions/C02-03.md) |
| C02-04 | Serverless VPC Access configuration | [Çöz](C02-04.md) | [Kontrol et](../answers/cloudRunFunctions/C02-04.md) |
| C02-05 | Connecting Redis and private VM services | [Çöz](C02-05.md) | [Kontrol et](../answers/cloudRunFunctions/C02-05.md) |
| C03-01 | Identity, tokens and IAM authorization | [Çöz](C03-01.md) | [Kontrol et](../answers/cloudRunFunctions/C03-01.md) |
| C03-02 | Runtime identity and function-to-function invocation | [Çöz](C03-02.md) | [Kontrol et](../answers/cloudRunFunctions/C03-02.md) |
| C03-03 | Ingress, egress and VPC Service Controls | [Çöz](C03-03.md) | [Kontrol et](../answers/cloudRunFunctions/C03-03.md) |
| C03-04 | CMEK scope and setup | [Çöz](C03-04.md) | [Kontrol et](../answers/cloudRunFunctions/C03-04.md) |
| C03-05 | CMEK deployment, versions and key loss | [Çöz](C03-05.md) | [Kontrol et](../answers/cloudRunFunctions/C03-05.md) |
| C04-01 | Memorystore and Redis connectivity | [Çöz](C04-01.md) | [Kontrol et](../answers/cloudRunFunctions/C04-01.md) |
| C04-02 | Environment-variable configuration | [Çöz](C04-02.md) | [Kontrol et](../answers/cloudRunFunctions/C04-02.md) |
| C04-03 | Firestore documents, events and snapshots | [Çöz](C04-03.md) | [Kontrol et](../answers/cloudRunFunctions/C04-03.md) |
| C04-04 | Secret Manager, versions and cross-project access | [Çöz](C04-04.md) | [Kontrol et](../answers/cloudRunFunctions/C04-04.md) |
| C05-01 | Idempotency, completion and temporary files | [Çöz](C05-01.md) | [Kontrol et](../answers/cloudRunFunctions/C05-01.md) |
| C05-02 | Errors, local testing and runtime portability | [Çöz](C05-02.md) | [Kontrol et](../answers/cloudRunFunctions/C05-02.md) |
| C05-03 | Cold starts, object reuse and networking | [Çöz](C05-03.md) | [Kontrol et](../answers/cloudRunFunctions/C05-03.md) |
| C05-04 | Retry configuration and failure handling | [Çöz](C05-04.md) | [Kontrol et](../answers/cloudRunFunctions/C05-04.md) |
| C05-05 | Configuration, scaling and traffic splitting | [Çöz](C05-05.md) | [Kontrol et](../answers/cloudRunFunctions/C05-05.md) |

## Kaynak kapsamı

Sorular bu PDF sürümlerinin bilgi ve ayrıntılarını ölçer. Kota, runtime desteği, retry varsayılanları, trigger kısıtları ve komut örnekleri güncel ürün dokümantasyonu yerine kullanılmamalıdır. Her cevabın PDF sayfası vardır. Web kaynaklarından yeni sınav kapsamı eklenmedi.

Güvenlik modülü s. 13’teki CLI örneği ilk neslin invoke rolünü kullanırken metin yeni neslin rolünü de açıklıyor. S. 23’te aktif instance’a gelen yeni çağrıların başarısızlığı slaytta “may fail”, açıklamada “will fail” olarak yazılmış. Sorular bu ayrımları gözetir. Ayrıntı: [kaynak notları](../SOURCE-NOTES.md).

[Tüm quizler](../README.md) · [Kapsam haritası](../COVERAGE.md)
