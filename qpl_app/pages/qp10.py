from qpl_app.pages.page_utils import qp_page_app


def app():

    qp_page_app(10, comment='Influencer Artists',
                songs_played_daria=['לילה כיום יאיר', 'שמתי לי פודרה', 'מתנות', 'ברד'],
                songs_played_roni=['מערכת הדם', 'MS', 'נס', 'tessellate', 'עיניים זרות', 'dissolve me'])
