ps2 = """
<ProfileScreen2>:
    name:'profile2'
    FitImage:
        source:"themes\classic_theme\profile.png"
    MDToolbar:
        title:"Profile" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
    
    MDCard:
        focus_behavior:True
        size_hint:.7,.5
        pos_hint:{'center_x': 0.5, 'center_y': 0.45}
        elavation:25
        MDFloatLayout:
            MDLabel:
                id:username
                text:'UserName'
                color:app.theme_cls.accent_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.80}
            
            MDLabel:
                id:emailid
                text:'EmailId'
                color:app.theme_cls.accent_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.50}
            
            MDRectangleFlatButton:
                text:"Log Out" 
                text_color:app.theme_cls.accent_color
                pos_hint:{'center_x': 0.8, 'center_y': 0.30}
                #size_hint:(0.035, 0.05)
                on_press:
                    root.manager.current='profile1'
                    app.profile_status(2) 
    
                            
"""
