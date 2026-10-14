# PCD-S15 GKE ağırlıklı karma sınav

50 soru · 120 dakika kişisel çalışma hedefi · 47 tek seçim + 3 çift seçim.

14 Ekim 2026. S13 tarzında İngilizce senaryolar ve yakın alternatifler. 38 SkillCertPro uyarlaması ve kaynakta sınırlı kalan konular için 12 resmî belge temelli tamamlayıcı soru. Bu konu dağılımı senin aktardığın deneyimlere göre hazırlanmıştır; gerçek sınav dağılımı tahmini değildir.

GKE 20; CI/CD 7; Workflows 5; Workstations 4; Buildpacks 3; Eventarc 3; Gemini 2; veri 4; Identity Platform 1; Cloud Tasks 1. GKE sayımı, GKE bağlamındaki geliştirici araçları ve gözlemlenebilirlik kararlarını da içerir.

Çift seçim: Q09, Q26, Q43. Tam doğru küme 1 puan; kısmi puan yok. Diğerlerinde tek seçenek.

İlk turda ayrı cevap anahtarını açma. Cevapları `1-b, 2-a+c` şeklinde gönderebilirsin. Kararsız kaldığın ikinci seçenek isteğe bağlı.

Başlangıç: ____ · Bitiş: ____ · Mola: ____ · Ek süre/yardım: ____

## Bölüm 1 Sorular 1 ile 10

### Question 01

Your application running on a GKE Standard cluster exports a custom business metric to Cloud Monitoring, and you want a HorizontalPodAutoscaler to scale the Deployment based on that metric. You configured the HPA to reference the custom metric, but it reports an unavailable metric value and never scales on it, while CPU-based scaling on the same cluster works correctly. The custom metric name is correct, its Cloud Monitoring data is present, and the adapter identity already has the required read permissions. No custom metrics adapter is installed. What should you do to enable scaling on the Cloud Monitoring metric?

**Select ONE answer.**

**A.** Deploy the Custom Metrics Stackdriver Adapter to the cluster so the HPA controller can read the metric from Cloud Monitoring through the custom and external metrics API.

**B.** Increase the metrics-server resource limits so that it can scrape the additional custom metric from each Pod.

**C.** Reconfigure the application to write the metric to standard output as structured JSON, create a logs-based metric, and point the HPA resource block directly at the Cloud Logging sink so the controller polls it each sync interval.

**D.** Switch the HPA manifest to apiVersion autoscaling/v1 and add the custom metric under targetCPUUtilizationPercentage.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 02

Your team has deployed a new version of an application to GKE, but users are reporting errors. You need to quickly revert to the previous working version while minimizing user impact. The Deployment history shows multiple revisions. The immediately preceding revision is the known good version, and no GitOps controller is reverting emergency changes. What is the fastest method to accomplish this using kubectl?

**Select ONE answer.**

**A.** Run kubectl scale deployment/my-app --replicas=0, update the manifest, then scale back up.

**B.** Run kubectl rollout history deployment/my-app, then run kubectl set image deployment/my-app container=previous-image:tag.

**C.** Run kubectl delete deployment my-app, then run kubectl apply -f previous-deployment.yaml.

**D.** Run kubectl rollout undo deployment/my-app to automatically roll back to the previous revision.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 03

You are developing an application with Cloud Firestore that needs to update 200 product documents with new pricing information. You do not need to read any documents or make decisions based on current values. You want to minimize latency and avoid transaction contention. All 200 updates must commit together or none must take effect, and the batch is within request-size limits. What should you do?

**Select ONE answer.**

**A.** Use a Firestore transaction to read all 200 documents first, then write the updated prices to ensure consistency.

**B.** Use the bulk writer with the 500/50/5 rule to gradually ramp up parallel writes for large batch operations.

**C.** Execute 200 individual update operations in parallel using Promise.all() to maximize throughput.

**D.** Use a batched write to group the update operations and commit them atomically without reading documents.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 04

You are configuring a Cloud Build pipeline for a Python application. Your integration tests generate JUnit XML test reports that your team needs to analyze after builds complete. You want to persist these test results outside of the build environment following Google-recommended best practices. The reports must be retained after successful builds; preserving reports from failed builds is handled separately. What should you do?

**Select ONE answer.**

**A.** Configure the Cloud Build ‘artifacts‘ section with an ‘objects‘ block specifying a Cloud Storage bucket location and the paths to the test report XML files.

**B.** Use Cloud Logging to write the test results by configuring the test framework to output results to STDOUT during the build step.

**C.** Configure a custom volume in the build step and mount it to persist test results across build steps and after the build completes.

**D.** Write the test results to /workspace/test_results and configure the build to automatically persist all files in /workspace to Cloud Storage.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 05

An incident affects several microservices that together make up one customer-facing application; the services are registered to an application managed in an app-enabled folder with App Hub. You want a single Gemini Cloud Assist investigation that reasons across the entire application rather than one resource at a time. The organization has access to the investigations offering and the operator has the required permissions. What should you do?

**Select ONE answer.**

**A.** Run a separate project-level investigation for each underlying service and then manually correlate the observations and hypotheses across all of the individual reports yourself.

**B.** Run the investigation against a regional log bucket so it captures all of the application‘s services.

**C.** Run an application-level Gemini Cloud Assist investigation from Cloud Hub for the App Hub application.

