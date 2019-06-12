import sys
sys.path.insert(0, '../LIMEaid/LIMEaid')
import get_college_datasets as gcd
import pandas as pd

COLUMNS_TO_KEEP = ['SalaryClass', 'HCM2', 'SATVR25', 'SATVR75', 'SATMT25',
                   'SATMT75', 'SATWR25', 'SATWR75', 'ACTCM25', 'ACTCM75',
                   'ACTEN25', 'ACTEN75', 'ACTMT25', 'ACTMT75', 'ACTWR25',
                   'ACTWR75', 'PCIP01']
CHARS_WITH_PARENTHESIS = r"\(.*\)"
COMMA_STR = r","
DOLLAR_STR = "$"
DOT_ZERO_ZERO_STR = ".00"
EMPTY_STR = ""
FORMATTED_SCHOOL_NAME = 'Formatted School Name'
HYPHEN_STR = "-"
INST_NAME = 'INSTNM'
MID_CAREER_MEDIAN_SALARY = 'Mid-Career Median Salary'
SALARY = 'Salary'
SALARY_CLASS = 'SalaryClass'
SCHOOL_NAME = 'School Name'
SCHOOL_NAME_EXTRACT_1 = 'School Name Extract 1'
SCHOOL_NAME_EXTRACT_2 = 'School Name Extract 2'
SPACE_HYPHEN_SPACE_STR = r"[\s]*-[\s]*"


def clean_and_merge_college_datasets():
    """
    This function cleans and joins the two datasets
    The two datasets have a common field called School Name
    but the values are not standardized. 
    One of the datasets has School abbreviation included in the name
    along with the region name in some cases
    and there are differences in terms of special characters used
    In addition, the function also hand selects features in merged dataset
    and converts the Median Mid career mean salary into categorical type
    with three classes: Low (0), Median (1) and High (2)
    based on the salary ranges
    This will be the column used for Classification target
    """
    scorecard = gcd.get_most_recent_cohorts()
    salaries = gcd.get_salaries_by_region()

    # rename INSTNM column
    scorecard.rename(columns={INST_NAME: SCHOOL_NAME}, inplace=True)

    # formatting step 1: remove all characters within parenthesis
    salaries[SCHOOL_NAME_EXTRACT_1] = \
        salaries[SCHOOL_NAME].str.replace(CHARS_WITH_PARENTHESIS, EMPTY_STR)
    # formatting step 2: replace all commas with hyphens
    salaries[SCHOOL_NAME_EXTRACT_2] = \
        salaries[SCHOOL_NAME_EXTRACT_1].str.replace(COMMA_STR, HYPHEN_STR)
    # formatting step 3: replace all
    # (zero or more spaces-hyphen-zero or more spaces) with hyphen(no spaces)
    salaries[FORMATTED_SCHOOL_NAME] = \
        salaries[SCHOOL_NAME_EXTRACT_2].str.replace(SPACE_HYPHEN_SPACE_STR,
                                                    HYPHEN_STR)

    # format the 'Mid-Career Median Salary' column
    salaries[] = \
        salaries[MID_CAREER_MEDIAN_SALARY].str.replace(DOLLAR_STR, EMPTY_STR)
    salaries[MID_CAREER_MEDIAN_SALARY] = \
        salaries[MID_CAREER_MEDIAN_SALARY].str.replace(COMMA_STR, EMPTY_STR)
    salaries[MID_CAREER_MEDIAN_SALARY] = \
        salaries[MID_CAREER_MEDIAN_SALARY].str.replace(DOT_ZERO_ZERO_STR, EMPTY_STR)
    salaries[] = pd.to_numeric(salaries[MID_CAREER_MEDIAN_SALARY])

    # Create new column SalaryClass to make the Salary ranges into classes
    salaries[SALARY_CLASS] = 100
    salaries.loc[salaries[SALARY].between(0, 75, inclusive=False),
                 SALARY_CLASS] = 0
    salaries.loc[salaries[SALARY].between(75, 90, inclusive=True),
                 SALARY_CLASS] = 1
    salaries.loc[salaries[SALARY].between(90, 500, inclusive=False),
                 SALARY_CLASS] = 2

    # Delete rows with SalaryClass 100
    rows_to_drop = salaries[salaries['SalaryClass'] == 100].index
    salaries.drop(rows_to_drop, inplace=True)

    # rename the join column on the scorecard dataset
    scorecard.rename(columns={SCHOOL_NAME: FORMATTED_SCHOOL_NAME},
                     inplace=True)

    formatted_join = \
        pd.merge(salaries, scorecard, on=FORMATTED_SCHOOL_NAME, how='inner')

    # Keep only the required columns in the final dataframe
    final_df = formatted_join[COLUMNS_TO_KEEP]

    # replace NA values with the mean of the feature
    final_df = final_df.fillna(final_df.mean())

    return final_df


def load_college_dataset():
    """
    This function just invokes the clean and merge college dataset
    to load the final dataset and returns to the callee function
    """
    dataset = clean_and_merge_college_datasets()
    return dataset
