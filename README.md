# Linux Defense Scripts
Intended for use in defense competitions, probably not the real-world. They're janky but they work. Courtesy of John Ford. Enjoy :)
Note: They all have shebangs so no need to worry about typing in python3, just type the script name.
### Setup
```
git clone https://github.com/TheCatLover/Linux-Defense-Scripts.git
cd Linux-Defense-Scripts
chmod 755 *
```
### [history.py](history.py)
#### The Idea
During defense competitions, it's often important to view command history so you know what those pesky attackers have been up to. Fortunately, bash logs command history. Unfortunately, it only logs it on exit, not in realtime, and in a location that's obvious to anyone who knows bash so that they could just delete the file. Also, many distros use shells other than bash, such as dash or zsh.
So here's what you do: Remove all the shells that aren't bash and set every regular user's shell to bash - and while we're at it, let's set users with id less than 1000 to nologin because they shouldn't have access to a shell anyway. Next, change the history to be logged immediately after a command is executed, and finally, change the location of the bash history file to some place the red team won't think of looking.
#### Usage
- `history.py -s` ⇒ setup - aka remove all shells other than bash, make /bin/sh point to bash, and set user shells to bash
- `history.py -u [username]` or `history.py -u root` ⇒ add code to user's bashrc that changes history logging to /opt/.kernel/[username]/.history because why would anyone look in a hidden directory labelled kernel, am I right?
Note: if you want to view all the commands that have been recently executed, try `tail /opt/.kernel/*/.history` or `tail -n [num lines] /opt/.kernel/*/.history`. Use a `tail -f [history file]` to view commands being typed in realtime. Maybe give it an &, though I honestly haven't tried that because I wasn't smart enough to think of that until writing this README.
#### Future Work
The problem remains that red team could create a new user, and if you didn't history.py -u that user, you won't have a logfile for them. Also, let's say you accidentally history.py -u some user multiple times. The same code that's already there would be once again added. It still works, but it's a waste of space, and as a perfectionist, I hate that with a passion. So sometime this summer I'll make this spawn a process that continually checks for new users and automatically creates a logfile for them, deprecating the -u option. It shouldn't be too hard. Python makes everything ridiculously easy.
### [monitor.py](monitor.py)
#### The Idea
The `who` command allows you to see what pesky red teamer just logged in on your machine. Now typing in 'who' gets annoying after a while, so here's a script that basically does that for you and lets you know when it notices a new terminal session. In other words, you'll always know when someone logs in. I'm sure there's a cleaner way of accomplishing this, but hey, tried and tested and this works just fine.
#### Usage
`nohup monitor.py &`, you'll notice a new process running that you can find with the `ps` command (`ps aux | grep python3` if you want to see it) and on logins, everyone with a terminal open should get a message saying "NEW SHELL" followed by the name of the user and shelltype as displayed by the who command. Yeah fine, maybe it's technically called a session not a shell, but I really don't care. You go ahead and change it if that bothers you. You'll also get the NEW SHELL message when you start up the script for the first time, but don't worry about that, that's just because it has to load your session in the first time around.
### [commands.py](commands.py)
#### The Idea
When an attacker breaks in, they'll probably run a `whoami` or `pwd` or `uname -a` or something like that, and eventually they'll run an `ls` or `cat`. So if you know that, might as well make those commands kick them out and warn you that they got in! Then if you want to use those commands, just preceed them with a . like `.ls` instead of `ls`. Not very functional in the real world, but possible for defense competitions. Sounds like a good idea, right? No, it's terrible. Why would you ever do that? Are you insane?
#### Disusage
Yes, I am insane, and I therefore tried this. Let me tell you, it's really difficult to remember to put .s in front of all your commands, and when you don't, you get kicked out. Oh, and by the way, the login scripts in Linux make use of some of those commands. So you are permanently locked out unless you boot in recovery and switch things around. Oh, and all the program/services running that use those commands? They don't work either. Good luck.
Okay, but I'll satisfy your curiousity and tell you how to use this script anyway. Edit it, and for every command that you want to be updated in this way, add `update("[command]")` accordingly (or remove the existing ones if you don't want them updated). Then run `commands.py`.
#### Future Work
I suppose you could use this but with fewer/different commands than I included. My suggestion if you were to do that: figure out which commands are required for login and ensure you don't update those. Or if you get really used to putting a . in front of all your commands for some reason, then it might not be as dangerous. So feel free to play around with this but AT YOUR OWN RISK. You have no clue how this could affect your machine or the other programs that are running on it that make use of those commands. I do not recommend using this script EVER. It's a terrible thing. YOU HAVE BEEN WARNED
