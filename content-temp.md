
<!--Intermission-->

<br>
<img src="assets/intermission.jpg" alt="GOTO Rate Intro" style="width: 100%"/>


------------------

<div class="vertically-centered"><font size="100%"><span style="line-height:150%">
IoT Protocols in Industry
</span></font></div>


## What's a Fieldbus?

_"Industrial, digital bus used for real-time distributed control."_

* Mainly used in **manufacturing** (assembly lines, process control, etc.)
* Connects instruments in the shop-floor
* Allows different topologies (daisy-chain, tree, etc.)
* Controllers where originally connected through serial _(just picture the cable salads)_; a fieldbus solves that issue
* Cost-effective (less cables, easier maintenance)
* 


## Fieldbus and Industrial Ethernet standards

* Modbus RTU (serial) (published in **1979!**)
* Modbus TCP (Ethernet)
* Profibus (serial)
* Profinet
* CAN (a _vehicle bus_, in reality)
* Bitbus
* EtherCAT
* DeviceNET
* BACnet (_Although I wouldn't call it a fielbus..._)
* Etc.


## _Just a normal_ PLC

<img src="assets/plc-s7-cabinet.jpg" alt="PLC S7" style="width: 100%"/>


## What's a PFC? (with an F!)

**P**rogrammable **F**ieldbus **C**ontroller

* Not to be confused with a PLC (Programmable **Logic** Controller)
* They often support different fieldbuses by default
* Easily expandable (new I/O modules can be attached, motor drivers, etc.)
* Most of them **run an OS** (and it's possible to create custom images)
* Manufacturers provide **SDKs in different languages**
* Connectivity (at least 2x network interfaces, WiFi, 3G/LTE failover, serial, etc.)
* More and more have **built-in HTTP APIs**
* Most provide web servers for configuration, HMIs or SCADA functionalities
* They may replace the proprietary automation software suites

## What's a PFC?

<img src="assets/pfc-wago.jpg" alt="IO-Link example topology" style="width: 100%"/>


## IO-Link: _State of the art_

_"Quote that summarizes the protocol..."_

* **Not a fieldbus**
* Bla bla bla


## IO-Link: Topology example

<div class="vertically-centered" style="height: 100%">
<img src="assets/io-link-topology.jpg" alt="IO-Link example topology"/>
</div>


## IO-Link: Master / sensor aggregator

<img src="assets/io-link-master-ay1020.jpg" alt="IO-Link example topology" style="width: 100%"/>

------------------

## OPC-UA: _State of the art_

_"Quote that summarizes the protocol..."_

* **Not a protocol**, but a "unified architecture"
* Bla bla bla

------------------

<!--This image was provided by the organizers to encourage the attendees to rate the session. There's a similar image at the beginning of the presentation. Instead of Markdown, HTML is used to make sure the picture is adequately scaled.-->

<img src="assets/outro-ams17.png" alt="GOTO Rate Intro" style="width: 100%"/>