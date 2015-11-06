import pandas as pd
from atus_analysis.models import PersonInfo


def get_summary_data_from_atus_data(apps, schema_creation):
    atus_sum_df = pd.read_csv("atus_data/astussum_2014.dat", names=[
        'person_id', 'weight', 'youngest_child', 'age', 'sex', 'education', 'race',
               'metro_status', 'labor_status', 'weekly_earnings'])
    for row in atus_sum_df.iterrows():
        person_id = row[1].person_id
        weight = row[1].weight
        youngest_child = row[1].youngest_child
        age = row[1].age
        sex = row[1].sex
        education = row[1].education
        race = row[1].race
        metro_status = row[1].metro_status
        labor_status = row[1].labor_status
        weekly_earnings = row[1].weekly_earnings
        PersonInfo.objects.create(id=person_id, person_id=person_id, weight=weight, youngest_child=youngest_child,
                                  age=age, sex=sex, education=education, race=race, metro_status=metro_status,
                                  labor_status=labor_status, weekly_earnings=weekly_earnings)


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