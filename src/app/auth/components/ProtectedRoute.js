import StudioManager from 'rest/StudioManager'


class ProtectedRoute extends StudioManager {
    constructor(props) {super(props)
        this.state={
            server_msg: null,
        }
    }

    componentDidMount() {
        this.REST.GET('protected_route').then(response => {
            this.setState({server_msg: response.data.payload})
        })
    }

    render() {
        return (
            <div className='protected-route-wrapper'>
                <div className='protected-route-container'>
                    <h1>{this.state.server_msg}</h1>
                </div>
            </div>
        )
    }
}


export default ProtectedRoute
