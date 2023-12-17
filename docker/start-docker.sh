#!/bin/bash

IMAGE_NAME="test-image:v1"
# プロジェクトのルートディレクトリへのパスを設定
PROJECT_PATH=$(cd $(dirname $0)/..; pwd)

# イメージのビルド
docker image build -t "$IMAGE_NAME" .

# コンテナの作成　プロジェクトパスにバインド
docker run -it -v ${PROJECT_PATH}:/home "$IMAGE_NAME" /bin/bash
