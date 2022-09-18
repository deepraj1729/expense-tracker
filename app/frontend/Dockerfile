FROM python:3.9.0-alpine

# The source directory
WORKDIR /code

#Copy requirements
COPY requirements.txt /code/requirements.txt

#Install the required packages
RUN pip install --no-cache-dir -r /code/requirements.txt

#Copy the remaing files and folders
COPY ./.env /code/.env

COPY ./app /code/app

#Entrypoint
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]