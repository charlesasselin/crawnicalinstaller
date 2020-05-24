crawnical-installer

## Description
Crawnical Installer is a Lightroom preset installer. It copies the files imported and pastes it in the Lightroom presets folder to make it useable in the app. 

## Dependencies
- Python 3.6 (I recommend using Pyenv to manage Python versions for the environment https://github.com/pyenv/pyenv)

- Poetry 0.12 or higher (https://python-poetry.org/)

## Build instructions
1. Add your preset folder the base folder in ressources with the name "Presets". It is important to rename the folder to "Presets" because this is the the name that is used to have access to the path to copy the preset files.

2. This script uses Poetry. To make it work, you will need to install a Poetry version higher than 0.12. Use Poetry  to install the dependencies that the project needs.

        $ poetry install

3. I made the macosfix.sh script that fixes a problem regarding shiboken2. Use the following command to use it:

        $ bash macosfix.sh

    What it does is it copies the *libshiboken2.abi3.xx.yy.dylib* (where xx and yy are version numbers) from site-packages/shiboken2/ to both site-packages/PyInstaller/hooks/ and site-packages/PySide2/

    The Qtxml import was also added to fix this issue.

4. To run the app, use this command line in terminal:

        $ poetry run fbs run

    Make sure that you are not in the root folder but in the crawnical_installer folder (the one with and undercase and not the dash)

5. When the app runs correctly, use the following command to build it:

        $ poetry run fbs freeze
