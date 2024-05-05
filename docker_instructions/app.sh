#!/bin/bash

cd project_dir

alembic revision --autogenerate -m "upgrade_new" && alembic upgrade head

gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
# shellcheck disable=SC2093

