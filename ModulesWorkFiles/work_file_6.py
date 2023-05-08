#Vitalik
# Sakovets
def task6():
    type = input("Введіть тип даних (char, int, str, float):")
    fileobj = open('df.txt','r')
    for i in fileobj:
        try:
            if(type == "int"):
                print(int(i))
            elif(type == "str"):
                print(str(i))
            elif ((type == "char") & (len(i.strip()) == 1)):
                print(i)
            elif ((type == "float")&((float(i)%1) > 0)):
                print(i)
        except:
            pass
    fileobj.close()