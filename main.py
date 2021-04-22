import json, locale
from modules.computing import compute_data, get_base_payload
from modules.files import get_year_data



def main():
  """ Main module """

  locale.setlocale(locale.LC_ALL, 'en_US.utf8')
  print(locale.getlocale(locale.LC_ALL))

  print('Inicializando compilador de dados')

  # Gets directives
  with open('data/directives.js', 'r') as payload:
    directives = json.load(payload)

  final_data = []

  # For each year in directives
  for directive in directives['years']:
    if int(directive['year']) <= 2020:
      payload = get_base_payload(directive['year'])
      print(f'Analizando dados do ano de {directive["year"]}')
      payload = get_year_data(directive, payload)
      final_data.append(compute_data(payload))

  with open('results.json', 'w') as result_file:
    json.dump(final_data, result_file)



if __name__ == "__main__":
  main()