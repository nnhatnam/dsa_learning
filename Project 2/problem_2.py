import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    files = []
    if suffix == '' or suffix is None or suffix[0] != "." or not os.path.exists(path):
        return files


    # Fix bug given by Udacity mentor
    dir = path
    if os.path.isfile(dir) and os.access(dir, os.R_OK):
        dir = os.path.split(dir)[0]

    for p in os.listdir(dir):
        full_path = os.path.join(dir, p)

        if os.path.isfile(full_path):
            if p.endswith(suffix):
                files.append(full_path)
        else:
            files.extend(find_files(suffix, full_path))
    return files


if __name__ == "__main__":
    for file in find_files(".c", "."):
        print(file)
    # .\testdir\subdir1\a.c
    # .\testdir\subdir3\subsubdir1\b.c
    # .\testdir\subdir5\a.c
    # .\testdir\t1.c

    print(find_files("c", "."))
    # [] - suffix is not value

    print(find_files(None, "."))
    # [] - suffix is None

    print(find_files("", None))
    # [] - path is None

    for file in find_files(".h", "."):
        print(file)
    # .\testdir\subdir1\a.h
    # .\testdir\subdir3\subsubdir1\b.h
    # .\testdir\subdir5\a.h
    # .\testdir\t1.h

    for file in find_files(".h", ".."):
        print(file)
    # ..\Project 2\testdir\subdir1\a.h
    # ..\Project 2\testdir\subdir3\subsubdir1\b.h
    # ..\Project 2\testdir\subdir5\a.h
    # ..\Project 2\testdir\t1.h

    # Test bugs given by Udacity mentor
    print("Test bug")
    path = "./ex.py"
    suffix = ".py"
    for file in find_files(suffix, path):
        print(file)
    # .\ex.py
    # .\problem_1.py
    # .\problem_2.py
    # .\problem_3.py
    # .\problem_4.py
    # .\problem_5.py
    # .\problem_6.py
    # .\testdir\t1.py

    print("Test bug 2")
    path = "./this_is_a_file"
    suffix = ".py"
    for file in find_files(suffix, path):
        print(file)
    # .\ex.py
    # .\problem_1.py
    # .\problem_2.py
    # .\problem_3.py
    # .\problem_4.py
    # .\problem_5.py
    # .\problem_6.py
    # .\testdir\t1.py
