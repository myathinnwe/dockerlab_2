FROM python:3.8-slim

WORKDIR /app

COPY app-env.py /app

RUN pip install --no-cache-dir Flask

ARG PORT

ENV PORT=$PORT

EXPOSE $PORT

CMD ["python", "app-env.py"]
