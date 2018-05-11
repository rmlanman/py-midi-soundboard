# Py Midi Soundboard

This is a super simple midi soundboard I wrote for a dumb office toy. I am by no means a python developer, so the code
follows no practices nor conventions. Take at your own risk

### My Setup (dependencies...sort of)

 * A midi keyboard (I used the [midiplus AKM320](https://www.amazon.com/midiplus-AKM320-MIDI-Keyboard-Controller/dp/B00VHKMK64/))
 * A [Raspberry Pi 2b](https://www.amazon.com/Raspberry-Pi-Model-Desktop-Linux/dp/B00T2U7R7I/) (a Pi3 would work just fine also and might be cheaper)
 * An 8GB Micro SD Card
 * [Raspbian NOOBS](https://www.raspberrypi.org/downloads/noobs/) 2.8
 * [Alsa Seq Python bindings](https://github.com/ppaez/alsaseq) - [Docs](http://pp.com.mx/python/alsaseq/project.html)
 * PyYaml - installed using apt-get
 * PyGame - installed using apt-get
 
### Installation

 1. Set up your raspberry pi by using the NOOBS guide. I highly recommend only installing Raspbian LITE, as I ended up
removing a few things that were taking up a ton of disk space on the full install.
 2. Create a directory `/opt/soundboard` and copy soundboard.py here
 3. Copy soundboard.conf.tpl to `/etc/soundboard.conf` and add your configurations
 4. Add your sound files to your configured sounds directory
 5. Copy soundboard.service into `/etc/systemd/system/`
 6. Register the soundboard as a service: `systemctl daemon-reload && systemctl enable soundboard && systemctl start soundboard --no-block`
 7. ???
 8. Profit
 
You will need to restart the soundboard as you change configuration, this can be done using `systemctl restart soundboard`