import sys
from emulate import execute_assembly
from decode import decode
from machine import Machine


def main(argv):
    machine_state = Machine()
    filename = argv[0]
    print("Decoding File: {}\n".format(filename))
    binary_instructions = decode(filename, machine_state)
    exit(1)
    print("Executing Instructions:")
    machine_state = execute_assembly(binary_instructions, filename, machine_state)


if __name__ == "__main__":
   main(sys.argv[1:])