import sys
sys.path.insert(0, '../LIMEaid/LIMEaid')
from model import get_college_datasets as gcd
import pandas as pd


def clean_and_merge_college_datasets():
    """
    This function cleans and joins the two datasets
    """
    scorecard = gcd.get_most_recent_cohorts()
    salaries = gcd.get_salaries_by_region()

    # rename INSTNM column
    scorecard.rename(columns={'INSTNM': 'School Name'}, inplace=True)

    # formatting step 1: remove all characters within parenthesis
    salaries['School Name Extract 1'] = \
        salaries['School Name'].str.replace(r"\(.*\)", "")
    # formatting step 2: replace all commas with hyphens
    salaries['School Name Extract 2'] = \
        salaries['School Name Extract 1'].str.replace(r",", "-")
    # formatting step 3: replace all
    # (zero or more spaces-hyphen-zero or more spaces) with hyphen(no spaces)
    salaries['Formatted School Name'] = \
        salaries['School Name Extract 2'].str.replace(r"[\s]*-[\s]*", "-")

    # format the 'Mid-Career Median Salary' column
    salaries['Mid-Career Median Salary'] = \
        salaries['Mid-Career Median Salary'].str.replace("$", "")
    salaries['Mid-Career Median Salary'] = \
        salaries['Mid-Career Median Salary'].str.replace(",", "")
    salaries['Mid-Career Median Salary'] = \
        salaries['Mid-Career Median Salary'].str.replace(".00", "")
    salaries['Salary'] = pd.to_numeric(salaries['Mid-Career Median Salary'])

    # Create new column SalaryClass to make the Salary ranges into classes
    salaries['SalaryClass'] = 100
    salaries.loc[salaries['Salary'].between(0, 75, inclusive=False),
                 'SalaryClass'] = 0
    salaries.loc[salaries['Salary'].between(75, 90, inclusive=True),
                 'SalaryClass'] = 1
    salaries.loc[salaries['Salary'].between(90, 500, inclusive=False),
                 'SalaryClass'] = 2

    # Delete rows with SalaryClass 100
    rows_to_drop = salaries[salaries['SalaryClass'] == 100].index
    salaries.drop(rows_to_drop, inplace=True)

    # rename the join column on the scorecard dataset
    scorecard.rename(columns={'School Name': 'Formatted School Name'},
                     inplace=True)

    formatted_join = \
        pd.merge(salaries, scorecard, on='Formatted School Name', how='inner')

    # Keep only the required columns in the final dataframe
    columns_to_keep = ['SalaryClass', 'HCM2', 'SATVR25', 'SATVR75', 'SATMT25',
                       'SATMT75', 'SATWR25', 'SATWR75', 'ACTCM25', 'ACTCM75',
                       'ACTEN25', 'ACTEN75', 'ACTMT25', 'ACTMT75', 'ACTWR25',
                       'ACTWR75', 'PCIP01']

    final_df = formatted_join[columns_to_keep]

    # replace NA values with the mean of the feature
    final_df = final_df.fillna(final_df.mean())

    return final_df


def load_college_dataset():
    """
    This function just returns the cleaned and joined college dataset
    """
    dataset = clean_and_merge_college_datasets()
    return dataset
