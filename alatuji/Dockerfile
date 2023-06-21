FROM python:3.10.6

ENV PYTHONUNBUFFERED 1

RUN python -m pip install poetry

ENV DOCKERVERSION=18.03.1-ce
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKERVERSION}.tgz \
  && tar xzvf docker-${DOCKERVERSION}.tgz --strip 1 \
                 -C /usr/local/bin docker/docker \
  && rm docker-${DOCKERVERSION}.tgz

WORKDIR /alatuji

COPY . .

ENV PATH="/root/.local/bin:$PATH"

RUN poetry config virtualenvs.create false && poetry lock --no-update && poetry install

ENTRYPOINT ["poetry", "run", "python", "uji.py"] 
