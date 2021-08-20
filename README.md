# CS3219-a2
Kubernetes Task

# Prerequisites
1. Docker Desktop with Kubernetes enabled
2. Kubectl installed


# How to deploy
1. Run `docker build -t testapp ./webapp` to build the docker image
2. Run `kubectl apply -f ./flask.yaml` to run the Kubernetes pod
3. Run `kubectl get pods` to see the status of the pod
4. Once the status is `Running` proceed to run `kubectl port-forward flask-service 8000:8000` (Make sure to leave this terminal on)
5. Visit [`localhost:8000`](http://localhost:8000) to view the webpage

# Tech Stack
1. Flask
2. Gunicorn