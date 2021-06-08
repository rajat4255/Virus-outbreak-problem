def Virus_test(strchar):
   N=int(input())
   sample=list()
  
   if N>0 and N<11:
        for i in range(0,N):
         sample.insert(i,input())
        print(sample) 
           
   else:
       return "invalid input"

print(Virus_test(input()))        
    
