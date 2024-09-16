import React from 'react'
import {StyledEngineProvider, ThemeProvider} from '@mui/material/styles'
import {theme} from 'material/theme/Theme'

import MainRouter from 'app/MainRouter'


class Main extends React.Component {
    render() {
        return (
            <ThemeProvider theme={theme}>
                <StyledEngineProvider injectFirst>
                    <MainRouter/>
                </StyledEngineProvider>
            </ThemeProvider>
        )
    }
}


export default Main
