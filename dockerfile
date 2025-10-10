FROM  python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -e .

EXPOSE 5000

ENV FLASk_APP=application.py


CMD [ "python" , "application.py"]

