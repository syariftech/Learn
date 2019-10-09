import cv2

import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import proses as p
import sys

class Main(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self)
        self.parent = parent
        
#frame judul
        self.MainFrame = tk.Frame(self.parent, width=1350,background="red")
        self.MainFrame.grid(row=0, column=0, columnspan=3, padx=10, pady=15, sticky="NSEW")
        self.MainFrame.grid_propagate(0)
#frame input gambar
        self.MainFrame1 = tk.LabelFrame(self.parent, height=0, background="lightblue", text="Open Image", font="Arial 14", fg="black")
        self.MainFrame1.grid(row=1, column=0, padx=10, sticky="NSEW")
        self.MainFrame1.grid_propagate(0)
#hsv
        self.MainFrame2 = tk.LabelFrame(self.parent, height=70, background="lightblue", text="Method", font="Arial 14", fg="black")
        self.MainFrame2.grid(row=2, column=0, padx=10, sticky="NSEW")
        self.MainFrame2.grid_propagate(0)
#prapengolahan
        self.MainFrame3 = tk.LabelFrame(self.parent, width=150 ,height=300, background="lightblue", text="Pra Pengolahan", font="Arial 14", fg="black")
        self.MainFrame3.grid(row=3, column=0, rowspan=1,padx=10, sticky="NSEW")
        self.MainFrame3.grid_propagate(0)
##proses
        self.MainFrame4 = tk.Frame(self.parent, height=100, background="lightblue")
        self.MainFrame4.grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")
        self.MainFrame4.grid_propagate(0)
#output
        self.MainFrame5 = tk.LabelFrame(self.parent, background="lightblue", text="Output", font="Arial 14", fg="black")
        self.MainFrame5.grid(row=2, column=1, rowspan=3, columnspan=4, padx=0, sticky="NSEW")
        self.MainFrame5.grid_propagate(0)
#footer
        self.MainFrame6 = tk.LabelFrame(self.parent, height=50, width=1000, text="Made By : ", background="lightgray")
        self.MainFrame6.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="NSEW")
        self.MainFrame6.grid_propagate(0)
        
        self.form()
                   
    def form(self):
        
#frame judul
        #logo
        self.PathTestingImg = "F:\Kuliah\Semester 6\Proposal Bissmillah\Program\logo.png"
        self.imT = Image.open(self.PathTestingImg)
        self.imT = ImageTk.PhotoImage(self.imT)
        self.label1 = tk.Label(self.MainFrame, bg="spring green2", image=self.imT)
        self.label1.pack(side="top")
        
#frame 1
#label data training
        self.label1 = tk.Label(self.MainFrame1, text="Image Training", font="Georgia", relief="ridge", background="lightblue")
        self.label1.grid(row=3, column=0, sticky="NSEW", padx=8, pady=10)
        #textbox data training
        bukadatatraining = tk.StringVar(self.MainFrame1, value="")
        self.textboxdatatraining = tk.Entry(self.MainFrame1, textvariable = bukadatatraining, width=50)
        self.textboxdatatraining.grid(row=3, column=1, sticky="NSEW", pady=10)
        #button browse training
        self.path = tk.Button(self.MainFrame1, text="Browse", font="Georgia", width=8, background="lightblue", command=lambda:bukadatatraining.set(filedialog.askdirectory()))
        self.path.grid(row=3, column=5, padx=5)
        
        #label data testing
        self.label2 = tk.Label(self.MainFrame1, text="Image Testing", font="Georgia", relief="ridge", background="lightblue")
        self.label2.grid(row=4, column=0, sticky="NSEW", padx=8, pady=10)
        #textbox data testing
        bukadatatesting = tk.StringVar(self.MainFrame1, value="")
        self.textboxdatatesting = tk.Entry(self.MainFrame1, textvariable = bukadatatesting, width=50)
        self.textboxdatatesting.grid(row=4, column=1, sticky="NSEW", pady=10)
        #button browse testing
        self.path1 = tk.Button(self.MainFrame1, text="Browse", font="Georgia", width=8, background="lightblue", command=lambda:bukadatatesting.set(filedialog.askopenfilename()))
        self.path1.grid(row=4, column=5, sticky="", padx=5, pady=5)
    
