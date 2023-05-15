import os

def modify_files(directory, filename_to_exclude):
    for filename in os.listdir(directory):
        if filename.endswith(".ctl") and filename != filename_to_exclude:
            with open(os.path.join(directory, filename), 'r') as f:
                content = f.read()

            new_content = content.replace('public void send_Command(int pCommand)\n  {', 'public void send_Command(int pCommand)\n  {\n    createLog()')

            with open(os.path.join(directory, filename), 'w') as f:
                f.write('#uses "classes/Scs/controllers/ScsDeviceController"\n' + new_content)

directory = ""  # Change to your directory path
filename_to_exclude = ""  # Change to your filename to exclude
modify_files(directory, filename_to_exclude)
