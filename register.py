from tkinter import*
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter
import mysql.connector


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
        img=img.resize((600,450),Image.LANCZOS)
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






if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
