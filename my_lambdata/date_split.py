import pandas as pd

class date(str):
  def __init__(self, mdy):  

    self.mdy = mdy

  @property
  def day(self):
    return str(self.mdy).split('/')[1]

  @property
  def month(self):
    return str(self.mdy).split('/')[0]

  @property
  def year(self):
    return str(self.mdy).split('/')[2]

def date_converter(day):
    """
    simply takes a string with the appropriate date format
    and converts to a date object
    input is a date (MM/DD/YY) as a string
    output is the date as a date object
    """
    return date(day)


def date_splitter(dataframe, date_col):
  """
  input is a dataframe and the name of the date column
  output is the dataframe with 3 new columns for day, month, year
  """

  # create copy of dataframe
  df = dataframe.copy()

  # create names for the day, month, and year columns
  month_name = str(date_col)+' month'
  day_name = str(date_col)+' day'
  year_name = str(date_col)+' year'

  # create empty columns for day, month, year
  df[month_name] = [0] * len(df)
  df[day_name] = [0] * len(df)
  df[year_name] = [0] * len(df)

  # use .apply and date_converter to convert date strings to date objects
  df[date_col] = df[date_col].apply(date_converter)

  # go through each row, get the day, month, and year, and assign column values
  for i in range (len(df)):
    day = df[date_col][i].day
    month = df[date_col][i].month
    year = df[date_col][i].year

    df.loc[i, day_name] = day
    df.loc[i, month_name] = month
    df.loc[i, year_name] = year

  # cast the date column back into string format
  df[date_col] = df[date_col].astype(str)

  return df