FROM python
WORKDIR /opt
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /opt/results
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt
COPY ./calcpicelery /opt/calcpicelery
COPY ./main.py /opt/main.py
COPY ./monitoring.py /opt/monitoring.py
COPY ./shema.py /opt/shema.py

CMD ["/usr/bin/supervisord", "-n"]
