import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from bank_system import BankSystem

class BankUI:
    """A user interface Class to manage Bank Accounts"""

    def __init__(self, bank_system):
        try:
            # The bank object that manages the accounts
            self.bank_system=bank_system

            self.window = tk.Tk()
            self.window.title(self.bank_system.getName() +" Management System")
            self.window.configure(bg="#FFFFFF")

            # Frame to display bank logo and Name
            self.frame_bank_info=tk.Frame(self.window, width=700,bg="#FFFFFF")
            self.frame_bank_info.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
            # Frame to create a new account
            self.frame_add_account=tk.Frame(self.window, highlightthickness=1, highlightbackground='grey')
            self.frame_add_account.grid(row=1, column=0, padx=10, pady=10)
            # Frame to transfer money from one account to another
            self.frame_transfer_money=tk.Frame(self.window,highlightthickness=1, highlightbackground='grey')
            self.frame_transfer_money.grid(row=1, column=1,padx=10, pady=10)
            # Frame to display Account details
            self.frame_bank_details=tk.Frame(self.window,highlightthickness=1, highlightbackground='grey')
            self.frame_bank_details.grid(row=2, columnspan=2,padx=10, pady=10)

            # Adding Logo and Company Title to the Window
            original_image = Image.open("logo.jpeg")
            resized_image = original_image.resize((50, 50), Image.ANTIALIAS) #re-sizing the image
            self.logo_image = ImageTk.PhotoImage(resized_image)
            self.logo_label = tk.Label(self.frame_bank_info, image=self.logo_image,bg="#FFFFFF")
            self.logo_label.grid(row=0,column=0)
            self.company_title = tk.Label(self.frame_bank_info, text=self.bank_system.getName(), font=("Helvetica", 12),bg="#FFFFFF")
            self.company_title.grid(row=0,column=1)

            # Labels and Entry Widgets in frame_add_account
            # Heading for the frame
            self.frame1_label = tk.Label(self.frame_add_account, text="Add Account", fg="black", font = ("Arial", 12))
            self.frame1_label.grid(row=0,column=0, columnspan=2)

            self.fName_label=tk.Label(self.frame_add_account,text="First Name:")
            self.fName_label.grid(row=1,column=0, sticky='w',padx=10, pady=10)
            self.fName_box = tk.Entry(self.frame_add_account)
            self.fName_box.grid(row=1,column=1,padx=10, pady=10)

            self.lName_label=tk.Label(self.frame_add_account,text="Last Name:")
            self.lName_label.grid(row=2,column=0, sticky='w',padx=10, pady=10)
            self.lName_box = tk.Entry(self.frame_add_account)
            self.lName_box.grid(row=2,column=1,padx=10, pady=10)

            self.account_no_label=tk.Label(self.frame_add_account,text="Account No:")
            self.account_no_label.grid(row=3,column=0, sticky='w',padx=10, pady=10)
            self.account_no_box = tk.Entry(self.frame_add_account)
            self.account_no_box.grid(row=3,column=1,padx=10, pady=10)

            self.balance_label=tk.Label(self.frame_add_account,text="Balance:")
            self.balance_label.grid(row=4,column=0, sticky='w',padx=10, pady=10)
            self.balance_box = tk.Entry(self.frame_add_account)
            self.balance_box.grid(row=4,column=1,padx=10, pady=10)

            self.add_account_Btn = tk.Button(self.frame_add_account,text="Add Account", command=self.add_account)
            self.add_account_Btn.grid(row=5,column=1,padx=10, pady=10)

            # Labels and Entry Widgets in frame_transfer_money
            # Heading for the frame
            self.frame2_label = tk.Label(self.frame_transfer_money, text="Transfer Money", fg="black", font = ("Arial", 12))
            self.frame2_label.grid(row=0,column=2,padx=10, pady=10, columnspan=2)

            self.transfer_from_label=tk.Label(self.frame_transfer_money,text="Transfer From:")
            self.transfer_from_label.grid(row=1,column=2, sticky='w',padx=10, pady=10)
            self.transfer_from_box = tk.Entry(self.frame_transfer_money)
            self.transfer_from_box.grid(row=1,column=3,padx=10, pady=10)

            self.transfer_to_label=tk.Label(self.frame_transfer_money,text="Transfer To:")
            self.transfer_to_label.grid(row=2,column=2, sticky='w',padx=10, pady=10)
            self.transfer_to_box = tk.Entry(self.frame_transfer_money)
            self.transfer_to_box.grid(row=2,column=3,padx=10, pady=10)

            self.amount_label=tk.Label(self.frame_transfer_money,text="Amount:")
            self.amount_label.grid(row=3,column=2, sticky='w',padx=10, pady=10)
            self.amount_box = tk.Entry(self.frame_transfer_money)
            self.amount_box.grid(row=3,column=3,padx=10, pady=10)

            self.transfer_Btn = tk.Button(self.frame_transfer_money,text="Transfer Money", command=self.transfer_funds)
            self.transfer_Btn.grid(row=4,column=3,padx=10, pady=10)

            #Display current Bank details in the frame_bank_details
            self.display_accounts()

            # Link the on_closing function to the window close event
            self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
            # Display the window
            self.window.mainloop()
        except Exception as e:
            messagebox.showinfo("Error",e.__str__())

    def transfer_funds(self):
        try:
            fromAccount=self.transfer_from_box.get()
            toAccount=self.transfer_to_box.get()
            amount=float(self.amount_box.get())
            # Transfer money from one account to another
            self.bank_system.transfer(fromAccount,toAccount,amount)
            #The bank acount details view
            self.all_Accounts_View=self.update_account_view()
        except Exception as e:
            messagebox.showinfo("Error",e.__str__())

    def add_account(self):
        try:
            fName=self.fName_box.get()
            lName=self.lName_box.get()
            accountNo=self.account_no_box.get()
            balance=float(self.balance_box.get())
            # Creating the account within the Bank
            self.bank_system.addAccount(fName,lName,accountNo,balance)
            print("The account has been added successfully")
            #The bank acount details view
            self.all_Accounts_View=self.update_account_view()
        except Exception as e:
            messagebox.showinfo("Error",e.__str__())

    def on_closing(self):
        try:
            self.bank_system.write_customers_to_file()
            self.window.destroy()
        except Exception as e:
            messagebox.showinfo("Error",e.__str__())
            self.window.destroy()

    def display_accounts(self):
        try:
            self.frame3_label = tk.Label(self.frame_bank_details, text="Bank Accounts", fg="black", font = ("Arial", 12))
            self.frame3_label.pack()
            # create the table to display current bank accounts in the system
            self.table = ttk.Treeview(self.frame_bank_details, columns=('Account Number', 'First Name', 'Last Name', 'Balance'), show='headings')
            self.table.heading('Account Number', text='Account Number')
            self.table.heading('First Name', text='First Name')
            self.table.heading('Last Name', text='Last Name')
            self.table.heading('Balance', text='Balance')
            # Set the width of the columns
            self.table.column("#1", width=100)
            self.table.pack()
            all_accounts=self.bank_system.getAccounts()
            for id,account in all_accounts.items():
                    self.table.insert('', 'end', values=(id, account.getFirstName(), account.getLastName(), account.getBalance()))
        except Exception as e:
            messagebox.showinfo("Error",e.__str__())

    def update_account_view(self):
        try:
            #Clear the table and display updated values
            self.table.delete(*self.table.get_children())
            # Displaying current bank accounts in the system
            all_accounts=self.bank_system.getAccounts()
            for id,account in all_accounts.items():
                    self.table.insert('', 'end', values=(id, account.getFirstName(), account.getLastName(), account.getBalance()))
        except Exception as e:
            messagebox.showinfo("Error",e.__str__())


try:
    main_bank=BankSystem("First UAE Bank", "bank_repository.pkl")
    bank_system=BankUI(main_bank)
except Exception as e:
    print(e)


