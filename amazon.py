import amazonproduct

#config = {
#  'access_key': '',
#  'secret_key: '',
#  'associate_tag: '',
#  'locale': 'us'
#}

# ANSI = ['place your ANSI here separated by commas']
api = amazonproduct.API(cfg=config)

for i in items_purchased:
  res = api.itemlookup(ANSI, ResponseGroup='OfferSummary')
  results = res.append
  
print(results)

