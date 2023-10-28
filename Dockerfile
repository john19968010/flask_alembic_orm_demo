FROM python:3.10.13-slim AS build-env
RUN python -m venv /opt/venv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM gcr.io/distroless/python3-debian11
COPY --from=build-env /opt/venv /opt/venv
WORKDIR /usr/src/app/
COPY . .

ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]