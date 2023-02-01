# Create the base image
FROM python:3.7-slim

# Change the working directory
WORKDIR /app/

# Install Dependency
COPY requirements.txt /app/
RUN pip install -r ./requirements.txt

# Copy local folder into the container
COPY app.py /app/
COPY /templates/index.html /app/templates/index.html
COPY gender_model.pkl /app/gender_model.pkl
COPY age_model.pkl /app/age_model.pkl
COPY X_test_gender.npz /app/X_test_gender.npz
COPY X_test_age.npz /app/X_test_age.npz

# Set "python" as the entry point
ENTRYPOINT ["python"]

# Set the command as the script name
CMD ["app.py"]

#Expose the post 5000.
EXPOSE 5000