Python のパッケージを内部用に配信するためのサンプル実装

※この実装はほとんどの実装を Claude を使用しています。

## 構成

- example/main.py: pkgfoo, pkgbar を呼び出すコード
- pkgfoo: pkgfoo のパッケージ。 `foo(val: string)` という関数を呼び出すことができる。
- pkgbar: pkgbar のパッケージ。 `bar()` という関数を呼び出すことができる。pkgfoo の foo 関数を内部で使用している。

## セットアップ方法

### 必要条件

- Python 3.13.6 (asdf などのツールでバージョン管理)
- Google Cloud CLI (gcloud) が設定済み
- GCP Artifact Registry の Python リポジトリが作成済み

### セットアップ手順

1. リポジトリをクローンする

```bash
git clone git@github.com:tatsuyayamauchi/python-internal-package-example.git
cd python-internal-package-example
```

2. Python バージョンを確認・設定する

```bash
python --version  # 3.13.6 であることを確認
```

3. 必要なツールをインストールする

```bash
pip install build twine keyring
pip install keyrings.google-artifactregistry-auth
```

4. GCP Artifact Registry の認証を設定する

```bash
gcloud auth application-default login
gcloud config set artifacts/repository YOUR_PROJECT_ID
gcloud config set artifacts/location asia-northeast1
```

# Artifact Registry の認証を設定

```bash
python -m keyring --list-backends

gcloud artifacts print-settings python --project=YOUR_PROJECT_ID \
   --repository=YOUR_REPO_NAME \
   --location=asia-northeast1
```

5. 各パッケージの wheel を作成し、Artifact Registry にアップロードする

```bash
# pkgfoo パッケージをビルド・アップロード
cd pkgfoo
python -m build
python -m twine upload --repository-url https://asia-northeast1-python.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME dist/\*
cd ..

# pkgbar パッケージをビルド・アップロード
cd pkgbar
python -m build
python -m twine upload --repository-url https://asia-northeast1-python.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/ dist/*
cd ..
```

6. Artifact Registry からパッケージをインストールする

```bash
# Artifact Registry からパッケージをインストール
pip install --index-url https://asia-northeast1-python.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/simple/ \
   --trusted-host asia-northeast1-python.pkg.dev \
   pkgfoo pkgbar
```

7. サンプルアプリケーションを実行する

```bash
python example/main.py
```

## GCP Artifact Registry の設定

### リポジトリの作成

```bash
# Python リポジトリを作成
gcloud artifacts repositories create YOUR_REPO_NAME \
    --repository-format=python \
    --location=asia-northeast1 \
    --description="Internal Python packages"
```

### .pypirc ファイルの設定 (オプション)

ホームディレクトリに `.pypirc` ファイルを作成すると、twine の設定が簡単になります：

```ini
[distutils]
index-servers = artifact-registry

[artifact-registry]
repository = https://asia-northeast1-python.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/
```

設定後は以下のようにアップロードできます：

```bash
twine upload --repository artifact-registry dist/*
```

### パッケージの依存関係

- pkgbar は pkgfoo に依存している
- インストール順序は pkgfoo → pkgbar の順で行うことを推奨
