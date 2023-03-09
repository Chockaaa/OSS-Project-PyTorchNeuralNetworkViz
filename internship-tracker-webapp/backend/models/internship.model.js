const mongoose = require('mongoose');

const internshipSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true,
    },
    company: {
        type: String,
        required: true,
    },
    period: {   
        type: String,
        required: true,
    },
    stage: {
        type: String,
        required: true,
    },
    role: {
        type: String,
        required: true,
    },
    link:{
        type: String,
        required: true,
    },
});


const Internship = mongoose.model('Internship', internshipSchema);

module.exports = Internship;