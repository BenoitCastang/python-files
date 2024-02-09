def fibonacci(first_term, second_term, last_term):
    print("\n1st term =", first_term) 
    print("2nd term =", second_term) 
    for i in range(last_term - 2):
        current_term = first_term + second_term
        first_term = second_term
        second_term = current_term
        if i == 0:
            print("3rd term =", current_term) 
        else:
            print(str(i + 3) + "th term =", current_term) 

fibonacci(int(input("First term: ")), int(input("Second term: ")), int(input("Last term: ")))
