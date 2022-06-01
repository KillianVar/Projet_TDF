def chemin(bdd, id1, id2):
    list1 = [[id1]]
    list2 = [[id2]]
    t = True
    while t:
        l1 = []
        for i in list1[-1]:
            l1.append(bdd[i]['father'])
            l1.append(bdd[i]['mother'])
        list1.append(l1)
        l2 = []
        for i in list2[-1]:
            l2.append(bdd[i]['father'])
            l2.append(bdd[i]['mother'])
        list2.append(l2)
        for i in range(len(list1)):
            for m in list1[i]:
                for j in range(len(list2)):
                    if m in list2[j]:
                        common_ancestor = m
                        t = False
        return f"Le plus court chemin vaut {i+j} et leur ancêtre commun est {common_ancestor}"
