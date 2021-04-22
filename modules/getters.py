import math
from datetime import datetime


def get_fields(line):
  """ Returns sanitized field data from a line, as an array """ 
  return line.replace('"', '').split(';')


def get_age(directive, fields):
  """ Returns the age for a candidate based on directives and line data """
  raw_date = fields[directive['birthDateIndex']]
  date_format = directive['birthDateFormat']

  if(directive.get('birthDatePadYear', False)):
    if '/' in raw_date:
      p = raw_date.split('/')
      raw_date = f'{p[0]}/{p[1]}/19{p[2]}'
    elif '-' in raw_date:
      p = raw_date.split('-')
      raw_date = f'{p[0]}-{p[1]}-19{p[2]}'

  this_year = datetime(directive['year'], 1, 1)
  try:
    birthdate = datetime.strptime(raw_date, date_format)
  except:
    birthdate = None
  
  if birthdate:
    age = this_year - birthdate
    age = math.floor(age.days / 365.25)
  else:
    age = None
  
  return age


def get_is_female(directive, fields):
  """ Returns if a candidate is female """
  gender_field = fields[directive['genderIndex']]
  return ('fem' in gender_field or 'FEM' in gender_field) if gender_field != '#NE#' else None


def get_was_elected(directive, fields):
  """ Returns wether a candidate was elected """
  elected_field = fields[directive['isElectedIndex']]
  return not('N' in elected_field or 'n' in elected_field)
