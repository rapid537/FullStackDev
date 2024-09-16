import {ToastContainer, toast} from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'


export function toaster() {
    return (
        <ToastContainer
        autoClose={3000}
        closeOnClick={true}
        hideProgressBar={true}
        limit={5}
        position='bottom-right'
        theme='dark'/>
    )
}

export function toastify(response) {
    // types: success, error, info, warning
    return toast[response.data.toast.type](response.data.toast.text)
}
