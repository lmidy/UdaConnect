FROM python:3.8

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt


COPY . /app

RUN python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location.proto

EXPOSE 5004

CMD ["python", "main.py"]