import collections
import os
import pathlib
import subprocess

import colorama

colorama.init()


Status = collections.namedtuple("Status", "code, commits, behind, ahead")


def git_remote():
    ret = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"], capture_output=True,
    )
    return ret.stdout


def git_status():
    ret = subprocess.run(["git", "status"], capture_output=True)
    return Status(
        ret.returncode,
        b"nothing to commit, working tree clean" not in ret.stdout,
        b"Your branch is behind of" in ret.stdout,
        b"Your branch is ahead of" in ret.stdout,
    )


def find_uncommited_changes(root):
    try:
        for path in root.iterdir():
            if not path.is_dir():
                continue
            os.chdir(path)
            status = git_status()
            color = colorama.Style.BRIGHT
            if status.code:
                color += colorama.Fore.WHITE
            elif status.commits:
                color += colorama.Fore.RED
            else:
                color = colorama.Style.DIM + colorama.Fore.CYAN

            behind = "<-" if status.behind else "  "
            remote = "^" if git_remote() else " "
            ahead = "->" if status.ahead else "  "
            print(
                f"{behind}{remote}{ahead}"
                f" {color}{path.name}{colorama.Style.RESET_ALL}"
            )
    finally:
        os.chdir(root)


def main():
    find_uncommited_changes(pathlib.Path.cwd())


if __name__ == "__main__":
    main()
