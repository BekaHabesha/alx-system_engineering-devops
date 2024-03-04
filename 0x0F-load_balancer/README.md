<H1 align="center", height="1500"> <ins> README.md File </ins> </H1>
<H1 align="center"> <ins> 0x0F. Load balancer README.md</ins> </H1>

<p align="center">
  <img src="https://i.ibb.co/JttfyKD/0x0-C-Web-server-Alx-logo.png" />
</p>

##

* **File_name:📋** 📖 [**README.md**](https://github.com/BekaHabesha/alx-system_engineering-devops/blob/master/0x0F-load_balancer/README.md)
* **Created: 📅** <ins>**On March 04, 2024**</ins>🕙
* **Author:🖊️** 👨🏻‍💻 [***Bereket Dereje Mekonnen***](https://intranet.alxswe.com/users/BereketDerejeMekonnen) 🧑‍💻
* **Project Title: 🔠**  💻 [**0x0F. Load balancer**](https://intranet.alxswe.com/projects/275) 📝🔡
* **GitHub repository: 📦** 🗂 [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops) 🗂
* **Directory: 💼** 📂 [**0x0F-load_balancer**](https://github.com/BekaHabesha/alx-system_engineering-devops/tree/master/0x0F-load_balancer)
* **Project Tasks: 📚** <ins>**💯Mandatory💯 and ⁉️Advanced♨️**</ins>
* **Tasks in number: 🔢** <ins>**3 Tasks (2-Mandatory and 1-Advanced)**</ins>
* **Mandatory_Tasks:** 💯 <ins>**From Task 0 to 1**</ins> 💯
* **Advanced_Tasks:** ⁉️ <ins>**Task 2**</ins> ♨️

###   

<p align="center">
  <img src="https://www.cloud4u.com/upload/medialibrary/5a6/0_CCK15OF3DizmOITk.png" />
</p>
                     
##

## <ins>**PROJECT_TITLE</ins>: 🔠**  💻 [**0x0F. Load balancer**](https://intranet.alxswe.com/projects/275) 📝🔡

## <ins>**GITHUB_REPOSITORY</ins>: 📦** 🗂 [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops) 🗂

## <ins>**DIRECTORY</ins>: 💼** 📂 [**0x0F-load_balancer**](https://github.com/BekaHabesha/alx-system_engineering-devops/tree/master/0x0F-load_balancer)

###

<h2>Concepts</h2>

* *For this project, we expect you to look at these concepts:*
  * [**Load balancer**](https://intranet.alxswe.com/concepts/46)
  * [**Web stack debugging**](https://intranet.alxswe.com/concepts/68)

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png" />
  <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/bae58c9f066a9668001ef4b4c39778407439d2f9.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T162011Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9aae1e35ee53d8b37fd3edd09279883be18491f98a59dba1683c7f1d231603c5" />
  <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/6cefdd14b2f8c36789cba132bd5a10d42d88a177.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240304%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240304T162010Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8f584f47fc0f97ff0054b34e1197fc86b719c4503da7a1321acad59309f3334b" />
</p>

###

<h1> Background Context </h1>

* **You have been given 2 additional servers:**
  * gc-[STUDENT_ID]-web-02-XXXXXXXXXX
  * gc-[STUDENT_ID]-lb-01-XXXXXXXXXX<br>
Let’s improve our web stack so that there is [**redundancy**](https://intranet.alxswe.com/rltoken/xnAaJdhmAxx7PoH3l6EwDg) for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.
###
For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/PC-Netzteil_%28redundant%29.jpg/220px-PC-Netzteil_%28redundant%29.jpg" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Reliability_block_diagram.png/220px-Reliability_block_diagram.png" />
</p>

###

<h1> <ins>Resources</ins> :floppy_disk:</H1>

### **Read or watch:** :heavy_check_mark:
* [**Introduction to load-balancing and HAproxy**](https://intranet.alxswe.com/rltoken/B7f3oz8i3Xvvom_YQZzLnQ)
* [**HTTP header**](https://intranet.alxswe.com/rltoken/sZ9v3Vq2tgLwN_PWVQketw)
* [**Debian/Ubuntu HAProxy packages**](https://intranet.alxswe.com/rltoken/2VRAgtKKR9g6Xfb0xzGiSg)

<p align="center">
  <img src="https://www.haproxy.com/img/containers/posts/haproxy-configuration-load-balance-your-servers.png/d3d71b2ca84a588091a93bb3ffbdfc87.png" />
  <img src="https://cdn.tutsplus.com/cdn-cgi/image/width=424/net/uploads/legacy/511_http/response_header.png" />
  <img src="https://linuxgenie.net/wp-content/uploads/2023/04/3-1024x423.jpg" />
  <img src="https://learn.microsoft.com/en-us/azure/load-balancer/media/load-balancer-overview/load-balancer.png" />
  <img src="https://webhostinggeeks.com/howto/wp-content/uploads/2023/07/HAProxy-Load-Balancing.png" />
  <img src="https://programmaticponderings.files.wordpress.com/2015/02/simple-load-balanced-2.png" />
  <img src="https://i.stack.imgur.com/iv9N3.png" />
</p>

###

<H1><ins>Requirements</ins> :floppy_disk:</H1>

<H2>General :heavy_check_mark:</H2>

* **Allowed editors:** ${{\color{red}{\textsf{ vi\ \}}}}\$ , ${{\color{red}{\textsf{ vim\ \}}}}\$ , ${{\color{red}{\textsf{ emacs\ \}}}}\$.
* All your <ins>**files</ins>** will be **interpreted** on <ins>**Ubuntu 16.04 LTS**</ins>
* All your <ins>**files**</ins> should **end with a new line**
* A ${{\color{red}{\textsf{ README.md\ \}}}}$ <ins>**file**</ins>, at the root of the folder of the project is mandatory.
* All your <ins>**Bash script files**</ins> must be **executable**
* Your **Bash script** must pass ${{\color{red}{\textsf{ Shellcheck\ \}}}}\$ (**version** ${{\color{red}{\textsf{ 0.3.7\ \}}}}\$) without any errors.
* The <ins>**first line of all your Bash scripts</ins>** should be exactly [**#!/usr/bin/env bash**](./0-custom_http_response_header)
* The <ins>**second line of all your Bash scripts</ins>** should be a comment explaining what is the script doing.

<p align="center">
  <img src="https://static.thegeekstuff.com/wp-content/uploads/2016/01/1-weighted-scheduling-load-balancer.png" />
  <img src="https://static.thegeekstuff.com/wp-content/uploads/2016/01/2-round-robin-load-balancer.png" />
  <img src="https://static.thegeekstuff.com/wp-content/uploads/2016/01/3-osi-layer-load-balancer.png" />
  <img src="https://static.thegeekstuff.com/wp-content/uploads/2016/01/4-layer7-load-balancer.png" />
</p>

###

## <ins>**PROJECT_TITLE</ins>: 🔠**  💻 [**0x0F. Load balancer**](https://intranet.alxswe.com/projects/275) 📝🔡

## <ins>**GITHUB_REPOSITORY</ins>: 📦** 🗂 [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops) 🗂

## <ins>**DIRECTORY</ins>: 💼** 📂 [**0x0F-load_balancer**](https://github.com/BekaHabesha/alx-system_engineering-devops/tree/master/0x0F-load_balancer)

<p align="center">
  <img src="https://javachallengers.com/wp-content/uploads/2023/09/load_balancer_java.png" />
</p>

##

* **File_name:📋** 📖 [**README.md**](https://github.com/BekaHabesha/alx-system_engineering-devops/blob/master/0x0F-load_balancer/README.md)
* **Created: 📅** <ins>**On March 04, 2024**</ins>🕙
* **Author:🖊️** 👨🏻‍💻 [***Bereket Dereje Mekonnen***](https://intranet.alxswe.com/users/BereketDerejeMekonnen) 🧑‍💻
* **Project Title: 🔠**  💻 [**0x0F. Load balancer**](https://intranet.alxswe.com/projects/275) 📝🔡
* **GitHub repository: 📦** 🗂 [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops) 🗂
* **Directory: 💼** 📂 [**0x0F-load_balancer**](https://github.com/BekaHabesha/alx-system_engineering-devops/tree/master/0x0F-load_balancer)
* **Project Tasks: 📚** <ins>**💯Mandatory💯 and ⁉️Advanced♨️**</ins>
* **Tasks in number: 🔢** <ins>**3 Tasks (2-Mandatory and 1-Advanced)**</ins>
* **Mandatory_Tasks:** 💯 <ins>**From Task 0 to 1**</ins> 💯
* **Advanced_Tasks:** ⁉️ <ins>**Task 2**</ins> ♨️

###

<p align="center">
  <img src="https://i.ibb.co/y5wmQyd/Alx-enginn-Build-ur-future.png" />
</p>

<H1 align="center"> <ins> PROJECT TASKS (Mandatory and Advanced)</ins>:floppy_disk:</H1>

<H1 align="center">MANDATORY_TASKS (From Task 0 to 1) :cd:</h1>

## **No. 0. Double the number of webservers** :heavy_check_mark:
* **File:**
  * [**0-custom_http_response_header**](./0-custom_http_response_header)
###
In this first task you need to configure ${{\color{red}{\textsf{ web\ \}}}}$**-**${{\color{red}{\textsf{ 02\ \}}}}$ to be identical to ${{\color{red}{\textsf{ web\ \}}}}$**-**${{\color{red}{\textsf{ 01\ \}}}}$. Fortunately, you built a Bash script during your [**web server project**](), and they’ll now come in handy to easily configure ${{\color{red}{\textsf{ web\ \}}}}$**-**${{\color{red}{\textsf{ 02\ \}}}}$. Remember, always try to automate your work!<br>
Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.
###
* <ins>**Requirements</ins>:**
  * Configure Nginx so that its HTTP response contains a custom header (on ${{\color{red}{\textsf{ web\ \}}}}$**-**${{\color{red}{\textsf{ 01\ \}}}}$ and ${{\color{red}{\textsf{ web\ \}}}}$**-**${{\color{red}{\textsf{ 02\ \}}}}$)
    * The name of the custom HTTP header must be ${{\color{red}{\textsf{ X\ \}}}}$**-**${{\color{red}{\textsf{ Served\ \}}}}$**-**${{\color{red}{\textsf{ By\ \}}}}$
    * The value of the custom HTTP header must be the hostname of the server Nginx is running on
  * Write [**0-custom_http_response_header**](./0-custom_http_response_header) so that it configures a brand new Ubuntu machine to the requirements asked in this task
    * [**Ignore**](https://intranet.alxswe.com/rltoken/k3Bt6zu1On_-mDszxi0Z9w)   [**SC2154**](https://intranet.alxswe.com/rltoken/9KwKHb9H8OJqcSK0saRIOA) for ${{\color{red}{\textsf{ Shellcheck\ \}}}}\$
###

<ins>**Example</ins>:**
```js
sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
sylvain@ubuntu$
```

If your server’s hostnames are not properly configured (**[**${{\color{red}{\textsf{ STUDENT\ \}}}}$**_**${{\color{red}{\textsf{ ID\ \}}}}$**]-**${{\color{red}{\textsf{ web\ \}}}}$**-**${{\color{red}{\textsf{ 01\ \}}}}$ and **[**${{\color{red}{\textsf{ STUDENT\ \}}}}$**_**${{\color{red}{\textsf{ ID\ \}}}}$**]-**${{\color{red}{\textsf{ web\ \}}}}$**-**${{\color{red}{\textsf{ 02\ \}}}}$.), follow this [**tutorial**](https://intranet.alxswe.com/rltoken/qSor8ulAHl4HedrO6KJEoQ).

##

## **No. 1. Install your load balancer**:heavy_check_mark:
* **File:**
  * [**1-install_load_balancer**](./1-install_load_balancer)
###
**Install** and configure **HAproxy on** your${{\color{red}{\textsf{ lb\ \}}}}$**-**${{\color{red}{\textsf{ 01\ \}}}}$ server.
###

* <ins>**Requirements</ins>:**
  * Configure HAproxy so that it send traffic to ${{\color{red}{\textsf{ web\ \}}}}$**-**${{\color{red}{\textsf{ 01\ \}}}}$ and ${{\color{red}{\textsf{ web\ \}}}}$**-**${{\color{red}{\textsf{ 02\ \}}}}$
  * Distribute requests using a roundrobin algorithm
  * Make sure that HAproxy can be managed via an init script
  * Make sure that your servers are configured with the right hostnames: **[**${{\color{red}{\textsf{ STUDENT\ \}}}}$**_**${{\color{red}{\textsf{ ID\ \}}}}$**]-**${{\color{red}{\textsf{ web\ \}}}}$**-**${{\color{red}{\textsf{ 01\ \}}}}$ and **[**${{\color{red}{\textsf{ STUDENT\ \}}}}$**_**${{\color{red}{\textsf{ ID\ \}}}}$**]-**${{\color{red}{\textsf{ web\ \}}}}$**-**${{\color{red}{\textsf{ 02\ \}}}}$. If not, follow this [**tutorial**](https://intranet.alxswe.com/rltoken/YkfzgEa6xNHrQbkKmJN4zg).
  * For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements
###

<ins>**Example</ins>:**
```js
sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:19 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
X-Served-By: 03-web-02
Accept-Ranges: bytes

sylvain@ubuntu$
```

###

<h1 align="center">ADVANCED_TASKS (From Task 2) :cd:</h1>

## **No. 2. Add a custom HTTP header with Puppet** :heavy_check_mark:
* **File:**
  * [**2-puppet_custom_http_response_header.pp**](./2-puppet_custom_http_response_header.pp)
###
* Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
  * The name of the custom HTTP header must be ${{\color{red}{\textsf{ X\ \}}}}$**-**${{\color{red}{\textsf{ Served\ \}}}}$**-**${{\color{red}{\textsf{ By\ \}}}}$
  * The value of the custom HTTP header must be the hostname of the server Nginx is running on
  * Write [**2-puppet_custom_http_response_header.pp**](./2-puppet_custom_http_response_header.pp) so that it configures a brand new Ubuntu machine to the requirements asked in this task
 
###
