
def Identify_Triplets(Array, size):

    Triplets = True


    for i in range(0, size-2):              #Getting the first value from the array
        num1 = Array[i]

        for j in range( i+1, size-1 ):      #Getting the second value from array
            num2 = Array[j]

            for k in range( i+3, size ):    #Getting the third value from array
                num3 = Array[k]
                sum= num1 + num2 + num3     #Adding all the three values and finding the sum of them

                if ( sum == 0 ):
                    print( "triplets are", Array[i], Array[j], Array[k])    #If the Sum comes as 0 then we got the triplets
                    Triplets = True

    if ( Triplets == False ):
        print(" Triplets does not exist ")



Array = [1,3,6,2,-1,2,8,-2,9]            #Initializing an array of numbers



size = len(Array)



Identify_Triplets( Array, size )