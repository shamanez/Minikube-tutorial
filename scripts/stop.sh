#!/bin/bash

echo "Deleting Kubernetes resources..."
kubectl delete -f manifests/service.yaml
kubectl delete -f manifests/deployment.yaml
kubectl delete -f config/config-map.yaml

echo "Stopping Minikube..."
minikube stop