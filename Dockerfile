FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y bash curl

COPY downloadmeshroom.sh downloadmeshroom.sh

RUN /bin/bash ./downloadmeshroom.sh

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
