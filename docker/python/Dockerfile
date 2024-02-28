FROM python:3.12-bullseye

# pythonの出力表示をDocker用に調整
ENV PYTHONUNBUFFERD=1

WORKDIR /src

RUN pip install poetry

# poetryの定義ファイルをコピー（存在する場合）
COPY pyproject.toml* poetry.lock* ./

# venvのファイルをプロジェクトディレクトリの下に置く（全てのプロジェクトに適用するように）
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# uvicornサーバー立ち上げ
ENTRYPOINT ["poetry", "run", "uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--reload" , "--port", "8001", "--log-config", "log_config.yml"]
