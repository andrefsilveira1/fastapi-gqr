def calculate_gqr(data):
    TotalGas, c1, c2, c3, nc4, ic4, nc5, ic5 = data
    gqr = TotalGas / (float(c1) +
                     2 * float(c2) +
                     3 * float(c3) +
                     4 * (float(nc4) + float(ic4)) +
                     5 * (float(nc5) + float(ic5)))
    
    return gqr
