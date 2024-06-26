# import json
# import requests
# import tomli
# from pathlib import Path
# from requests.exceptions import HTTPError

import ccte_api as cte

## Test chemical search
toluene = 'DTXSID7021360'
p_xylene = 'DTXSID2021868'
o_xylene = 'DTXSID3021807'
m_xylene = ' DTXSID6026298'

print("Chemical APIs")
c = cte.Chemical()

print("chemical search")
cs = c.search(by='equals',word='toluene')
print(cs)
print("\n")

print("chemical details")
cd = c.details(by='dtxsid',word=toluene)
print(cd)
print("\n")

print("batch details")
bd = c.details(by='batch',word=[toluene,p_xylene,o_xylene,m_xylene])
print(bd)
print("\n")

print('batch search')
bs = c.search(by='batch',word=['toluene','p-xylene','o-xylene','108-38-3'])
print(bs)
print("\n")


print("Exposure APIs")
e = cte.Exposure()

print("Function Search")
fs = e.search(by='fc',word=toluene)
print(fs)

print("QSUR Search")
qs = e.search(by='qsur',word=toluene)
print(qs)

print("Product Search")
ps = e.search(by='puc',word=toluene)
print(ps)

print("List Presence Search")
ls = e.search(by='lpk',word=toluene)
print(ls)

print("PUC Vocabulary")
pv = e.vocabulary(by='puc')
print(pv)

print("LPK Vocabulary")
lv = e.vocabulary(by='lpk')
print(lv)

print("FC Vocabulary")
fv = e.vocabulary(by='fc')
print(fv)

# path = Path.home().joinpath(".config.toml")
# if not path.is_file():
#     raise FileExistsError(f"{path} does not exist.")
# with open(path,mode='rb') as fp:
#     config = tomli.load(fp)

# config = config['ccd_api']
# headers = {k:v for k,v in config.items() if k in ['accept','x-api-key']}
# config['host'] = "https://api-ccte.epa.gov/chemical/detail/search/by-dtxsid/DTXSID702"

# gets = requests.get(config['host'],headers=headers)
# info = json.loads(gets.content)


# host = "https://api-ccte.epa.gov/chemical/detail/search/by-dtxsid/"
# headers = {**headers,**{"content-type":"application/json"}}
# chems = [toluene,p_xylene,o_xylene,m_xylene]
# word = '["'+'","'.join(chems)+'"]'
# posts = requests.post(host,headers=headers,data=word)
# print(json.loads(posts.content))
# host = 'https://api-ccte.epa.gov//chemical/search/equal/toluene'
