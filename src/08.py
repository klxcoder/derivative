w1, b1, w2, b2 = 1, 0, 1, 0
x = 2

for i in range(1):
    y1 = w1 * x + b1
    y2 = w2 * y1 + b2
    # print(y2) # 2
    L = 1 / 2 * (y2 - 10) ** 2
    # print(L) # 32.0

alpha = 0.01

for i in range(50):
    # forward
    y1 = w1 * x + b1
    y2 = w2 * y1 + b2
    # calculate loss
    L = 1 / 2 * (y2 - 10) ** 2
    # calculate derivative of loss with respect to w2, b2
    dl_dy2 = y2-10
    dy2_dw2 = y1
    dy2_db2 = 1
    dl_dw2 = dl_dy2*dy2_dw2
    dl_db2 = dl_dy2*dy2_db2
    dy1_w1 = x
    dy1_b1 = 1
    # calculate derivative of loss with respect to w1, b1
    dy2_dy1 = w2
    dl_dy1 = dl_dy2 * dy2_dy1
    dy1_dw1 = x
    dy1_db1 = 1
    dl_dw1 = dl_dy1 * dy1_dw1
    dl_db1 = dl_dy1 * dy1_db1
    # Update w2, b2, w1, b1
    w2 = w2 - alpha * dl_dw2
    b2 = b2 - alpha * dl_db2
    w1 = w1 - alpha * dl_dw1
    b1 = b1 - alpha * dl_db1
    # print predicted value and loss
    print(f"{y2:.10f}, {L:.10f}")