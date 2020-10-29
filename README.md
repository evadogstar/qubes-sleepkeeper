# qubes-sleepkeeper

Qubes-Sleepkeeper - automaticaly shutdown your Qubes OS if no password provided after wakeup from sleep.

When your Qubes wakeup from sleep it request to enter screensaver password to unload your PC.
If the attacker force you to enter the password or begin password guessing then he have only limited time to do this.
If screen will not be unlocked after some time and shutdown task will not be canceled then Qubes will shutdown automaticaly. 

## Installation

Copy files to dom0 and other
```
sudo qvm-run --pass-io NAMEOFAPPVM 'cat /path/to/qubes-sleepkeeker.py' > /usr/bin/qubes-sleepkeeper
sudo chmod +x /usr/bin/qubes-sleepkeeper
sudo qvm-run --pass-io NAMEOFAPPVM 'cat /path/to/qubes-sleepkeeper.service' > /etc/systemd/system/qubes-sleepkeeper.service
sudo systemctl enable qubes-sleepkeeper.service
```

you can also disable it at any time 
```
sudo systemctl disable qubes-sleepkeeper.service
```

Done.
