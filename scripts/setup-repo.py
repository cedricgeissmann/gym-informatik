#!/usr/bin/env python3

import os


try:
    import git
except ModuleNotFoundError:
    import pip

    pip.main(["install", "--user", "GitPython"])
    print("Git wurde installiert. Lasse das Skript nochmals laufen!")
    exit()


def main():
    test_dir = os.path.join(".", "new-repo")
    try:
        os.mkdir(test_dir)
        print(f"Ordner {test_dir} wurde erstellt.")
    except OSError:
        print(f"Ordner {test_dir} besteht bereits.")

    repo = git.Repo.init(test_dir)
    print("Neues Repository wurde erstellt.")
    name = input("Name: ")
    email = input("Email: ")
    username = input("Benutzername: ")
    repo_name = input("Repository Name: ")

    with repo.config_writer() as cfg:
        cfg.set_value("user", "name", name)
        cfg.set_value("user", "email", email)
        cfg.write()

    repo.create_remote(
        "origin", f"https://{username}@github.com/{username}/{repo_name}.git"
    )


if __name__ == "__main__":
    main()
