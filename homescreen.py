hs = """
<HomeScreen>:    
    name:'home'
    MDTextField:
        id:link
        hint_text:"ENTER URL"
        helper_text:"Or click on the + button to report an url"
        helper_text_mode:"on_focus"
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:250
        color_mode:'accent'
        required:True
    
    MDRectangleFlatButton:
        text:"Search" 
        pos_hint:{'center_x': 0.8, 'center_y': 0.5}
        size_hint:(0.045, 0.05)
        disabled:True if link.text== '' else False
        on_press:
            root.manager.current='search' 
            app.get_url()
        
            
    MDFloatingActionButton:
        icon:"plus"
        pos_hint:{'center_x': 0.9, 'center_y': 0.1}
        on_press:
            app.float()
        
    
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDToolbar:
                    title:"MyApp" 
                    pos_hint:{'top':1.0}  
                    left_action_items:[["menu", lambda x: nav_drawer.set_state('toggle')]]
                    elevation:10
        
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation:'vertical'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Settings'
                            on_press:
                                root.manager.current = 'settings'
                                nav_drawer.set_state('toggle')
                            IconLeftWidget:
                                icon:'tools'
                                on_press:
                                    root.manager.current = 'settings'
                                    nav_drawer.set_state('toggle')
                        OneLineIconListItem:
                            text:'FAQs'
                            on_press:
                                root.manager.current = 'faqs'
                                nav_drawer.set_state('toggle')
                            IconLeftWidget:
                                icon:'puzzle'                   
                                on_press:
                                    root.manager.current = 'faqs'     
                                    nav_drawer.set_state('toggle')
                        OneLineIconListItem:
                            text:'Feedback'
                            on_press:
                                root.manager.current = 'feedback'
                                nav_drawer.set_state('toggle')
                            IconLeftWidget:
                                icon:'pencil'
                                on_press:
                                    root.manager.current = 'feedback'
                                    nav_drawer.set_state('toggle')
                        OneLineIconListItem:
                            text:'Profile'
                            on_press:
                                #root.manager.current = 'profile1'
                                app.profile_status(0)
                                nav_drawer.set_state('toggle')
                            IconLeftWidget:
                                icon:'account'
                                on_press:
                                    #root.manager.current = 'profile1'
                                    app.profile_status(0)
                                    nav_drawer.set_state('toggle')
"""
