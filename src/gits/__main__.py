import subprocess
import pathlib
import os


def find_uncommited_changes(root):
    try:
        for path in root.iterdir():
            if not path.is_dir():
                continue
            os.chdir(path)
            ret = subprocess.run(['git', 'status'], capture_output=True)
            status = ' '
            if ret.returncode:
                status = '1'
            elif b'nothing to commit, working tree clean' not in ret.stdout:
                status = '!'
            print(status, path.name)
            # print(ret.returncode, path.name)
            # print(ret.stdout.decode('utf-8'))
    finally:
        os.chdir(root)


def main():
    find_uncommited_changes(pathlib.Path.cwd())
        


if __name__ == '__main__':
    main()
