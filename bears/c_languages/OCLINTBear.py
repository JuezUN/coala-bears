import os

from coalib.bearlib.abstractions.Linter import linter
from dependency_management.requirements.PipRequirement import PipRequirement
from coalib.results.RESULT_SEVERITY import RESULT_SEVERITY

@linter(executable='oclint-0.13',
        output_format='regex',
        output_regex=r'.*:(?P<line>\d+):(?P<column>\d+):(?P<message>.*)')

class OCLINTBear:
    """
    Lints your Python files!

    Checks for coding standards (like well-formed variable names), detects
    semantical errors (like true implementation of declared interfaces or
    membership via type inference), duplicated code.

    See http://pylint-messages.wikidot.com/all-messages for a list of all
    checks and error codes.

    https://pylint.org/
    """

    LANGUAGES = {'C', 'C++'}
    REQUIREMENTS = {PipRequirement('pylint', '1.*')}
    AUTHORS = {'amrondonp@github.com'}
    AUTHORS_EMAILS = {'amrondonp@gmail.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Unused Code', 'Formatting', 'Duplication', 'Security',
                  'Syntax'}
    SEE_MORE = 'https://pylint.org/'

    @staticmethod
    def create_arguments(filename, file, config_file):
      """
      :param pylint_rcfile:
          The configuration file Pylint shall use.
      """
      return "-no-analytics", filename
