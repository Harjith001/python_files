I=[]
F=[]
#Read the Inputs and Assign to the respective list
#@start-editable@

S = []
def inp():
    for i in range(0,3):
        I.append(float(input()))
        F.append(float(input()))

#@end-editable@

#define function for inflationrate
#@start-editable@
   
def inflationrate():
    for i in range(0,3):
        S.append(((F[i] - I[i])/I[i])*100)
    return S

#@end-editable@
    
#define function for averageinflationrate
#@start-editable@
   
def average_inflation_rate():
    return ((sum(S)/len(S)))

inp()
inflationrate()

#@end-editable@


AIF=average_inflation_rate()
#Average Inflation rate value in 4 precision format
#@start-editable@
   
print('{0:.4f}'.format(AIF))

#@end-editable@