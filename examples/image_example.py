#    Copyright 2020 by Brett J. Moan
#
#    This file is part of pyautoeios.
#
#    pyautoeios is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyautoeios is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pyautoeios.  If not, see <https://www.gnu.org/licenses/>.

import os
import pyautoeios as pyauto

pyauto.pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = True

pyauto.inject_clients()
for client in pyauto.clients:
    pyauto.pair_client(client)
    box = pyauto.locateOnScreen(
        image=os.path.join("examples", "TUphiXbRhV.png"), confidence=0.999
    )
    pyauto.moveTo(box)
