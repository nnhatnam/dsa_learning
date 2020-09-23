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
    if suffix == '' or suffix is None or suffix[0] != "." or not os.path.isdir(path):
        return []
    files = []
    for p in os.listdir(path):
        full_path = os.path.join(path, p)

        if os.path.isfile(full_path):
            if p.endswith(suffix):
                files.append(full_path)
        else:
            files.extend(find_files(suffix, full_path))
    return files


if __name__ == "__main__":
    print(find_files(".c", "."))
    # ['.\testdir\subdir1\a.c', '.\testdir\subdir3\subsubdir1\b.c', '.\testdir\subdir5\a.c', '.\testdir\t1.c']

    print(find_files("c", "."))
    # [] - suffix is not value

    print(find_files(None, "."))
    # [] - suffix is None

    print(find_files("", None))
    # [] - path is None

    print(find_files(".h", "."))
    # ['.\testdir\subdir1\a.h', '.\testdir\subdir3\subsubdir1\b.h', '.\testdir\subdir5\a.h', '.\testdir\t1.h']

    print(find_files(".h", ".."))
    # ['..\Project 2\testdir\subdir1\a.h', '..\Project 2\testdir\subdir3\subsubdir1\b.h',
    # '..\Project 2\testdir\subdir5\a.h', '..\Project 2\testdir\t1.h']
