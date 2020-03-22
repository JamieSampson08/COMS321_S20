class Register:
    def __init__(self, number, is_conditional=False):

        # set usage
        if 0 <= number <= 7:
            self.use = "Arguments/Results"
        elif 9 <= number <= 15:
            self.use = "Temporaries"
        elif 19 <= number <= 27:
            self.use = "Saved"
        elif number == 28:
            self.use = "Stack Pointer"
        elif number == 29:
            self.use = "Frame Pointer"
        elif number == 30:
            self.use = "Return Address"
        elif number == 31:
            self.use = "Constant Value 0"
        else:
            self.use = "General Register"

        self.address = 0 if number == 31 else None
        self.reg_number = number
        self.is_conditional = is_conditional

    def print_register(self):
        if self.address:
            print("X{} {:06x} {:010d}".format(self.reg_number, self.address, self.address))
        else:
            print("Register X{}'s Address is None".format(self.reg_number))
