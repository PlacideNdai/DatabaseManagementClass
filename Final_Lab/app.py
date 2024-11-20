while True:
    commend = int(input("""choose a command below: \n
    1) simple select 
    2) select from more than 1 table  
    3) subquery function  
    4) Group by 
    5) Update 
    6) Exist\n """))
    
    if commend == 6:
        print("bye..")
        break
    
    elif commend == 2:
        print("select from 2 or more tables")
    
    elif commend == 3:
        print("subquery select")
        
    elif commend == 4:
        print("Group by")
        
    elif commend == 5: 
        print("Update")
        
    else:
        print('simple select')
        