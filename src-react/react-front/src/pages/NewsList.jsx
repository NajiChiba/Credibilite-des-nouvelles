import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { CircularProgress } from '@material-ui/core';
import NewsCard from '../components/NewsCard';

const NewsList = () => {
    const [news, setNews] = useState([]);

    const query = `
    {
      allNews{
        id
        title
        body
      }
    }
    `
    
    const getNews = async () => {
        const response = await axios.get(`http://localhost:8000/graphql?query=${query}`)
        .catch(error => console.log('Error'))

        if(response && response.data)
            setNews(response.data.data.allNews)
    }

    useEffect( () => {
        getNews(); 
    }, [])
    
    
    return (
        <>
        {   
            
            news !== []  ? 
            (<div className='text-center' style={{ display: "flex", flexWrap: "wrap", marginLeft: "auto", marginRight: "auto" }}>
                {   
                    news.length > 11 ?
                    news.splice(0, 70).map((t, idx) => (
                        <NewsCard key={idx} id={t.id} tt={t.title} bd={t.body}/>
                    ))
                    :
                    news.map((t, idx) => (
                        <NewsCard key={idx} id={t.id} tt={t.title} bd={t.body}/>
                    ))
                }
                </div>)
            :<>
                <br />
                <br />
                <br />
                <CircularProgress/>
            </>

        }
    
        </>
    )
};

export default NewsList;