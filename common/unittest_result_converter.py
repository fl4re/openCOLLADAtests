import timeit
import unittest
import xml.etree.ElementTree as Et


class UnitTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super(UnitTestResult, self).__init__(stream, descriptions, verbosity)
        self.error_map = {}
        self.failure_map = {}
        self.successes = []
        self.start_time = 0
        self.times = {}

    def startTest(self, test):
        self.start_time = timeit.default_timer()
        super(UnitTestResult, self).startTest(test)

    def stopTest(self, test):
        super(UnitTestResult, self).stopTest(test)
        end_time = timeit.default_timer()
        self.times[test] = end_time - self.start_time

    def addError(self, test, err):
        super(UnitTestResult, self).addError(test, err)
        self.error_map[test] = err

    def addFailure(self, test, err):
        super(UnitTestResult, self).addFailure(test, err)
        self.failure_map[test] = err

    def addSuccess(self, test):
        super(UnitTestResult, self).addSuccess(test)
        self.successes.append(test)


class UnitTestResultConverter(object):
    def __init__(self, results):
        """
        :param results: test results
        :type results: UnitTestResult
        """
        self.results = results

    def to_junit_xml_file(self, suite_name, xml_file_path):
        test_suite = Et.Element('testsuite')
        test_suite.set('name', suite_name)
        test_suite.set('tests', str(self.results.testsRun))
        test_suite.set('errors', str(len(self.results.errors)))
        test_suite.set('failures', str(len(self.results.failures)))
        test_suite.set('skips', str(len(self.results.skipped)))

        for tc in self.results.successes:
            self._test_case_element(test_suite, tc)

        for tc in self.results.failures:
            self._test_case_element(
                test_suite, tc[0], type='failure', message=self.results.failure_map[tc[0]][1].message, text=tc[1])

        for tc in self.results.skipped:
            self._test_case_element(test_suite, tc[0], type='skipped', message=tc[1])

        for tc in self.results.errors:
            self._test_case_element(
                test_suite, tc[0], type='error', message=self.results.error_map[tc[0]][1].message, text=tc[1])

        tree = Et.ElementTree(test_suite)
        tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

    def _test_case_element(self, parent_element, test, type=None, message=None, text=None):
        test_id = test.id()
        dot_pos = test_id.rfind('.')
        test_case = Et.SubElement(parent_element, 'testcase')
        test_case.set('classname', test_id[:dot_pos])
        test_case.set('name', test_id[dot_pos + 1:])
        test_case.set('time', str(self.results.times[test]))
        if type is not None:
            type_element = Et.SubElement(test_case, type)
            if message is not None:
                type_element.set('message', message)
            if text is not None:
                type_element.text = text
