from codebase.model import getcollegedatasets as gcd
import numpy as np
import pandas as pd


def cleanandmergecollegedatasets():
    scorecard = gcd.getmostrecentcohorts()
    salaries = gcd.getsalariesbyregion()
    
    #rename INSTNM column
    scorecard.rename(columns={'INSTNM':'School Name'}, inplace=True)

    #formatting step 1: remove all characters within parenthesis
    salaries['School Name Extract 1'] = \
        salaries['School Name'].str.replace(r"\(.*\)","")
    #formatting step 2: replace all commas with hyphens
    salaries['School Name Extract 2'] = \
        salaries['School Name Extract 1'].str.replace(r",","-")
    #formatting step 3: replace all 
    #(zero or more spaces-hyphen-zero or more spaces) with hyphen(without spaces)
    salaries['Formatted School Name'] = \
        salaries['School Name Extract 2'].str.replace(r"[\s]*-[\s]*","-")

    #format the 'Mid-Career Median Salary' column
    salaries['Mid-Career Median Salary'] = \
        salaries['Mid-Career Median Salary'].str.replace("$","")
    salaries['Mid-Career Median Salary'] = \
        salaries['Mid-Career Median Salary'].str.replace(",","")
    salaries['Mid-Career Median Salary'] = \
        salaries['Mid-Career Median Salary'].str.replace(".00","")
    salaries['Salary'] = pd.to_numeric(salaries['Mid-Career Median Salary'])

    #Create new column SalaryClass to make the Salary ranges into classes
    salaries['SalaryClass'] = 100
    salaries.loc[salaries['Salary'].between(0, 75, inclusive=False), 'SalaryClass'] = 0
    salaries.loc[salaries['Salary'].between(75, 90, inclusive=True), 'SalaryClass'] = 1
    salaries.loc[salaries['Salary'].between(90, 500, inclusive=False), 'SalaryClass'] = 2

    # Delete rows with SalaryClass 100
    rowstodrop = salaries[ salaries['SalaryClass'] == 100 ].index
    salaries.drop(rowstodrop , inplace=True)

    #rename the join column on the scorecard dataset
    scorecard.rename(columns={'School Name':'Formatted School Name'} \
        , inplace=True)

    formattedjoin = \
        pd.merge(salaries, scorecard, on='Formatted School Name', how='inner')

    #Keep only the required columns in the final dataframe
    columnstokeep = ['SalaryClass','HCM2','PREDDEG','HBCU','PBI','MENONLY', \
    'WOMENONLY','SATVR25','SATVR75','SATMT25','SATMT75','SATWR25','SATWR75','SATVRMID', \
    'SATMTMID','SATWRMID','ACTCM25','ACTCM75','ACTEN25','ACTEN75','ACTMT25','ACTMT75', \
    'ACTWR25','ACTWR75','PCIP01','PCIP03','PCIP04','PCIP05','PCIP09','PCIP10','PCIP11', \
    'PCIP12','PCIP13','PCIP14','PCIP15','PCIP16','PCIP19','PCIP22','PCIP23','PCIP24', \
    'PCIP25','PCIP26','PCIP27','PCIP29','PCIP30','PCIP31','PCIP38','PCIP39','PCIP40', \
    'PCIP41','PCIP42','PCIP43','PCIP44','PCIP45','PCIP46','PCIP47','PCIP48','PCIP49', \
    'PCIP50','PCIP51','PCIP52','PCIP54','DISTANCEONLY','UGDS']

    finaldf = formattedjoin[columnstokeep]

    return finaldf
