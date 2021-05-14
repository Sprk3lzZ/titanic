import pandas
def distance(x1 = 0,x2 = 0):
    """
    Arguments: [x1:(float) first position, x2:(float) second position]
    Return: The distance x1/x2
    """
    return abs(x1 - x2)
def main(file, k, age):
    csv = get_info(file)
    print(read_info(csv, csv.Age, age))
    return True
def get_info(file):
    return pandas.read_csv(file, sep = ',')
def read_info(csv, param, reference):
    closerID, closerDist,closerValue= csv.PassengerId[0], distance(param[0],reference),param[0]
    for i in range(len(param)):
        if(distance(param[i], reference) < closerDist):
            closerID, closerDist,closerValue= csv.PassengerId[i], distance(param[i],reference),param[i]
    return closerID,closerDist,closerValue
def read_infoStr(csv, param, reference):
    closerID, closerValue= csv.PassengerId[0], param[0]
    for i in range(len(param)):
        if(distance(param[i], reference) == closerDist):
            closerID, closerDist,closerValue= csv.PassengerId[i], distance(param[i],reference),param[i]
    return closerID,closerDist,closerValue

main("titanic.csv", 1, 94)