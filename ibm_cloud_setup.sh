REGISTRY_HOSTNAME=$1
IBM_CLOUD_API_KEY=$2
ICR_NAMESPACE=$3

kubectl create secret docker-registry --namespace=${ICR_NAMESPACE} ibmcloud-toolchain-${REGISTRY_HOSTNAME} --docker-server=${REGISTRY_HOSTNAME} --docker-password=${IBM_CLOUD_API_KEY} --docker-username=iamapikey --docker-email=a@b.com
kubectl patch serviceaccount/default -p '{"imagePullSecrets":[{"name":"ibmcloud-toolchain-${REGISTRY_HOSTNAME}"}]}' --namespace=${ICR_NAMESPACE}