# Use Python runtime
FROM python:3.12-slim

WORKDIR /app

# Copy project
COPY . .

# Install dependencies
RUN pip install --no-cache-dir google-adk

# Expose port
EXPOSE 8080

# Run ADK API server
CMD ["adk", "api_server", "--host", "0.0.0.0", "--port", "8080"]
