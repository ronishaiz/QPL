from qpl_app.pages.page_utils import qp_page_app


def app():

    qp_page_app(21, songs_played_daria=["love and feeling", "moon song", "reunite", "still feel it all",
                                        "we've been loving in silence", "like we're wired"],
                songs_played_roni=["passionflower", "sober", "as it was", "חולשה לאישה", "hate to be lame",
                                   "כשאור דולק בחלונך", "fever to the form"])
