class Calculation:
    def __init__(self) -> None:
        self.num1 = None
        self.num2 = None

    def sume(self):
        return self.num1 + self.num2

    def tafrigh(self):
        return self.num1 - self.num2

    def zarb(self):
        return self.num1 * self.num2

    def taghsim(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero"