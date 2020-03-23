class Register:
    def __init__(self, number, is_conditional=False):

        # set usage
        if 0 <= number <= 7:
            self.use = "Arguments/Results"
        elif 9 <= number <= 15:
            self.use = "Temporaries"
        elif number == 16:
            self.use = "IP0"  # Linker's Scratch Register
        elif number == 17:
            self.use = "IP1" # Linker's Scratch Register
        elif number == 18:
            self.use = "Platform Register"
        elif 19 <= number <= 27:
            self.use = "Saved"
        elif number == 28:
            self.use = "SP"  # Stack Pointer
        elif number == 29:
            self.use = "FP"  # Frame Pointer
        elif number == 30:
            self.use = "LR"  # Return Address/Link Register
        elif number == 31:
            self.use = "XZR"  # Constant Value 0
        else:
            self.use = "General Register"

        self.data = 0
        self.reg_number = number
        self.is_conditional = is_conditional

    def print_register(self):
        use_info = "  "
        if self.use in ["XZR", "SP", "FP", "LR", "IP1", "IP0"]:
            use_info = "({})".format(self.use)
        information = "{:>5} X{:<3}: {:018x} ({:d})".format(use_info, self.reg_number, self.data, self.data)
        print(information)

