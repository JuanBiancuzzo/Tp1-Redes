import argparse

from lib.parameter import ClientParameter, OutputVerbosity

class CustomHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if action.option_strings:
            parts = []
            for option_string in action.option_strings:
                parts.append(option_string)
            return ', '.join(parts)
        else:
            return super()._format_action_invocation(action)

def obtainParameters():
    parser = argparse.ArgumentParser(
        prog = "download", 
        description = "Default description",
        formatter_class=CustomHelpFormatter,
    )

    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument(
        "-v", "--verbose", 
        action = "store_const", 
        const = OutputVerbosity.VERBOSE,
        help = "increase output verbosity"
    )
    verbosity.add_argument(
        "-q", "--quite", 
        action = "store_const",
        const = OutputVerbosity.QUIET,
        help = "decrease output verbosity"
    )

    parser.add_argument("-H", "--host", default="", dest="addr", help="server IP address")
    parser.add_argument("-p", "--port", default="", dest="port", help="port port")

    parser.add_argument("-d", "--dst", default="", dest="filepath", help="destination file path")
    parser.add_argument("-n", "--name", default="", dest="filename", help="name file name")

    args = parser.parse_args() # Sale completamente 

    outputVerbosity = OutputVerbosity.NORMAL
    if args.verbose is not None:
        outputVerbosity = args.verbose
    elif args.quite is not None:
        outputVerbosity = args.quite

    return ClientParameter(
        outputVerbosity,
        host = args.addr,
        port = args.port,
        filePath = args.filepath,
        nameFile = args.filename
    )

def main(parameter):
    print(parameter)

if __name__ == "__main__":
    parameter = obtainParameters()
    main(parameter)
