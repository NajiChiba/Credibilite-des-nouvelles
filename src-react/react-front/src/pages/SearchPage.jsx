import React, { Component, Fragment } from 'react';
import axios from 'axios';
import { Form, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import NewsCard from '../components/NewsCard';

class App extends Component {

  state = {
    result: [],
    userInput: null,
  }


  handleSubmit = event => {
    event.preventDefault();

    // requete de recherche :  
    const query = {
      query: {
        query_string: { "fields": ["title", "body"], query: `*${this.state.userInput}*` }
      }
    };
    var input = document.getElementById("userText").value;
    this.setState({ userInput: input });
    // get 'http://localhost:9200/ < index ou je stock les données > /_search
    axios.get('http://localhost:9200/news-index/_search', {
      params: {
        source: JSON.stringify(query),
        source_content_type: 'application/json'
      }
    }).then(res => {
      var result = res.data.hits.hits;
      this.setState({ result: result });
      console.log(this.state.result);
      for (let i = 0; i < this.state.result.length; i++) {
        console.log(this.state.result[i]["_source"]["title"]);
      }
    })

  }

  render() {
    return (


      <Fragment>
        <div className="container-sm mt-2" style={{ width: '600px' }}>
          <div className="container-sm mt-2 mb-4" style={{ width: '600px' }}>
            <Form className='mb5'>
              <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                <Form.Control dir='rtl' type="text" placeholder="Search" name="query" id="userText" onChange={e => { this.setState({ userInput: e.target.value }) }} />
              </Form.Group>
              <Button variant="primary" type="submit" onClick={this.handleSubmit}>
                Search
              </Button>
            </Form>
            <div style={{ margin: '20px' }}>

            </div>
          </div>
        </div>

        <div className='text-center' style={{ display: "flex", flexWrap: "wrap", marginLeft: "auto", marginRight: "auto" }}>
            {this.state.result &&
                this.state.result.splice(0, 70).map((t, idx) => (
                  <>
                    <NewsCard key={idx} tt={t["_source"]["title"]} bd={t["_source"]["body"]} />
                    <br/>
                  </>
                    ))
              
            }
        </div>
      </Fragment>
    );
  }
}

export default App;