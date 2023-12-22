<H1 align="center", height="1500"> <ins> README.md File </ins> </H1>
<H1 align="center"> <ins>  0x05. Processes and signals README.md</ins> </H1>

<p align="center">
  <img src="https://i.ibb.co/VQrnvVN/0x05-Processes-and-signals-Alx-logo.png" />
</p>

##

* **File_name:** [**README.md file**](https://github.com/BekaHabesha/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/README.md)
* **Created:** <ins>**On December 22, 2023**</ins>
* **Author:** [***Bereket Dereje Mekkonen***](https://intranet.alxswe.com/users/BereketDerejeMekonnen)
* **Project:** [**0x05. Processes and signals**](https://intranet.alxswe.com/projects/255)
* **GitHub repository:** 📂 [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops)
* **Directory:** 📂 [**0x05-processes_and_signals**](https://github.com/BekaHabesha/alx-system_engineering-devops/tree/master/0x05-processes_and_signals)
* **Project Tasks:** <ins>**Mandatory and Advanced**</ins>
* **Tasks in number:** <ins>**12 Tasks (9-Mandatory & 3-Advanced)**</ins>
* **Mandatory_Tasks:** <ins>**From Task 0 to 8**</ins>
* **Advanced_Tasks:** <ins>**From Task 9 to 11**</ins>

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

<h1> <ins>Background Context</ins> :floppy_disk:</H1>

<p align="center">
  <img src="https://i0.wp.com/techieroop.com/wp-content/uploads/2019/06/run-bash-script-in-parallel.png?fit=%2C&ssl=1" />
</p>

<h1> <ins>Resources</ins> :floppy_disk:</H1>

### **Read or watch:** :heavy_check_mark:
* [**Linux PID**](https://intranet.alxswe.com/rltoken/qVGxUt1QMIV4B4oVrQBlQg)
* [**Linux process**](https://intranet.alxswe.com/rltoken/px2TdWSjVO8i9SB5gHchAw)
* [**Linux signal**](https://intranet.alxswe.com/rltoken/qQSGz9CN52PVF3IPCuaRiw)
* [**Process management in linux**](https://intranet.alxswe.com/rltoken/XlYrlghzNZ6Z1cbI_IPaiA)

### **man or help:** :heavy_check_mark:
* ${{\color{red}{\textsf{ ps\ \}}}}$
* $\mathscr{\color{red}{pgrep}}$
* ${{\color{red}{\textsf{ pkill\ \}}}}$
* $\mathscr{\color{red}{kill}}$
* ${{\color{red}{\textsf{ exit\ \}}}}$
* $\mathscr{\color{red}{trap}}$


<p align="center">
  <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fphoenixnap.com%2Fkb%2Fbash-for-loop&psig=AOvVaw3GxvZNLKKiOIU-vbrqcMc1&ust=1703280084542000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMDJrve6oYMDFQAAAAAdAAAAABAR" />
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
  <img src="https://phoenixnap.com/kb/wp-content/uploads/2021/12/indices.sh-for-loop-script.png" />
  <img src="https://static.javatpoint.com/tutorial/bash/images/bash-for-loop-output2.png" />
</p>

###

<H2> <ins>Copyright - Plagiarism</ins> :heavy_check_mark:</H2>

* You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
* You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
* You are not allowed to publish any content of this project.
* Any form of plagiarism is strictly forbidden and will result in removal from the program.

<p align="center">
  <img src="https://phoenixnap.com/kb/wp-content/uploads/2021/12/bash-case-shows-file-types.png" />
  <img src="https://linuxhint.com/wp-content/uploads/2022/03/word-image-922.png" />
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
  <img src="https://ciracollege.com/wp-content/uploads/2020/11/How-to-Learn-Python.jpg" />
</p>

##

<H1><ins>More Info</ins> :floppy_disk:</H1>

For those who want to know more and learn about all signals, check out [**this article**](https://intranet.alxswe.com/rltoken/BOU-KVNMqfKEIBo_VOI26A).

<p align="center">
  <img src="https://ciracollege.com/wp-content/uploads/2020/11/How-to-Learn-Python.jpg" />
</p>

##

## <ins>**PROJECT_TITLE</ins>:**   [**0x05. Processes and signals**](https://intranet.alxswe.com/projects/255)

## <ins>**GITHUB_REPOSITORY</ins>: 📂**    [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops)

## <ins>**DIRECTORY</ins>: 📂**   [**0x05-processes_and_signals**](https://github.com/BekaHabesha/alx-system_engineering-devops/tree/master/0x05-processes_and_signals)

##
* **File_name:** [**README.md file**](https://github.com/BekaHabesha/alx-system_engineering-devops/blob/master/0x05-processes_and_signals/README.md)
* **Created:** <ins>**On December 22, 2023**</ins>
* **Author:** [***Bereket Dereje Mekkonen***](https://intranet.alxswe.com/users/BereketDerejeMekonnen)
* **Project:** [**0x05. Processes and signals**](https://intranet.alxswe.com/projects/255)
* **GitHub repository:** 📂 [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops)
* **Directory:** 📂 [**0x05-processes_and_signals**](https://github.com/BekaHabesha/alx-system_engineering-devops/tree/master/0x05-processes_and_signals)
* **Project Tasks:** <ins>**Mandatory and Advanced**</ins>
* **Tasks in number:** <ins>**12 Tasks (9-Mandatory & 3-Advanced)**</ins>
* **Mandatory_Tasks:** <ins>**From Task 0 to 8**</ins>
* **Advanced_Tasks:** <ins>**From Task 9 to 11**</ins>

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
* **Write a <ins>**Bash script</ins> that displays** its <ins>**own PID</ins>.**

```js
BekaHabesha@ubuntu$ ./0-what-is-my-pid
4120
BekaHabesha@ubuntu$ 
```

##

## **No. 1. List your processes**:heavy_check_mark:
* **File:**
  * [**1-list_your_processes**](./1-list_your_processes)
###
* **Write a <ins>**Bash script</ins> that displays** a list of <ins>**currently running processes</ins>.**

* **<ins>Requirements</ins>:**
  * Must show all processes, for all users, including those which might not have a TTY
  * Display in a user-oriented format
  * Show process hierarchy

```js
BekaHabesha@ubuntu$ ./1-list_your_processes | head -50
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ksoftirqd/0]
root         4  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/0:0]
root         5  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/0:0H]
root         7  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [rcu_sched]
root         8  0.0  0.0      0     0 ?        S    Feb13   0:03  \_ [rcuos/0]
root         9  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcuob/0]
root        11  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [migration/0]
root        12  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [watchdog/0]
root        13  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [khelper]
root        14  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kdevtmpfs]
root        15  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [netns]
root        16  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [writeback]
root        17  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kintegrityd]
root        18  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [bioset]
root        19  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/u3:0]
root        20  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kblockd]
root        21  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [ata_sff]
root        22  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khubd]
root        23  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [md]
root        24  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [devfreq_wq]
root        25  0.0  0.0      0     0 ?        S    Feb13   0:41  \_ [kworker/0:1]
root        27  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khungtaskd]
root        28  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kswapd0]
root        29  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [vmstat]
root        30  0.0  0.0      0     0 ?        SN   Feb13   0:00  \_ [ksmd]
root        31  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [fsnotify_mark]
root        32  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ecryptfs-kthrea]
root        33  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [crypto]
root        45  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kthrotld]
root        46  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:1]
root        65  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [deferwq]
root        66  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [charger_manager]
root       108  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kpsmoused]
root       125  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [scsi_eh_0]
root       126  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:2]
root       172  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [jbd2/sda1-8]
root       173  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [ext4-rsv-conver]
root       409  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [iprt]
root       549  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [kworker/u3:1]
root       808  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kauditd]
root       834  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [rpciod]
root       846  0.0  0.0      0     0 ?        S<   Feb13   0:00  \_ [nfsiod]
root         1  0.0  0.4  33608  2168 ?        Ss   Feb13   0:00 /sbin/init
root       373  0.0  0.0  19472   408 ?        S    Feb13   0:00 upstart-udev-bridge --daemon
root       378  0.0  0.2  49904  1088 ?        Ss   Feb13   0:00 /lib/systemd/systemd-udevd --daemon
root       518  0.0  0.1  23416   644 ?        Ss   Feb13   0:00 rpcbind
statd      547  0.0  0.1  21536   852 ?        Ss   Feb13   0:00 rpc.statd -L
BekaHabesha@ubuntu$ 
```

##

## **No. 2. Show your Bash PID** :heavy_check_mark:
* **File:**
  * [**2-show_your_bash_pid**](./2-show_your_bash_pid)
###
* **Using your previous exercise command, Write a <ins>**Bash script</ins> that displays lines containing the** ${{\color{red}{\textsf{ bash\ \}}}}$ word, **thus allowing you to easily get the <ins>PID</ins> of your Bash process.**

* **<ins>Requirements</ins>:**
  * You **cannot use** ${{\color{red}{\textsf{ pgrep\ \}}}}$ 
  * The **third line of your script must be** # ${{\color{red}{\textsf{ shellcheck disable=SC2009\ \}}}}$  (for more info about ignoring (${{\color{red}{\textsf{ shellcheck\ \}}}}$ error [**here**](https://intranet.alxswe.com/rltoken/vErRT8QGU2bwJ6FLvPLzxw))

```js
BekaHabesha@ubuntu$ ./2-show_your_bash_pid
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_PID
sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep bash
BekaHabesha@ubuntu$ 
```
* **Here we can see that my Bash PID is** ${{\color{red}{\textsf{ 4404\ \}}}}$ 

##

## **No. 3. Show your Bash PID made easy** :heavy_check_mark:
* **File:**
  * [**3-show_your_bash_pid_made_easy**](./3-show_your_bash_pid_made_easy)
###
* **Write a <ins>**Bash script</ins> that displays the <ins>PID</ins>** along with the process name, of processes whose name contain the word ${{\color{red}{\textsf{ bash\ \}}}}$ .

* **<ins>Requirements</ins>:**
  * You **cannot use** the ${{\color{red}{\textsf{ ps\ \}}}}$.

```js
BekaHabesha@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4555 bash
BekaHabesha@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4557 bash
BekaHabesha@ubuntu$ 
```

* **<ins>Here we can see that</ins>:**
  * **For the first iteration:** the ${{\color{red}{\textsf{ bash\ \}}}}$ **PID** is (${{\color{red}{\textsf{ 4404\ \}}}}$ and that the ${{\color{red}{\textsf{ 3-show_your_bash_pid_made_easy\ \}}}}$ **script PID** is ${{\color{red}{\textsf{ 4555\ \}}}}$ .
  * **For the second iteration:** the ${{\color{red}{\textsf{ bash\ \}}}}$ **PID** is (${{\color{red}{\textsf{ 4404\ \}}}}$ and that the ${{\color{red}{\textsf{ 3-show_your_bash_pid_made_easy\ \}}}}$ **script PID** is ${{\color{red}{\textsf{ 4557\ \}}}}$ .

##

## **No. 4. To infinity and beyond**:heavy_check_mark:
* **File:**
  * [**4-to_infinity_and_beyond**](./4-to_infinity_and_beyond)
###
* **Write a <ins>**Bash script</ins> that displays** ${{\color{red}{\textsf{ To infinity and beyond\ \}}}}$ <ins>**indefinitely</ins>.** 

* **<ins>Requirements</ins>:**
  * You must **use** the ${{\color{red}{\textsf{ while\ \}}}}$ **loop** (${{\color{red}{\textsf{ for\ \}}}}$ and ${{\color{red}{\textsf{ until\ \}}}}$ are forbidden)
  * In between **each iteration of the loop,** add a ${{\color{red}{\textsf{ sleep 2\ \}}}}$ **.**

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
* **Note that I** ${{\color{red}{\textsf{ ctrl+c\ \}}}}$ (killed) the Bash script in the example.

##

## **No. Don't stop me now!** :heavy_check_mark:
* **File:**
  * [**5-dont_stop_me_now**](./5-dont_stop_me_now)
###
* **We stopped our** ${{\color{red}{\textsf{ 4-to_infinity_and_beyond\ \}}}}$ process using ${{\color{red}{\textsf{ ctrl+c\ \}}}}$ in the previous task, there is actually another way to do this.

* **Write a <ins>**Bash script</ins> that stops** ${{\color{red}{\textsf{ 4-to_infinity_and_beyond\ \}}}}$ <ins>**process</ins>.** 

* **<ins>Requirements</ins>:**
  * You must **use** ${{\color{red}{\textsf{ kill\ \}}}}$

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

* **Terminal #1**
```js
BekaHabesha@ubuntu$ ./5-dont_stop_me_now
BekaHabesha@ubuntu$ 
```

* **I opened 2 terminals in this example, started by running my** ${{\color{red}{\textsf{ 4-to_infinity_and_beyond\ \}}}}$ **Bash script in terminal #0 and then moved on terminal #1 to run** ${{\color{red}{\textsf{ 5-dont_stop_me_now\ \}}}}$ . We can then see in terminal #0 that my process has been terminated.
  
##

## **No. 6. Stop me if you can** :heavy_check_mark:
* **File:**
  * [**6-stop_me_if_you_can**](./6-stop_me_if_you_can)
###
* **Write a <ins>**Bash script</ins> that stops** ${{\color{red}{\textsf{ 4-to_infinity_and_beyond\ \}}}}$ <ins>**process</ins>.** 

* **<ins>Requirements</ins>:**
  * You **cannot use** ${{\color{red}{\textsf{ kill\ \}}}}$ or ${{\color{red}{\textsf{ killall\ \}}}}$

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

* **Terminal #1**
```js
BekaHabesha@ubuntu$ ./6-stop_me_if_you_can
BekaHabesha@ubuntu$ 
```

* **I opened 2 terminals in this example, started by running my** ${{\color{red}{\textsf{ 4-to_infinity_and_beyond\ \}}}}$ **Bash script in terminal #0 and then moved on terminal #1 to run** ${{\color{red}{\textsf{ 6-stop_me_if_you_can\ \}}}}$ . We can then see in terminal #0 that my process has been terminated.


##

## **No. 7. Highlander**:heavy_check_mark:
* **File:**
  * [**7-highlander**](./7-highlander)
###
* **Write a <ins>**Bash script</ins> that displays:**
  * ${{\color{red}{\textsf{ To infinity and beyond\ \}}}}$ *indefinitely*
  * With a ${{\color{red}{\textsf{ sleep 2\ \}}}}$ *in between each iteration* 

  * ${{\color{red}{\textsf{ I am invincible!!!\ \}}}}$ when receiving a ${{\color{red}{\textsf{ SIGTERM\ \}}}}$ signal

* **Make a copy of your** ${{\color{red}{\textsf{ 6-stop_me_if_you_can\ \}}}}$ **script, name it** (${{\color{red}{\textsf{ 67-stop_me_if_you_can\ \}}}}$, that kills the ${{\color{red}{\textsf{ 7-highlander\ \}}}}$ process instead of the ${{\color{red}{\textsf{ 4-to_infinity_and_beyond\ \}}}}$ one.

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

* **Terminal #1**
```js
BekaHabesha@ubuntu$ ./67-stop_me_if_you_can
BekaHabesha@ubuntu$ ./67-stop_me_if_you_can 
BekaHabesha@ubuntu$ ./67-stop_me_if_you_can 
BekaHabesha@ubuntu$ 
```

* **I started** ${{\color{red}{\textsf{ 7-highlander\ \}}}}$ **in terminal #0 and then run** ${{\color{red}{\textsf{ 67-stop_me_if_you_can\ \}}}}$ **in terminal #1 , for every iteration we can see** ${{\color{red}{\textsf{ I am invincible!!!\ \}}}}$ appearing in terminal #0.

##

## **No. 8. Beheaded process** :heavy_check_mark:
* **File:**
  * [**8-beheaded_process**](./8-beheaded_process)
###
* **Write a <ins>**Bash script</ins> that kills the process** ${{\color{red}{\textsf{ 7-highlander\ \}}}}$ .

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

* **Terminal #1**
```js
BekaHabesha@ubuntu$ ./8-beheaded_process
BekaHabesha@ubuntu$ 
```

* **I started** ${{\color{red}{\textsf{ 7-highlander\ \}}}}$ **in terminal #0 and then run** ${{\color{red}{\textsf{ 8-beheaded_process\ \}}}}$ **in terminal #1 , for every iteration we can see that the** ${{\color{red}{\textsf{ 7-highlander\ \}}}}$ has been killed.

##

## **No. 9. To file, or not to file** :heavy_check_mark:
* **File:**
  * [**9-to_file_or_not_to_file **](./9-to_file_or_not_to_file)
###
* **Write a <ins>**Bash script</ins> that displays numbers from 1 to 20 and:**
  * displays ${{\color{red}{\textsf{ 4\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from China\ \}}}}$ for the 4th loop iteration
  * displays ${{\color{red}{\textsf{ 9\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Japan\ \}}}}$ for the 9th loop iteration
  * displays ${{\color{red}{\textsf{ 17\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Italy\ \}}}}$ for the 17th loop iteration

* **<ins>Requirements</ins>:**
  * You must **use** the ${{\color{red}{\textsf{ while\ \}}}}$ **loop** (${{\color{red}{\textsf{ for\ \}}}}$ and ${{\color{red}{\textsf{ until\ \}}}}$ are forbidden)
  * You must **use** the ${{\color{red}{\textsf{ case\ \}}}}$ **statements**

```js
BekaHabesha@ubuntu$ file school
school: cannot open `school' (No such file or directory)
BekaHabesha@ubuntu$ ./9-to_file_or_not_to_file 
school file does not exist
sylvain@ubuntu$ touch school
BekaHabesha@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is empty
school is a regular file
BekaHabesha@ubuntu$ echo 'betty' > school 
BekaHabesha@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is not empty
school is a regular file
BekaHabesha@ubuntu$ rm school
BekaHabesha@ubuntu$ mkdir school
BekaHabesha@ubuntu$ ./9-to_file_or_not_to_file 
school file exists
school file is not empty
BekaHabesha@ubuntu$ 
```

##

## **No. 10. FizzBuzz** :heavy_check_mark:
* **File:**
  * [**10-fizzbuzz**](./10-fizzbuzz)
###
* **Write a <ins>**Bash script</ins> that displays numbers from 1 to 20 and:**
  * displays ${{\color{red}{\textsf{ 4\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from China\ \}}}}$ for the 4th loop iteration
  * displays ${{\color{red}{\textsf{ 9\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Japan\ \}}}}$ for the 9th loop iteration
  * displays ${{\color{red}{\textsf{ 17\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Italy\ \}}}}$ for the 17th loop iteration

* **<ins>Requirements</ins>:**
  * You must **use** the ${{\color{red}{\textsf{ while\ \}}}}$ **loop** (${{\color{red}{\textsf{ for\ \}}}}$ and ${{\color{red}{\textsf{ until\ \}}}}$ are forbidden)
  * You must **use** the ${{\color{red}{\textsf{ case\ \}}}}$ **statements**

```js
BekaHabesha@ubuntu$ ./10-fizzbuzz | head -20
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
BekaHabesha@ubuntu$ 
```

#

<h1 align="center">ADVANCED_TASKS (From Task 20 to 21) :cd:</h1>

## **No. Read and cut** :heavy_check_mark:
* **File:**
  * [**100-read_and_cut**](./100-read_and_cut)
###
* **Write a <ins>**Bash script</ins> that displays numbers from 1 to 20 and:**
  * displays ${{\color{red}{\textsf{ 4\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from China\ \}}}}$ for the 4th loop iteration
  * displays ${{\color{red}{\textsf{ 9\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Japan\ \}}}}$ for the 9th loop iteration
  * displays ${{\color{red}{\textsf{ 17\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Italy\ \}}}}$ for the 17th loop iteration

* **<ins>Requirements</ins>:**
  * You must **use** the ${{\color{red}{\textsf{ while\ \}}}}$ **loop** (${{\color{red}{\textsf{ for\ \}}}}$ and ${{\color{red}{\textsf{ until\ \}}}}$ are forbidden)
  * You must **use** the ${{\color{red}{\textsf{ case\ \}}}}$ **statements**

```js
BekaHabesha@ubuntu$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:106::/var/run/dbus:/bin/false
landscape:x:103:109::/var/lib/landscape:/bin/false
sshd:x:104:65534::/var/run/sshd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
vagrant:x:1000:1000::/home/vagrant:/bin/bash
colord:x:106:112:colord colour management daemon,,,:/var/lib/colord:/bin/false
statd:x:107:65534::/var/lib/nfs:/bin/false
sylvain:98:99:Sylvain:/home/sylvain:/bin/bash
puppet:x:108:114:Puppet configuration management daemon,,,:/var/lib/puppet:/bin/false
ubuntu:x:1001:1001:Ubuntu:/home/ubuntu:/bin/bash
BekaHabesha@ubuntu$ ./100-read_and_cut
root:0:/root
daemon:1:/usr/sbin
bin:2:/bin
sys:3:/dev
sync:4:/bin
games:5:/usr/games
man:6:/var/cache/man
lp:7:/var/spool/lpd
mail:8:/var/mail
news:9:/var/spool/news
uucp:10:/var/spool/uucp
proxy:13:/bin
www-data:33:/var/www
backup:34:/var/backups
list:38:/var/list
irc:39:/var/run/ircd
gnats:41:/var/lib/gnats
nobody:65534:/nonexistent
libuuid:100:/var/lib/libuuid
syslog:101:/home/syslog
messagebus:102:/var/run/dbus
landscape:103:/var/lib/landscape
sshd:104:/var/run/sshd
pollinate:105:/var/cache/pollinate
vagrant:1000:/home/vagrant
colord:106:/var/lib/colord
statd:107:/var/lib/nfs
sylvain:99:/bin/bash
puppet:108:/var/lib/puppet
ubuntu:1001:/home/ubuntu
BekaHabesha@ubuntu$ 
```

##

## **No. 12. Tell the story of passwd** :heavy_check_mark:
* **File:**
  * [**101-tell_the_story_of_passwd**](./101-tell_the_story_of_passwd)

<p align="center">
  <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/03ca27392c6338e696fc0c3b08765f02c98457a1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231221%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231221T184919Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ce35c70b75b1be3c6a5dbeb3d0114714124cdac045ec9ca9c9cf40ba79ca8938" />
</p>


###
* **Write a <ins>**Bash script</ins> that displays numbers from 1 to 20 and:**
  * displays ${{\color{red}{\textsf{ 4\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from China\ \}}}}$ for the 4th loop iteration
  * displays ${{\color{red}{\textsf{ 9\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Japan\ \}}}}$ for the 9th loop iteration
  * displays ${{\color{red}{\textsf{ 17\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Italy\ \}}}}$ for the 17th loop iteration

* **<ins>Requirements</ins>:**
  * You must **use** the ${{\color{red}{\textsf{ while\ \}}}}$ **loop** (${{\color{red}{\textsf{ for\ \}}}}$ and ${{\color{red}{\textsf{ until\ \}}}}$ are forbidden)
  * You must **use** the ${{\color{red}{\textsf{ case\ \}}}}$ **statements**

```js
BekaHabesha@ubuntu$ ls
100-read_and_cut              1-for_best_school         6-superstitious_numbers
101-tell_the_story_of_passwd  2-while_best_school       7-clock
102-lets_parse_apache_logs    3-until_best_school       8-for_ls
103-dig_the-data              4-if_9_say_hi                  9-to_file_or_not_to_file
10-fizzbuzz                   5-4_bad_luck_8_is_your_chance
BekaHabesha@ubuntu$ ./8-for_ls
read_and_cut
tell_the_story_of_passwd
lets_parse_apache_logs
dig_the-data
fizzbuzz
for_best_school
while_best_school
until_best_school
if_9_say_hi
4_bad_luck_8_is_your_chance
superstitious_numbers
clock
for_ls
to_file_or_not_to_file
BekaHabesha@ubuntu$ 
```

##

## **No. 13. Let's parse Apache logs**: heavy_check_mark:
* **File:**
  * [**102-lets_parse_apache_logs**](./102-lets_parse_apache_logs)

<p align="center">
  <img src="https://intranet.alxswe.com/images/contents/sysadmin/projects/80/such_awk.jpg" />
</p>
###
* **Write a <ins>**Bash script</ins> that displays numbers from 1 to 20 and:**
  * displays ${{\color{red}{\textsf{ 4\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from China\ \}}}}$ for the 4th loop iteration
  * displays ${{\color{red}{\textsf{ 9\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Japan\ \}}}}$ for the 9th loop iteration
  * displays ${{\color{red}{\textsf{ 17\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Italy\ \}}}}$ for the 17th loop iteration

* **<ins>Requirements</ins>:**
  * You must **use** the ${{\color{red}{\textsf{ while\ \}}}}$ **loop** (${{\color{red}{\textsf{ for\ \}}}}$ and ${{\color{red}{\textsf{ until\ \}}}}$ are forbidden)
  * You must **use** the ${{\color{red}{\textsf{ case\ \}}}}$ **statements**

```js
BekaHabesha@ubuntu$ ls
100-read_and_cut              1-for_best_school         6-superstitious_numbers
101-tell_the_story_of_passwd  2-while_best_school       7-clock
102-lets_parse_apache_logs    3-until_best_school       8-for_ls
103-dig_the-data              4-if_9_say_hi                  9-to_file_or_not_to_file
10-fizzbuzz                   5-4_bad_luck_8_is_your_chance
BekaHabesha@ubuntu$ ./8-for_ls
read_and_cut
tell_the_story_of_passwd
lets_parse_apache_logs
dig_the-data
fizzbuzz
for_best_school
while_best_school
until_best_school
if_9_say_hi
4_bad_luck_8_is_your_chance
superstitious_numbers
clock
for_ls
to_file_or_not_to_file
BekaHabesha@ubuntu$ 
```

##

## **No. 14. Dig the data**: heavy_check_mark:
* **File:**
  * [**103-dig_the-data**](./103-dig_the-data)
###
* **Write a <ins>**Bash script</ins> that displays numbers from 1 to 20 and:**
  * displays ${{\color{red}{\textsf{ 4\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from China\ \}}}}$ for the 4th loop iteration
  * displays ${{\color{red}{\textsf{ 9\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Japan\ \}}}}$ for the 9th loop iteration
  * displays ${{\color{red}{\textsf{ 17\ \}}}}$ *and then* ${{\color{red}{\textsf{ bad luck from Italy\ \}}}}$ for the 17th loop iteration

* **<ins>Requirements</ins>:**
  * You must **use** the ${{\color{red}{\textsf{ while\ \}}}}$ **loop** (${{\color{red}{\textsf{ for\ \}}}}$ and ${{\color{red}{\textsf{ until\ \}}}}$ are forbidden)
  * You must **use** the ${{\color{red}{\textsf{ case\ \}}}}$ **statements**

```js
BekaHabesha@ubuntu$ ls
100-read_and_cut              1-for_best_school         6-superstitious_numbers
101-tell_the_story_of_passwd  2-while_best_school       7-clock
102-lets_parse_apache_logs    3-until_best_school       8-for_ls
103-dig_the-data              4-if_9_say_hi                  9-to_file_or_not_to_file
10-fizzbuzz                   5-4_bad_luck_8_is_your_chance
BekaHabesha@ubuntu$ ./8-for_ls
read_and_cut
tell_the_story_of_passwd
lets_parse_apache_logs
dig_the-data
fizzbuzz
for_best_school
while_best_school
until_best_school
if_9_say_hi
4_bad_luck_8_is_your_chance
superstitious_numbers
clock
for_ls
to_file_or_not_to_file
BekaHabesha@ubuntu$ 
```

##