#frame 2
#radio button HSV
        var = tk.IntVar(self.MainFrame2)
        self.label = tk.Label(self.MainFrame2, text="HSV", width=12, font="Georgia", relief="ridge", background="lightblue")
        self.label.grid(row=5, column=0, padx=8 , pady=10)
        
        self.radiobutton = tk.Radiobutton(self.MainFrame2, text="Hue", variable=var, value=0, background="lightblue", command=self.selchue)
        self.radiobutton.grid(row=5, column=1, padx=10)
        
        self.radiobutton1 = tk.Radiobutton(self.MainFrame2, text="Saturation", variable=var, value=1, background="lightblue", command=self.selcstr)
        self.radiobutton1.grid(row=5, column=2, padx=10)
        
        self.radiobutton2 = tk.Radiobutton(self.MainFrame2, text="Value", variable=var, value=2, background="lightblue", command=self.selcvle)
        self.radiobutton2.grid(row=5, column=3, padx=10)
        
        self.radiobutton3 = tk.Radiobutton(self.MainFrame2, text="HSV Colour", variable=var, value=3, background="lightblue", command=self.selchsv)
        self.radiobutton3.grid(row=5, column=4, padx=10)       
        
#frame 3
#proses prapengolahan
        
#label hasil image selected
        self.asli ='noimage.png'
        self.noimage = Image.open(self.asli)
        self.noimage = self.noimage.resize((170, 227), Image.ANTIALIAS)
        self.noimage = ImageTk.PhotoImage(self.noimage)
        self.CitraAsli = tk.Label(self.MainFrame3, bg="blue", image=self.noimage)
        self.CitraAsli.grid(row=2, column=0, padx=3, pady=3, sticky="NSEW")
        
        self.asli = tk.Label(self.MainFrame3, text="Image Selected", font="Georgia", background="lightblue")
        self.asli.grid(row=0, column=0, padx=30, pady=0)
               
#label hasil image testing
        self.asli ='noimage.png'
        self.noimageHist = Image.open(self.asli)
        self.noimageHist = self.noimageHist.resize((170, 227), Image.ANTIALIAS)
        self.noimageHist = ImageTk.PhotoImage(self.noimageHist)
        self.CitraHist = tk.Label( self.MainFrame3, bg="blue", image=self.noimageHist)
        self.CitraHist.grid(row=2, column=1, padx=3, pady=3)
        
        self.lblhist = tk.Label(self.MainFrame3, text="Image Histogram EQ", font="Georgia", background="lightblue")
        self.lblhist.grid(row=0, column=1, padx=30, pady=0)
        
#frame 4
        #button proses
        self.path = tk.Button(self.MainFrame4, command =self.proses,text="Calculate", font="arial 12 bold", width=8, height = 2, background="lightblue")
        self.path.grid(row=5, column=0, padx=5)
        self.path = tk.Button(self.MainFrame4, command =self.testing,text="Testing", font="arial 12 bold", width=8, height = 2, background="lightblue")
        self.path.grid(row=5, column=1, padx=5)
        self.path = tk.Button(self.MainFrame4, command =self.clearform,text="Refresh", font="arial 12 bold", width=8, height = 2, background="lightblue")
        self.path.grid(row=5, column=2, padx=5)
        self.path = tk.Button(self.MainFrame4, command = self.close_window,text="Exit", font="arial 12 bold", width=7, height = 2, background="lightblue", foreground="red")
        self.path.grid(row=5, column=3, padx=5)
        
