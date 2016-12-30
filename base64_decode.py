import sys, base64, getopt

def decode():
    version()

    writeFile = False
    outFile = 0

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:i:s:", ["help", "output=", "input=", "string="])

    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:

        if opt in ("-h", "--help"):
            help()
            sys.exit()

        elif opt in ("-o", "--output"):
            outFile = open(arg, 'w')
            writeFile = True
			
        elif opt in ("-i", "--input"):
            inFile = open(arg, "r")
            inString = inFile.read()
            output = base64.b64decode(inString)

            if writeFile == True:
                outFile.write(str(output, "utf-8"))

            elif writeFile == False:
                sys.stdout.write("\n%s\n" % output)
			
        elif opt in ("-s", "--string"):
            output = base64.b64decode(arg)

            if writeFile == True:
                outFile.write(str(output, "utf-8"))

            elif writeFile == False:
                sys.stdout.write("\n%s\n" % output)

def version():
    sys.stdout.write("\nBASE64 decode Script 0.2\n")
    sys.stdout.write("decode BASE64 string or file\n")
    sys.stdout.write("Author: Johannes Schroeter - www.devwerks.net\n\n")

def help():
    sys.stdout.write("base64_decode.py -o/--output FILEPATH -i/--input INPUTFILE -s/--string BASE64STRING\n")
    sys.stdout.write("Example: base64_decode.py -s dGVzdA==\n\n")

def main():
    decode()
    sys.exit()

if __name__ == "__main__":
    main()
