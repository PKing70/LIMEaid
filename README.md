[![Build Status](https://travis-ci.org/PKing70/LIMEaid.svg?branch=master)](https://travis-ci.org/PKing70/LIMEaid)
[![Coverage Status](https://coveralls.io/repos/github/PKing70/LIMEaid/badge.svg?branch=master)](https://coveralls.io/github/PKing70/LIMEaid?branch=master)

# LIMEaid

## Implementation of LIME for Tabular Classification Data

Local Interpretable Model-agnostic Interpretations (LIME) is a tool.

The LIMEaid team has authored their own version of LIME.

## Team Members

### Suman Bhagavathula

### Patrick King

### Javier Salido

## Data

- [Source 1: Data.gov - College Scoreboard](https://catalog.data.gov/dataset/college-scorecard)

- [Source 2: Kaggle - Where it pays to attend college](https://www.kaggle.com/smithashivakumar/college)

- Additional sources: We also evaluate additonal models using the common Iris dataset from sklearn.

## Software dependencies and license information

### Programming language

- Python version 3.6 and above

#### Python packages needed

- [NumPy](https://www.numpy.org)
- [sklearn](https://scikit-learn.org)
- [matplotlib](https://matplotlib.org/)

#### License Information

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). As a permissive license, it puts only very limited restriction on reuse and has therefore an excellent license compatibility. For detailed description of the contents of license please refer to the file [LICENSE](https://github.com/PKing70/LIMEaid/blob/master/LICENSE).

## Directory Structure

LIMEaid is organized as follows:

```

LIMEaid (master)
|     .coveragerc
|     .gitignore
|     .travis.yml
|     LICENSE
|     README.md
|     __init__.py
|     environment.yml
|     setup.py
|
|----- docs
|     |      ComponentSpec.ipynb
|     |      FunctionalSpec.md
|     |      LIMEaidTechReview.pdf
|     |      LIMEaidFinal.pdf
|
|----- examples
|     |      __init__.py
|     |      LIME_Education_ex.py
|     |      LIME_Iris_ex.py
|     |      LIME_Education_ex_notebook.ipynb
|     |      LIME_Iris_ex_notebook.ipynb
|
|----- LIMEaid
|     |      __init__.py
|     |      version.py
|     |  
|     |----- controller
|     |      |   __init__.py
|     |      |   LIMEaid.py
|     |      |   fit_sklearn_models.py
|     |
|     |----- data
|     |      |   Most-_Recent-_Cohorts-_Scorecard-_Elements.csv
|     |      |   salaries-by-region.csv
|     |
|     |----- model
|     |      |   __init__.py
|     |      |   get_college_datasets.py
|     |      |   load_college_dataset.py
|     |
|     |----- unittests
|     |      |   __init__.py
|     |      |   test_get_college_datasets.py
|     |      |   test_run_ml_models_for_college_ds.py
|     |      |   test_lime_fit.py
|     |      |   test_lime_display.py
|     |      |   test_versionpy.py
|     |
|     |----- view
|     |      |    __init__.py
|     |      |   LIMEdisplay.py
