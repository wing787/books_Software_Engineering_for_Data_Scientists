FROM python:3.10

COPY requiments.txt .

RUN pip install --upgrade -r requiments.txt

COPY . .

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
