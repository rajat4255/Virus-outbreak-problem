def Virus_test(strchar):
   N=int(input())
   sample=list()
   for i in range(0,N):
      sample.insert(i,input())
       
   if N>0 and N<11:
        print(sample) 
           # TODO: write code...
   else:
       return "invalid input"

print(Virus_test(input()))        
        
