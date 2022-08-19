#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Author: Mauro Soria

import os
import sys

#f sys.version_info < (3, 7):
    #sys.stdout.write("Sorry, dirsearch requires Python 3.7 or higher\n")
    #ys.exit(1


if sys.version_info < (3, 8):
    from quo import container
    from quo.widget import Box, Label

    content = Box(
            Label("Webprobe requires Python <=3.8\n\nPress `Ctrl-C` to quit", style="fg:red")
            )
    container(content, bind=True, full_screen=True)

from webprobe.lib.core.argument_parser import ArgumentParser
from webprobe.lib.controller.controller import Controller
from webprobe.lib.output.verbose_output import CLIOutput
from webprobe.lib.output.silent_output import PrintOutput


class Program:
    def __init__(self):
        self.script_path = os.path.dirname(os.path.realpath(__file__))

        self.arguments = ArgumentParser(self.script_path)

        if self.arguments.quiet:
            self.output = PrintOutput(self.arguments.color)
        else:
            self.output = CLIOutput(self.arguments.color)

        self.controller = Controller(self.script_path, self.arguments, self.output)


if __name__ == "__main__":
    main = Program()
