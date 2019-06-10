adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
a=[i for i in adhoc if (i>5)]
b=[i for i in adhoc if (i<=2)]
print("Numbers greater than 5 are: ",a,"\nNumbers greater than equal to 2 are: ",b)
