from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("1350x700+0+0")
        # Background Image
        self.bg = ImageTk.PhotoImage(file='Images/i7.jpg')
        bg = Label(self.root, image=self.bg).place(x=10, y=0, relwidt=1, relheight=1)
        # Register Form
        frame1 = Frame(self.root, bg='white')
        frame1.place(x=480, y=100, width=722, height=500)

        title = Label(frame1, text="REGISTER HERE", font=('times new roman', 20, 'bold',), bg='white',
                      fg='black').place(x=50, y=30)
        # ------------------------------------ROW 1----------------------------------------
        f_name = Label(frame1, text="First Name", font=('times new roman', 15, 'bold',), bg='white',
                       fg='black').place(x=50, y=100)

        self.txt_fname = Entry(frame1, font=('times new roman', 15), bg='lightgray')
        self.txt_fname.place(x=50,y=130,width=250)


        l_name = Label(frame1, text="Last Name", font=('times new roman', 15, 'bold',), bg='white',
                       fg='black').place(x=370, y=100)

        self.txt_lname = Entry(frame1, font=('times new roman', 15), bg='lightgray')
        self.txt_lname.place(x=370, y=130, width=250)

        # --------------------------------------ROW 2------------------------------------------------
        contact = Label(frame1, text="Contact No.", font=('times new roman', 15, 'bold',), bg='white',
                        fg='black').place(x=50, y=170)

        txt_contact = Entry(frame1, font=('times new roman', 15), bg='lightgray').place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=('times new roman', 15, 'bold',), bg='white',
                      fg='black').place(x=370, y=170)

        txt_email = Entry(frame1, font=('times new roman', 15), bg='lightgray').place(x=370, y=200, width=250)

        # -----------------------------------------ROW 3----------------------------------------------------

        question = Label(frame1, text="Security Question", font=('times new roman', 15, 'bold',), bg='white',
                         fg='black').place(x=50, y=240)

        cmb_quest = ttk.Combobox(frame1, font=('times new roman', 13), state='readonly', justify='center')
        cmb_quest['values'] = ('Select', 'Your First Pet Name', 'Your Birth Place', 'Your Best Friend Name')
        cmb_quest.place(x=50, y=270, width=250)
        cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=('times new roman', 15, 'bold',), bg='white',
                       fg='black').place(x=370, y=240)

        txt_answer = Entry(frame1, font=('times new roman', 15), bg='lightgray').place(x=370, y=270, width=250)

        # -------------------------------------ROW 4------------------------------------------------------------

        password = Label(frame1, text="Password", font=('times new roman', 15, 'bold',), bg='white',
                         fg='black').place(x=50, y=310)

        txt_password = Entry(frame1, font=('times new roman', 15), bg='lightgray').place(x=50, y=340, width=250)

        confirm_pass = Label(frame1, text="Confirm Password", font=('times new roman', 15, 'bold',), bg='white',
                             fg='black').place(x=370, y=310)

        txt_confirm_pass = Entry(frame1, font=('times new roman', 15), bg='lightgray').place(x=370, y=340, width=250)

        # ----------------------- TERM
        chk = Checkbutton(frame1, text="I Agree The Term & Condition", onvalue=1, offvalue=0, bg='white',
                          font=('times new roman', 12)).place(x=50, y=370)

        self.btn_img = ImageTk.PhotoImage(file='Images/f1button.jpg')
        btn_register = Button(frame1, image=self.btn_img, bd=0, cursor='hand2', command=self.register_data).place(x=50,
                                                                                                                  y=410)

    def register_data(self):
        print(self.txt_fname.get(), self.txt_lname.get())


root = Tk()

obj = Register(root)
root.mainloop()
