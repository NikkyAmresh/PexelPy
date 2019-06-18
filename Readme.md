#PexelPy
* Pics Downloader with pexel API in python

----
##What is PexelPy?
> With help of **PexelPy** you can download a large number of images within one command 

----

##requirements 
   
    $ pip install requests 

----

## Setup
To get your API please visit [here](https://www.pexels.com/api/new/)

* setup your API-KEY:

###auth.py
    apikey='YOUR-API-KEY' 
    

----
## Usage:
* **New download**

        $ python app.py rose 10 xlq

    python app.py [category] [quantity] [quality] 

   * 6 qualities are available :
    * 'XLQ' for extra low quality
    * 'LQ' for low quality
    * 'M' for medium quality
    * 'HD' for HD quality
    * 'FHD' for FHD quality
    * 'N' for original quality
    * 'P' for portrait
    * 'L' for landscape


* **To continue last interrupt**
 

        $ python app.py last 


----
## Thanks
* Thanks for checking it :) 
