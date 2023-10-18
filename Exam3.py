def tri_a_bulles(tableau):
    n = len(tableau)

    for i in range(n):
        
        nombre = False

        for j in range(0, n-i-1):
            if tableau[j] > tableau[j+1]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]

                nombre = True


        if not nombre:
            break

    return tableau

tableau = [1,5,3,6,2,4]
tri_a_bulles(tableau)
print("Tableau trié :", tableau)