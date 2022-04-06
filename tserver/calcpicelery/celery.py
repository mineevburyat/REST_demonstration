from celery import Celery
app = Celery()

class Config:
  result_expires=3600
  task_track_started=True
  enable_utc=True
  timezone='Asia/Irkutsk'
  result_backend='rpc://'
  broker_url='pyamqp://guest@rabbitmqsrv/'
  include=['calcpicelery.tasks']

app.config_from_object(Config)

