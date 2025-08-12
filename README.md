Python のパッケージを内部用に配信するためのサンプル実装

※この実装はほとんどの実装を Claude を使用しています。

## 構成

- example/main.py: pkgfoo, pkgbar を呼び出すコード
- pkgfoo: pkgfoo のパッケージ。 `foo(val: string)` という関数を呼び出すことができる。
- pkgbar: pkgbar のパッケージ。 `bar()` という関数を呼び出すことができる。pkgfoo の foo 関数を内部で使用している。

## セットアップ方法

### 必要条件

- Python 3.13.6 (asdf などのツールでバージョン管理)

### セットアップ手順

1. リポジトリをクローンする

   ```bash
   git clone <repository-url>
   cd python-internal-package-example
   ```

2. Python バージョンを確認・設定する

   ```bash
   python --version  # 3.13.6 であることを確認
   ```

3. 各パッケージを開発モードでインストールする

   ```bash
   # pkgfoo パッケージをインストール
   cd pkgfoo
   pip install -e .
   cd ..

   # pkgbar パッケージをインストール
   cd pkgbar
   pip install -e .
   cd ..
   ```

4. サンプルアプリケーションを実行する
   ```bash
   python example/main.py
   ```

### パッケージの依存関係

- pkgbar は pkgfoo に依存している
- インストール順序は pkgfoo → pkgbar の順で行うことを推奨
