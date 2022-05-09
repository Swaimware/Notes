# Internet

## Tools

* muffet http://localhost:3000   used to check links on websites

## Provider

* Digital Ocean a good place to host a cloud linux

## Network

* Tracepath apple.com    
* dig apple.com
* nslookup apple.com
* ip -br a   to find your own ip -br stands for brief
* ifconfig   another exploration of own Network
* 127.0.0.1 is localhost
* Port 80 for http  Port 443 for https
* overthewire.org   learn security and SSH
* SCP sends files over SSH
* SCP ~/.bashrc root@xxx.xxx.xxx.xxx:   don't forget the : at end
* mullvad vpn
* ssh root@xxx.xxx.xxx.xxx

## Request

### Verbs

* Get - HttpGet - Request Resource
* POST - HttpPost - Create Resource
* PUT - HttpPut- Update Resource
* PATCH - HttpPatch - Update Partial Resource
* DELETE - HttpDelete - Delete Resource
* More Verbs these are the most common

### Headers - Metadata about the request

* Content Type - The format of Content
* Content Length - Size of Content
* Authorization - Who's making the call
* Accept - What types can Accept
* Cookies - Passenger data in the request
* Hundred more Headers available plus can creat your own

### Content

* HTML, CSS, JavaScript, XML, JSON
* Content is not valid with some Verbs
* Information to help fulfill request
* Binary and blobs common (e.g. .jpg)

## Response

### Status Code - Operation Status

* 100-199 - Informational
* 200-299 - Success
* 300-399 - Redirection
* 400-499 - Client Errors
* 500-599 - Server Errors

### Headers - Metadata about the Response

* Content Type - The format of Content
* Content Length - Size of Content
* Expires - When to consider stale
* Cookies - Passenger data in the request
* More headers available

### Content
