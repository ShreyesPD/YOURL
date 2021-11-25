"""
<SettingsScreen>:
    name:'settings'
    MDBoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:"Settings" 
            pos_hint:{'top':1.0}  
            left_action_items:[["home", lambda x:app.go_back('home')]]
            elevation:10
        
        ScrollView:
            MDList:
               
                                     
"""

ss = """
<SettingsScreen>:
    name:'settings'
    MDBoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:"Settings" 
            pos_hint:{'top':1.0}  
            left_action_items:[["home", lambda x:app.go_back('home')]]
            elevation:10
        
        ScrollView:
            MDList:
                OneLineListItem:
                    text:'Theme'
                    on_press:
                        app.show_themepicker()
                        root.f=1
        
        MDRectangleFlatButton:
            text:"Save Changes" 
            #pos_hint:{'center_x': 0.8, 'center_y': 0.5}
            #disabled:True if root.f== 0 else False      
            on_press:
                app.store_theme(root.f)
                root.f=0             
"""

"""
 OneLineListItem:
                    Spinner:
                        id:spinner_id1
                        text:"Theme"
                        values:['Light','Dark']
                
                OneLineListItem:
                    Spinner:
                        id:spinner_id2
                        text:"Color"
                        values:['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']

                OneLineListItem:
                    Spinner:
                        id:spinner_id3
                        text:"Accent"
                        values:['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        
"""
