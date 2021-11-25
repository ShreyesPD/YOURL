shs = """
<SearchScreen>:
    name:'search'
    
    MDToolbar:
        title:"Search Results" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
    
    MDLabel:
        id:label1
        text:'URL'
        pos_hint:{'center_x': 0.5, 'center_y': 0.7}
       
    MDLabel:
        id:label2
        text:'STATUS'
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}

"""
