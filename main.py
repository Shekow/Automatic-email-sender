from Emails import EmailSender
from argparse import ArgumentParser
import sys


def main():
    parser = ArgumentParser()
    parser.add_argument("-u", "--username", help="Username(e-mail address)")
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument("-t", "--template", help="Template file(HTML)")
    parser.add_argument(
        "-f",
        "--csvfile",
        help="The name of a csv file that has the required data: 'receiver', 'subject', 'attachments'(optional), and any required context (in case of using a template)",
    )
    parser.add_argument("-s", "--subject", help="Subject of the emails (will be taken from the csv file if not provided)")

    args = parser.parse_args()
    try:
        sender = EmailSender(args.username, args.password)
        sender.setTemplate(args.template)
        sender.sendFromCSV(args.csvfile, True, args.subject)
    except:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
