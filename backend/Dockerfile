FROM python as prepare

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./main.py /app/main.py

ARG INNER_BACKEND_HTTP_SERVER_PORT
EXPOSE ${INNER_BACKEND_HTTP_SERVER_PORT}

ARG INNER_BACKEND_WS_SERVER_PORT
EXPOSE ${INNER_BACKEND_WS_SERVER_PORT}

FROM prepare as production
COPY ./src /app/src
#  3001 should be taken from INNER_BACKEND_HTTP_SERVER_PORT env var
CMD uvicorn main:app --host 0.0.0.0 --port 3001


FROM prepare as development
# 3001 should be taken from INNER_BACKEND_HTTP_SERVER_PORT env var
CMD MODE='migration' python main.py; MODE='mock' python main.py; uvicorn main:app --reload --host 0.0.0.0 --port ${SERVER_PORT}
