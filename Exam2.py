def tri_a_bulles(montableau):
    n = len(montableau)
    for i in range(n):

        echanger = False


        for i in range(0, n-i-1):

            if montableau[i] > montableau[i+1]:
                montableau[i], montableau[i+1] = montableau[i+1], montableau[i]
                echanger = True


        if not echanger:
            break

    return montableau

def parcours(montableau):
    print("Tableau original : ", montableau)
    tableau_tri = tri_a_bulles(montableau)
    print("Tableau trié : ", tableau_tri)

parcours([1, 5, 3, 6, 2, 4])
