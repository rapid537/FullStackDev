from api.studio_api import StudioAPI
from bartend import db


class AuthAPI(StudioAPI):
    def create(self):
        try:
            db.session.add(self.kwargs.get('object'))
            db.session.commit()
        except Exception:
            db.session.rollback()

    def get_or_create(self, **kwargs):
        user = self.model.query.filter_by(
            username=kwargs.get('username')
        ).first()

        if not user:
            user = self.model(**kwargs)
            db.session.add(user)
            db.session.commit()

        return user

    def update_or_create(self, **kwargs):
        user = self.model.query.filter_by(
            username=kwargs.get('username')
        ).first()

        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            db.session.commit()
        else:
            user = self.model(**kwargs)
            db.session.add(user)
            db.session.commit()

    def delete(self):
        try:
            db.session.delete(self.kwargs.get('object'))
            db.session.commit()
        except Exception:
            db.session.rollback()

    def email_or_none(self):
        return self.model.query.filter_by(
            email=self.kwargs.get('email')
        ).one_or_none()

    def username_or_none(self):
        return self.model.query.filter_by(
            username=self.kwargs.get('username')
        ).one_or_none()

    def username_lower_or_none(self):
        """
        case insensitive username lookup
        """
        return self.model.query.filter_by(
            username=self.kwargs['username']
        ).first() or self.model.query.filter_by(
            username=self.kwargs['username'].lower()
        ).first()
