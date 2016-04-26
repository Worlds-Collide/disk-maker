from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy as np 
import matplotlib.pyplot as plt

from . import logger

def calcSemis(totalMass, smallMass, largeMass, nSmall, inner, outer, alpha, returnFigure=False):
    """
    calculate the position of bodies in a disk matching a given surface density profile

    the code assumes a bimodal mass distribution with small and large bodies
    commonly refered to as planetesimals and embryos

    Parameters
    ----------        
    totalMass : float
        the desired total mass in the disk in earth-masses
    smallMass, largeMass : float
        the mass of each small and large body in earth-masses
    nSmall : int
        the number of small bodies
    inner, outer : float
        the inner and outer orbital distance of the disk in AU
    alpha : float
        the disk surface density profile where
        sigma propto mass**-alpha
    returnFigure : bool, optional
        make a fugure showing the mass distribution

    Returns
    ----------   
    finalSemi: array
        the distribution of semimajor axes of the bodies
    finalMass: array
        the masses of the bodies at the given semimajor axes
    fig: figure object
        if the returnFigure keyword is True this is a matplotlib figure object

    a warning will be printed if the final mass in bodies is more than 5 percent discrepent
    from the requested total mass
    """

    nLarge = int((totalMass - (nSmall * smallMass)) / largeMass)

    logger.info('{} large bodies'.format(nLarge))
    logger.info('{} total bodies'.format(nLarge+nSmall))

    missingMass = (totalMass - (nSmall * smallMass) - 
        (largeMass * nLarge))

    # produce a warning if there is more than 5% missing mass
    if missingMass >= totalMass * 0.05:
        logger.warning('{} missing mass'.format(missingMass))
    else:
        logger.info('{} missing mass'.format(missingMass))

    # how many times more massive is large relative to small
    massMultiplier = largeMass / smallMass

    # convert from surface density to radius
    power = alpha * 0.5

    span = outer - inner

    # calculate the initial positions using only small bodies
    unidist = np.linspace(0, 1, nSmall + ((largeMass * nLarge) / smallMass))
    powdist = unidist**(power)

    spacings = (powdist * span) + inner

    # we make the final disk by masking bodies
    maskSmall = np.ones_like(spacings, dtype=bool)
    maskLarge = np.zeros_like(spacings, dtype=bool)

    pos = len(unidist) / nLarge 
    for i in range(nLarge):
        maskLarge[int((i*pos)+(0.5*pos))] = True
        maskSmall[int((i*pos)+(0.5*pos)-(massMultiplier/2)):int((i*pos)+(0.5*pos)+(massMultiplier/2))] = False

    finalSemi = np.r_[spacings[maskLarge],spacings[maskSmall]]
    finalMass = np.r_[np.ones_like(spacings[maskLarge]) * largeMass, np.ones_like(spacings[maskSmall]) * smallMass]

    if returnFigure:
        fig, ax1  = plt.subplots(1, 1, figsize=[6,7])
        ax1.scatter(np.arange(unidist.shape[0])[maskLarge],spacings[maskLarge],s=300,color='r',alpha=0.5,edgecolors='k')
        ax1.scatter(np.arange(unidist.shape[0])[maskSmall],spacings[maskSmall])
        ax1.grid()
        ax1.set_xlabel('Body number')
        ax1.set_ylabel('Semimajor axis')

        return finalSemi, finalMass, fig

    return finalSemi, finalMass


if __name__ == '__main__':

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
    fig.show()


