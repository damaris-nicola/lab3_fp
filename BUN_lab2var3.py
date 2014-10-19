def afis_meniu(lungime_sir):
    if lungime_sir != 0:
        print("1. Citirea unei liste de numere intregi")
        print("2. Gasirea secventei de lungime maxima care are toate elementele egale")
        print("3. Gasirea secventei de lungime maxima care are oricare doua elemente consecutive de semne contrare")
        print("4. Iesirea din aplicatie\n")
    else:
        print("1. Citirea unei liste de numere intregi")
        print("2. Iesirea din aplicatie\n")


def citire_lista(sir, n):
    print("Introduceti elemenetele listei")
    for i in range(0, n):
        nr = int(input())
        sir.append(nr)
    return sir


def get_secv_elem_egale(sir, secv):
    lungime = 1
    maxim = 1
    indice = 0
    elem = sir[0]
    n = len(sir)

    for i in range(0, n - 1):
        if sir[i] == sir[i + 1]:
            if sir[i] == elem:
                lungime += 1
        else:
            if lungime > maxim:
                maxim = lungime
                indice = i - maxim + 1
            elem = sir[i + 1]
            lungime = 1

    if lungime > maxim:
        maxim = lungime
        indice = n - maxim

    for i in range(indice, indice + maxim):
        nr = sir[i]
        secv.append(nr)
    return secv


def get_secv_elem_semne_diferite(sir, secv):
    lungime = 1
    maxim = 1
    indice = 0
    n = len(sir)
    for i in range(0, n - 1):
        if sir[i] * sir[i + 1] < 0:
            lungime += 1
        else:
            if lungime > maxim:
                maxim = lungime
                indice = i - maxim + 1
            lungime = 1
    for i in range(indice, indice + maxim):
        nr = sir[i]
        secv.append(nr)
    return secv


def main():
    should_run = True
    sir = []
    while should_run:
        lungime_sir = len(sir)
        afis_meniu(lungime_sir)
        ans = input("Ce doriti sa faceti?\n")
        if ans == "1":
            sir = []
            print("Introduceti numarul elementelelor listei")
            n = int(input("n="))
            sir = citire_lista(sir, n)

        elif ans == "2":
            secv = []
            secv = get_secv_elem_egale(sir, secv)
            print("Subsecventa de lungime maxima care are numerele egale este: {}".format(secv))
        elif ans == "3":
            secv = []
            secv = get_secv_elem_semne_diferite(sir, secv)
            print(
                "Subsecventa de lungime maxima care are oricare doua elemente consecutine de lungime maxima este: {}"
                .format(secv)
            )
        elif ans == "4":
            should_run = False
        else:
            print("Optiunea aleasa nu este valida")


if __name__ == "__main__":
    main()
