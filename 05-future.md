<div class="vertically-centered"><font size="100%"><span style="line-height:150%">
A glimpse into the future
</span></font></div>

------------------

<br/>
<p style="text-align:center;">
<img src="assets/closer-than-we-think.jpg" alt="Future Factory Farms" style="width: 100%"/>
</p>


## Information Centric Networking (ICN) vs Host Centric Networking (HCN)

<p style="text-align:center;">
<img src="assets/icn.png" alt="ICN" style="width: 60%"/>
</p>

 * HCN: Conversation between **hosts** &mdash; **who** to talk to.
 * ICN: Spreads **data** objects &mdash; **what** to say


## Data Distribution Service (DDS)

<p style="text-align:center;">
<img src="assets/dds.jpg" alt="Data Distribution Service" style="width: 80%"/>
</p>


## DDS in a nutshell

* Has been around for some time &mdash; DDS 1.0 (2005).
* Main entities:
	* Domain Participant
	* Data Writer
	* Publisher
	* Data Reader
	* Subscriber
	* Topic 
* All networking is abstracted. Usually implemented on top of raw sockets
* Anycasting and Multicasting
  
  
## ICN in a nutshell I

* Shares _packet forwarding_ with IP mostly
* Outline of request - response
	* **Consumer** requests **named data**: **Interest**
	* **Interest** is forwarded to a place (or places) where named data exists
	* **Forwarder** records the interface on which the Interest was received
	* **Data** is returned in a **Content** message
	* Data in Content is **signed** to avoid tampering
* A lot of caching strategies possible  &mdash; see the web

 
## ICN in a nutshell II
  
* **Communication** between **consumers** and **named data**
* **Forwarders** interact with messages and maintain a state per-message (!== IP)
* **Data name** instead of IP address
* Anycasting and Multicasting
* **Consumer** can roam &mdash; easy mobility


## ICN in a nutshell III

* Is a research topic
* Many open questions:
* Routing
	* Congestion control
	* Push (event) also, not only polling
* Multiple research projects: US, Europe
* Watch this space
