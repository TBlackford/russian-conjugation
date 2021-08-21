import React from 'react';

import './App.css';
import HomePage from '@pages/HomePage';
import { Route, Switch } from "react-router-dom";


const NoMatch = () => (
    <div>
        Page Not Found
    </div>
)


function App() {
    return (
        <div className="main-content">
            <div>
                <Switch>
                    <Route exact path="/" component={ HomePage }/>
                    <Route path="*">
                        <NoMatch/>
                    </Route>
                </Switch>
            </div>
        </div>
    );
}

export default App;
