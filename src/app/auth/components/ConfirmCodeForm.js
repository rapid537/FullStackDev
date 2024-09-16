import StudioButton from 'material/buttons/StudioButton'
import StudioForm, {yup} from 'studio/StudioForm'
import StudioInput from 'material/input/StudioInput'
import StudioTitleBar from 'studio/StudioTitleBar'


class ConfirmCodeForm extends StudioForm {
    constructor() {super()
        this.state = {keycode: false}
    }

    formID() {
        return 'confirm-code-form'
    }

    renderChildren(props) {
        return (
            <>
                <StudioInput
                type='text'
                name='keycode'
                labelText={props.errors?.keycode ? props.errors.keycode : 'Six Digit Code'}
                required={true}
                value={props.values?.keycode}
                error={this.state.keycode}
                onChange={props.handleChange}/>

                <StudioButton
                type='submit'
                text='Confirm'
                variant='contained'
                size='large'
                form={this.formID()}/>
            </>
        )
    }

    initialValues() {
        return {keycode: ''}
    }

    onSubmit(values) {
        const payload = {
            email: this.SESSION.user.userMail,
            keycode: values.keycode,
        }

        this.REST.POST('confirm_code', payload)
        .then(response => this.handleResponse(response))
    }

    handleResponse(response) {
        if (response?.data?.formik_error) {
            this.setState({[response.data.formik_error]: true})
        }

        console.log(response)
    }

    formSchema() {
        return yup.object().shape({
            keycode: yup.string()
            .min(6, 'Too Short')
            .max(6, 'Too Long'),
        })
    }

    renderTitleBar() {
        return <StudioTitleBar title='Confirmation Code'/>
    }
}


export default ConfirmCodeForm
