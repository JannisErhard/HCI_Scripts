"""Title: $title"""
import numpy as np

from pyscf import gto, scf, ao2mo
from pyscf.shciscf import shci
from pyscf.tools import molden, fcidump
import pickle 
import apost3d as apost   # Laila's PySCF to fchk


NAME = 'output' + '_EPS'
GEOM = """GEOMETRY"""
CHARGE = atcharge
MULT = spinmult
BASIS = """basis_set1"""

# basis read mod
element = 'DUMMY'
basis_type = 'aug-cc-pwCVQZ'
with open(element+'_'+basis_type+'.pkl', 'rb') as f:
    molpro_scrap = pickle.load(f)
    basis = molpro_scrap['basis']

def run_shci(atcoords, charge, mult, basis, fname, unit='B'):
    # Build PySCF molecule
    mol = gto.Mole()
    mol.atom = atcoords
    mol.charge = charge
    mol.spin = mult - 1
    mol.basis = basis

    mol.unit = unit
    mol.build()

    # Create HF molecule
    mf = scf.RHF( mol )
    mf.conv_tol = 1e-9
    mf.scf()

    # Write MOLDEN and FCIDUMP
    #molden.from_scf(mf, f"{fname}.molden", ignore_h=False)
    # Write Gaussian and FCIDUMP
    ovlp = mf.get_ovlp()
    apost.write_fchk(mol, mf, fname, ovlp, basis_name=basis_type)
    fcidump.from_scf(mf, f"{fname}.FCIDUMP", tol=0.0)

    # Number of orbital and electrons
    norb = mf.mo_coeff.shape[0]
    nelec = mol.nelectron
    n_a = (nelec + mult - 1) // 2
    n_b = nelec - n_a

    # Create SHCI molecule for just variational opt.
    # Active spaces chosen to reflect valence active space.
    mch = shci.SHCISCF( mf, norb, nelec )
    mch.fcisolver.mpiprefix = 'mpirun -np ntasks' #2
    mch.fcisolver.stochastic = True
    mch.fcisolver.nPTiter = 0   # Turn off perturbative calc.
    mch.fcisolver.sweep_iter = [ 0]
    # mch.fcisolver.DoRDM = True
    mch.fcisolver.DoSpinOneRDM = True
    mch.fcisolver.sweep_epsilon = [ EPS]
    shci.writeSHCIConfFile(mch.fcisolver, [n_a, n_b], False)
    e_shci = mch.mc1step()[0]

    # File cleanup
    mch.fcisolver.cleanup_dice_files()
    return (mch, norb, n_a, n_b)


mc, norb, na, nb = run_shci(GEOM, CHARGE, MULT, basis, NAME, unit='B')
dm_ab = mc.fcisolver.make_rdm1s()  # in MOs
dm2 = mc.fcisolver.make_rdm12(mc.ci, norb, (na,nb))[1]
np.savez(f"{NAME}.ci.npz", energy=mc.e_tot, coeff=mc.ci, rdm1=dm_ab, rdm2=dm2)



