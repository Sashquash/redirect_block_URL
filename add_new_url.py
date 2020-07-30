import sys, os, argparse, socket

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--redirect", help="to redirect a URL to another",action="append", dest="redirect", metavar="<redircted URL>")
parser.add_argument("-ra", help="specify 2. URL for --redirect", action="append", dest="redirect", metavar="<original URL>")
parser.add_argument("-b", "--block", help="block a website",metavar="<blocked URL>")
parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")

args = parser.parse_args()
if os.geteuid() != 0:
    print("Not in sudo, will restart program in sudo:")
    os.execvp("sudo", ["sudo", "python3"] + sys.argv)
if args.block:
    check = 0
    while check == 0:
        fir_row = "0.0.0.0 " + args.block
        sec_row = "::      " + args.block
        thi_row = "0.0.0.0 www." + args.block
        fou_row = "::      www." + args.block
        answer = input("\nAre you sure to add:\n" + fir_row +"\n" + sec_row +"\n"+thi_row+"\n"+fou_row+"\nto the file /etc/hosts. This will localy block the website. (y/n)\n")
        if answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes":
            break
        else:
            args.block = input("Enter the new URL:\n")

    with open("/etc/hosts", "a") as hosts:
        hosts.write("\n# Firewall extension by python script\n" + fir_row + "\n" + sec_row + "\n" + thi_row + "\n" + fou_row)
elif len(args.redirect) == 2:
    redirect_url = args.redirect[0]
    original_url = args.redirect[1]
    ip = ""
    check = 0
    while check == 0:
        try:
            ip = socket.gethostbyname(redirect_url)
        except:
            print("Is " + redirect_url + " a valid URL? Or maybe you don't have internet connection...")
            redirect_url = input("Enter the new URL:\n")
            continue
    
        row = ip + " " + original_url
        answer = input("\nAre you sure to add:\n" + row + "\nto the file /etc/hosts. This will redirect " + original_url + " to " + redirect_url + " (y/n)\n")
        if answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes":
            break
        else:
            redirect_url = input("Enter the new URL:\n")
    with open("/etc/hosts", "a") as hosts:
           hosts.write("\n# Redirect extension by python script\n" + row)
