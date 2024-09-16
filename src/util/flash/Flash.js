import swal from 'sweetalert'


export default function flash(response, handleNext=null) {
    swal({
        title: response.data.flash.title || null,
        text: response.data.flash.text || null,
        timer: response.data.flash.timer || null,
        buttons: response.data.flash.buttons || {
            cancel: false,
            confirm: false,
        },
    })
    .then(() => handleNext && handleNext(response))
}
