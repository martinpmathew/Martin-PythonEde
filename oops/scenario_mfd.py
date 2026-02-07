"""
Objectives
Creation of abstract classes and abstract methods;
multiple inheritance of abstract classes;
overriding abstract methods;
delivering multiple child classes.
Scenario
You are about to create a multifunction device (MFD) that can scan and print documents;
the system consists of a scanner and a printer;
your task is to create blueprints for it and deliver the implementations;
create an abstract class representing a scanner that enforces the following methods:
scan_document – returns a string indicating that the document has been scanned;
get_scanner_status – returns information about the scanner (max. resolution, serial number)
Create an abstract class representing a printer that enforces the following methods:
print_document – returns a string indicating that the document has been printed;
get_printer_status – returns information about the printer (max. resolution, serial number)
Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
MFD2 – should be a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device;
MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.
Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.
"""

from abc import ABC, abstractmethod

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

    @abstractmethod
    def get_scanner_status(self):
        pass

class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

    @abstractmethod
    def get_printer_status(self):
        pass

class MFD1(Scanner, Printer):
    def __init__(self, serial):
        self.serial = serial
        self.res = "300x300 DPI"

    def scan_document(self):
        return f"Document scanned by MFD1 ({self.serial})"

    def get_scanner_status(self):
        return f"Scanner Res: {self.res}, S/N: {self.serial}"

    def print_document(self):
        return f"Document printed by MFD1 ({self.serial})"

    def get_printer_status(self):
        return f"Printer Res: {self.res}, S/N: {self.serial}"


class MFD2(MFD1): # Inheriting MFD1 to save code, but boosting specs
    def __init__(self, serial):
        super().__init__(serial)
        self.res = "600x600 DPI"
        self.history = []

    def print_document(self):
        msg = f"Document printed by MFD2 ({self.serial})"
        self.history.append(msg)
        return msg

    def get_history(self):
        return f"Operation History: {self.history}"


class MFD3(MFD2): # Premium device adding Fax capabilities
    def __init__(self, serial):
        super().__init__(serial)
        self.res = "1200x1200 DPI"

    def send_fax(self):
        return f"Fax sent by MFD3 ({self.serial})"


# --- MFD1: Cheap Device ---
device1 = MFD1("CHEAP-001")
print(f"MFD1 Status: {device1.get_printer_status()}")
print(device1.scan_document())

print("-" * 30)

# --- MFD2: Medium Device with History ---
device2 = MFD2("MED-002")
print(f"MFD2 Status: {device2.get_scanner_status()}")
print(device2.print_document())
print(device2.get_history())

print("-" * 30)

# --- MFD3: Premium Device with Fax ---
device3 = MFD3("PREM-999")
print(f"MFD3 Status: {device3.get_printer_status()}")
print(device3.print_document())
print(device3.send_fax())