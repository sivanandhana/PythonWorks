from abc import ABC

from abc import abstractmethod


class Editor:


    @abstractmethod
    def create_module_and_package(self):

        pass

    @abstractmethod
    def edit(self):

        pass
    @abstractmethod
    def execute(self):

        pass
    @abstractmethod
    def debug(self):

        pass

class Vscode(Editor):

    def create_module_and_package(self):
        print("vs code can create modules and pakage")

    def edit(self):
        print("vs code can edit")

    def execute(self):
        print("vs code can edit")

    def debug(self):
        print("vs code can debug")
        
    @property
    def extension(self):

        print("vs code has extension")

vscode_instance=Vscode()

vscode_instance.create_module_and_package()

vscode_instance.edit()

vscode_instance.execute()

vscode_instance.debug()

vscode_instance.extension