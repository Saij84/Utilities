import os

path = "Z:\TV\Friends\Friends Season 1 COMPLETE 720p.BRrip.sujaidr (pimprg)\english subtitles"

for file in os.listdir(path):
    lvl1 = "_".join(file.split(".")[:-1])
    newName = lvl1.replace("psychd", "sujaidr") + ".srt"
    os.rename(file, path + "\\" + newName)
