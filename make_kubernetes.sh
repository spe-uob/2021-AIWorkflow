#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied -- check what kubectl contexts you have (kubectl config get-contexts) and use that (kubectl config set-context <context>)"
    exit 1
fi
kubectl config use-context $1
kubectl apply -f backend-service.yaml,backend-deployment.yaml,frontend-tcp-service.yaml,frontend-deployment.yaml,database-claim0-persistentvolumeclaim.yaml,database-deployment.yaml,database-service.yaml
kubectl get pods
exit 0