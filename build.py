import os
import shutil

def main():
    os.system("python -m compileall -b src")
  
    apk_dir = "."
    os.makedirs(apk_dir, exist_ok=True)
  
    apk_path = "."
    shutil.copy(apk_path, apk_dir)
  
    print("tudo certo :D")
  
if __name__ == "__main__":
    main()
