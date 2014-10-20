def menu_display(list_length):
    """
    Display de menu as long as the received messages are valid.
    The displayed menu is different for case when we did not yet introduced any list.
    :param list_length:int
    :return:none
    """
    if list_length != 0:
        print("1. Citirea unei liste de numere intregi")
        print("2. Gasirea secventei de lungime maxima care are toate elementele egale")
        print("3. Gasirea secventei de lungime maxima care are oricare doua elemente consecutive de semne contrare")
        print("4. Iesirea din aplicatie\n")
    else:
        print("1. Citirea unei liste de numere intregi")
        print("2. Iesirea din aplicatie\n")


def read_list(lista, n):
    """
    Read the n given elements of the list
    :param lista: list
    :param n: int
    :return: list
    """
    print("Introduceti elemenetele listei")
    for i in range(0, n):
        nr = int(input())
        lista.append(nr)
    return lista

def get_seq_equal_nos(lista, subseq):
    """
    Return the longest subsequence with equal element within given list .
    :param lista:list
    :param subseq:list
    :return:list
    """
    length = 1
    maxim = 1
    indice = 0
    elem = lista[0]
    n = len(lista)

    for i in range(0, n - 1):
        if lista[i] == lista[i + 1]:
            if lista[i] == elem:
                length += 1
        else:
            if length > maxim:
                maxim = length
                indice = i - maxim + 1
            elem = lista[i + 1]
            length = 1

    if length > maxim:
        maxim = length
        indice = n - maxim

    for i in range(indice, indice + maxim):
        nr = lista[i]
        subseq.append(nr)
    return subseq


def get_seq_nos_different_signs(lista, subseq):
    """
    Return the longest subsequence with different element signs within given list .
    :param lista: list
    :param subseq: list
    :return:list
    """
    length = 1
    maxim = 1
    indice = 0
    n = len(lista)
    for i in range(0, n - 1):
        if lista[i] * lista[i + 1] < 0:
            length += 1
        else:
            if length > maxim:
                maxim = length
                indice = i - maxim + 1
            length = 1
    for i in range(indice, indice + maxim):
        nr = lista[i]
        subseq.append(nr)
    return subseq


def main():
    should_run = True
    lista = []
    while should_run:
        lungime_sir = len(lista)
        menu_display(lungime_sir)
        ans = input("Ce doriti sa faceti?\n")
        if ans == "1":
            lista = []
            print("Introduceti numarul elementelelor listei")
            n = int(input("n="))
            lista = read_list(lista, n)

        elif ans == "2":
            subseq = []
            subseq = get_seq_equal_nos(lista, subseq)
            print("Subsecventa de lungime maxima care are numerele egale este: {} \n".format(subseq))
        elif ans == "3":
            subseq = []
            subseq = get_seq_nos_different_signs(lista, subseq)
            print(
                "Subsecventa de lungime maxima care are oricare doua elemente consecutine de lungime maxima este: {} \n"
                .format(subseq)
            )
        elif ans == "4":
            should_run = False
        else:
            print("Optiunea aleasa nu este valida\n")


if __name__ == "__main__":
    main()
