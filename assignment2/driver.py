import sys
from emulate import execute_assembly
from decode import decode


def main(argv):

    filename = argv[0]
    print("Decoding File: {}\n".format(filename))
    binary_instructions = decode(filename)

    print("Executing Instructions:")
    execute_assembly(binary_instructions)


if __name__ == "__main__":
   main(sys.argv[1:])