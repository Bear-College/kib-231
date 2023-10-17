try:
    somefile = open("hello.txt", "w")
    try:
        somefile.write("hello word")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)    