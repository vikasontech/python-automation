import pyperclip

def gist_function():

    # sample url 
    #https://gist.github.com/vikasontech/6246993ca66c85b8f0773ce7351b38a2#file-getuserresources-sh

    inp = pyperclip.paste()

    print("==============================================")
    print("your copied value is as below ")
    print(inp)
    print("==============================================")

    x = inp.split("/")
    newgist = "{{< "+x[2].split(".")[0] +" "+ x[3] +" "+ x[4].split("#")[0] + ">}}"

    pyperclip.copy(newgist)

    print("==============================================")
    print("your gist is "+ newgist + " is copied to the clipboard.")
    print("==============================================")


def main():

    while True:
        try:
            input("please copy the gist url and then press any key...")
            gist_function()
            print("=======================================")
            print("=======================================")
            print("=======================================")
            print("=======================================")
        except IndexError as e:
            print("Invalid value please select valid gist url")


