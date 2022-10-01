from Apartment import *

def mergesort(apartmentList):
    if len(apartmentList)>1:
        mid = len(apartmentList)//2
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]:
                apartmentList[k]=lefthalf[i]
                i=i+1
            else:
                apartmentList[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            apartmentList[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            apartmentList[k]=righthalf[j]
            j=j+1
            k=k+1


def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList)-1):
        if apartmentList[i] > apartmentList[i+1]:
            return False
    return True
        
    
def getBestApartment(apartmentList):
    mergesort(apartmentList)
    best = apartmentList[0]
    return best.getApartmentDetails()


def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    worst = apartmentList[-1]
    return worst.getApartmentDetails()


def getAffordableApartments(apartmentList, budget):
    mergesort(apartmentList)
    affordable = []
    
    for i in range(len(apartmentList)):
        if apartmentList[i].getRent() <= budget:
            affordable.append(apartmentList[i])

    affordableString = ''
    if len(affordable) == 0:
        return affordableString
    else:
        for j in range(len(affordable)-1):
            affordableString += affordable[j].getApartmentDetails() + '\n'
        affordableString += affordable[-1].getApartmentDetails()

    return affordableString
