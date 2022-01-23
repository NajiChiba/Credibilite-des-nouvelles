import React from 'react';
import {LinkContainer} from 'react-router-bootstrap';

import {
    Navbar,
    Nav,
    Container
} from 'react-bootstrap'

const Header = () => {
    return (
        <>
            <Navbar bg="primary" variant="dark">
                <Container>
                    <LinkContainer to="/">
                        <Navbar.Brand >Home</Navbar.Brand>
                    </LinkContainer>
                    <Nav className="me-auto">
                        
                        <LinkContainer to="/news">
                            <Nav.Link >News List</Nav.Link>
                        </LinkContainer>
                        
                        <LinkContainer to="/check-news">
                            <Nav.Link >Check News</Nav.Link>
                        </LinkContainer>

                        <LinkContainer to="/check-feeling">
                            <Nav.Link >Check Feeling</Nav.Link>
                        </LinkContainer>

                        <LinkContainer to="/search">
                            <Nav.Link >Search News</Nav.Link>
                        </LinkContainer>
                    </Nav>
                </Container>
            </Navbar>
            
        </>
    );
};

export default Header;