**D.** Run one Gemini Cloud Assist investigation that spans multiple projects at once by listing every project as a resource.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 06

A Cloud Run source deployment uses Google buildpacks. An approved build step needs a documented, non-secret build-time environment variable to control how assets are compiled. Setting the variable only on the running service changes application behavior but leaves the compiled assets unchanged. Which configuration supplies it at the required phase?

**Select ONE answer.**

**A.** Use only --set-env-vars on the service because runtime variables are inherited by every Cloud Build step.

**B.** Use the source deployment build environment configuration, such as --set-build-env-vars, when creating the new build.

**C.** Set the value on the Cloud Run revision after it is deployed so the existing image is rebuilt in place.

**D.** Grant the build identity Cloud Run Invoker so it can read environment variables from running instances.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 07

You are implementing a canary deployment strategy for a Cloud Run service using Cloud Deploy. This is the first time deploying the application to the target environment. The canary deployment is configured with 10%, 50%, and 75% traffic phases before the stable phase. What behavior should you expect during this first deployment?

**Select ONE answer.**

**A.** Cloud Deploy skips the canary phases and deploys directly to the stable phase at 100%, because there is no existing revision to split traffic with.

**B.** Cloud Deploy prompts you to manually advance through each canary phase, waiting for your approval to create the initial baseline revision.

**C.** Cloud Deploy creates placeholder revisions at each percentage phase and proceeds through all configured canary phases before reaching stable.

**D.** Cloud Deploy fails the deployment with an error indicating that canary deployments require an existing stable revision in the target environment.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 08

Your company is deploying a web application on GKE that needs to be accessible only from within your organization‘s VPC network. The application requires HTTP(S) load balancing with URL-based routing to multiple backend services. You need to configure the Ingress resource to deploy the appropriate load balancer type. What should you do?

**Select ONE answer.**

**A.** Use spec.ingressClassName: ‘gce-internal‘ in the Ingress manifest instead of annotations to deploy an internal Application Load Balancer.

**B.** Create a Service of type LoadBalancer with the annotation networking.gke.io/load-balancer-type: ‘Internal‘ to expose the application internally.

**C.** Add the annotation kubernetes.io/ingress.class: ‘gce-internal‘ to the Ingress manifest to deploy an internal Application Load Balancer.

**D.** Add the annotation kubernetes.io/ingress.class: ‘gce‘ to the Ingress manifest to deploy an external Application Load Balancer with firewall rules limiting access to internal IPs.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 09

A Workflows execution retrieves pricing and stock information from independent HTTP services. A final decision needs both responses. Each branch must write its result into a variable initialized in the parent scope, and the final decision must run only after both branches finish. Which TWO elements should be configured?

**Select TWO answers.**

**A.** Place the independent calls in branches of a parallel step and put the final decision after that parallel step.

**B.** Give the two branches identical step names so one branch automatically waits for the other.

**C.** Add both parent result variables to the parallel step shared list so the branches may assign them.

**D.** Use a single Cloud Tasks queue with concurrency two, which provides the workflow with both response bodies.

**E.** Define the results only as branch-local variables and reference them directly from the parent after the parallel step.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 10

Your team uses Cloud Build triggers to automatically deploy container images to Cloud Run when commits are pushed to your GitHub repository. You want to ensure each deployed revision can be traced back to its source code commit for debugging and audit purposes. How should you configure your cloudbuild.yaml file to accomplish this?

**Select ONE answer.**

**A.** Create a custom script in your cloudbuild.yaml that queries the GitHub API to retrieve the commit SHA and passes it to subsequent build steps through environment variables.

**B.** Configure your Cloud Build trigger to use webhook events with a custom payload that includes the commit SHA as a trigger substitution.

**C.** Tag the container image with the $COMMIT_SHA substitution variable in your cloudbuild.yaml file. Use the same tag when pushing to Artifact Registry and deploying to Cloud Run.

**D.** Configure your build steps to tag images with the current timestamp using $BUILD_ID and store the Git SHA in a separate metadata file in Cloud Storage.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 2 Sorular 11 ile 20

### Question 11

You are optimizing a Cloud Build pipeline that builds Docker images for a Node.js application. The builds are currently slow because Docker rebuilds all layers each time, even when only the application code changes. The Dockerfile has not changed in months, and most build time is spent downloading npm dependencies. You want to speed up subsequent builds while keeping the pipeline configuration simple. The Dockerfile copies the unchanged package manifest and lockfile and installs dependencies before copying application source. A previously built cache image exists. What should you do?

**Select ONE answer.**

**A.** Configure a persistent disk attached to Cloud Build workers to store the Docker build cache across multiple build executions.

**B.** Configure the cloudbuild.yaml to pull a previously built image from Artifact Registry and use the --cache-from argument with docker build to reuse unchanged layers from the cached image.

**C.** Store the node_modules directory in a Cloud Storage bucket and copy it into the build context at the start of each build using a gcloud storage cp step.

**D.** Increase the Cloud Build machine type to E2_HIGHCPU_32 to download and install npm dependencies faster during each build execution.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 12

A workflow successfully reserves inventory and then calls an idempotent pricing endpoint. Pricing sometimes returns HTTP 503, but repeating the inventory reservation would create a second reservation. The pricing endpoint is safe to repeat. You want a bounded retry with increasing delays that preserves the completed reservation. What should you configure?

