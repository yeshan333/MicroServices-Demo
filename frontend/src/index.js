import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'
//import Tweet from './Tweet'
import TweetList from './TweetList'
import Tweet from './Tweet';
/* import { instanceOf } from 'prop-types';
import { Cookies } from 'react-cookie'; */

class Main extends React.Component {
/*     static propTypes = {
        cookies: instanceOf(Cookies).isRequired
    }; */

    constructor(props) {
        super(props);
        this.state = {
            tweets: []
        }
    }

    componentDidMount() {
        var self = this;
        $.ajax({
            url: 'http://127.0.0.1:5000/api/v2/tweets',
            success: function(data) {
                //console.log(typeof data + '1')
                console.log(typeof data['tweets_list'][0] + '66');//type：string
                //console.log(data['tweets_list'][0]['_id'])//undefined
                //const tweets_list = JSON.parse(data['tweets_list'][0]);
                //console.log(typeof tweets_list);
                self.setState({
                    tweets: data['tweets_list']
                });
                alert(self.state.tweets);
                return console.log("Sucess");
            },
            error: function() {
                return console.log("Failed")
            }
        })
    }

    addTweet(tweet) {
        let newTweet = this.state.tweets;
        newTweet.unshift({
            'id': new Date().toUTCString(), 'name': 'guest', 'body': tweet, 'timestamp': new Date().toLocaleDateString(), 'tweetedby': 'guest'
        });
        //console.log(newTweet);
        this.setState({tweets: newTweet});
    }

    render() {
        return (
            <div className="container">
                <Tweet sendTweet={this.addTweet.bind(this)} />
                <TweetList tweets={this.state.tweets} />
            </div>
        );
    }
}

let documentReady = () => {
    ReactDOM.render(
        <Main />,
        document.getElementById('root')
    );
};

$(documentReady);