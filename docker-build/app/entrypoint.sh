#!/usr/bin/env bash

set -e

echo "start entrypoint"
alembic upgrade head
echo "DONE"

exec "$@"
