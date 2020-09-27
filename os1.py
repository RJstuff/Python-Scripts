import os

def check_directory(directory):
    if not os.path.exists:
        print("Creating folder name: " , directory)
        os.makedirs(directory)
    else:
        pass

ans = check_directory("R_Project")
print(ans)
