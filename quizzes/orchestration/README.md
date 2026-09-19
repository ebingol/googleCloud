# Orchestration — 8 quiz / 40 soru

Klasörde tek PDF var: Introduction to Microservices (16 sayfa). O01 setleri bu PDF’ye dayanır. OQ setleri paylaştığın Choreography and Orchestration quizini ve cevaplarda bağlantısı verilen resmî dokümanları esas alır; eksik bir ders PDF’sinin sayfa referansı varmış gibi gösterilmez.

Önerilen sıra: O01-01 → O01-04, ardından OQ-01 → OQ-04. Eventarc önceliğinse doğrudan OQ-04 ile başlayabilirsin.

## Setler

| Quiz | Konu | Sorular | Cevaplar |
|---|---|---|---|
| O01-01 | Monoliths, SOA and the Enterprise Service Bus | [Çöz](O01-01.md) | [Kontrol et](../answers/orchestration/O01-01.md) |
| O01-02 | Microservice boundaries and choosing a starting architecture | [Çöz](O01-02.md) | [Kontrol et](../answers/orchestration/O01-02.md) |
| O01-03 | Development, technology choice and independent scaling | [Çöz](O01-03.md) | [Kontrol et](../answers/orchestration/O01-03.md) |
| O01-04 | Operational burden, network latency, testing and debugging | [Çöz](O01-04.md) | [Kontrol et](../answers/orchestration/O01-04.md) |
| OQ-01 | Cloud Tasks: delivery, scheduling, destinations and identity | [Çöz](OQ-01.md) | [Kontrol et](../answers/orchestration/OQ-01.md) |
| OQ-02 | Choreography versus orchestration | [Çöz](OQ-02.md) | [Kontrol et](../answers/orchestration/OQ-02.md) |
| OQ-03 | Workflows: execution state and long-running coordination | [Çöz](OQ-03.md) | [Kontrol et](../answers/orchestration/OQ-03.md) |
| OQ-04 | Eventarc Standard: CloudEvents, Audit Logs and Pub/Sub | [Çöz](OQ-04.md) | [Kontrol et](../answers/orchestration/OQ-04.md) |

## Paylaşılan sonuç: %75 (3/4)

- Cloud Tasks, choreography ve Workflows soruları başarılı. Bu sonuçlardan güven düzeyi çıkarılmadı.
- Eventarc: serbest format seçeneği yanlış işaretlenmiş; Cloud Audit Logs doğru seçilmiş. Eksik kalan doğru seçenek Pub/Sub taşıma katmanıdır (Eventarc Standard kapsamı).
- Tekrar odağı: CloudEvents = olay formatı, Pub/Sub = taşıma, Audit Logs = olası kaynak; uygulamanın Eventarc kuyruğunu poll etmesi gerekmez.

## Kaynak ayrımı ve belirsizlik

Cloud Tasks sorusundaki işaretlenmeyen token seçeneği için yanlış geri bildirimi paylaşılmamış. Bunu otomatik olarak yanlış kabul etmiyoruz. Resmî doküman kimlikli HTTP task çağrılarını destekler. Token için yapılandırılan service account ile Cloud Tasks service agent’ın işlevi ayrılmalıdır. Bu yüzden belirsiz seçeneği aynen yeni select-two sorusuna taşımadık.

[HTTP task kimlik doğrulaması](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks) · [Eventarc Standard](https://docs.cloud.google.com/eventarc/standard/docs/overview) · [CloudEvents](https://docs.cloud.google.com/eventarc/docs/cloudevents)

[Paylaştığın orijinal sonuç metni](../orchestration-quiz-results.txt) · [Tüm quizler](../README.md)
