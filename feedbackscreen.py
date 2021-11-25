fes = """
<FeedbackScreen>:
    name:'feedback'
    MDToolbar:
        title:"Feedback" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
    MDLabel:
        text:'This is feedback screen'
"""
