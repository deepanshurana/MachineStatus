import React from 'react';
import {BrowserRouter, Route, Switch, Link} from 'react-router-dom';
import Status from './status';
import Details from './details';

import './App.css';

class App extends React.Component {
  render(){
    return (
      <BrowserRouter>
          <Switch>
            <Route exact path='/' component={Status} />
            <Route path='/status' component={Details} />
          </Switch>
      </BrowserRouter>
    )
  }
}
export default App;
