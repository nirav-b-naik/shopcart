def check_offer(mobile):
    offered = mobile.filter(offer=True)
    not_offered = mobile.filter(offer=False)
    return offered, not_offered
