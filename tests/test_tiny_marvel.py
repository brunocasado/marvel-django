from marvel.libs import MarvelCli



def test_all_characters():
    mcli = MarvelCli(apikey='f96141b7126e6e58b552d37efecfb476', private='e3d21219730066f2769ac63a6642a4985a97846e')
    data = mcli.get_all_customers(params={ 'offset': 10 })
    # print (data.results)
    for a in data:
        print ('trying make request. Total Data: {0}'.format(a.total))

    assert (1==1)