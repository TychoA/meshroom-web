FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev curl tar gzip && \
    pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY downloadmeshroom downloadmeshroom

RUN /app/downloadmeshroom

COPY . .

# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]