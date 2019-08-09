import os, sys
from os.path import relpath

relapath = os.getcwd()
relapublic = relapath + "\public"
print(relapath)

def generate_file_dropdown (workingpath, savename):
    os.chdir(relapath)
    fout = open("public/Drop-down_html_files/" + savename + ".html","w+")
    fout.write(
    """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <title>Bootstrap Example</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
        </head>
        <body>

        <div class="container">
        <h2>Video Selector</h2>
        <p>Select a Video from the public directory</p>
     """)
    fout.write (
     """ 
       <div class="dropdown">
         <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Dropdown Example
         <span class="caret"></span></button>
        <ul class="dropdown-menu">
    """
    )
    dropdownfirst = """<li><a href= """
    dropdownlast = "</a></li>"
     
    directorylist = os.listdir(workingpath)
    for i in range (0, len(directorylist)):
        try:
            os.chdir(workingpath)
            os.chdir(directorylist[i])
            dropdownsecond = "/Drop-down_html_files/" + relpath(workingpath, relapath).replace("\\", "^") + "^" + directorylist[i] + ".html" + ">" 
            os.chdir(relapath)
        except:
            os.chdir(relapath)
            os.chdir("public/Video_Frame_Files")
            if ("mp4" in directorylist[i]):
                frameout = open(directorylist[i].replace("mp4" , "html"),"w+")
                frameout.write (
                """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                  <title>Bootstrap Example</title>
                  <meta charset="utf-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1">
                  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
                  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
                </head>
                <body>
                <div class="container">
                  <h2>Responsive Embed</h2>
                  <p>Create a responsive video and scale it nicely to the parent element with an 16:9 aspect ratio</p>
                  <div class="embed-responsive embed-responsive-16by9">
                    <iframe class="embed-responsive-item" src=
                """
                )
                
                frameout.write ('"/' + relpath(workingpath, relapublic) + "\\" + directorylist[i] + '"') 
                print('"' + relpath(workingpath, relapublic) + "\\" + directorylist[i] + '"') 
                frameout.write (
                """
                allowfullscreen></iframe>
                    </div>
                    </div>
                    </body>
                    </html>
                </html>
                """
                )
                frameout.close()
            dropdownsecond =   '"' + "/Video_Frame_Files/" + directorylist[i].replace("mp4", "html") + '"' + ">" 
            #print(dropdownsecond)
        
        fout.write (dropdownfirst + dropdownsecond + directorylist[i] + dropdownlast)
     
    #		<li><a href="#">HTML</a></li>
    #		<li><a href="#">CSS</a></li>
    #		<li><a href="#">JavaScript</a></li>
            
    fout.write (
     """ 
           </ul>
           </div> 
            </div>
        </body>
        </html>
    """
     )
    fout.close()
    
os.chdir ("public")
maindirectory = os.getcwd()
def crawl_all_folders (currentfolder): 
    os.chdir (currentfolder)
    
    directorylist = os.listdir(currentfolder)
    generate_file_dropdown (currentfolder, relpath(currentfolder,relapath).replace("\\" , "^"))

    os.chdir(currentfolder)
    
    for i in range (0, len(directorylist)):
        try:
            loopdir = os.getcwd()
            os.chdir(directorylist[i])
            crawl_all_folders (os.getcwd())
            os.chdir(loopdir)
        except:
            pass #os.listdir returned us a file and not a folder, no need to generate dropdownlist
            
#generate_file_dropdown (os.getcwd())
crawl_all_folders (os.getcwd())