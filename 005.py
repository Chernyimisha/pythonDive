# выввести в консоль таблицу умножения как в тетрадке

for i in range(2, 10, 4):
    for j in range(1, 11):
        for k in range(i, i + 4):
            print(f"{k:>1} x {j:>2} = {k*j:>2}", end=" \t")
        print()
    print()

