<H1 align="center"> <ins> Postmortem</ins> </H1>
<H1 align="center"> <ins> 500 Internal Server Error and 503 Service Unavailable Error</ins> </H1>

Upon the release of [**alx-system_engineering-devops**](https://github.com/BekaHabesha/alx-system_engineering-devops) project [**0x19. Postmortem**](https://intranet.alxswe.com/projects/294), approximately 06:00🕕 **East African🌍 Time🕰** ***(EAT)*** here in **Addis Ababa** capital of **Ethiopia**, The firist one is an outage occurred on an isolated [**Ubuntu 14.04**](https://releases.ubuntu.com/focal) container running an Apache web server. GET requests on the server led to [**500 Internal Server Error's**](https://github.com/BekaHabesha/alx-system_engineering-devops/blob/master/0x19-postmortem/README.md), when the expected response was an HTML file📋 defining a simple [**Holberton WordPress site**](https://blog.holbertonschool.com/) and the second one [**The HyperText Transfer Protocol (HTTP) 503 Service Unavailable server error**](https://github.com/BekaHabesha/alx-system_engineering-devops/blob/master/0x19-postmortem/README.md) causes are a server that is down for maintenance or that is overloaded. This response code indicates that the server is not ready to handle the request. This response should be used for temporary conditions and the Retry-After HTTP header should, if possible, contain the estimated time for the recovery of the service.

###

<H1 align="center"> <ins> No 1. 500 Internal Server Error</ins> </H1>

<H1>💻🌐<ins>Debugging🛄 ♻️Process📚</ins> :heavy_check_mark:</H1>

* [**The Web UI Debug Window(Bug debugger Brennan)**](https://thebrennan.com/blogs/how-to-guides/the-web-ui-debug-window) (BDB... as in my actual initials... made that up on the spot, pretty good, huh?) encountered the issue upon opening the project and being, well, instructed to address it, roughly 19:20 PST. He promptly proceeded to undergo solving the problem.
  * 1. Checked running processes using <ins>**ps aux**</ins>. 
    * Two <ins>**apache2**</ins> processes - ${{\color{red}{\textsf{ root\ \}}}}\$ and ${{\color{red}{\textsf{ www\ \}}}}\$**-**${{\color{red}{\textsf{ data\ \}}}}\$ - were properly running.
  * 2. Looked in the ${{\color{red}{\textsf{ sites\ \}}}}\$**-**${{\color{red}{\textsf{ available\ \}}}}\$ folder📂 of the <ins>**/etc/apache2/**</ins> 📦Directory🗂.
    * Determined that the ${{\color{red}{\textsf{ web\ \}}}}\$ ${{\color{red}{\textsf{ server\ \}}}}\$ was serving content located in <ins>**/var/www/html/**</ins>.
  * 3. In terminal one, ran ${{\color{red}{\textsf{ strace\ \}}}}\$ on the PID of the ${{\color{red}{\textsf{ root\ \}}}}\$ Apache process.
    * In the other terminal, curl the ${{\color{red}{\textsf{ server\ \}}}}\$. 
    * Expected great things... only to be disappointed. 
    * ${{\color{red}{\textsf{ strace\ \}}}}\$ gaves us no useful information.
  * 4. Repeated step 3, except on the **PID** of the ${{\color{red}{\textsf{ www\ \}}}}\$**-**${{\color{red}{\textsf{ data\ \}}}}\$ process. 
    * This time we Kept our expectations lower ... but was rewarded! 
      * ${{\color{red}{\textsf{ strace\ \}}}}\$ revelead an **-1 ENOENT (No such file or directory)** error occurring upon an attempt to access the file <ins>**/var/www/html/wp-includes/class-wp-locale.phpp</ins>**.
  * 5. Then Looked through files in the <ins>**/var/www/html/</ins>** 📦Directory🗂 one-by-one, 
    * using ${{\color{red}{\textsf{ Vi\ \}}}}\$ ${{\color{red}{\textsf{ pattern\ \}}}}\$ matching to try and locate the erroneous **.phpp** file extension. 
      * Located it in the <ins>**wp-settings.php</ins>** file. (Line 137, ***require_once( ABSPATH . WPINC . <ins>**/class-wp-locale.php</ins>** );***).
  * 6. Then Removed the trailing ${{\color{red}{\textsf{ p\ \}}}}\$ from the line.
  * 7. The we Tested another test using ${{\color{red}{\textsf{ curl\ \}}}}\$ command on the ${{\color{red}{\textsf{ server\ \}}}}\$. 
    * ${{\color{red}{\textsf{ 200\ \}}}}\$ ${{\color{red}{\textsf{ A\ \}}}}\$ **-ok!**
  * 8. Then Wrote a ${{\color{red}{\textsf{ Puppet\ \}}}}\$ ${{\color{red}{\textsf{ manifest\ \}}}}\$ to **automate <ins>fixing the error</ins>**.

###

<H1>📮🏷<ins>Summation</ins>📍📌 :heavy_check_mark:</H1>

In full, the <ins>**WordPress app</ins>** was encountering a critical error in [**wp-settings.php**](./https://intranet.alxswe.com/user_containers/648990/webterm/wp-settings.php) when tyring to load the file [**class-wp-locale.phpp**](https://intranet.alxswe.com/user_containers/648990/webterm/class-wp-locale.phpp). The correct file name, located in the ${{\color{red}{\textsf{ wp\ \}}}}\$**-**${{\color{red}{\textsf{ content\ \}}}}\$ 📦Directory🗂 of the 📱application📲 folder📂, was [**class-wp-locale.php](https://intranet.alxswe.com/user_containers/648990/webterm/class-wp-locale.php).<br>
Patch involved a simple fix on removing the trailing ${{\color{red}{\textsf{ p\ \}}}}\$.

###

<H1>🔧🔱<ins>Prevention</ins>⚜️⚙️ :heavy_check_mark:</H1>

* This outage was not a ${{\color{red}{\textsf{ web\ \}}}}\$ ${{\color{red}{\textsf{ server\ \}}}}\$ ${{\color{red}{\textsf{ error\ \}}}}\$, but it is an ${{\color{red}{\textsf{ application\ \}}}}\$ ${{\color{red}{\textsf{ error\ \}}}}\$. To prevent such outages moving forward, please keep the following in mind.
  * **📮 🔎<ins>Test!</ins>🔍 📍🔎<ins>Test</ins>🔍 🔎<ins>Test</ins>🔍🔖 🔎<ins>Test</ins>🔍🏷** 
    * Test the ${{\color{red}{\textsf{ application\ \}}}}\$ before deploying. 
      * This ${{\color{red}{\textsf{ error\ \}}}}\$ would have arisen and could have been addressed earlier had the app been tested.
  * **📮 ♻️📉<ins>Status monitoring</ins>📈♻️** 
    * Enable some ${{\color{red}{\textsf{ uptime\ \}}}}\$**-**${{\color{red}{\textsf{ monitoring\ \}}}}\$ ${{\color{red}{\textsf{ service\ \}}}}\$ 
      * such as [UptimeRobot](https://uptimerobot.com/) to alert instantly upon outage of the website.
###

> [!NOTE]
> Note that in response to this type of error, 
> I wrote a Puppet manifest [**0-strace_is_your_friend.pp**](https://github.com/BekaHabesha/alx-system_engineering-devops/blob/master/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp) 
> to automate fixing of any such identitical errors should they occur in the future. 
> The manifest replaces any **phpp** extensions in the file **/var/www/html/wp-settings.php** with **php**.
##

> [!IMPORTANT]
> But of course, it will never occur again, 
> because we are Alx gradjuate programmers, 
> and we never make errors!

##

<H1 align="center"> <ins> No 2. 503 Service Unavailable Error</ins> </H1>

<H2>🏷<ins>Issue Summary</ins>:📌 :heavy_check_mark:</H2>

* **Start Time: ⏱** 🕕 11:01 PM (East Africa Time — EAT)
* **End Time:  🕰** 🕤 11:45 PM (EAT)
##

* **🔦<ins>Impact</ins>:💡** 
  * **🔍Service Affected🔎:**
    * ${{\color{red}{\textsf{ Authentication\ \}}}}\$ ${{\color{red}{\textsf{ System\ \}}}}\$
##
  * **👨🏽‍💻User Experience💻:** 
    * ${{\color{red}{\textsf{ Users\ \}}}}\$ ${{\color{red}{\textsf{ encountered\ \}}}}\$ ${{\color{red}{\textsf{ persistent\ \}}}}\$ ${{\color{red}{\textsf{ 503\ \}}}}\$ ${{\color{red}{\textsf{ errors\ \}}}}\$, 
    * **rendering** the entire **authentication system** inaccessible. 
    * ${{\color{red}{\textsf{ 100\ \}}}}\$${{\color{red}{\textsf{ %\ \}}}}\$ of users were affected.
##

* **🪜⛓<ins>Root Cause</ins>🪔🧿:** 
  * Overloaded authentication servers due to a sudden surge in user traffic.
##

* **🗓⏱<ins>Timeline</ins>⌚️🗓:** in **EAT**
  * **⏲️11:01 PM🕰:**
    * Anomaly detected with a surge in ${{\color{red}{\textsf{ 503\ \}}}}\$ ${{\color{red}{\textsf{ errors\ \}}}}\$ through monitoring alerts.
  * **⏲️11:05 PM🕰:**
    * Initiated investigation into server logs to understand error patterns and identify potential causes.
  * **⏲️11:10 PM🕰:**
    * Assumed potential server misconfiguration or a sudden increase in malicious traffic.
  * **⏲️11:15 PM🕰:**
    * Explored misleading paths including the possibility of a DDoS attack and recent code changes causing a bug in the authentication system.
  * **⏲️11:20 PM🕰:**
    * Escalated the incident to the System Operations Team and Network Infrastructure Team.
  * **⏲️11:25 PM🕰:**
    * <ins>**Action Plan</ins>:**
      * The identifiedroot cause as overloaded authentication servers due to a sudden surge in user traffic.
      * Added additional authentication servers to distribute the load evenly.
      * Implemented rate limiting to control incoming traffic and prevent server overload.
  * **⏲️11:30 PM🕰:**
    * <ins>**Communication Overhaul</ins>:**
      * Refined communication strategy to provide transparent updates to users about the situation and expected resolution times.
  * **⏲️11:35 PM🕰:**
    * <ins>**Verification Playground</ins>:**
      * Conducted thorough testing to ensure the implemented measures effectively resolved the issue.
  * **⏲️11:40 PM🕰:**
    * <ins>**Documenting the Battlefield</ins>:**
      * Updated system documentation to include details of the outage incident, root cause, and implement resolutions.
  * **⏲️11:45 PM🕰:**
    * <ins>**Future-Proofing Measures</ins>:**
      * Initiated tasks for ongoing improvements, including enhanced monitoring, auto-scaling mechanisms, and code optimizations.

##

## **🪜📡⛓<ins>Root Cause and Resolution</ins>🪔📜🧿:** 

* **⛓<ins>Root Cause Explanation🪔:**
  * The authentication servers were overwhelmed by an unexpected and substantial increase in user traffic, resulting in the generation of ${{\color{red}{\textsf{ 503\ \}}}}\$ ${{\color{red}{\textsf{ errors\ \}}}}\$.
##

* **📡Resolution Details🧿:** 
  * Increased the capacity of the authentication server pool to handle higher concurrent connections.
  * Implemented rate limiting to control the number of incoming requests and prevent server overload.
  * Refined the communication strategy to keep users informed about the situation.

##

## **🔍🔰⚠️<ins>Corrective and Preventative Measures</ins>🔎🚸🛡:** 

* **🔍🔰Areas for Improvement/Fixing🔎🚸:**
  * Enhance monitoring to proactively identify traffic spikes and potential server overload.
  * Implement auto-scaling mechanisms to dynamically adjust server resources based on traffic patterns.
##

* **🔍⚠️Specific Tasks🔎🛡:**
  * <ins>**TODO</ins>:** Improve monitoring to set up alerts for traffic spikes and server health.
  * <ins>**TODO</ins>:** Implement auto-scaling configurations for the authentication server pool.
  * <ins>**TODO</ins>:** Conduct a comprehensive review of the authentication system code to identify potential optimizations.
  * <ins>**TODO</ins>:** Update the incident response playbook to include procedures for handling sudden traffic spikes.

##

## **🔍🔰⚠️<ins>Conclusion</ins>🔎🚸🛡:** 

* The widespread ${{\color{red}{\textsf{ 503\ \}}}}\$ ${{\color{red}{\textsf{ error\ \}}}}\$ outage, lasting from **⏲️11:01 PM🕰:** to **⏲️11:45 PM🕰:** **EAT**,
  * resulted from ${{\color{red}{\textsf{ overloaded\ \}}}}\$ ${{\color{red}{\textsf{ authentication\ \}}}}\$ ${{\color{red}{\textsf{ servers\ \}}}}\$ due to an **unforeseen surge in user traffic**. 
##

* The ${{\color{red}{\textsf{ postmortem\ \}}}}\$ provides insights into the ${{\color{red}{\textsf{ incident\ \}}}}\$**’s** ${{\color{red}{\textsf{ impact\ \}}}}\$, 
  * The steps taken during the resolution, and a roadmap for ongoing improvements. 
  * This comprehensive analysis ensures a transparent understanding of the outage, 
    * its causes, and the measures in place to fortify against similar challenges.

###
