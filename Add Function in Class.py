import os

def modify_files(directory, filename_to_exclude):
    for filename in os.listdir(directory):
        if filename.endswith(".CTL") and filename != filename_to_exclude:
            with open(os.path.join(directory, filename), 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write('#uses "classes/Scs/controllers/ScsDeviceController"\n' + content)
                f.seek(0, os.SEEK_END)
                content = f.read().replace('public void send_Command(int pCommand)\n  {', 'public void send_Command(int pCommand)\n  {\ncreateLog()')
                f.seek(0)
                f.write(content)

directory = "/path/to/your/directory"  # Change to your directory path
filename_to_exclude = "filename.CTL"  # Change to your filename to exclude
modify_files(directory, filename_to_exclude)
