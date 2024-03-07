count=0
number_of_tests=3
number_of_students=5

while count < number_of_students:
    input("What is your name: ")
    test1= int(input("Test 1 score score : "))
    test2= int(input("Test 2 score score : "))
    test3= int(input("Test 3 score score : "))
    
    total_score=(test1+test2+test3)
    average_score=(total_score/number_of_tests)
    
    print(f"Your total score is {total_score}\n Your average is {average_score}")
    
    count +=1