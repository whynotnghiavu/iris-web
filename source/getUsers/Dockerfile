FROM python:3.9

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app
COPY main.py .

# Copy wait-for-it.sh
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

ENV SERVER_IP=0.0.0.0

# Run the application using wait-for-it.sh to wait for the database
CMD ["/wait-for-it.sh", "db:5432", "--", "python", "main.py"]
