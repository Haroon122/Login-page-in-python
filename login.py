from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter
import mysql.connector
from register import Register


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Login Page")
        self.reset_pass_window = None


 #================veriables================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_cPassword=StringVar()
        self.var_nwPassword=StringVar()



        # =========background frame============
        main_frm = Frame(self.root, bg="white", width=1350, height=700)
        main_frm.place(x=0, y=0)

        # =============login image============
        login_img = Image.open(r"E:\python projects\orignal login\data\login.jpg")
        login_img = login_img.resize((700,500), Image.LANCZOS)
        self.login_photo = ImageTk.PhotoImage(login_img)
        lbl_L = Label(main_frm, bg="white", image=self.login_photo)
        lbl_L.place(x=100,y=70,width=700,height=500)
        # =========login frame============
        login_frm = Frame(main_frm, bg="white", width=350, height=350)
        login_frm.place(x=880, y=100)

        # =============top heading================
        heading = Label(login_frm, text="sign in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=100, y=5)

        # ===============sign in button======================
        s_btn = Button(login_frm,command=self.login_pg, width=39, pady=7, text="sign in", bg="#57a1f8", fg="white", border=0, cursor="hand2")
        s_btn.place(x=35, y=204)

        # =============sign up button=================
        s_up = Button(login_frm,activebackground="white",command=self.signUP, text="sign up", border=0, bg="white", fg="#57a1f8", cursor="hand2")
        s_up.place(x=220, y=270)

        # =============forget button=================
        f_up = Button(login_frm,command=self.forget_pass,activebackground="white", text="Forget password ", border=0, bg="white", fg="#57a1f8", cursor="hand2")
        f_up.place(x=133, y=305)        

        # ==============dont account label=================
        Ac_lbl = Label(login_frm, text="Don't have an account?", fg="black", bg="white",font=("Microsoft YaHei UI Light", 9))         
        Ac_lbl.place(x=75, y=270)


        # =============line 1 email frame=============
        line_frm = Frame(login_frm, width=295, height=2, bg="black")
        line_frm.place(x=25, y=107)

        # =============line 2 password frame=============
        line1_frm = Frame(login_frm, width=295, height=2, bg="black")
        line1_frm.place(x=25, y=177)

        # ==========user entry box=============
        self.user = Entry(login_frm, width=25, fg="black", bg="white", border=0, font=("Microsoft YaHei UI Light", 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, "Email")
        self.user.bind("<FocusIn>", self.on_enter)
        self.user.bind("<FocusOut>", self.on_leave)

        # ==========password entry box=============
        self.passw = Entry(login_frm, width=25, fg="black", bg="white", border=0, font=("Microsoft YaHei UI Light", 11))
        self.passw.place(x=30, y=150)
        self.passw.insert(0, "Password")
        self.passw.bind("<FocusIn>", self.on_enter)
        self.passw.bind("<FocusOut>", self.on_leave)

    def on_enter(self, event):
        if event.widget == self.user:
            self.user.delete(0, "end")
        elif event.widget == self.passw:
            self.passw.delete(0, "end")

    def on_leave(self, event):
        name = event.widget.get()
        if name == "":
            if event.widget == self.user:
                self.user.insert(0, "Email")
            elif event.widget == self.passw:
                self.passw.insert(0, "Password")


# ===============LOGIN WORKING=============
    def login_pg(self):
        E_mail = self.user.get()
        password = self.passw.get()

        if E_mail == "admin" and password == "123":
            messagebox.showinfo("Successful", "Successful login", parent=self.root)
        elif E_mail == "" or password == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="h@Roon#123Abc", database="login_page")
            curr = conn.cursor()
            curr.execute("SELECT * FROM register WHERE email=%s AND password=%s", (E_mail, password))
            row = curr.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid User Name or Password", parent=self.root)
            else:
                open_main = messagebox.askyesno("Access", "Access only admin", parent=self.root)
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_recognization_system(self.new_window)
                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()

#================================Reset Password==================================            
    def forget_pass(self):
        if self.user.get() == "":
            messagebox.showerror("Error", "Please Enter the Email to Reset Password",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="h@Roon#123Abc", database="login_page")
            curr = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            values = (self.user.get(),)
            curr.execute(query, values)
            row = curr.fetchone()

            if row is None:
                messagebox.showerror("Error", "Email Address not found. Please Enter a Valid Email Address",parent=self.root)
            else:
                conn.close()
                self.reset_pass_window = Toplevel(self.root)
                self.reset_pass_window.title("Forget Password")
                self.reset_pass_window.geometry("400x500+880+100")

                frm2 = Frame(self.reset_pass_window, bg="white")
                frm2.place(x=0, y=0, width=400, height=450)

                l = Label(self.reset_pass_window, text="Forget Password", bg="white", fg="#57a1f8",
                          font=("times new roman", 18, "bold"))
                l.place(x=0, y=0, relwidth=1)

                # Security Question
                Q2_lbl = Label(self.reset_pass_window, text="Select Security Questions", font=("roboto", 11, "bold"),
                               bg="white", fg="black")
                Q2_lbl.place(x=100, y=55)

                Q2_comb = ttk.Combobox(self.reset_pass_window, textvariable=self.var_securityQ, width=23,
                                       font=("Microsoft YaHei UI Light", 11), state="readonly")
                Q2_comb["values"] = ("Select Question", "Best Friend", "Primary School Name", "Born Date")
                Q2_comb.current(0)
                Q2_comb.place(x=100, y=85)

                # Security Answer
                A_lbl = Label(self.reset_pass_window, text="Security Answer", font=("roboto", 11, "bold"),
                              bg="white", fg="black")
                A_lbl.place(x=100, y=120)

                a1_entr = Entry(self.reset_pass_window, textvariable=self.var_securityA, bd=2, relief="ridge", width=25,
                                font=("Microsoft YaHei UI Light", 11))
                a1_entr.place(x=100, y=145)

                # New Password
                nw_lbl = Label(self.reset_pass_window, text="New Password", font=("roboto", 11, "bold"),
                               bg="white", fg="black")
                nw_lbl.place(x=100, y=205)

                nw_entr = Entry(self.reset_pass_window, textvariable=self.var_nwPassword, bd=2, relief="ridge", width=25,
                                font=("Microsoft YaHei UI Light", 11))
                nw_entr.place(x=100, y=235)

                # Reset Button
                btn = Button(self.reset_pass_window, command=self.reset_pass, width=15, text="Reset", fg="white",
                             bg="#57a1f8", border=0, font=("Microsoft YaHei UI Light", 15))
                btn.place(x=120, y=280)

    def reset_pass(self):
        if self.var_securityQ.get() == "Select Question":
            messagebox.showerror("Error", "Please Select Security Question",parent=self.reset_pass_window)
        elif self.var_securityA.get() == "":
            messagebox.showerror("Error", "Please enter security Answer",parent=self.reset_pass_window)
        elif self.var_nwPassword.get() == "":
            messagebox.showerror("Error", "Please enter the new password",parent=self.reset_pass_window)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="h@Roon#123Abc",
                                           database="login_page")
            curr = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
            value = (self.user.get(), self.var_securityQ.get(), self.var_securityA.get())
            curr.execute(query, value)
            row = curr.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please Enter the correct answer",parent=self.reset_pass_window)
            else:
                query = "UPDATE register SET password=%s WHERE email=%s"
                value = (self.var_nwPassword.get(), self.user.get())
                curr.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, please login with the new password !!!",parent=self.reset_pass_window)
                # Clear the entry fields
                self.var_securityQ.set("Select Question")
                self.var_securityA.set("")
                self.var_nwPassword.set("")
                # Destroy the reset password window
                self.reset_pass_window.destroy()

    
    def signUP(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


#########################################################################################
class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Registration Form")
        self.root.resizable(False,False)

    #================veriables================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password=StringVar()
        self.var_cPassword=StringVar()

    #=============main back frame==============
        bk_frm=Frame(self.root,bg="white")
        bk_frm.place(x=0,y=0,width=1350,height=700)

    #===============register image============
        img=Image.open(r"E:\python projects\orignal login\data\register.jpg")
        img=img.resize((600,450),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)
        lbl=Label(bk_frm,image=self.photo)
        lbl.place(x=50, y=70, width=600, height=450)

    #======================register frame================
        R_frm=Frame(bk_frm,bg="white")
        R_frm.place(x=700,y=70,width=600,height=500)

    #=========1st label register here===========
        Tp_lbl=Label(R_frm,text="REGISTER HERE",font=("times new roman", 23, "bold"),bg="white",fg="#57a1f8")
        Tp_lbl.place(x=10,y=5)

    #=========2nd label name===========
        N_lbl=Label(R_frm,text="First Name",font=("roboto", 11, "bold"),bg="white",fg="black")
        N_lbl.place(x=10,y=80)

    #=========3rd label last name===========
        L_lbl=Label(R_frm,text="Last Name",font=("roboto", 11, "bold"),bg="white",fg="black")
        L_lbl.place(x=300,y=80)

    #=========4th label contact no===========
        L_lbl=Label(R_frm,text="Contact No",font=("roboto", 11, "bold"),bg="white",fg="black")
        L_lbl.place(x=10,y=150)

    #=========5th label email===========
        E_lbl=Label(R_frm,text="Email",font=("roboto", 11, "bold"),bg="white",fg="black")
        E_lbl.place(x=300,y=150)

    #=========6th seacurity quation===========
        Q_lbl=Label(R_frm,text="Select Security Questions",font=("roboto", 11, "bold"),bg="white",fg="black")
        Q_lbl.place(x=10,y=220)

    #=========7th seacurity Answer===========
        A_lbl=Label(R_frm,text="Security Answer",font=("roboto", 11, "bold"),bg="white",fg="black")
        A_lbl.place(x=300,y=220)

    #=========8th Password===========
        p_lbl=Label(R_frm,text="Password",font=("roboto", 11, "bold"),bg="white",fg="black")
        p_lbl.place(x=10,y=290)

    #=========9th Confirm Password===========
        cp_lbl=Label(R_frm,text="Confirm Password",font=("roboto", 11, "bold"),bg="white",fg="black")
        cp_lbl.place(x=300,y=290)


        self.var_check=IntVar()
    #==========terms condition check box========
        c_box=Checkbutton(R_frm,variable=self.var_check,activebackground="white",text="I Agree The Terms & Conditions",font=("roboto", 11, "bold"),bg="white",fg="black",onvalue=1,offvalue=0)
        c_box.place(x=10,y=365)

    #==========1 name entry box===============
        n_entr=Entry(R_frm,bd=2,textvariable=self.var_fname,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        n_entr.place(x=10,y=110)

    #==========2 last name entry box===============
        l_entr=Entry(R_frm,bd=2,textvariable=self.var_lname,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        l_entr.place(x=300,y=110)

    #==========3 contact entry box===============
        c_entr=Entry(R_frm,bd=2,textvariable=self.var_contact,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        c_entr.place(x=10,y=180)

    #==========4 email entry box===============
        e_entr=Entry(R_frm,bd=2,textvariable=self.var_email,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        e_entr.place(x=300,y=180)

    #=========5 S_Q combobox====================
        Q_comb=ttk.Combobox(R_frm,textvariable=self.var_securityQ,width=23,font=("Microsoft YaHei UI Light",11),state="readonly")
        Q_comb["values"]=("Select Question","Best Friend","Primary School Name","Born Date")
        Q_comb.current(0)
        Q_comb.place(x=10,y=253)

    #==========6 s_answer box===============
        a_entr=Entry(R_frm,bd=2,textvariable=self.var_securityA,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        a_entr.place(x=300,y=253)

    #==========7 password box===============
        p_entr=Entry(R_frm,bd=2,textvariable=self.var_password,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        p_entr.place(x=10,y=320)

    #==========8 confirm password box===============
        cp_entr=Entry(R_frm,textvariable=self.var_cPassword,bd=2,relief="ridge",width=25,font=("Microsoft YaHei UI Light",11))
        cp_entr.place(x=300,y=320)

    #============REGISTER BUTTON================
        R_btn=Button(R_frm,command=self.registerr,width=25,pady=6,text="Register Now",font=("Microsoft YaHei UI Light",10),bg="#57a1f8",fg="white",border=0,cursor="hand2")
        R_btn.place(x=10,y=400)

    #============login BUTTON================
        R_btn=Button(R_frm,command=self.login_rtn,width=25,pady=6,text="Login",font=("Microsoft YaHei UI Light",10),bg="#57a1f8",fg="white",border=0,cursor="hand2")
        R_btn.place(x=300,y=400)

    def login_rtn(self):
        self.root.destroy()


    #====================working=============================
    
    def registerr(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select Question" or self.var_securityA.get()=="" or self.var_password.get()=="":
            messagebox.showerror("Error","All Fields are required", parent=self.root)
        elif self.var_password.get()!=self.var_cPassword.get():
            messagebox.showerror("Error","Password & Confirm Password must be same", parent=self.root)
        elif self.var_check.get()== 0:
            messagebox.showerror("Error","please agree terms & condition", parent=self.root)
        else:
            try:               
                conn = mysql.connector.connect(host="localhost", user="root", password="h@Roon#123Abc", database="login_page")
                curr = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)
                curr.execute(query, value)
                row = curr.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists. Please try another email.", parent=self.root)
                else:
                        # Insert the new user into the database
                    query = "INSERT INTO register (first_name, last_name, contact_no, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    values = (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_password.get()
                    )
                    curr.execute(query, values)

                        # Commit the changes and close the connection
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Successful", "Registration Successful", parent=self.root)
                    self.clear_fields()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

    def clear_fields(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_securityQ.set("Select Question")
        self.var_securityA.set("")
        self.var_password.set("")
        self.var_cPassword.set("")





if __name__ == "__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()
    
