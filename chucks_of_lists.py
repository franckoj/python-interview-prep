#Break a list into chunks of size N in Python
#asked in micron interview 2022
def list_to_chuncks(l,n):
     x = [l[i:i+n] for i in range(0,len(l),n)]
     return x
