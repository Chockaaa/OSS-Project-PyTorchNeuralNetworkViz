import React from 'react'
import React, { useEffect, useState } from 'react';

const DisplayImage = () => {
    const [imageSrc, setImageSrc] = useState('');
    
    // Assuming you have received the image path or URL from the server
    useEffect(() => {
        const receivedImageSrc = 'image.png'; // Replace with the actual image path or URL
    
        // Set the received image source
        setImageSrc(receivedImageSrc);
    }, []);
    
    return (
        <div>
        {imageSrc ? (
            <img src={imageSrc} alt="Generated Image" />
        ) : (
            <p>Loading image...</p>
        )}
        </div>
    );
    };

export default DisplayImage
