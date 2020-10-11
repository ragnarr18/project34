class Collition_detection:
    def __init__(self):
        self.x_translations = None
        self.z_translations = None
        self.temp_char_pos = None
        self.cs = 0.2

    def x_collition_detection(self, x_translations, z_translations, temp_char_pos):

        self.x_translations = x_translations
        self.z_translations = z_translations
        self.temp_char_pos = temp_char_pos
        self.num_of_translations = len(self.x_translations)
        self.x_collition = False
        self.z_collition = False


        if self.temp_char_pos.x - self.cs < 0:
            return True
            
        if self.temp_char_pos.x + self.cs > 10:
            return True
        
        #### Map collitions
        for i in range(self.num_of_translations):
            # The 4 edges of a map box
            x1 = self.x_translations[i] - 0.5
            x2 = self.x_translations[i] + 0.5
            z1 = self.z_translations[i] - 0.5
            z2 = self.z_translations[i] + 0.5

            if self.temp_char_pos.x + self.cs > x1 and self.temp_char_pos.x + self.cs < x1 + 0.1 and self.temp_char_pos.z + self.cs > z1 and self.temp_char_pos.z - self.cs < z2:
                return True
            if self.temp_char_pos.x - self.cs < x2 and self.temp_char_pos.x - self.cs > x2 - 0.1 and self.temp_char_pos.z + self.cs > z1 and self.temp_char_pos.z - self.cs < z2:
                return True

        
    def z_collition_detection(self, x_translations, z_translations, temp_char_pos):

        self.x_translations = x_translations
        self.z_translations = z_translations
        self.temp_char_pos = temp_char_pos
        self.num_of_translations = len(self.x_translations)
        self.x_collition = False
        self.z_collition = False
        

        if self.temp_char_pos.z - self.cs < 0:
            return True
        if self.temp_char_pos.z + self.cs > 10:
            return True

        for i in range(self.num_of_translations):
            # The 4 edges of a map box
            x1 = self.x_translations[i] - 0.5
            x2 = self.x_translations[i] + 0.5
            z1 = self.z_translations[i] - 0.5
            z2 = self.z_translations[i] + 0.5

            if self.temp_char_pos.z + self.cs > z1 and self.temp_char_pos.z + self.cs < z1 + 0.1 and self.temp_char_pos.x + self.cs > x1 and self.temp_char_pos.x - self.cs < x2:
                return True
            if self.temp_char_pos.x - self.cs < z2 and self.temp_char_pos.z - self.cs > z2 - 0.1 and self.temp_char_pos.x + self.cs > x1 and self.temp_char_pos.x - self.cs < x2:
                return True