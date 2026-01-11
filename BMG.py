# Virtual Logic Circuit Simulator
# Simulates AND, OR, XOR, NOT logic gates
# Also generates truth tables for all gates

# === LOGIC GATE FUNCTIONS ===
def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def XOR(a, b):
    return a ^ b

def NOT(a):
    return 0 if a == 1 else 1


# === PART 1: USER INPUT ===
print("=== Logic Gate Simulator ===")
print("1 - AND")
print("2 - OR")
print("3 - XOR")
print("4 - NOT")

choice = int(input("Select a logic gate: "))

if choice == 4:
    a = int(input("Enter input A (0 or 1): "))
    print("NOT Result:", NOT(a))
else:
    a = int(input("Enter input A (0 or 1): "))
    b = int(input("Enter input B (0 or 1): "))

    if choice == 1:
        print("AND Result:", AND(a, b))
    elif choice == 2:
        print("OR Result:", OR(a, b))
    elif choice == 3:
        print("XOR Result:", XOR(a, b))
    else:
        print("Invalid selection!")


# === PART 2: TRUTH TABLES ===
print("\n=== TRUTH TABLES ===")

# AND gate
print("\nAND Gate")
print("A B | Result")
for A in [0, 1]:
    for B in [0, 1]:
        print(A, B, "|", AND(A, B))

# OR gate
print("\nOR Gate")
print("A B | Result")
for A in [0, 1]:
    for B in [0, 1]:
        print(A, B, "|", OR(A, B))

# XOR gate
print("\nXOR Gate")
print("A B | Result")
for A in [0, 1]:
    for B in [0, 1]:
        print(A, B, "|", XOR(A, B))

# NOT gate
print("\nNOT Gate")
print("A | Result")
for A in [0, 1]:
    print(A, "|", NOT(A))

# === COMBINED EXPRESSION ===
print("\nTruth Table for A AND (B OR C)")
print("A B C | Result")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            result = AND(A, OR(B, C))
            print(A, B, C, "|", result)
