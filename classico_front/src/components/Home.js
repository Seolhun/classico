import React, { Component } from 'react'

class Home extends Component {
  render () {
    return (
        <div className="row" className="bgwhite">
            <div className="tab-content mgt30" id="trending-tabs">
                <div className="tab-pane in active" id="ajax-content">
                    <div className="col-md-8 col-md-offset-2 col-sm-12 col-sm-offset-0 col-xs-12 col-xs-offset-0">
                        <div className="trending-load-more div-center mg0">
                            <div className="col-md-12 col-sm-12 col-xs-12">
                                <div className="trending-item-container">
                                    <div className="row">
                                        <div className="col-md-1 col-sm-1 col-xs-1 starring">
                                            <a className="toggle-favorite-service">
                                              <div className="star-count" id="service-4225">18</div>
                                            </a>
                                        </div>
                                        <a className="col-md-2 col-sm-2 col-xs-2 pointer" href="https://stackshare.io/lets-encrypt">
                                            <div className="service-logo"><img src="./data/4vBYgpew.png" alt="4vbygpew" /></div>
                                        </a>
                                        <a href="https://stackshare.io/lets-encrypt" className="pointer">
                                        </a>
                                        <div className="col-md-7 col-md-offset-0 col-sm-7 col-sm-offset-0 col-xs-8 col-xs-offset-0">
                                            <a href="https://stackshare.io/lets-encrypt" className="pointer"></a>
                                            <div className="heigt66">
                                                <a href="https://stackshare.io/lets-encrypt" className="pointer">
                                                    <div id="service-card-trending">
                                                        <span id="service-name-trending">Let's Encrypt</span>
                                                        <span className="hint--top"></span>                                                        
                                                        <span className="hint--top" data-align="left" data-hint="Votes">
                                                          <span className="trending-reason-count">14</span>
                                                        </span>
                                                        <span className="hint--top">
                                                         | 
                                                        </span>
                                                        <span className="hint--top" data-align="left" data-hint="Stacks including this">
                                                          <span className="trending-reason-count">59</span>
                                                        </span>
                                                    </div>
                                                    <div className="trending-description">
                                                        A free, automated, and open Certificate Authority (CA)
                                                    </div>
                                                    <ol className="breadcrumb col-md-10 hidden-xs bread-nav bread-data">
                                                        <li>
                                                            <span className="sub-category">Certificate Authority</span>
                                                        </li>
                                                    </ol>
                                                </a>
                                                <div className="hidden-md hidden-lg hidden-sm">
                                                    <a href="https://stackshare.io/lets-encrypt" className="pointer"></a><a className="btn btn-ss-g btn-xs hint--top visit-web" data-hint="https://letsencrypt.org" data-align="left" href="https://letsencrypt.org/">Visit Website</a></div>
                                            </div>
                                        </div>
                                        <div className="col-md-2 col-sm-2 hidden-xs">
                                            <div className="visit-web2">
                                                <a target="_blank" className="btn btn-ss-g btn-xs btn-block visit-web3" href="https://letsencrypt.org/">Visit Website</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <hr className="visible-xs" />
                            </div>
                        </div>
                        <div className="div-center">
                            <div className="row"><a className="trending-tab-load-more-services btn btn-ss-alt btn-lg visit-more" href="https://stackshare.io/trending/tools#">More</a></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
  }
}

export default Home
