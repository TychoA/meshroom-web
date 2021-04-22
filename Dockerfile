FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev vim git && \
    pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
