with open("hello.txt", "w") as somefile:
    somefile.write("hello world")
with open("hello.txt", "a") as file:
    file.write("\ngood bye, world")