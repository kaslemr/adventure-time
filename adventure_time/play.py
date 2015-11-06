import pandas as pd


def get_summary_data_from_atus_data(apps, schema_creation):
    atus_sum_df = pd.read_csv("atus_data/astussum_2014.dat", names=[
        'id', 'person_id', 'weight', 'youngest_child', 'age', 'sex', 'education', 'race',
               'metro_status', 'labor_status', 'weekly_earnings',
        ""
    ])


"""
Do we want to clean the data up for human consumption (like below)?
or leave it in API format?




def sex_fix(sex):
    for i in sex:
        if i == 1:
            i = "male"
        elif i == 2:
            i = "female"


def youngest_child_fix(youngest_child):
    for i in youngest_child:
        if i < 0:
            i = "NaN"
"""