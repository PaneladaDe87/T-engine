import os
import shutil

def main():
    os.system("python -m compileall -b src")
    apk_dir = "./debug.apk"
    os.makedir(apk_dir, exist_ok=True)
    
    apk_path = "./debug.apk"
    shutil.copy(apk_path, apk_dir)
    
    print("tudo certo :D")
    
if __name__ == "__main__":
    main()
