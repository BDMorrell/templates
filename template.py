#!/usr/bin/env python3
import readline
from pathlib import Path
from collections import defaultdict

here = Path(__file__).parent.absolute()

def getDefaultName(path, name):
    if name is None:
        return path.name
    else:
        return name

def getSubdirs(directory):
    return [x for x in directory.iterdir() if x.is_dir()]

class Template:
    def __init__(self, path, name=None):
        self.path = path
        self.name = getDefaultName(path, name)

    @property
    def shortName(self):
        return self.path.name

class Collection:
    def __init__(self, path, name=None):
        self.path = path
        self.name = getDefaultName(path, name)
        self.templates = [Template(template, self.name+'/'+template.name) for template in getSubdirs(path)]

def removeDuplicatesFromListDict(ld):
    return dict([(key, ld[key]) for key in ld if len(ld[key]) == 1])

class TemplateLibrary:
    def __init__(self, collectionPaths):
        self.collections = [Collection(path) for path in collectionPaths]
        self.templates = [template for collection in self.collections for template in collection.templates]

    def getFrienlyListDict(self):
        longName = defaultdict(list)
        shortName = defaultdict(list)
        for t in self.templates:
            longName[t.name].append(t)
            shortName[t.shortName].append(t)
        if len(longName) != len(self.templates):
            print("Warning: there are insertecting collections of templates!")
        niceDict = removeDuplicatesFromListDict(shortName)
        niceDict.update(longName)
        return niceDict

def readyAutocomplete(hints):
    readline.parse_and_bind("tab: complete")
    def completer(text, state):
        options = [ str(x) for x in hints if x.startswith(text)]
        if state < len(options):
            return options[state]
        else:
            return None
    readline.set_completer(completer)

def getCollectionPaths():
    collections = [here / 'default']
    collections.extend(getSubdirs(here / 'collections'))
    return collections

def makeTemplateLibrary():
    return TemplateLibrary(getCollectionPaths())

def promptFromDictionary(Dict, prompt=''):
    selection = None
    readyAutocomplete(Dict)
    while selection is None:
        text = input(prompt)
        if text in Dict:
            selection = Dict[text]
        else:
            print('that is not a valid choice')
    return selection

def main():
    lib = makeTemplateLibrary()
    inputDict = lib.getFrienlyListDict()
    selectedList = promptFromDictionary(inputDict, "template? ")
    selection = None
    if len(selectedList) == 1:
        selection = selectedList[0]
    else:
        print("There are "+str(len(selectedList))+" matching templates.")
        options = dict([(str(item.path.relative_to(here)), item) for item in selectedList])
        print([str(key) for key in options])
        selection = promptFromDictionary(options, "Which one do you want? ")
    print(selection)
    print(selection.path)

if __name__ == "__main__":
    main()

