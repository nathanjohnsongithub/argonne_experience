class Workers:

    def __init__(self, name, wage, hours):
        self.name = name
        self.wage = wage
        self.hours = hours

    def to_string(self):
        return 'Name={}, Wage={}, Hours={}'.format(self.name, self.wage, self.hours)



n1 = Workers('Nathan', 20, 40)
k1 = Workers('Krisjanis', 25, 30)

print(n1.to_string)
print(k1.to_string)