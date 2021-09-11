**Note:**
- For the screenshots, you can store all of your answer images in the `answer-img` directory.
- because i using new MackBook pro (M1), i have Kubernetes through docker desktop. but i have issue with prometheus node
exporter. so i solve this issue by setup prometheus via this command -> 
`helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring -f prometheus_values.yaml`

## Verify the monitoring installation
**ALl pods for the three components** -> `kubectl get po --all-namespaces`
```
NAMESPACE       NAME                                                     READY   STATUS    RESTARTS   AGE
default         backend-app-5f749755f4-ds2q7                             1/1     Running   0          8m33s
default         backend-app-5f749755f4-lkv2m                             1/1     Running   0          8m33s
default         backend-app-5f749755f4-rcpr5                             1/1     Running   0          8m33s
default         frontend-app-75cd57cfd-j6pt5                             1/1     Running   0          8m33s
default         frontend-app-75cd57cfd-wv567                             1/1     Running   0          8m33s
default         frontend-app-75cd57cfd-x8r6p                             1/1     Running   0          8m33s
default         trial-app-6cd98d67f4-75swj                               1/1     Running   0          8m32s
default         trial-app-6cd98d67f4-cgcqt                               1/1     Running   0          8m32s
default         trial-app-6cd98d67f4-kflbr                               1/1     Running   0          8m32s
kube-system     coredns-558bd4d5db-9v5p4                                 1/1     Running   0          24m
kube-system     coredns-558bd4d5db-kxwmp                                 1/1     Running   0          24m
kube-system     etcd-docker-desktop                                      1/1     Running   0          24m
kube-system     kube-apiserver-docker-desktop                            1/1     Running   0          24m
kube-system     kube-controller-manager-docker-desktop                   1/1     Running   0          24m
kube-system     kube-proxy-gqz7r                                         1/1     Running   0          24m
kube-system     kube-scheduler-docker-desktop                            1/1     Running   0          24m
kube-system     storage-provisioner                                      1/1     Running   0          23m
kube-system     vpnkit-controller                                        1/1     Running   0          23m
monitoring      alertmanager-prometheus-kube-prometheus-alertmanager-0   2/2     Running   0          17m
monitoring      prometheus-grafana-6cbd5c4995-7bz54                      2/2     Running   0          18m
monitoring      prometheus-kube-prometheus-operator-85c8b795-7sjsw       1/1     Running   0          18m
monitoring      prometheus-kube-state-metrics-76f66976cb-5qjhj           1/1     Running   0          18m
monitoring      prometheus-prometheus-kube-prometheus-prometheus-0       2/2     Running   0          17m
monitoring      prometheus-prometheus-node-exporter-f24hf                1/1     Running   0          18m
observability   jaeger-operator-dbf5767c-b2p46                           1/1     Running   0          12m
```

**All services for the three components** -> `kubectl get svc --all-namespaces`
```
NAMESPACE       NAME                                                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                        AGE
default         backend-service                                      LoadBalancer   10.111.17.141    localhost     80:31797/TCP                   9m16s
default         frontend-service                                     LoadBalancer   10.110.4.134     localhost     8080:32390/TCP                 9m15s
default         kubernetes                                           ClusterIP      10.96.0.1        <none>        443/TCP                        24m
default         trial-service                                        LoadBalancer   10.104.238.44    <pending>     8080:31790/TCP                 9m14s
kube-system     kube-dns                                             ClusterIP      10.96.0.10       <none>        53/UDP,53/TCP,9153/TCP         24m
kube-system     prometheus-kube-prometheus-coredns                   ClusterIP      None             <none>        9153/TCP                       19m
kube-system     prometheus-kube-prometheus-kube-controller-manager   ClusterIP      None             <none>        10252/TCP                      19m
kube-system     prometheus-kube-prometheus-kube-etcd                 ClusterIP      None             <none>        2379/TCP                       19m
kube-system     prometheus-kube-prometheus-kube-proxy                ClusterIP      None             <none>        10249/TCP                      19m
kube-system     prometheus-kube-prometheus-kube-scheduler            ClusterIP      None             <none>        10251/TCP                      19m
kube-system     prometheus-kube-prometheus-kubelet                   ClusterIP      None             <none>        10250/TCP,10255/TCP,4194/TCP   18m
monitoring      alertmanager-operated                                ClusterIP      None             <none>        9093/TCP,9094/TCP,9094/UDP     18m
monitoring      prometheus-grafana                                   ClusterIP      10.103.124.59    <none>        80/TCP                         19m
monitoring      prometheus-kube-prometheus-alertmanager              ClusterIP      10.110.224.21    <none>        9093/TCP                       19m
monitoring      prometheus-kube-prometheus-operator                  ClusterIP      10.111.252.108   <none>        443/TCP                        19m
monitoring      prometheus-kube-prometheus-prometheus                ClusterIP      10.96.228.169    <none>        9090/TCP                       19m
monitoring      prometheus-kube-state-metrics                        ClusterIP      10.98.154.131    <none>        8080/TCP                       19m
monitoring      prometheus-operated                                  ClusterIP      None             <none>        9090/TCP                       18m
monitoring      prometheus-prometheus-node-exporter                  ClusterIP      10.105.53.88     <none>        9100/TCP                       19m
observability   jaeger-operator-metrics                              ClusterIP      10.108.130.195   <none>        8383/TCP,8686/TCP
```
-------

