class iptools():
  def getIP():
    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

  def pingIP(target):
    import os
    cmd="ping "+target
    os.system(cmd)
  
  def getWebsiteIP(target):
    import socket
    import sys
    ends=[".org", ".com", ".info", ".net", ".html", ".htm", ".us", ".co", ".gov", ".xyz", ".edu", ".me", ".ly", ".site", ".app",".ae", ".io", ".nz"]
    for item in ends:
      if item in target:
        print(f'The {target} IP address is {socket.gethostbyname(target)}')
        input("Press any key to exit")
        return
    sys.exit("Please enter a valid website address with a different extension")
