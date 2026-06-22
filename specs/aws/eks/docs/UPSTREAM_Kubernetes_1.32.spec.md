---
id: "@specs/aws/eks/docs/UPSTREAM_Kubernetes_1.32"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "Kubernetes 1.32 API Reference"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Kubernetes 1.32 API Reference (Upstream)

EKS is a Certified Kubernetes conformant service. The EKS management plane delegates
to the Kubernetes control plane and manages the cluster lifecycle. The EKS store
emulates the AWS management API (CreateCluster, DeleteCluster, etc.) but does NOT
emulate the Kubernetes API directly. In local dev, use k3s/kind/minikube for the
actual Kubernetes API surface.

## Key Kubernetes Concepts

### Cluster Components
- **Control Plane**: API server, etcd, controller manager, scheduler
- **Worker Nodes**: kubelet, kube-proxy, container runtime
- **Networking**: CNI plugin, Service CIDR, Pod CIDR

### Kubernetes API Groups

| Group | Resources | Purpose |
|-------|-----------|---------|
| `core/v1` | Pods, Services, Nodes, Namespaces, ConfigMaps, Secrets | Core resources |
| `apps/v1` | Deployments, StatefulSets, DaemonSets, ReplicaSets | Workloads |
| `networking.k8s.io/v1` | NetworkPolicies, Ingresses | Networking |
| `rbac.authorization.k8s.io/v1` | Roles, RoleBindings | RBAC |
| `storage.k8s.io/v1` | StorageClasses, PVs, PVCs | Storage |
| `autoscaling/v1` | HorizontalPodAutoscalers | Autoscaling |

### EKS-Specific Additions
- **IAM Roles for Service Accounts (IRSA)**: Pod-level IAM via OIDC federation
- **EKS Pod Identity**: Simplified IRSA replacement
- **VPC CNI**: AWS-managed networking
- **aws-auth ConfigMap**: Maps IAM principals to k8s RBAC

## Reference

- Kubernetes API Reference: https://kubernetes.io/docs/reference/
- Kubernetes API Concepts: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
- EKS Best Practices: https://aws.github.io/aws-eks-best-practices/
