from bartend import db


class StudioBaseFixture:
    def generate():
        raise NotImplementedError

    def db_add(*data):
        [db.session.add(o) for o in data]
        db.session.commit()

    def db_delete(*data):
        [db.session.delete(o) for o in data]
        db.session.commit()

    def item_to_dict(data):
        data = vars(data)
        # remove the SqlAlchemy Instance object
        data.pop('_sa_instance_state', None)

        return data
