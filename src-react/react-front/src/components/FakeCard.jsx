import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Chip from '@material-ui/core/Chip';

const FakeCard = () => {
    return (
        <Chip className='mb-2' color="secondary" label="Fake News" style={{width:'250px', backgroundColor:'#DC3545'}} />
             
    );
};

export default FakeCard;