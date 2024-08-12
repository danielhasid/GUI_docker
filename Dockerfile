FROM python:3.10-slim

# Set the working directory
WORKDIR /

# Copy and install Python dependencies
COPY reqs.txt .
RUN pip install -r reqs.txt

# Copy the rest of the application code
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    git && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

# Clone the GitHub repository
RUN git clone https://github.com/danielhasid/GUI_docker.git

# Set working directory to the cloned repo
WORKDIR /GUI_docker

# Run tests
CMD ["pytest"]
