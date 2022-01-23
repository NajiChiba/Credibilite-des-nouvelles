import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';
import CheckNew from './pages/CheckNew';
import Home from './pages/Home';
import NewsList from './pages/NewsList';
import Header from './components/Header';
import SearchPage from './pages/SearchPage'
import CheckFeeling from './pages/CheckFeeling'

function App() {
  return (
    <div className="App">
      <Router>
        <Header/>
        <Switch>
          <Route exact path="/" children={<Home/>} />
          <Route exact path="/check-news" children={<CheckNew/>} />
          <Route exact path="/check-feeling" children={<CheckFeeling/>} />
          <Route exact path="/news" children={<NewsList/>} />
          <Route exact path="/search" children={<SearchPage/>} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
