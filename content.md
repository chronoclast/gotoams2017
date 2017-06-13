% A Gentle Introduction to IoT Protocols: MQTT, CoAP, HTTP & WebSockets  
% Antonio Almeida and Jaime González-Arintero  
% June 14, 2017

------------------

<!--This image was provided by the organizers to encourage the attendees to rate the session. There's a similar image at the end of the presentation. Instead of Markdown, HTML is used to make sure the picture is adequately scaled.-->

<p style="text-align:center;">
<img src="assets/intro-ams17.png" alt="GOTO Rate Intro" style="width: 100%"/>
</p>


## Visionaries

### >_ On-line Man-Computer Communication, 1962

<p style="text-align:center;">
<img src="assets/visionaries-on-line-man-machine.png" alt="On-line Man-Computer Communication" style="width: 80%"/>
</p>


## Visionaries

### >_ The Computer as a Communication Device, 1968

<p style="text-align:center;">
<img src="assets/visionaries-computer-as-a-communication-device.png" alt="The Computer as a Communication Device" style="width: 80%"/>
</p>


## Arpanet

<p style="text-align:center;">
<img src="assets/arpanet.png" alt="Arpanet" style="width: 80%"/>
</p>


## Connected devices

### >_ Some figures...

<p style="text-align:center;">
<img src="assets/machines-go-online.png" alt="Machines Go Online" style="width: 60%"/><blockquote style="float:right">-MIT Technology Review, 2014</blockquote><br clear="all" />
</p>


## Connected devices

### >_ Some figures...

* 14 bn connected devices | Bosch SI
* 50 bn connected devices | Cisco
* 309 bn IoT supplier revenue | Gartner
* 1.9 tn IoT economic value add | Gartner
* 7.1 tn IoT solutions revenue | IDC

> _By 2020, component costs will have come down to the point that connectivity will become standard feature, even for processors costing **less than $1**._  
- Peter Middleton, Gartner


## Constrained devices

* IETF Definition: **[tools.ietf.org/html/rfc7228](https://tools.ietf.org/html/rfc7228)**
* Limited processing power
* Unreliable networking
* Low power _(so they can run on batteries)_

------------------

<div class="vertically-centered"><font size="150%">
Why more protocols?
</font></div>


## MQTT: Basics

**M**essage **Q**ueue **T**elemetry **T**ransport

_"Publish-subscribe-based "lightweight" messaging protocol, for use on top of the TCP/IP protocol."_

* Publish-subscribe
* A **message broker** is required
* Standard: ISO/IEC PRF 20922
* Small code footprint
* Limited network bandwidth / constrained environments
* Developed in 1999 (and released royalty free in 2010)
* Data agnostic


## MQTT: Simplified example

<p style="text-align:center;">
<img src="assets/mqtt-simplified.png" alt="GOTO Rate Intro" style="width: 100%;"/>
</p>


## MQTTS and MQTT-SN

_"Publish-subscribe-based "lightweight" messaging protocol, for use on top of the TCP/IP protocol."_

* Bla bla bla
* Bla bla bla
* Learn more: [mqtt.org](http://mqtt.org)


## MQTT: Learn more

<!--TO REVIEW-->

There are client libraries and wrappers for practically all languages used in M2M setups, as well as 

* Learn more: **[mqtt.org](http://mqtt.org)**
* Software: **[mqtt.org/software](http://mqtt.org/software)**
* Recommended broker: **Mosquitto ([mosquitto.org](https://mosquitto.org))**
* Lots of good tutorials out there

------------------

## CoAp

_"Quote that summarizes the protocol..."_

* Standard:
* Bla bla bla

------------------

## HTTP

_"Quote that summarizes the protocol..."_

* Standard:
* Bla bla bla

------------------

## WebSockets

_"Quote that summarizes the protocol..."_

* Standard:
* Bla bla bla

------------------

<div class="vertically-centered"><font size="100%"><span style="line-height:150%">
Get Tough: Adoption of IoT Protocols in Industry
</span></font></div>


## What's a Fieldbus?

_"Industrial, digital bus used for real-time distributed control."_

* Mainly used in manufacturing (assembly lines, process control, etc.)
* Connects instruments in the shop-floor
* Allows different topologies (daisy-chain, tree, etc.)
* Bla bla bla

------------------

## Fieldbus standards

* Modbus RTU (serial) (published in **1979!**)
* Modbus TCP (Ethernet)
* Profibus (serial)
* CAN (a _vehicle bus_, in reality)
* Bitbus
* EtherCAT
* DeviceNET
* BACnet (_Although I wouldn't call it a fielbus..._)
* Etc.

------------------

## Industrial Ethernet standards

* Profinet
* CAN (a _vehicle bus_ in reality)
* 

------------------

## What's a PFC?

**P**rogrammable **F**ieldbus **C**ontrollers

* Not to be confused with a PLC (Programmable **Logic** Controller)
* They often support different fieldbuses by default
* Easily expandable (new I/O modules can be attached, motor drivers, etc.)

------------------

## What's a PFC?

<img src="assets/pfc-wago.jpg" alt="IO-Link example topology" style="width: 100%"/>

------------------

## IO-Link: _State of the art_

_"Quote that summarizes the protocol..."_

* **Not a fieldbus**
* Bla bla bla

------------------

## IO-Link: Topology example

<img src="assets/io-link-topology.jpg" alt="IO-Link example topology" style="height: 100%"/>

------------------

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

<!-- DISCARDED / BACKUP SLIDES

## IoT Protocols: MQTT, CoAP, HTTP & WebSockets

IoT is a buzzword. As a developer, I’m sure you’ve heard it many times - so many times that you probably tune it out as background noise at this point. Don’t let that phase you. IoT is nothing but a name for a set of ideas that you as developer should consider seriously. In this talk we'll take a practical - with demos - tour into application protocols for IoT.

### Outline of today's talk:

* MQTT
* CoAP
* HTTP
* WebSockets
* When **to use (or not!)** each of these protocols

------------------

## Bonus

* Adoption of these protocols in the **industrial world**
* Integration with existing fieldbuses
* And of course... **DEMOS!**

-->