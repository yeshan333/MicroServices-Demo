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
/*         const {cookies} = props;
        this.state = {
            userId: cookies.get('session'),
        }; */
        this.state = {
            tweets: [
            {
                'id': 1,
                'name': 'guest',
                'body': '"Listen to your heart. It knows all things!"- Paulo Coelho # Motivation',
                'tweetedby': 'guest',
                'timestamp': new Date().toISOString()
            },
            {
                'id': 2,
                'name': 'guest',
                'body': '"Listen to your heart. It knows all things!"- Paulo Coelho # Motivation',
                'tweetedby': 'guest',
                'timestamp': new Date().toUTCString()
            }]
        }
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