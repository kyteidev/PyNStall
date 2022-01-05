versionsUrl = "https://raw.githubusercontent.com/LifeTecLover999/Cypher-versions/main/versions?token=AVLBPXLT4DDRMITREVFWGQDB3YL6S" #The versions file has to be in .txt format!

from tkinter import Label, Entry, Tk, CENTER, LEFT, END, StringVar, PhotoImage, Checkbutton, BooleanVar
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import tkinter.ttk as ttk

import os
import requests
import urllib.request
import urllib
import webbrowser
from bs4 import BeautifulSoup

global cwd
cwd = "path/to/install/location"
versionstring = "PyNStall v1.0"

def callback(url):
    webbrowser.open_new(url)

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False

print('connected' if connect() else 'no internet!')

def main():
    # check for internet connection, if no: exit program
    if (connect()):
        window()
    else:
        nointernet()

def download(dest_folder: str):

    MediaUrl = 'link.to/mediafire/download'

    url = MediaUrl

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-2].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    if not os.path.exists(("%s\%s" % (dest_folder, filename))):
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        url = soup.find("a", class_="popsok").get('href')
        r = requests.get(url)

        print("File Name : " + soup.find("div", class_="filename").get_text())
        print(soup.find("ul", class_="details").get_text())

        cwd = "path/to/file"
        dest_folder = cwd

        r = requests.get(url, stream=True)
        filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
        file_path = os.path.join(dest_folder, filename)
        if r.ok:
            print("Saving %s to %s." % (filename, os.path.abspath(file_path)))
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
            success()
        else:  # HTTP status code 4XX/5XX
            global errormessage
            errormessage = ("Download failed: status code {}\n{}".format(r.status_code, r.text))
            print(errormessage)
            error()
    else:
        duplicate()



def downloadfile():

        global version
        version = dropdown.get()
        download(dest_folder=cwd)
def window():
    # setup window

    window = Tk()
    window.resizable(False, False)
    window.title("PyNStallInstaller")

    # centre window and set size

    window_height = 250
    window_width = 265
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

    # labels

    title = Label(window, text="PyNStall", font="Helvetica 18 bold")
    subtitle = Label(window, text="Open-source Python installer", justify=CENTER, font="Helvetica 11 bold")
    desc1 = "Click 'Install' to install the app!"
    description = Label(window, text=desc1, justify=LEFT, font="Helvetica 10")
    folder_string = Label(window, text="Directory:", font="Helvetica 10")
    versionchoose_string = Label(window, text="Version:", font="Helvetica 10")
    version_string = Label(window, text=versionstring, foreground="gray", font="Helvetica 8")

    # buttons

    btn_install = ttk.Button(window, text="Install", width=20, command=downloadfile)
    btn_path = ttk.Button(window, text="...", width=2, command=directoryopen)
    btn_cancel = ttk.Button(window, text="Quit", width=20, command=close)

    # dropdown

    VERSIONS = []

    url = versionsUrl
    page = requests.get(url)
    versions = (page.text).strip()

    splitstr = versions.split("\n")

    for i in splitstr:
        VERSIONS.append(i)

    variable = StringVar(window)
    variable.set(VERSIONS[0])

    global dropdown
    dropdown = ttk.Combobox(window, values=VERSIONS, width=7)
    dropdown.configure(state="readonly")
    dropdown.current(0)

    # setup directory entry

    global directory
    directory = Entry(width=22, foreground="black")
    path = directory.get()
    directory.insert(0, cwd)

    # place all widgets on window

    version_string.place(x=1, y=1)
    title.place(x=80, y=10)
    subtitle.place(x=25, y=42)
    description.place(x=40, y=70)


    directory.place(x=84, y=115)
    folder_string.place(x=20, y=113)
    btn_path.place(x=225, y=112)

    dropdown.place(x=120, y=140)
    versionchoose_string.place(x=65, y=139)

    btn_install.place(x=70, y=170)
    btn_cancel.place(x=70, y=200)

    window.mainloop()



def directoryopen():
    # open directory window

    dir_name = fd.askdirectory()
    global cwd
    cwd = dir_name
    directory.delete(0, END)
    directory.insert(0, cwd)

def success():
    msg.showinfo("PyNStall", "Successfully installed the app!")
    exit()


def duplicate():
    msg.showerror("PyNStall", "The app is already installed!")


def nointernet():
    root = Tk()
    root.withdraw()
    msg.showerror("PyNStall", "Could not connect to the internet!\nAn active internet connection is required for the installation.")

def error():
    global errormessage
    msg.showerror("PyNStall", errormessage)

def close():
    exit()

if __name__ == '__main__':
    main()