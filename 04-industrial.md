
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

## _Fieldbuses, fieldbuses all the way..._

<p style="text-align:center;">
<img src="assets/industrial-protocols-overview.jpg" alt="Industrial protocols overview" style="width: 80%"/>
</p>

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
* And many, many more...


## _Just a normal_ PLC

<img src="assets/plc-s7-cabinet.jpg" alt="PLC S7" style="width: 100%"/>


## What's a PFC? (with an F!) I

### >_ **P**rogrammable **F**ieldbus **C**ontroller

* Not to be confused with a PLC (Programmable **Logic** Controller)
* They often support different fieldbuses by default
* Easily expandable (new I/O modules can be attached, motor drivers, etc.)
* Most of them **run an OS** (and it's possible to create custom images)


## What's a PFC? (with an F!) II

### >_ **P**rogrammable **F**ieldbus **C**ontroller

* Manufacturers provide **SDKs in different languages**
* Connectivity (at least 2x network interfaces, WiFi, 3G/LTE failover, serial, etc.)
* More and more have **built-in HTTP APIs**
* Most of them integrate web servers for configuration, HMIs or SCADA functionalities
* They may replace the proprietary automation software suites


## What's a PFC?

<img src="assets/pfc-wago.jpg" alt="IO-Link example topology" style="width: 100%"/>


## IO-Link: _State of the art_

_"IO-Link is the first standardised IO technology worldwide (IEC 61131-9) for the communication with sensors and actuators. **IO-Link is no fieldbus** but the further development of the existing, tried-and-tested connection technology."_

* 3-wire connections
* Smart sensors: they work out-of-the-box, and they "identify" themselves
* Descriptive files that include information of the manufacturer, the type, and the calibration
* Sensors can be replaced, and the calibration and specs file updated remotely
* IO-Link masters support different fieldbus and Industrial Ethernet standards


## IO-Link: Topology example

<p style="text-align:center;">
<img src="assets/io-link-topology.jpg" alt="Industrial protocols overview" style="width: 80%"/>
</p>



## IO-Link: Master / sensor aggregator

<img src="assets/io-link-master-ay1020.jpg" alt="IO-Link example topology" style="width: 100%"/>


<!--
------------------

## OPC-UA: _State of the art_

_"Quote that summarizes the protocol..."_

* **Not a protocol**, but a "unified architecture"
* Bla bla bla

-->

------------------