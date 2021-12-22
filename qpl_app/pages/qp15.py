from qpl_app.pages.page_utils import qp_page_app


def app():

    qp_page_app(15, songs_played_daria=['how deep is your love', 'אנטרקטיקה', 'into you', 'riptide'],
                songs_played_roni=['hideaway', 'trust me', 'take me to church', 'adventure of a lifetime',
                                   'small change girl'],
                comment='Pop Party')
