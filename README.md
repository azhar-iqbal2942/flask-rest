# flask-rest-api

## To Run the project locally

```
docker build -t flask-rest-api .
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-rest-api sh -c "flask run --host 0.0.0.0"
```

### Course E-Book
[E-Book Link](https://rest-apis-flask.teclado.com/)
