def afa_szamitas(nettó_ár, afa_szazalek=27):
    brutto_ár = nettó_ár * (1 + afa_szazalek / 100)
    return brutto_ár

# Példa használat
netto = 10000  # Ft
brutto = afa_szamitas(netto)
print(f"Nettó ár: {netto} Ft")
print(f"Bruttó ár: {brutto:.2f} Ft")
