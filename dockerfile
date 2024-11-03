# Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh isi folder ke dalam image
COPY . .

# Expose port untuk aplikasi
EXPOSE 5000

# Command untuk menjalankan aplikasi
CMD ["python", "app.py"]
