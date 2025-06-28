#slim is for smaller version
FROM python:3.10-slim 
# setting working directory in a container
WORKDIR /application_portal
# copying all our project files in a container
COPY . .
# installing everything mentioned in requirements.txt to create same environment for everyone 
RUN pip install --no-cache-dir -r requirements.txt
# to tell on which port we working 
EXPOSE 8000
# tells container to start python app.py when the container starts 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
