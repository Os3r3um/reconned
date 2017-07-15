import argparse, os, requests, time, csv
import datetime

today = datetime.date.today()

__author__ = 'Caleb Kinney'

global url, secure


def get_args():
    parser = argparse.ArgumentParser(
        description='PyBrute')
    parser.add_argument(
        '-d', '--domain', type=str, help='Domain', required=False, default=False)
    parser.add_argument(
        '-s', '--secure', help='Secure', nargs='?', required=False, default=False)
    parser.add_argument(
        '-b', '--bruteforce', help='Bruceforce', nargs='?', default=False)
    parser.add_argument(
        '--upgrade', help='Upgrade', nargs='?', default=False)
    parser.add_argument(
        '--install', help='Install', nargs='?', default=False)
    parser.add_argument(
        '--vpn', help='VPN Check', nargs='?', default=False)
    parser.add_argument(
        '-p', '--ports', help='Ports', nargs='?', default=False)

    # return url, secure
    return parser.parse_args()


# url, secure, bruteforce = get_args()

newpath = r'Output/PyBrute'
if not os.path.exists(newpath):
    os.makedirs(newpath)


def banner():
    print("\033[1;31m__________        __________                __     ")
    print("\033[1;31m\______   \___.__.\______   \_______ __ ___/  |_  ____")
    print("\033[1;31m |     ___<   |  | |    |  _/\_  __ \  |  \   __\/ __ \ ")
    print("\033[1;31m |    |    \___  | |    |   \ |  | \/  |  /|  | \  ___/")
    print("\033[1;31m |____|    / ____| |______  / |__|  |____/ |__|  \___  >")
    print("\033[1;31m           \/             \/                         \/ ")


def sublist3r():
    if vpn is not False:
        vpncheck()
    sublist3rFileName = ("Output/PyBrute/" + domain + "_sublist3r.txt")
    Subcmd = (("python bin/Sublist3r/sublist3r.py -v -t 15 -d %s -o " + sublist3rFileName) % (domain))
    print("\n\033[1;31mRunning Command: \033[1;37m" + Subcmd)
    os.system(Subcmd)
    print("\n\033[1;31mSublis3r Complete\033[1;37m")
    time.sleep(1)


def sublist3rBrute():
    if vpn is not False:
        vpncheck()
    sublist3rFileName = ("Output/PyBrute/" + domain + "_sublist3r.txt")
    Subcmd = (("python bin/Sublist3r/sublist3r.py -v -b -t 15 -d %s -o " + sublist3rFileName) % (domain))
    print("\n\033[1;31mRunning Command: \033[1;37m" + Subcmd)
    os.system(Subcmd)
    print("\n\033[1;31mSublis3r Complete\033[1;37m")
    time.sleep(1)
    eyewitness(sublist3rFileName)


def domainrecon():
    if vpn is not False:
        vpncheck()
    JHdomainCMD = "python bin/domain/enumall.py %s" % (domain)
    print("\n\033[1;31mRunning Command: \033[1;37m" + JHdomainCMD)
    os.system(JHdomainCMD)
    print("\n\033[1;31mDomain Complete\033[1;37m")
    time.sleep(1)


