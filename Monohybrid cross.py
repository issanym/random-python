

def crossing():

    parent_1=input("Mother genotype: ")
    parent_2=input("Father genotype: ")

    #=================================================================================
    genotype1_1=parent_1[0].upper()+parent_1[1].lower()
    genotype2_1=parent_2[0].lower()+parent_2[1].upper()
    #=================================================================================
    genotype1_2=parent_1[0].lower()+parent_1[1].upper()
    genotype2_2=parent_2[0].upper()+parent_2[1].lower()
    #=================================================================================



    if parent_1==parent_1.upper(): 
        if parent_2==parent_2.upper():
            print("All the children will be homozygous Dominant")
        elif parent_2 == parent_2.lower():
            print("All the children will be heterozygous")
        else:
            print("50% of the children will be heterozygous and 50% will be homozygous Ressecive")

    elif parent_1==parent_1.lower():
        if parent_2==parent_2.lower():
            print("All the children will be homozygous Ressecive")
        elif parent_2 == parent_2.upper():
            print("All the children will be heterozygous")
        else:
            print("50% of the children will be heterozygous and 50% will be homozygous Ressecive")

    elif genotype1_1==parent_1:
        if parent_2==parent_2.upper():
            print("50% of the children will be heterozygous and 50% will be homozygous Dominant")
        elif parent_2==parent_2.lower():
            print("50% of the children will be heterozygous and 50% will be homozygous Ressecive")
        else:
            print("50% of the children will be heterozygous, 25% will hetrozygous dominat and 25% will heterozygous ressecive")

    elif parent_1 == genotype1_2:
        if parent_2 == parent_2.upper():
            print("50% of the children will be heterozygous and 50% will be homozygous Dominant")
        elif parent_2==parent_2.lower():
            print("50% of the children will be heterozygous and 50% will be homozygous Ressecive")
        else:
            print("50% of the children will be heterozygous, 25% will hetrozygous dominat and 25% will heterozygous ressecive")


while True:
    crossing()
    query = input("add a new cross? (yes/no): ").lower()
    if query != "yes":
        if query != 'Y':
          if  query != 'y':
                print("Bye Bye")
                break
