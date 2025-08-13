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
   git clone git@github.com:tatsuyayamauchi/python-internal-package-example.git
   cd python-internal-package-example
   ```

2. Python バージョンを確認・設定する

   ```bash
   python --version  # 3.13.6 であることを確認
   ```

3. ビルドツールをインストールする

   ```bash
   pip install build
   ```

4. 各パッケージの wheel を作成する

   ```bash
   # pkgfoo パッケージのwheelを作成
   cd pkgfoo
   python -m build
   cd ..

   # pkgbar パッケージのwheelを作成
   cd pkgbar
   python -m build
   cd ..
   ```

5. 作成した wheel ファイルをインストールする

   ```bash
   # pkgfoo パッケージをインストール
   pip install pkgfoo/dist/pkgfoo-*.whl

   # pkgbar パッケージをインストール
   pip install pkgbar/dist/pkgbar-*.whl
   ```

6. サンプルアプリケーションを実行する
   ```bash
   python example/main.py
   ```

### パッケージの依存関係

- pkgbar は pkgfoo に依存している
- インストール順序は pkgfoo → pkgbar の順で行うことを推奨
