ml_project
==============================

ML project based on Kaggle competition for ML in Prod course on MADE 2021

Main idea of the work is to use Google Colab resources to make the project.
Please see the notebook to find the way how to run VSCode in Google Colab.

Project running
------------
1. Installation
python setup.py install
2. Training
python heart_ml/models/train_model.py configs/train_config.yaml
3. Predicting
python heart_ml/models/predict_model.py configs/predict_config.yaml
4. Tests
Because in Colab default pytest still based on version 2, to run tests use the following
python -m pytest tests/

Self-assessment
------------
-2) Нomework1 branch created: +1
-1) ml_project named: +0
0) Details in PR: +2
1) EDA notebook added: +2
2) Project structure: +2
3) logging system used: +2
4) tests covered: +3
5) fake test data not used: +0
6) Configurations used: +3
7) Dataclasses for configs: +3
8) Transformers from example used: +0
9) Readme details about training: +3
10) predict pipeline: +3
11) Only Click used, no Hydra: +0
12) No CI/CD for that work: +0
13) Self assessment done: +1

Result: 25


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Folder for logs.
    │   ├── processed      <- The final output dataset.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebook, which include EDA and main tool for work via Google Colab.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    │
    ├── heart_ml           <- Source code for use in this project.
    │   ├── __init__.py    <- Makes heart_ml a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py     <- Consists of pipeline definition for prediction
    │   │   └── train_model.py       <- Consists of pipeline definition for train
    │   │   └── train_model.py       <- Several functions for modelling (train, predict, read and write model)
    │   │
    │   └── entities       <- Scripts to create exploratory and results oriented visualizations
    │       └── feature_params.py           <- Dataclass for parameters for features
    │       └── split_params.py             <- Dataclass for parameters for splitting
    │       └── train_params.py             <- Dataclass for parameters for training
    │       └── train_pipeline_params.py    <- Dataclass for parameters for train pipeline
    │       └── predict_pipeline_params.py  <- Dataclass for parameters for train pipeline
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
