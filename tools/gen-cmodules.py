#!/usr/bin/env python

# Generate genhdr/cmodules.h for inclusion in py/objmodule.c.

from __future__ import print_function

import sys
import os
from glob import glob

def update_modules(path):
    modules = []
    for module in sorted(os.listdir(path)):
        if not os.path.isfile('%s/%s/micropython.mk' % (path, module)):
            continue # not a module
        modules.append(module)

    # Print header file for all external modules.
    print('// Automatically generated by genmodules.py.\n')
    for module in modules:
        print('extern const struct _mp_obj_module_t %s_user_cmodule;' % module)
    print('\n#define MICROPY_EXTRA_BUILTIN_MODULES \\')
    for module in modules:
        print('    { MP_ROM_QSTR(MP_QSTR_%s), MP_ROM_PTR(&%s_user_cmodule) }, \\' % (module, module))
    print()

if __name__ == '__main__':
    update_modules(sys.argv[1])
