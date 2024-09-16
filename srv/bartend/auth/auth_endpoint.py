import datetime
from flask import session

from bartend import bcrypt
from bartend.auth.alerts import Alert
from bartend.auth.models import User
from dev.dev_session import clear_session_data
from dev.dev_session import create_session
from dev.dev_session import make_temp_session
from endpoint.studio_endpoint import StudioEndpoint
from mail.no_reply.outbound_email import AuthEmail


class AuthEndpoint(StudioEndpoint):
    def protected_route(self):
        return self.respond(payload='I am a protected route!')

    def sign_up(self):
        if not User.validate(self.data):
            return self.respond(flash=self.flash(Alert.invalid))

        user = User.api(email=self.data['email']).email_or_none()
        if user and user.email_verified:
            return self.respond(
                formik_error='email',
                flash=self.flash(Alert.email_exists),
            )

        user = User.api(username=self.data['username']).username_lower_or_none()
        if user and user.email_verified:
            return self.respond(
                formik_error='name',
                flash=self.flash(Alert.user_exists),
            )

        try:
            confirmation_code = AuthEmail().send_confirm_code(email_address=self.data['email'])

            if confirmation_code:
                user = User.api().get_or_create(
                    username=self.data['username'],
                    email=self.data['email'],
                    keygen=bcrypt.generate_password_hash(confirmation_code).decode('utf-8'),
                    stamp=datetime.datetime.now(datetime.timezone.utc),
                )

                make_temp_session(user)

                return self.respond(
                    flash=self.flash(Alert.code_sent),
                    status_code=201,
                    next='/auth/confirm-code',
                )

            return self.respond(flash=self.flash(Alert.code_not_sent))
        except Exception:
            return self.respond(flash=self.flash(Alert.code_error))

    def sign_in(self):
        user = User.api(email=self.data['email']).email_or_none()

        if user and user.email_verified:
            try:
                confirmation_code = AuthEmail().send_confirm_code(email_address=self.data['email'])

                User.api().update_or_create(
                    username=user.username,
                    keygen=bcrypt.generate_password_hash(confirmation_code).decode('utf-8'),
                    stamp=datetime.datetime.now(datetime.timezone.utc),
                )

                make_temp_session(user)

                return self.respond(
                    flash=self.flash(Alert.code_sent),
                    status_code=201,
                    next='/auth/confirm-code',
                    username=user.username,
                    email=user.email,
                )
            except Exception:
                return self.respond(flash=self.flash(Alert.code_not_sent))

        return self.__account_status_response(user=user if user else None)

    def sign_out(self):
        return self.respond(clear_session_data(), next='/auth/sign-in')

    def confirm_code(self):
        if not session.get('email'):
            return self.__account_status_response()

        user = User.api(email=session['email']).email_or_none()

        if not user:
            return self.respond(
                flash=self.flash(Alert.invalid),
                status_code=206,
                next='/auth/sign-up',
            )

        if not user.stamp or not user.keygen:
            return self.__account_status_response(user)

        if self.__is_valid_stamp(user.stamp):
            if bcrypt.check_password_hash(user.keygen, self.data['keycode']):
                User.api().update_or_create(
                    username=user.username,
                    email_verified=True,
                    keygen=None,
                    stamp=None,
                )

                clear_session_data()

                return self.respond(
                    response=create_session(user),
                    status_code=201,
                    next='/',
                )

        return self.respond(formik_error='keycode')

    def __is_valid_stamp(self, stamp):
        if ((datetime.datetime.now() - stamp) < datetime.timedelta(minutes=15)):
            return True

        return False

    def __account_status_response(self, user=None):
        if user and user.email_verified:
            return self.respond(
                flash=self.flash(Alert.invalid),
                status_code=202,
                next='/auth/sign-in',
            )

        return self.respond(
            flash=self.flash(Alert.invalid),
            status_code=202,
            next='/auth/sign-up',
        )
