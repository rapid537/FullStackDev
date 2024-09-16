import StudioButton from 'material/buttons/StudioButton'
import StudioForm, {yup} from 'studio/StudioForm'
import StudioInput from 'material/input/StudioInput'
import StudioTitleBar from 'studio/StudioTitleBar'


class SignInForm extends StudioForm {
    constructor(props) {super(props)
        this.state = {
            emailError: false,
        }
    }

    renderChildren(props) {
        return (
            <>
                <StudioInput
                type='email'
                name='email'
                labelText={props.errors?.email ? props.errors.email : 'Email Address'}
                required={true}
                value={props.values?.email && props.values.email}
                error={this.state.emailError}
                onChange={props.handleChange}/>

                <StudioButton
                type='submit'
                text='Submit'
                variant='contained'
                size='large'
                form={this.formID()}/>
            </>
        )
    }

    formSchema() {
        return yup.object().shape({
            email: yup.string()
            .max(75, 'Invalid Email Format')
            .email('Invalid Email Format'),
        })
    }

    initialValues() {
        return {
            email: '',
        }
    }

    formID() {
        return 'sign-in-form'
    }

    onSubmit(values) {
        this.REST.POST('sign_in', values)
        .then(response => this.handleResponse(response))
    }

    renderTitleBar() {
        return <StudioTitleBar title='Sign In'/>
    }

    handleResponse(response, values) {
        if (response.data.formik_error) {
            return this.setState({[response.data.formik_error]: true})
        }

        console.log(response)

        if (response.status === 201) {
            return this.stateful({
                user: {
                    userName: response.data.username,
                    userMail: response.data.email,
                },
            })
        }
    }
}


export default SignInForm
