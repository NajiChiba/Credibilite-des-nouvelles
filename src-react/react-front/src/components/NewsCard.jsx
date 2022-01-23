import React from 'react';
import { Card } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const NewsCard = (props) => {
    const { tt: title, bd: body } = props;
    return (
        <>
        <Card
            border="primary"
            style={{ width: '600px', margin: "10px" }}
            className="mb-2 mt-3"
        >
            {<Card.Header> <h6>{`${title}`}</h6></Card.Header>}
            <Card.Body>
                <Card.Text>
                {`${body}`}
                </Card.Text>
            </Card.Body>
        </Card>

        {/*<Accordion defaultActiveKey="0">
            <Accordion.Item eventKey="0">
                <Accordion.Header></Accordion.Header>
                
                <Accordion.Body></Accordion.Body>
            </Accordion.Item>
    </Accordion>*/}
        </>
    );
};

export default NewsCard;