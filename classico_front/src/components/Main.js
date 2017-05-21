import React from 'react'
import { Switch, Route } from 'react-router-dom'
import Home from './Home'
import Detail from './Detail'

const Main = () => {
    return (
		<Switch>
		  <Route exact path='/' component={Home} />
		  <Route path='/:detail' component={Detail} />
		</Switch>
    )
}

export default Main
