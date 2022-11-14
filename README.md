# homey-hopping.com

<a href="https://www.homeyhopping.com/index.php" target="_blank">Visit my site here!</a>

A fully-automated responsive website that compiles current NYC rental listings from three distinct websites featuring Python's BeautifulSoup package. Through the use of three spiders, distinct .csv files are generated and parsed to update the to display results. The site is automatically updated once a day using a cron job at the remote host for the spiders (PythonAnywhere).

**NOTE: To reduce unnecessary lag and to optimize CPU usage caused by FTP requests from remote host to primary host, there was an attempt made to use Siteground's built-in Linux shell to automatically run the spiders and update scripts. However, Siteground's Fedora system doesn't allow for external packages like 'bs4' to be installed (read-only environment w/o user root access to change this), so a remote host to run the scripts was necessary to fully automate the site.**

## TO-DO
1. Port to Node.js and implement Express.js for better organization and optimization of site performance.
2. Use Express.js to create login/logout for users to "Favorite" certain listings, and share listings by copy/paste (MongoDB).
3. Use Express.js to create a subscription-based mailing list that notifies subscribed users once a day via email of new listings (MongoDB).
