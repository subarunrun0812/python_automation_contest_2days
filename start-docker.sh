#!/bin/bash

IMAGE_NAME="test-image:v1"
PROJECT_PATH=$(cd $(dirname $0); pwd)
CONTAINER_NAME="my_python_container"

# イメージのビルド
docker image build -t "$IMAGE_NAME" ./docker

# 既存のコンテナを確認し、存在する場合は削除
if [ $(docker ps -aq -f name=^/${CONTAINER_NAME}$) ]; then
    docker rm -f ${CONTAINER_NAME}
fi

# コンテナの作成　プロジェクトパスにバインドし、SSHポートフォワーディングを設定
docker run -d --name ${CONTAINER_NAME} -p 2222:22 --workdir /home -v ${PROJECT_PATH}:/home "$IMAGE_NAME"
