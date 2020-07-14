#!/usr/bin/env python3
import os
import readline
from pathlib import Path

here = Path(__file__).parent.absolute()

def readyAutocomplete(hints):
    readline.parse_and_bind("tab: complete")
    def completer(text, state):
        options = [ x for x in hints if x.startswith(text)]
        if state < len(options):
            return options[state]
        else:
            return None
    readline.set_completer(completer)

def getCollections():
    collections = [here / 'default']
    collections.extend(getSubdirs(here / 'collections'))
    return collections

def getSubdirs(directory):
    return [x for x in directory.iterdir() if x.is_dir()]

def getTemplates(collections):
    return [template for collection in collections for template in getSubdirs(collection)]

def getTemplateTouples(collections):
    templates = getTemplates(collections)
    templateList = [(x.name, x) for x in templates]
    return sorted(templateList, key=lambda template: template[0])
    # TODO: DEAL WITH DUPLICATES, to be "collection/template"

def main():
    templates = getTemplateTouples(getCollections())
    readyAutocomplete([x[0] for x in templates])
    print(input("hi"))
    
if __name__ == "__main__":
    main()

