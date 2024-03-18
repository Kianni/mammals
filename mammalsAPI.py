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
                species = data['species_guess']
                wikipedia_url = self.get_wikipedia_url(data['taxon']['id']) or 'No Wikipedia URL found'
                return species, wikipedia_url
            else:
                return None, None
        else:
            return None, None

def main():
    primate = Taxon('Primates')
    p_species, p_url = primate.get_species_and_url()
    print(f"Species: {p_species}")
    print(f"Wikipedia URL: {p_url}")

    rodentia = Taxon('Rodentia')
    r_species, r_url = rodentia.get_species_and_url()
    print(f"Species: {r_species}")
    print(f"Wikipedia URL: {r_url}")

    artiodactyla = Taxon('Artiodactyla')
    a_species, a_url = artiodactyla.get_species_and_url()
    print(f"Species: {a_species}")
    print(f"Wikipedia URL: {a_url}")

    carnivora = Taxon('Carnivora')
    c_species, c_url = carnivora.get_species_and_url()
    print(f"Species: {c_species}")
    print(f"Wikipedia URL: {c_url}")

    chiroptera = Taxon('Chiroptera')
    ch_species, ch_url = chiroptera.get_species_and_url()
    print(f"Species: {ch_species}")
    print(f"Wikipedia URL: {ch_url}")
    
if __name__ == '__main__':
    main()