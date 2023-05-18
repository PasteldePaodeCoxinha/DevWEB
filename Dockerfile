FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

COPY . .

CMD ["flask","run","--debug","--host=0.0.0.0"]