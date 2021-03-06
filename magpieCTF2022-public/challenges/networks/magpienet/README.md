# MagpieNet
### Category: Networks
### Author: Josh Novak (rm -rf /)

**NOTE: The Magpienet challenge was too unstable during the competition and was removed from the competition after a few hours, but the code is still included here.**

## Description
You've heard of them before: scrapped, forgotten projects where companies become too enamoured with an idea
and then they fail spectacularly.... well Mom and Pops Flags were one of those companies. They had been 
researching ways to move and hide flags "under the radar", so they decided upon creating a network 'protocol'
called MagpieNet that would do this. Unfortunately, they didn't realize that it still ran over TCP/IP... so 
not too long in they decided to scrap the project. The last, disgruntled, employee spitefully hid a flag he
used for testing in this network somewhere... however we don't know where and we don't even know how to 
access MagpieNet in the first place! The only lead we have is a packet capture from his developer computer
days before he was let go. Take a look and maybe you'll find some clues. If I recall correctly, they had been
using a TCP port within the 35000 to 54999 range to test one of the routers, if that helps narrow it down.

## Hints
1. Mom and Pops Flags use certain subdomains when testing their projects.

## Solution
1. Search through pcap, looking for TCP communication between 35000 and 54999. Find a few packets where
   10.0.18.5 communicated to srv1.momandpopsflags.ca (shows the load balancer IP) on port 46442
  - You need to find the DNS entry for srv1.momandpopsflags.ca to match the IP to the domain
2. Note the commands he used: JOIN, PING, TRACE, LEAVE
3. Using TRACE, you see that it tells you to try to connect to other routers to see if they know it
4. Connect around to routers attempting pings: three things to find
  - File node
  - Encryption node
  - Flag node
5. Once the file node is found read the contents, get the contents of note.txt
6. After that, you go to the encryption node and attempt to decrypt it. It gives an error and shows
   the plaintext of the key and IV and clues you in to it using RC2
7. Decrypt the message (in something like cyberchef)
8. Figure out how solution works from note
9. Discover all nodes of the network
10. Calculate a hamiltonian path (more than one)
11. Connect to flag node and enter it in with spaces between each router address (e.g., A B C D E A)
12. Get the flag

## Flag
magpie{n0_n33d_t0_r31nv3nt_th3_wh33l}
