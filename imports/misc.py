import re

## Return category code for given row.
def category(row: str):
    if re.match(r'^B', row):
        return 'COU'
    elif re.match(r'^FS', row):
        return 'FXS'
    elif re.match(r'^FX', row):
        return 'FXX'
    elif re.match(r'^G', row):
        return 'GEN'
    elif re.match(r'^U', row):
        return 'UTL'
    elif re.match(r'^X', row):
        return 'INT'
    else:
        return ''

## Return accounting code for given row.
def acccode(row: str):
    if re.match(r'^B', row):
        return 'COUNCIL'
    elif re.match(r'^FS', row):
        return 'FXS'
    elif re.match(r'^FX', row):
        return 'FXX'
    elif re.match(r'^G', row):
        return 'GENERAL'
    elif re.match(r'^U', row):
        return 'UTILITY'
    elif re.match(r'^X', row):
        return 'INTERNAL'
    else:
        return ''

## Strip multiple spaces from row.
def strp(row: str):
    return re.sub(' +', ' ', row)

## Replaces DAY in pte with NET
def day_to_net(row: str):
    return re.sub('DAY', 'NET', row)