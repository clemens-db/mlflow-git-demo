import mlflow

with mlflow.start_run():
    mlflow.log_metric('test', 0.1)
