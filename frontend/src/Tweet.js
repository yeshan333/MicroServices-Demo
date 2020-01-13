import React, {Component} from 'react'

class Tweet extends Component {
    constructor(props) {
        super(props);
        //https://zh-hans.reactjs.org/docs/refs-and-the-dom.html#callback-refs
        this.tweetTextArea = React.createRef();
    }

    sendTweet(event) {
        event.preventDefault();
        const node = this.tweetTextArea.current;
        this.props.sendTweet(node.value);
    }

    render() {
        return (
            <div className="row">
                <form onSubmit={this.sendTweet.bind(this)}>
                <div className="input-field">
                    <textarea ref={this.tweetTextArea} className="materialize-textarea" />
                    <label>How do you doing?</label>
                    <button className="btn waves-effect waves-light right">
                        Tweet Now<i className="material-icons right">send</i>
                    </button>
                </div>
                </form>
            </div>
        );
    }
}

export default Tweet;