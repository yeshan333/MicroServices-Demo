import React from 'react'
import ReactDOM from 'react-dom'

class Main extends React.Component {
    render() {
        return (
            <div>
                <h1>Welcome to cloud-native-app !</h1>
            </div>
        );
    }
}

let documentReady = () => {
    ReactDOM.render(
        <Main />,
        document.getElementById('react'),
    );
};

$(documentReady);//Jquery Object，匿名函数在网页载入完成后开始执行