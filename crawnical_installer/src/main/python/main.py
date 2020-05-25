from fbs_runtime.application_context.PySide2 import ApplicationContext
from pathlib import Path
from PySide2 import QtUiTools, QtCore, QtGui, QtXml
import sys
import os
import shutil
import platform


def main():
    appctxt = ApplicationContext()
    presets = []
    for preset in Path(appctxt.get_resource("Presets")).iterdir():
        presets.append(preset)

    ui_path = appctxt.get_resource("installer_design.ui")
    icon_path = appctxt.get_resource("icon_blue.png")
    window = QtUiTools.QUiLoader().load(ui_path)
    pixmap = QtGui.QPixmap(icon_path)
    window.label.setPixmap(pixmap)
    # if window.lineEdit.textChanged() is in licenseList:
    window.pushButton.clicked.connect(lambda: run(presets, window))
    window.show()
    exit_code = appctxt.app.exec_()
    return exit_code


def run(presets, window):
    home_folder = os.path.expanduser("~")
    user_platform = platform.system()

    if user_platform == "Darwin":
        for preset in presets:
            preset_path = Path(preset)
            # Target path 1 is for previous versions of lightroom
            target_path_1 = (
                Path(home_folder)
                / "Library"
                / "Application Support"
                / "Adobe"
                / "Lightroom"
                / "Develop Presets"
                / "Crawnical Preset Pack"
            )
            target_path_1.mkdir(parents=True, exist_ok=True)
            target_path_1 = target_path_1 / preset_path.name
            # Target path 2 is for new versions of lightroom
            target_path_2 = (
                Path(home_folder)
                / "Library"
                / "Application Support"
                / "Adobe"
                / "CameraRaw"
                / "Settings"
                / "Crawnical Preset Pack"
            )
            target_path_2.mkdir(parents=True, exist_ok=True)
            target_path_2 = target_path_2 / preset_path.name
            shutil.copyfile(str(preset_path), str(target_path_1))
            shutil.copyfile(str(preset_path), str(target_path_2))

    if user_platform == "Windows":
        for preset in presets:
            preset_path = Path(preset)
            # Target path 1 is for previous versions of lightroom
            target_path_1 = (
                / Path(home_folder)
                / "AppData"
                / "Roaming"
                / "Adobe"
                / "Lightroom"
                / "Develop Presets"
                / "Crawnical Preset Pack"
            )
            target_path_1.mkdir(parents=True, exist_ok=True)
            target_path_1 = target_path_1 / preset_path.name
            # Target path 2 is for new versions of lightroom
            target_path_2 = (
                / Path(home_folder)
                / "AppData"
                / "Roaming"
                / "Adobe"
                / "CameraRaw"
                / "Settings"
                / "Crawnical Preset Pack"
            )
            target_path_2.mkdir(parents=True, exist_ok=True)
            target_path_2 = target_path_2 / preset_path.name

            shutil.copyfile(str(preset_path), str(target_path_1))
            shutil.copyfile(str(preset_path), str(target_path_2))

    if user_platform == "Linux":
        print("This application does not support Linux")

    window.progressBar.setValue(100)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    sys.exit(main())
