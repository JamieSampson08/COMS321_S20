import sys
from emulate import execute_assembly
from decode import decode
from machine import Machine

machine_state = Machine()


def main(argv):
    filename = argv[0]
    print("Decoding File: {}\n".format(filename))
    binary_instructions = decode(filename)

    print("Executing Instructions:")
    machine_state = execute_assembly(binary_instructions, filename)


if __name__ == "__main__":
   main(sys.argv[1:])