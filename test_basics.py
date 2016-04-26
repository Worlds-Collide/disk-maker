"""Basic sanity checks to verify that ktransit works.
To run, simply type "py.test".
"""

import numpy as np

def test_import():
    """Can we import diskmaker successfully?"""
    import diskmaker
    from diskmaker.create import calcSemis


def test_create():
    """
    can we run code to create a disk
    """
    from diskmaker.create import calcSemis
    ###
    totalmass = 5.0
    smallmass = 0.01
    largemass = 0.1
    nsmallbodies = 200
    inner = 0.2
    outer = 4.0
    alpha = 3/2
    #####

    finalSemi, finalMass, fig = calcSemis(totalmass, smallmass, 
        largemass, nsmallbodies, inner, outer, alpha, returnFigure=True)

    maxdiff = finalMass*0.05
    assert np.abs((np.sum(finalMass) - totalmass)/totalmass) < 0.05
