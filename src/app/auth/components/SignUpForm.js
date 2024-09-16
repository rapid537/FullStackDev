import StudioButton from 'material/buttons/StudioButton'
import StudioForm, {yup} from 'studio/StudioForm'
import StudioInput from 'material/input/StudioInput'
import StudioLoading from 'studio/StudioLoading'
import StudioTitleBar from 'studio/StudioTitleBar'


class SignUpForm extends StudioForm {
    constructor(props) {super(props)
        this.state = {
            name: false,
            email: false,
            loading: false,
        }
    }

    renderChildren(props) {
        return (
            <>
                {this.state.loading && <StudioLoading/>}

                <StudioInput
                type='text'
                name='name'
                labelText={props.errors?.name ? props.errors.name : 'Display Name'}
                required={true}
                value={props.values?.name}
                error={this.state.name}
                onChange={props.handleChange}/>

                <StudioInput
                type='email'
                name='email'
                labelText={props.errors?.email ? props.errors.email : 'Email Address'}
                required={true}
                value={props.values?.email}
                error={this.state.email}
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
        return (
            yup.object().shape({
                name: yup.string()
                .min(2, 'Too Short')
                .max(64, 'Too Long'),

                email: yup.string()
                .max(127, 'Invalid Email Format')
                .email('Invalid Email Format'),
            })
        )
    }

    initialValues() {
        return ({
            name: '',
            email: '',
        })
    }

    formID() {
        return 'sign-up-form'
    }

    onSubmit(values) {
        this.setState({loading: true})

        const payload = {
            username: values.name,
            email: values.email,
        }

        this.REST.POST('sign_up', payload)
        .then(response => this.handleResponse(response, values))
    }

    handleResponse(response, values) {
        this.setState({loading: false})

        if (response?.data?.formik_error) {
            this.setState({[response.data.formik_error]: true})
        }

        if (response.status === 201) {
            this.stateful({
                user: {
                    userName: values.name,
                    userMail: values.email,
                }
            })
        }
    }

    renderTitleBar() {
        return <StudioTitleBar title='Sign Up'/>
    }
}


export default SignUpForm
