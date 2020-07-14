import fileinput
import os.path as path

variables = [
        (">>PROJNAME<<", "the project name"),
        (">>EXECNAME<<", "the name of the output binary")
        ]

files = [
        "CMakeLists.txt",
        "src/CMakeLists.txt",
        "test/CMakeLists.txt",
        "README.md"
        ]

def processFile(path, substitutions):
    with fileinput.FileInput(path, inplace=True, backup='.bak') as file:
        for line in file:
            newline = line
            for sub in substitutions:
                newline = newline.replace(sub[0], sub[1])
            print(newline, end='')

def promptSubstitutions(variables):
    substitutions = []
    for var in variables:
        print('What should ' + var[1] + ' be set to?\nIt is represented with"' + var[0] + '".')
        sub = input(">")
        substitutions.append((var[0], sub))
    return substitutions

def getThisDirectory():
    return path.dirname(path.abspath(__file__))

if __name__ == '__main__':
    subs = promptSubstitutions(variables)
    for f in files:
        p = path.abspath(path.join(getThisDirectory(),f))
        processFile(p, subs)

