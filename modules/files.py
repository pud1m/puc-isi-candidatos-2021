import os
from .getters import get_fields, get_age, get_is_female, get_was_elected

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
