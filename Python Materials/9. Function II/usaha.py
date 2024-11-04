def beban_usaha(operasional, non_operasional):
    beban = operasional + non_operasional
    print(f"Beban usaha yang dikeluarkan sebesar : {beban}")
    return beban

def laba_bersih(laba_kotor, operasional, non_operasional):
    laba = laba_kotor - operasional - non_operasional
    print(f"Laba bersih yang dihasilkan sebesar : {laba}")
    return laba

