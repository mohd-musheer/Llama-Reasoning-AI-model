FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    cmake \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Clone llama.cpp
RUN git clone https://github.com/ggerganov/llama.cpp

# Build llama.cpp
RUN cmake -B llama.cpp/build llama.cpp \
    && cmake --build llama.cpp/build --config Release

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Make startup script executable
RUN chmod +x start.sh

# Expose FastAPI port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s \
CMD curl -f http://localhost:8000/health || exit 1

CMD ["./start.sh"]