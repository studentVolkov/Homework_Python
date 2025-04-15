class User:
    def __init__(self, first_name, last_name):
        self.fn = first_name
        self.ln = last_name

    def print_name(self):
        print(self.fn)

    def print_last_name(self):
        print(self.ln)

    def print_last_name_and_first_name(self):
        print(self.fn, self.ln, sep=" ")