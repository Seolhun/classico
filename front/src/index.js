import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
//import $ from 'jquery';
// import App from './App';

// jquery checking
//$("continer");

// react
const language = navigator.languages && (navigator.languages[0] || // Chrome / Firefox
    navigator.language || // All browsers
    navigator.userLanguage); // IE <= 10

// index Class Def
class BodyList extends Component {
  constructor(props) {
    super(props);
    this.state = {
        default: {},
        data: {},
        lang: ""
    };
  }

  componentDidMount() {
    axios
      .get("/json/lang.js")
      .then(({data})=> {
        let lang = "";
        let txt = {};

        txt.default = data.default;

        if (language.indexOf("ko") !== -1) {
            txt.data = data.ko;
            lang = "ko";
        } else if (language.indexOf("ja") !== -1) {
            txt.data = data.ja;
            lang = "ja";
        } else {
            txt.data = data.en;
            lang = "en";
        }        

        this.setState({ 
            default : txt.default,
            data : txt.data,
            lang : lang
        });
      })
      .catch((err)=> {})

  }

  componentWillUnmount() {
    this.serverRequest.abort();
  }

  render() {
    if (this.state.lang.length > 0) {
        return (
            <div className="site-wrapper-inner" id={this.state.lang}>
                <div className="cover-container">
                    <div className="masthead clearfix">
                        <div className="inner">
                            <h3 className="masthead-brand">{this.state.data.ti[0]}</h3>
                        </div>
                    </div>
                    <div>
                        <h1>{this.state.data.fi[0]}</h1>
                        <div className="list-group mt30">
                            {this.state.default.fi_url[1].map((x, i) =>
                                <a key={i} href={this.state.default.fi_url[1][i]} className="list-group-item"><span className="label label-info label-pill pull-xs-right">{this.state.default.fi[1][i].length === 0 ? '' : this.state.default.fi[1][i]}</span>{this.state.data.fi[1][i]}</a>
                            )}
                        </div>
                    </div>
                    <hr />
                    <div>
                        <h1>{this.state.data.se[0][0]}</h1>
                        <div className="list-group mt30">
                            {this.state.default.se_url[1].map((x, i) =>
                                <a key={i} href={this.state.default.se_url[1][i]} className="list-group-item"><span className="label label-info label-pill pull-xs-right">{this.state.default.se[1][i].length === 0 ? this.state.data.le[0] : this.state.default.se[1][i] + " | " + this.state.data.le[0]}</span>{this.state.data.se[1][i]}</a>
                            )}
                        </div>
                    </div>
                </div>
                <div className="mastfoot">
                    <div className="inner">
                        <p className="footer-text">{this.state.data.cm[0]} <a className="comment-area" data-clipboard-text={this.state.default.cm[0]}>{this.state.default.cm[0]}</a> - {this.state.data.cm[1]}</p>
                    </div>
                </div>
            </div>        
        );
    } else {
        return (
            <div className="site-wrapper-inner" id={this.state.lang}>
                <p>Processing</p>
            </div>
        )
    }
  }
}

ReactDOM.render(
  <BodyList />,
  document.getElementById("container")
);
