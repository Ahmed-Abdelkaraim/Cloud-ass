FROM python:3-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir   nltk 
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["python","main.py"]
