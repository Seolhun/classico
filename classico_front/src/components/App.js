import React, {Component} from 'react'
import Header from './Header'
import Main from './Main'

class App extends Component {
  constructor(props) {
    super(props)
    let loc = location.pathname
    this.state = { loc : loc }
  }

  componentWillReceiveProps() {
	let loc = location.pathname
    if (loc === this.state.loc) {
        return
    }
    this.setState({ loc: loc })
  }

  render () {
    return (
        <div className="container">
          <Header loc={this.state.loc} />
          <Main loc={this.state.loc} />
        </div>
    )
  }
}

export default App
