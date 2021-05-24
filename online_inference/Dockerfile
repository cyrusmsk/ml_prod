FROM python:3.6-slim-buster
COPY requirements.txt ./requirements.txt
COPY model.pkl /model.pkl
COPY app.py /app.py

RUN apt-get update \
    && apt-get install -y git \
    && apt-get clean \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir "git+https://github.com/made-ml-in-prod-2021/cyrusmsk@Homework1#egg=heart_ml&subdirectory=ml_project"
WORKDIR .

ENV PATH_TO_MODEL="/model.pkl"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]