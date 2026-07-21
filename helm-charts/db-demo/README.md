## Deploy DB Demo with Helm

### Prerequisites

- Kubernetes cluster (Minikube, AKS, EKS, GKE, etc.)
- Helm 3.x

### Install

```bash
git clone https://github.com/aussiearef/NewRelicOne.git

cd NewRelicOne/"Helm charts"/db-demo

helm install db-demo .
```

### Verify

```bash
kubectl get pods
kubectl get svc
```

### Uninstall

```bash
helm uninstall db-demo
```