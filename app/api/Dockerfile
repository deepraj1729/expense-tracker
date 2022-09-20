FROM python:3.9.0-alpine

# The source directory
WORKDIR /api

#Copy requirements
COPY requirements.txt /code/requirements.txt

#Install the required packages
RUN pip install --no-cache-dir -r /code/requirements.txt

#Copy remaining items excluding mentioned in .dockerignore
COPY . .

EXPOSE 8000
#Entrypoint
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]