#frame 5
#        output
#        label hasil hue
        self.asli ='noimage2.png'
        self.huenoimage = Image.open(self.asli)
        self.huenoimage = self.huenoimage.resize((120, 150), Image.ANTIALIAS)
        self.huenoimage = ImageTk.PhotoImage(self.huenoimage)
        self.Citrahue = tk.Label(self.MainFrame5, bg="blue", image=self.huenoimage)
        self.Citrahue.grid(row=1, column=0, padx=5, pady=0,)
        
        self.lblhue = tk.Label(self.MainFrame5, text="Hue", font="Georgia", background="lightblue")
        self.lblhue.grid(row=0, column=0)
        
        #label hasil saturation
        self.asli ='noimage2.png'
        self.stnoimage = Image.open(self.asli)
        self.stnoimage = self.stnoimage.resize((120, 150), Image.ANTIALIAS)
        self.stnoimage = ImageTk.PhotoImage(self.stnoimage)
        self.Citrast = tk.Label(self.MainFrame5, bg="blue", image=self.stnoimage)
        self.Citrast.grid(row=1, column=1, padx=5, pady=0,)
        
        self.lblst = tk.Label(self.MainFrame5, text="Saturation", font="Georgia", background="lightblue")
        self.lblst.grid(row=0, column=1)
        
        #image hasil Value
        self.asli ='noimage2.png'
        self.vlunoimage = Image.open(self.asli)
        self.vlunoimage = self.vlunoimage.resize((120, 150), Image.ANTIALIAS)
        self.vlunoimage = ImageTk.PhotoImage(self.vlunoimage)
        self.Citravlu = tk.Label(self.MainFrame5, bg="blue", image=self.vlunoimage)
        self.Citravlu.grid(row=1, column=2, padx=5, pady=0,)
        
        self.lblvlu = tk.Label(self.MainFrame5, text="Value", font="Georgia", background="lightblue")
        self.lblvlu.grid(row=0, column=2)
        
        #label HSV
        self.asli ='noimage2.png'
        self.hsvnoimage = Image.open(self.asli)
        self.hsvnoimage = self.hsvnoimage.resize((120, 150), Image.ANTIALIAS)
        self.hsvnoimage = ImageTk.PhotoImage(self.hsvnoimage)
        self.Citravhsv = tk.Label(self.MainFrame5, bg="blue", image=self.hsvnoimage)
        self.Citravhsv.grid(row=1, column=3, padx=5, pady=0,)
        
        self.lblhsv = tk.Label(self.MainFrame5, text="HSV Colour", font="Georgia", background="lightblue")
        self.lblhsv.grid(row=0, column=3)

        #label hasil output
        self.asli ='noimage3.png'
        self.hsloutnoimage = Image.open(self.asli)
        self.hsloutnoimage = self.hsloutnoimage.resize((236, 270), Image.ANTIALIAS)
        self.hsloutnoimage = ImageTk.PhotoImage(self.hsloutnoimage)
        self.Citravhslout = tk.Label(self.MainFrame5, bg="blue", image=self.hsloutnoimage)
        self.Citravhslout.grid(row=1, column=4, padx=10, pady=0,)
        
        self.lblhslout = tk.Label(self.MainFrame5, text="Skin Detection", font="Georgia", background="lightblue")
        self.lblhslout.grid(row=0, column=4)
                
        #label keterangan hasil output
        self.label11 = tk.Label(self.MainFrame5, text="Size (Pixel) :",font="arial 14 bold", background="lightblue", width=0,height=0)
        self.label11.grid(row=6, column=0)
        
        self.labelsizepixel = tk.Label(self.MainFrame5, text="0",font="arial 20 bold", background="lightblue", width=0,height=0)
        self.labelsizepixel.grid(row=6, column=1)
        
        #label keterangan hasil output
        self.label11 = tk.Label(self.MainFrame5, text="Skin Detec :",font="arial 14 bold", background="lightblue", width=0,height=0)
        self.label11.grid(row=6, column=2)
        
        self.labelpersent = tk.Label(self.MainFrame5, text="0 %",font="arial 20 bold", background="lightblue", width=0,height=0)
        self.labelpersent.grid(row=6, column=3)
        
        #label keterangan hasil output
        self.labelklasifikasi = tk.Label(self.MainFrame5, text="Bukan PornoGrapic",font="arial 18 bold", bg="lightblue", fg="red", width=0,height=0)
        self.labelklasifikasi.grid(row=6, column=4)
        
#        self.label11 = tk.Label(self.MainFrame5, text="Bukan PornoGrapic",font="arial 12 bold", background="lightgray", width=0,height=0)
#        self.label11.grid(row=6, column=5)
        
        
        #frame 6
        #label footer
        self.label = tk.Label(self.MainFrame6, text="Moh. Syarif G. Ishak  |   T 3 1 1 5 0 8 4   |   F A K U L T A S   I L M U   K O M P U T E R   |   T E K N I K   I N F O R M A T I K A   |   2 0 1 9", font="impact")
        self.label.grid(row=2, column=2, sticky="NSEW", padx=260, )
        self.label.config(background="lightgray")
        self.MainFrame6.grid_propagate(0)
        
        
        
    def proses(self):
        a = p.ImageProses()
        pathImgTrain = self.textboxdatatraining.get()
        
        folder_imgTrain = a.getImgTrain(pathImgTrain)                 
        kumpulan_gbr = a.loadImgTrain(folder_imgTrain)
        
        hasilPraOlah = []
        for img in kumpulan_gbr:
            hasil = a.prapengolahan(img)
            hasilPraOlah.append(hasil)
            
        hasilcrop = []
        for cgambar in hasilPraOlah:
            crop = a.cropface(cgambar)
            skin = a.skintrain(cgambar)
            hasilcrop.append(crop)        
        
        
        
          
