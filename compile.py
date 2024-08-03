r"Compile HCI/aug-cc-pwcvqz database."


import atomdb
from atomdb.utils import MULTIPLICITIES
from atomdb.periodic import element_symbol
from atomdb import element_number
import aux_file
import numpy as np
from glob import glob


MYDATAPATH = "./"
def wrap_compile(atnums, charges):
    """
    atnums: list
    charges: list
    """
    if not isinstance(atnums, list) and isinstance(atnums, int):
        atnums = [atnums]
    if not isinstance(charges, list) and isinstance(charges, int):
        charges = [charges]
    print(atnums)
    print(charges)
    failed = []
    sucess = []
    for atnum in atnums:
        atname = element_symbol(atnum)
        for charge in charges:
            mult = MULTIPLICITIES[(atnum, charge)]
            #atomdb.datasets.hci.run(atnum, charge, mult,0,'hci',datapath=MYDATAPATH)
            aux_file.run(atnum, charge, mult,0,'hci',datapath=MYDATAPATH)
            try:
                #print(f'Compiling {atname}, atnumber {atnum}, charge {charge}, mult {mult}')
                atomdb.datasets.hci.run(atnum, charge, mult,0,'hci',datapath=MYDATAPATH)
                  # compile just wraps run
                  #atomdb.compile(atnum, charge, mult, 0, 'hci', datapath=MYDATAPATH)
                sucess.append((atnum, charge, mult))
            except:
                failed.append((atnum, charge, mult))
            
    print('Summary')
    print(f'{len(sucess)} completed')
    for ok in sucess:
        print(ok)
    # Check the following
    print(f'{len(failed)} failed')
    for bad in failed:
        print(bad)


# Compile atoms HCI dataset up to Ar (neutral atoms and ions)
#------------------------------------------------------------

fpath = f'*/*.fchk' # regex describing where all the fchk files will be
dbfiles = glob(fpath) # regex interpreter that will find all files that corespond to the previously defined pattern



atoms = [f.split('/')[-1].split('_')[0] for f in dbfiles]
atoms = sorted(set(atoms))
print(atoms)
atnums = [int(atom) for atom in atoms]
# atnums = sorted(atnums)
# atnums = list(set(atnums))

for atnum in atnums:
    charges = list(range(-1, atnum))
    print(charges)
    wrap_compile(atnum, charges)
