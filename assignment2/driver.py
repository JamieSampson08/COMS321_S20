import sys

from decode import decode
from emulate import execute_assembly
from machine import Machine


def main(argv):
    machine_state = Machine()
    filename = argv[0]
    print("Decoding File: {}\n".format(filename))
    binary_instructions = decode(filename)

    print("\nExecuting Instructions:")
    machine_state = execute_assembly(binary_instructions, filename, machine_state)
    # ex_dump(machine_state)  # DEBUGGING


if __name__ == "__main__":
    main(sys.argv[1:])
