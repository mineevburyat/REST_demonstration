FROM python
WORKDIR /opt
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
COPY ./requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt
COPY ./main.py /opt/main.py
COPY ./shema.py /opt/shema.py
COPY ./tclient.py /opt/tclient.py

ENTRYPOINT ["uvicorn", "main:app", "--host 0.0.0.0", "--port 8000", "--workers 4"]
