<H1 align="center", height="1500"> <ins> README.md File </ins> </H1>
<H1 align="center"> <ins>  0x05. Processes and signals README.md</ins> </H1>

<p align="center">
  <img src="https://i.ibb.co/YbhzbPX/0x05-Processes-and-signals-Alx-logo.png" />
</p>

##

* **File_name:📋** 📖 [**README.md**](https://github.com/BekaHabesha/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/README.md)
* **Created: 📅** <ins>**On December 22, 2023**</ins>🕙
* **Author:🖊️** 👨🏻‍💻 [***Bereket Dereje Mekkonen***](https://intranet.alxswe.com/users/BereketDerejeMekonnen) 🧑‍💻
* **Project Title: 🔠**  💻 [**0x05. Processes and signals**](https://intranet.alxswe.com/projects/255) 📝🔡
* **GitHub repository: 📦** 🗂 [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops) 🗂
* **Directory: 💼** 📂 [**0x05-processes_and_signals**](https://github.com/BekaHabesha/alx-system_engineering-devops/tree/master/0x05-processes_and_signals)
* **Project Tasks: 📚** <ins>**Mandatory💯 and Advanced ⁉️**</ins>
* **Tasks in number: 🔢** <ins>**12 Tasks (9-Mandatory & 3-Advanced)**</ins>
* **Mandatory_Tasks:** 💯 <ins>**From Task 0 to 8**</ins> 💯
* **Advanced_Tasks:** ⁉️ <ins>**From Task 9 to 11**</ins> ♨️

###   

<p align="center">
  <img src="https://i.ibb.co/ZV48Drd/Alx-next-generation.png" />
</p>
                     
##

## <ins>**PROJECT_TITLE</ins>:**   [**0x05. Processes and signals**](https://intranet.alxswe.com/projects/255)

## <ins>**GITHUB_REPOSITORY</ins>: 📂**    [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops)

## <ins>**DIRECTORY</ins>: 📂**   [**0x05-processes_and_signals**](https://github.com/BekaHabesha/alx-system_engineering-devops/tree/master/0x05-processes_and_signals)

###

<p align="center">
  <img src="https://d1m75rqqgidzqn.cloudfront.net/wp-data/2021/06/11162836/iStock-1313617131.jpg" />
</p>


# About ${{\color{red}\Huge\{\textsf{ Bash\}}}}$ projects 

* **<ins>Unless stated</ins>, all your projects will be <ins>auto-corrected with Ubuntu 20.04 LTS</ins>.**

<p align="center">
  <img src="https://static.javatpoint.com/linux/images/linux-signals1.png" />
</p>

<h1> <ins>Resources</ins> :floppy_disk:</H1>

### **Read or watch:** :heavy_check_mark:
* [**Linux PID**](https://intranet.alxswe.com/rltoken/qVGxUt1QMIV4B4oVrQBlQg)
* [**Linux process**](https://intranet.alxswe.com/rltoken/px2TdWSjVO8i9SB5gHchAw)
* [**Linux signal**](https://intranet.alxswe.com/rltoken/qQSGz9CN52PVF3IPCuaRiw)
* [**Process management in linux**](https://intranet.alxswe.com/rltoken/XlYrlghzNZ6Z1cbI_IPaiA)

### **man or help:** :heavy_check_mark:
* ${{\color{red}{\textsf{ ps\ \}}}}$
* ${{\color{red}{\textsf{ pgrep\ \}}}}$
* ${{\color{red}{\textsf{ pkill\ \}}}}$
* ${{\color{red}{\textsf{ kill\ \}}}}$
* ${{\color{red}{\textsf{ exit\ \}}}}$
* ${{\color{red}{\textsf{ trap\ \}}}}$

<p align="center">
  <img src="https://www.bogotobogo.com/Linux/images/process/ProcessState.png" />
</p>

###

<H1><ins>Learning Objectives</ins>:floppy_disk:</H1>

* At the end of this project, You are expected to be able to [**explain to anyone**](https://intranet.alxswe.com/rltoken/_zeQBWHdlNNOM-5IqFDhSQ), **Without the help of Google:**

<p align="center">
  <img src="https://www.norberthires.blog/content/images/2022/01/the-feynman-technique.png" />
</p>

###

<H2> <ins>General Learning Objectives</ins> :heavy_check_mark:</H2>

* **What is a <ins>PID</ins>.**
* **What is a <ins>process</ins>.**
* **How to <ins>find a process’ PID</ins>.**
* **How to <ins>kill a process</ins>.**
* **What is a <ins>signal</ins>.**
* **What are the <ins>2 signals</ins> that cannot be <ins>ignored</ins>.**

<p align="center">
  <img src="https://i.ibb.co/tXVbgc6/shell-process.png" />
  <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff644f574-97c7-488c-8fc8-2c5f096604be_796x329.png" />
  <img src="https://www.bogotobogo.com/Linux/images/process/exec_ls.png" />
</p>

###

<H2> <ins>Copyright - Plagiarism</ins> :heavy_check_mark:</H2>

* You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
* You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
* You are not allowed to publish any content of this project.
* Any form of plagiarism is strictly forbidden and will result in removal from the program.

<p align="center">
  <img src="https://i.ibb.co/8csnv7s/Alx-do-hard-things.jpg" />
</p>

##

<H1><ins>Requirements</ins> :floppy_disk:</H1>

<H2>General :heavy_check_mark:</H2>

* Allowed editors: <ins>**vi**</ins>, <ins>**vim**</ins>, <ins>**emacs**</ins>.
* All your <ins>**files**</ins> will be **interpreted** on <ins>**Ubuntu 20.04 LTS</ins>.**
* All your <ins>**files**</ins> should **end with a new line**
* A ${{\color{red}{\textsf{ README.md\ \}}}}$ <ins>**file**</ins>, at the root of the folder of the project is mandatory.
* All **your Bash script files** must be **executable**.
* Your **<ins>Bash script**</ins> **must <ins>pass**</ins> ${{\color{red}{\textsf{ Shellcheck\ \}}}}$ (**version** ${{\color{red}{\textsf{ 0.7.0\ \}}}}$ **) without any error.**
* The <ins>**first line of all your Bash scripts</ins>** should be exactly [**#!/usr/bin/env bash**](./1-for_best_school)
* The <ins>**second line of all your Bash scripts</ins>** should be a **a comment explaining what is the <ins>script doing</ins>.**

<p align="center">
  <img src="https://www.tecmint.com/wp-content/uploads/2015/05/Linux-Health-Monitoring.png" />
  <img src="https://image2.slideserve.com/4586249/signal-sources-l.jpg" />
</p>

##

<H1><ins>More Info</ins> :floppy_disk:</H1>

For those who want to know more and learn about all signals, check out [**this article**](https://intranet.alxswe.com/rltoken/BOU-KVNMqfKEIBo_VOI26A).

<p align="center">
  <img src="https://people.cs.rutgers.edu/~pxk/416/notes/images/04-proc_states_2.png" />
  <img src="https://qph.cf2.quoracdn.net/main-qimg-be1eec15881160468eed9acc375eccda-pjlq" />
</p>

##

## <ins>**PROJECT_TITLE</ins>:**   [**0x05. Processes and signals**](https://intranet.alxswe.com/projects/255)

## <ins>**GITHUB_REPOSITORY</ins>: 📂**    [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops)

## <ins>**DIRECTORY</ins>: 📂**   [**0x05-processes_and_signals**](https://github.com/BekaHabesha/alx-system_engineering-devops/tree/master/0x05-processes_and_signals)

##

* **File_name:📋**
  * 📖 [**README.md**](https://github.com/BekaHabesha/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/README.md) 📖 **file**
* **Created: 📅** 
  * 📅 <ins>**On December 22, 2023**</ins> 🕙
* **Author:🖊️** 
  * 👨🏻‍💻 [***Bereket Dereje Mekkonen***](https://intranet.alxswe.com/users/BereketDerejeMekonnen) 🧑‍💻
* **Project Title: 🔠**  
  * 💻 [**0x05. Processes and signals**](https://intranet.alxswe.com/projects/255) 🔡
* **GitHub repository: 📦** 
  * 🗂 [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops) 🗂
* **Directory: 💼** 
  * 📂 [**0x05-processes_and_signals**](https://github.com/BekaHabesha/alx-system_engineering-devops/tree/master/0x05-processes_and_signals)
* **Project Tasks: 📚** 
  * <ins>**Mandatory💯 and Advanced ⁉️**</ins>
* **Tasks in number: 🔢** 
  * <ins>**12 Tasks (9-Mandatory & 3-Advanced)**</ins>
* **Mandatory_Tasks:** 
  * 💯 <ins>**From Task 0 to 8**</ins> 💯
* **Advanced_Tasks:** 
  * ⁉️ <ins>**From Task 9 to 11**</ins> ♨️

###

<p align="center">
  <img src="https://i.ibb.co/y5wmQyd/Alx-enginn-Build-ur-future.png" />
</p>

<H1 align="center"> <ins> PROJECT TASKS (Mandatory and Advanced)</ins>:floppy_disk:</H1>

<H1 align="center">MANDATORY_TASKS (From Task 0 to 8) :cd:</h1>

## **No. 0. What is my PID** :heavy_check_mark:
* **File:**
  * [**0-what-is-my-pid**](./0-what-is-my-pid)
###
* **Write a** <ins>**Bash script</ins> that displays** its <ins>**own PID</ins>.**
###
```js
BekaHabesha@ubuntu$ ./0-what-is-my-pid
556
BekaHabesha@ubuntu$ 
```

##

## **No. 1. List your processes**:heavy_check_mark:
* **File:**
  * [**1-list_your_processes**](./1-list_your_processes)
###
* **Write a** <ins>**Bash script</ins> that displays** a list of <ins>**currently running processes</ins>.**
###
* **<ins>Requirements</ins>:**
  * Must show **all <ins>processes</ins>, for all <ins>users</ins>,** including those which might not have a **<ins>TTY</ins>.**
  * **Display in a <ins>user-oriented format</ins>.**
  * Show **<ins>process hierarchy</ins>.**
###
```js
BekaHabesha@ubuntu$ ./1-list_your_processes | head -50
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.6 100412 11196 ?        Ss   19:49   0:07 /sbin/init
root           2  0.0  0.0   2456  1328 ?        Sl   19:49   0:02 /init
root           5  0.0  0.0   2484   212 ?        Sl   19:50   0:00  \_ plan9 --control-socket 6 --log-level 4 --server-fd 7 --pipe-fd 9 --log-truncate
root         301  0.0  0.0   2464   108 ?        Ss   19:50   0:00  \_ /init
root         302  0.0  0.0   2480   112 ?        S    19:50   0:00  |   \_ /init
bekihab+     303  0.0  0.3   6212  5240 pts/0    Ss   19:50   0:01  |       \_ -bash
bekihab+     560  0.0  0.1   4780  3172 pts/0    S+   22:27   0:00  |           \_ bash ./1-list_your_processes
bekihab+     562  0.0  0.2   7908  3400 pts/0    R+   22:27   0:00  |           |   \_ ps -auxf
bekihab+     561  0.0  0.0   3220  1000 pts/0    S+   22:27   0:00  |           \_ head -50
root         304  0.0  0.3   7516  5004 pts/1    Ss   19:50   0:00  \_ /bin/login -f
bekihab+     322  0.0  0.3   6120  5060 pts/1    S+   19:50   0:00      \_ -bash
root          58  0.0  0.9  47728 15232 ?        S<s  19:50   0:04 /lib/systemd/systemd-journald
root          86  0.0  0.3  21964  5580 ?        Ss   19:50   0:03 /lib/systemd/systemd-udevd
root          93  0.0  0.1   4760  1904 ?        Ss   19:50   0:02 snapfuse /var/lib/snapd/snaps/core22_1033.snap /snap/core22/1033 -o ro,nodev,allow_other,suid
root          97  0.0  0.0   4492   188 ?        Ss   19:50   0:00 snapfuse /var/lib/snapd/snaps/core22_864.snap /snap/core22/864 -o ro,nodev,allow_other,suid
root          98  0.0  0.0   4492   168 ?        Ss   19:50   0:00 snapfuse /var/lib/snapd/snaps/bare_5.snap /snap/bare/5 -o ro,nodev,allow_other,suid
root         107  0.0  0.0   4624   196 ?        Ss   19:50   0:00 snapfuse /var/lib/snapd/snaps/gtk-common-themes_1535.snap /snap/gtk-common-themes/1535 -o ro,nodev,allow_other,suid
root         111  0.0  0.0   4492   172 ?        Ss   19:50   0:00 snapfuse /var/lib/snapd/snaps/ubuntu-desktop-installer_1276.snap /snap/ubuntu-desktop-installer/1276 -o ro,nodev,allow_other,suid
root         112  0.0  0.0   4492   172 ?        Ss   19:50   0:00 snapfuse /var/lib/snapd/snaps/snapd_20092.snap /snap/snapd/20092 -o ro,nodev,allow_other,suid
root         117  0.0  0.1   4768  1748 ?        Ss   19:50   0:03 snapfuse /var/lib/snapd/snaps/ubuntu-desktop-installer_1278.snap /snap/ubuntu-desktop-installer/1278 -o ro,nodev,allow_other,suid
root         121  0.0  0.1   4784  1772 ?        Ss   19:50   0:06 snapfuse /var/lib/snapd/snaps/snapd_20290.snap /snap/snapd/20290 -o ro,nodev,allow_other,suid
systemd+     140  0.0  0.7  25532 12720 ?        Ss   19:50   0:02 /lib/systemd/systemd-resolved
root         187  0.0  0.1   4304  2696 ?        Ss   19:50   0:01 /usr/sbin/cron -f -P
message+     188  0.0  0.2   8580  4576 ?        Ss   19:50   0:00 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         193  0.0  1.1  30096 19048 ?        Ss   19:50   0:01 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
syslog       194  0.0  0.3 222400  5196 ?        Ssl  19:50   0:00 /usr/sbin/rsyslogd -n -iNONE
root         195  0.5  2.4 1319364 40776 ?       Ssl  19:50   0:50 /usr/lib/snapd/snapd
root         196  0.0  0.4  15324  7264 ?        Ss   19:50   0:02 /lib/systemd/systemd-logind
root         213  0.0  0.2   4780  3324 ?        Ss   19:50   0:00 /bin/bash /snap/ubuntu-desktop-installer/1278/bin/subiquity-server
root         365  0.2  6.1 1762412 102132 ?      Sl   19:50   0:25  \_ /snap/ubuntu-desktop-installer/1278/usr/bin/python3.10 -m subiquity.cmd.server --use-os-prober --storage-version=2 --postinst-hooks-dir=/snap/ubuntu-desktop-installer/1278/etc/subiquity/postinst.d
root         383  0.2  2.2  43096 36508 ?        S    19:50   0:25      \_ python3 /snap/ubuntu-desktop-installer/1278/usr/bin/cloud-init status --wait
root         217  0.0  0.0   3236  1076 hvc0     Ss+  19:50   0:00 /sbin/agetty -o -p -- \u --noclear --keep-baud console 115200,38400,9600 vt220
root         219  0.0  0.0   3192  1080 tty1     Ss+  19:50   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         243  0.0  1.3 107196 21956 ?        Ssl  19:50   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
bekihab+     314  0.0  0.5  16900  8972 ?        Ss   19:50   0:00 /lib/systemd/systemd --user
bekihab+     315  0.0  0.2 103336  3464 ?        S    19:50   0:00  \_ (sd-pam)
BekaHabesha@ubuntu$ 
```

##

## **No. 2. Show your Bash PID** :heavy_check_mark:
* **File:**
  * [**2-show_your_bash_pid**](./2-show_your_bash_pid)
###
* **Using your previous exercise command, Write a** <ins>**Bash script</ins> that displays lines containing the** ${{\color{red}{\textsf{ bash\ \}}}}$ word, **thus allowing you to easily get the <ins>PID</ins> of your Bash process.**
###
* **<ins>Requirements</ins>:**
  * You **cannot use** ${{\color{red}{\textsf{ pgrep\ \}}}}$ 
  * The **third line of your script must be** # ${{\color{red}{\textsf{ shellcheck disable=SC2009\ \}}}}$  (for more info about ignoring (${{\color{red}{\textsf{ shellcheck\ \}}}}$ error [**here**](https://intranet.alxswe.com/rltoken/vErRT8QGU2bwJ6FLvPLzxw))
###
```js
BekaHabesha@ubuntu$ ./2-show_your_bash_pid
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_PID
sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep bash
BekaHabesha@ubuntu$
BekaHabesha@ubuntu$ ./2-show_your_bash_pid
root         213  0.0  0.2   4780  3324 ?        Ss   19:50   0:00 /bin/bash /snap/ubuntu-desktop-installer/1278/bin/subiquity-server
bekihab+     303  0.0  0.3   6212  5240 pts/0    Ss   19:50   0:01 -bash
bekihab+     322  0.0  0.3   6120  5060 pts/1    S+   19:50   0:00 -bash
bekihab+     563  0.0  0.2   4780  3324 pts/0    S+   22:28   0:00 bash ./2-show_your_bash_pid
bekihab+     565  0.0  0.1   4024  2020 pts/0    R+   22:28   0:00 grep bash
```
###
* **Here we can see that my Bash PID is** ${{\color{red}{\textsf{ 4404\ \}}}}$ 

##

## **No. 3. Show your Bash PID made easy** :heavy_check_mark:
* **File:**
  * [**3-show_your_bash_pid_made_easy**](./3-show_your_bash_pid_made_easy)
###
* **Write a** <ins>**Bash script</ins> that displays the <ins>PID</ins>** along with the process name, of processes whose name contain the word ${{\color{red}{\textsf{ bash\ \}}}}$ .
###
* **<ins>Requirements</ins>:**
  * You **cannot use** the ${{\color{red}{\textsf{ ps\ \}}}}$.
###
```js
BekaHabesha@ubuntu$ ./3-show_your_bash_pid_made_easy
322 bash
566 bash
BekaHabesha@ubuntu$ ./3-show_your_bash_pid_made_easy
322 bash
568 bash
BekaHabesha@ubuntu$ 
```
### 
* **<ins>Here we can see that</ins>:**
  * **For the first iteration:** ${{\color{red}{\textsf{ bash\ \}}}}$ **PID** is ${{\color{red}{\textsf{ 4404\ \}}}}$ and that the [**3-show_your_bash_pid_made_easy**](./3-show_your_bash_pid_made_easy) **script PID** is ${{\color{red}{\textsf{ 4555\ \}}}}$ .
  * **For the second iteration:** ${{\color{red}{\textsf{ bash\ \}}}}$ **PID** is (${{\color{red}{\textsf{ 4404\ \}}}}$ and that the [**3-show_your_bash_pid_made_easy**](./3-show_your_bash_pid_made_easy) **script PID** is ${{\color{red}{\textsf{ 4557\ \}}}}$ .

##

## **No. 4. To infinity and beyond**:heavy_check_mark:
* **File:**
  * [**4-to_infinity_and_beyond**](./4-to_infinity_and_beyond)
###
* **Write a** <ins>**Bash script</ins> that displays** ${{\color{red}{\textsf{ To infinity and beyond\ \}}}}$ <ins>**indefinitely</ins>.** 
###
* **<ins>Requirements</ins>:**
  * **In between each iteration of the loop, add a** ${{\color{red}{\textsf{ sleep 2\ \}}}}$
###
```js
BekaHabesha@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
^C
BekaHabesha@ubuntu$ 
```
###
* **Note that I** ${{\color{red}{\textsf{ ctrl+c\ \}}}}$ (killed) the Bash script in the example.

##

## **No. Don't stop me now!** :heavy_check_mark:
* **File:**
  * [**5-dont_stop_me_now**](./5-dont_stop_me_now)
###
* **We stopped our** [**4-to_infinity_and_beyond**](./4-to_infinity_and_beyond) process using ${{\color{red}{\textsf{ ctrl+c\ \}}}}$ in the previous task, there is actually another way to do this.
###
* **Write a** <ins>**Bash script</ins> that stops** [**4-to_infinity_and_beyond**](./4-to_infinity_and_beyond) <ins>**process</ins>.** 
###
* **<ins>Requirements</ins>:**
  * You must **use** ${{\color{red}{\textsf{ kill\ \}}}}$
###
* **Terminal #0**
```js
BekaHabesha@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
BekaHabesha@ubuntu$ 
```
###
* **Terminal #1**
```js
BekaHabesha@ubuntu$ ./5-dont_stop_me_now
BekaHabesha@ubuntu$ 
```
###
* **I opened 2 terminals in this example, started by running my** [**4-to_infinity_and_beyond**](./4-to_infinity_and_beyond) **Bash script in terminal #0 and then moved on terminal #1 to run** [**5-dont_stop_me_now**](./5-dont_stop_me_now) . We can then see in **terminal #0 that my process has been terminated.**
  
##

## **No. 6. Stop me if you can** :heavy_check_mark:
* **File:**
  * [**6-stop_me_if_you_can**](./6-stop_me_if_you_can)
###
* **Write a** <ins>**Bash script</ins> that stops** [**4-to_infinity_and_beyond**](./4-to_infinity_and_beyond)  <ins>**process</ins>.** 
###
* **<ins>Requirements</ins>:**
  * You **cannot use** ${{\color{red}{\textsf{ kill\ \}}}}$ or ${{\color{red}{\textsf{ killall\ \}}}}$
###
* **Terminal #0**
```js
BekaHabesha@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
BekaHabesha@ubuntu$ 
```
###
* **Terminal #1**
```js
BekaHabesha@ubuntu$ ./6-stop_me_if_you_can
BekaHabesha@ubuntu$ 
```
###
* **I opened 2 terminals in this example, started by running my** [**4-to_infinity_and_beyond**](./4-to_infinity_and_beyond) **Bash script in terminal #0 and then moved on terminal #1 to run** [**6-stop_me_if_you_can**](./6-stop_me_if_you_can) . We can then see in **terminal #0 that my process has been terminated.**

## 

## **No. 7. Highlander**:heavy_check_mark:
* **File:**
  * [**7-highlander**](./7-highlander)
###
* **Write a** <ins>**Bash script</ins> that displays:**
  * ${{\color{red}{\textsf{ To infinity and beyond\ \}}}}$ *indefinitely*
  * With a ${{\color{red}{\textsf{ sleep 2\ \}}}}$ *in between each iteration* 
  * ${{\color{red}{\textsf{ I am invincible!!!\ \}}}}$ when receiving a ${{\color{red}{\textsf{ SIGTERM\ \}}}}$ signal
###
* **Make a copy of your** [**6-stop_me_if_you_can**](./6-stop_me_if_you_can) **script, name it** [**67-stop_me_if_you_can**](./67-stop_me_if_you_can) , that kills the [**7-highlander**](./7-highlander) process instead of the [**4-to_infinity_and_beyond**](./4-to_infinity_and_beyond) one.
####
* **Terminal #0**
```js
BekaHabesha@ubuntu$ ./7-highlander
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
^C
BekaHabesha@ubuntu$ 
```
###
* **Terminal #1**
```js
BekaHabesha@ubuntu$ ./67-stop_me_if_you_can
BekaHabesha@ubuntu$ ./67-stop_me_if_you_can 
BekaHabesha@ubuntu$ ./67-stop_me_if_you_can 
BekaHabesha@ubuntu$ 
```
###
* **I started** [**7-highlander**](./7-highlander) **in terminal #0 and then run** [**67-stop_me_if_you_can**](./67-stop_me_if_you_can) **in terminal #1 , for every iteration we can see** ${{\color{red}{\textsf{ I am invincible!!!\ \}}}}$ **appearing in terminal #0.**

##

## **No. 8. Beheaded process** :heavy_check_mark:
* **File:**
  * [**8-beheaded_process**](./8-beheaded_process)
###
* **Write a** <ins>**Bash script</ins> that kills the process** [**7-highlander**](./7-highlander) .
###
* **Terminal #0**
```js
BekaHabesha@ubuntu$ ./7-highlander 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Killed
BekaHabesha@ubuntu$ 
```
###
* **Terminal #1**
```js
BekaHabesha@ubuntu$ ./8-beheaded_process
BekaHabesha@ubuntu$ 
```
###
* **I started** [**7-highlander**](./7-highlander) **in terminal #0 and then run** [**8-beheaded_process**](./8-beheaded_process) **in terminal #1 , for every iteration we can see that the** [**7-highlander**](./7-highlander) **has been killed.**

#

<h1 align="center">ADVANCED_TASKS (From Task 9 to 11) :cd:</h1>

## **No. 9. Process and PID file** :heavy_check_mark:
* **File:**
  * [**100-process_and_pid_file**](./100-process_and_pid_file)
###
* **Write a** <ins>**Bash script</ins> that:**
  * **Creates the file** $\mathcal{\color{red}{/var/run/myscript.pid}}$ **containing its <ins>PID</ins> .**
  * **Displays** ${{\color{red}{\textsf{ To infinity and beyond\ \}}}}$ **indefinitely .**
  * **Displays** ${{\color{red}{\textsf{ I hate the kill command\ \}}}}$ **when receiving a <ins>SIGTERM signal</ins> .**
  * **Displays** ${{\color{red}{\textsf{ Y U no love me?!\ \}}}}$ **when receiving a <ins>SIGINT signal</ins> .**
  * **Deletes the file** $\mathcal{\color{red}{/var/run/myscript.pid}}$ and **terminates itself when receiving a <ins>SIGQUIT</ins> or <ins>SIGTERM signal</ins> .**

<p align="center">
  <img src="https://i.ibb.co/HFQCs3t/for-no-9.jpg" />
</p>

###
```js
BekaHabesha@ubuntu$ sudo ./100-process_and_pid_file
To infinity and beyond
To infinity and beyond
^CY U no love me?!
BekaHabesha@ubuntu$ 
```
###
* **<ins>Executing</ins>** the [**100-process_and_pid_file**](./100-process_and_pid_file) **<ins>script</ins> and <ins>killing</ins> it with** ${{\color{red}{\textsf{ ctrl+c\ \}}}}$ **.**
###
* **Terminal #0**
```js
BekaHabesha@ubuntu$ sudo ./100-process_and_pid_file
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
I hate the kill command
BekaHabesha@ubuntu$ 
```
###
* **Terminal #1**
```js
BekaHabesha@ubuntu$ sudo pkill -f 100-process_and_pid_file
BekaHabesha@ubuntu$ 
```
###
* **Starting** [**100-process_and_pid_file**](./100-process_and_pid_file) **in the terminal #0 and then killing it in the terminal #1.**

##

## **No. 10. Manage my process** :heavy_check_mark:
* **File:**
  * [**101-manage_my_process**](./101-manage_my_process) ,
  * [**manage_my_process**](./manage_my_process)

<p align="center">
  <img src="https://i.ibb.co/kyjshWF/for-no-10.jpg" />
</p>

###
* **<ins>Read</ins>:**
  * [**&**](https://intranet.alxswe.com/rltoken/R4YSgPT1k0PhWCrB0TYzoQ)
  * [**init.d**](https://intranet.alxswe.com/rltoken/sVqN4oNYYO6ojS4ctT02Jw)
  * [**Daemon**](https://intranet.alxswe.com/rltoken/kCoQ5aYO3towdDQFVPcfNg)
  * [**Positional parameters**](https://intranet.alxswe.com/rltoken/TJ2rxUwRsnM1mJQHSCnOQA)
###
* **<ins>man</ins>:** ${{\color{red}{\textsf{ sudo\ \}}}}$
###
<ins>**Programs</ins> that are detached from the <ins>terminal</ins> and <ins>running in the background</ins> are called <ins>daemons</ins> or <ins>processes</ins>,** need to be managed. **The general <ins>minimum set of instructions</ins> is:** ${{\color{red}{\textsf{ start\ \}}}}$ **,** ${{\color{red}{\textsf{ restart\ \}}}}$ **and** ${{\color{red}{\textsf{ stop\ \}}}}$ **.** The **<ins>most popular</ins> way of doing so on <ins>Unix system</ins> is to use the <ins>init scripts</ins>.**
###
* **Write a** [**manage_my_process**](./manage_my_process) <ins>**Bash script</ins> that:**
  * **Indefinitely Writes** ${{\color{red}{\textsf{ I am alive!\ \}}}}$ **to the file** $\mathcal{\color{red}{/tmp/my(_)process}}$
  * **In between every** ${{\color{red}{\textsf{ I am alive!\ \}}}}$ **message, the program should <ins>pause</ins> for <ins>2 seconds</ins>.**
###
* **Write** <ins>**Bash (init) script</ins>** [**101-manage_my_process**](./101-manage_my_process) **that <ins>manages</ins>** [**manage_my_process**](./manage_my_process) . (both files need to be pushed to git)
###
* **<ins>Requirements</ins>:**
  * **When <ins>passing the argument</ins>** ${{\color{red}{\textsf{ start\ \}}}}$ **:** 
    * **Starts** [**manage_my_process**](./manage_my_process) **.**
    * **Creates a file containing its PID in** $\mathcal{\color{red}{/var/run/}}$[**my_process**](./manage_my_process)${{\color{red}{\textsf{ .pid\ \}}}}$ **.** 
    * **Displays** [**manage_my_process**](./manage_my_process) ${{\color{red}{\textsf{ started\ \}}}}$ **.**
  * **When <ins>passing the argument</ins>** ${{\color{red}{\textsf{ stop\ \}}}}$ **:** 
    * **Stops** [**manage_my_process**](./manage_my_process) **.**
    * **Deletes the file** $\mathcal{\color{red}{/var/run/}}$[**my_process**](./manage_my_process)${{\color{red}{\textsf{ .pid\ \}}}}$ **.** 
    * **Displays** [**manage_my_process**](./manage_my_process) ${{\color{red}{\textsf{ stoped\ \}}}}$ **.**
  * **When <ins>passing the argument</ins>** ${{\color{red}{\textsf{ restart\ \}}}}$ **:** 
    * **Stops** [**manage_my_process**](./manage_my_process) **.**
    * **Deletes the file** $\mathcal{\color{red}{/var/run/}}$[**my_process**](./manage_my_process)${{\color{red}{\textsf{ .pid\ \}}}}$ **.** 
    * **Starts** [**manage_my_process**](./manage_my_process) **.**
    * **Creates a file containing its PID in** $\mathcal{\color{red}{/var/run/}}$[**my_process**](./manage_my_process)${{\color{red}{\textsf{ .pid\ \}}}}$ **.** 
    * **Displays** [**manage_my_process**](./manage_my_process) ${{\color{red}{\textsf{ restarted\ \}}}}$ **.**
  * **<ins>Displays</ins>** ${{\color{red}{\textsf{ start\ \}}}}$ **:** 
    * **Starts** [**manage_my_process**](./manage_my_process) **.**
    * **Creates a file containing its PID in**$\mathcal{\color{red}{/var/run/}}$[**my_process**](./manage_my_process)${{\color{red}{\textsf{ .pid\ \}}}}$ **.** 
    * **Displays** ${{\color{red}{\textsf{ Usage:\ \}}}}$ [**my_process**](./manage_my_process) [**{start|stop|restart}**](./manage_my_process), **if any other argument or no argument is passed.**
###
**Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing [**./101-manage_my_process start**](./101-manage_my_process start) , in our case it will simply create a new process instead of saying that it is already started.**
###
```js
BekaHabesha@ubuntu$ ./101-manage_my_process
Usage: manage_my_process {start|stop|restart}
BekaHabesha@ubuntu$ ./101-manage_my_process start
manage_my_process started
BekaHabesha@ubuntu$ tail -f -n0 /tmp/my_process 
I am alive!
I am alive!
I am alive!
I am alive!
^C
BekaHabesha@ubuntu$ sudo ./101-manage_my_process stop
manage_my_process stopped
BekaHabesha@ubuntu$ cat /var/run/my_process.pid 
cat: /var/run/my_process.pid: No such file or directory
BekaHabesha@ubuntu$ tail -f -n0 /tmp/my_process 
^C
BekaHabesha@ubuntu$ sudo ./101-manage_my_process start
manage_my_process started
BekaHabesha@ubuntu$ cat /var/run/my_process.pid 
11864
BekaHabesha@ubuntu$ ./101-manage_my_process restart
manage_my_process restarted
BekaHabesha@ubuntu$ cat /var/run/my_process.pid 
11918
BekaHabesha@ubuntu$ tail -f -n0 /tmp/my_process 
I am alive!
I am alive!
I am alive!
^C
BekaHabesha@ubuntu$ 
```

##

## **No. 11. Zombie** :heavy_check_mark:
* **File:**
  * [**102-zombie.c**](./102-zombie.c)

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/255/C6mO7b3.jpg" />
</p>

###
* **<ins>Read</ins>:** [**what a zombie process is.**](https://intranet.alxswe.com/rltoken/Tb86ZoSxR6ORCKYlZaYzHw)
###
* **Write a** <ins>**C program</ins> that creates <ins>5 zombie processes<ins>.**
###
* **<ins>Requirements</ins>:**
  * **For every <ins>zombie processes<ins> created, it displays** the ${{\color{red}{\textsf{ Zombie process created, PID:\ \}}}}$ [**ZOMBIE_PID**](./102-zombie.c) 
  * **Your code should use the <ins>Betty style<ins>. It will be checked using** ${{\color{red}{\textsf{ betty-style.pl\ \}}}}$ and ${{\color{red}{\textsf{ betty-doc.pl\ \}}}}$ **.**
  * **When your code is done creating the <ins>parent process<ins> and the <ins>zombies<ins>, use the function bellow**
###
```js
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
```
###
* **<ins>Example</ins>:**
###
* **Terminal #0**
```js
BekaHabesha@ubuntu$ gcc 102-zombie.c -o zombie
BekaHabesha@ubuntu$ ./zombie 
Zombie process created, PID: 938
Zombie process created, PID: 939
Zombie process created, PID: 941
Zombie process created, PID: 942
Zombie process created, PID: 944
^C
BekaHabesha@ubuntu$ 
```
###
* **Terminal #1**
```js
BekaHabesha@ubuntu$ ps aux | grep -e 'Z+.*<defunct>'
bekihab+     920  0.0  0.0      0     0 pts/2    Z+   22:44   0:00 [zombie] <defunct>
bekihab+     922  0.0  0.0      0     0 pts/2    Z+   22:44   0:00 [zombie] <defunct>
bekihab+     923  0.0  0.0      0     0 pts/2    Z+   22:44   0:00 [zombie] <defunct>
bekihab+     925  0.0  0.0      0     0 pts/2    Z+   22:44   0:00 [zombie] <defunct>
bekihab+     926  0.0  0.0      0     0 pts/2    Z+   22:44   0:00 [zombie] <defunct>
bekihab+    1036  0.0  0.0      0     0 pts/4    Z+   22:47   0:00 [zombie] <defunct>
bekihab+    1037  0.0  0.0      0     0 pts/4    Z+   22:47   0:00 [zombie] <defunct>
bekihab+    1039  0.0  0.0      0     0 pts/4    Z+   22:47   0:00 [zombie] <defunct>
bekihab+    1040  0.0  0.0      0     0 pts/4    Z+   22:47   0:00 [zombie] <defunct>
bekihab+    1042  0.0  0.0      0     0 pts/4    Z+   22:47   0:00 [zombie] <defunct>
bekihab+    1048  0.0  0.1   4032  2088 pts/5    S+   22:47   0:00 grep --color=auto -e Z+.*<defunct>
BekaHabesha@ubuntu$ 
```
###
* **In Terminal #0, I start by compiling** ${{\color{red}{\textsf{ 102-zombie.c\ \}}}}$ and **executing** ${{\color{red}{\textsf{ zombie\ \}}}}$ **which creates <ins>5 zombie processes</ins>. In Terminal #1, I display the list of <ins>processes</ins> and look for <ins>lines containing</ins>** [**Z+.* <defunct>**](./102-zombie.c) **which catches <ins>zombie process</ins>.**

##