**Select ONE answer.**

**A.** Retry the entire workflow execution whenever any step fails, including the inventory reservation.

**B.** Catch the 503 and return a successful workflow result without obtaining a price.

**C.** Attach a retry policy with an appropriate predicate, maximum retries, and exponential backoff to the pricing call only.

**D.** Increase the HTTP timeout indefinitely so pricing failures never reach the workflow.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 13

Your application running on GKE experiences intermittent connection failures to Memorystore for Redis during instance scaling and maintenance operations. You need to implement a resilient connection strategy that minimizes application disruptions. What should you do?

**Select ONE answer.**

**A.** Enable Memorystore AUTH and in-transit encryption to establish persistent connections that survive instance maintenance events without requiring reconnection logic.

**B.** Configure the GKE cluster to use a Memorystore read replica as the primary endpoint, and failover to the primary node only when the replica is unavailable.

**C.** Deploy multiple Basic Tier Memorystore instances and implement client-side sharding to distribute load, reducing the impact when any single instance undergoes maintenance.

**D.** Implement retry logic with exponential backoff in your application code to handle temporary connection failures, and configure a connection pool to efficiently manage Redis connections.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 14

Your organization is migrating an order processing system to Cloud Tasks. The Cloud Tasks queue dispatches tasks to a Cloud Run function that updates inventory in Cloud SQL. During testing, you observe that some inventory updates are being processed multiple times, causing data inconsistencies. What is the recommended approach to prevent these issues?

**Select ONE answer.**

**A.** Configure the queue with max_concurrent_dispatches set to 1 to ensure only one task is processed at a time across the entire queue.

**B.** Use a stable order identifier and atomically record that identifier together with the inventory mutation in one database transaction, treating a previously committed identifier as a successful duplicate.

**C.** Enable automatic deduplication in Cloud Tasks by setting a unique task name for each order to prevent duplicate task creation.

**D.** Set max_attempts to 1 in the queue‘s RetryConfig to prevent any retries and eliminate the possibility of duplicate processing.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 15

You are deploying a microservices application to GKE that requires database credentials and API keys. Your security team mandates that sensitive data must be encrypted at rest and access must be controlled through IAM policies. You also need to audit when secrets are accessed. What should you do?

**Select ONE answer.**

**A.** Store the secrets in Secret Manager and use Workload Identity Federation for GKE to authenticate your application to access them via the Secret Manager API. Enable the relevant Data Access audit logs for secret access.

**B.** Create Kubernetes Secrets with the data encoded in base64 and enable application-layer secrets encryption with Cloud KMS on your GKE cluster.

**C.** Store the credentials in ConfigMaps and restrict access using Kubernetes RBAC policies on the namespace.

**D.** Store the secrets as environment variables directly in your Deployment manifests and encrypt the manifests using Cloud KMS before storing them in your Git repository.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 16

You are configuring an Ingress resource on GKE to expose multiple services externally. Your cluster is VPC-native, and you want to take advantage of container-native load balancing for optimal traffic distribution. Backend NEGs are enabled and configured correctly; you want to avoid allocating unnecessary node ports. Which Service type should you use for the backend Services referenced by the Ingress?

**Select ONE answer.**

**A.** Use type: ExternalName for the backend Services to map directly to external DNS names for improved routing performance.

**B.** Use type: NodePort for the backend Services, as this is always required for Ingress regardless of container-native load balancing settings.

**C.** Use type: LoadBalancer for the backend Services to ensure each service has its own external IP address for the Ingress to reference.

**D.** Use type: ClusterIP for the backend Services when container-native load balancing is enabled.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 17

A developer uses a supported Python client library inside Cloud Workstations to reproduce a production authorization issue as app-runtime. The library uses ADC. Network access and app-runtime resource permissions are verified, the developer may impersonate that service account, and no environment credential file overrides ADC. The test must use app-runtime without creating a long-lived key. Which action should the developer take?

**Select ONE answer.**

**A.** Run gcloud auth login and leave the client library to use whichever personal ADC file already exists.

**B.** Export a service account JSON key to the persistent home directory and configure the library to read it.

**C.** Grant app-runtime the Cloud Workstations User role so all code in the workstation switches to that identity.

**D.** Create local ADC using gcloud auth application-default login --impersonate-service-account=app-runtime@PROJECT_ID.iam.gserviceaccount.com.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 18

Your HorizontalPodAutoscaler on a GKE Standard cluster correctly scales a Deployment out toward its maxReplicas during traffic spikes. However, many of the new Pods remain in a Pending state with FailedScheduling events indicating insufficient CPU on the existing nodes. You need the cluster to provide capacity for the additional Pods automatically. What should you do?

**Select ONE answer.**

**A.** Reduce the maxReplicas value in the HorizontalPodAutoscaler so that the Deployment never requests more Pods than the current nodes can schedule.

**B.** Enable cluster autoscaler on the node pool so that nodes are added automatically when Pods cannot be scheduled due to insufficient resources.

**C.** Lower the CPU resource requests on the Deployment‘s containers so that more Pods can be packed onto the existing nodes during traffic spikes.

**D.** Create a second HorizontalPodAutoscaler that targets the same Deployment using memory utilization so that the combined autoscalers distribute Pods more evenly across the available nodes and avoid the Pending state.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 19

