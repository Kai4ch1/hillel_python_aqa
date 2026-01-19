FROM python:3.12
LABEL authors="macbookair"
WORKDIR /app
COPY . .
RUN pip install psycopg2-binary
RUN pip install assertpy
RUN pip install faker
CMD ["python", "db.py"]
