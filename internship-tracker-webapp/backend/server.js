const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const { ServerApiVersion } = require('mongodb');

require('dotenv').config();

const app = express();
const port = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());


const uri = process.env.ATLAS_URI;

mongoose.connect(uri, {useNewUrlParser: true, useUnifiedTopology: true, ServerApi: ServerApiVersion.v1});
const connection = mongoose.connection;
connection.once('open', () => {console.log("MongoDB database connection established successfully");})


const internshipsRouter = require('./routes/internships');
const usersRouter = require('./routes/users');

app.use('/internships', internshipsRouter);
app.use('/users', usersRouter);


app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
    }
);