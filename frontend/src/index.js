import React from 'react'
import ReactDOM from 'react-dom'
import $ from 'jquery'

class Main extends React.Component {
    render() {
        return (
            <div>Welcome to Cloud Native App</div>
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