A GKE Standard application normally needs 250m CPU and 512Mi memory. Load tests show peaks of 1000m CPU and 768Mi memory. Platform policy requires reserving only the normal requirement while imposing hard limits of 1000m CPU and 1Gi memory. All values are validated for this application. Which resource configuration satisfies both the reservation policy and peak requirements?

**Select ONE answer.**

**A.** Set both CPU request and limit to 1000m, and set both memory request and limit to 1Gi to ensure guaranteed QoS class.

**B.** Set no resource requests or limits and rely on GKE Autopilot to automatically determine the appropriate resource values.

**C.** Set CPU request to 250m with no CPU limit, and set both memory request and limit to 512Mi.

**D.** Set CPU request to 250m with limit of 1000m, and set memory request to 512Mi with limit of 1Gi.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 20

A platform team maintains an approved Cloud Workstations container image. Developers need more VM memory and a larger persistent home disk, while retaining exactly the same development tools. The team wants these settings managed through the workstation service rather than changes to application code. Where should it configure the machine type and home disk settings?

**Select ONE answer.**

**A.** Modify the application Deployment resource requests and limits inside the development Kubernetes cluster.

**B.** Set CPU and memory limits in the Dockerfile and increase the size of an image layer containing /home.

**C.** Add flags to the IDE launch configuration, which provisions the VM and expands its persistent disk.

**D.** Change the workstation configuration machine and persistent directory settings while retaining its container image reference.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 3 Sorular 21 ile 30

### Question 21

Your team is deploying a production application on GKE that accesses API keys from Secret Manager. The security team requires that applications always use validated and tested secret versions rather than automatically picking up new versions that might contain errors. An operator must not be able to change the secret selected by moving an alias without a corresponding release configuration change. How should you configure your application to follow Google-recommended best practices?

**Select ONE answer.**

**A.** Configure your application to always use the latest alias when accessing secrets to ensure it automatically receives the most recent credentials.

**B.** Create a custom version alias called ‘production‘ and have your application always access this alias to simplify secret management.

**C.** Reference secrets by their specific version number in your deployment configuration and update version numbers through your existing release processes.

**D.** Store secrets locally in your GKE cluster as Kubernetes Secrets and manually sync them from Secret Manager periodically to maintain control over version updates.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 22

Your team is building a loan-approval process composed of six independent HTTP services that must run in a defined order, with conditional branching based on each service‘s response. You need to define the orchestration logic in a single place, observe the execution state of every step, and avoid running any worker infrastructure while the process is idle. Which approach should you use?

**Select ONE answer.**

**A.** Deploy a Compute Engine managed instance group that runs a controller process which calls each service in order, persists the current step to a database, and evaluates branching logic from configuration files.

**B.** Publish a message to a Pub/Sub topic for each service and let each service subscribe to the previous service‘s topic.

**C.** Define the process as a Workflows workflow that calls each HTTP service in sequence and uses conditional steps for branching.

**D.** Chain the services together by having each service enqueue a Cloud Tasks task that targets the next service in the sequence.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 23

You are developing a microservice that runs on a GKE cluster, and you use VS Code with the Cloud Code plugin. While debugging a deployment issue, you want to browse the cluster‘s Pods, Deployments, and Services and stream live container logs directly from your IDE without switching to a separate terminal or the Google Cloud console. What should you do?

**Select ONE answer.**

**A.** Use the Cloud Code Kubernetes Explorer in VS Code to browse the cluster‘s resources and stream logs from the selected Pods.

**B.** Install a standalone Kubernetes dashboard add-on on the cluster, expose it through a load balancer, and open the dashboard URL in a browser tab next to VS Code to monitor resources and tail container logs.

**C.** Run repeated kubectl get and kubectl logs commands in the VS Code integrated terminal to list resources and follow the logs of each container.

**D.** Configure a Cloud Monitoring dashboard for the cluster and create log-based metrics so that you can inspect the state of each Pod and Deployment from the console.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 24

Your team is running a microservices application on a GKE cluster. You need to collect custom Prometheus metrics from your application pods and send them to Cloud Monitoring for analysis and alerting. You want to use Google‘s recommended approach with minimal operational overhead. What should you do?

**Select ONE answer.**

**A.** Install the Ops Agent on all GKE nodes and configure it to scrape Prometheus metrics from each pod‘s endpoint by specifying individual pod IPs in the agent configuration.

**B.** Create a Cloud Function that periodically queries each pod‘s metrics endpoint and writes the data to Cloud Monitoring using the custom metrics API with JSON payloads.

**C.** Enable Managed Service for Prometheus on the GKE cluster and create a PodMonitoring custom resource that specifies the metrics endpoint and scrape interval for your application pods.

**D.** Deploy and configure a self-managed Prometheus server in the cluster, then use the Prometheus remote write API to export all metrics to Cloud Monitoring every 30 seconds.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 25

A team deploys a supported Python service with gcloud run deploy --source. It expects Google buildpacks to detect the runtime, but the submitted source directory also contains an old Dockerfile and build logs show Dockerfile instructions being executed. The service no longer needs the custom Dockerfile. Which change makes the source deployment follow the intended buildpacks path?

**Select ONE answer.**

**A.** Set a runtime environment variable named USE_BUILDPACKS and keep the submitted Dockerfile unchanged.

