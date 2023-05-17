import os
import shutil

def main():
    os.system("python -m compileall -b src")
    
    apk_path = "debug.apk"
    shutil.copy(apk_path)
    
    print("tudo certo :D")
    
if __name__ == "__main__":
    main()
