FROM python:3.12.6

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "ArtI/manage.py", "runserver", "0.0.0.0:8000"]
