# for more insights check 
import pandas as pd
import numpy as np
import datetime
import pickle
import sys

element=sys.argv[1]
basis_type = sys.argv[2]
url = f"https://www.molpro.net/info/basis.php?search=1&element={element}&basis={basis_type}&print=1"
dfs = pd.read_html(url)

molpro_scrap = {}
molpro_scrap['info'] = {'url':url, 'Element':element, 'Basis_Type':basis_type, 'Download_Time':datetime.datetime.now()}

# parsing of df objects according to description
contraction = 0
basis = {}
basis[element] = []

for l in range(0,len(dfs)):# each data field being one angular momentum
    if len(dfs[l].columns) > 1:# special case on website as of Jul25, 2024: if the primitive function is to be used, sometimes only the exponent is given
        for column in range(1,len(dfs[l].columns)):# columns are contractions
            basis[element].append([l])
            for line in np.ndarray.tolist(dfs[l].values):
                if line[column] > 0.0:
                    basis[element][contraction].append([line[0],line[column]])
            contraction+=1
    else:# special case as of Jul25, 2024: if the primitive function is to be used, sometimes only the exponent is given
        for line in np.ndarray.tolist(dfs[l].values):
            basis[element].append([l , [line[0], 1.0]])

molpro_scrap['basis'] = basis 

with open(element+'_'+basis_type+'.pkl', 'wb') as f:
    pickle.dump(molpro_scrap, f)
