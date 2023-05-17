import os
import subprocess

def main():
    subprocess.run(['python', '-m', 'compileall', '-b', 'src'])

    apk_directory = 'apk'
    os.makedirs(apk_directory, exist_ok=True)
    apk_path = './debug.apk'
    subprocess.run(['cp', apk_path, apk_directory])

    print('APK gerado com sucesso!')

if __name__ == '__main__':
    main()
