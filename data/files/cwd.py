import os
<<<<<<< HEAD
path = os.getcwd()
print(f"current working directory: {path}")

for file in os.listdir(path):
    print(file)
=======

def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print(f"The directory contains the following")
    for file in os.listdir(path):
        print(file)

def run():
    print("Processing...")
    cwd()

if __name__ == "__main__":
    run()
>>>>>>> 65451eceff32461c01311f2d75734624b5bc66b3
