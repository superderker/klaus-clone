FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    exuberant-ctags \
    && rm -rf /var/lib/apt/lists/*

COPY . /klaus
WORKDIR /klaus

RUN pip install --no-cache-dir .

RUN git config --global --add safe.directory '*'

EXPOSE 80
ENTRYPOINT ["klaus"]
CMD ["--host", "0.0.0.0", "--port", "80"]
