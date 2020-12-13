import numpy as np

def generateObjects(nb_objects, mean):
    sigma = float(mean/4)
    return sigma * np.random.randn(nb_objects,2) + mean

def naif(data):

    pareto_optimal = []
    for i in data:
        dominated = False
        for j in data:
            if i != j and i[0]>=j[0] and i[1]>=j[1]:
                dominated = True
                break
        if not dominated:
            pareto_optimal.append(i)

    return pareto_optimal

def triLexico(data):

    pareto_optimal = []
    #lexiList = data

    for i in range(1,len(data)-1):
        x = data[i]
        j = i
        while j > 0 and (data[j-1][0] > x[0] or (data[j-1][0] == x[0] and data[j-1][1] > x[1])):
            data[j] = data[j-1]
            j -= 1
        data[j] = x

    pareto_optimal.append(data[0])

    min_c2 = data[0][1]
    id_min = 0
    for i in range(1,len(data)-1):
        if data[i][1] < min_c2 or (data[i] == data[id_min]):
            min_c2 = data[i][1]
            id_min = i
            pareto_optimal.append(data[i])

    return pareto_optimal


if __name__ == "__main__":
    nb_objects = 10
    mean = 4

    # Load of all the objects and their weigth
    data = generateObjects(nb_objects,mean).tolist()
    print(data)

    print(naif(data))
    print(triLexico(data))