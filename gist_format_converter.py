import pyperclip
def main():
    #inp = input('Input word you want to search or input (q/Q) for quit: ')

    #inp = "https://gist.github.com/vikasontech/0c234848552c269dd9b0d5004f267dee#file-resourceserverconfig-java"
    inp = pyperclip.paste()

    print("gist value", {inp})

    x = inp.split("/")
    newgist = "{{< "+x[2].split(".")[0] +" "+ x[3] +" "+ x[4].split("#")[0] + ">}}"

    pyperclip.copy(newgist)

    print(newgist)

main()
