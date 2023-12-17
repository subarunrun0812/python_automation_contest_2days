#!/bin/bash
IMAGE_NAME="test-image:v1"
PROJECT_PATH=$(cd $(dirname $0); pwd)

# イメージのビルド
docker image build -t "$IMAGE_NAME" ./docker

# コンテナの作成　プロジェクトパスにバインド
docker run -it -v ${PROJECT_PATH}:/home "$IMAGE_NAME" /bin/bash -c "Xvfb :99 & export DISPLAY=:99 && /bin/bash"
