#!/usr/bin/env python

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Copyright 2011-2014, the ilastik developers

import ilastik_main

if __name__ == "__main__":
    # Special command-line control over default tmp dir
    import ilastik.monkey_patches
    ilastik.monkey_patches.extend_arg_parser(ilastik_main.parser)
    
    # Examples:
    # python ilastik.py --headless --project=MyProject.ilp --output_format=hdf5 raw_input.h5/volumes/data
    # python ilastik.py --playback_speed=2.0 --exit_on_failure --exit_on_success --debug --playback_script=my_recording.py
    
    parsed_args, workflow_cmdline_args = ilastik_main.parser.parse_known_args()        
    ilastik_main.main(parsed_args, workflow_cmdline_args)
