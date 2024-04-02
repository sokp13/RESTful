# Flask API
## This is a sample Flask REST API with Swagger docs.

### Building the Docker image
To build the Docker image in terminal, navigate to the directory the Dockerfile is contained in and run:

```
    docker build -t myapi .
```

This will build the image with the name "myapi".

### Running the Container
To run the Docker container, run:

```
    docker run -p 80:8080 myapi
```

This maps port 80:8080 (local host) inside the container.

Now you can access the API at: http://localhost/

And access the Swagger UI at: http://localhost/swagger

### API Reference
The Swagger UI contains full reference documentation for the API.

Some key endpoints are:

* GET –>    / "Healthcheck" endpoint
* POST –>   /access                 –> Grant access to a user
* PUT –>    /access/{name}/{server} –> Update access for user/server
* DELETE –> /access/{name}/{server} –> Revoke access

### Persisting Data
As this just runs an in-memory Python app, data will be lost when the container is stopped or restarted.

# Enhanced Microservice
### Running on Kubernetes (K8s)
Run the three commands:

```
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    kubectl apply -f configmap.yaml
```

In order to check each application, run the get command for K8s:
```
    kubectl get all
```

Now you can access the API on port 31234: http://localhost:31234/
as well as access the Swagger UI here: http://localhost:31234/swagger

The /fib and /config enhancement endpoints will be visible there.

Additionally, in a terminal window, you can curl results from the Fibonacci endpoint:
```
    curl localhost:31234/fib?length={insert number here}
```

Difficulties were persistent in deploying the Swagger-UI correctly with the RESTful endpoints. The usage of Claude.ai, and a Medium article (https://diptochakrabarty.medium.com/flask-python-swagger-for-rest-apis-6efdf0100bd7) provided a useful blueprint on how to establish GET and POST to add onto for DELETE and PUT methods.
