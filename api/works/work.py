import requests
import logging

log = logging.getLogger(__name__)

def get_all_works():
    url = 'https://api.datacite.org/dois'
    headers = {'Content-Type': 'application/json'}
    params = '?client-id=snd.bils'
    response = requests.get(url + params, headers=headers)
    assert response.status_code == 200
    works_array = []

    for item in response.json()['data']:
        work_dict = dict()
        work_dict['title']=item['attributes']['titles'][0].get('title', '')
        work_dict['description']=item['attributes']['descriptions'][0].get('description', '')
        work_dict['year']=item['attributes'].get('published', '')
        work_dict['doi']=item['attributes'].get('doi', '')
        work_dict['access_constraints']=item['attributes'].get('rightsList', '')
        work_dict['authors']=item['attributes'].get('creators', [])

        works_array.append(work_dict)

    return works_array

def get_work_by_id(identifier):
    url = 'https://api.datacite.org/dois/'
    headers = {'Content-Type': 'application/json'}
    params = identifier
    log.info(params)
    response = requests.get(url + params, headers=headers)
    assert response.status_code == 200
    item = response.json()['data']
    work_dict = dict()

    work_dict['title']=item['attributes']['titles'][0].get('title', '')
    work_dict['description']=item['attributes']['descriptions'][0].get('description', '')
    work_dict['year']=item['attributes'].get('published', '')
    work_dict['doi']=item['attributes'].get('doi', '')
    work_dict['access_constraints']=item['attributes'].get('rightsList', '')
    work_dict['authors']=item['attributes'].get('creators', [])
     
    related_ids=item['attributes'].get('relatedIdentifiers', '')

    work_dict['reference']=get_crossref_metadata(related_ids)

    return work_dict

def get_crossref_metadata(related_ids):
    url = 'https://api.crossref.org/works/'
    headers = {'Content-Type': 'application/json'}
    reference = dict()

    if len(related_ids) != 0:
      if related_ids[0]['relationType'] == 'IsSupplementTo':
        doi = related_ids[0]['relatedIdentifier'] 
        log.info(doi)
        response = requests.get(url + doi, headers=headers)
        assert response.status_code == 200
        item = response.json()
        reference['author']=item['message']['author']
        reference['title']=item['message']['title'][0]
        reference['doi']=doi

    return reference
