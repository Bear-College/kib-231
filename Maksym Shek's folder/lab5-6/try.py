try:
    somefile = open("C:\\Users\\Super\\Desktop\\MAKSYM SHEK\\Maksym Shek's folder\\lab5-6\\hello.txt", "w")
    try:
        somefile.write("hello word")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)    