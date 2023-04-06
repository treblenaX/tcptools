<h1>TCP/IP Tools</h1>
<p>Please check the individual markdown files or refer to the dropdowns below...</p>
<details>
                <summary>Using "ping"</summary>
                    <!-- space for the script -->

## `ping` three popular websites (for 5 or so packets each)
    1. Ping www.amazon.com three times
    2. Ping www.google.com  three times
    3. Ping www.microsoft.com three times


>What were the min/avg/max/stddev statistics for each?

`www.amazon.com`

    min = 2.955 ms
    avg = 92.156 ms
    max = 187.913 ms
    stddev = 65.451 ms

`www.google.com`

    min = 2.464 ms
    avg = 67.271 ms
    max = 151.284 ms
    stdev = 55.732 ms

`www.microsoft.com`

    min = 3.522 ms
    avg = 68.188 ms
    max = 208.974 ms
    stdev = 77.802 ms

>Was there any packet loss on any of the pings?

There were no packet loss on any of the pings I did for `www.amazon.com`, `www.google.com`, and `www.microsoft.com`

>Did the IP address change for a given website between pings?

The IP address did not change for a website between pings; however, I did notice how the ping URL address is different than what I put in. For example, `ping www.amazon.com` did not ping `www.amazon.com` directly. Rather, it pinged `d3ag4hukkh62yn.cloudfront.net`. However, Google's case was different as they did not have a different URL that is pinged.

---
## Terminal Output
`ping www.amazon.com`

    PING d3ag4hukkh62yn.cloudfront.net (18.65.233.187): 56 data bytes
    64 bytes from 18.65.233.187: icmp_seq=0 ttl=247 time=2.955 ms
    64 bytes from 18.65.233.187: icmp_seq=1 ttl=247 time=44.564 ms
    64 bytes from 18.65.233.187: icmp_seq=2 ttl=247 time=88.319 ms
    64 bytes from 18.65.233.187: icmp_seq=3 ttl=247 time=137.028 ms
    64 bytes from 18.65.233.187: icmp_seq=4 ttl=247 time=187.913 ms
    
    --- d3ag4hukkh62yn.cloudfront.net ping statistics ---
    5 packets transmitted, 5 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 2.955/92.156/187.913/65.451 ms

`ping www.google.com`

    PING www.google.com (172.217.14.228): 56 data bytes
    64 bytes from 172.217.14.228: icmp_seq=0 ttl=56 time=2.464 ms
    64 bytes from 172.217.14.228: icmp_seq=1 ttl=56 time=16.246 ms
    64 bytes from 172.217.14.228: icmp_seq=2 ttl=56 time=59.073 ms
    64 bytes from 172.217.14.228: icmp_seq=3 ttl=56 time=107.290 ms
    64 bytes from 172.217.14.228: icmp_seq=4 ttl=56 time=151.284 ms
    
    --- www.google.com ping statistics ---
    5 packets transmitted, 5 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 2.464/67.271/151.284/55.732 ms

`ping www.microsoft.com`

    PING e13678.dscb.akamaiedge.net (23.216.81.152): 56 data bytes
    64 bytes from 23.216.81.152: icmp_seq=0 ttl=53 time=208.974 ms
    64 bytes from 23.216.81.152: icmp_seq=1 ttl=53 time=96.555 ms
    64 bytes from 23.216.81.152: icmp_seq=2 ttl=53 time=16.085 ms
    64 bytes from 23.216.81.152: icmp_seq=3 ttl=53 time=3.522 ms
    64 bytes from 23.216.81.152: icmp_seq=4 ttl=53 time=15.806 ms
    
    --- e13678.dscb.akamaiedge.net ping statistics ---
    5 packets transmitted, 5 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 3.522/68.188/208.974/77.802 ms

</details>
<details>
                <summary>Using "tracert"</summary>
                    <!-- space for the script -->

## Use `tracert` (or `traceroute`, depending on your OS) on the following sites:
    www.amazon.com
    www.google.com
    www.microsoft.com

>What was the target server's IP address?

`www.amazon.com`
    
184.26.81.5

`www.google.com`

108.170.245.97

`www.microsoft.com`

 23.216.81.152

> How many hops were needed to reach the target?

`www.amazon.com`
    
11 hops

`www.google.com`

11 hops

`www.microsoft.com`

11 hops


> Can you identify your ISP from the intermediate server DNS names?

