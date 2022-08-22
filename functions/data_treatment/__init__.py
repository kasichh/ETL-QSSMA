import pandas as pd


def change_date_format(date_colum):
    date_colum = pd.to_datetime(date_colum, format="%Y/%m/%d")
    date_colum = date_colum.dt.strftime('%d/%m/%Y')
    return date_colum


def date_format_with_null_values(date_colum):
    date_colum = date_colum.apply(lambda x: str(x)[-2:] + '/' + str(x)[4:6] + '/' + str(x)[:4])
    return date_colum



