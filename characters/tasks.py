from marvel import celery_app
from marvel.libs import MarvelCli
from characters.models import Character

@celery_app.task(bind=True)
def sync_characters(self):
    mcli = MarvelCli(apikey='f96141b7126e6e58b552d37efecfb476', private='e3d21219730066f2769ac63a6642a4985a97846e')
    response = mcli.get_all_customers({ 'offset': 10 })
    
    return response