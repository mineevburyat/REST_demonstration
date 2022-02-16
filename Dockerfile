FROM python:3.9
WORKDIR /opt
COPY ./requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt
COPY ./app /opt/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
