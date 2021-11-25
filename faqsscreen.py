fs = """
<FaqsScreen>:
    name:'faqs'
    MDToolbar:
        title:"FAQs" 
        pos_hint:{'top':1.0}  
        #size_hint:(1,1)
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
    MDLabel:
        text:'This is FAQs screen'
"""
