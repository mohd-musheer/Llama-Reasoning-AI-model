#!/bin/bash

# Start llama-server in background

./llama.cpp/build/bin/llama-server \
-m ./model/llama3-q4_k_m.gguf \
-c 1024 \
-ngl 0 &

# Wait a bit for server startup
sleep 5

# Start FastAPI

uvicorn app.api:app --host 0.0.0.0 --port 8000