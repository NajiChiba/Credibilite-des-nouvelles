import React, { useState, Fragment } from 'react';
import { Form, Card, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import FakeCard from '../components/FakeCard';
import RealCard from '../components/RealCard';

const CheckNew = () => {
    
    const [news, setNews] = useState([]);
    const [result, setResult] = useState([]);
    
    
    const check_news = () => {
        axios.post('http://127.0.0.1:8000/news', {
            content: news
        })
        .then(function(response){
            console.log('Result : ', response.data);
            setResult(response.data);
        })
        .catch(function(err){
            console.log('error here');
        });
    }


    
    return (


        <Fragment>
            <div className="container-sm mt-5" style={{ width: '800px', display: "flex", flexWrap: "wrap", marginLeft: "auto", marginRight: "auto"}}>
                <Card
                    border={ 'primary'}
                    style={{ width: '700px', margin: "10px" }}
                    className="mb-2 mt-3"
                >
                    <Card.Body>
                        <Card.Text>
                            <div className="container-sm mt-2 mb-4" style={{ width: '600px',  }}>
                                <Form className='mb5'>
                                    <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                                        <h5>Check an Article</h5>
                                        <Form.Control dir='rtl' placeholder="Check an Article" name='article' value={news} onChange={e => {setResult(''); setNews(e.target.value)}} as="textarea" rows={3} />
                                    </Form.Group>
                                    <Button type="button" variant="primary" onClick={() => check_news()}>
                                        Check Article
                                    </Button>
                                </Form>
                                <div style={{ margin: '20px' }}>
                                    {
                                        news && (
                                            result === 'real' ?
                                                <RealCard/>
                                                : (
                                                    result ==='fake' ?
                                                        <FakeCard/>
                                                        : <></>
                                                )
                                        )
                                    }
                                </div>
                            </div>
                        </Card.Text>
                    </Card.Body>
                </Card>
            </div>

        </Fragment>
    );

};

export default CheckNew;