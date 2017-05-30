import json

from coalib.bearlib.abstractions.Linter import linter
from dependency_management.requirements.NpmRequirement import NpmRequirement
from coalib.results.Result import Result
from coalib.results.RESULT_SEVERITY import RESULT_SEVERITY
from coalib.settings.Setting import path


@linter(executable='oclint-0.12')
class OclintBear:
    """
    OCLint is a static code analysis tool for improving quality and 
    reducing defects by inspecting C, C++ and Objective-C code
    
    See <http://oclint.org/> for more information.
    """

    LANGUAGES = {'C', 'C++'}
    AUTHORS = {'amrondonp@github.com'}
    AUTHORS_EMAILS = {'amrondonp@gmail.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Unused Code', 'Code smells', 'Complicated code', 'Bad practices',
                  'Possible bugs'}

    severity_map = {
        1: RESULT_SEVERITY.MAJOR,
        2: RESULT_SEVERITY.NORMAL,
        3: RESULT_SEVERITY.NORMAL
    }

    @staticmethod
    def create_arguments(filename, file, config_file):
        return "-no-analytics", "-report-type", "json", filename

    def process_output(self, output, filename, file):
        warnings = json.loads(output)["violation"] if output else []
        for violation in warnings:
            yield Result.from_values(
                origin = self,
                message = violation['rule'] + " " +  violation['message'],
                file = violation['path'],
                line = int(violation['startLine']),
                end_line = int(violation['endLine']),
                column = int(violation['startColumn']),
                end_column = int(violation['endColumn']),
                severity = self.severity_map[violation["priority"]])
