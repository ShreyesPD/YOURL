fes = """
<FeedbackScreen>:
    name:'feedback'
    
    MDToolbar:
        title:"Feedback" 
        pos_hint:{'top':1.0}  
        left_action_items:[["home", lambda x:app.go_back('home')]]
        elevation:10
    
        
    MDTextField:
        id:fd2
        multiline:True
        icon_right:'message'
        hint_text:"Type a message"
        pos_hint:{'center_x': 0.5, 'center_y': 0.60}
        size_hint_x:0.7
        #size_hint_y:0.1
        #width_hint:0.5
        color_mode:'accent'
        line_color_normal:app.theme_cls.accent_color
        required:True 
    
    MDRectangleFlatButton:
        text:"Submit"
        text_color:app.theme_cls.accent_color 
        pos_hint:{'center_x': 0.8, 'center_y': 0.1}
        size_hint:(0.045, 0.05)
        disabled:True if fd2.text=='' else False


"""
