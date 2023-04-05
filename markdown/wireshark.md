<!-- space for the script -->

I was able to capture the DHCP traffic for my laptop by `releasing` and `renewing` my IP address.

Since I am on the MacOS, I released my IP address by doing these commands [(source)](https://apple.stackexchange.com/questions/17401/how-can-i-release-and-renew-my-dhcp-lease-from-terminal):

    sudo ipconfig set en0 BOOTP
    sudo ipconfig set en0 DHCP

Then I `renewed` my IP address by going into my Network settings and renewing the DHCP lease using the Apple GUI.

Here is the result where we can see the `Discover, Offer, Request, and Acknowledgement`:

![dhcp image](https://github.com/treblenaX/tcptools/blob/main/img/dhcp.png)

>Looks like the IP lease time is 90 days!