[![Build Status](https://travis-ci.org/PKing70/LIMEaid.svg?branch=master)](https://travis-ci.org/PKing70/LIMEaid)
[![Coverage Status](https://coveralls.io/repos/github/PKing70/LIMEaid/badge.svg?branch=master)](https://coveralls.io/github/PKing70/LIMEaid?branch=master)

# LIMEaid

LIMEaid is an implementation of Local Interpretable Model-agnostic Interpretations (LIME) to help explain what machine learning classifier models are doing. LIMEaid supports explaining individual predictions for classifiers of data in tables (numpy arrays of numerical or categorical data), with a package called limeaid.

LIMEaid is based on and inspired by Marco Tulio Ribeiro's LIME work presented in [this paper](https://arxiv.org/abs/1602.04938), with his code made available [here.](https://github.com/marcotcr/lime)

LIMEaid helps explain any black box classifier (from an sklearn classifier method), with two or more classes.

For additional documentation of LIMEaid, see:

* [LIMEaid component specification](docs/ComponentSpec.ipynb)
* [LIMEaid functional specification](docs/FunctionalSpec.md)
* [LIMEaid project presentation](docs/LIMEaid_Final.pdf)

## Install

The lime package is on [PyPI](https://pypi.org/project/LIMEaid/). Simply run:

```sh
pip install limeaid
```

Or [clone](https://help.github.com/en/articles/cloning-a-repository) this repository, then run:

```sh
python setup.py install
```

## How to use

For tutorials in using LIMEaid with our provided dataset, which merges and classifies a prediction of mean, mid-career salary expectation (low, medium or high) based on where one graduated from college, see:

* [LIMEaid Educaton example code](examples/LIME_Education_ex.py)
* [LIMEaid Education notebook](examples/LIME_Education_ex_notebook.ipynb)

LIMEaid functions with other (tabular, numeric) datasources too. For a tutorial using the standard Iris dataset provided with scikit-learn, see:

* [LIMEaid Iris example code](examples/LIME_Iris_ex.py)
* [LIMEaid Iris notebook](examples/LIME_Iris_ex_notebook.ipynb)

__Important:__ 

* The Jupyter notebooks examples above _require_ the LIMEaid PyPI to be installed to run.

* The .py examples must be run from the top level LIMEaid directory:

```sh
../LIMEaid > python .\examples\LIME_Education_ex.py
```

NOTE: If you are still running into issues with module path during import, this is a known issue.
You can refer to [Issue 26](https://github.com/PKing70/LIMEaid/issues/26) which has details on the workaround that can be used.


## Data

- [Source 1: Data.gov - College Scoreboard](https://catalog.data.gov/dataset/college-scorecard)

- [Source 2: Kaggle - Where it pays to attend college](https://www.kaggle.com/smithashivakumar/college)

- Additional sources: We also evaluate additonal models using the common Iris dataset from sklearn.

## Software dependencies and license information

### Programming language

- [Python](https://www.python.org/downloads/) version 3.6 or above

#### Python packages needed

- [Graphviz](http://graphviz.org/)
- [Matplotlib](https://matplotlib.org/)
- [NumPy](https://www.numpy.org)
- [scikit-learn](https://scikit-learn.org)

#### License information

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). As a permissive license, it puts only very limited restriction on reuse and has therefore an excellent license compatibility. For detailed description of the contents of license please refer to the file [LICENSE](https://github.com/PKing70/LIMEaid/blob/master/LICENSE).

## Directory structure

LIMEaid is organized as follows:

```sh

LIMEaid (master)
|     .coveragerc
|     .gitignore
|     .travis.yml
|     __init__.py
|     environment.yml
|     LICENSE
|     README.md
|     requirements.txt
|     setup.py
|
|----- docs
|     |      ComponentSpec.ipynb
|     |      Data515TechReview.pptx
|     |      FunctionalSpec.md
|     |      LIMEaidFinal.pdf
|     |      LIMEaidFinal.pptx
|     |
|     |----- images
|     |     |     Components.png
|     |     |     Limeaid.png
|
|----- examples
|     |     __init__.py
|     |     LIME_Education_ex.py
|     |     LIME_Education_ex_notebook.ipynb
|     |     LIME_Iris_ex.py
|     |     LIME_Iris_ex_notebook.ipynb
|
|----- LIMEaid
|     |     __init__.py
|     |     version.py
|     |  
|     |----- controller
|     |     |     __init__.py
|     |     |     fit_sklearn_models.py
|     |     |     LIMEaid.py
|     |
|     |----- data
|     |     |     Most-_Recent-_Cohorts-_Scorecard-_Elements.csv
|     |     |     salaries-by-region.csv
|     |
|     |----- model
|     |     |     __init__.py
|     |     |     get_college_datasets.py
|     |     |     load_college_dataset.py
|     |
|     |----- unittests
|     |     |     __init__.py
|     |     |     test_get_college_datasets.py
|     |     |     test_lime_display.py
|     |     |     test_lime_fit.py
|     |     |     test_run_ml_models_for_college_ds.py
|     |     |     test_versionpy.py
|     |
|     |----- view
|     |     |     __init__.py
|     |     |     LIMEdisplay.py
```

## Team members

* [Suman Bhagavathula](mailto:sumanbh@uw.edu)

* [Patrick King](mailto:pking70@uw.edu)

* [Francisco Javier Salido Magos](mailto:javiers@uw.edu)
