import random

def Rule1(IDList):
    ID=calculateID(IDList)
    if(IDList.count(ID)>=5):
        return ID
    else:
        return False

def Rule2(IDList):
    NearestNeighborsList=[IDList[1],IDList[3],IDList[4],IDList[6]]
    ID=calculateID(NearestNeighborsList)
    if(NearestNeighborsList.count(ID)>=3):
        return ID
    else:
        return False

def Rule3(IDList):
    FurtherNeighborsList=[IDList[0],IDList[2],IDList[5],IDList[7]]
    ID=calculateID(FurtherNeighborsList)
    if(FurtherNeighborsList.count(ID)>=3):
        return ID
    else:
        return False

def Rule4(IDList,probability):
    n=random.randrange(1, 100, 1, int)

    if(n<=probability):
        return calculateID(IDList)
    else:
        return False

def calculateID(id_list):
    NO_CELL = 0
    set_id = 0
    most_frequent = 0
    unique_vals = set(id_list)
    if len(id_list) > 0:
        for val in unique_vals:
            if val != NO_CELL and val != 1:
                frequence = id_list.count(val)
                #print(frequence)
                if frequence == most_frequent:
                    set_id = random.choice([set_id, val])           #if there is the same frequence of 2 IDs choice one
                elif frequence > most_frequent:
                    most_frequent = frequence
                    set_id = val                                    #set the most frequent ID
    return set_id