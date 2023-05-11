#t**2-3*t+1=0
#differential equations
def square(a, b, c):
   d=(b**2-4*a*c)
   t1=(-b-d**0.5)/2*a
   t2=(-b+d**0.5)/2*a

   if(d > 0):
      z = "y == c1*e**({}*x)+c2**({}*x)"
      print(z.format(t1, t2))
   elif(d == 0): 
      z = "y == e**(t*x)*(c1+c2*x)"
      print(z.format(t1, t2))
   else:
      z = "y == e**(k1*x)*(c1*(math.cos(p*x)))+c2*(math.sin(p*x))"
      print(z.format(t1, t2))


square(2, -3, 1)
