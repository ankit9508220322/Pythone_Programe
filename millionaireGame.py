questions = [

    ["Which of the following best defines a data structure?",
     "A programming language", "A way to store, organize, and manage data",
     "A software development tool", "An algorithm", 2],

    ["Which of the following is NOT a type of data structure?",
     "Primitive", "Abstract", "Derived", "Logical", 4],

    ["Which data structure supports random access?",
     "Stack", "Queue", "Array", "Linked List", 3],

    ["Memory allocation for arrays is generally done in:",
     "Heap", "Stack", "Contiguous memory locations", "Random locations", 3],

    ["A sparse matrix is a matrix with:",
     "Mostly zero values", "Mostly non-zero values",
     "Only diagonal elements", "Only one row", 1],

    ["Which representation is suitable for sparse matrices?",
     "Regular 2D array", "Linked list representation",
     "Single variable", "Hash table", 2],

    ["Which of the following is TRUE about stack?",
     "FIFO", "LIFO", "Random access", "Used for BFS", 2],

    ["The postfix form of (A + B) * C is:",
     "AB + C *", "A + BC *", "AB C + *", "AB + *C", 3],

    ["Which data structure is used in expression evaluation?",
     "Queue", "Stack", "Tree", "Graph", 2],

    ["Infix to postfix conversion uses which traversal order?",
     "BFS", "DFS", "Stack-based evaluation", "Backtracking", 3],

    # ... continue same pattern for remaining questions ...

]

# Loop for each question
for q in questions:
    print("\n--------------------------------------")
    print(q[0])
    print("a.", q[1])
    print("b.", q[2])
    print("c.", q[3])
    print("d.", q[4])
    print("\n");
    # User answer
    ans = int(input("Enter your answer "))

    # Check answer
    if ans == q[5]:
        print("Correct Answer !Congratulations")
    else:
        print(f"Incorrect!answer Correct answer is OPTIONS {q[5]}.")
