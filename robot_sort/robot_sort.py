class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

   
        # while light_is_on == True:
            # keep moving right move right 
            # nothing in hand then swap nothing with item at current position on current postion + 1?
            # comapre item, this function compares 
            # the held item with what in from of the robot, 
            # so the thing to the right or in front because when i starts at zero it first evaluates itself


            # at the start the robot is at 15 but holding nothing
            # make robot pick up item in fron of him by swapping
            # robot pickes up 15
            # then moves right
            # compare 15 to 41 return -1
            # swap 15 for 41
            # move right
            # now holding 41
            # compare 41 to 58 return -1 
            # swaps 41 with 58 and moves right sorted array on right maybe insertion sort?[15, 41]
            # now holding 58
            # compares 58 to 49 return 1 i now want to move 49 over but how? 
            # swap 58 for 49 now holding 49 and in front of 58
            # compare 49 to 58 return -1
            # swap 49 for 58 
            # move right
            # do i have to account for an empty space that's created when the robot is holding something

            # robot starts here
            #  r                        while can mover right keep moving right  
            # [15, 41, 58, 49, 26,]
            #      r
            # [15, 41, 58, 49, 26,]      nothing in hand so move to second item swap with none value now 41 in hand
            #   r                     
            # [15, 26  , 26, 49, none]      is item in hand(41) greater than 15? returns 1 
            #           r
            # [15,   , 58, 49, 26,] is item in hand (41) > 58 return -1 
    def sort(self):
        """
        Sort the robot's list.
        """
       
        self.swap_item()
        while 1 == 1:
            self.set_light_on()

            while self.can_move_right() == True:

                self.move_right()
                if self.compare_item() == -1:
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    self.swap_item()
                    self.move_right()
                if self.compare_item() == 1:
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                if self.compare_item() == 0:
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    self.swap_item()
            self.swap_item()
            if self.can_move_right() == False:
                
            if self.light_is_on() == False:
                return 1

            while self.can_move_left() == True:
                self.move_left()
            
            

            print('done')
            
         

        # if robot cant move right we've reached thenn end of the list
        # if self.can_move_right() == False: 
        #     return
        # # get second item
        # self.move_right()
        # self.swap_item()
        # print(f'holding: {self._item}')
        # print(f'positon: {self._position}')
        # while the light is on keep looping
        # turn light 

        

l = [15, 41, 58, 49, 26,]

# l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

roboposition = SortingRobot(l)
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`


    robot = SortingRobot(l)
   
    robot.sort()
    print(robot._list)
