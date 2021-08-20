docker build -t testapp ./webapp
kubectl apply -f ./flask.yaml
kubectl get
kubectl port-forward flask-service 8000:8000