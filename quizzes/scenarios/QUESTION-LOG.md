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
