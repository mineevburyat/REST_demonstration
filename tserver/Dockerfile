FROM python
WORKDIR /opt
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /opt/results
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt
COPY ./gen-py /opt/gen-py
COPY ./calcpicelery /opt/calcpicelery
COPY ./tserver.py /opt/tserver.py
EXPOSE 9000
EXPOSE 9001
ENTRYPOINT ["/usr/bin/supervisord", "-n"]
# ENTRYPOINT ["celery", "-A", "calcpicelery", "worker", "-l", "info"]
# ENTRYPOINT [ "/bin/bash" ]
#docker build -t tserver .
#docker run -d -p 9000:9000 --rm  tserver