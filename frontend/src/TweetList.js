import React, {Component} from 'react'
import Tweettemplate from './TweetTemplate'

class TweetList extends Component {
    render() {
        let tweetlist = this.props.tweets.map(tweet => <Tweettemplate key={tweet._id} {...tweet} />);
        //console.log(tweetlist);
        return (
            <div>
                <ul className="collection">
                    {tweetlist}
                </ul>
            </div>
        );
    }
}

export default TweetList;