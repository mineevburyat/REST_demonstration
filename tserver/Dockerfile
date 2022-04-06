FROM python
WORKDIR /opt
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUN mkdir -p /opt/results
COPY ./requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt
COPY ./calcpicelery /opt/calcpicelery
COPY ./tserver.py /opt/tserver.py
COPY ./monitoring.py /opt/monitoring.py
COPY ./shema.py /opt/shema.py
EXPOSE 9000
ENTRYPOINT ["celery", "-A", "calcpicelery", "worker", "-l", "info"]
# ENTRYPOINT [ "/bin/bash" ]
#docker build -t tserver .
#docker run -d -p 9000:9000 --rm  tserver