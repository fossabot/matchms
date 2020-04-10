def set_ionmode_na_when_missing(spectrum_in):

    """set ionmode to 'n/a' if the metadata does not contain a key 'ionmode'."""

    spectrum = spectrum_in.clone()

    # Set ionmode to "n/a" when ionmode is missing from the metadata
    if spectrum.get("ionmode") is None:
        spectrum.set("ionmode", "n/a")

    return spectrum
