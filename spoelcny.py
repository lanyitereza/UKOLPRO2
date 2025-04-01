celkovyVydej = (cas1 + cas2) * 5
rozdil = celkoveKalorie - celkovyVydej
 
if rozdil > 0:
    print(f"přebytek: {rozdil:.f1} kcal")
elif rozdil < 0:
    print(f"Nedostatek: {-rozdil:.1f} kcal")
else:
    print("Kalorická bilance je vyrovnaná")
 