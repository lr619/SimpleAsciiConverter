#Idea for image
'''
    create a python program that converts images to text art.
    Idea on how to do this.
        1. create a function to convert image to black and white
        2. convert BW image to an array list of pixel lists
        3. create a algorithm to determine whate charater to print based upon value in list per pixels
    

    what programs we will need???py
'''
from PIL import Image
from os import getcwd 

'''
files= listdir('.')#here we list out all images in the current directory

print('===========openable files===========')
for f in files:
    if ".py" not in f:
        print(" >>> ",f)
'''
cdirect=getcwd()
#n =input("write openable file name here:\n >>>>>")
n=str(cdirect+'\\tree.jpg')
print(n)

def filewrite(pd):
    with open('picdata.txt','w') as file:#this is just a way to check for received data
        file.write(str(pd)) 
'''==========================Create a list with file data==========================='''
m=Image.open(n,'r')
bwim=m.convert('L')
#issue: image is too large, for image set, therefore we need to compress the image
'''Figure out how to compress said image.'''
dim=m.size
print(f'size of picture is {dim}')

#in order for this to exactly work we need to compress the image. one way we can try to do that is by using the thumbnail image
bwim.thumbnail((50,50))

dim=bwim.size
pd=list(bwim.getdata())

'''
so in order to convert the images to a certain ascii character, we can determine that by writing creating a range of numbers for it to work.
'''
print(dim[0],dim[1])
tdlist=[]
for n in range(dim[0]):#converts the function to file
    templist=[]
    for i in range(dim[1]):
        templist.append(pd[(n*int(dim[0]))+i])
    tdlist.append(templist)

file=open('picdata.txt','w')
test=0
for i in tdlist:
    file.write(str(i)+'\n')
    test+=1
file.close()    
print(test)

for i in range(len(tdlist)):
    for n in range(len(tdlist[i])):
        val=tdlist[i][n]
        if int(val) >199 and int(val)<256:
            tdlist[i][n]="  "
        elif int(val)<200 and int(val)>49:
            tdlist[i][n]="//"
        else:
            tdlist[i][n]="||"
strlst=[]
for i in tdlist:
    string=''
    for n in i:
        string=string+str(n)
    strlst.append(string)
file2=open('pic.txt','w')
for i in strlst:
    file2.write(str(i)+'\n')

file2.close()
