class mainform_init():
    image_width_tuple = ("원본유지","1024","800","640")
    space_tuple = ("없음","좁게","보통","넓게")
    image_format_tuple = ("PNG","JPG","BMP")
    
    
    def __init__(self):
        pass

    def refresh_screen(self,mainform):
        for item in self.image_width_tuple:
            
            mainform.cbox_Image_width.addItem(item)

        for item in self.space_tuple:
            
            mainform.cbox_Space.addItem(item)

        for item in self.image_format_tuple:
            
            mainform.cbox_Image_format.addItem(item)