## Setup the Jaeger and Prometheus source
![Alt text](./answer-img/grafana-login.png?raw=true "Grafana")
![Alt text](./answer-img/grafana-data-source.png?raw=true "Grafana data source")

-------

## Create a Basic Dashboard
![Alt text](./answer-img/prometheus-dashboard-1.png?raw=true "basic-grafana")
![Alt text](./answer-img/prometheus-dashboard-2.png?raw=true "basic-grafana")

-------

## Describe SLO/SLI
Service-Level Indicator aka **SLI** is A measurement that indicates the level of performance a service is achieving. In other words, we use "SLI" to check whether "SLO" is achieved or not.

**in context of:**
- *monthly uptime*, the backend services is functioning over 99.99% of time in month.
- *request response time*, the front services has API response time less than 200ms for 99.99% request
-------

## Creating SLI metrics.
for measure these SLIs we can using **Four Golden Signals** and add to it a service uptime.
1. **Latency** time taken to serve a request (measured by *ms*).
2. **Traffic** amount of stress on a system from demand (measured by *requests/second*).
3. **Saturation** overall capacity of a service like memory or CPU (measured by *percentage number*).
4. **Errors** number of requests that are failing (measured by *fixed number*).
5. **Uptime** percentage of time the service are available and functioning (measured by *percentage number*).
-------

## Create a Dashboard to measure our SLIs
![Alt text](./answer-img/dashboard.png?raw=true "dashboard")
![Alt text](./answer-img/uptime.png?raw=true "uptime")
![Alt text](./answer-img/40X-error.png?raw=true "40-x")
![Alt text](./answer-img/50X-error.png?raw=true "50-x")

-------

## Tracing our Flask App
![Alt text](./answer-img/jaeger-dashboard.png?raw=true "jaeger-dashboard")

--------

## Jaeger in Dashboards
![Alt text](./answer-img/grafana-tracing.png?raw=true "grafana-tracing")

--------

## Report Error
TROUBLE TICKET

**Name:** Post new start error

**Date:** 2021-09-11

**Subject:** MongoDB not accessible

**Affected Area:** Backend Service

**Severity:** Critical

**Description:** on backend service `/star` Endpoint need to access mongodb service to complete process of POST request, but this service
not exist on accessible and when review cluster service it also not exist on it.

--------

## Creating SLIs and SLOs
1. Services uptime should be grate than 99.99%.
2. Service HTTP response time should be less than 200ms for 99.99% responses.
3. Service HTTP request should have status code 20X for 99.99% requests.

--------

## Building KPIs for our plan
- All service uptime should be grate than 99.99%.
- Average response time to HTTP request should be less than 200ms.
- Percentage of CPU utilization should be less than 90%
- Percentage of Memory utilization should be less than 90%.

## Final Dashboard
- **CPU utilization** Cluster percentage CPU usage.
- **Memory utilization** Cluster percentage memory usage.
- **Service Uptime** Service Percentage uptime.
- **40X errors** number of requests with 40X status code.
- **50X errors** number of requests with 50X status code.
- **Backend Tracing** jaeger tracing with backend service.
- **Success Requests** number of requests with 20X status code.
- **Request duration per API** duration average per API endpoint

![Alt text](./answer-img/final-dashboard-1.png?raw=true "grafana-tracing")
![Alt text](./answer-img/final-dashboard-2.png?raw=true "grafana-tracing")