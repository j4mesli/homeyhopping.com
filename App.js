const express = require('express');
const morgan = require('morgan');

// create server
const app = express();
const port = process.env.PORT || 3000;
app.listen(port, () => {
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
app.get('/subscribe', (req, res) => {
    res.status(302).redirect('/404');
//     res.render('subscribe', {
//         title: 'SUBSCRIBE',
//     });
});

// redirects
// // 404
app.use((req, res) => {
    res.status(404).render('404', { 
        title: '404',
    });
});
