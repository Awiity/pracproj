import os
import time

start_time = time.time()
image_formats = [
    ".apng",
    ".gif",
    ".png",
    ".avif",
    ".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp",
    ".svg",
    ".webp"
]
executable_formats = [
    ".exe",
    ".msi",
    ".wsf",
    ".bat",
    ".bin",
    ".com",
    ".lnk",
    ".url"
]
# https://en.wikipedia.org/wiki/List_of_archive_formats
archive_formats = [
    ".7z",
    ".s7z",
    ".apk",
    ".arc", ".ark",
    ".dar",
    ".dmg",
    ".genozip",
    ".jar",
    ".rar",
    ".tar.gz", ".tgz", ".tar.Z", ".tar.bz2", ".tbz2", ".tar.lz",
    ".war", ".wim",
    ".zip", ".zipx",

]
text_formats = [
    ".asc",
    ".doc",
    ".docx",
    ".rtf",
    ".msg",
    ".txt",
    ".pdf",
    ".wpd", ".wps"
]
table_formats = [
    ".csv",
    ".xlsx"
]
# Directories
rootFolder_path = "../"
imageFolder_path = "Pictures/"
executableFolder_path = "Executables/"
archiveFolder_path = "Archives/"
textFolder_path = "Texts/"
tableFolder_path = "Tables/"

total_filesMoved = 0
for file in os.listdir(rootFolder_path):
    print(f"LOG: file: {file}")

    if any(frmt in file for frmt in image_formats):
        total_filesMoved += 1
        print(f"LOG: file: {file}, format: IMAGE, newPath: {rootFolder_path + imageFolder_path + file}")
        os.rename(rootFolder_path + file, rootFolder_path + imageFolder_path + file)

    if any(frmt in file for frmt in executable_formats):
        total_filesMoved += 1
        print(f"LOG: file: {file}, format: EXEC, newPath: {rootFolder_path + executableFolder_path + file}")
        os.rename(rootFolder_path + file, rootFolder_path + executableFolder_path + file)
        total_filesMoved += 1

    if any(frmt in file for frmt in archive_formats):
        print(f"LOG: file: {file}, format: ARCH, newPath: {rootFolder_path + archiveFolder_path + file}")
        os.rename(rootFolder_path + file, rootFolder_path + archiveFolder_path + file)
        total_filesMoved += 1

    if any(frmt in file for frmt in text_formats):
        print(f"LOG: file: {file}, format: TEXT, newPath: {rootFolder_path + textFolder_path + file}")
        os.rename(rootFolder_path + file, rootFolder_path + textFolder_path + file)
        total_filesMoved += 1

    if any(frmt in file for frmt in table_formats):
        print(f"LOG: file: {file}, format: TABLE, newPath: {rootFolder_path + imageFolder_path + file}")
        os.rename(rootFolder_path + file, rootFolder_path + tableFolder_path + file)
        total_filesMoved += 1


end_time = time.time()
print(f"LOG: Program executed. Total files moved: {total_filesMoved}\n"
      f"\tTime elapsed: {(end_time - start_time) * 1000}ms")
