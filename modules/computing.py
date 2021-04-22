

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
