FROM python
WORKDIR /opt
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
COPY ./requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt
COPY ./main.py /opt/main.py
COPY ./shema.py /opt/shema.py
COPY ./tclient.py /opt/tclient.py
EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app",  "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
# CMD ["python", "main.py"]
#docker build -t tclient .
#docker run -d -p 8000:8000 --rm  tclient