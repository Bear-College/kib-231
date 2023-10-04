text = input("Print some text: ")
with open("C:\DIMA SHCHENSNEVYCH\PythonBachelor\Dima Shchensnevych's folder\lab5-6\myfile.txt", "w") as file:
        file.write (text)

with open("C:\DIMA SHCHENSNEVYCH\PythonBachelor\Dima Shchensnevych's folder\lab5-6\myfile.txt", "r") as file:
        conten = file.read()
        print(conten)


