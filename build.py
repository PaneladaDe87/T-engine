import os
import shutil

def main():
    os.system("python -m compileall -b source")
    apk_dir = "debug/apk"
    os.makedirs(apk_dir, exist_ok=True)
    
    apk_path = "debug/apk/app-debug.apk"
    shutil.copy(apk_path, apk_dir)
    
    print("tudo certo :D")
    
main()
