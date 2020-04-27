# Binary Emulator
Jamie Sampson   
Spring 2019 : COM S 321 - Computer Architecture

## How to Use:
./run.sh <.machine file>

## Exporting:
Create Tar File: tar -czvf binary_emulator.tar.gz  submission
Unpack Tar File: tar -xzvf binary_emulator.tar.gz 

##Python Files
- conditionals.py : class for B.cond usage
- constants.py : currently, just static sizes of mem and stack
- decode.py : decodes the binary
- directory.py : list of all the legv8 instructions
- driver.py : calls decoding and executing
- emulate.py : actually calls the assembly instructions on the machine
- formatting.py : Enum of instruction types and all possible sub values
- helpers.py : print functions (like DUMP)
- instruction.py : class that holds an assembly instruction
- machine.py : class that to track and mock a machine
- register.py : class to do register formatting and printing

## Directories
- assembly_files  
    - legv8emul by Jeremy Sheaffer
- machine_files

## Scripts
- run.sh

## Misc.
- group.txt

## Tools
- IDE: PyCharm
- Language: Python


