class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def display(c):
        if c.img>0:
            return f"{c.real} + {c.img}i"
        else:
            return f"{c.real} {c.img}i"

    def add(self,c2):
        return Complex(self.real+c2.real, self.img+c2.img)

    def sub(self,c2):
        return Complex(self.real-c2.real, self.img-c2.img)

    def multiply(self,c2):
        real=(self.real*c2.real)-(self.img*c2.img)
        img=(self.img*c2.real)+(self.real*c2.img)
        return Complex(real,img)

print("First Complex number:")
real1=int(input("Real part:"))
img1=int(input("Imaginary part:"))
a=Complex(real1,img1)

print("Second Complex number:")
real2=int(input("Real part:"))
img2=int(input("Imaginary part:"))
b=Complex(real2,img2)

print(f"Addition: {a.add(b).display()}")
print(f"Subtraction: {a.sub(b).display()}")
print(f"Multiplication: {a.multiply(b).display()}")


