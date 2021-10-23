import os
path = os.getcwd()
print(f"current working directory: {path}")

for file in os.listdir(path):
    print(file)