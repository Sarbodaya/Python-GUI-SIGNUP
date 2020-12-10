from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql


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
        self.txt_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name", font=('times new roman', 15, 'bold',), bg='white',
                       fg='black').place(x=370, y=100)

        self.txt_lname = Entry(frame1, font=('times new roman', 15), bg='lightgray')
        self.txt_lname.place(x=370, y=130, width=250)

        # --------------------------------------ROW 2------------------------------------------------
        contact = Label(frame1, text="Contact No.", font=('times new roman', 15, 'bold',), bg='white',
                        fg='black').place(x=50, y=170)

        self.txt_contact = Entry(frame1, font=('times new roman', 15), bg='lightgray')
        self.txt_contact.place(x=50, y=200, width=250)
        email = Label(frame1, text="Email", font=('times new roman', 15, 'bold',), bg='white',
                      fg='black').place(x=370, y=170)

        self.txt_email = Entry(frame1, font=('times new roman', 15), bg='lightgray')
        self.txt_email.place(x=370, y=200, width=250)
        # -----------------------------------------ROW 3----------------------------------------------------

        question = Label(frame1, text="Security Question", font=('times new roman', 15, 'bold',), bg='white',
                         fg='black').place(x=50, y=240)

        self.cmb_quest = ttk.Combobox(frame1, font=('times new roman', 13), state='readonly', justify='center')
        self.cmb_quest['values'] = ('Select', 'Your First Pet Name', 'Your Birth Place', 'Your Best Friend Name')
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=('times new roman', 15, 'bold',), bg='white', fg='black')
        answer.place(x=370, y=240)

        self.txt_answer = Entry(frame1, font=('times new roman', 15), bg='lightgray')
        self.txt_answer.place(x=370, y=270, width=250)

        # -------------------------------------ROW 4------------------------------------------------------------

        password = Label(frame1, text="Password", font=('times new roman', 15, 'bold',), bg='white',
                         fg='black').place(x=50, y=310)

        self.txt_password = Entry(frame1, font=('times new roman', 15), bg='lightgray', show="*")
        self.txt_password.place(x=50, y=340, width=250)
        confirm_pass = Label(frame1, text="Confirm Password", font=('times new roman', 15, 'bold',), bg='white',
                             fg='black').place(x=370, y=310)

        self.txt_confirm_pass = Entry(frame1, font=('times new roman', 15), bg='lightgray',show="*")
        self.txt_confirm_pass.place(x=370, y=340, width=250)
        # ----------------------- TERM & Condition-----------------------------------------------
        self.var_check = IntVar()
        chk = Checkbutton(frame1, text="I Agree The Term & Condition", variable=self.var_check, onvalue=1, offvalue=0,
                          bg='white',
                          font=('times new roman', 12)).place(x=50, y=370)

        self.btn_img = ImageTk.PhotoImage(file='Images/f1button.jpg')
        btn_register = Button(frame1, image=self.btn_img, bd=0, cursor='hand2', command=self.register_data).place(x=50,
                                                                                                                  y=410)

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0, END)
        self.txt_confirm_pass.delete(0, END)
        self.cmb_quest.current(0)

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_contact == '' or self.txt_email.get() == "" or self.cmb_quest.get() == 'Select' \
                or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_confirm_pass.get() == " ":

            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        elif self.txt_password.get() != self.txt_confirm_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our condition !!!", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employee")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s", self.txt_email.get())
                row = cur.fetchone()
                # print(row)
                if row is not None:
                    messagebox.showerror("Error", "User Already Exists !!!", parent=self.root)
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values ("
                                "%s, "
                                "%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(), self.txt_lname.get(), self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.cmb_quest.get(),
                                 self.txt_answer.get(), self.txt_password.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registered Successfully")
                    self.clear()
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


root = Tk()

obj = Register(root)
root.mainloop()
