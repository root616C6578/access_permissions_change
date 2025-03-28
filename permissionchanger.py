import subprocess

admin = "Administrator" # Admin user

# Users to block permissions
users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10']

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

# Directories to change permissions
dirs = [r"C:\Windows\System32\cmd.exe", 
        r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", 
        r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell_ise.exe",
        r"C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe",
        r"C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell_ise.exe" ]

def change_permissions(dirs, users, admin):

    # Change permissions for directories
    for dir in dirs:
        subprocess.run(f'takeown /F "{dir}" /A && icacls "{dir}" /grant {admin}:F', shell=True) # Take ownership and grant full control to admin
        print(f"Permissions for {dir} have been changed")

    # Block permissions for users
    for user in users:
        for dir in dirs:
            subprocess.run(f'icacls "{dir}" /deny {user}:WR', shell=True) # Deny write and read permissions
            print(f"Permissions were blocked for {user} in {dir}")

    print(f"Permissions have been changed for {len(users)} users successfully") # Print success message
  
def happyend():
    size = input("Введіть розмір грудей: ")
    b = ' ' * int(size)
    boobs = f'({b}.{b}Y{b}.{b})'
    print(boobs)
  
if __name__ == "__main__":
    change_permissions(dirs, users, admin)
    happyend()
