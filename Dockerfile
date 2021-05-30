FROM python:3.9.5-alpine3.13
WORKDIR /code
ENV FASTAPI_APP=app.py
ENV FASTAPI_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers make
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "wsgi.py"]
