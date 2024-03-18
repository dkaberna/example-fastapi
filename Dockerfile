FROM python:3.12.2

# Optional cmd
# where it will run from
WORKDIR /usr/src/app

# will place it within WORKDIR
COPY requirements.txt ./ 

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy everything in current directory into current directory in container (i.e., WORKDIR)
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]