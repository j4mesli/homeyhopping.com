const express = require('express');
const morgan = require('morgan');

// create server
const app = express();
app.listen(3000, 'localhost', () => {
    console.log("listening on http://localhost:3000");
});

// middleware
app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(express.urlencoded({
    extended: true,
}));
app.use(morgan('dev'));

// routes
// // home
app.get('/', (req, res) => {
    res.render('index', {
        title: 'HOME',
    });
});
// // send
app.get('/send', (req, res) => {
    res.render('send', {
        title: 'SEND LISTING',
    });
});

// redirects
// // 404
app.use((req, res) => {
    res.status(404).render('404', { 
        title: '404',
    });
});