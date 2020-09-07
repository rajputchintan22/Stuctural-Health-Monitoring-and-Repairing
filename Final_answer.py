import os
import webbrowser
from tkinter.filedialog import askopenfilename

def my_gui():
    filename1 = askopenfilename()
    os.system(
        "python -W ignore labeler/label_main.py --graph=models/main.pb --labels=models/main.txt --image=" + filename1)
    fp = open("labeler/answer.txt", "r")
    s = fp.readline()
    s.replace("\n", "")
    fp.close()
    if s != "acid_attack":
        os.system(
            "python -W ignore labeler/label_sub.py --graph=models/" + s + ".pb --labels=models/" + s + ".txt --image=" + str(
                filename1))


my_gui()
fp = open("labeler/answer.txt", "r")
s = fp.readlines()
fp.close()
fp = open("results.html", "r")
html = fp.readlines()
fp.close()
s[0] = s[0].replace("\n", "")
html[9] = ((s[0].replace("_", " ")).upper()) + "\n"
html[12] = s[1]
html[15] = s[2]
html[18] = s[3]
fp = open("results.html", "w")
fp.writelines(html)
fp.close()
webbrowser.open_new("results.html")