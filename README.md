**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

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
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
