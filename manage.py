#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "friends.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "programming.settings")
>>>>>>> 621cea3977d452f37c0660709c7ee3bdabf964b2

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
