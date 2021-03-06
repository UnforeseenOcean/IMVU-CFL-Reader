__author__ = 'Toyz'

from handlers.cfl.CFLMaker import CFLMaker
from distutils.core import setup
import py2exe
import sys
import os

print "Building UI CFL file"
uiCFLMaker = CFLMaker("./interface/built/ui.cfl")

uiLocation = "./interface"
for i in os.listdir(uiLocation):
    if os.path.isfile(os.path.join(uiLocation, i)):
        f = open(os.path.join(uiLocation, i), "rb")
        uiCFLMaker.store(i, str(f.read()))
        f.close()

uiCFLMaker.finish()

sys.path.append("C:\\Windows\\WinSxS\\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.21022.8_none_bcb86ed6ac711f91")
data_files = [('.', [uiCFLMaker.path()]),
              (".", ["C:\\Windows\\WinSxS\\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.21022.8_none_bcb86ed6ac711f91\\msvcp90.dll"])
              ]

setup(windows=[{"script":"main_gui.py"}], options={"py2exe":{"includes":["sip"]}}, data_files=data_files)
