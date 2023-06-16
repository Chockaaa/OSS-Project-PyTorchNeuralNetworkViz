import React, { useEffect, useState } from 'react';
import img_url from './neural_network.png'

const DisplayImage = () => {
    return (
            <img src={img_url} alt="Generated Image" />
    );
};

export default DisplayImage
