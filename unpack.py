import sys, getopt, os, zipfile, olefile

import jsbeautifier
# Current path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def decode():
    version()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])

    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:

        if opt in ("-h", "--help"):
            help()
            sys.exit()

        elif opt in ("-f", "--file"):
            zip_ref = zipfile.ZipFile(arg, "r")
            output = arg + "_unpacked"
            zip_ref.extractall(output)
            zip_ref.close()

            for path, subdirs, files in os.walk(output):
                for name in files:
                    sys.stdout.write("%s\n" % name)
                    if name.endswith(".bin"):
                        oleFile = os.path.join(path, name)
                        ole = olefile.OleFileIO(oleFile)
                        oleList = ole.listdir()
                        for i in oleList:
                            sys.stdout.write("%s\n" % i)
                            pics = ole.openstream(i)
                            data = pics.read()
                            parcelID = os.path.join(path,i[0])
                            outFile = open(parcelID, 'w')
                            outFile.write(data)

def version():
    sys.stdout.write("\nOLE Unpack Script 0.1\n")
    sys.stdout.write("Unpack .docx OLE files\n")
    sys.stdout.write("Author: Johannes Schroeter - www.devwerks.net\n\n")


def help():
    sys.stdout.write("unpack.py -f/--file FILEPATH\n")
    sys.stdout.write("Example: unpack.py -f test.docx\n\n")

def main():
    decode()
    sys.exit()


if __name__ == "__main__":
    main()
