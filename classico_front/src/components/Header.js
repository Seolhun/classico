import React, { Component } from 'react'

class Header extends Component {

  render () {
    return (
        <header>
            <div className="container">
                <div id="trending-header">
                    <div>
                        <span className="trending-title">Trending</span>
                    </div>
                    <div id="trending-sub-header">
                        What's hot across StackShare today
                    </div>
                    <div className="row mgt30">
                        <div className="col-md-10 col-md-offset-1">
                            <div className="input-group">
                                <input type="text" className="form-control" placeholder="Search for..." />
                                <span className="input-group-btn">
                                  <button className="btn btn-default" type="button">Go!</button>
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
    )
  }
};

export default Header
