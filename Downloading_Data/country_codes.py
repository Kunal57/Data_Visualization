from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
  """ return the pygal 2-digit country code for the given country """
  for code, name in COUNTRIES.items():
    if name == country_name:
      return code
  # if the country wasn't found, return None.
  return None
