# FastAPI
## コンテナ起動まで
### 1. リポジトリをclone

### 2. パッケージをインストール

```bash
docker compose run --rm --entrypoint "poetry run install --no-root" app
```

### 3. コンテナ作成&起動

```bash
docker compose up -d
```
## マイグレーション
### 1. appコンテナに入る

```bash
cd docker
```

```bash
docker compose exec app bash
```

### 2. マイグレーション実行

```bash
poetry run alembic upgrade head
```
