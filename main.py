def Virus_test(strchar):
   N=int(input())
   sample=list()
  
   if N>0 and N<11:
        for i in range(0,N):
         sample.insert(i,input())
        for j in range(0,N):
            temp=sample[j]
            m=0
            for k in range(0,len(temp)):
                c=temp[k]
                
                temp1=0
                count=0
                for l in range(0,len(strchar)):
                    if c==strchar[l]:
                        temp1=l
                        break
                        
                    count=count+1
                
                if count==len(strchar):
                    print("NEGATIVE")
                    break
                if temp1>m:
                    m=temp1
                if temp1<m:
                    print("NEGATIVE")
                    break
                if k==len(temp)-1:
                    print("POSITIVE")
   else:        
       return "invalid input"
   return ""
print(Virus_test(input()))        
    
