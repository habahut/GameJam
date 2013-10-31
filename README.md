GameJam
=======

Created by Trevor Haba and Thanh Nguyen, for the Hampshire College game jam in fall 2013.

This is a silly 2d shooter game. Dinosaurs randomly spawn and try to attack you. You can shoot them 
with 3 weapons, a bow and arrow, a machine gun, and a rocket launcher. 

You can access these weapons by pressing the 1, 2 or 3 keys. WASD moves your character, and press Q to dash towards
your cursor. Clicking the mouse shoots whatever weapon you have equipped.

This was created in under 24 hours, so the code is quite sloppy in places. We used python and Pygame.

I created what I think is a fairly clever weapon swap system. The weapons use a Factory design pattern
to return the projectile, allowing the game to easily switch out which weapon the player has equipped.

I tried to make procedurally generated gore, which sort of works. It works best when shooting down and to the right.
Then you can see the impact your weapon would have in the blood streaks / spatter. Given a bit more time we could have
worked out more of the kinks, but I am pleased with what we could come up with in 24 hours.
