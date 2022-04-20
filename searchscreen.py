shs = """
<SearchScreen>:
    name:'search'
    FitImage:
        source:'themes\classic_theme\search.png'

    MDToolbar:
        title:"Search Results" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
        #size_hint_x:1
    
    BoxLayout:
        orientation:'vertical'
        MDLabel:
            id:label1
            text:'URL'
            #pos_hint:{'center_x': 0.5, 'center_y': 0.7}
        
        MDLabel:
            id:label2
            text:'STATUS'
            #pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        
        MDRectangleFlatButton:
            text:"Next" 
            pos_hint:{'center_x': 0.87, 'center_y': 0.04}
            #disabled:True if root.f== 0 else False      
            on_press:
                root.manager.current='search2'

        # MDLabel:
        #     id:label4
        #     text:'Domain Info'
        #     #pos_hint:{'center_x': 0.5, 'center_y': 0.2}
        
                                
        # BoxLayout:
        #     orientation:'vertical'
        #     canvas.before:
        #         BorderImage:
        #             source:"themes\classic_theme\search.png"
        #             size:self.size
        #             #size_hint_x:1
        #             #size_hint_y:1
        #             #width:self.parent.width
        #             #height:self.parent.heightS
"""
shs2 = """
<SearchScreen2>:
    name:'search2'
    FitImage:
        source:'themes\classic_theme\search.png'

    MDToolbar:
        title:"Search Results" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
        #size_hint_x:1
    
    MDLabel:
        id:label3
        text:'STATUS'
        #pos_hint:{'center_x': 0.5, 'center_y': 0.3} 
    
    MDRectangleFlatButton:
        text:"Previous" 
        pos_hint:{'center_x': 0.13, 'center_y': 0.04}
        #disabled:True if root.f== 0 else False      
        on_press:
            root.manager.current='search'
    
    MDRectangleFlatButton:
        text:"Next" 
        pos_hint:{'center_x': 0.87, 'center_y': 0.04}
        #disabled:True if root.f== 0 else False      
        on_press:
            root.manager.current='search3'
        
"""

shs3 = """
<SearchScreen3>:
    name:'search3'
    FitImage:
        source:'themes\classic_theme\search.png'

    MDToolbar:
        title:"Search Results" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
        #size_hint_x:1

    MDLabel:
        id:label4
        text:'Domain Info'
        #pos_hint:{'center_x': 0.5, 'center_y': 0.3} 

    MDRectangleFlatButton:
        text:"Previous" 
        pos_hint:{'center_x': 0.13, 'center_y': 0.04}
        #disabled:True if root.f== 0 else False      
        on_press:
            root.manager.current='search2'

    MDRectangleFlatButton:
        text:"Next" 
        pos_hint:{'center_x': 0.87, 'center_y': 0.04}
        #disabled:True if root.f== 0 else False      
        on_press:
            root.manager.current='search4'

"""
shs4 = """
<SearchScreen4>:
    name:'search4'
    FitImage:
        source:'themes\classic_theme\search.png'

    MDToolbar:
        title:"Search Results" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
        #size_hint_x:1

    MDLabel:
        id:label5
        text:'Security Info'
        #pos_hint:{'center_x': 0.5, 'center_y': 0.3} 

    MDRectangleFlatButton:
        text:"Previous" 
        pos_hint:{'center_x': 0.13, 'center_y': 0.04}
        #disabled:True if root.f== 0 else False      
        on_press:
            root.manager.current='search3'

    MDRectangleFlatButton:
        text:"Next" 
        pos_hint:{'center_x': 0.87, 'center_y': 0.04}
        #disabled:True if root.f== 0 else False      
        on_press:
            root.manager.current='search5'

"""

shs5 = """
<SearchScreen5>:
    name:'search5'
    FitImage:
        source:'themes\classic_theme\search.png'

    MDToolbar:
        title:"Search Results" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
        #size_hint_x:1

    MDLabel:
        id:label6
        text:'Domain Info'
        #pos_hint:{'center_x': 0.5, 'center_y': 0.3} 

    MDRectangleFlatButton:
        text:"Previous" 
        pos_hint:{'center_x': 0.13, 'center_y': 0.04}
        #disabled:True if root.f== 0 else False      
        on_press:
            root.manager.current='search4'

    # MDRectangleFlatButton:
    #     text:"Next" 
    #     pos_hint:{'center_x': 0.87, 'center_y': 0.04}
    #     #disabled:True if root.f== 0 else False      
    #     on_press:
    #         root.manager.current='search5'

"""
