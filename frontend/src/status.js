import React from 'react';
import {Link} from 'react-router-dom';



class Status extends React.Component {
    state = {
        status: []

    };



    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/api/');
            const status = await res.json();
            this.setState({
                status
            });
            console.log(this.state)
        }catch(e) {
            console.log(e);
        }
    }
    render () {
    const {status} = this.state;
    const renderItems = (item, i) => {
      const {id, owner, data} = item;
      return <div className="container" key={i}>
    <h6 className="white-text">{id, owner}</h6>
        <div className="center">
          {/* <img src={paralaxiom} alt="An image"></img> */}
        </div>
        <div className="app-dashboard">{Object.keys(data).map((key, i) => {

          return (<div key={i} className={data[key] ? 'green items card' : 'red items card'}>
                    <Link to={
                      {
                        pathname: `/status/${key}`,
                        state: key
                      }

                    }

                    
                    >
                      <div className="card-title white-text">{key}</div>
                      <div className='card-content'>{data[key]}</div>
                    </Link>     
                  </div>)
   
    })}
        </div>
      </div>
    }
    const renderDashboard = () =>{
      return status.map((item, i)=>{
      return renderItems(item, i);
    });
    }
    return (
      <div>
          {renderDashboard()}
       </div>
    )
  }
    

};


export default Status;