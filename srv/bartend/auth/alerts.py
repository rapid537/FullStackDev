class Alert:
    code_error = {
        'title': 'Error',
        'text': 'Please try again',
    }

    code_sent = {
        'title': 'Confirmation code sent',
        'text': 'Please verify your email address\n\nThis code will expire in 15 mins',
    }

    code_not_sent = {
        'title': 'Email Error',
        'text': 'Please verify your email address and try again'
    }

    email_confirmed = {
        'title': 'Email Confirmed',
        'text': 'Sign in to continue',
    }

    email_exists = {
        'title': 'Email Already Exists',
        'text': 'Sign in to continue',
    }

    user_exists = {
        'title': 'User Already Exists',
        'text': 'Sign in to continue',
    }

    invalid = {
        'title': 'Bad Credentials',
        'text': 'Invalid User Info',
    }
