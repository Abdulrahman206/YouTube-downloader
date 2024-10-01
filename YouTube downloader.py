import tkinter
import customtkinter
from pytube import YouTube

def Startdownload():
    try:
        ytlink = link.get()
        print(f"URL: {ytlink}")  # For debugging
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        print(f"Title: {ytObject.title}")  # For debugging
        video = ytObject.streams.get_highest_resolution()
        video.download()
        print("Download completed")  # For debugging
        finishLable.configure(text="Downloaded!", text_color="green")
    except Exception as e:
        print(f"Error: {e}")  # For debugging
        finishLable.configure(text=f"Download Error: {str(e)}", text_color="red")

    


def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    byte_downloaded = total_size - bytes_remaining
    percentage_of_completion = byte_downloaded / total_size* 100
    per = str(int(percentage_of_completion))

    pPercent.configure(text=per+'%')
    pPercent.update()

    progress_bar.set(byte_downloaded / total_size)
    progress_bar.update()




# System Setting 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Download")

# Adding UI
title = customtkinter.CTkLabel(app,text="insert a youtube Link")
title.pack(padx=10,pady=10)

# Link input
url_var = tkinter.StringVar()
link= customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()


# finishing download
finishLable = customtkinter.CTkLabel(app,text="")
finishLable.pack()


# progress percentage
pPercent = customtkinter.CTkLabel(app,text="%0")
pPercent.pack()

progress_bar = customtkinter.CTkProgressBar(app,width=400)
progress_bar.set(0)
progress_bar.pack(padx=10,pady=10)



# Download Button
Download = customtkinter.CTkButton(app,text="Download",command=Startdownload)
Download.pack(padx=10,pady=10)

# Run
app.mainloop()