# SkillCertPro Professional Cloud Developer soru incelemesi

5 Ekim 2026. Satın alınan 18 denemenin tamamı tarandı. Değerlendirmem: **seçilerek kullanılabilecek anlamlı sorular var; özellikle son setler mevcut seviyene daha uygun. Ancak platformun cevap anahtarı güvenilir bir hakem değil.** Bütün paketi sırayla çözmek yerine tekrarları ve sorunlu soruları ayıklayarak tam sınav oluşturmak daha verimli.

## İncelemenin kapsamı

18 setten **1.050 soru kaydı** çıkarıldı. İlk iki set 59'ar, 3–17. setler 60'ar, son set 32 soru içeriyor. Ürün sayfasındaki 1.050 ile uyumlu; satın alma sonrası başlıktaki 1.052 ile değil. HTML sayfa başlıkları ve set numaraları doğrulandı.

Tüm soru gövdeleri ve platform anahtarları tarandı; aynı gövdelerin tekrarları eşlendi ve seçilen cevap metinleri karşılaştırıldı. Şüpheli soruların seçenek/açıklamaları ve 50 ön adayın bütün seçenekleri ayrıca okundu. PT12'nin 60 sorusu daha ayrıntılı incelendi. **Her açıklamanın her cümlesi, her komut veya görsel bağımsız doğrulanmış değildir.** Görsel içeren 65 kaydın görsel ayrıntıları tam kontrol edilmiş sayılmaz. Bu bir soru bankası kalite taraması; laboratuvar doğrulaması veya bütün bankanın hatasızlık onayı değil.

19. sayfa soru seti değil; bir Master Cheat Sheet PDF gömüyor. HTML'den çıkarılan kısa metin PDF içeriği değildir. Bu bonus PDF bu incelemede değerlendirilmedi.

PT1/PT6 ilk sorularda boş Check, PT12'de boş Finish Test kullanıldı. Platformdaki bu inceleme kayıtları ve PT12 0/60 **kullanıcının sınav sonucu değildir**.

## Tekrarlar ve seviyeye uygunluk

- Noktalama ve boşluk farkları kaldırılınca **760 farklı soru gövdesi**, **156 tekrar grubu**, **290 tekrar yuvası** var. 760 farklı kavram demek değil; isimleri/sayıları değiştirilmiş yakın tekrarlar bunun dışında.
- PT1–11: 658 kayıt; eski Stackdriver/GCR/App Engine ağırlığı, kısa tanım soruları, tekrarlar ve bozuk seçenekler daha belirgin.
- PT12: ilk bölümünde güncel senaryolar, devamında eski/tekrarlı içerikle karışık yapı var.
- PT13–18: 332 kayıt; GKE, Cloud Run, geliştirici araçları, Secret Manager, Cloud Tasks ve Gemini açısından daha uygun başlangıç havuzu. Buna rağmen burada da teknik yanlışlar var.
- Gövde kelime sayısı medyanı PT1–11'de 47, PT12'de 46, PT13–18'de 52. Seçenekler dahil değil. Bu ölçüm gerçek sınavla uzunluk veya zorluk eşdeğerliği kanıtlamaz.

Senin için asıl değer yeni bir ürün adı görmekten çok, birbirine yakın iki çözümü hangi koşulun ayırdığını çalışmak. Bazı sorularda diğer üç seçenek belirgin biçimde yanlış; bunları zor veya güçlü ölçüm diye sunmamalıyız.

## Somut kalite sorunları

