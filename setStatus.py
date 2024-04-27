def setStatus(b1, y2, y1, status_n):
    b2 = abs(y2 - y1)
    bsize = b2
    status_a = status_n

    if (b2 - b1) / b1 < -0.01:
        status_n = 'Decreasing'
    elif (b2 - b1) / b1 > 0.025:
        status_n = 'Increasing'
    bsize = b2
    print(status_n)
    return bsize, b1, b2, y2, y1, status_a, status_n