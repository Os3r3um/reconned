# Recon
Bug Bounty Hunting Recon Script

Gist: Some terrible python code leveraging awesome programs that I use personally for bug bounty recon… I hope to spend time to make it better.

NOTE: This is an active recon – only perform on application you have permission to test. 

Tools leveraged:
- Sublist3r by Ahmed Aboul-Ela (https://github.com/aboul3la/Sublist3r)
- Domain by Jason Haddix (https://github.com/jhaddix/domain)
- Knock by Gianni Amato (https://github.com/guelfoweb/knock)
- EyeWitness by ChrisTruncer  (https://github.com/ChrisTruncer/EyeWitness)

Usage: 
python PyBrute.py -d example.com -p --vpn

Commands:

  --install/--upgrade – Both do the same function – install all prerequisite tools (Kali is a prerequisite AFAIK)

  -d – domain you want to preform recon on

  --vpn – Check if you are on VPN (update with your provider)

  -b – Use ONLY Sublis3r's subdomain methods (+ subbrute)

  -s n – List of URL’s include only HTTPS
  
  -p - Add port 8080 for HTTP and 8443 for HTTPS
