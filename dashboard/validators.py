import os
from django.core.exceptions import ValidationError


def validate_path(value):
    if os.path.isfile(value) is False:
        raise ValidationError('The file is not present in %s' % value)


def clean_executable_path(self):
        if self.installed_by_npm is False:
            if os.path.isfile(self.executable_path) is False:
                raise ValidationError('The 123 file is not present in %s' % self.executable_path)
        else:
            if self.executable_path not in os.popen('npm view "' + self.executable_path + '" version').read():
                raise ValidationError(self.executable_path + 'is not present as an NPM module')