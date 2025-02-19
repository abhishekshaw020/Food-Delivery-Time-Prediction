FROM python:3.11
WORKDIR /food_delivery
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 8080
CMD ["python", "app.py"]
