import subprocess
import time
admin = "MAIN\Administrator" # Admin user

# Users to block permissions
users = ['MAIN\user1', 'MAIN\user2', 'MAIN\user3', 'MAIN\user4', 'MAIN\user5', 'MAIN\user6', 'MAIN\user7', 'MAIN\user8', 'MAIN\user9', 'MAIN\user10']

# Print hello message
hello = '''
+--- italic

               __                          _           
 /  / _ _ _   /__)_ _ _  ' _  _ '     _   / )/ _   _ _ 
(__/_) (-/ __/   (-/ //)/_) _) /()/)_) __(__/)(//)(/(- 
                                                 _/    

---+ italic

'''
print(hello)
time.sleep(3)

# Directories to change permissions
dirs = [r"C:\Windows\System32\cmd.exe", 
        r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", 
        r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell_ise.exe",
        r"C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe",
        r"C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell_ise.exe" ]

def change_permissions(dirs, users, admin):

    # Change permissions for directories
    for dir in dirs:
        subprocess.run(f'takeown /F "{dir}" /A && icacls "{dir}" /grant "{admin}":F', shell=True) # Take ownership and grant full control to admin
        print(f"Permissions for {dir} have been changed")

    # Block permissions for users
    for user in users:
        for dir in dirs:
            subprocess.run(f'icacls "{dir}" /deny "{user}":WR', shell=True) # Deny write and read permissions
            print(f'Permissions were blocked for "{user}" in {dir}')

    print(f"Permissions have been changed for {len(users)} users successfully") # Print success message
<<<<<<< HEAD

def cancel_change(dirs, users):
    # Cancel permissions for directories
    for dir in dirs:
        subprocess.run(f'icacls "{dir}" /reset', shell=True) # Reset permissions
        print(f"Permissions for {dir} have been reset")

    # Cancel permissions for users
    for user in users:
        for dir in dirs:
            subprocess.run(f'icacls "{dir}" /remove {user}', shell=True) # Remove permissions
            print(f"Permissions were removed for {user} in {dir}")

    print(f"Permissions have been reset for {len(users)} users successfully") # Print success message
    
=======
  
>>>>>>> 4b0725070299c01f1cb7c3e0273c5ac0e742ddfb
def happyend():
    size = input("Введіть розмір грудей: ")
    b = ' ' * int(size)
    boobs = f'({b}.{b}Y{b}.{b})'
    print(boobs)
<<<<<<< HEAD

if __name__ == "__main__":
    change_permissions(dirs, users, admin)
    happyend()
=======
  
if __name__ == "__main__":
    change_permissions(dirs, users, admin)
    happyend()
>>>>>>> 4b0725070299c01f1cb7c3e0273c5ac0e742ddfb
