import pandas as pd

def load_respondent_data(apps, schema_editor):

    summary = pd.read_csv("atus/atussum_2014.dat")
    summary.rename(columns={'tucaseid':'respondent_id', 'TUFINLWGT':'weight', 'TRYHHCHILD':'youngest_child',
                            'TEAGE':'age', 'TESEX':'sex', 'PEEDUCA':'education', 'PTDTRACE':'race',
                            'GTMETSTA':'metro_status', 'TELFS':'labor_status', 'TRERNWA':'wkly_earnings',
                            'TEMJOT': 'multiple_job_status', 'TRDPFTPT': 'full_or_part_job_status',
                            "TESCHENR": 'school_enrollment', 'TESCHLVL': 'school_level',
                           'TRSPPRES': 'presence_spouse', 'TESPEMPNOT': 'spouse_employment_status',
                           'TRCHILDNUM': "num_children", "TEHRUSLT": 'typical_work_hrs',
                           }, inplace=True)
    summary = summary.drop('PEHSPNON', 1)
    summary = summary.drop('TRTEC', 1)
    summary = summary.drop('TRSPFTPT', 1)
    summary = summary.drop('TUDIARYDAY', 1)
    summary = summary.drop('TRHOLIDAY', 1)
    summary = summary.drop('TRTHH', 1)
    summary = summary[["respondent_id", "weight", "age", "sex",
                                 "education", "race", "metro_status",
                                 "labor_status", "wkly_earnings",
                                 "multiple_job_status", "full_or_part_job_status",
                                 "school_enrollment", "school_level", "typical_work_hrs"]]

    Respondent = apps.get_model("atus", "Respondent")

    for index, row in summary.iterrows():
        respondent = row.respondent_id
        weight = row.weight
        age = row.age
        sex = row.sex
        education = row.education
        race = row.race
        metro_status = row.metro_status
        labor_status = row.labor_status
        wkly_earnings = row.wkly_earnings
        multiple_job_status = row.multiple_job_status
        full_or_part_job_status = row.full_or_part_job_status
        school_enrollment = row.school_enrollment
        school_level = row.school_level
        typical_work_hrs = row.typical_work_hrs

        Respondent.objects.create(respondent=respondent, weight=weight,
                                  age=age, sex=sex, education=education,
                                  race=race, metro_status=metro_status,
                                  labor_status=labor_status, wkly_earnings=wkly_earnings,
                                  multiple_job_status=multiple_job_status,
                                  full_or_part_job_status=full_or_part_job_status,
                                  school_enrollment=school_enrollment,
                                  school_level=school_level,
                                  typical_work_hrs=typical_work_hrs)


def load_household_data(apps, schema_editor):

    household_data = pd.read_csv("atus/atusrost_2014.dat")
    household_data = household_data.rename(columns={"TUCASEID": 'respondent_id',
                                                "TULINENO": "individual_in_household",
                        "TEAGE": "age", "TERRP": "relation",
                        "TESEX":"sex"})
    household_data = household_data.drop('TXAGE', 1)
    household_data = household_data.drop('TXRRP', 1)
    household_data = household_data.drop('TXSEX', 1)
    household_data = household_data[household_data.individual_in_household != 1]

    def subtract_one(x):
        return x - 1

    household_data['individual_in_household'] = household_data['individual_in_household'].map(lambda x: subtract_one(x))


    HouseholdMember = apps.get_model("atus", "HouseholdMember")
    Respondent = apps.get_model("atus", "Respondent")


    for index, row in household_data.iterrows():
        respondent = row.respondent_id
        relative_id = row.individual_in_household
        age = row.age
        relation = row.relation
        sex = row.sex
        HouseholdMember.objects.create(respondent=Respondent.objects.get(respondent=respondent), relative_id=relative_id,
                                          age=age, relation=relation, sex=sex)


def load_activity_title_data(apps, schema_editor):

    activities = pd.read_csv("atus/lexiconwex2014.txt", encoding="ISO-8859-1", header=-1)
    activities = activities[[0,1]]
    activities = activities.dropna()
    activities = activities.rename(columns={0:"code", 1:"title"})

    def add_zeros(x):
        if len(str(int(x))) < 6:
            return "0" + str(int(x))
        else:
            return str(int(x))

    activities['code'] = activities['code'].map(lambda x: add_zeros(x))

    ActivityTitle = apps.get_model("atus", "ActivityTitle")

    for index, row in activities.iterrows():
            code = row.code
            title = row.title


            ActivityTitle.objects.create(code=code,
                                        title=title,
                                                    )


