FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

WORKDIR /app

# CMD uvicorn main:app --host 0.0.0.0 --port 80
CMD uvicorn main:app --host 0.0.0.0 --port 80 --reload
# CMD uvicorn main:app --host 0.0.0.0 --port 80 --workers 4