**B.** Remove the Dockerfile from the submitted source and redeploy from source using the supported buildpacks runtime.

**C.** Deploy with --image and provide the Python source directory as the image reference.

**D.** Grant the runtime service account Artifact Registry Reader so Cloud Build ignores Dockerfile instructions.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 26

A custom Cloud Workstations image includes starter files under /home/user/project. Existing workstation configurations mount a persistent disk at /home, and developers report that the starter files are missing when the workstation starts. Existing user projects must be preserved, and defaults should be supplied only when absent. Which TWO changes implement this requirement?

**Select TWO answers.**

**A.** Store the default project files outside /home in the container image, such as under /opt/project-template.

**B.** Replace the persistent home disk with ephemeral storage so the image contents always remain visible.

**C.** Add an idempotent container startup script that copies missing defaults into the mounted home directory after user initialization.

**D.** Copy the entire template into /home during every startup with overwrite enabled, so every developer receives the latest defaults.

**E.** Add an IAM role to the workstation user so the persistent disk stops masking image directories.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 27

Your organization uses Cloud Build to run automated tests before deploying containers to GKE. You need to ensure that only images built by Cloud Build can be deployed to production clusters. The required build attestation is already generated for each eligible image; enforce the rule during ordinary admission rather than only logging violations. How should you configure deployment validation?

**Select ONE answer.**

**A.** Enable Binary Authorization and configure a policy requiring attestations from the built-by-cloud-build attestor before allowing image deployment.

**B.** Enable Artifact Analysis vulnerability scanning and configure GKE to reject images with critical vulnerabilities.

**C.** Configure Cloud Build to add a custom label to all container images and create a GKE admission controller that checks for this label during deployment.

**D.** Configure Cloud Build to push images only to a private Artifact Registry and restrict GKE to pull images only from that registry.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 28

Your team uses Cloud Workstations for development. Developers need a consistent environment that includes a specific JDK version, internal Maven repositories pre-configured, and the Cloud Code plugin pre-installed in their IDE. You want new workstation instances to start with these tools already available without requiring developers to run setup scripts after launch. What should you do?

**Select ONE answer.**

**A.** Build a custom container image that extends a Cloud Workstations base image, includes the required JDK and pre-installed Cloud Code plugin, and reference that image in the workstation configuration.

**B.** Create a workstation configuration that uses the default base image, and instruct each developer to run an initialization shell script after their first login to install the required tools.

**C.** Configure a Cloud Build trigger that runs whenever a developer creates a workstation, installs the JDK and plugin over SSH, and then notifies the developer when the environment is ready.

**D.** Use a Cloud Workstations startup metadata script defined on the workstation cluster to install the JDK and Cloud Code plugin every time the workstation starts.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 29

A frequently executed query in your Cloud Spanner application builds its SQL string by concatenating different user-supplied filter values directly into the statement text on every request. You observe that Spanner re-parses and re-plans the statement repeatedly, and a security reviewer flags the concatenation. You want to improve execution efficiency and reduce risk. What should you do?

**Select ONE answer.**

**A.** Wrap the query in a read-write transaction so Spanner persists the compiled plan for the session and reuses it for every subsequent concatenated statement.

**B.** Move the filtering logic out of SQL by reading all rows into the application and applying the user-supplied filters in memory with client-side code.

**C.** Add a STORING clause to the table‘s primary index so the query results are cached and the plan no longer needs to be recompiled for each set of values.

**D.** Rewrite the query to use bound query parameters in place of the inline literal values so Spanner can reuse the cached execution plan across requests.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 30

An Eventarc handler writes one processing charge per event into Cloud SQL. A repeated delivery of the same CloudEvent creates an additional charge even though the source object has not changed. Multiple handler instances can receive the duplicate concurrently. You need to preserve independent legitimate events while preventing duplicate charges. Which design is appropriate?

**Select ONE answer.**

**A.** Use the object filename alone as a permanent deduplication key, ignoring distinct event generations and sources.

**B.** Use the CloudEvent source and id as a stable key and atomically record that key with the charge in a database transaction.

**C.** Acknowledge the event before writing the charge and keep processed IDs only in local memory.

**D.** Limit the service to one instance and assume Eventarc will then deliver each event exactly once.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 4 Sorular 31 ile 40

### Question 31

Eventarc Standard successfully starts a workflow for each Storage event. Some workflows then fail in a downstream HTTP processing step. Operations expects Eventarc to restart each failed workflow automatically, but no replacement execution appears. Delivery to the workflow succeeded. What should the team change to recover from these downstream failures?

**Select ONE answer.**

**A.** Change the trigger event type to object-deleted so Eventarc interprets downstream failures as delivery failures.

**B.** Grant Eventarc Viewer to the workflow service account so it can request automatic replay.

**C.** Implement appropriate step retries and error handling inside the workflow, with an explicit recovery process for terminal execution failures.

**D.** Increase only the Eventarc delivery retry duration because every failed execution remains an unacknowledged event.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 32

A latency-sensitive service on GKE experiences sudden, sharp traffic spikes. Your HorizontalPodAutoscaler scales out correctly but too gradually, so Pods are overwhelmed before enough replicas are added. You want the autoscaler to add replicas more aggressively during spikes while keeping scale-down conservative. What should you do?

**Select ONE answer.**

