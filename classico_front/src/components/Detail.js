import React, { Component } from 'react'

class Detail extends Component {

  render () {
    return (
        <div>
            <header className="service">
                <div className="container">
                    <div className="row">
                        <ol className="breadcrumb col-md-10 col-xs-12 bread-nav detail-1">
                            <li className="active">
                                <a className="btn btn-ss-g-alt btn-xs" itemprop="applicationSubCategory" href="/business-intelligence">Business Intelligence</a>
                            </li>
                            <li>
                                <a itemprop="applicationCategory" href="/analytics">Analytics</a>
                            </li>
                            <li>
                                <a href="/utilities">Utilities</a>
                            </li>
                        </ol>
                    </div>
                    <div className="title-wrap">
                        <div className="row">
                            <div className="col-md-9 col-xs-12">
                                <div className="sp-service-logo col-md-2 col-xs-12">
                                    <a target="_blank" href="https://github.com/hashedin/squealy"><img alt="image" src="https://img.stackshare.io/service/6951/no-img-open-source.png" /></a>
                                </div>
                                <div className="service-wrap">
                                    <div className="col-md-10 col-xs-12">
                                        <a target="_blank" itemprop="name" href="https://github.com/hashedin/squealy">SQueaLy</a>
                                        <a className="source-code-link" href="https://github.com/hashedin/squealy" target="_blank">
                                            <span className="hint--top" data-align="left" data-hint="Open Source" />
                                        </a>
                                    </div>
                                    <div className="col-md-10 col-xs-12">
                                        <span itemprop="alternativeHeadline">Fast track analytics for business</span>
                                    </div>
                                </div>
                            </div>
                            <div className="col-md-3 col-md-offset-0 col-sm-offset-4 col-sm-4 col-xs-offset-3 col-xs-6 mgt20">
                                <div className="row">
                                    <div className="service-mob col-md-3 col-md-offset-0 col-sm-3 col-sm-offset-0 col-xs-9 col-xs-offset-3">
                                        <div className="service-trending-container detail-2">
                                            <a className="toggle-favorite-service service-fav" data-remote="true" href="/favorite_services/toggle/6951">
                                                <div className="star-count">1</div>
                                                <span className="detail-3">Favorite</span>
                                            </a>
                                        </div>
                                    </div>
                                    <div className="col-md-9 col-sm-9 col-xs-12 mgb10">
                                        <div>
                                            <a className="btn btn-ss-alt btn-lg i-use-this btn-block drop-theme-arrows-bounce-dark drop-target" data-link="/stacks/i_use_this/6951" data-service="6951">I Use This</a>
                                            <div className="visible-xs">
                                                <a target="_blank" className="btn btn-ss-g-alt btn-block i-use-this drop-theme-arrows-bounce-dark drop-target mgt20" id="visit-website" href="https://github.com/hashedin/squealy">Visit Website</a>
                                            </div>
                                            <div className="div-center hidden-xs website-block mgt10"><a target="_blank" className="btn-block btn btn-ss-g-alt btn-xs" href="https://github.com/hashedin/squealy">Visit Website</a></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
            <div className="row">
                <div className="tab-content detail-4">
                    <div className="tab-pane in active" id="ajax-content">
                        <div className="container">
                            <div className="row">
                                <div className="col-md-12 col-xs-12">
                                    <div className="row clearfix">
                                        <div className="row mga0">
                                            <div className="pd28">
                                                <div id="service-description">
                                                    <span itemprop="about">SQueaLy is an open-source, self-deployable application for developers. It is a micro service for business intelligence and analytics which uses SQL queries to generate reporting APIs with fine-grained security.</span>
                                                </div>
                                                <div id="reasons">
                                                    <div className="section-title">
                                                        Why people like SQueaLy
                                                    </div>
                                                    <div id="reasons-container mga0">
                                                        <div className="row mga0">
                                                            <div id="reasons-section">
                                                                <table className="wd100">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td className="row reasons-list detail-5" data-service_id="6951" id="reasons-list-tile">
                                                                                <div className="panel-group col-md-11 col-md-offset-1 col-sm-12 col-sm-offset-0">
                                                                                </div>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </div>
                                                        </div>
                                                        <div className="row">
                                                            <div className="add-reason col-md-6 col-md-offset-2 col-sm-offset-1 col-sm-6 detail-6">
                                                                <div className="add-reason-title">
                                                                    Add a one-liner
                                                                </div>
                                                                <form className="new_reason" id="new_reason" action="/reasons" accept-charset="UTF-8" data-remote="true" method="post">
                                                                    <input name="utf8" type="hidden" value="✓" />
                                                                    <div className="hint--top" data-align="left" data-hint="eg &quot;Easy setup&quot;, &quot;Great customer support&quot;, or &quot;GitHub integration&quot;" id="reason-input">
                                                                        <input className="form-control new-reason-text" data-behavior="submit_on_enter" placeholder="Why do you like using SQueaLy?" style="width:280px" maxlength="55" required="required" size="55" type="text" name="reason[text]" id="reason_text" />
                                                                        <span className="counter">55</span>
                                                                        <br />
                                                                        <div id="btn-responsive">
                                                                            <input type="submit" name="commit" value="Submit" className="btn btn-ss hint--top detail-7" />
                                                                        </div>
                                                                    </div>
                                                                    <input type="hidden" value="6951" name="reason[service_id]" id="reason_service_id" />
                                                                </form>
                                                            </div>
                                                            <div className="add-reason col-md-4 col-sm-5 detail-8">
                                                                <div id="btn-responsive"><a className="btn btn-ss hint--top detail-9"data-hint="Tell other developers about your experience with SQueaLy" data-align="left" href="/reviews/new?service_id=6951">Add a review</a></div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <br />
                                                </div>
                                            </div>
                                            <div className="similar-service-logos detail-10">
                                                <div className="row">
                                                    <div className="detail-11">
                                                        <div className="section-title">
                                                            SQueaLy integrates with
                                                        </div>
                                                    </div>
                                                </div>
                                                <div className="row detail-12">
                                                    <div className="col-md-12">
                                                        <div className="row detail-13">
                                                            <div className="col-md-1 stack-logo detail-14">
                                                                <a data-hint="PostgreSQL" data-align="left" className="hint--top detail-15" href="/postgresql"><img alt="PostgreSQL" className="company-icon" src="https://img.stackshare.io/service/1028/ASOhU5xJ.png" /></a>
                                                            </div>
                                                            <div className="col-md-1 stack-logo detail-14">
                                                                <a data-hint="PostgreSQL" data-align="left" className="hint--top detail-15" href="/postgresql"><img alt="PostgreSQL" className="company-icon" src="https://img.stackshare.io/service/1028/ASOhU5xJ.png" /></a>
                                                            </div>                                                        
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <br />
                                            <br />
                                        </div>
                                    </div>
                                    <div>
                                        <div className="row detail-16">
                                            <div className="section-title similar detail-16">
                                                <a href="/business-intelligence">Similar Tools &amp; Services</a>
                                            </div>
                                        </div>
                                        <div className="row detail-12">
                                            <div className="col-md-12">
                                                <div className="row similar-services-items detail-18">
                                                    <div className="col-md-1 stack-logo detail-19">
                                                        <a data-hint="GoodData" data-align="left" className="hint--top" href="/gooddata"><img alt="GoodData" className="company-icon" src="https://img.stackshare.io/service/285/62z_9s83.png" /></a>
                                                        <div className="row similar-services-items">
                                                            <a href="/gooddata">GoodData</a>
                                                        </div>
                                                    </div>
                                                    <div className="col-md-1 stack-logo detail-19">
                                                        <a data-hint="GoodData" data-align="left" className="hint--top" href="/gooddata"><img alt="GoodData" className="company-icon" src="https://img.stackshare.io/service/285/62z_9s83.png" /></a>
                                                        <div className="row similar-services-items">
                                                            <a href="/gooddata">GoodData</a>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
  }
}

export default Detail
