from qpl_app.pages.page_utils import qp_page_app


def app():

    qp_page_app(20, songs_played_daria=["blindsided", "running down the hill", "golden", "stay alive", "electric feel"],
                songs_played_roni=["motion sickness", "roslyn", "the gold", "זה לא אותו דבר", "hey ma",
                                   "I know the end"])
