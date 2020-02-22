from tkinter import * #Comes Defalut With Python3
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import PIL # Install Using PIP
from PIL import ImageTk, Image
import sys

 
#Main Class Object
class application:
    def __init__(self,master):
        self.master = master
        self.c_size = (700,500)
        self.setup_gui(self.c_size)
        self.img=None
 
    def setup_gui(self,s):
        Label(self.master,text = 'Image Viewer',pady=5,bg='black',fg='white',
            font=('Ubuntu',15)).pack()
        self.canvas = Canvas(self.master,height=s[1],width=s[0],
            bg='black',bd=10,relief='ridge')
        self.canvas.pack()
        txt = '''
                    
                    ! No Image
        '''
        self.wt = self.canvas.create_text(s[0]/2-270,s[1]/2,text=txt
            ,font=('',30),fill='red')
        f=Frame(self.master,bg='white',padx=5,pady=5)
        Button(f,text='Open New Image',bd=2,fg='white',bg='black',font=('',15)
            ,command=self.make_image).pack(side=LEFT)
        f.pack()
        f2=Frame(self.master,bg='white',padx=5,pady=5)
        Button(f2,text='convert',bd=2,fg='white',bg='black',font=('',10),command=self.make_text).pack(side=LEFT)
        f2.pack()
        
        self.status=Label(self.master,text = 'Current Image: None',bg='gray',
            font=('Ubuntu',15),bd=2,fg='black',relief='sunken',anchor=W)
        self.status.pack(side=BOTTOM,fill=X)
 
 
    def make_image(self):
        try:
            File = fd.askopenfilename()

            self.pilImage = Image.open(File)
            re=self.pilImage.resize((700,500),Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(re)
            self.canvas.delete(ALL)
            self.canvas.create_image(self.c_size[0]/2+10,self.c_size[1]/2+10,
                anchor=CENTER,image=self.img)
            self.status['text']='Current Image:'+File

        except:
            ms.showerror('Error!','File type is unsupported.')


    def make_text(self):
        
        inimg = self.pilImage
        width, height = inimg.size
        aspect_ratio = height/width
        new_width = 70
        new_height = aspect_ratio * new_width * 0.9
        inimg = inimg.resize((new_width, int(new_height)))
        
        inimg = inimg.convert('L')
        pixels = inimg.getdata()

        # replace each pixel with a character from array
        chars = ["+","*","^","#","@","!","?","/","{","}","=","F","G","H","I","J","K"]
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)

        # split string of chars into multiple strings of length equal to new width and create a list
        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
        print(ascii_image)

        # write to a text file.
        with open("ascii_image.txt", "w") as f:
         f.write(ascii_image)


#creating object of class and tk window-
root=Tk()
root.configure(bg='white')
root.title('Image Viewer')
application(root)
root.resizable(0,0)
root.mainloop()