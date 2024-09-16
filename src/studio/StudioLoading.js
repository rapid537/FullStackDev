import React from 'react'

import ReactLoading from 'react-loading'


class StudioLoading extends React.Component {
    constructor(props) {super(props)
        this.state={}
    }

    render() {
        return this.props.mini ? (
            this.renderMini()
        ) : this.renderFullPage()
    }

    renderMini() {
        return (
            <div className='loading-mask-mini'>
                <div className='loading-mini'>
                    <ReactLoading
                    className='react-loading-mini'
                    type='spin'
                    color='lime'
                    delay={0}/>
                </div>
            </div>
        )
    }

    renderFullPage() {
        return (
            <div className='loading-mask'>
                <div className='loading'>
                    <h5>
                        One moment
                        <br/>
                        we're working on your request
                    </h5>

                    <ReactLoading
                    className='react-loading'
                    type='spinningBubbles'
                    color='dodgerblue'
                    delay={0}/>
                </div>
            </div>
        )
    }
}


export default StudioLoading
