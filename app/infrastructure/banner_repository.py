from app.models import Banner


class BannerRepository:
    def __init__(self, db_session):
        self.repo = db_session

    def get_last_banner_message(self):
        last_banner = self.repo \
            .query(Banner) \
            .order_by(Banner.id.desc()) \
            .first()
        if last_banner:
            return last_banner.banner_message
        else:
            return None

    def save_banner_message(self, message):
        new_banner = Banner(banner_message=message)
        self.repo.add(new_banner)
        try:
            self.repo.commit()
        except:
            return None
        return new_banner.id
