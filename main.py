# TEST	#

import os
import sys
from Core.FCommon import *

from subprocess import call

if len(sys.argv) < 2:
    print 'Please use at least one of those test : ' \
          '["COHERENCY_TEST", "VALIDATE_TEST", "EXPORT_IMPORT_TEST", "EXPORT_ONLY_TEST", "UNIT_TEST"]'
else:

    # Install Requirements
    # INSTALLATION_FILE = "Install/log.txt"
    # configDict1 = {}

    # if os.path.isfile(INSTALLATION_FILE):
    #    f = open(INSTALLATION_FILE)
    #    line = f.readline()
    #    while line:
    #        while line.count("\t\t") > 0:
    #            line = line.replace("\t\t", "\t")
    #        key, value = line.split("\t", 1)
    #        if key in configDict1:
    #            print ("Warning: Ignoring redefinition of configuration " +
    #                   "key: " + key + ".")
    #            continue
    #
    #        # print("key" + key + ";value  " + value.strip())
    #        configDict1[key] = value.strip()  # remove \n
    #        line = f.readline()
    #        # f.close

    # startTest = False
    # if configDict1["Install"] == "0":
    #     if call(["python", "install.py"]):
    #         target = open(INSTALLATION_FILE, 'w')
    #         target.write("Install	1")
    #         startTest = True
    #     else:
    #         print "Error: an error occurred during python package installation"

    # if configDict1["Install"] == "1" or startTest:
        # Launch Test
        OPERATION_ARG = sys.argv[1]

        OP = []
        for op in OPERATIONS:
            result = OPERATION_ARG.find(op)
            if result != -1:
                OP.append(op)

        for op in OP:

            # Coherency Test
            if op == "COHERENCY_TEST":

                if len(sys.argv) < 3:
                    print "COHERENCY_TEST need to have a .dae specified"
                else:
                    input_filename = sys.argv[2]

                    from Script.FTest_Coherency import FTest_Coherency

                    myTest = FTest_Coherency(input_filename)
                    myTest.DoProcess()

            # Validation test
            if op == "VALIDATE_TEST":

                if len(sys.argv) < 3:
                    print "VALIDATE_TEST need to have a .dae specified"
                else:
                    input_filename = sys.argv[2]

                    from Script.FTest_Validate import FTest_Validate

                    myTest = FTest_Validate(input_filename)
                    myTest.DoProcess()

            # EXPORT_IMPORT test
            if op == "EXPORT_IMPORT_TEST":
                from Script.FTest_Exporter_Import import FTest_Exporter_Import

                myTest = FTest_Exporter_Import("")
                myTest.DoProcess()

            # EXPORT test
            if op == "EXPORT_ONLY_TEST":
                from Script.FTest_Exporter import FTest_Exporter

                myTest = FTest_Exporter("")
                myTest.DoProcess()

            #  Unit Test with pyTest
            if op == "UNIT_TEST":

                if len(sys.argv) < 5:
                    print "UNIT_TEST need to have a .dae specified, unitTestDir and xml result file"
                else:
                    input_filename = sys.argv[2]
                    unitTestDir = sys.argv[3]
                    xmlResultFile = sys.argv[4]

                    from Core.FColladaTest import FColladaTest

                    myTest = FColladaTest(input_filename)
                    myTest.DoUnitTest(input_filename, unitTestDir, xmlResultFile)

                    ###Image Comparaison Test
                    # from FTest_ImgComparator import *
                    # input_filename2 = sys.argv[2]
                    # myTest = FTest_ImgComparator(input_filename)
                    # result = myTest.DoProcess(input_filename, input_filename2)
                    # if result == True:
                    # print ('OK')
                    # else:
                    # print ('BAD')

                    ###Import/Render/Export/Validation test
                    # from FTest import *
                    # myTest = FTest(input_filename)
                    # myTest.DoProcess()
