import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description='A simple command-line calculator.')

# Define the positional arguments
parser.add_argument('num1', type=float, help='The first number.')
parser.add_argument('num2', type=float, help='The second number.')
parser.add_argument('operator', type=str, help='The operator (+, -, *, /).')

# Parse the arguments
args = parser.parse_args()

# Perform the calculation based on the operator
if args.operator == '+':
    result = args.num1 + args.num2
elif args.operator == '-':
    result = args.num1 - args.num2
elif args.operator == '*':
    result = args.num1 * args.num2
elif args.operator == '/':
    result = args.num1 / args.num2
else:
    print("Invalid operator. Please use +, -, *, or /.")
    exit()

print(f"Result of {args.num1} {args.operator} {args.num2}: {result}")