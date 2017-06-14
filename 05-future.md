## A glimpse into the future

<p style="text-align:center;">
<img src="assets/visions_future.jpg" alt="Future Factory Farms" style="width: 80%"/>
</p>


## Information Centric Networking (ICN) vs Host Centric Networking (HCN)

<p style="text-align:center;">
<img src="assets/icn-cloud.png" alt="Future Factory Farms" style="width: 80%"/>
</p>

 * HCN: conversation between **hosts** &mdash; **who** to talk to.
 * ICN: spreads **data** objects &mdash; **what** to say

## Data Distribution Service (DDS)

<p style="text-align:center;">
<img src="assets/dds.png" alt="Data Distribution Service" style="width: 80%"/>
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
 * All networking is abstracted. Usually implemented on top of raw sockets.
 * Anycasting and Multicasting.
  
## ICN in a nutshell I

 * shares _packet forwarding_ with IP mostly.
 * Outline of request - response
   1. **Consumer** requests **named data**: **Interest**.
   2. **Interest** is forwarded to a place (or places) where named data exists.
   3. **Forwarder** records the interface on which the Interest was received.
   4. **Data** is returned in a **Content** message.
   5. Data in Content is **signed** to avoid tampering.
 * A lot of caching strategies possible  &mdash; see the web.  
  
## ICN in a nutshell II
  
 * **Communication** between **consumers** and **named data**.
 * **Forwarders** interact with messages and maintain a state per-message (!== IP).
 * **Data name** instead of IP address. 
 * Anycasting and Multicasting.
 * **Consumer** can roam &mdash; easy mobility.
 
## ICN in a nutshell III

 * Is a research topic.
 * Many open questions:
   * Routing.
   * Congestion Control.
   * Push (Event) also, not only Polling. 
 * Multiple research projects: US, Europe.
 * Watch this space.
   