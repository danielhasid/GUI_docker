FROM python:3.10-slim
WORKDIR /app
COPY reqs.txt .
RUN pip install -r reqs.txt
COPY . .
# Install system dependencies
RUN apt-get update && apt-get install -y  wget unzip && \ 
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
apt install -y ./google-chrome-stable_current_amd64.deb && \
rm google-chrome-stable_current_amd64.deb && \
apt-get clean




# Install Python dependencies

CMD ["pytest"]