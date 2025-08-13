N = int(input("Enter N (1-10): "))

stack = []

stack.append((N, 'A', 'C', 'B', 0))

while stack:
    n, source, destination, auxiliary, state = stack.pop()

    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        continue

    if state == 0:
        
        stack.append((n, source, destination, auxiliary, 1))
        
        stack.append((n - 1, source, auxiliary, destination, 0))
    else:
        
        print(f"Move disk {n} from {source} to {destination}")
        
        stack.append((n - 1, auxiliary, destination, source, 0))
