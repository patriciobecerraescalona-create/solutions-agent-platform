#!/usr/bin/env bash
set -e

cd /home/patricio/workspace/solutions-agent-platform

echo "=== DEPLOY START ==="
git pull origin main

docker compose -f infra/docker/docker-compose.yml up -d --build

echo "=== HEALTH CHECK ==="

for i in {1..10}; do
  if curl -f http://localhost:8000/health; then
    echo ""
    echo "=== DEPLOY OK ==="
    exit 0
  fi

  echo "Health check failed, retry $i/10..."
  sleep 2
done

echo "=== DEPLOY FAILED ==="
docker logs --tail=80 sap_api
exit 1
