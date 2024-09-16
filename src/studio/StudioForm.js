import {Formik} from 'formik'
import FormControl from '@mui/material/FormControl'

import StudioManager from 'rest/StudioManager'


class StudioForm extends StudioManager {
    render() {
        return (
            <Formik
            validationSchema={this.formSchema}
            initialValues={this.initialValues()}
            onSubmit={async values => this.onSubmit(values)}>

                {props => (
                    <div className='studio-form'>
                        <form
                        id={this.formID()}
                        className={this.formID()}
                        onSubmit={props.handleSubmit}>

                            {this.renderTitleBar()}
                            <FormControl >
                                {this.renderChildren(props)}
                            </FormControl>

                        </form>
                    </div>
                )}

            </Formik>
        )
    }

    formID() {
        throw new Error('Must implement formID override method')
    }

    renderChildren() {
        throw new Error('Must implement renderChildren override method')
    }

    initialValues() {
        throw new Error('Must implement initialValues override method')
    }

    onSubmit() {
        throw new Error('Must implement onSubmit override method')
    }

    formSchema() {
        throw new Error('Must implement formSchema override method')
    }

    renderTitleBar() {
        return null
    }
}


export * as yup from 'yup'
export default StudioForm
