import React from 'react';
class Details extends React.Component {
    render() {
        const {state} = this.props.location
        console.log(this.props)
    return state;
    }
}

export default Details;