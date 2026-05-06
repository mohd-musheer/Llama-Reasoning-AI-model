#!/bin/bash

set -e

echo "Starting llama.cpp server..."

./llama.cpp/build/bin/llama-server \
  -m ./model/llama3-q4_k_m.gguf \
  -c 1024 \
  --host 0.0.0.0 \
  --port 8080 \
  -ngl 0 > llama.log 2>&1 &

echo "Waiting for model to fully load..."

until curl -s http://127.0.0.1:8080/v1/models | grep -q "data"; do
    echo "Model still loading into memory..."
    sleep 5
done

echo "Model loaded successfully!"

echo "Starting FastAPI..."

exec uvicorn app.api:app \
    --host 0.0.0.0 \
    --port 8000