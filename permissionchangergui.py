from tkinter import *
from tkinter import ttk
from permissionchanger import change_permissions, cancel_change # Import functions from permissionchanger.py

hello = '''
+--- dwhistler
US R_ H N  _P RMISSION
  x  . x xx  x        
  x  . x xx  x        
  x  . . xx  x        
  x  . . .x  x        
  x  . . .x  x        
  .  . . ..  .                     
USER_CHANGE_PERMISSION                                                                                                            
'''
admin = "Administrator" # Admin user

users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10'] # Users to block permissions

# Print hello message
dirs = [r"C:\Windows\System32\cmd.exe", 
        r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", 
        r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell_ise.exe",
        r"C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe",
        r"C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell_ise.exe" ]





# INIT GUI
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("Permission Changer")
def on_change_permissions():
    ttk.Label(frm, text="Permissions have been changed successfully").grid(column=0, row=1)
def on_cancel_change():
    ttk.Label(frm, text="Permissions have been reset successfully").grid(column=0, row=2)

ttk.Label(frm, text=hello).grid(column=0, row=0)
change_permissions_button = ttk.Button(frm, text="Change Permissions", command=lambda:( change_permissions(dirs, users, admin), on_change_permissions()))
change_permissions_button.grid(column=0, row=2)
change_permissions_button.grid(column=1, row=2)
cancel_change_button = ttk.Button(frm, text="Cancel Change", command=lambda:( cancel_change(dirs, users), on_cancel_change()))
cancel_change_button.grid(column=2, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=2)

root.mainloop()
