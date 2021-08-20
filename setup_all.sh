docker build -t testapp ./webapp
kubectl apply -f ./flask.yaml
kubectl get