import dagshub
import mlflow

mlflow.set_tracking_uri('https://dagshub.com/VijayBSN/mini-project.mlflow')
dagshub.init(repo_owner='VijayBSN', repo_name='mini-project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

  