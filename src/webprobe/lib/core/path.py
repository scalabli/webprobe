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

from webprobe.lib.utils.fmt import get_encoding_type


class Path:
    def __init__(self, path=None, status=None, response=None):
        encoding_type = get_encoding_type(response.body)
        self.path = path
        self.status = status
        self.redirect = response.redirect
        self.body = response.body.decode(encoding_type, errors="ignore")
        self.length = response.length
        self.response = response

    def __str__(self):
        return self.path