def knockpy():
    rootdomainStrip = domain.replace(".", "_")
    os.system("rm " + rootdomainStrip + "*")
    if vpn is not False:
        vpncheck()
    knockpyCmd = ("python bin/knockpy/knockpy/knockpy.py -c " + domain)
    print("\n\033[1;31mRunning Command: \033[1;37m" + knockpyCmd)
    os.system(knockpyCmd)
    filenameKnock = (rootdomainStrip + "*")
    knockpyFilenameInit = ("Output/PyBrute/" + domain + "_knock.csv")
    print("\n\033[1;31mSleeping (1/3)...zzzzzZZZzzzz\033[1;37m")
    time.sleep(1)
    os.system("cp " + filenameKnock + ".csv " + knockpyFilenameInit)
    print("\n\033[1;31mSleeping (2/3)...zzzzzZZZzzzz\033[1;37m")
    time.sleep(1)
    knockpySubs = []
    with open(knockpyFilenameInit, 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            knockpySubs.append(row[3])
    filenameKnocktxt = (knockpyFilenameInit + ".txt")
    f1 = open(filenameKnocktxt, "w")
    for hosts in knockpySubs:
        hosts = "".join(hosts)
        f1.writelines("\n" + hosts)
    f1.close()
    time.sleep(1)
    os.system("rm " + knockpyFilenameInit)
    os.system("rm " + filenameKnock + ".csv")


def eyewitness(filename):
    rootdomain = domain
    EWHTTPScriptIPS = (
        "python bin/EyeWitness/EyeWitness.py -f " + filename + " --active-scan --no-prompt --headless  -d " + "Output/PyBrute/" + rootdomain + "-" + time.strftime(
            '%m-%d-%y-%H-%M') + "-Sublist3r-EW ")
    if vpn is not False:
        print(
            "\n\033[1;31mIf not connected to VPN manually run the following command on reconnect:\n\033[1;37m" + EWHTTPScriptIPS)
        vpncheck()
        print("\n\033[1;31mRunning Command: \033[1;37m" + EWHTTPScriptIPS)
        os.system(EWHTTPScriptIPS)
    print("\a")


def upgradeFiles():
    binpath = r'bin'
    if not os.path.exists(binpath):
        os.makedirs(binpath)
    else:
        os.system("rm -r bin")
        os.makedirs(binpath)
    sublist3rUpgrade = ("git clone https://github.com/aboul3la/Sublist3r.git ./bin/Sublist3r")
    print("\n\033[1;31mRunning Command: \033[1;37m" + sublist3rUpgrade)
    os.system(sublist3rUpgrade)
    subInstallReq = ("sudo pip install -r bin/Sublist3r/requirements.txt")
    print("\n\033[1;31mRunning Command: \033[1;37m" + subInstallReq)
    os.system(subInstallReq)
    eyeWitnessUpgrade = ("git clone https://github.com/ChrisTruncer/EyeWitness.git ./bin/EyeWitness")
    print("\n\033[1;31mRunning Command: \033[1;37m" + eyeWitnessUpgrade)
    os.system(eyeWitnessUpgrade)
    print("Sublis3r Installed")
    eyeInstallReq = ("sudo bash bin/EyeWitness/setup/setup.sh")
    print("\n\033[1;31mRunning Command: \033[1;37m" + eyeInstallReq)
    os.system(eyeInstallReq)
    cpphantomjs = ("cp phantomjs bin/EyeWitness/bin/")
    print("\n\033[1;31mRunning Command: \033[1;37m" + cpphantomjs)
    os.system(cpphantomjs)
    movephantomjs = ("mv phantomjs bin/")
    print("\n\033[1;31mRunning Command: \033[1;37m" + movephantomjs)
    os.system(movephantomjs)
    print("EyeWitness Installed")
    domainUpgrade = ("git clone https://github.com/jhaddix/domain.git ./bin/domain")
    print("\n\033[1;31mRunning Command: \033[1;37m" + domainUpgrade)
    os.system(domainUpgrade)
    print("Domain Installed")
    knockpyUpgrade = ("git clone https://github.com/guelfoweb/knock.git ./bin/knockpy")
    print("\n\033[1;31mRunning Command: \033[1;37m" + knockpyUpgrade)
    print("Knockpy Installed")
    os.system(knockpyUpgrade)


def subdomainfile():
    sublist3rFileName = ("Output/PyBrute/" + domain + "_sublist3r.txt")
    reconFileName = (domain + ".lst")
    subdomainAllFile = ("Output/PyBrute/" + domain + "-all.txt")
    knockpyFileName = ("Output/PyBrute/" + domain + "_knock.csv.txt")
    with open(sublist3rFileName) as f:
        SubHosts = f.read().splitlines()
    f.close()
    time.sleep(2)
    f1 = open(subdomainAllFile, "w")
    for hosts in SubHosts:
        hosts = "".join(hosts)
        f1.writelines("\n" + hosts)
    f1.close()
    with open(reconFileName) as f:
        SubHosts = f.read().splitlines()
    f.close()
    time.sleep(2)
    f1 = open(subdomainAllFile, "a")
    for hosts in SubHosts:
        hosts = "".join(hosts)
        f1.writelines("\n" + hosts)
    f1.close()
    with open(knockpyFileName) as f:
        SubHosts = f.read().splitlines()
    f.close()
    time.sleep(2)
    f1 = open(subdomainAllFile, "a")
    for hosts in SubHosts:
        hosts = "".join(hosts)
        f1.writelines("\n" + hosts)
    f1.close()
    domainList = open(subdomainAllFile, 'r')
    uniqueDomains = set(domainList)
    domainList.close()
    subdomainUniqueFile = ("Output/PyBrute/" + domain + "-unique.txt")
    uniqueDomainsOut = open(subdomainUniqueFile, 'w')
    for domains in uniqueDomains:
        domains = domains.replace('\n', '')
        if domains.endswith(domain):
            uniqueDomainsOut.writelines("https://%s" % domains + "\n")
            if ports is not False:
                uniqueDomainsOut.writelines("https://%s" % domains + ":8443" + "\n")
            if secure is False:
                uniqueDomainsOut.writelines("http://%s" % domains + "\n")
                if ports is not False:
                    uniqueDomainsOut.writelines("http://%s" % domains + ":8080" + "\n")
    uniqueDomainsOut.close()
    time.sleep(5)
    reconFileNamecsv = (domain + ".csv")
    os.remove(sublist3rFileName)
    os.remove(reconFileName)
    os.remove(reconFileNamecsv)
    os.remove(knockpyFileName)
    eyewitness(subdomainUniqueFile)


def vpncheck():
    vpnck = requests.get('http://ipinfo.io')
    # Change "Comcast" to your provider or City")
    if "Comcast" in vpnck.content:
        print("\n\033[1;31mNot connected via VPN \033[1;37m")
        print("\n" + vpnck.content)
        quit()
    else:
        print("\n\033[1;31mConnected via VPN \033[1;37m")
        print("\n" + vpnck.content)
        time.sleep(5)


if __name__ == "__main__":
    banner()
    args = get_args()
    domain = args.domain
    secure = args.secure
    bruteforce = args.bruteforce
    upgrade = args.upgrade
    install = args.install
    ports = args.ports
    vpn = args.vpn
    if upgrade is not False:
        upgradeFiles()
    if install is not False:
        upgradeFiles()
    if domain is not False:
        if bruteforce is not False:
            sublist3rBrute()
        else:
            sublist3r()
            domainrecon()
            knockpy()
            subdomainfile()
    print("Done!")
