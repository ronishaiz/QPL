from qpl_app.pages.page_utils import qp_page_app


def app():

    qp_page_app(6, songs_played_daria=["הזאב והאיילה", "כעץ אני", "עירומה", "תחת עורי", "the animals",
                                       "בגלל הלילה", "ברד", "videotape"],
                songs_played_roni=["when you were young", "505", "ברד", "sailor man", "בצורת",
                                   "אף פעם", "עיניים זרות", "supergirl"],
                comment='QP Show')
