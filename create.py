from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy as np 

from . import logger

def calcSemis(totalMass, smallMass, largeMass, nSmall, inner, outer, alpha):
    """
    the purpose of this code is to calculate the position of bodies
    in a disk matching a given surface density profile

    the code assumes a bimodal mass distribution with small and large bodies
    commonly refered to as planetesimals and embryos

    args:
        totalMass:: the desired total mass in the disk in earth-masses
        smallMass:: the mass of each small body in earth-masses
        largeMass:: the mass of each large body in earth-masses
        nSmall:: the number of small bodies
        inner:: the inner orbital distance of the disk in AU
        outer:: the outer orbital distance of the disk in AU
        alpha:: the disk surface density profile where
            sigma propto mass**-alpha
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
        maskLarge[int(i*pos)+(0.5*pos)] = True
        maskSmall[int(i*pos)+(0.5*pos)-(massMultiplier/2):int(i*pos)+(0.5*pos)+(massMultiplier/2)] = False

    finalSemi = np.r_[spacings[masklarge],spacings[masksmall]]
    finalMass = np.r_[np.ones_like(spacings[masklarge]) * largemass, np.ones_like(spacings[masksmall]) * smallmass]

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

    calcSemis(totalmass, smallmass, largemass, nsmallbodies, inner, outer, alpha)

    plt.scatter(np.arange(unidist.shape[0])[masklarge],spacings[masklarge],s=300,color='r',alpha=0.5,edgecolors='k')
    plt.scatter(np.arange(unidist.shape[0])[masksmall],spacings[masksmall])
    plt.grid()
    plt.xlabel('Body number')
    plt.ylabel('Semimajor axis')
