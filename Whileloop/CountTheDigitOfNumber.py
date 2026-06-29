s="khaasi"
b="sikhaa"

fre1={}
fre2={}
for i in range(len(s)):
  if s[i] in fre1:
    
  
    fre1[s[i]]+=1
    

  else :
    fre1[s[i]]=1
    
for j in range(len(b)):
  if b[j] in fre2:
    
  
    fre2[b[j]]+=1
    

  else :
    fre2[b[j]]=1
    
    

print(fre1==fre2)






