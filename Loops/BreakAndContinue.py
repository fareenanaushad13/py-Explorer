# Break :  used to terinate the loop when encountered

# Continue: terminate execution in the current iteration & continue execution of the loop with the next iteration

#Break
i = 1
while i <= 5:
    print(i)
    if( i == 3):
        break
    i +=  1
print("loop end!!")    

#Continue
i = 0
while i < 5:
    if( i == 3):
        i += 1
        continue
    print(i)
    i += 1    

    
