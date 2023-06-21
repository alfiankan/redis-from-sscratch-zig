FROM python:3.10.6

ENV PYTHONUNBUFFERED 1

RUN python -m pip install poetry

WORKDIR /workspace

COPY . .

ENV PATH="/root/.local/bin:$PATH"

RUN poetry config virtualenvs.create false && poetry lock --no-update && poetry install

ENTRYPOINT ["poetry", "run", "python", "main.py"] 

EXPOSE 6379/tcp
