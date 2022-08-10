def f(task):
    number=''
    arr=[]
    for i in task:
        
        if i.isdigit():
            number+=i
        elif i =='+':
            arr.append(int(number))
            arr.append('+')
            number=''
        elif i =='-':
            arr.append(int(number))
            arr.append('-')
            number=''
        elif i =='*':
            arr.append(int(number))
            arr.append('*')
            number=''
        else:
            arr.append(int(number))
            arr.append('/')
            number=''
    arr.append(int(number))
    
    pr=[arr[0]]
    for i in range(len(arr)-1):
        
        if arr[i]=='+':
            
            pr.append(int(arr[i+1]))
        elif arr[i]=='-':
            
            pr.append(-int(arr[i+1]))
        elif arr[i]=='*':
            
            pr[-1]=pr[-1]*int(arr[i+1])
        elif arr[i]=='/':
            
            pr[-1]=pr[-1]/int(arr[i+1])
        
    return sum(pr)


fg=True
task = '100/3/4*5-6'
print(f(task))