# STEP 1: Pin the exact Python version
FROM python:3.13.5-slim

# STEP 2: Install Chrome and dependencies 
# (This ensures the 'computer' has a browser)
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# STEP 3: Set up your app directory
WORKDIR /app

# STEP 4: Pin your requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# STEP 5: Copy your project
COPY . .

# STEP 6: Execute
# We run Unit Tests first to follow the Test Pyramid!
CMD ["pytest", "tests/unit", "tests/test_home.py"]
