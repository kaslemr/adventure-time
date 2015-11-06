from rest_framework.fields import CharField


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