def load_activity_response_data(apps, schema_editor):
    activity_codes = pd.read_csv("atus/atussum_2014.dat")
    activity_codes.drop(activity_codes.columns[1:18], axis=1, inplace=True)
    activity_codes = pd.melt(activity_codes, id_vars=['tucaseid'],
                         value_vars=['t010101',
                                     't010102', 't010201', 't010299',
       't010301', 't010399', 't010401', 't010501', 't019999', 't020101',
       't020102', 't020103', 't020104', 't020199', 't020201', 't020202',
       't020203', 't020301', 't020302', 't020303', 't020399', 't020401',
       't020402', 't020499', 't020501', 't020502', 't020599', 't020601',
       't020602', 't020699', 't020701', 't020799', 't020801', 't020901',
       't020902', 't020903', 't020904', 't020905', 't020999', 't029999',
       't030101', 't030102', 't030103', 't030104', 't030105', 't030106',
       't030108', 't030109', 't030110', 't030111', 't030112', 't030199',
       't030201', 't030202', 't030203', 't030299', 't030301', 't030302',
       't030303', 't030399', 't030401', 't030402', 't030403', 't030404',
       't030405', 't030499', 't030501', 't030502', 't030503', 't030504',
       't030599', 't039999', 't040101', 't040102', 't040103', 't040104',
       't040105', 't040106', 't040108', 't040109', 't040110', 't040111',
       't040112', 't040199', 't040201', 't040203', 't040301', 't040302',
       't040303', 't040401', 't040402', 't040403', 't040404', 't040405',
       't040501', 't040502', 't040503', 't040504', 't040505', 't040506',
       't040507', 't040508', 't040599', 't049999', 't050101', 't050102',
       't050103', 't050104', 't050199', 't050201', 't050202', 't050203',
       't050205', 't050301', 't050302', 't050303', 't050304', 't050305',
       't050399', 't050401', 't050403', 't050404', 't050499', 't059999',
       't060101', 't060102', 't060103', 't060199', 't060201', 't060202',
       't060301', 't060302', 't060303', 't060399', 't060401', 't060403',
       't060499', 't069999', 't070101', 't070102', 't070103', 't070104',
       't070105', 't070199', 't070201', 't079999', 't080101', 't080201',
       't080202', 't080203', 't080301', 't080399', 't080401', 't080402',
       't080403', 't080501', 't080502', 't080601', 't080602', 't080701',
       't080702', 't080799', 't089999', 't090101', 't090103', 't090104',
       't090199', 't090201', 't090202', 't090301', 't090401', 't090501',
       't090502', 't090599', 't099999', 't100101', 't100102', 't100103',
       't100199', 't100201', 't100304', 't100305', 't109999', 't110101',
       't110201', 't110299', 't120101', 't120199', 't120201', 't120202',
       't120299', 't120301', 't120302', 't120303', 't120304', 't120305',
       't120306', 't120307', 't120308', 't120309', 't120310', 't120311',
       't120312', 't120313', 't120399', 't120401', 't120402', 't120403',
       't120404', 't120499', 't120501', 't120502', 't120503', 't120504',
       't129999', 't130101', 't130102', 't130103', 't130104', 't130105',
       't130106', 't130107', 't130108', 't130109', 't130110', 't130112',
       't130113', 't130114', 't130115', 't130116', 't130117', 't130118',
       't130119', 't130120', 't130122', 't130124', 't130125', 't130126',
       't130127', 't130128', 't130129', 't130130', 't130131', 't130132',
       't130133', 't130134', 't130136', 't130199', 't130202', 't130203',
       't130204', 't130205', 't130206', 't130210', 't130213', 't130214',
       't130215', 't130216', 't130218', 't130219', 't130222', 't130224',
       't130225', 't130226', 't130227', 't130229', 't130231', 't130299',
       't130301', 't130302', 't139999', 't140101', 't140102', 't140103',
       't140104', 't140105', 't149999', 't150101', 't150102', 't150103',
       't150104', 't150105', 't150106', 't150199', 't150201', 't150202',
       't150203', 't150204', 't150299', 't150301', 't150302', 't150401',
       't150402', 't150499', 't150501', 't150601', 't150602', 't150701',
       't159999', 't160101', 't160102', 't160103', 't160104', 't160105',
       't160106', 't160107', 't160108', 't160199', 't169999', 't180101',
       't180201', 't180202', 't180203', 't180204', 't180205', 't180206',
       't180207', 't180208', 't180209', 't180299', 't180301', 't180302',
       't180303', 't180304', 't180305', 't180401', 't180402', 't180403',
       't180404', 't180405', 't180499', 't180501', 't180502', 't180503',
       't180504', 't180599', 't180601', 't180602', 't180603', 't180604',
       't180699', 't180701', 't180702', 't180703', 't180704', 't180799',
       't180801', 't180802', 't180803', 't180804', 't180805', 't180806',
       't180807', 't180899', 't180901', 't180902', 't180903', 't180905',
       't180999', 't181001', 't181002', 't181099', 't181101', 't181201',
       't181202', 't181203', 't181204', 't181205', 't181299', 't181301',
       't181302', 't181399', 't181401', 't181501', 't181599', 't181601',
       't181699', 't181801', 't181899', 't189999', 't500101', 't500103',
       't500105', 't500106', 't500107']).sort_values(by="tucaseid")

    activity_codes = activity_codes.rename(columns={"tucaseid": "respondent_id",
                                                    "variable": 'code',
                                "value": "minutes"})

    activity_codes["code"] = activity_codes["code"].str.replace(r't', r'')

    activity_codes = activity_codes[:3850]

    ActivityResponse = apps.get_model("atus", "ActivityResponse")
    Respondent = apps.get_model("atus", "Respondent")
    ActivityTitle = apps.get_model("atus", "ActivityTitle")


    for index, row in activity_codes.iterrows():
        respondent = row.respondent_id
        code = row.code
        minutes = row.minutes


        ActivityResponse.objects.create(respondent=Respondent.objects.get(respondent=respondent),
                                       code=ActivityTitle.objects.get(code=code),
                                        minutes=minutes)