My ISP seems to be derivable from this DNS and IP: `lo0--5.uwcr-atg-1.infra.washington.edu (198.48.66.5)`. It seems that my second hop for all of the routes hits this point where it is a public IP address for the first time. 

![whatismyipaddress.com image](https://github.com/treblenaX/tcptools/blob/main/img/isp.png)

According to `whatismyipaddress.com`, my ISP is the University of Washington which makes total sense as I am on the UW WiFi. 

> Identify the "class" of IP address for each major step in the trip

`www.amazon.com`

    1   10      Class A
    2   198     Class C
    3   10      Class A
    4   10      Class A
    5   10      Class A
    6   209     Class C
    7   198     Class C
    8   163     Class B
    9   162     Class B   
    10  23      Class A  
    11  184     Class B 

`www.google.com`

    1   10      Class A
    2   198     Class C
    3   10      Class A
    4   10      Class A
    5   10      Class A
    6   209     Class C
    7   74      Class A
    8   *       *
    9   209     Class C
    10  142     Class B
    11  108     Class A

`www.microsoft.com`

    1   10      Class A
    2   198     Class C
    3   10      Class A
    4   10      Class A
    5   10      Class A
    6   209     Class C
    7   206     Class C
    8   *       * 
    9   *       * 
    10  *       *
    11  23      Class A

---
## Terminal Output

`traceroute www.amazon.com`

    traceroute to e15316.dsca.akamaiedge.net (184.26.81.5), 64 hops max, 52 byte packets
    1  irb--2523.uwir-ads-1.infra.washington.edu (10.18.0.2)  6.054 ms  2.203 ms  2.132 ms
    2  lo0--5.uwcr-atg-1.infra.washington.edu (198.48.66.5)  3.487 ms  3.225 ms  3.666 ms
    3  ae4--1009.uwcr-atg-1.infra.washington.edu (10.132.5.75)  2.685 ms  3.533 ms  2.630 ms
    4  wi_nat_int.uwcf-atg-2.infra.washington.edu (10.132.255.21)  2.027 ms  1.961 ms  2.060 ms
    5  et-8-0-0--4080.uwcr-atg-1.infra.washington.edu (10.132.255.22)  2.350 ms  2.879 ms  2.692 ms
    6  ae20--4010.icar-sttl1-3.infra.pnw-gigapop.net (209.124.188.134)  3.140 ms  3.207 ms  3.253 ms
    7  hundredge-0-0-0-24.817.core1.seat.net.internet2.edu (198.71.47.5)  5.101 ms  5.881 ms  6.732 ms
    8  fourhundredge-0-0-0-48.4079.agg2.seat.net.internet2.edu (163.253.1.165)  5.449 ms
        fourhundredge-0-0-0-49.4079.agg2.seat.net.internet2.edu (163.253.1.167)  4.525 ms  5.675 ms
    9  162.252.69.123 (162.252.69.123)  5.099 ms  2.291 ms  3.153 ms
    10  ae4.sabey-sea2.netarch.akamai.com (23.203.145.159)  4.596 ms  5.730 ms  10.624 ms
    11  a184-26-81-5.deploy.static.akamaitechnologies.com (184.26.81.5)  2.539 ms  3.667 ms  3.211 ms

`traceroute www.google.com`

    traceroute to www.google.com (142.250.217.68), 64 hops max, 52 byte packets
    1  irb--2523.uwir-ads-1.infra.washington.edu (10.18.0.2)  3.580 ms  1.708 ms  2.402 ms
    2  lo0--5.uwcr-atg-1.infra.washington.edu (198.48.66.5)  2.123 ms  2.793 ms  2.125 ms
    3  ae4--1009.uwcr-atg-1.infra.washington.edu (10.132.5.75)  2.205 ms  2.744 ms  2.172 ms
    4  wi_nat_int.uwcf-atg-2.infra.washington.edu (10.132.255.21)  2.522 ms  3.888 ms  2.037 ms
    5  et-8-0-0--4080.uwcr-atg-1.infra.washington.edu (10.132.255.22)  2.645 ms  3.064 ms  3.253 ms
    6  ae20--4011.icar-sttl1-3.infra.pnw-gigapop.net (209.124.190.134)  3.250 ms  2.424 ms  5.331 ms
    7  74.125.51.244 (74.125.51.244)  3.811 ms  3.595 ms  2.792 ms
    8  * * *
    9  209.85.254.236 (209.85.254.236)  177.589 ms
        142.251.50.242 (142.251.50.242)  5.953 ms
        209.85.254.236 (209.85.254.236)  4.429 ms
    10  142.251.55.199 (142.251.55.199)  3.040 ms
        142.251.55.197 (142.251.55.197)  3.107 ms  2.670 ms
    11  108.170.245.97 (108.170.245.97)  4.420 ms
        sea09s29-in-f4.1e100.net (142.250.217.68)  2.726 ms
        108.170.245.97 (108.170.245.97)  3.850 ms

`traceroute www.microsoft.com`

    traceroute to e13678.dscb.akamaiedge.net (23.216.81.152), 64 hops max, 52 byte packets
    1  irb--2523.uwir-ads-1.infra.washington.edu (10.18.0.2)  3.487 ms  2.006 ms  2.104 ms
    2  lo0--5.uwcr-atg-1.infra.washington.edu (198.48.66.5)  2.473 ms  2.526 ms  13.315 ms
    3  ae4--1009.uwcr-atg-1.infra.washington.edu (10.132.5.75)  19.658 ms  2.873 ms  3.460 ms
    4  wi_nat_int.uwcf-atg-2.infra.washington.edu (10.132.255.21)  2.660 ms  2.762 ms  2.172 ms
    5  et-8-0-0--4080.uwcr-atg-1.infra.washington.edu (10.132.255.22)  2.927 ms  5.696 ms  3.098 ms
    6  ae20--4010.icar-sttl1-3.infra.pnw-gigapop.net (209.124.188.134)  2.663 ms  3.083 ms  6.241 ms
    7  six-sea2.netarch.akamai.com (206.81.80.168)  3.155 ms  3.980 ms  3.123 ms
    8  * * *
    9  * * *
    10  * * *
    11  a23-216-81-152.deploy.static.akamaitechnologies.com (23.216.81.152)  4.141 ms  2.418 ms  3.298 ms
</details>
<details>
                <summary>Using "ngrok"</summary>
                    <!-- space for the script -->

I checked out "ngrok" and deployed a really quick website! 

![ngrok image](https://github.com/treblenaX/tcptools/blob/main/img/ngrok.png)</details>
<details>
                <summary>Using packet-capture tools</summary>
                    <!-- space for the script -->

## Capture the DHCP traffic for your laptop
    Filter out any extraneous traffic so we see only the DHCP traffic
    Submit a screenshot of the DORA process and the lease time offered by the DHCP server.

I was able to capture the DHCP traffic for my laptop by `releasing` and `renewing` my IP address.

Since I am on the MacOS, I released my IP address by doing these commands [(source)](https://apple.stackexchange.com/questions/17401/how-can-i-release-and-renew-my-dhcp-lease-from-terminal):

    sudo ipconfig set en0 BOOTP
    sudo ipconfig set en0 DHCP

Then I `renewed` my IP address by going into my Network settings and renewing the DHCP lease using the Apple GUI.

Here is the result where we can see the `Discover, Offer, Request, and Acknowledgement`:

![dhcp image](https://github.com/treblenaX/tcptools/blob/main/img/dhcp.png)

>Looks like the IP lease time is 90 days!</details>
<details>
                <summary>Spy on your opponents</summary>
                    <!-- space for the script -->

    Begin playing an online multiplayer game (your choice!)
    Capture the traffic for the online game play

        Filter out any extraneous traffic
        See if you can identify your name/handle or other identifying information in the stream
        Take a screen shot of Wireshark and explain what you found in the README.md file.

    You don't need to be correct, but you do need to be convincing

I played on `www.krunker.io`, an online browser first-person shooter.

![krunker image](https://github.com/treblenaX/tcptools/blob/main/img/krunker.png)

![udp image](https://github.com/treblenaX/tcptools/blob/main/img/udp.png)

I checked out the UDP protocol packets in Wireshark and found that the data for the UDP protocols are encrypted! This was the value in the packet I was looking at:

    4908d4e0eed5f822dd55aa2cbaa5935c4a117131cb720a5a77739884647bb25efd100bb12d7d7a16a77aa81c0a6e88c440809686a3dceacc7ee4ba125a06b967eef2b0786962119dca831050a81c9da08d4563b4e76f80e4246cf772d4d4be6a35c1dc1dcbabb10b90796090c886e5619f9dfb0df38fdf3aaa0ea02d90f7181be82ef7536c059373cdc45a0953aa7cf2bd2c76fe878de8fd185d00ad09e0a640bdb990c320a0d3e68dbdef24bd8702ce78ac91fb7b0f7a90834837f771cb749a8eab450658aef1c9da28865f02de1fc15372a8c40ae1bccabccb353c0bdb24cf327a870f89d37ef4f8f25ac8e18f404dd797a4eab031b3496614532f3678abd83c593dbba7630bbb9f86a4512dbe2f18d5c1d2d4f0972fed62dcf1f291591e32ecc9b996bbdee29acaeb5992ecce6824c6f8e39141f53beb57d9673bdb0654e25a880612c47f4bd4cafd5f83911e30b46b96344baca266dd33d95a4e4c60ee3d37b4d69da62d70e431428c9d26ae33af461ee10af7660558fd01c7d87bded15ab2d0f23e4f7ed315745c42e95287acf5cb3f5e4c6e2c2349101b79c291d1140278fd88d9145134d881790cb77437aa330ce596d4af6e413fef05e91f6b158dfde9f18109d70cb4a9f9e46908d6e90eac9f9c9b0580e1b8bf54d68c783f49d5710d16df114d13948768e8888b312fc2bf82720e0169c4d32a8ece21848b8873630929393231faef7ad08b6b9f0697f4c4b201f7d6558d824ae766f6d5eb737d982e1579da08784e9db28dfc657fcfeda48f88a48b03362fe4a7017ea79cc5d7b784234bf983436875a80e9dc4ec123c09e802aee78544a67905f17eabc5330955d24a68df6b6c29b752b47571ef72dded9435169e9a1731662f484423e44dacdaed074ab785907dd5bc4bac01e729d9ec327149e993748f3613d2586835adc9946c797c0f326512a23954f7e305bb9b7108d5b089c4135f54310f0e4d6720bbbcdde2970d298dc6e0608b490d7bdabd2b8d6f293727454692f751cf8fc9031e35fc0acde6b11ecbf3639e0dcbd71912707a71db497a04af629505471d8f9079fe22d652aa6f36f2e558b34e95cab016298fafd6942250b0a24624c7c02b8676026b5c9846be80be47f69886af35f05be94bbe64802a4662d3a0e0b6c076fbfacbc44071a3dc323eed1b0fb4c3b94e9bdbfdfd1fc18d29e011c255141277b247e9225edb5e6e299716e208276ba855fc9b2f99bb226c4907b62a8a2d9bf57f4f0ffc5d07cd5bf828b51fce9cd7e1f824dd9d22afe2c802ee4fb18c4e8d0199c7ed839921b7de81f4f560332a91f40a25dd7f1a13e78317476f61a851a87daf89d2fd9d16703973375181fd4ec9f5e072c8055746777826792c5df1609ddde14688721d336d5dc1e93919975455e668d7c03e8b7e50cd622767a2f28790ad5a0e187330e057dae0c09052fa149d3227c5a3f5c67b9e5de2d54ee3878ac595ea861bcb93d3127f5babf871771bdb051ebb11513e64a1d4054ae1ad72632b05aa8328e1f207c9e4de29c72b3941e4caaace92a14de066a728d9c384a8c4ccd126ebb80e521d072d18a70023d883af7c243bfe6e7a86104a6db452070188b9aaec491e22b10e8ec291856cefc79831a3ce5e95030441ec2805ac0f48d4b5efd133c6fd770b391e175289042df3df5a3dceacc2

I thought that these were hexadecimals that could be translated to ASCII text but the patterns do not match up and the conversion is just plain gibberish. Therefore, I concluded that there is some sort of encryption with these UDP messages that is hiding information from packet sniffers like me! Great for security, not so fun for solving this exercise.

</details>
<details>
                <summary>Insecure web server</summary>
                    <!-- space for the script -->

    Navigate to http://150.230.36.255/
    Submit the login form with any email and password while capturing packets with Wireshark.
    Filter out any extraneous traffic so we see only the traffic to the server
    Take a screen shot of Wireshark showing the payload (email, password) you sent to the server
    Store the screen shot in the Github repo

After filtering out the traffic to packets with a destination to `150.230.36.255`, we can see how our payload is insecure and how I found the credentials I put into the website.

    email: t@t.com
    password: test

![insecure web server with data](https://github.com/treblenaX/tcptools/blob/main/img/insecure.png)

</details>