**A.** Reduce the kube-controller-manager HPA sync period cluster-wide so the autoscaling loop evaluates metrics more frequently.

**B.** Replace the HorizontalPodAutoscaler with a CronJob that pre-scales the Deployment on a schedule, add a second HPA on memory, and configure a Cloud Monitoring alert that triggers a Cloud Function to patch the replica count.

**C.** Lower the target CPU utilization threshold to a very small value so the HorizontalPodAutoscaler keeps the Deployment running near maxReplicas at all times.

**D.** Configure the HorizontalPodAutoscaler‘s behavior.scaleUp policies in autoscaling/v2 with a higher Pods or Percent rate and a short stabilization window, while leaving scaleDown conservative.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 33

An order workflow must pause until an authorized reviewer approves it through an existing service. Approval can take hours, and the service can send an authenticated callback when the decision is ready. The workflow must retain its execution context without repeatedly polling the approval service or keeping a custom worker running. Which mechanism should it use?

**Select ONE answer.**

**A.** Keep a Cloud Run request open for the entire approval period and return only when the reviewer decides.

**B.** Create an execution-specific callback endpoint, provide it to the approval service, and use events.await_callback with an appropriate timeout.

**C.** Schedule a new workflow every minute to retrieve the approval status and reconstruct the original execution context.

**D.** Start a Cloud Composer environment solely to keep a Python polling process alive while the workflow is paused.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 34

You have a GKE cluster in project-a that needs to pull container images from an Artifact Registry Docker repository in project-b. The GKE cluster uses the Compute Engine default service account for its nodes. You want to configure access following Google-recommended security practices. What should you do?

**Select ONE answer.**

**A.** Create a new service account in project-b with Artifact Registry Reader role, export its key, and configure imagePullSecrets in GKE with the key file.

**B.** Grant the Artifact Registry Reader role on the Artifact Registry repository in project-b to the Compute Engine default service account from project-a.

**C.** Enable cross-project access on the Artifact Registry repository and configure an imagePullSecret in the GKE namespace referencing the repository credentials.

**D.** Grant the Storage Object Viewer role on project-b to the Compute Engine default service account from project-a.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 35

A workflow runs as order-orchestrator and invokes a private Cloud Run service using OIDC. The worker runs as invoice-worker and writes invoice objects to Cloud Storage. Token audience and network routing are correct. The call is rejected with an IAM permission error before worker code starts. The worker already has the required bucket access. Which permission should be added to the appropriate identity?

**Select ONE answer.**

**A.** Grant invoice-worker Cloud Run Invoker on the workflow execution resource.

**B.** Grant order-orchestrator Cloud Run Invoker on the worker service.

**C.** Grant the human who deployed the workflow Storage Object Creator on the bucket.

**D.** Grant the Eventarc service agent Storage Object Creator so it can authorize all downstream calls.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 36

You operate a multi-tenant B2B application that uses Identity Platform tenants to isolate each customer organization. Your sales team onboards several new customers each day, and you need each new customer‘s isolated identity space and its sign-in providers to be created automatically as part of your provisioning workflow, with no manual console steps. What should you do?

**Select ONE answer.**

**A.** Create a single shared tenant for all customers and separate organizations by adding a customer-id custom claim to every user.

**B.** Use the Identity Platform tenant management API through the Admin SDK to programmatically create a new tenant and configure its identity providers during your onboarding workflow.

**C.** Have an administrator create each tenant and configure its identity providers manually in the Google Cloud console as customers are onboarded.

**D.** For each new customer, run a Terraform pipeline that provisions a dedicated Google Cloud project, enables Identity Platform, configures the providers, and wires up a separate Cloud Run backend so customers are isolated at the project boundary.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 37

A container running on GKE sets a CPU request of 250m and a CPU limit of 1000m. The Deployment has a HorizontalPodAutoscaler that targets 60% average CPU utilization. Under load, each Pod consistently uses 300m of CPU. Each Pod contains only this one container, and resource metrics are healthy. What average CPU utilization value will the HorizontalPodAutoscaler use to make its scaling decision?

**Select ONE answer.**

**A.** 60%, because the HPA reports its configured target value until the next sync period recalculates the real utilization.

**B.** 30%, because the HPA calculates utilization as a percentage of the container‘s CPU limit (300m / 1000m).

**C.** 120%, because the HPA calculates utilization as a percentage of the container‘s CPU request (300m / 250m), not its limit.

**D.** 75%, because the HPA averages the CPU request and limit (625m) and reports usage relative to that midpoint.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 38

You are building container images with Cloud Build and storing them in Artifact Registry. Your integration tests, which run as a Cloud Build step, must connect to a Cloud SQL instance that only accepts traffic from internal IP addresses within your VPC. The default Cloud Build worker pool cannot reach these resources. The network team has validated a private-pool connectivity design, including the database route; ordinary peering is not being assumed to provide transitive connectivity. Which build execution environment should you configure?

**Select ONE answer.**

**A.** Create a Cloud Build private pool with the validated private network connectivity and configure the build trigger to use that worker pool.

**B.** In each Cloud Build step that needs database access, install the Cloud SQL Auth Proxy and configure it with a service account that has the Cloud SQL Admin role.

**C.** Add a firewall rule that allows ingress from 0.0.0.0/0 to your Cloud SQL instance, and continue using the default Cloud Build worker pool.

