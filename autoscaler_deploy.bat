docker build -t testapp ./webapp
kubectl apply -f ./configs/flask.yaml
kubectl autoscale -n flask deployment flask-app --min=1 --max=10 --cpu-percent=50
kubectl port-forward -n flask service/flask-service 8000:8000