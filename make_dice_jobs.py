#!/usr/bin/env python 
import os
import pickle 
from itertools import chain

PSE = [['H', 1],['He', 2],['Li', 3],['Be', 4],['B', 5],['C', 6],['N', 7],['O', 8],['F', 9],['Ne', 10],['Na', 11],['Mg', 12],['Al', 13],['Si', 14],['P', 15],['S', 16],['Cl', 17],['Ar', 18],['K', 19],['Ca', 20],['Sc', 21],['Ti', 22],['V', 23],['Cr', 24],['Mn', 25],['Fe', 26],['Co', 27],['Ni', 28],['Cu', 29],['Zn', 30],['Ga', 31],['Ge', 32],['As', 33],['Se', 34],['Br', 35],['Kr', 36]]
# Atomic number to symbol and vice versa
atnum2symbol, symbol2atnum = {}, {}
for i in PSE:
    atnum2symbol[i[1]] = i[0]
    symbol2atnum[i[0]] = i[1]


def find_charges(element):
    nelec = symbol2atnum[element] 
    charges = [x for x in range(0,nelec)]
    charges.append(-1)
    return charges 


with open('multiplicities.pkl', 'rb') as f:
    multiplicities = pickle.load(f)


# Set up parameters
atoms = ['K']
#BASIS = 'aug-cc-pwCVQZ'
BASIS = 'aug-cc-CVQZ'
epsilon = '5e-4'
NTASKS = '20'
NNODES = '1'

charges = find_charges(atoms[0])




def make_jobs(mol, charge, spin=None, eps=None):
    # System definition
    geometry = f'{mol}  0.0 0.0 0.0'
    z = symbol2atnum[mol]
    print(multiplicities[z-1])
    if spin is None:
        spin=multiplicities[z-1][charge+3]-1
        
        
    print(f"system {mol}, Q={charge}, s={spin}")
    if eps is None:
        eps = 1e-4
    mul = spin + 1
    basisname = BASIS.lower().replace("-", "")

    # Select a template
    template = 'dice_template_noPT.py'
    with open(template, 'r') as f:
        content = f.read()
    
    fname = f'{z:04d}_q{charge:03d}_m{mul:02d}_k00_sp_hci_{basisname}'
    content = content.replace("output", fname)
    content = content.replace("GEOMETRY", geometry)
    content = content.replace("atcharge", str(charge))
    content = content.replace("spinmult", str(mul))
    content = content.replace("basis_set1", BASIS)
    content = content.replace("ntasks", NTASKS) 
    content = content.replace("EPS", eps)

    # Make job folder
    folder = f'{mol}_{charge}_{spin}'
    if not os.path.exists(folder):
        os.makedirs(folder) 
    # write HCI job script        
    with open(f'{folder}/run_dice.py', 'w') as f:
        f.write(content)
    
    with open('run_dice.sh', 'r') as f:
        content = f.read()

    content = content.replace("TIME", '0-03:00:00')
    content = content.replace("MEMORY", '4G')
    content = content.replace("n_tasks", NTASKS)
    content = content.replace("n_nodes", NNODES) 
    content = content.replace("ACC", 'def-ayers')  # Alternative: 'rrg-ayers-ab'
    content = content.replace("NAME", folder)
    # write slurm file        
    with open(f'{folder}/run_dice.sh', 'w') as f:
        f.write(content)


for atm in atoms:
    for charge in charges:
        make_jobs(atm, charge, spin=None, eps=epsilon)
