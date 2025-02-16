
FROM ubuntu:latest

# Install required dependencies
RUN apt-get update && apt-get install -y wget curl unzip socat python3 python3-pip

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable

# Copy flag file
RUN echo "MAGNUS{r3mo4e_de3u8g4ng_p0rt}" > /flag

# Start Chrome with remote debugging enabled
CMD ["google-chrome", "--remote-debugging-port=13370", "--disable-gpu", "--headless=new", "--no-sandbox", "google.com"]
