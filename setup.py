from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30830",
      url="",
      author="Renjie Fu",
      author_email="renjie.fu@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_point={'console_scripts':['comp30830_systeminfo=systeminfo.main:main']
                   }
      )