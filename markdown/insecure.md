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

