### --- WORK IN PROGRESS! ---

# A Gentle introduction to IoT protocols: MQTT, CoAP, HTTP & WebSockets

####_A presentation by Antonio Almeida & Jaime González-Arintero for the [GOTO Conference Amsterdam 2017](https://gotoams.nl/2017/sessions/126)._

## Introduction

IoT is a buzzword. As a developer, I’m sure you’ve heard it many times - so many times that you probably tune it out as background noise at this point. Don’t let that phase you. IoT is nothing but a name for a set of ideas that you as developer should consider seriously. In this talk we'll take a practical - with demos - tour into application protocols for IoT.

This presentation uses [Markdown](https://en.wikipedia.org/wiki/Markdown) and PanDoc. _And a little help from some HTML tags._

The generated output can be an HTML/JavaScript slideshow, or a PDF file (using the `beamer` LaTeX class).

## Installing Pandoc

**NOTE:** These guidelines are taken from the [Pandoc documentation](http://pandoc.org/installing.html). If you find issues installing it, always refer to the official source.

### macOS

The easiest way is using Homebrew, also known as Brew. It's fairly easy to install, simply follow the [official guide](https://brew.sh).

Once ready open the terminal, and run:  
`$ brew install pandoc`

Homebrew will probably update the existing packages first, and will proceed to install Pandoc afterwards. Once ready, to make sure that it's working, the current version can be retrieved using the following command:  
`$ pandoc -v`

### Ubuntu (most distros)

The following command will first retrieve the latest existing packages:  
`$ sudo apt-get update`

After that, we can proceed to install Pandoc with:  
`$ sudo apt-get install pandoc`

### Debian

For 32-bit systems, there are [several packages available](https://packages.debian.org/search?keywords=pandoc) in the Debian repository.

For 64-bit systems, the easiest is to download the Debian package `pandoc-1.19.2.1-1-amd64.deb` from the [downloads page](https://github.com/jgm/pandoc/releases/tag/1.19.2.1), and execute:  
`$ sudo dpkg -i $DEB`  
(Where `$DEB` is the path to the downloaded package.)

Should you find issues, please refer to the [official installation guidelines](http://pandoc.org/installing.html).

### Windows

In Windows systems, simply download and execute the installer `pandoc-1.19.2.1-windows.msi` from the [downloads page](https://github.com/jgm/pandoc/releases/tag/1.19.2.1).

## Generating the Slides

### In HTML (interactive, using Slidy)

**To produce an interactive presentation in HTML & JavaScript**, using [Slidy](https://www.w3.org/Talks/Tools/Slidy2/#(1)), head to the the path of the cloned repository (or wherever the folder with this content was downloaded and unpacked), and run the following command:   
`$ pandoc -s -i -t slidy content.md -o presentation.html`

With all HTML slide formats, the `--self-contained` option can be used to produce a single file that contains all of the data necessary to display the slide show, including linked scripts, stylesheets, images, and videos. If so, the command will look like:  
`$ pandoc -s --self-contained -i -t slidy content.md -o presentation.html`

### In PDF (using the LaTeX beamer class)

--- WORK IN PROGRESS! ---

## To-Do

* **FIRST OF ALL... FINISH THE CONTENT!**
* Explain all the options of the Pandoc issued commands.
* Explain how to generate a PDF with the beamer class.
* Add pics of IO-Link devices.
* Brief mention of the [Mitsubishi MELSEC-Q Series](http://www.mitsubishielectric.com/fa/products/cnt/plcq/items/)
* Add pics of different Linux-capable PFCs (Wago, Beckhoff).
* Add pics of industrial-grade gateways .