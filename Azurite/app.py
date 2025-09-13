class getapp:
    baseApp = None

    @staticmethod
    def set_base_app(app):
        getapp.baseApp = app

    @staticmethod
    def app():
        return getapp
app = getapp.app()