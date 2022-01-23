import React, {Fragment} from 'react';
import { Form, Card, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const Home = () => {
    return (



            <Fragment>
                <div  style={{ width: '800px', display: "flex", flexWrap: "wrap", marginLeft: "auto", marginRight: "auto", marginTop: "130px" }}>
                    <Card
                        border={'primary'}
                        style={{ width: '700px', margin: "10px" }}
                        className="mb-2 mt-3"
                    >
                        <Card.Body>
                            <Card.Text>
                                <div className="container-sm mt-2 mb-4" style={{ width: '600px', }}>
                                    <h1>No SQL Project</h1>
                                    <h6> Realisé par Chiba Abdenaji et Etteboudy Imane </h6>
                                    <h6> Encadré par Professeur El Aachak Lotfi  </h6>
                                    <h6> 2020 - 2021  </h6>
                                </div>
                            </Card.Text>
                        </Card.Body>
                    </Card>
                </div>

            </Fragment>

    );
};

export default Home;