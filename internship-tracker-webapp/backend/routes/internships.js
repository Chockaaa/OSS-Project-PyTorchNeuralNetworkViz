const router = require('express').Router();
const Internship = require('../models/internship.model');
let internships = require('../models/internship.model');

router.route('/').get((req, res) => {
    internships.find()
        .then(internships => res.json(internships))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/addInternship').post((req, res) => {
    const username = req.body.username;
    const company = req.body.company;
    const period = req.body.period;
    const stage = req.body.stage;
    const role = req.body.role;
    const link = req.body.link;


    

    const newInternship = new internships({
        username,
        company,
        period,
        stage,
        role,
        link,
    });

    newInternship.save()
        .then(() => res.json('Internship added!'))
        .catch(err => res.status(400).json('Error: ' + err));
});

router.route('/deleteInternship').delete((req, res) => {
    const username = req.body.username;
    const company = req.body.company;

    Internship.deleteOne({ username: username, company: company })
        .then(() => res.json('Internship deleted!'))
        .catch(err => res.status(400).json('Error: ' + err));
});



module.exports = router;