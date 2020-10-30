# qubes-sleepkeeper

Qubes-Sleepkeeper - automaticaly shutdown your Qubes OS if no password provided after wakeup from sleep.

When your Qubes wakeup from sleep it request to enter screensaver password to unload your PC.
If the attacker force you to enter the password or begin password guessing then he have only limited time to do this.
If screen will not be unlocked after some time and shutdown task will not be canceled then Qubes will shutdown automaticaly. 

### Dependences

* python3-tkinter

## Installation

Copy files to dom0. `.service` file is systemd service. Need to install and enable. This service run `qubes-sleepkeeper` program after wakeup to protect your Qubes and shutdown it if you will not cancel.

In dom0:

```
sudo qubes-dom0-update install python3-tkinter
sudo qvm-run --pass-io NAMEOFAPPVM 'cat /path/to/qubes-sleepkeeper.py' > /usr/bin/qubes-sleepkeeper
sudo chmod +x /usr/bin/qubes-sleepkeeper
sudo qvm-run --pass-io NAMEOFAPPVM 'cat /path/to/qubes-sleepkeeper.service' > /etc/systemd/system/qubes-sleepkeeper.service
sudo systemctl enable qubes-sleepkeeper.service
```

Now, test it
```
sudo systemctl start qubes-sleepkeeper.service
```

If you see BOX with timer than all is working fine. Cancel this box and try to suspend your system and wakeup. If you don't see the box disable the service and investigate what happen.

You can disable sleepkeeper at any time 
```
sudo systemctl disable qubes-sleepkeeper.service
```

Done.
