

def calculate_total(ot, st, im, hc):
    if hc and ot > 15:
        ot -= 5
        if im:
            ot -= (0.1 * ot)
    ot += (st * ot)
    return ot