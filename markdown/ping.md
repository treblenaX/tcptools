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

