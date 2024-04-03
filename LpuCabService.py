from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from tkinter import messagebox
import mysql.connector


def values():
    if userNameValue.get() == "" or userPasswordValue.get() == "":
        messagebox.showerror("Error", "All fields are mandatory")
    elif (userNameValue.get() == "Abhishek" and userPasswordValue.get() == "12345") or (userNameValue.get() == "Brajesh" and userPasswordValue.get() == "00000"):
        top = Toplevel(abhishek)
        top.geometry("500x566")

        def func():
            to_value = cmb_value_to.get()
            from_value = cmb_value_from.get()
            mobile_number = mobile_entry_value.get()
            day = day_value_entry.get()
            samay = time_value_entry.get()
            if (to_value == "BH-1" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-1") or (to_value == "BH-1" and from_value == "Unihospital") or (to_value == "BH-1" and from_value == "Foodfactory") or (to_value == "Unihospital" and from_value == "BH-1") or (to_value == "Foodfactory" and from_value == "BH-1"):
                fare_value.set("10 Rupees")
                fare_value_entry.update()
                # print(f"You have to pay {fare}")
            elif (to_value == "BH-8" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-8") or (to_value == "BH-8" and from_value == "Unihospital") or (to_value == "BH-8" and from_value == "Foodfactory") or (to_value == "Unihospital" and from_value == "BH-8") or (to_value == "Foodfactory" and from_value == "BH-8"):
                fare_value.set("10 Rupees")
                fare_value_entry.update()
            elif (to_value == "BH-2" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-2"):
                fare_value.set("15 Rupees")
                fare_value_entry.update()
            elif (to_value == "BH-3" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-3"):
                fare_value.set("20 Rupees")
                fare_value_entry.update()
            elif (to_value == "BH-4" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-4"):
                fare_value.set("20 Rupees")
                fare_value_entry.update()
            elif (to_value == "BH-5" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-5"):
                fare_value.set("25 Rupees")
                fare_value_entry.update()
            elif (to_value == "BH-6" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-6"):
                fare_value.set("25 Rupees")
                fare_value_entry.update()
            elif (to_value == "BH-7" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-7"):
                fare_value.set("30 Rupees")
                fare_value_entry.update()
            elif (mobile_number == "") or (to_value == "") or (samay == "") or (day == "") or (from_value == ""):
                messagebox.showerror("Error", "All fields are mandatory")
            else:
                fare_value.set("10 Rupees")
                fare_value_entry.update()
            conn = mysql.connector.connect(
                host="localhost", user="root", password="rootpassword", database="abhishekdb1")
            my_cursor = conn.cursor()
            query = ("select * from register_customer where phone=%s")
            value = (mobile_entry_value.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "You have already booked")
            else:
                my_cursor.execute(
                    "insert into register_customer values(%s, %s, %s)", (mobile_entry_value.get(), day_value.get(), time_value.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Booking Successfull")
            print(mobile_entry_value.get())
            print(day_value.get())
            print(time_value.get())
        top.title("lpuCABservice")
        top.wm_iconbitmap("taxi.ico")
        top.geometry("500x400")

        mobile_label = Label(top, text="Mobile")
        mobile_label.grid(row=0, column=0)

        mobile_entry_value = StringVar()
        mobile_entry = Entry(top, textvariable=mobile_entry_value)
        mobile_entry.grid(row=0, column=1)

        place = ["BH-1", "BH-2", "BH-3", "BH-4", "BH-5", "BH-6",
                 "BH-7", "BH-8", "MainGate", "Foodfactory", "Unihospital"]

        from_label = Label(top, text="From")
        from_label.grid(row=1, column=0)
        cmb_value_from = StringVar()
        from_value_combobox = ttk.Combobox(
            top, values=place, textvariable=cmb_value_from, width=17, state="readonly")
        from_value_combobox.grid(row=1, column=1, padx=30)

        to_label = Label(top, text="To")
        to_label.grid(row=2, column=0)
        cmb_value_to = StringVar()
        to_value_combobox = ttk.Combobox(
            top, values=place, textvariable=cmb_value_to, width=17, state="readonly")
        to_value_combobox.grid(row=2, column=1)

        fare_label = Label(top, text="Fare")
        fare_label.grid(row=3, column=0)

        fare_value = StringVar()
        fare_value_entry = Entry(
            top, textvariable=fare_value, state='disabled')
        fare_value_entry.grid(row=3, column=1)

        day_label = Label(top, text="Day")
        day_label.grid(row=4, column=0)

        day_value = StringVar()
        day_value_entry = Entry(top, textvariable=day_value)
        day_value_entry.grid(row=4, column=1)

        time_label = Label(top, text="Time")
        time_label.grid(row=5, column=0)

        time_value = StringVar()
        time_value_entry = Entry(top, textvariable=time_value)
        time_value_entry.grid(row=5, column=1)

        sumbit_btn = Button(top, text="Book now", bg="dodgerBlue",
                            command=func)
        # sumbit_btn.configure(command=)
        sumbit_btn.grid(row=6, column=1)
        top.mainloop()
    else:
        messagebox.showerror("Error", "Invalid username and password")


def book():
    top = Toplevel(abhishek)

    def user_values():
        conn = mysql.connector.connect(
            host="localhost", user="root", password="rootpassword", database="abhishekdb1")
        my_cursor = conn.cursor()
        query = ("select * from newregistration where email=%s")
        value = (email_value.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()
        if row != None:
            messagebox.showerror(
                "Error", "You have already registered try another email")
        else:
            my_cursor.execute(
                "insert into newregistration values(%s,%s,%s)", (
                    customer_name_value.get(),
                    mobile_number_value.get(),
                    email_value.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "You hava registered successfully")
    # top = Tk()
    top.title("lpuCABservice")
    top.wm_iconbitmap("taxi.ico")
    top.geometry("389x409")
    top.minsize(280, 309)

    customer_name = Label(top, text="Name")
    customer_name.grid(row=0, column=0)
    customer_name_value = StringVar()
    customer_name_entry = Entry(top, textvariable=customer_name_value)
    customer_name_entry.grid(row=0, column=1)

    gender_label = Label(top, text="Gender")
    gender_label.grid(row=1, column=0)
    gender1 = Radiobutton(top, text="Male", value="Male")
    gender1.select()
    gender1.grid(row=1, column=1)
    gender2 = Radiobutton(top, text="female", value="female")
    gender2.grid(row=1, column=2)

    mobile_number = Label(top, text="Mobile No")
    mobile_number.grid(row=2, column=0)
    mobile_number_value = StringVar()
    mobile_number_entry = Entry(top, textvariable=mobile_number_value)
    mobile_number_entry.grid(row=2, column=1)

    email_address = Label(top, text="Email Id")
    email_address.grid(row=3, column=0)
    email_value = StringVar()
    email_entry = Entry(top, textvariable=email_value)
    email_entry.grid(row=3, column=1)

    # password_label = Label(top, text="Password")
    # password_label.grid(row=4, column=0)
    # password_value = StringVar()
    # password_label_entry = Entry(top, textvariable=password_value)
    # password_label_entry.grid(row=4, column=1)

    submit_button = Button(top, text="Submit", command=user_values)
    submit_button.grid()

    top.mainloop()


abhishek = Tk()
abhishek.title("lpuCABservice")
abhishek.wm_iconbitmap("taxi.ico")
abhishek.geometry("313x256")

abhishek.minsize(313, 256)
title_name = Label(abhishek, text="Welcome to lpuCABservice",
                   bg="dodgerblue", font=('vardana', 17, BOLD))
title_name.grid()

login_frame = Frame(abhishek)
login_frame.grid()

userName_label = Label(login_frame, text="Username")
userName_label.grid(pady=5)
userNameValue = StringVar()
userName_entry = Entry(login_frame, textvariable=userNameValue)
userName_entry.grid(row=0, column=1, pady=5)

userPassword_label = Label(login_frame, text="Password")
userPassword_label.grid()
userPasswordValue = StringVar()
userPassword_entry = Entry(login_frame, textvariable=userPasswordValue)
userPassword_entry.grid(row=1, column=1)

login_button = Button(text="Login Now", bg="skyBlue", padx=10, command=values)
login_button.grid(pady=10)

new_user_button = Button(
    text="New user?", bg="Yellow", padx=10, command=book)
new_user_button.grid()


abhishek.mainloop()
