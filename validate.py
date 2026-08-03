import os

required_files=[
    "index.html",
    "style.css"
]

for file in required_files:

    if not os.path.exists(file):


        raise Exception(f"{file} Missing")

print("Validation Successful")

print("github actions working")