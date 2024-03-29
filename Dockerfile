FROM python:3.7

ADD . /
RUN pip install -r requirements.txt

RUN python setup.py build_ext --inplace

EXPOSE 8090
ENTRYPOINT ["python", "app.py"]