**D.** Configure a Serverless VPC Access connector in the same region as your Cloud Build trigger, and reference the connector in your cloudbuild.yaml file.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 39

Your team is developing a multi-tenant application using Cloud Firestore where each tenant has a ‘reviews‘ subcollection under their document. You need to query all reviews across all tenants where the rating equals 5 stars. The query runs in an authorized server backend. No collection-group index for this field exists yet. What must you configure before executing this query?

**Select ONE answer.**

**A.** Create a single-field or composite index with collection group scope for the ‘reviews‘ collection on the rating field.

**B.** Enable the collection group query feature in the Firestore database settings and configure security rules.

**C.** Create a root-level ‘all_reviews‘ collection and duplicate all review documents there for cross-tenant queries.

**D.** Configure a single-field ascending index for each tenant‘s reviews subcollection individually.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 40

Your team is deploying a Java application to GKE that reads configuration from a properties file. The application needs to pick up configuration changes without requiring a pod restart. You want to use a ConfigMap for this configuration and implement the simplest solution. The application can reload configuration, and a short propagation delay is acceptable; the mount must not use subPath. How should you configure the application to consume the ConfigMap?

**Select ONE answer.**

**A.** Create an immutable ConfigMap and use a rolling deployment strategy to update pods when configuration changes occur.

**B.** Inject the ConfigMap as environment variables and configure a liveness probe to detect stale configuration and trigger pod replacement.

**C.** Mount the ConfigMap as a volume at the path where your application reads the configuration file. Configure your application to watch for file changes.

**D.** Reference the ConfigMap using environment variables in the container specification. Configure a sidecar container to restart the main container when the ConfigMap changes.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

## Bölüm 5 Sorular 41 ile 50

### Question 41

A developer accidentally ran a DELETE statement that removed millions of rows from an AlloyDB for PostgreSQL cluster about 20 minutes ago. The cluster has continuous backup enabled and the pre-deletion timestamp is within its recoverable window. You need to recover the deleted data with minimal data loss while keeping the original cluster intact for investigation. What should you do?

**Select ONE answer.**

**A.** Use point-in-time recovery to restore the cluster‘s data to a new cluster at a timestamp just before the DELETE ran, then validate and reconcile the recovered rows.

**B.** Export the entire database to Cloud Storage with pg_dump, manually search the dump files for the deleted rows, recreate them with INSERT statements, and re-import the reconstructed table back into the running cluster.

**C.** Create a cross-region secondary cluster and promote it, because the secondary still retains the rows that were just deleted on the primary cluster.

**D.** Restore the most recent automated daily backup directly over the existing cluster to roll it back to the last full backup taken before the DELETE occurred.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 42

A workload on GKE handles variable request volume that maps well to CPU, so you want to scale the replica count horizontally on CPU. The per-Pod memory footprint also varies significantly between releases, and you want memory requests right-sized automatically without manual tuning. You want a managed, Google-recommended approach that avoids two controllers fighting over the same resource. The cluster meets the prerequisites, and use of the Beta multidimensional autoscaling feature is approved. What should you do?

**Select ONE answer.**

**A.** Configure a single HorizontalPodAutoscaler that targets both CPU and memory utilization, which also resizes Pod memory requests automatically.

**B.** Configure Multidimensional Pod Autoscaling so the workload scales horizontally on CPU while a vertical component right-sizes memory requests.

**C.** Configure a Vertical Pod Autoscaler in Auto mode on CPU and memory, which adds replicas once Pods reach their resource limits.

**D.** Create a HorizontalPodAutoscaler on CPU and a Vertical Pod Autoscaler in Auto mode that simultaneously adjusts both CPU and memory requests, and let the two controllers reconcile their recommendations on the same Deployment during each scaling cycle.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 43

A Cloud Storage object-finalized Eventarc trigger starts an existing workflow. The trigger uses event-starter, while the workflow runs as document-orchestrator and calls a private Cloud Run processor. Event receiver, Storage transport permissions, and network routing are already configured. Neither the workflow-start permission nor processor-invocation permission has been granted. Which TWO least-privilege grants complete this chain?

**Select TWO answers.**

**A.** Grant event-starter Workflows Invoker on the destination workflow.

**B.** Grant document-orchestrator Cloud Run Invoker on the processor service.

**C.** Grant event-starter Cloud Run Invoker on the processor instead of granting workflow-start access.

**D.** Grant the Storage service agent Project Owner so its privileges propagate through the entire chain.

**E.** Grant the human uploader Cloud Run Admin because the event uses the uploader identity for every downstream call.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 44

You are developing a Python application using Cloud Code in VS Code and want to build container images without writing a Dockerfile. The Python runtime and dependencies are supported, and the team wants a maintained source-to-image builder. What should you configure in your development environment?

**Select ONE answer.**

**A.** Enable the Cloud Build extension in VS Code which automatically containerizes applications using AI-based detection.

**B.** Write a custom shell script that invokes ‘docker build‘ with auto-generated Dockerfile contents based on file extensions.

**C.** Configure Cloud Code to use Google Cloud buildpacks, which auto-detect the language and create container images from source code.

**D.** Configure Cloud Code to use Kaniko builder which automatically generates Dockerfile from source analysis.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 45

