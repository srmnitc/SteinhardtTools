import pytest
import os,sys,inspect
import numpy as np
import pybop.core as pc
import pybop.crystal_structures as pcs

def test_q_2():
    #this might take a while, it will find all qs
    atoms, boxdims = pcs.make_crystal('bcc', repetitions = [6, 6, 6])
    sys = pc.System()
    sys.assign_atoms(atoms, boxdims)
    #sys.read_inputfile("tests/bcc.dat")
    sys.get_neighbors(method = 'voronoi')
    #sys.get_neighbors(method = 'cutoff', cutoff=0.9)

    sys.calculate_q(2)
    q = sys.get_qvals(2)
    assert np.round(np.mean(np.array(q)), decimals=2) == 0.00 