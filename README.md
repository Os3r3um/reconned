# Recon
Bug Bounty Hunting Recon Script

**Gist:** Some ~~terrible~~ continually updated python code leveraging some awesome tools that I use for bug bounty reconnaissance. 

PyBrute uses several subdomain enumeration tools and wordlists to create a unique list of subdmains that are passed to EyeWitness for reporting with categorized screenshots, server response headers and signature based default credential checking. *(resources are saved to ./bin and output is saved to ./Output/PyBrute)*


**_NOTE: This is an active recon – only perform on applications that you have permission to test against._**

##### Tools leveraged:
###### Subdomain Enumeraton Tools:
1. [Sublist3r](https://github.com/aboul3la/Sublist3r) by Ahmed Aboul-Ela 
2. [enumall](https://github.com/jhaddix/domain) by Jason Haddix 
3. [Knock](https://github.com/guelfoweb/knock) by Gianni Amato 
4. [Subbrute](https://github.com/TheRook/subbrute) by TheRook 
5. [massdns](https://github.com/blechschmidt/massdns) by B. Blechschmidt 

###### Reporting + Wordlists:
- [EyeWitness](https://github.com/ChrisTruncer/EyeWitness) by ChrisTruncer  
- [SecList](https://github.com/danielmiessler/SecLists) (DNS Recon List) by Daniel Miessler 
- [LevelUp All.txt Subdomain List](https://github.com/jhaddix) by Jason Haddix 

##### Usage
````
Example 1: python PyBrute.py -d example.com
Uses subdomain example.com with no brutefoce (Sublist3r enumall, Knock)

Example 2: python PyBrute.py -d example.com -b -p --vpn
Uses subdomain example.com with seclist subdomain list bruteforcing (massdns, subbrute, Sublist3r and enumall), adds ports 8443/8080 and checks if on VPN

Example 3: python PyBrute.py -d example.com -b --bruteall
Uses subdomain example.com with large-all.txt bruteforcing (massdns, subbrute, Sublist3r and enumall)

Example 4: python PyBrute.py -d example.com --quick
Uses subdomain example.com and only Sublist3r (+subbrute)

Note: --bruteall must be used with the -b flag
````
Option | Description
------ | --- 
--install/--upgrade  |  Both do the same function – install all prerequisite tools (Kali is a prerequisite AFAIK)
--vpn   |   Check if you are on VPN (update with your provider)
--quick |   Use ONLY Sublis3r's subdomain methods (+ subbrute)
--bruteall  |   Bruteforce with JHaddix All.txt List instead of SecList
-d  |   The domain you want to preform recon on
-b  |   Bruteforce with subbrute/massdns and SecList wordlist
-s n    |   Only HTTPs domains
-p  |   Add port 8080 for HTTP and 8443 for HTTPS 

##### Updates
- 07-15-2017: Updated to include error handling and updated reconnaissance  techniques from Bugcrowd's [LevelUp](https://pages.bugcrowd.com/level-up-virtual-hacking-conference) Conference (including subbrute/masscan and subdomain lists) - influenced by Jason Haddix's talk [Bug Hunter's Methodology 2.0](https://t.co/Umhj4NUtJ5)