You rotated a Secret Manager secret used by your Cloud Build pipeline by adding a new version with the latest credential. Your security policy requires that the previous version become unreadable through the Secret Manager API immediately after rotation, but you must be able to roll back to the previous version within a 7-day window in case the new credential causes build failures. Revocation of the credential at its external provider is outside this requirement. What should you do with the previous secret version?

**Select ONE answer.**

**A.** Set a 7-day expiration time on the secret resource, allowing all versions to be deleted automatically when the rollback window closes.

**B.** Disable the previous secret version immediately after rotation. If a rollback is required within 7 days, enable the version again; otherwise destroy the version after 7 days.

**C.** Destroy the previous secret version immediately after rotation, and if a rollback is needed within 7 days, recover it from the Secret Manager soft-delete recycle bin.

**D.** Leave the previous version enabled and remove the explicit version pin from cloudbuild.yaml so that Cloud Build automatically uses the newest enabled version, then delete the old version after 7 days.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 46

You are using Cloud Code for VS Code to develop a multi-service Kubernetes application. You want to improve your local development workflow by only building and deploying the frontend service you are actively working on, while still maintaining dependencies with the backend services. How should you configure your project?

**Select ONE answer.**

**A.** Create separate VS Code workspaces for each service and use VS Code‘s multi-root workspace feature to switch between frontend and backend development contexts.

**B.** Set the SKAFFOLD_BUILD_ONLY environment variable to the frontend service name before starting your debug session to limit the build scope.

**C.** Configure multiple .vscode/launch.json configurations with different container image names and manually switch between configurations when working on different services.

**D.** Define Skaffold modules in your skaffold.yaml file by naming each configuration with the metadata.name field, then select specific modules to build in the Cloud Code run configuration.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 47

A unit test that Gemini Code Assist generated for a coupon-expiration function passes on some days and fails on others. You determine that the function calls datetime.now() directly, so the test result depends on the current date. You want a reliable, deterministic test with minimal redesign. What should you do?

**Select ONE answer.**

**A.** Ask Gemini Code Assist to refactor the function so the current time is an injected parameter, and update the test to pass a fixed timestamp.

**B.** Configure the CI runner to reset its system clock to a fixed date before each run, add a wrapper that pins the timezone, and document the required clock state so developers can reproduce failures locally.

**C.** Add a retry to the failing test so it runs up to five times and passes if any attempt succeeds.

**D.** Mark the test as expected-to-fail so it no longer blocks the pipeline while still appearing in reports.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 48

Your company has deployed an internal web application on Google Kubernetes Engine behind an HTTPS load balancer. You have enabled Identity-Aware Proxy (IAP) to control access. A security audit reveals that an attacker who bypasses the load balancer could potentially forge identity headers. You need to ensure your application verifies user identities securely. What should you do?

**Select ONE answer.**

**A.** Configure VPC firewall rules to block all traffic that does not originate from the load balancer‘s IP address range.

**B.** Read the x-goog-authenticated-user-email header directly in your application to retrieve the authenticated user‘s email address for authorization decisions.

**C.** Grant the IAP-secured Web App User role only to specific users and rely on IAP‘s authentication to validate all requests.

**D.** Verify the x-goog-iap-jwt-assertion header in your application code by validating the JWT signature using Google‘s public keys and checking the audience claim.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 49

You are configuring a Cloud Monitoring alerting policy for your GKE workload that monitors container memory utilization. You want the alerting policy to create an incident only when memory utilization exceeds 85% for a sustained period, avoiding alerts from brief spikes. What configuration should you apply?

**Select ONE answer.**

**A.** Set the condition combiner to ‘All conditions are met‘ and create a second condition that checks if memory utilization has been above 85% for a minimum of 5 minutes.

**B.** Configure the alerting policy with the Missing data option set to ‘Missing data treated as values that violate the policy condition‘ to ensure all memory spikes are captured.

**C.** Set the alignment period to aggregate memory utilization over a consistent time interval. Configure a retest window duration that requires the threshold to be exceeded for multiple consecutive evaluation periods.

**D.** Configure the Rolling window function to ‘percent change‘ so that the alerting policy only triggers when memory utilization changes by more than 85% relative to the baseline.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---

### Question 50

Your security team requires that the database password used by your Cloud Build integration tests be rotated automatically every 30 days. After rotation, a Cloud Run function must call the secret-management application to generate a new password and add it as a new secret version. You want to follow Google-recommended best practices. What should you do?

**Select ONE answer.**

**A.** Configure a rotation period and next rotation time on the secret in Secret Manager, and set a topic to receive rotation notifications. Configure the Cloud Run function as a Pub/Sub subscriber to the rotation topic so it adds a new secret version when triggered.

**B.** Create a Cloud Scheduler job that runs every 30 days and invokes the Cloud Run function over HTTPS. Have the function generate a new password and call the AddSecretVersion API to add the new version.

**C.** Enable automatic key rotation on the Cloud KMS key that encrypts the Secret Manager secret. Configure an Eventarc trigger on the cryptoKeyVersions.create audit log entry to invoke the Cloud Run function to add a new secret version.

**D.** Set a Cloud KMS rotation period of 30 days on a key, and use the key to encrypt the password file in Cloud Storage. Configure a Cloud Storage notification on the encrypted object to trigger the Cloud Run function to add a new secret version.

Cevabım: ___ · Güven (isteğe bağlı): ___

Kararsız ikinci seçenek / bilmediğim kavram: ___

---
