# homey-hopping.com

<a href="https://www.homeyhopping.com/index.php">Visit my site here!</a>

A fully-automated responsive website that compiles current NYC rental listings from three distinct websites featuring Python's BeautifulSoup package. Through the use of three spiders, distinct .csv files are generated and parsed to update the to display results. The site is automatically updated using a cron job at the remote host for the spiders (PythonAnywhere).

**NOTE: To reduce unnecessary lag and to optimize CPU usage caused by FTP requests from remote host to primary host, there was an attempt made to use Siteground's built-in Linux shell to automatically run the spiders and update scripts. However, Siteground's Fedora system doesn't allow for external packages like 'bs4' to be installed (read-only environment w/o user root access to change this), so a remote host to run the scripts was necessary to fully automate the site.**
