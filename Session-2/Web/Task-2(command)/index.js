const express = require('express');
const app = express();
const { exec } = require('child_process');

app.use(express.static('public'));

app.get('/', (req, res) => {
  return res.sendFile(__dirname + '/index.html')
});

app.get('/cowsay/:message', (req, res) => {
  exec(`cowsay ${req.params.message}`, {timeout: 5000}, (error, stdout) => {
    if (error) return res.status(500).end();
    res.type('txt').send(stdout).end();
  });
});

app.listen(3000, () => {
  console.log('listening');
});
