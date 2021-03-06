FROM python:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--workers=4"]