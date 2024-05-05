#!/bin/bash
# shellcheck disable=SC2164
cd "$PWD"
# Останавливаем контейнеры
docker rm --force work_app
docker rm --force db_app
docker rm --force kafka
docker rm --force kafka_consumer
docker rm --force zookeeper
# Собираем образы заново
docker-compose build
# Запускаем контейнеры
docker-compose up -d