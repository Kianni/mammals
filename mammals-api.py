import requests
import random

class Taxon:
    def __init__(self, taxon_name):
        self.taxon_name = taxon_name
        self.taxon_id = self.get_taxon_id()

    def get_taxon_id(self):
        response = requests.get(f'https://api.inaturalist.org/v1/taxa/autocomplete?q={self.taxon_name}')
        data = response.json()
        if data['results']:
            return data['results'][0]['id']
        else:
            return None

    def get_random_obj_by_taxon_id(self):
        response = requests.get(f'https://api.inaturalist.org/v1/observations?taxon_id={self.taxon_id}')
        data = response.json()
        if data['results']:
            return random.choice(data['results'])
        else:
            return None

    def get_wikipedia_url(self, taxon_id):
        response = requests.get(f'https://api.inaturalist.org/v1/taxa/{taxon_id}')
        data = response.json()
        if data['results']:
            return data['results'][0]['wikipedia_url']
        else:
            return None

    def get_species_and_url(self):
        if self.taxon_id:
            data = self.get_random_obj_by_taxon_id()
            if data:
                species = data['species_guess'] or self.taxon_name
                wikipedia_url = self.get_wikipedia_url(data['taxon']['id']) or 'No Wikipedia URL found'
                return species, wikipedia_url
            else:
                return None, None
        else:
            return None, None

def main():
    taxon = Taxon('Primates')
    species, url = taxon.get_species_and_url()
    print(f"Species: {species}")
    print(f"Wikipedia URL: {url}")
    
if __name__ == '__main__':
    main()