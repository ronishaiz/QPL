from qpl_app.pages.page_utils import qp_page_app


def app():

    qp_page_app(5, songs_played_daria=['videotape', 'הזאב והאיילה', 'תחת עורי', 'ברד', 'בגלל הלילה',
                                       'sex on fire', 'עירומה', 'כעץ אני'],
                songs_played_roni=['ברד', 'sailor man', 'בצורת', 'supergirl', '505', 'sex on fire',
                                   'violet hill', 'tessellate'])
