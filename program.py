class Operation:
    def __init__(self,number1,number2) -> None:
        self.number1 = number1
        self.number2 = number2
    
    @property
    def multyply(self):
        return  self.number1 * self.number2
    
    @property
    def plus(self):
        return self.number1 + self.number2
    
    @property
    def minus(self):
        return self.number1 - self.number2
    @property
    def division(self):
        return self.number1 / self.number2
        
op = str(input(f"Enter your Operation: \t+\t-\tx\t/    :"))
while(op == "*"):
    m1 = float(input("Multyply operation,enter your number 1 :"))
    m2 = float(input("Multyply operation,enter your number 2 :"))
    multy = Operation(m1,m2)
    print(f"your operation is : ({multy.multyply})")
    continue

while(op == "+"):
    s1 = float(input("Plus operation,enter your number 1 :"))
    s2 = float(input("Plus operation,enter your number 2 :"))
    sumOp = Operation(s1,s2)
    print(f" your operation is : ({sumOp.plus})")       
    continue
while(op == "-"):
    m1 = float(input("Minus operation,enter your number 1 :"))
    m2 = float(input("Minus operation,enter your number 2 :"))
    minusOp = Operation(m1,m2)
    print(f" your operation is : ({minusOp.minus})")
    op = str(input(f"Enter your Operation: \t+\t-\tx\t/    :"))
    continue
while(op == "/"):
    d1 = float(input("Division operation,enter your number 1 :"))
    d2 = float(input("Division operation,enter your number 2 :"))
    divisionOp = Operation(d1,d2)
    print(f"Division operation,your operation is : ({divisionOp.division})")
  
