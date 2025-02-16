import qrcode

flag = "MAGNUS{st9s_2nd_3ncrypt10n_1s_4lw4ys_b3tt3r}"
qr = qrcode.make(flag)
qr.save("flag_qr.png")

print("QR Code saved as flag_qr.png")

