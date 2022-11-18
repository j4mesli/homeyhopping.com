# homey-hopping.com

<a href="https://homeyhopping.onrender.com/" target="_blank">Visit my site here!</a>

A fully-automated responsive website that compiles current NYC rental listings from three distinct websites featuring Node.js and Python's BeautifulSoup package. Through the use of three spiders, distinct .csv files are generated and parsed to update the search results. The site is automatically updated once a day using a cron job at the remote host for the spiders (PythonAnywhere).

**NOTE: THIS SITE WAS MIGRATED OVER FROM SITEGROUND TO RENDER.COM TO ACCOMODATE FOR NODE.JS IMPLEMENTATION. HOWEVER, THE DOMAIN "HOMEYHOPPING.COM" WILL NOT BE AVAILABLE FOR USE TO CONNECT TO THIS SITE UNTIL DECEMBER 2nd, 2022.**

## TO-DO
1. ~~Port to Node.js and implement Express.js for better organization and optimization of site performance.~~ ✅
2. Use Mongoose to create a subscription-based mailing list that notifies subscribed users once a day via email of new listings (MongoDB).
3. Use Passport.js to create login/logout for users to "Favorite" certain listings, and view past listings from the site!