| Kaynak | Bulgu | Seçime etkisi |
|---|---|---|
| PT5 Q50 / PT8 Q49 / PT9 Q32 | Aynı Service discovery sorusu PT5'te Endpoint/env, diğerlerinde Service DNS anahtarı taşıyor. | Kaynak anahtarına göre yanlış sayılmaz. [Kubernetes Service](https://kubernetes.io/docs/concepts/services-networking/service/) ile düzeltilmeli. |
| PT10 Q10 | Pod IP değişimini soruyor; dört seçenek de autoscaling hakkında. Açıklama Service diyor ama bu seçenek yok. | Olduğu gibi kullanılamaz. |
| PT11 Q11 | Instance sayısı artmasın şartına rağmen ek instance oluşturan maxSurge=1 seçilmiş. | Kök ve anahtar çelişkisi; ele. |
| PT12 Q59 | Eski/etkin olmayan bucket'a aniden yüksek trafik için anahtar bucket dağıtımını seçiyor. | [Storage request rate](https://docs.cloud.google.com/storage/docs/request-rate) kademeli artışı öneriyor; anahtar hatalı. |
| PT12 Q35 | Log-based metric'in geçmiş loglarla geriye doğru doldurulacağı yazıyor. | [Logging belgesi](https://docs.cloud.google.com/logging/docs/logs-based-metrics) ile çelişiyor. |
| PT17 Q8 | Artifact Registry cleanup JSON'unda versionPrefixes kullanıyor, Docker tag önekleriyle version öneklerini karıştırıyor. | [Doğru alanlar](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy): tagPrefixes ve versionNamePrefixes farklı. |
| PT17 Q60 | hash(user_id) % N aynı kullanıcının işlemlerini farklı shard'lara dağıtır diyor. | Matematiksel olarak aynı user_id aynı prefix'i verir; kullanıcının sıcak yazma akışını bu yöntemle dağıttığı sonucu çıkmaz. |
| PT18 Q4 / PT17 Q50 | Retry limitleri birinde iki bağımsız sert üst sınır, diğerinde birlikte sağlanan koşullar diye öğretiliyor. | [Cloud Tasks belgesi](https://docs.cloud.google.com/tasks/docs/configuring-queues) birlikte sağlanma davranışını açıklıyor; PT18 Q4 düzeltilmeli. |
| PT16 Q50 | Kubernetes API üzerinden secret okuma problemini etcd encryption ile çözüyor. | At-rest encryption ile API authorization farklı; bu sorunun gerekçesi güvenilmez. |

Ayrıca Stackdriver Debugger'ı güncel hizmet gibi anlatan eski sorular var. Hizmet **31 Mayıs 2023'te kapatıldı**; Cloud Code ile IDE debugging ayrı ve güncel bir konu. [Google deprecation kaydı](https://docs.cloud.google.com/stackdriver/docs/deprecations/debugger-deprecation)

İç envanterde 137 kayda editoryal not kondu. Bunların hepsi doğrulanmış hata değildir: belirsizlik, güncellik kontrolü, düşük öğrenme değeri ve karşılaştırma referansları da var. Bu sayıdan bir “hata oranı” çıkarmıyoruz.

## Yararlanacağımız başlıklar

GKE tarafında HPA'nın requests üzerinden çalışması, sidecar etkisini ContainerResource ile ayırmak, GitOps replicas çatışması, BackendConfig ve WIF başlangıç sorunları iyi adaylar. Cloud Code source mapping ve Skaffold file sync de senin söylediğin debugging ihtiyacına uygun.

Gemini adı geçen **11 soru gövdesi** var; hepsi aynı değerde değil. Deterministik test, dependency injection, private code customization ve MCP ile araç kullanımı anlamlı. “Thumbs-down düğmesine bas” sorusu senin seviyen için düşük getirili. Workstations ortak geliştirme ortamı sorusu da seçilmeye değer. Güncel ürün belgeleri bu ana mekanizmaları destekliyor: [Workstations image özelleştirme](https://docs.cloud.google.com/workstations/docs/customize-container-images), [Gemini code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization), [Gemini agent mode](https://docs.cloud.google.com/gemini/docs/codeassist/agent-mode).

Cloud Tasks adı geçen 17 gövde var; retry, backoff, dispatch ve dedup ayrımları kullanılabilir. Ancak **hiçbir soru gövdesinde Eventarc adı geçmiyor**; açıklama/seçenek kayıtlarında iki yerde geçmesi doğrudan kapsam sayılmaz. Güncel [resmî rehber](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) Eventarc'ı açıkça içeriyor. Kaynağa dayanan tam sınavda bu boşluk resmî belgeye dayanan, ayrıca etiketlenen ek bir senaryoyla tamamlanmalı.

## Tam sınav için hazırlanan ön seçim

[50 adaylık seçim dosyası](skillcertpro-exam-candidates.json) hazır: rehberin yaklaşık **32/23/24/21** ağırlığı için **16/12/12/10** soru; 11 alt bölümün hepsinden aday var. Kaynak ID'si, konu ve gerekli düzeltme notu ayrı kayıtlı. Bu liste **henüz PCD-S13 sınavı değildir**.

Son sınav oluşturulurken seçenekler ve gerekçeler yeniden doğrulanacak, eski setlerle karar düzeyinde tekrar karşılaştırması yapılacak; Eventarc eksikliği için tekrarlı bir deployment adayı değiştirilecek. Gemini/Workstations adayı olması “yepyeni konu” ya da gerçek sınav soru sayısı tahmini anlamına gelmez. İngilizce sorular ve ayrı Türkçe anahtar düzeni korunacak.

Udemy'den hazırlanmış S12 aynen hazır ve çözülmemiş durumda. Bu inceleme herhangi bir ilk puanı değiştirmedi.

## Çalışma kayıtları

- [Soru kaynağı](skillcertpro-questions.json): 1.050 soru, seçenek, platform anahtarı ve açıklama.
- [İnceleme envanteri](skillcertpro-review-inventory.json): 1.050 kaydın tarama durumu, tekrar ilişkisi, görsel işareti ve editoryal notları.
- [Tekrar grupları](skillcertpro-duplicates.json).
- [Ayrıntılı inceleme notları](SKILLCERTPRO-REVIEW-NOTES.md): cevap ipuçları içerir.

Satıcının “gerçek sınav soruları” iddiası bağımsız doğrulanmadı; soru kalitesinin veya gerçek sınavla eşdeğerliğin kanıtı olarak kullanılmadı.
