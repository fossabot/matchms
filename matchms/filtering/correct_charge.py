import numpy


def correct_charge(spectrum_in):
    """correct the charge based on ionmode"""

    spectrum = spectrum_in.clone()

    ionmode = spectrum.get("ionmode", None)

    charge = spectrum.get("charge", None)

    if charge is None:
        charge = 0
    elif charge == 0 and ionmode == 'positive':
        charge = 1
    elif charge == 0 and ionmode == 'negative':
        charge = -1
    else:
        pass

    # Correct charge when in conflict with ionmode (trust ionmode more!)
    if numpy.sign(charge) == 1 and ionmode == 'negative':
        charge *= -1
    elif numpy.sign(charge) == -1 and ionmode == 'positive':
        charge *= -1

    spectrum.set("charge", charge)

    return spectrum
