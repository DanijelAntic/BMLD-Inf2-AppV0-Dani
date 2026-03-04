def umrechnen(meter):
    """
    Rechnet Meter in Zentimeter um.

    Args:
        meter: Wert in Meter (float oder int)

    Returns:
        float: Wert in Zentimeter
    """
    return meter * 100


def millimeter_zu_zentimeter(millimeter):
    """
    Rechnet Millimeter in Zentimeter um.

    Args:
        millimeter: Wert in Millimeter (float oder int)

    Returns:
        float: Wert in Zentimeter
    """
    return millimeter / 10


def meter_zu_kilometer(meter):
    """
    Rechnet Meter in Kilometer um.

    Args:
        meter: Wert in Meter (float oder int)

    Returns:
        float: Wert in Kilometer
    """
    return meter / 1000


def sekunden_zu_minuten(sekunden):
    """
    Rechnet Sekunden in Minuten um.

    Args:
        sekunden: Wert in Sekunden (float oder int)

    Returns:
        float: Wert in Minuten
    """
    return sekunden / 60


def minuten_zu_stunden(minuten):
    """
    Rechnet Minuten in Stunden um.

    Args:
        minuten: Wert in Minuten (float oder int)

    Returns:
        float: Wert in Stunden
    """
    return minuten / 60


def stunden_zu_tage(stunden):
    """
    Rechnet Stunden in Tage um.

    Args:
        stunden: Wert in Stunden (float oder int)

    Returns:
        float: Wert in Tagen
    """
    return stunden / 24


def tage_zu_monate(tage):
    """
    Rechnet Tage in Monate um (durchschnittlich 30,44 Tage pro Monat).

    Args:
        tage: Wert in Tagen (float oder int)

    Returns:
        float: Wert in Monaten
    """
    return tage / 30.44


def monate_zu_jahre(monate):
    """
    Rechnet Monate in Jahre um.

    Args:
        monate: Wert in Monaten (float oder int)

    Returns:
        float: Wert in Jahren
    """
    return monate / 12


def milligramm_zu_gramm(mg):
    """
    Rechnet Milligramm in Gramm um.

    Args:
        mg: Wert in Milligramm (float oder int)

    Returns:
        float: Wert in Gramm
    """
    return mg / 1000


def gramm_zu_kilogramm(g):
    """
    Rechnet Gramm in Kilogramm um.

    Args:
        g: Wert in Gramm (float oder int)

    Returns:
        float: Wert in Kilogramm
    """
    return g / 1000


def kilogramm_zu_tonne(kg):
    """
    Rechnet Kilogramm in Tonne um.

    Args:
        kg: Wert in Kilogramm (float oder int)

    Returns:
        float: Wert in Tonnen
    """
    return kg / 1000