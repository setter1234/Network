import os
content_range = []
basefilename = input("basefilename: if file1.txt file2.txt then input 'file' ")
lastfilename = input("lastfilename: if file1.txt file2.txt then input '.txt' ")
number = int(input("number of file: start from 0 input last number"))
print("input content range : start end\n")
for i in range(number+1):
    start,end = map(int,input().split())
    content_range.append([start,end,basefilename+str(i)+lastfilename])
    
content_range.sort(key=lambda x:x[0])
print(content_range)

f = open(content_range[0][2],"rb")
print(basefilename)
print(f)
line = f.read()
f.close()

for i in range(1,number+1):
    f = open(content_range[i][2],"rb")
    if(content_range[i-1][1] > content_range[i][1]):
        content_range[i][1] = content_range[i-1][1]
        continue
    elif(content_range[i-1][1] < content_range[i][0]):
        print(i)
        print(content_range[i-1][1])
        print(content_range[i][0])
        print("the file is omission\n")
        f.close()
        raise Exception
    else:
        line += f.read()[content_range[i-1][1]-content_range[i][0]+1:]
    f.close()

print(line)
print("don`t overlap your store filename to other\n")
store = input("input store file name :")
if not os.path.isfile(store):
    store = os.path.join(store)
    store = open(store,"wb")
    store.write(line)
    store.close()



