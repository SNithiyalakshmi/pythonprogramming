 
def rotate(lst, y):
    return [lst[-x:] + lst[:-y]]
l=list(map(int,input().split(' ')))    
p=int(input())            
print(''.join(str(y) for y in rotate(l,p)))   
