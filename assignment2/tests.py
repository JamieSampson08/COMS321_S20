import unittest
from decode import decode
from directory import instruct_dir


class MyTestCase(unittest.TestCase):

    # doesn't work anymore, but was used to test reading of B.cond values through Rt
    def test_bcond(self):
        test_opcode = instruct_dir["B.cond"]["opcode"].decode("utf-8")
        condaddr = "0000000000000000"
        rt = "00000"
        master_opcode = test_opcode + condaddr + rt
        instructions = decode(None, test_master_opcode=master_opcode)
        for i in instructions:
            print(i.assembly)


if __name__ == '__main__':
    unittest.main()
