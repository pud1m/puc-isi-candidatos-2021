import json, os, math, locale
from datetime import datetime


def main():
  """ Main module """

  locale.setlocale(locale.LC_ALL, 'en_US.utf8')
  print(locale.getlocale(locale.LC_ALL))

  print('Inicializando compilador de dados')

  # Gets directives
  with open('data/directives.json', 'r') as payload:
    directives = json.load(payload)

  # For each year in directives
  for directive in directives['years']:
    if int(directive['year']) <= 2000:
      payload = get_base_payload(directive['year'])
      print(f'Analizando dados do ano de {directive["year"]}')
      payload = get_year_data(directive, payload)
      print(compute_data(payload))
  


def get_base_payload(year):
  """ Returns a base payload for the year """
  return {
    'year': year,
    'gender': {
      'universe': 0,
      'women': 0,
      'totalElected': 0,
      'womenElected': 0,
    },
    'age': {
      'candidates': [],
      'elected': []
    }
  }


def compute_data(payload):
  """ Returns a dict with computed data from the payload """
  return {
    'year': payload['year'],
    'gender': {
      'total': payload['gender']['universe'],
      'women': 100/(payload['gender']['universe'] or 1) * payload['gender']['women'],
      'womenElected': 100/(payload['gender']['totalElected'] or 1) * payload['gender']['womenElected']
    },
    'avgAge': {
      'candidates': sum(payload['age']['candidates']) / len(payload['age']['candidates']),
      'elected': sum(payload['age']['elected']) / len(payload['age']['elected'])
    }
  }


def get_year_data(directive, payload):
  """ Fetches the info for a year, using the data from the directive """

  for filename in os.listdir(f'data/tse/{directive["year"]}'):
    print(f'Lendo arquivo {filename}')
    with open(f'data/tse/{directive["year"]}/{filename}', 'r', encoding='latin-1') as file:
      content = file.readlines()
    

    for line in content:
      fields = get_fields(line)
      age = get_age(directive, fields)
      is_female = get_is_female(directive, fields)
      was_elected = get_was_elected(directive, fields)

      if age:
        payload['age']['candidates'].append(age)
        if was_elected:
          payload['age']['elected'].append(age)
      
      if is_female is not None:
        payload['gender']['universe'] += 1
        if is_female:
          payload['gender']['women'] += 1

      if was_elected:
        payload['gender']['totalElected'] += 1
        if is_female:
          payload['gender']['womenElected'] += 1
  
  return payload


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


if __name__ == "__main__":
  main()