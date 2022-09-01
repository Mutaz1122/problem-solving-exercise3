from typing import List
txt = 'wePlayTennis'
def cap_space(txt: str) -> str:
    for i in range(len(txt)-1):
        t3=txt[i]  
        if t3.isupper():
           t1=txt[0:i]
           t2=txt[i+1:]
           txt=t1+" "+ t3.lower()+t2
           
           
    return txt     

cap_space(txt)      
