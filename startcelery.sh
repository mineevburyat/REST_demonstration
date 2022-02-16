#!/bin/sh
cd /opt
celery -A calpicelery worker -l info -c 4