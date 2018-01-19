import requests
import json

import pdb

url = 'http://pplapi.com/'

def query_database(country='fr', number=1):
    """
        Query data from the server
    """
    
    req = requests.get(url + 'batch/1000/country/' + country + '/sample.json')
    pdb.set_trace()
    if req.status_code == 200:
        return req.json()


def save_data(data):
    """
        Saves data to local files
    """
    pdb.set_trace()
    with open(data[0]['country'] + '.json', 'w') as f:
        json.dump(elem, f)


def load_data():
    """
        Loads data from local file(s)
    """
    pass

def get_class(data):
    true_class = []
    for c in data:
        for ppl in c:
            if ppl.json()['country_tld'] == 'fr':
                true_class.append[0]
            else:
                true_class.append[1]

    return true_class

def main():
    data = query_database()

    if data:
        save_data(data)

    pdb.set_trace() 

if __name__ == '__main__':
    main()