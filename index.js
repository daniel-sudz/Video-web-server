var express = require('express');
var app = express();
app.get('/', function(req, res){
    res.sendfile('public.html', { root: __dirname + "/public/Drop-down_html_files/" } );
});
app.use('/', express.static(__dirname + '/public')); // ← adjust
app.listen(3000, function() { console.log('listening'); });