"""This software compares the contents of two directory paths by analyzing the
contents of each folder and each item's size within the folder. If any folders/files
are different or have a different size, their file path and name will be printed
in the shell.
"""
#TEST1


from Tkinter import *
import tkFileDialog
import tkMessageBox
import os


#detele this line:
w = 3


def choosePath1():
    folderPath = tkFileDialog.askdirectory()
    Path1Dict = createDict(folderPath)
    pathName1.set(folderPath)
    return Path1Dict
    
def choosePath2():
    folderPath = tkFileDialog.askdirectory()
    Path2Dict = createDict(folderPath)
    pathName2.set(folderPath)
    return Path2Dict

def compareDict():
    Path1Dict = createDict(pathName1.get())
    Path2Dict = createDict(pathName2.get())

    #Compare Path1Dict to path2Dict
    for item in Path1Dict.keys():
        #Compare each file name in Path1Dict to Path2Dict
        if item not in Path2Dict:
            textBox1.insert(END, '+:\'' + item + '\'\n')
        else:       
            #Compare each file size in Path1Dict to Path2Dict
            if Path1Dict[item] != Path2Dict[item]:
                textBox3.insert(END, item + 'size: 1)' + str(Path1Dict[item])+ ' vs. 2)' + str(Path2Dict[item]) + ' bytes\n')
                #print(item + ' is ' + str(Path1Dict[item]) + ' bytes in Directory 1, but ' + str(Path2Dict[item]) + ' bytes in Directory 2')

    #Compare Path2Dict to path1Dict (Look for files not in 1 that are in 2)
    for item in Path2Dict.keys():
        #Compare each file name in Path1Dict to Path2Dict
        if item not in Path1Dict:
            textBox2.insert(END, '+:\'' + item + '\'\n')
        else:       
            pass


       

def createDict(folderDir):
    contents1 = os.listdir(folderDir)
    #path1 = pathName1.get()
    #contents1 = os.listdir(path1)
    print contents1
    #fullname = folderName +'//'+ contents1[0]
    #print fullname
    totalSize=0
    dict1 = {}
    for item in contents1:

        #If a file, get it's name (key) and assign it it's size (value)
        if os.path.isfile(os.path.join(folderDir, item)):            
            fileSize = os.path.getsize(os.path.join(folderDir, item))
            dict1[item] = fileSize
            totalSize += fileSize

        #If a folder, walk through all it's contents and add the size
        elif os.path.isdir(os.path.join(folderDir, item)):
            dirSize = 0
            for root, dirs, files in os.walk(os.path.join(folderDir, item), topdown=False):
                
                for name in files:
                    dirSize += os.path.getsize(os.path.join(root, name))
                for name in dirs:
                    pass
            #textBox.insert(END, 'Total size of ' + item + ' is: ' + str(dirSize) + '\n')
            #print 'Total size of ' + item + ' is: ' + str(dirSize)
            dict1[item] = dirSize
            totalSize += dirSize

        else:
            print 'Error: unrecognized item in folder'

    print 'Total folder size: ' + str(totalSize)
    return dict1



root = Tk()
root.title("PDF_GUI")
root.geometry("1100x650+20+20")




#SET BOX LENGTHS AND POSITIONS
column1x = 20
column2x = 515
column3x = 590
row1y = 50
rowDist = 40
pathNameTextBoxLength = 80
browseButtonWidth = 8
pathPageBoxLength = 10



#TEXT: PATH 1 NAME
pathName1 = StringVar(None)
pathName1text = Entry(root, width = pathNameTextBoxLength, textvariable = pathName1)
pathName1text.place(x=column1x, y=row1y)

#PUSH BUTTON: BROWSE for PATH 1
button1 = Button(root, text = "Browse", width = browseButtonWidth, command = choosePath1)
button1.place(x=column2x, y=row1y-3)


#TEXT: PATH 2 NAME
pathName2 = StringVar(None)
pathName2text = Entry(root, width = pathNameTextBoxLength, textvariable = pathName2)
pathName2text.place(x=column1x, y=row1y + rowDist)

#PUSH BUTTON: BROWSE for PATH 2
button2 = Button(root, text = "Browse", width = browseButtonWidth, command = choosePath2)
button2.place(x=column2x, y=row1y-3 + rowDist)

#PUSH BUTTON: COMPARE
button2 = Button(root, text = "Compare Directories", width = browseButtonWidth*3, height = 2, command = compareDict)
button2.place(x=column2x+200, y=row1y+10)



#TEXT BOX 1: Values only in Directory 1
labelText1 = StringVar() #create a string GUI object
labelText1.set("Items only in Directory 1")
label1 = Label(root, textvariable = labelText1, height = 4) #define attributes of label
label1.place(x = 200, y = 160) #where to place it
textBox1 = Text(root, height = 10, width = 60) #CREATES LARGE TEXT BOX
#textBox1.insert(END, "Select student information above")
textBox1.place(x = 10, y = 220)
#textBox1.tag_config(height = 20, width = 40)


#TEXT BOX 2: Values only in Directory 2
labelText2 = StringVar() #create a string GUI object
labelText2.set("Items only in Directory 2")
label2 = Label(root, textvariable = labelText2, height = 4) #define attributes of label
label2.place(x = 700, y = 160) #where to place it
textBox2 = Text(root, height = 10, width = 60) #CREATES LARGE TEXT BOX
#textBox2.insert(END, "Select student information above")
textBox2.place(x = 550, y = 220)
#textBox2.tag_config(height = 20, width = 40)


#TEXT BOX 3: Show item size mismatches
labelText3 = StringVar() #create a string GUI object
labelText3.set("Items with different sizes in each directory: (Dir 1 vs Dir 2)")
label3 = Label(root, textvariable = labelText3, height = 4) #define attributes of label
label3.place(x = 375, y = 400) #where to place it
textBox3 = Text(root, height = 10, width = 120) #CREATES LARGE TEXT BOX
#textBox3.insert(END, "Select student information above")
textBox3.place(x = 50, y = 460)

#textBox3.tag_config(height = 20, width = 40)


root.mainloop()
