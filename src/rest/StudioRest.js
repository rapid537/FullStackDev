import REST from 'rest/Rest'
import StudioSession from 'rest/StudioSession'


class StudioRest extends StudioSession {
    constructor(props) {super(props)
        this.REST = new REST()
    }
}


export default StudioRest
