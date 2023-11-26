FROM python as prepare

ARG BACKEND_DIR_FOR_CLI_HINTS
RUN mkdir -p ${BACKEND_DIR_FOR_CLI_HINTS}; touch ${BACKEND_DIR_FOR_CLI_HINTS}/main.py
WORKDIR ${BACKEND_DIR_FOR_CLI_HINTS}

COPY ./requirements.txt ${BACKEND_DIR_FOR_CLI_HINTS}/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ${BACKEND_DIR_FOR_CLI_HINTS}/requirements.txt

ARG INNER_BACKEND_HTTP_SERVER_PORT
EXPOSE ${INNER_BACKEND_HTTP_SERVER_PORT}

ARG INNER_BACKEND_WS_SERVER_PORT
EXPOSE ${INNER_BACKEND_WS_SERVER_PORT}

FROM prepare as production
COPY ./src ${BACKEND_DIR_FOR_CLI_HINTS}/src
COPY ./main.py ${BACKEND_DIR_FOR_CLI_HINTS}/main.py
#  3001 should be taken from INNER_BACKEND_HTTP_SERVER_PORT env var
CMD uvicorn main:app --host 0.0.0.0 --port 3001


FROM prepare as development
# 3001 should be taken from INNER_BACKEND_HTTP_SERVER_PORT env var
CMD MODE='migration' python main.py; MODE='mock' python main.py; uvicorn main:app --reload --host 0.0.0.0 --port ${SERVER_PORT}