#==============================================================================
                            # BLOK TESTING
#==============================================================================        
        
    def testing(self):
        a = p.ImageProses()
        pathImgTesting = self.textboxdatatesting.get()
#        gambartesting = a.loadImgTest(pathImgTesting)
        
#tampil gambar
        imgpilih = Image.open(self.textboxdatatesting.get())
        imgpilih = imgpilih.resize((170, 227),  Image.ANTIALIAS)
        imgpilih = ImageTk.PhotoImage(imgpilih)
        self.CitraAsli.configure(image=imgpilih)
        self.CitraAsli.image=imgpilih
        
#tampil gambar Histogram                
        gambarhist = a.ImgHeist(pathImgTesting)
        
        imgHist = Image.fromarray(gambarhist)
        imgHist = imgHist.resize((170, 227),  Image.ANTIALIAS)
        imgHist = ImageTk.PhotoImage(imgHist)
        self.CitraHist.configure(image=imgHist)
        self.CitraHist.image=imgHist
        
        gambarskin = a.skintesting(pathImgTesting)

        imgSkin = Image.fromarray(gambarskin)
        imgSkin = imgSkin.resize((236, 270),  Image.ANTIALIAS)
        imgSkin = ImageTk.PhotoImage(imgSkin)
        self.Citravhslout.configure(image=imgSkin)
        self.Citravhslout.image=imgSkin
        self.labelsizepixel.config(text=a.gepixel())
        message = ''
        persent = a.getpersent()
        if persent <= 20:
            message = 'Bukan Porno Graphic'
        elif persent <= 35:
            message = 'Semi Porno Graphic'
        elif persent > 36:
            message = 'Porno Graphic'
        
        
        self.labelpersent.config(text=str(persent) + " %")
        self.labelklasifikasi.config(text= message)
        
        
    def selchue(self):
        a = p.ImageProses()
        pathImgTesting = self.textboxdatatesting.get()
       
        gambarhue = a.pilihhue(pathImgTesting)
        
        imghue = Image.fromarray(gambarhue)
        imghue = imghue.resize((120, 150),  Image.ANTIALIAS)
        imghue = ImageTk.PhotoImage(imghue)
        self.Citrahue.configure(image=imghue)
        self.Citrahue.image=imghue
#        cv2.imshow("hue",gambarhue)
        
    def selcstr(self):
        a = p.ImageProses()
        pathImgTesting = self.textboxdatatesting.get()
       
        gambarstr = a.pilihstr(pathImgTesting)
        
        imgstr = Image.fromarray(gambarstr)
        imgstr = imgstr.resize((120, 150),  Image.ANTIALIAS)
        imgstr = ImageTk.PhotoImage(imgstr)
        self.Citrast.configure(image=imgstr)
        self.Citrast.image=imgstr
#        cv2.imshow("hue",gambarhue)
        
    def selcvle(self):
        a = p.ImageProses()
        pathImgTesting = self.textboxdatatesting.get()
       
        gambarvle = a.pilihvle(pathImgTesting)
        
        imgvle = Image.fromarray(gambarvle)
        imgvle = imgvle.resize((120, 150),  Image.ANTIALIAS)
        imgvle = ImageTk.PhotoImage(imgvle)
        self.Citravlu.configure(image=imgvle)
        self.Citravlu.image=imgvle
#        cv2.imshow("hue",imgvle)
        
    def selchsv(self):
        a = p.ImageProses()
        pathImgTesting = self.textboxdatatesting.get()
       
        gambarhsv = a.pilihhsv(pathImgTesting)
        
        imghsv = Image.fromarray(gambarhsv)
        imghsv = imghsv.resize((120, 150),  Image.ANTIALIAS)
        imghsv = ImageTk.PhotoImage(imghsv)
        self.Citravhsv.configure(image=imghsv)
        self.Citravhsv.image=imghsv
#        cv2.imshow("hue",imgvle)
            
    
    def close_window(self, event=None):
        self.parent.destroy()
    
    def clearform(self):
        self.textboxdatatraining.delete(0, END)
        self.textboxdatatesting.delete(0, END)
    
                
def main():
    root = tk.Tk()
    root.geometry("1024x768")
    root.configure(background='lightblue')
    root.iconbitmap('F:\Kuliah\Semester 6\Proposal Bissmillah\Program\icon.ico')
    root.state("zoomed")
    root.resizable(1,1)
    app = Main(root)
    
    app.parent.title("Skin Detection")
    root.mainloop()
    
if __name__ == '__main__':
    main()
