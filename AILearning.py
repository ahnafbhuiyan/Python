def main():
    #Sets
    shapes = ["square",'circle']
    setOfShapes = set(shapes)
    print (setOfShapes)
    setOfShapes.add('rectangle')
    print(setOfShapes)
    print("g" in setOfShapes)
    newShapes = {'square','circle'}
    print(setOfShapes|newShapes)
    #

    #Dictionaries
    roomNumbers = {'Abishan': 1,'Ahnaf': {2,"yes"}, 'Dinith': [3,"Dinousar"],'Mo': 4, 'Azen': 5}
    print(roomNumbers['Abishan'])
    del roomNumbers['Azen']
    print(roomNumbers)
    roomNumbers['Abishan'] = [1,"funny"]
    print(roomNumbers['Abishan'])
    print(roomNumbers.keys())
    print(roomNumbers.values())
    print(roomNumbers.items())
    print(len(roomNumbers))
    #does not work: roomNumbers.add['Azen':5]
    #

    #Script with Dictionary
    fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}

    for fruit, price in fruitPrices.items():
        if price<2.00:
            print("%s cost %f a pound" %(fruit,price))
        else:
            print(fruit+ " too expensive")
    #

    
    #List comprehensions: Lambda, map, filter 
    m = (list(map(lambda x:x*x, [1,2,3])))
    print (m)

    f= list(filter(lambda x:x>2, m))
    print (f)
    
            

if __name__=='__main__':
    main()
    
