import os
import shutil

def main():
    os.system("python -m compileall -b source")
    apk_dir = "./bin"
    os.makedirs(apk_dir, exist_ok=True)
    
    apk_path = "./bin/debug.apk"
    shutil.copy(apk_path, apk_dir)
    
    print("tudo certo :D")
    
if __name__ == "__build__":
    main()
